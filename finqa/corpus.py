"""The filing universe and the system's view of a question.

The system may read only: financebench_id, question, doc_name (optional, Path A).
Gold fields (answer, evidence, justification) are read only by finqa/evals/gold.py.
"""
from __future__ import annotations
import json
import re
from dataclasses import dataclass, asdict
from functools import lru_cache
from . import paths

DOC_RE = re.compile(r"^(?P<key>.+?)_(?P<year>\d{4})(?P<q>Q\d)?_(?P<type>10K|10Q|8K|EARNINGS|ANNUALREPORT)", re.I)
# e.g. MCDONALDS_8K_dated-2023-01-06: no period in the usual place, the year comes from the date
DOC_RE2 = re.compile(r"^(?P<key>.+?)_(?P<type>10K|10Q|8K|EARNINGS)_dated-(?P<year>\d{4})", re.I)
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")

# PDFs without metadata whose text is identical to a filing that has metadata (checked by MD5 of the
# extracted text, 2026-11-11). They are copies, so they are not in the universe (A6).
DUPLICATES = {
    "AMCOR_2022_8K_2022-04-26": "AMCOR_2022_8K_dated-2022-04-26",
    "AMCOR_2022_8K_2022-07-01": "AMCOR_2022_8K_dated-2022-07-01",
    "FOOTLOCKER_2022_10Q": "FOOTLOCKER_2023Q3_10Q",
    "ULTABEAUTY_2023Q1_EARNINGS": "ULTABEAUTY_2024Q1_EARNINGS",
    "ULTABEAUTY_2023Q2_EARNINGS": "ULTABEAUTY_2024Q2_EARNINGS",
}


@dataclass(frozen=True)
class Filing:
    doc_name: str
    company_key: str     # e.g. JOHNSON_JOHNSON
    company: str         # display name from metadata, e.g. "Johnson & Johnson"
    year: int            # fiscal period in the file name
    quarter: str | None  # "Q2" or None
    doc_type: str        # 10K, 10Q, 8K, EARNINGS
    date: str | None     # for dated 8-Ks
    sector: str | None
    has_metadata: bool


def parse_doc_name(doc: str) -> dict:
    m = DOC_RE.match(doc) or DOC_RE2.match(doc)
    if not m:
        raise ValueError(f"cannot parse filing name {doc}")
    d = DATE_RE.search(doc)
    t = m["type"].upper()
    return dict(company_key=m["key"].upper(), year=int(m["year"]),
                quarter=(m.groupdict().get("q") or None),
                doc_type="10K" if t == "ANNUALREPORT" else t, date=d.group(1) if d else None)


@lru_cache(maxsize=1)
def filings() -> dict[str, Filing]:
    """All filings that have a PDF: metadata entries + PDFs parsed from the file name (A6, A20)."""
    meta = {}
    for line in paths.DOC_INFO.read_text().splitlines():
        r = json.loads(line)
        meta[r["doc_name"]] = r
    names = {}
    for r in meta.values():
        names.setdefault(parse_doc_name(r["doc_name"])["company_key"], r["company"])
    out = {}
    for pdf in sorted(paths.PDFS.glob("*.pdf")):
        doc = pdf.stem
        if doc in DUPLICATES:
            continue
        p = parse_doc_name(doc)
        r = meta.get(doc)
        sector = r.get("gics_sector") if r else None
        if sector is None:  # parsed file: borrow the sector of another filing of the same company
            sector = next((m.get("gics_sector") for d, m in meta.items()
                           if parse_doc_name(d)["company_key"] == p["company_key"]), None)
        out[doc] = Filing(doc_name=doc, company=names.get(p["company_key"], p["company_key"].title()),
                          sector=sector, has_metadata=r is not None, **p)
    return out


def companies() -> dict[str, str]:
    """company_key -> display name, for the router's enforced choice."""
    out = {}
    for f in filings().values():
        out.setdefault(f.company_key, f.company)
    return dict(sorted(out.items()))


@dataclass
class Question:
    id: str
    question: str
    doc_name: str | None = None   # None = Path B


def questions(path_b: bool = False) -> list[Question]:
    """System view of the 150 questions. Never returns gold fields."""
    out = []
    for line in paths.QUESTIONS.read_text().splitlines():
        r = json.loads(line)
        out.append(Question(id=r["financebench_id"], question=r["question"],
                            doc_name=None if path_b else r["doc_name"]))
    return out


def split() -> dict[str, list[str]]:
    return json.loads(paths.SPLIT.read_text())


def as_dict(x) -> dict:
    return asdict(x)
