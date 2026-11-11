"""Command-line driver. Every pass appends JSONL and skips finished keys, so a killed job can resume (A14, A21).

  python -m finqa.cli pass0 --what plan|route --set all
  python -m finqa.cli pass1 --run NAME --set dev --mode full|bare|oracle --arm r0 [--path B] [--unans] [--glossary] [--images]
  python -m finqa.cli pass2 --run NAME [--thinking]
  python -m finqa.cli embed --set all
"""
from __future__ import annotations
import argparse
import asyncio
import json
import os
import sys
import time

from . import answer, corpus, llm, parse, paths, pass0, retrieve, verify

P0 = paths.RUNS / "pass0"


def read_jsonl(p) -> list[dict]:
    if not os.path.exists(p):
        return []
    out = []
    for line in open(p):
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass  # a line cut by a killed job
    return out


def question_set(name: str, unans: bool = False, path_b: bool = False) -> list[corpus.Question]:
    sp = corpus.split()
    ids = None if name == "all" else set(sp[name])
    if unans:
        from .evals.unanswerable import build  # eval data: built from question text and metadata only
        return build(ids)
    return [q for q in corpus.questions(path_b=path_b) if ids is None or q.id in ids]


async def run_tasks(tasks, out_path, limit):
    done = 0
    t0 = time.time()
    sem = asyncio.Semaphore(limit)

    async def one(t):
        async with sem:
            try:
                return await t
            except Exception as e:  # noqa: BLE001 - one failed request must not stop the batch
                return {"error": repr(e)}
    with open(out_path, "a") as f:
        for fut in asyncio.as_completed([one(t) for t in tasks]):
            rec = await fut
            if "error" in rec and "key" not in rec:
                print("task error:", rec["error"], file=sys.stderr)
                continue
            f.write(answer.dumps(rec) + "\n")
            f.flush()
            done += 1
            if done % 10 == 0:
                print(f"  {done}/{len(tasks)} done, {time.time() - t0:.0f} s", file=sys.stderr)
    print(f"finished {done}/{len(tasks)} in {time.time() - t0:.0f} s", file=sys.stderr)


def cmd_pass0(a):
    P0.mkdir(parents=True, exist_ok=True)
    out = P0 / f"{a.what}.jsonl"
    qs = question_set(a.set, path_b=True) + (question_set(a.set, unans=True) if a.what == "plan" else [])
    done = {r["qid"] for r in read_jsonl(out)}
    cl = llm.client()
    fn = pass0.plan if a.what == "plan" else pass0.route
    todo = [q for q in qs if q.id not in done]
    print(f"pass0 {a.what}: {len(todo)} to do", file=sys.stderr)

    async def go(q):
        r = await fn(cl, q)
        r["key"] = q.id
        return r
    asyncio.run(run_tasks([go(q) for q in todo], out, a.limit))


def cmd_pass1(a):
    run = paths.RUNS / a.run
    run.mkdir(parents=True, exist_ok=True)
    cfg = {k: v for k, v in vars(a).items() if k != "func"}
    cfg["model"] = llm.MODEL
    (run / "config.json").write_text(json.dumps(cfg, indent=1))
    out = run / "pass1.jsonl"
    done = {r["key"] for r in read_jsonl(out) if "key" in r}
    qs = question_set(a.set, unans=a.unans, path_b=(a.path == "B"))
    plans = {r["qid"]: r["plan"] for r in read_jsonl(P0 / "plan.jsonl")}
    routes = {r["qid"]: r["candidates"] for r in read_jsonl(P0 / "route.jsonl")}
    oracle = {}
    if a.mode == "oracle":
        from .evals.gold import oracle_pages  # oracle setting only: gold pages are the input by definition
        oracle = oracle_pages()
    items = []
    for q in qs:
        docs = [q.doc_name] if q.doc_name else routes.get(q.id)
        if docs is None:
            sys.exit(f"no route for {q.id}: run pass0 --what route first")
        for d in docs:
            items.append((q, d))
    cl = llm.client()

    async def go(q, d):
        if a.mode == "oracle":
            pages, ranked, pack = oracle[q.id], [], []
        else:
            sel = retrieve.select_pages(d, q.question, arm=a.arm, plan=plans.get(q.id), budget=a.budget)
            pages, ranked, pack = sel["pages"], sel["ranked"], sel["pack"]
        if a.mode == "bare":
            rec = await answer.run_bare(cl, q, d, pages, ranked, pack)
        else:
            rec = await answer.run_full(cl, q, d, pages, ranked, glossary=a.glossary, use_images=a.images, pack=pack)
        rec.update(key=f"{q.id}|{d}", question=q.question)
        return rec
    todo = [(q, d) for q, d in items if f"{q.id}|{d}" not in done]
    print(f"pass1 {a.run}: {len(todo)} of {len(items)} to do (model {llm.MODEL})", file=sys.stderr)
    asyncio.run(run_tasks([go(q, d) for q, d in todo], out, a.limit))


def cmd_pass2(a):
    run = paths.RUNS / a.run
    p1 = {r["key"]: r for r in read_jsonl(run / "pass1.jsonl") if "key" in r}
    suffix = a.suffix or ("_think" if a.thinking else "")
    vout = run / f"pass2{suffix}.jsonl"
    done = {r["key"] for r in read_jsonl(vout)}
    cl = llm.client()
    todo = [r for r in p1.values() if r["status"] == "CANDIDATE" and r["key"] not in done]
    print(f"pass2 {a.run}: verify {len(todo)} candidates (model {llm.MODEL}, thinking={a.thinking})", file=sys.stderr)
    asyncio.run(run_tasks([verify.verify(cl, r, r["question"], thinking=a.thinking, free_json=a.free_json)
                           for r in todo], vout, a.limit))
    finalize(a.run, thinking=a.thinking, suffix=suffix)


def finalize(run_name: str, thinking: bool = False, suffix: str | None = None) -> list[dict]:
    """Apply the verifier verdicts, then G8 per question. Writes final.jsonl (or final_think.jsonl)."""
    run = paths.RUNS / run_name
    p1 = [r for r in read_jsonl(run / "pass1.jsonl") if "key" in r]
    suffix = suffix if suffix is not None else ("_think" if thinking else "")
    ver = {r["key"]: r for r in read_jsonl(run / f"pass2{suffix}.jsonl")}
    cfg0 = json.loads((run / "config.json").read_text())
    routes = {r["qid"]: r["candidates"] for r in read_jsonl(P0 / "route.jsonl")}
    by_q: dict[str, list[dict]] = {}
    for r in p1:
        r = dict(r)
        r["answer_model"] = cfg0.get("model")
        if r["status"] == "CANDIDATE":
            v = ver.get(r["key"])
            if v is not None:
                r["verifier_model"] = v.get("model")
            if v is None:
                r["status"], r["reason"] = "NOT_FOUND", "not verified (verifier pass missing)"
            elif v["pass"]:
                r["status"] = "ANSWER"
            else:
                vd = v.get("verdict") or {}
                flags = [k for k in ("period_ok", "unit_ok", "value_in_correct_column") if vd.get(k) is False]
                r["status"] = "NOT_FOUND"
                r["reason"] = (f"verifier: answer_supported={vd.get('answer_supported')}"
                               + (f", failed {', '.join(flags)}" if flags else "") + f". {vd.get('problem', '')}").strip()
        by_q.setdefault(r["qid"], []).append(r)
    cfg = json.loads((run / "config.json").read_text())
    rows = []
    for qid, recs in by_q.items():
        order = [recs[0]["doc"]] if cfg.get("path") != "B" else routes.get(qid, [])
        rows.append(verify.combine(qid, recs[0]["question"], recs, order))
    if cfg.get("path") == "B":  # questions with no candidate filing never reached pass 1
        for qid, cands in routes.items():
            if not cands and qid not in by_q and any(q.id == qid for q in question_set(cfg["set"], path_b=True)):
                q = next(q for q in question_set(cfg["set"], path_b=True) if q.id == qid)
                rows.append(verify.combine(qid, q.question, [], []))
    out = run / f"final{suffix}.jsonl"
    with open(out, "w") as f:
        for r in sorted(rows, key=lambda r: r["qid"]):
            f.write(json.dumps(r, default=str) + "\n")
    print(f"final: {len(rows)} rows -> {out}", file=sys.stderr)
    return rows


def cmd_finalize(a):
    finalize(a.run, thinking=a.thinking, suffix=a.suffix)


def cmd_embed(a):
    """A19 R1: embed pages of the needed filings and all query texts. Model served with vLLM as an embedding model."""
    import numpy as np
    from openai import OpenAI
    cl = OpenAI(base_url=llm.BASE_URL, api_key="none", timeout=600)
    retrieve.VEC_DIR.mkdir(parents=True, exist_ok=True)
    qs = question_set(a.set) + question_set(a.set, unans=True)
    docs = sorted({q.doc_name for q in qs})
    for i, d in enumerate(docs):
        p = retrieve.VEC_DIR / f"{d}.npy"
        if p.exists():
            continue
        texts = [(t.strip() or "(empty page)")[:6000] for t in parse.load(d)["plain"]]
        vecs = []
        for j in range(0, len(texts), 64):
            r = cl.embeddings.create(model=llm.MODEL, input=texts[j:j + 64])
            vecs += [e.embedding for e in r.data]
        v = np.asarray(vecs, dtype=np.float32)
        v /= np.linalg.norm(v, axis=1, keepdims=True) + 1e-9
        np.save(p, v)
        print(f"  embedded {i + 1}/{len(docs)} {d} {len(texts)} pages", file=sys.stderr)
    inst = "Instruct: Given a question about a company's SEC filing, retrieve the filing page that answers it\nQuery: "
    texts = sorted({q.question for q in qs})
    out = []
    for j in range(0, len(texts), 64):
        r = cl.embeddings.create(model=llm.MODEL, input=[inst + t for t in texts[j:j + 64]])
        for t, e in zip(texts[j:j + 64], r.data):
            v = np.asarray(e.embedding, dtype=np.float32)
            out.append({"text": t, "vec": (v / (np.linalg.norm(v) + 1e-9)).round(6).tolist()})
    with open(retrieve.VEC_DIR / "queries.jsonl", "w") as f:
        for r in out:
            f.write(json.dumps(r) + "\n")
    print(f"embedded {len(texts)} queries", file=sys.stderr)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="finqa")
    sub = ap.add_subparsers(required=True)
    s = sub.add_parser("pass0")
    s.add_argument("--what", choices=["plan", "route"], required=True)
    s.add_argument("--set", default="all")
    s.add_argument("--limit", type=int, default=32)
    s.set_defaults(func=cmd_pass0)
    s = sub.add_parser("pass1")
    s.add_argument("--run", required=True)
    s.add_argument("--set", default="dev")
    s.add_argument("--mode", choices=["full", "bare", "oracle"], default="full")
    s.add_argument("--arm", choices=["r0", "r1", "r2", "r3"], default="r0")
    s.add_argument("--path", choices=["A", "B"], default="A")
    s.add_argument("--unans", action="store_true")
    s.add_argument("--glossary", action="store_true")
    s.add_argument("--images", action="store_true")
    s.add_argument("--budget", type=int, default=12)
    s.add_argument("--limit", type=int, default=24)
    s.set_defaults(func=cmd_pass1)
    s = sub.add_parser("pass2")
    s.add_argument("--run", required=True)
    s.add_argument("--thinking", action="store_true")
    s.add_argument("--suffix", default=None, help="file suffix for a verifier variant, e.g. _phi4")
    s.add_argument("--free-json", action="store_true", help="reasoning verifier: no enforced schema")
    s.add_argument("--limit", type=int, default=16)
    s.set_defaults(func=cmd_pass2)
    s = sub.add_parser("finalize")
    s.add_argument("--run", required=True)
    s.add_argument("--thinking", action="store_true")
    s.add_argument("--suffix", default=None)
    s.set_defaults(func=cmd_finalize)
    s = sub.add_parser("embed")
    s.add_argument("--set", default="all")
    s.set_defaults(func=cmd_embed)
    a = ap.parse_args(argv)
    a.func(a)


if __name__ == "__main__":
    main()
