"""Pass 1: answer one question against one filing (A16, A17, A18, A21).

Modes:
  full   - call 1 (extract) -> G3/G5 code checks (1 retry) -> Python computes -> call 2 (write) -> G4 (1 retry)
  bare   - one free-text call, no checks (the 'model alone' setting of the sweep, A15)
  oracle - like full, but the pages are given by the caller (gold pages, eval only)
"""
from __future__ import annotations
import json
import re

from . import checks, llm, parse, prompts, retrieve
from .corpus import filings
from .formula import FormulaError, SCALES, evaluate, parse_raw, present

MAX_CHARS = 48_000      # about 12K tokens of page text
PAGE_CHARS = 9_000


def filing_info(doc: str) -> str:
    f = filings()[doc]
    period = f"{f.quarter} of fiscal year {f.year}" if f.quarter else f"fiscal year {f.year}"
    s = f"Company: {f.company}. Document: {f.doc_type} for {period}"
    if f.date:
        s += f", dated {f.date}"
    return s + f". File: {doc}."


def page_block(doc: str, pages: list[int], ranked_extras: list[int] | None = None) -> tuple[str, list[int]]:
    """Text of the pages, as the LLM sees it. Drops the lowest-ranked extra pages if the text is too long."""
    lay = parse.load(doc)["layout"]
    keep = list(pages)
    order_drop = [p for p in reversed(ranked_extras or []) if p in keep]

    def build(ps):
        return "\n\n".join(f"=== PAGE {p + 1} ===\n{retrieve.compact(lay[p])[:PAGE_CHARS]}" for p in sorted(ps))
    txt = build(keep)
    while len(txt) > MAX_CHARS and order_drop:
        keep.remove(order_drop.pop(0))
        txt = build(keep)
    return txt, sorted(keep)


def _ident(s: str) -> str:
    s = re.sub(r"[^a-z0-9_]", "_", s.lower()).strip("_")
    return s if s and not s[0].isdigit() else "v_" + s


def check_call1(out: dict, doc: str, shown: list[int]) -> tuple[list[str], dict]:
    """G3 + G5. Returns (errors, checked) where checked has values with ids, result, shown text."""
    errs = []
    d = parse.load(doc)
    vals = []
    seen = set()
    for i, v in enumerate(out.get("values") or [], 1):
        v = dict(v)
        v["name"] = _ident(v.get("name", f"value_{i}"))
        if v["name"] in seen:
            errs.append(f"value name '{v['name']}' is used twice")
        seen.add(v["name"])
        p = v.get("page", 0) - 1
        if p not in shown:
            errs.append(f"{v['name']}: page {v.get('page')} is not one of the given pages")
            continue
        if not checks.quote_on_page(v.get("quote", ""), [d["layout"][p], d["plain"][p]]):
            errs.append(f"{v['name']}: the quote is not on page {p + 1}. Copy it exactly from one line of the page")
            continue
        if not checks.raw_in_quote(v.get("raw", ""), v.get("quote", "")):
            errs.append(f"{v['name']}: raw '{v.get('raw')}' does not appear in its quote")
            continue
        v["id"] = f"v{len(vals) + 1}"
        v["page_index"] = p
        v["number"] = parse_raw(v["raw"])
        vals.append(v)
    status = out.get("status")
    checked = {"values": vals, "result": None, "shown": None, "shown_text": None}
    if status == "not_found":
        return errs, checked
    if not vals:
        errs.append("no value passed the checks; give exact quotes, or answer not_found")
        return errs, checked
    formula = (out.get("formula") or "").strip()
    display = out.get("display", "number")
    if formula and display != "text":
        nums = {v["name"]: v["number"] * SCALES.get(v["scale"], 1.0) for v in vals if v["number"] is not None}
        pers = {v["name"]: v.get("period") for v in vals}
        try:
            r = evaluate(formula, nums, pers)
            rnd = out.get("rounding", -1)
            shown_v, shown_t = present(r, display, out.get("out_scale", "units"), None if rnd is None or rnd < 0 else rnd)
            checked.update(result=r, shown=shown_v, shown_text=shown_t, formula=formula)
        except FormulaError as e:
            errs.append(f"formula: {e}")
    elif display != "text" and status == "found" and any(v["number"] is not None for v in vals):
        errs.append("formula is empty: write the formula with value names (for one value, its name)")
    return errs, checked


def call1_messages(question: str, doc: str, page_txt: str, glossary: bool) -> list[dict]:
    sys_p = prompts.CALL1_SYSTEM + ("\n\n" + prompts.GLOSSARY if glossary else "")
    return [{"role": "system", "content": sys_p},
            {"role": "user", "content": f"FILING: {filing_info(doc)}\n\nPAGES:\n{page_txt}\n\nQUESTION: {question}"}]


def evidence_text(checked: dict, out1: dict) -> str:
    lines = []
    for v in checked["values"]:
        lines.append(f'{v["id"]} {v["name"]} = {v["raw"]} ({v["scale"]}, {v["period"]}, column "{v["column_header"]}", '
                     f'page {v["page_index"] + 1}): "{v["quote"]}"')
    comp = ""
    if checked.get("shown_text") is not None:
        comp = f"\nCOMPUTED RESULT: {checked['formula']} = {checked['shown_text']}"
    return "EVIDENCE:\n" + "\n".join(lines) + comp + f"\nSTATUS: {out1.get('status')}"


def passage(doc: str, page: int, quote: str, raw: str) -> str:
    """The table or paragraph block around the quote, from the layout text (A17)."""
    lines = retrieve.compact(parse.load(doc)["layout"][page]).splitlines()
    head, rk = checks.norm(quote)[:15], checks.norm(raw)
    nl = [checks.norm(l) for l in lines]
    hit = next((i for i, l in enumerate(nl) if rk and rk in l and head and head in l), None)
    if hit is None:
        hit = next((i for i, l in enumerate(nl) if head and head in l), None)
    if hit is None:
        hit = next((i for i, l in enumerate(nl) if rk and rk in l), 0)
    lo, hi = max(0, hit - 6), min(len(lines), hit + 7)
    return "\n".join(lines[lo:hi])


async def run_full(cl, q, doc: str, pages: list[int], ranked: list[int], *, glossary: bool = False,
                   use_images: bool = False) -> dict:
    page_txt, shown = page_block(doc, pages, [p for p in ranked if p in pages])
    rec = {"qid": q.id, "doc": doc, "pages_shown": [p + 1 for p in shown], "attempts": []}
    msgs = call1_messages(q.question, doc, page_txt, glossary)
    if use_images:  # A12 experiment: page images instead of only text
        msgs[1]["content"] = [{"type": "text", "text": msgs[1]["content"]}] + \
            [llm.image_part(parse.render_png(doc, p, dpi=90)) for p in shown[:8]]
    checked, out1 = None, None
    for attempt in range(2):
        r = await llm.chat(cl, msgs, schema=prompts.CALL1_SCHEMA, max_tokens=3000)
        out1 = r.get("json") or {}
        errs, checked = check_call1(out1, doc, shown) if out1 else (["output was not valid JSON"], None)
        rec["attempts"].append({"call": 1, "out": out1, "errors": errs, "usage": r["usage"], "seconds": r["seconds"]})
        if not errs:
            break
        if attempt == 0:
            msgs = msgs + [{"role": "assistant", "content": r["text"]},
                           {"role": "user", "content": "Your output failed these checks:\n- " + "\n- ".join(errs) +
                            "\nFix them. Copy quotes exactly. If you cannot find exact evidence for this company and period, use status not_found."}]
    if out1.get("status") == "not_found":
        rec.update(status="NOT_FOUND", reason=f"extractor: {out1.get('reason', '')}".strip())
        return rec
    if errs:
        rec.update(status="NOT_FOUND", reason="code checks failed twice: " + "; ".join(errs[:3]))
        return rec
    rec.update(values=checked["values"], formula=checked.get("formula"), result=checked["result"],
               shown=checked["shown"], shown_text=checked["shown_text"], display=out1.get("display"),
               extract_status=out1.get("status"))
    # call 2: only checked evidence + the pages that the quotes come from
    qpages = sorted({v["page_index"] for v in checked["values"]})
    ctx, _ = page_block(doc, qpages)
    m2 = [{"role": "system", "content": prompts.CALL2_SYSTEM},
          {"role": "user", "content": f"FILING: {filing_info(doc)}\n\n{evidence_text(checked, out1)}\n\n"
                                      f"PAGES OF THE QUOTES:\n{ctx}\n\nQUESTION: {q.question}"}]
    ids = {v["id"] for v in checked["values"]}
    for attempt in range(2):
        r = await llm.chat(cl, m2, schema=prompts.CALL2_SCHEMA, max_tokens=800)
        out2 = r.get("json") or {}
        ans = out2.get("answer", "")
        cites = [c for c in out2.get("citations", []) if c in ids] or sorted(set(re.findall(r"v\d+", ans)) & ids)
        bad = checks.number_check(ans, checked["values"], checked["result"], checked["shown"]) if ans else ["(empty)"]
        errs2 = []
        if bad:
            errs2.append(f"numbers not in the evidence or the result: {', '.join(bad[:5])}")
        if not cites:
            errs2.append("no citation of a value ID")
        rec["attempts"].append({"call": 2, "out": out2, "errors": errs2, "usage": r["usage"], "seconds": r["seconds"]})
        if not errs2:
            break
        if attempt == 0:
            m2 = m2 + [{"role": "assistant", "content": r["text"]},
                       {"role": "user", "content": "Your answer failed these checks:\n- " + "\n- ".join(errs2) +
                        "\nUse only numbers from the evidence and the computed result, and cite value IDs."}]
    if errs2:
        rec.update(status="NOT_FOUND", reason="number check (G4) failed twice: " + "; ".join(errs2))
        return rec
    used = [v for v in checked["values"] if v["id"] in cites] or checked["values"]
    rec.update(status="CANDIDATE", answer=ans, citations=cites,
               provenance=[{"id": v["id"], "doc": doc, "pdf_page": v["page_index"] + 1, "quote": v["quote"],
                            "passage": passage(doc, v["page_index"], v["quote"], v["raw"]),
                            "column": v["column_header"], "period": v["period"], "scale": v["scale"]} for v in used])
    return rec


async def run_bare(cl, q, doc: str, pages: list[int], ranked: list[int]) -> dict:
    page_txt, shown = page_block(doc, pages, [p for p in ranked if p in pages])
    r = await llm.chat(cl, [{"role": "system", "content": prompts.BARE_SYSTEM},
                            {"role": "user", "content": f"FILING: {filing_info(doc)}\n\nPAGES:\n{page_txt}\n\nQUESTION: {q.question}"}],
                       max_tokens=800)
    return {"qid": q.id, "doc": doc, "pages_shown": [p + 1 for p in shown], "status": "BARE",
            "answer": llm.strip_think(r["text"]), "attempts": [{"call": "bare", "usage": r["usage"], "seconds": r["seconds"]}]}


def dumps(rec: dict) -> str:
    return json.dumps(rec, default=str)
