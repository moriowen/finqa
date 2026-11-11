"""Code guardrails G3 (quote check) and G4 (number check). Deterministic, no LLM (A18)."""
from __future__ import annotations
import re

from .formula import SCALES, parse_raw


def norm(s: str) -> str:
    """Remove all whitespace and lowercase. PDF text breaks words ('Incom e'), so spaces carry no meaning."""
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("−", "-")
    return re.sub(r"[\s|]+", "", s).lower()   # '|' is our column separator in compacted layout text


def quote_on_page(quote: str, page_texts: list[str]) -> bool:
    """G3: the quote exists on the page. '...' in a quote splits it into parts that must all exist, in order."""
    q = quote.strip().strip('"').strip()
    if len(norm(q)) < 4:
        return False
    hay = [norm(t) for t in page_texts]
    parts = [norm(p) for p in re.split(r"\.\.\.|…", q) if len(norm(p)) >= 4]
    if not parts:
        return False
    if _parts_on_one_line(q, page_texts):
        return True
    for h in hay:
        pos, ok = 0, True
        for p in parts:
            i = h.find(p, pos)
            if i < 0:
                ok = False
                break
            pos = i + len(p)
        if ok:
            return True
    return False


def _parts_on_one_line(quote: str, page_texts: list[str]) -> bool:
    """A quote like 'Total net revenue | 4,713,500' passes if each part is on the same page line, in order.
    The model often quotes the row label and the one column it used, and skips the other columns."""
    parts = [norm(p) for p in re.split(r"\||\.\.\.|…", quote) if norm(p)]
    if len(parts) < 2:
        return False
    for t in page_texts:
        lines = t.splitlines()
        for i in range(len(lines)):
            h = norm(" ".join(lines[i:i + 2]))   # a row label can wrap onto the next line
            pos, ok = 0, True
            for p in parts:
                j = h.find(p, pos)
                if j < 0:
                    ok = False
                    break
                pos = j + len(p)
            if ok:
                return True
    return False


def raw_in_quote(raw: str, quote: str) -> bool:
    r = norm(raw).replace("$", "")
    return bool(r) and r in norm(quote).replace("$", "")


_NUM = re.compile(r"(?<![\w.])[-−(]?\$?\s?\d[\d,]*(?:\.\d+)?\)?\s?%?")


def numbers_in_text(text: str) -> list[tuple[float, int, str]]:
    """Numbers in free text, skipping period labels (FY2018, Q2, 2018 as a year, 10-K, 8-K)."""
    out = []
    t = re.sub(r"\b(FY|Q[1-4]|H[12])\s?'?\d{2,4}\b", " ", text, flags=re.I)
    t = re.sub(r"\b(10-?K|10-?Q|8-?K)\b", " ", t, flags=re.I)
    t = re.sub(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}(,\s*\d{4})?", " ", t)
    t = re.sub(r"\[v\d+(?:\s*,\s*v\d+)*\]", " ", t)           # quote-ID citations
    for m in _NUM.finditer(t):
        tok = m.group(0).strip()
        core = re.sub(r"[^\d.]", "", tok)
        if not core or core == ".":
            continue
        if re.fullmatch(r"(19|20)\d{2}", core) and "," not in tok and "$" not in tok and "%" not in tok:
            continue  # a year
        v = float(core)
        dec = len(core.split(".")[1]) if "." in core else 0
        out.append((v, dec, tok))
    return out


def allowed_numbers(values: list[dict], result: float | None, shown: float | None) -> list[float]:
    """Every number the answer may contain: each value in every scale, the result, the shown result."""
    allowed = []
    for v in values:
        x = parse_raw(v.get("raw", ""))
        if x is None:
            continue
        absval = abs(x) * SCALES.get(v.get("scale", "units"), 1.0)
        allowed.append(abs(x))
        for s in SCALES.values():
            allowed.append(absval / s)
    for r in (result, shown):
        if r is None:
            continue
        allowed.append(abs(r))
        allowed.append(abs(r) * 100)
        for s in SCALES.values():
            allowed.append(abs(r) / s)
    return allowed


def number_check(answer: str, values: list[dict], result: float | None, shown: float | None) -> list[str]:
    """G4: each number in the answer is a checked value or the computed result. Returns the unsupported tokens."""
    allowed = allowed_numbers(values, result, shown)
    bad = []
    for v, dec, tok in numbers_in_text(answer):
        if v <= 12 and dec == 0 and "%" not in tok and "$" not in tok:
            continue  # small counts: "two segments", "3 years"
        tol = max(0.5 * 10 ** (-dec), 1e-9)
        if not any(abs(v - a) <= tol or (a and abs(v - a) / abs(a) <= 0.005) for a in allowed):
            bad.append(tok)
    return bad
