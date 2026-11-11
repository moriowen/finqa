"""E6: questions whose correct output is NOT_FOUND, built in code from the real questions (A22).

Type a (wrongdoc): same question + a filing of a company from a different sector, same doc type, nearest year.
Type b (shiftyear): every year in the question moved so that the latest one is 5 years before the filing year.
Uses only the question text and filing metadata, never gold fields.
"""
from __future__ import annotations
import random
import re

from ..corpus import Question, filings, questions

YEAR = re.compile(r"(FY\s?'?(?:20)?|(?<![\dA-Za-z])20)(\d{2})(?!\d)", re.I)


def shift_years(text: str, filing_year: int) -> str | None:
    ys = [2000 + int(m.group(2)) for m in YEAR.finditer(text)]
    if not ys:
        return None
    off = max(ys) - (filing_year - 5)
    if off <= 0:
        off = 0
    if off == 0:
        return None

    def rep(m):
        y = 2000 + int(m.group(2)) - off
        return (m.group(1) if m.group(1).upper().startswith("FY") else "20") + f"{y % 100:02d}"
    return YEAR.sub(rep, text)


def build(ids: set[str] | None = None, seed: int = 0) -> list[Question]:
    rng = random.Random(seed)
    fs = filings()
    out = []
    for q in questions():
        if ids is not None and q.id not in ids:
            continue
        f = fs[q.doc_name]
        pool = [g for g in fs.values() if g.sector and f.sector and g.sector != f.sector and g.doc_type == f.doc_type]
        if pool:
            best = min(abs(g.year - f.year) for g in pool)
            g = rng.choice(sorted([g for g in pool if abs(g.year - f.year) == best], key=lambda g: g.doc_name))
            out.append(Question(id=f"{q.id}__wrongdoc", question=q.question, doc_name=g.doc_name))
        s = shift_years(q.question, f.year)
        if s:
            out.append(Question(id=f"{q.id}__shiftyear", question=s, doc_name=q.doc_name))
    return out
