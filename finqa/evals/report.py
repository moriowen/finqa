"""Metrics for runs (E1, E4, E6, E8, E9) and the judge calibration (E3).

  python -m finqa.evals.report run NAME [NAME ...]     # metrics table
  python -m finqa.evals.report paper                   # E3: judge vs the paper's human labels
"""
from __future__ import annotations
import argparse
import glob
import json
import os
import random

from .. import paths
from ..cli import read_jsonl
from .gold import gold

LABELS = ("correct", "incorrect", "refusal")
# Final setup (A23): Gemma 4 12B verifier files end in _gemma4, gpt-oss-20b judge files in _oss20b.
VER = os.environ.get("FINQA_VERIFIER_TAG", "_gemma4")
JUD = os.environ.get("FINQA_JUDGE_TAG", "_oss20b")


def files(run: str) -> tuple[str, str]:
    """(final file, judge file) of a run. Bare runs have no verifier, so they use final.jsonl."""
    d = paths.RUNS / run
    if (d / f"final{VER}.jsonl").exists():
        return f"final{VER}.jsonl", f"judge{VER}{JUD}.jsonl"
    return "final.jsonl", f"judge{JUD}.jsonl"


def labels(run: str, thinking: bool = False) -> dict[str, str]:
    j = read_jsonl(paths.RUNS / run / ("judge_think.jsonl" if thinking else files(run)[1]))
    return {r["key"]: r["label"] for r in j}


def test_ids() -> set[str]:
    return set(json.loads(paths.SPLIT.read_text())["test"])


def rates(labs: list[str]) -> dict:
    n = len(labs)
    c, i, r = (sum(x == k for x in labs) for k in LABELS)
    return {"n": n, "correct": c, "incorrect": i, "refusal": r,
            "wrong_rate": i / n if n else 0, "coverage": (c + i) / n if n else 0,
            "selective_acc": c / (c + i) if c + i else 0, "accuracy": c / n if n else 0}


def bootstrap(labs: list[str], key: str, b: int = 2000, seed: int = 0) -> tuple[float, float]:
    rng = random.Random(seed)
    vals = []
    for _ in range(b):
        s = [labs[rng.randrange(len(labs))] for _ in labs]
        vals.append(rates(s)[key])
    vals.sort()
    return vals[int(0.025 * b)], vals[int(0.975 * b)]


def provenance(run: str) -> dict:
    """E4: for ANSWER rows on real questions, is a cited page a gold page of the gold filing?"""
    g = gold()
    hit = doc_ok = n = 0
    for r in read_jsonl(paths.RUNS / run / files(run)[0]):
        if r["status"] != "ANSWER" or "__" in r["qid"]:
            continue
        gd = g[r["qid"]]
        n += 1
        prov = r.get("provenance") or []
        doc_ok += any(p["doc"] == gd["doc_name"] for p in prov)
        hit += any(p["doc"] == gd["doc_name"] and p["pdf_page"] - 1 in gd["pages"] for p in prov)
    return {"answered": n, "doc_match": doc_ok, "page_hit": hit, "page_hit_rate": hit / n if n else 0}


def cost(run: str) -> dict:
    p1 = read_jsonl(paths.RUNS / run / "pass1.jsonl")
    calls = sum(len(r.get("attempts", [])) for r in p1)
    secs = sum(a.get("seconds", 0) for r in p1 for a in r.get("attempts", []))
    toks = sum((a.get("usage") or {}).get("total_tokens", 0) for r in p1 for a in r.get("attempts", []))
    nq = len({r["qid"] for r in p1}) or 1
    return {"calls_per_q": calls / nq, "llm_seconds_per_q": secs / nq, "tokens_per_q": toks / nq}


def run_metrics(run: str, thinking: bool = False) -> dict:
    labs = labels(run, thinking)
    g = gold()
    real = {k: v for k, v in labs.items() if "__" not in k}
    unans = {k: v for k, v in labs.items() if "__" in k}
    out = {"run": run, "real": rates(list(real.values())) if real else None}
    if real:
        out["real"]["wrong_ci"] = bootstrap(list(real.values()), "wrong_rate")
        out["real"]["acc_ci"] = bootstrap(list(real.values()), "accuracy")
        by = {}
        for k, v in real.items():
            by.setdefault(g[k]["question_type"], []).append(v)
        out["by_type"] = {t: rates(v) for t, v in sorted(by.items())}
        out["provenance"] = provenance(run)
        t = [v for k, v in real.items() if k in test_ids()]
        if t:
            out["test"] = rates(t)
            out["test"]["wrong_ci"] = bootstrap(t, "wrong_rate")
    if unans:
        fa = [v for v in unans.values()]
        out["unanswerable"] = {"n": len(fa), "false_answer": sum(v == "answer" for v in fa),
                               "false_answer_rate": sum(v == "answer" for v in fa) / len(fa)}
        for t in ("wrongdoc", "shiftyear"):
            sub = [v for k, v in unans.items() if k.endswith(t)]
            if sub:
                out["unanswerable"][t] = sum(v == "answer" for v in sub) / len(sub)
    out["cost"] = cost(run)
    return out


def mcnemar(run_a: str, run_b: str) -> dict:
    """Paired test on correct/not correct, same questions (E8)."""
    a, b = labels(run_a), labels(run_b)
    keys = [k for k in a if k in b and "__" not in k]
    n01 = sum(a[k] == "correct" and b[k] != "correct" for k in keys)
    n10 = sum(a[k] != "correct" and b[k] == "correct" for k in keys)
    from math import comb
    n = n01 + n10
    p = min(1.0, 2 * sum(comb(n, i) for i in range(0, min(n01, n10) + 1)) / 2 ** n) if n else 1.0
    return {"a": run_a, "b": run_b, "a_only_correct": n01, "b_only_correct": n10, "p_exact": p}


def verifier_check(run: str) -> dict | None:
    """Verifier decision vs judge label on the pre-verifier candidates (A18)."""
    d = paths.RUNS / run
    ver = {r["key"]: r["pass"] for r in read_jsonl(d / f"pass2{VER}.jsonl")}
    lab = {r["key"]: r["label"] for r in read_jsonl(d / f"judge_cands{VER}{JUD}.jsonl")}
    ks = [k for k in ver if k in lab]
    if not ks:
        return None
    q = lambda a, ok: sum(ver[k] == a and (lab[k] == "correct") == ok for k in ks)  # noqa: E731
    return {"n": len(ks), "accept_correct": q(True, True), "accept_wrong": q(True, False),
            "reject_correct": q(False, True), "reject_wrong": q(False, False)}


def paper_calibration(file: str | None = None) -> dict:
    """E3: our judge on the paper's 2,400 answers vs their human labels."""
    human = {}
    for f in sorted(glob.glob(str(paths.PAPER_RESULTS / "*.jsonl"))):
        cfg = os.path.basename(f)[:-6]
        for r in read_jsonl(f):
            human[f"{cfg}|{r['financebench_id']}"] = {"Correct Answer": "correct", "Incorrect Answer": "incorrect",
                                                      "Refusal": "refusal"}[r["label"]]
    ours = {r["key"]: r["label"] for r in read_jsonl(paths.RUNS / (file or f"judge_paper{JUD}.jsonl"))}
    keys = [k for k in ours if k in human]
    conf = {h: {o: 0 for o in LABELS} for h in LABELS}
    for k in keys:
        conf[human[k]][ours[k]] += 1
    agree = sum(conf[x][x] for x in LABELS)
    n_inc = sum(conf["incorrect"].values())
    return {"n": len(keys), "agreement": agree / len(keys) if keys else 0, "confusion_human_rows": conf,
            "false_correct_rate": conf["incorrect"]["correct"] / n_inc if n_inc else 0,
            "false_incorrect_rate": conf["correct"]["incorrect"] / max(1, sum(conf["correct"].values()))}


def paper_baselines() -> list[dict]:
    out = []
    for f in sorted(glob.glob(str(paths.PAPER_RESULTS / "*.jsonl"))):
        labs = [{"Correct Answer": "correct", "Incorrect Answer": "incorrect", "Refusal": "refusal"}[r["label"]]
                for r in read_jsonl(f)]
        out.append({"config": os.path.basename(f)[:-6], **rates(labs)})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("run")
    s.add_argument("runs", nargs="+")
    s.add_argument("--thinking", action="store_true")
    sub.add_parser("paper")
    sub.add_parser("baselines")
    a = ap.parse_args(argv)
    if a.cmd == "run":
        for r in a.runs:
            print(json.dumps(run_metrics(r, a.thinking), default=str))
    elif a.cmd == "paper":
        print(json.dumps(paper_calibration(), indent=1))
    else:
        for r in paper_baselines():
            print(json.dumps(r))


if __name__ == "__main__":
    main()
