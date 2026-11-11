"""Parse each PDF once (A6, A12, A13).

For every page we keep two texts:
  plain  - PyMuPDF get_text(): used for search (BM25, embeddings)
  layout - PyMuPDF get_text(sort=True): what the LLM reads, and what the quote check (G3) compares against
The page index is the provenance key (PDF page = index + 1, A10).
"""
from __future__ import annotations
import gzip
import json
import re
import sys
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache

import pymupdf

from . import paths

# A13 v2 statement-page detector: whitespace removed, short title line in the first 6 lines, table-heavy page.
_STMT = re.compile(
    r"^(condensed)?(consolidated)?(condensed)?("
    r"(?P<bs>balancesheets?|statements?of(financialposition|financialcondition))"
    r"|(?P<cf>statements?ofcashflows?)"
    r"|(?P<ci>statements?ofcomprehensive(income|loss|earnings))"
    r"|(?P<eq>statements?of(changesin)?(shareholders|stockholders|shareowners)?.{0,12}equity|(shareholders|stockholders).{0,3}equity)"
    r"|(?P<is>statements?of(consolidated)?(income|operations|earnings)))")


def statement_type(text: str) -> str | None:
    lines = [l.strip() for l in text.splitlines() if l.strip()][:6]
    for l in lines:
        if len(l) >= 90:
            continue
        m = _STMT.search(re.sub(r"\s+", "", l).lower())
        if m:
            toks = text.split()
            num = sum(any(c.isdigit() for c in t) for t in toks) / max(len(toks), 1)
            if num >= 0.25:
                return next(k for k in ("bs", "cf", "ci", "eq", "is") if m.group(k))
    return None


def parse_pdf(doc: str) -> dict:
    d = pymupdf.open(paths.PDFS / f"{doc}.pdf")
    plain, layout = [], []
    for pg in d:
        plain.append(pg.get_text())
        layout.append(pg.get_text(sort=True))
    stmts = {i: t for i, t in enumerate(statement_type(p) for p in plain) if t}
    return {"doc": doc, "n_pages": len(plain), "plain": plain, "layout": layout,
            "statements": {str(k): v for k, v in stmts.items()}}


def _path(doc: str):
    return paths.PAGES / f"{doc}.json.gz"


def _parse_and_save(doc: str) -> tuple[str, int]:
    out = _path(doc)
    if out.exists():
        return doc, -1
    data = parse_pdf(doc)
    tmp = out.with_suffix(".tmp")
    with gzip.open(tmp, "wt") as f:
        json.dump(data, f)
    tmp.rename(out)
    return doc, data["n_pages"]


@lru_cache(maxsize=16)
def load(doc: str) -> dict:
    p = _path(doc)
    if not p.exists():
        _parse_and_save(doc)
    with gzip.open(p, "rt") as f:
        d = json.load(f)
    d["statements"] = {int(k): v for k, v in d["statements"].items()}
    return d


def parse_all(docs: list[str], workers: int = 6) -> None:
    todo = [d for d in docs if not _path(d).exists()]
    print(f"parse: {len(todo)} of {len(docs)} filings to parse", file=sys.stderr)
    with ProcessPoolExecutor(workers) as ex:
        for i, (doc, n) in enumerate(ex.map(_parse_and_save, todo), 1):
            if i % 20 == 0 or i == len(todo):
                print(f"  {i}/{len(todo)} {doc} {n} pages", file=sys.stderr)


def render_png(doc: str, page: int, dpi: int = 110) -> bytes:
    """Page image for the verifier and the image fallback (A12). Made on demand, never stored."""
    d = pymupdf.open(paths.PDFS / f"{doc}.pdf")
    return d[page].get_pixmap(dpi=dpi).tobytes("png")
