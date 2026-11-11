"""The ONLY module that reads gold fields (answer, evidence, justification). Pipeline code must not import it (E10)."""
from __future__ import annotations
import json
from functools import lru_cache

from .. import paths


@lru_cache(maxsize=1)
def gold() -> dict[str, dict]:
    out = {}
    for line in paths.QUESTIONS.read_text().splitlines():
        r = json.loads(line)
        out[r["financebench_id"]] = {
            "question": r["question"], "answer": r["answer"], "justification": r.get("justification") or "",
            "doc_name": r["doc_name"], "company": r["company"], "question_type": r["question_type"],
            "question_reasoning": r.get("question_reasoning"),
            "pages": sorted({e["evidence_page_num"] for e in r["evidence"]}),
            "evidence_docs": sorted({e.get("doc_name", r["doc_name"]) for e in r["evidence"]}),
        }
    return out


def oracle_pages() -> dict[str, list[int]]:
    """Gold page indexes per question, for the oracle setting only."""
    return {k: v["pages"] for k, v in gold().items()}
