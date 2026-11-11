"""E5: page recall of the pages sent to the LLM, against the gold evidence pages."""
from __future__ import annotations
import json
import sys

from .. import corpus, retrieve
from ..cli import P0, read_jsonl
from .gold import gold


def recall(arm: str = "r0", set_name: str = "dev", budget: int = 12) -> dict:
    g = gold()
    plans = {r["qid"]: r["plan"] for r in read_jsonl(P0 / "plan.jsonl")}
    ids = set(corpus.split()[set_name]) if set_name != "all" else set(g)
    rows = []
    for qid in sorted(ids):
        q = g[qid]
        sel = retrieve.select_pages(q["doc_name"], q["question"], arm=arm, plan=plans.get(qid), budget=budget)
        gp = set(q["pages"])
        rows.append({"qid": qid, "type": q["question_type"], "recall": len(gp & set(sel["pages"])) / len(gp),
                     "all": gp <= set(sel["pages"]), "n_pages": len(sel["pages"])})
    by = {}
    for r in rows:
        by.setdefault(r["type"], []).append(r["recall"])
    return {"arm": arm, "set": set_name, "budget": budget, "n": len(rows),
            "recall": round(sum(r["recall"] for r in rows) / len(rows), 3),
            "all_gold_found": round(sum(r["all"] for r in rows) / len(rows), 3),
            "pages_mean": round(sum(r["n_pages"] for r in rows) / len(rows), 1),
            "by_type": {k: round(sum(v) / len(v), 3) for k, v in sorted(by.items())}}


if __name__ == "__main__":
    for arm in sys.argv[1:] or ["r0"]:
        print(json.dumps(recall(arm)))
