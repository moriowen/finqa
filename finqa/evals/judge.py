"""E2 judge and E3 calibration (A22). Runs against a vLLM server that serves openai/gpt-oss-120b.

Label of one output:
  status NOT_FOUND / AMBIGUOUS           -> refusal (no judge call)
  gold is a number and the answer text contains it at the gold precision -> correct (code, no judge call)
  otherwise                              -> gpt-oss-120b decides correct / incorrect / refusal
The same composite judge grades our answers, the bare answers, and the paper's answers (E3).

  python -m finqa.evals.judge run --run NAME          # grade runs/NAME/final.jsonl
  python -m finqa.evals.judge paper                   # grade the paper's 2,400 human-labeled answers
"""
from __future__ import annotations
import argparse
import asyncio
import glob
import json
import os
import re
import sys

from .. import llm, paths
from ..checks import numbers_in_text
from ..cli import read_jsonl, run_tasks
from .gold import gold

JUDGE_SYSTEM = """You grade an answer to a question about a company's SEC filing, against the gold answer written by a financial analyst.

Labels:
- "correct": the answer gives the same key fact, number or conclusion as the gold answer. Numbers count as the same if they agree at the precision of the gold answer, in any equivalent unit (1,577 million = 1.577 billion; 0.25 = 25%). For yes/no or judgment questions, the conclusion must agree with the gold answer; a different but reasonable explanation is acceptable if it does not contradict the gold answer. Extra details are fine if they are not wrong.
- "incorrect": the answer gives a different number, a different conclusion, the wrong period or company, or a hedge that never commits to the gold answer.
- "refusal": the answer declines, or says that the information is not available, and gives no answer.

Return only JSON: {"label": "correct" | "incorrect" | "refusal", "reason": "<one sentence>"}"""

REFUSAL_SYSTEM = """Classify a response to a question about a company's SEC filing. "refusal" if the response declines, or says that the information is not available or not in the document, without giving an answer. "answer" if it gives an answer (any number, fact or conclusion), even if hedged. Return only JSON: {"label": "refusal" | "answer", "reason": "<one sentence>"}"""


def gold_number(ans) -> tuple[float, int] | None:
    """A gold answer that is only a number (with $, %, commas, units) -> (value, decimals)."""
    s = str(ans).strip()
    m = re.fullmatch(r"\$?\s?(-?[\d,]*\.?\d+)\s?(%|percent|million|billion|thousand|times|x)?\.?", s, re.I)
    if not m:
        return None
    core = m.group(1).replace(",", "")
    if "." in core:  # trailing zeros carry no precision: "$8.70" means 8.7, "$303.00" means 303
        core = core.rstrip("0").rstrip(".")
    return abs(float(core)), (len(core.split(".")[1]) if "." in core else 0)


def number_match(gold_ans, text: str) -> bool:
    g = gold_number(gold_ans)
    if g is None or not text:
        return False
    gv, dec = g
    if gv == 0:
        return False  # a zero matches too many things by accident; the LLM judge decides
    for v, _, _ in numbers_in_text(text):
        for s in (1, 1e-3, 1e3, 1e-6, 1e6, 100, 0.01):
            if round(abs(v) * s, dec) == round(gv, dec):
                return True
    return False


async def grade(cl, key: str, question: str, gold_ans: str, justification: str, answer_text: str | None,
                status: str | None) -> dict:
    base = {"key": key}
    if status in ("NOT_FOUND", "AMBIGUOUS") or answer_text is None:
        return {**base, "label": "refusal", "by": "status"}
    if number_match(gold_ans, answer_text):
        return {**base, "label": "correct", "by": "code"}
    r = await llm.chat(cl, [{"role": "system", "content": JUDGE_SYSTEM},
                            {"role": "user", "content": f"QUESTION: {question}\n\nGOLD ANSWER: {gold_ans}\n\n"
                                                        f"GOLD JUSTIFICATION: {justification}\n\nANSWER TO GRADE: {answer_text}"}],
                       max_tokens=3000, reasoning_effort="medium")
    try:
        j = llm.parse_json(r["text"])
        lab = j.get("label")
    except Exception:  # noqa: BLE001
        j, lab = {}, None
    if lab not in ("correct", "incorrect", "refusal"):
        lab = "incorrect"  # conservative: an ungradable output never counts as correct
    return {**base, "label": lab, "by": "llm", "reason": j.get("reason", ""), "raw": r["text"][-400:]}


async def classify_refusal(cl, key: str, question: str, answer_text: str) -> dict:
    r = await llm.chat(cl, [{"role": "system", "content": REFUSAL_SYSTEM},
                            {"role": "user", "content": f"QUESTION: {question}\n\nRESPONSE: {answer_text}"}],
                       max_tokens=2000, reasoning_effort="low")
    try:
        lab = llm.parse_json(r["text"]).get("label")
    except Exception:  # noqa: BLE001
        lab = "answer"
    return {"key": key, "label": "refusal" if lab == "refusal" else "answer", "by": "llm"}


def cmd_run(a):
    run = paths.RUNS / a.run
    src = run / (f"final{a.src}.jsonl" if a.src is not None else ("final_think.jsonl" if a.thinking else "final.jsonl"))
    out = run / (f"judge{a.out}.jsonl" if a.out is not None else ("judge_think.jsonl" if a.thinking else "judge.jsonl"))
    rows = read_jsonl(src)
    done = {r["key"] for r in read_jsonl(out)}
    g = gold()
    cl = llm.client()
    tasks = []
    for r in rows:
        if r["qid"] in done:
            continue
        if "__" in r["qid"]:  # unanswerable: correct behavior is to refuse
            if r["status"] in ("NOT_FOUND", "AMBIGUOUS"):
                tasks.append(_const(r["qid"], "refusal"))
            elif r["status"] in ("BARE", "ANSWER"):  # same rule for both: an answer that only says "not here" is a refusal
                tasks.append(classify_refusal(cl, r["qid"], r["question"], r.get("answer") or ""))
            else:
                tasks.append(_const(r["qid"], "answer"))
            continue
        gd = g[r["qid"]]
        tasks.append(grade(cl, r["qid"], gd["question"], gd["answer"], gd["justification"], r.get("answer"), r["status"]))
    print(f"judge {a.run}: {len(tasks)} to grade", file=sys.stderr)
    asyncio.run(run_tasks(tasks, out, a.limit))
    # A18: also grade every pre-verifier candidate, to measure verifier false rejects and false accepts
    cout = run / f"judge_cands{a.out or ''}.jsonl"
    cdone = {r["key"] for r in read_jsonl(cout)}
    cl = llm.client()  # new client: the first one is bound to the event loop that asyncio.run closed
    ctasks = []
    for r in read_jsonl(run / "pass1.jsonl"):
        if r.get("status") != "CANDIDATE" or "__" in r["qid"] or r["key"] in cdone:
            continue
        gd = g[r["qid"]]
        ctasks.append(grade(cl, r["key"], gd["question"], gd["answer"], gd["justification"], r.get("answer"), None))
    if ctasks:
        print(f"judge {a.run}: {len(ctasks)} pre-verifier candidates to grade", file=sys.stderr)
        asyncio.run(run_tasks(ctasks, cout, a.limit))


async def _const(key, label):
    return {"key": key, "label": label, "by": "status"}


def cmd_paper(a):
    out = paths.RUNS / f"judge_paper{a.out or ''}.jsonl"
    done = {r["key"] for r in read_jsonl(out)}
    g = gold()
    cl = llm.client()
    tasks = []
    for f in sorted(glob.glob(str(paths.PAPER_RESULTS / "*.jsonl"))):
        cfg = os.path.basename(f)[:-6]
        for r in read_jsonl(f):
            key = f"{cfg}|{r['financebench_id']}"
            if key in done:
                continue
            gd = g[r["financebench_id"]]
            tasks.append(grade(cl, key, gd["question"], gd["answer"], gd["justification"], r.get("model_answer") or "", None))
    print(f"judge paper: {len(tasks)} to grade", file=sys.stderr)
    asyncio.run(run_tasks(tasks, out, a.limit))


def cmd_regrade(a):
    """Re-apply the code check to existing judge files after a change to number_match. It only turns a label
    into "correct" where code now finds the gold number; labels that were already correct stay correct."""
    g = gold()
    files_ = sorted(glob.glob(str(paths.RUNS / "*" / "judge*.jsonl")))
    for f in files_:
        run = os.path.basename(os.path.dirname(f))
        sfx = os.path.basename(f)[len("judge"):-len(".jsonl")]
        cands = sfx.startswith("_cands")
        src = {}
        if cands:
            src = {r["key"]: r.get("answer") for r in read_jsonl(paths.RUNS / run / "pass1.jsonl")}
        else:
            fin = paths.RUNS / run / (f"final{sfx.replace('_oss20b', '')}.jsonl")
            if not fin.exists():
                continue
            src = {r["qid"]: r.get("answer") for r in read_jsonl(fin)}
        rows, n = read_jsonl(f), 0
        for r in rows:
            qid = r["key"].split("|")[0]
            if "__" in qid or qid not in g or r["label"] == "correct":
                continue
            if number_match(g[qid]["answer"], src.get(r["key"]) or ""):
                r.update(label="correct", by="code", regraded=True)
                n += 1
        if n:
            with open(f, "w") as fh:
                fh.writelines(json.dumps(r) + "\n" for r in rows)
            print(f"{run}/{os.path.basename(f)}: {n} relabeled correct")
    ans = {}
    for fp in glob.glob(str(paths.PAPER_RESULTS / "*.jsonl")):
        cfg = os.path.basename(fp)[:-6]
        for r in read_jsonl(fp):
            ans[f"{cfg}|{r['financebench_id']}"] = (r["financebench_id"], r.get("model_answer") or "")
    for out in (paths.RUNS / "judge_paper_oss20b.jsonl", paths.RUNS / "judge_paper.jsonl"):
        rows, n = read_jsonl(out), 0
        for r in rows:
            if r["label"] != "correct" and r["key"] in ans and number_match(g[ans[r["key"]][0]]["answer"], ans[r["key"]][1]):
                r.update(label="correct", by="code", regraded=True)
                n += 1
        if n:
            with open(out, "w") as fh:
                fh.writelines(json.dumps(r) + "\n" for r in rows)
        print(f"{out.name}: {n} relabeled correct")


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(required=True)
    s = sub.add_parser("regrade")
    s.set_defaults(func=cmd_regrade)
    s = sub.add_parser("run")
    s.add_argument("--run", required=True)
    s.add_argument("--thinking", action="store_true")
    s.add_argument("--src", default=None, help="final file suffix to grade, e.g. _phi4")
    s.add_argument("--out", default=None, help="judge file suffix, e.g. _phi4_oss20b")
    s.add_argument("--limit", type=int, default=32)
    s.set_defaults(func=cmd_run)
    s = sub.add_parser("paper")
    s.add_argument("--out", default=None)
    s.add_argument("--limit", type=int, default=48)
    s.set_defaults(func=cmd_paper)
    a = ap.parse_args(argv)
    a.func(a)


if __name__ == "__main__":
    main()
