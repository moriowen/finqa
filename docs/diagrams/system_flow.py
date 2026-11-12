"""Draws docs/diagrams/system-flow.svg: the whole system, one row per stage, with the technology and the decision.

  python docs/diagrams/system_flow.py
"""
from __future__ import annotations
import textwrap
from html import escape
from pathlib import Path

W = 600
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"
KIND = {  # fill, stroke
    "data": ("#FFF6D6", "#B8962E"),
    "code": ("#E6F4EA", "#3C8D5A"),
    "llm": ("#E8EEFB", "#4A67B5"),
    "out": ("#F1F1F1", "#555555"),
}
RED = "#C0392B"

INDEX = [
    ("data", "Parse 363 filings", "PyMuPDF · 54K pages · two text views per page",
     "Chunk = one PDF page, not a token window. Tables stay whole, and the page number is the provenance. "
     "Plain text feeds search. Layout text (columns joined by \"|\") is what the model reads.", None),
    ("data", "Statement pack", "title regex + table density · about 4 pages per filing",
     "Most gold evidence is on the income statement, balance sheet or cash flow statement, so these pages "
     "are always shown to the model.", None),
    ("data", "Page embeddings", "Qwen3-Embedding-8B · NumPy in memory",
     "No vector database: 54K pages fit in memory. BM25 is built per filing at question time "
     "(largest filing: 667 pages).", None),
]
ANSWER = [
    ("code", "Route the question", "filing named → Path A. Else LLM picks company (1 of 42), period, type → up to 3 filings (Path B)",
     "Path B keeps up to 3 candidate filings instead of guessing one. Each runs alone, so two filings never "
     "share a prompt.", "no company"),
    ("code", "Select about 12 pages", "statement pack + BM25 + dense, fused by reciprocal rank",
     "Picked on dev with a rule fixed in advance: the cheapest option within 5 points of the best. Gold-page "
     "recall 84% → 87% with dense. LLM query planning added cost, not recall.", None),
    ("llm", "Call 1: extract values", "Qwen3.5 2B / 9B / 27B on vLLM · JSON schema enforced",
     "Each value comes with its page, exact quote, column, period and scale, plus a formula over value names. "
     "The model picks the numbers. It never does arithmetic.", None),
    ("code", "Check and compute (Python)", "G3 quote is on the page · G5 formula whitelist · evaluate",
     "Formulas may use only value names and avg, sum, cagr, abs, max, min. Constants only if they appear "
     "in the question. A failed check gets one retry with the error.", "fails twice"),
    ("llm", "Call 2: write the answer", "plain text that cites [v1], [v2] · G4 number check",
     "Every number in the text must be a checked value or the computed result. One retry with the error.",
     "fails twice"),
    ("llm", "Verifier", "Gemma 4 12B · cited pages as 150 dpi images",
     "Gemma checks the cited page images for period, unit, column and support. "
     "Anything but a clear yes is a refusal.", "not a clear yes"),
    ("code", "Combine filings (G8)", "Path B only",
     "One filing answers → that answer. All agree → answer. They disagree → AMBIGUOUS, with each value and "
     "its source.", "filings disagree"),
    ("out", "Answer row", "status · answer · computation · provenance · models",
     "Code attaches the provenance from checked values: filing, PDF page, quote, passage, column, scale. "
     "The LLM never writes a page number. No checked citation, no answer.", None),
]

BX, BW = 8, 236          # stage boxes
LX, LW = 256, 70         # abstain lane
NX, NW = 338, 256        # decision notes
PITCH, BH = 62, 48


def t(x, y, s, size=9, weight="normal", color="#111", anchor="start", style=""):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" '
            f'text-anchor="{anchor}" {style}>{escape(s)}</text>')


def main():
    o, y = [], 20
    o.append(t(BX, y, "How a question becomes an answer with provenance", 14, "bold"))
    y += 16
    o.append(t(BX, y, "Left: each stage and its technology. Right: the decision made at that stage and why. "
                      "Red: where the system refuses.", 8.5, color="#444"))
    y += 14
    lx = BX
    for k, lab in (("data", "data / index"), ("code", "code (deterministic)"), ("llm", "LLM call"), ("out", "output")):
        f, s = KIND[k]
        o.append(f'<rect x="{lx}" y="{y - 8}" width="11" height="9" rx="2" fill="{f}" stroke="{s}"/>')
        o.append(t(lx + 15, y, lab, 8.5, color="#333"))
        lx += 22 + 5.2 * len(lab)
    o.append(f'<line x1="{lx}" y1="{y - 3.5}" x2="{lx + 16}" y2="{y - 3.5}" stroke="{RED}" stroke-dasharray="3 2"/>')
    o.append(t(lx + 20, y, "refusal path", 8.5, color=RED))
    y += 8

    lane_top = lane_bot = None
    for title, rows in (("INDEX · once, offline", INDEX), ("ANSWER · for every question", ANSWER)):
        y += 18
        o.append(t(BX, y, title, 9.5, "bold", "#333", style='letter-spacing="0.6"'))
        o.append(t(NX, y, "DECISION AND REASON", 9.5, "bold", "#333", style='letter-spacing="0.6"'))
        y += 8
        for i, (kind, name, tech, note, abstain) in enumerate(rows):
            f, s = KIND[kind]
            top = y
            o.append(f'<rect x="{BX}" y="{top}" width="{BW}" height="{BH}" rx="6" fill="{f}" stroke="{s}" stroke-width="1"/>')
            o.append(t(BX + 10, top + 15, name, 10.5, "bold"))
            for j, line in enumerate(textwrap.wrap(tech, 50)[:3]):
                o.append(t(BX + 10, top + 27 + j * 9.6, line, 8.2, color="#333"))
            for j, line in enumerate(textwrap.wrap(note, 58)[:4]):
                o.append(t(NX, top + 10 + j * 11, line, 8.6, color="#222"))
            if abstain:
                cy = top + BH / 2
                o.append(f'<line x1="{BX + BW}" y1="{cy}" x2="{LX}" y2="{cy}" stroke="{RED}" stroke-dasharray="3 2" marker-end="url(#ra)"/>')
                o.append(t(BX + BW - 6, top + 13, abstain, 7.5, color=RED, anchor="end"))
                lane_top = cy - 14 if lane_top is None else lane_top
                lane_bot = cy + 14
            if i < len(rows) - 1:
                o.append(f'<line x1="{BX + BW / 2}" y1="{top + BH}" x2="{BX + BW / 2}" y2="{top + PITCH - 1}" stroke="#333" marker-end="url(#a)"/>')
            y += PITCH
        y -= PITCH - BH
    # abstain lane
    o.append(f'<rect x="{LX}" y="{lane_top}" width="{LW}" height="{lane_bot - lane_top}" rx="6" fill="#FDECEA" stroke="{RED}" stroke-dasharray="4 3"/>')
    mid = (lane_top + lane_bot) / 2
    for j, line in enumerate(("NOT_FOUND", "or", "AMBIGUOUS", "", "with the", "reason and", "the pages", "searched")):
        o.append(t(LX + LW / 2, mid - 40 + j * 11, line, 8 if j not in (0, 2) else 8.5, "bold" if j in (0, 2) else "normal", RED, "middle"))
    y += 22
    for j, line in enumerate(textwrap.wrap(
            "Evaluation sits outside the system and never feeds it: code grades numeric answers and gpt-oss-20b grades "
            "text answers against the gold answer. 51 dev questions for every choice above, 99 test questions run once.", 118)):
        o.append(t(BX, y + j * 11, line, 8.5, color="#444"))
    y += 26
    defs = ('<defs><marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">'
            '<path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker>'
            f'<marker id="ra" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L8,4 L0,8 z" fill="{RED}"/></marker></defs>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {y:.0f}" font-family="{FONT}" role="img" '
           f'aria-label="System flow: indexing, routing, retrieval, extraction, code checks, answer, verifier, combine, '
           f'output, with the decision at each stage and the refusal path.">{defs}{"".join(o)}</svg>')
    out = Path(__file__).with_name("system-flow.svg")
    out.write_text(svg)
    print(out, f"height {y:.0f}")


if __name__ == "__main__":
    main()
