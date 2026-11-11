"""Retrieval for one filing (A13, A19).

Pages sent to the LLM = statement pack (always) + extra pages ranked by the chosen arm, up to a page budget.
Arms: r0 = BM25 on the question; r1 = r0 + dense; r2 = r0 + query planning; r3 = all three.
"""
from __future__ import annotations
import json
import re
from functools import lru_cache

import numpy as np
from rank_bm25 import BM25Okapi

from . import parse, paths

STOP = set("the a an of and or in on for to is was what by as at from with its it be are this that does did has have "
           "which how much do if than then there their they them any all please answer question using based "
           "provide give state explain round decimal places units".split())


def tokens(s: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9&]+", s.lower()) if w not in STOP and len(w) > 1]


@lru_cache(maxsize=64)
def bm25(doc: str) -> BM25Okapi:
    return BM25Okapi([tokens(t) or ["_empty_"] for t in parse.load(doc)["plain"]])


def rank_bm25(doc: str, query: str) -> list[int]:
    s = bm25(doc).get_scores(tokens(query))
    return [int(i) for i in np.argsort(-s, kind="stable")]


def statement_pack(doc: str) -> list[int]:
    return sorted(parse.load(doc)["statements"])


# ---- dense (A19 R1): vectors are precomputed by the embedding job, so retrieval needs no server ----
VEC_DIR = paths.ARTIFACTS / "vectors"


@lru_cache(maxsize=64)
def _page_vecs(doc: str):
    p = VEC_DIR / f"{doc}.npy"
    return np.load(p) if p.exists() else None


@lru_cache(maxsize=1)
def _query_vecs() -> dict[str, np.ndarray]:
    p = VEC_DIR / "queries.jsonl"
    out = {}
    if p.exists():
        for line in p.read_text().splitlines():
            r = json.loads(line)
            out[r["text"]] = np.asarray(r["vec"], dtype=np.float32)
    return out


def rank_dense(doc: str, query: str) -> list[int] | None:
    pv, qv = _page_vecs(doc), _query_vecs().get(query)
    if pv is None or qv is None:
        return None
    return [int(i) for i in np.argsort(-(pv @ qv), kind="stable")]


def _rrf(lists: list[list[int]], k: int = 60) -> list[int]:
    score: dict[int, float] = {}
    for lst in lists:
        for r, p in enumerate(lst[:50]):
            score[p] = score.get(p, 0.0) + 1.0 / (k + r + 1)
    return sorted(score, key=lambda p: -score[p])


def select_pages(doc: str, question: str, arm: str = "r0", plan: dict | None = None,
                 budget: int = 12, extra_min: int = 5) -> dict:
    """Return {'pages': [...], 'pack': [...], 'ranked': [...]}. Pack first, then extras by rank."""
    pack = statement_pack(doc)
    lists = [rank_bm25(doc, question)]
    if arm in ("r1", "r3"):
        d = rank_dense(doc, question)
        if d is not None:
            lists.append(d)
    if arm in ("r2", "r3") and plan:
        for q in plan.get("queries", [])[:6]:
            lists.append(rank_bm25(doc, q))
    ranked = lists[0] if len(lists) == 1 else _rrf(lists)
    n_extra = max(extra_min, budget - len(pack))
    extras = [p for p in ranked if p not in pack][:n_extra]
    pages = sorted(set(pack) | set(extras))
    return {"pages": pages, "pack": pack, "ranked": ranked[:30]}


def compact(text: str) -> str:
    """Layout text with long space runs turned into ' | ' column separators, to save tokens."""
    t = re.sub(r"\$\s+", "$", text)
    t = re.sub(r"[ \t]{3,}", " | ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip()
