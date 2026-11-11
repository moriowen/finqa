"""Pass 0 (fixed Qwen3.5-27B): query planning (A19 R2) and the Path B router (A20)."""
from __future__ import annotations
import re

from . import llm, prompts
from .corpus import Filing, companies, filings


async def plan(cl, q) -> dict:
    r = await llm.chat(cl, [{"role": "system", "content": prompts.PLAN_SYSTEM},
                            {"role": "user", "content": q.question}], schema=prompts.PLAN_SCHEMA, max_tokens=400)
    return {"qid": q.id, "question": q.question, "plan": r.get("json") or {"queries": [], "statements": []}}


async def route(cl, q) -> dict:
    keys = list(companies())
    listing = "\n".join(f"{k}: {n}" for k, n in companies().items())
    r = await llm.chat(cl, [{"role": "system", "content": prompts.ROUTER_SYSTEM + "\n\nCompanies:\n" + listing},
                            {"role": "user", "content": q.question}], schema=prompts.router_schema(keys), max_tokens=300)
    out = r.get("json") or {"company": "NONE", "years": [], "quarter": "none", "doc_type": "none", "date": ""}
    return {"qid": q.id, "question": q.question, "route": out, "candidates": candidates(out, q.question)}


def _years(question: str, llm_years: list[int]) -> set[int]:
    ys = {y for y in llm_years if 1990 <= y <= 2035}
    for a, b in re.findall(r"(?:FY\s?'?|20)(\d{2})(?:\s?-\s?(?:FY\s?|20)(\d{2}))?\b", question, re.I):
        ys.add(2000 + int(a))
        if b:
            ys.add(2000 + int(b))
    return ys


def candidates(route_out: dict, question: str, k: int = 3) -> list[str]:
    """Metadata filter + ranking (A20). Returns up to k filings, best first. Empty = no company."""
    key = route_out.get("company", "NONE")
    if key == "NONE":
        return []
    fs: list[Filing] = [f for f in filings().values() if f.company_key == key]
    ys = _years(question, route_out.get("years") or [])
    t = route_out.get("doc_type", "none")
    q = route_out.get("quarter", "none")
    if ys:
        fs = [f for f in fs if f.year in ys or f.year - 1 in ys] or fs
    if t != "none":
        fs = [f for f in fs if f.doc_type == t] or fs
    date = route_out.get("date") or ""
    dm = re.search(r"\d{4}-\d{2}-\d{2}", date)

    def score(f: Filing):
        s = 0.0
        if ys and f.year == max(ys):
            s += 4
        if (q != "none") == bool(f.quarter):
            s += 2
        if q != "none" and f.quarter == q:
            s += 2
        if f.doc_type == "10K":
            s += 1
        if dm and f.date and f.date >= dm.group(0):
            s += 3 - min(2.9, (int(f.date.replace("-", "")) - int(dm.group(0).replace("-", ""))) / 1000)
        return (-s, -f.year)
    return [f.doc_name for f in sorted(fs, key=score)[:k]]
