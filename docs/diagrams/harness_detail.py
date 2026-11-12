"""Draws docs/diagrams/harness-detail.svg: low-level data flow inside the harness for one question and one filing.

  python docs/diagrams/harness_detail.py
"""
from __future__ import annotations
from html import escape
from pathlib import Path

W = 800
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "Menlo, Consolas, monospace"
KIND = {"in": ("#F1F1F1", "#555"), "llm": ("#E8EEFB", "#4A67B5"), "code": ("#E6F4EA", "#3C8D5A"),
        "out": ("#FFF6D6", "#B8962E")}
RED = "#C0392B"

# (kind, title, data lines (monospace), rule lines, on-failure text or None, retry_target_index or None)
ROWS = [
    ("in", "Input", [
        "question",
        "filing info: company, type, fiscal period",
        "pages: up to 12, layout text, '=== PAGE n ==='",
    ], ["Same input in the bare and full settings."], None, None),
    ("llm", "Call 1 · extract (Qwen3.5, JSON schema enforced by vLLM)", [
        "status: found | not_applicable | not_found",
        "values[≤12]: {name, raw, scale, period,",
        "              column_header, page, quote}",
        "formula: names + avg/sum/cagr/abs/max/min",
        "display, out_scale, rounding, reason",
    ], ["The schema forces this shape while the model",
        "decodes, so the output is always valid JSON."],
     "status = not_found → NOT_FOUND (the model's own refusal)", None),
    ("code", "G3 · quote check, for each value", [
        "page ∈ pages shown",
        "norm(quote) ⊂ norm(page text)   norm = drop spaces and '|'",
        "   (or every part of the quote on one line of the page)",
        "raw ⊂ quote",
        "pass → value gets id v1, v2, … and a parsed number",
    ], ["Catches invented quotes, wrong pages and",
        "numbers that are not in their quote."],
     "any fail → error list", 1),
    ("code", "G5 · formula check, then Python computes", [
        "parse formula; allow only value names and",
        "   avg, sum, cagr, abs, max, min",
        "numbers allowed only if they appear in the question",
        "value × scale (millions → 1e6), evaluate in Python",
        "result → shown_text by display, out_scale, rounding",
    ], ["The model never does arithmetic. A formula like",
        "x / 1000 is rejected: units come from out_scale.",
        "G3 and G5 errors go back to call 1 together."],
     "any fail → error list", 1),
    ("llm", "Call 2 · write the answer (plain text)", [
        "input: EVIDENCE  v1 name = raw (scale, period,",
        "       column, page): \"quote\"",
        "       COMPUTED RESULT  formula = shown_text",
        "       only the pages the quotes come from",
        "output: 1 to 4 sentences, cites [v1], [v2]",
    ], ["Call 2 sees checked values only, never the",
        "draft values that failed."], None, None),
    ("code", "G4 · number check", [
        "every number in the text ∈ checked values,",
        "   the computed result, or numbers inside a checked quote",
        "   (years, dates, page and note numbers are skipped)",
        "at least one citation [vN]; not cut off",
    ], ["Catches numbers the model made up while",
        "writing, and answers with no citation."],
     "any fail → error list", 4),
    ("code", "Provenance (code)", [
        "for each cited value: doc, PDF page, quote,",
        "   passage (13 lines around the quote), column,",
        "   period, scale   → status CANDIDATE",
    ], ["Built from checked values. The model never",
        "writes a page number."], None, None),
    ("llm", "Verifier (Gemma 4 12B, JSON schema)", [
        "input: question, filing info, evidence list,",
        "   computation, final answer,",
        "   images of up to 4 cited pages at 150 dpi",
        "output: {period_ok, unit_ok, value_in_correct_column,",
        "   answer_supported: yes | partly | no, problem}",
    ], ["Pass only if the three checks are true and",
        "answer_supported = yes. No retry."],
     "anything else → NOT_FOUND with the verifier's problem", None),
    ("out", "Output row", [
        "ANSWER: answer, computation, provenance, models",
        "NOT_FOUND: reason (which check failed), pages searched",
    ], ["Path B: one row per candidate filing, then G8",
        "combines them (disagree → AMBIGUOUS)."], None, None),
]

BX, BW = 10, 430
RX = 470
LH = 13


def t(x, y, s, size=10, weight="normal", color="#111", anchor="start", family=FONT):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}" '
            f'font-family="{family}">{escape(s)}</text>')


def main():
    o, y = [], 22
    o.append(t(BX, y, "Inside the harness: what data moves where, and what each check enforces", 15, "bold"))
    y += 17
    o.append(t(BX, y, "One question, one filing. Left: the data at each step. Right: the rule. Red: what happens on a failure.", 10, color="#444"))
    y += 14
    lx = BX
    for k, lab in (("in", "input"), ("llm", "LLM call"), ("code", "code check (deterministic)"), ("out", "output")):
        f, s = KIND[k]
        o.append(f'<rect x="{lx}" y="{y - 9}" width="12" height="10" rx="2" fill="{f}" stroke="{s}"/>')
        o.append(t(lx + 16, y, lab, 10, color="#333"))
        lx += 30 + 5.6 * len(lab)
    y += 18
    tops = []
    for i, (kind, title, data, rule, fail, retry) in enumerate(ROWS):
        f, s = KIND[kind]
        h = 22 + LH * len(data) + 8
        tops.append((y, h))
        o.append(f'<rect x="{BX}" y="{y}" width="{BW}" height="{h}" rx="6" fill="{f}" stroke="{s}"/>')
        o.append(t(BX + 10, y + 16, title, 11.5, "bold"))
        for j, line in enumerate(data):
            o.append(t(BX + 10, y + 32 + j * LH, line, 9.6, family=MONO, color="#222"))
        for j, line in enumerate(rule):
            o.append(t(RX, y + 16 + j * 13.5, line, 10.5, color="#222"))
        if fail:
            fy = y + 16 + len(rule) * 13.5 + 4
            o.append(t(RX, fy, "✗ " + fail, 10.5, "bold", RED))
            if fail.startswith("any fail"):
                o.append(t(RX, fy + 14, "1st time: errors go back to the model as a message,", 10, color=RED))
                o.append(t(RX, fy + 27, "and it tries once more. 2nd time: NOT_FOUND.", 10, color=RED))
        if i < len(ROWS) - 1:
            o.append(f'<line x1="{BX + BW / 2}" y1="{y + h}" x2="{BX + BW / 2}" y2="{y + h + 15}" stroke="#333" marker-end="url(#a)"/>')
        y += h + 16
    # retry loops: from a check row back to its LLM call row, along the left edge
    for i, (_, _, _, _, _, target) in enumerate(ROWS):
        if target is None:
            continue
        (ty, th), (cy, ch) = tops[target], tops[i]
        xL = BX + BW + 8 + 9 * (i % 3)
        y1, y2 = cy + ch / 2, ty + th / 2
        o.append(f'<path d="M{BX + BW},{y1} H{xL} V{y2} H{BX + BW + 2}" fill="none" stroke="{RED}" stroke-dasharray="4 3" marker-end="url(#ra)"/>')
    y += 4
    o.append(t(BX, y, "Retry message (1st failure): \"Your output failed these checks: - <errors>. Fix them. Copy quotes exactly. "
                      "If you cannot find exact evidence, use status not_found.\"", 9.5, color="#444"))
    y += 18
    defs = ('<defs><marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">'
            '<path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker>'
            f'<marker id="ra" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L8,4 L0,8 z" fill="{RED}"/></marker></defs>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {y:.0f}" role="img" '
           f'aria-label="Harness data flow: input, call 1 extract, quote check, formula check and Python compute, call 2 answer, '
           f'number check, provenance, verifier, output, with retry loops and refusal rules.">'
           f'<rect width="{W}" height="{y:.0f}" fill="#fff"/>{defs}{"".join(o)}</svg>')
    out = Path(__file__).with_name("harness-detail.svg")
    out.write_text(svg)
    print(out, f"height {y:.0f}")


if __name__ == "__main__":
    main()
