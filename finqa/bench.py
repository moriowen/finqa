"""Latency benchmark: the full pipeline (filing given), timed per stage, for one question at a time and for a batch.

Needs two vLLM servers: the answering model (FINQA_BASE_URL, FINQA_MODEL) and the verifier (VERIFIER_URL, VERIFIER_MODEL).
Streaming is on (FINQA_STREAM=1) so each call records time to first token.

  python -m finqa.bench --n 20 --out runs/bench/9b.jsonl
"""
from __future__ import annotations
import argparse
import asyncio
import json
import os
import statistics
import sys
import time

from openai import AsyncOpenAI

from . import answer, corpus, llm, retrieve, verify

ARM = "r1"


async def one(cl, clv, vmodel, q) -> dict:
    t0 = time.perf_counter()
    sel = retrieve.select_pages(q.doc_name, q.question, arm=ARM)
    t_ret = time.perf_counter() - t0
    rec = await answer.run_full(cl, q, q.doc_name, sel["pages"], sel["ranked"], pack=sel["pack"])
    t_p1 = time.perf_counter() - t0
    rec["key"] = f"{q.id}|{q.doc_name}"
    v = None
    if rec["status"] == "CANDIDATE":
        v = await verify.verify(clv, rec, q.question, model=vmodel)
    t_end = time.perf_counter() - t0
    c1 = [a for a in rec["attempts"] if a["call"] == 1]
    c2 = [a for a in rec["attempts"] if a["call"] == 2]
    llm_s = sum(a["seconds"] for a in rec["attempts"])
    return {
        "qid": q.id, "status": ("ANSWER" if v and v["pass"] else "NOT_FOUND") if v else rec["status"],
        "total_s": round(t_end, 2), "retrieval_ms": round(1000 * t_ret, 1),
        "call1_s": round(sum(a["seconds"] for a in c1), 2), "call1_ttft_s": c1[0].get("ttft") if c1 else None,
        "call2_s": round(sum(a["seconds"] for a in c2), 2), "call2_ttft_s": c2[0].get("ttft") if c2 else None,
        "verifier_s": v["seconds"] if v else 0.0, "verifier_ttft_s": v.get("ttft") if v else None,
        "code_checks_ms": round(1000 * (t_p1 - t_ret - llm_s), 1),
        "llm_calls": len(rec["attempts"]) + (1 if v else 0), "retries": max(0, len(c1) - 1) + max(0, len(c2) - 1),
        "call1_prompt_tokens": (c1[0].get("usage") or {}).get("prompt_tokens") if c1 else None,
        "call1_output_tokens": (c1[0].get("usage") or {}).get("completion_tokens") if c1 else None,
    }


def summary(rows: list[dict], label: str, wall: float | None = None) -> dict:
    def pct(k, p):
        xs = sorted(r[k] for r in rows if r.get(k) is not None)
        if not xs:
            return None
        i = min(len(xs) - 1, int(round(p * (len(xs) - 1))))
        return round(xs[i], 2)
    keys = ["total_s", "retrieval_ms", "call1_ttft_s", "call1_s", "code_checks_ms", "call2_s", "verifier_s"]
    out = {"label": label, "n": len(rows), **{f"{k}_p50": pct(k, 0.5) for k in keys}, **{f"{k}_p90": pct(k, 0.9) for k in keys},
           "llm_calls_mean": round(statistics.mean(r["llm_calls"] for r in rows), 2)}
    if wall:
        out.update(wall_s=round(wall, 1), questions_per_hour=round(3600 * len(rows) / wall))
    return out


async def main_async(a):
    qs = [q for q in corpus.questions() if q.id in set(corpus.split()["dev"])][: a.n]
    cl = llm.client()
    clv = AsyncOpenAI(base_url=os.environ["VERIFIER_URL"], api_key="none", timeout=900)
    vmodel = os.environ["VERIFIER_MODEL"]
    await one(cl, clv, vmodel, qs[0])  # warm-up (compile, caches); not counted
    rows = []
    for q in qs:  # single: one request at a time, idle GPU
        r = await one(cl, clv, vmodel, q)
        r["mode"] = "single"
        rows.append(r)
        print(f"single {q.id} {r['total_s']} s", file=sys.stderr)
    t0 = time.perf_counter()  # batch: all questions at once
    batch = await asyncio.gather(*(one(cl, clv, vmodel, q) for q in qs))
    wall = time.perf_counter() - t0
    for r in batch:
        r["mode"] = "batch"
    with open(a.out, "w") as f:
        for r in rows + list(batch):
            f.write(json.dumps(r) + "\n")
        f.write(json.dumps({"summary": [summary(rows, f"{llm.MODEL} single"), summary(list(batch), f"{llm.MODEL} batch of {len(qs)}", wall)]}) + "\n")
    print(json.dumps(summary(rows, "single")), file=sys.stderr)
    print(json.dumps(summary(list(batch), "batch", wall)), file=sys.stderr)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    asyncio.run(main_async(a))


if __name__ == "__main__":
    main()
