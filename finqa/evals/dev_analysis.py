"""Dev-split decisions (A12, A16, A18, A19, A15). Prints the numbers that choose the final configuration.

  python -m finqa.evals.dev_analysis
"""
from __future__ import annotations
import json

from .. import paths
from ..cli import read_jsonl
from .report import run_metrics
from .retrieval import recall


def verifier_errors(run: str, thinking: bool = False) -> dict:
    """A18: verifier verdict vs the judge label of the pre-verifier candidate answer."""
    lab = {r["key"]: r["label"] for r in read_jsonl(paths.RUNS / run / "judge_cands.jsonl")}
    ver = {r["key"]: r["pass"] for r in read_jsonl(paths.RUNS / run / ("pass2_think.jsonl" if thinking else "pass2.jsonl"))}
    keys = [k for k in ver if k in lab]
    tp = sum(ver[k] and lab[k] == "correct" for k in keys)
    fp = sum(ver[k] and lab[k] != "correct" for k in keys)
    fn = sum((not ver[k]) and lab[k] == "correct" for k in keys)
    tn = sum((not ver[k]) and lab[k] != "correct" for k in keys)
    return {"run": run, "thinking": thinking, "n": len(keys), "accept_correct": tp, "accept_wrong": fp,
            "reject_correct": fn, "reject_wrong": tn,
            "false_accept_rate": fp / (fp + tn) if fp + tn else None,
            "false_reject_rate": fn / (fn + tp) if fn + tp else None}


def main():
    out = {"retrieval": [recall(a) for a in ("r0", "r1", "r2", "r3")]}
    runs = ["dev-27b-full-r0", "dev-27b-bare-r0", "dev-27b-oracle", "dev-27b-oracle-img", "dev-9b-full-r0",
            "dev-9b-bare-r0", "dev-2b-full-r0", "dev-2b-full-r0-gloss", "dev-2b-bare-r0"]
    out["runs"] = {}
    for r in runs:
        try:
            out["runs"][r] = run_metrics(r)
        except Exception as e:  # noqa: BLE001
            out["runs"][r] = {"error": repr(e)}
    out["verifier"] = []
    for r in ("dev-27b-full-r0", "dev-9b-full-r0", "dev-2b-full-r0"):
        for t in (False, True):
            try:
                out["verifier"].append(verifier_errors(r, t))
            except Exception as e:  # noqa: BLE001
                out["verifier"].append({"run": r, "thinking": t, "error": repr(e)})
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
