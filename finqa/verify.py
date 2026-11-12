"""Pass 2 (fixed Qwen3.5-27B): verifier G6+G7 with page images, then G8 combine and the final rows (A18, A17)."""
from __future__ import annotations
import re

from . import llm, parse, prompts
from .answer import filing_info


async def verify(cl, rec: dict, question: str, thinking: bool = False, free_json: bool = False, model: str | None = None) -> dict:
    """free_json: for reasoning models. No enforced schema; the model reasons, then ends with the JSON object."""
    vals = "\n".join(f'{v["id"]} {v["name"]} = {v["raw"]} ({v["scale"]}), period {v["period"]}, column "{v["column_header"]}", '
                     f'page {v["page_index"] + 1}: "{v["quote"]}"' for v in rec["values"])
    comp = f"{rec.get('formula')} = {rec.get('shown_text')}" if rec.get("shown_text") is not None else "(no computation)"
    pages = sorted({p["pdf_page"] - 1 for p in rec["provenance"]})[:4]
    content = [{"type": "text", "text": f"QUESTION: {question}\n\nFILING: {filing_info(rec['doc'])}\n\nEVIDENCE:\n{vals}\n\n"
                                        f"COMPUTATION: {comp}\n\nFINAL ANSWER: {rec['answer']}\n\n"
                                        f"IMAGES: pages {', '.join(str(p + 1) for p in pages)}, in this order."}]
    content += [llm.image_part(parse.render_png(rec["doc"], p, dpi=150)) for p in pages]
    sys_p = prompts.VERIFIER_SYSTEM
    if free_json:
        sys_p += ("\n\nThink step by step, then end your reply with one JSON object with exactly these keys: "
                  '{"period_ok": true/false, "unit_ok": true/false, "value_in_correct_column": true/false, '
                  '"answer_supported": "yes"|"partly"|"no", "problem": "..."}')
    r = await llm.chat(cl, [{"role": "system", "content": sys_p}, {"role": "user", "content": content}],
                       schema=None if free_json else prompts.VERIFIER_SCHEMA,
                       max_tokens=8000 if free_json else (4000 if thinking else 600), thinking=thinking, model=model)
    if free_json:
        try:
            objs = re.findall(r"\{[^{}]*\"answer_supported\"[^{}]*\}", llm.strip_think(r["text"]))
            r["json"] = __import__("json").loads(objs[-1]) if objs else None
        except Exception:  # noqa: BLE001
            r["json"] = None
    v = r.get("json") or {}
    ok = bool(v) and v.get("answer_supported") == "yes" and all(v.get(k) is True for k in
                                                                ("period_ok", "unit_ok", "value_in_correct_column"))
    return {"key": rec["key"], "verdict": v, "pass": ok, "usage": r["usage"], "seconds": r["seconds"], "ttft": r.get("ttft"), "model": model or llm.MODEL}


def _first_word(s: str) -> str:
    m = re.match(r"\W*(yes|no)\b", s or "", re.I)
    return m.group(1).lower() if m else ""


def combine(qid: str, question: str, recs: list[dict], order: list[str]) -> dict:
    """G8. recs: verified pass-1 records of one question, one per candidate filing. order: candidate rank."""
    recs = sorted(recs, key=lambda r: order.index(r["doc"]) if r["doc"] in order else 99)
    searched = [{"doc": r["doc"], "pages": r.get("pages_shown", [])} for r in recs]
    base = {"qid": qid, "question": question, "pages_searched": searched, "candidates": order,
            "models": {"answer": recs[0].get("answer_model") if recs else None,
                       "verifier": next((r.get("verifier_model") for r in recs if r.get("verifier_model")), None)}}
    if recs and all(r["status"] == "BARE" for r in recs):
        r = recs[0]
        return {**base, "status": "BARE", "answer": r.get("answer"), "provenance": [], "reason": ""}
    if not recs:
        return {**base, "status": "AMBIGUOUS", "answer": None, "provenance": [],
                "reason": "the question does not identify a company in the corpus: which company?"}
    ans = [r for r in recs if r["status"] == "ANSWER"]
    if not ans:
        return {**base, "status": "NOT_FOUND", "answer": None, "provenance": [],
                "reason": " | ".join(f"{r['doc']}: {r.get('reason', '')}" for r in recs)}

    def row(r):
        models = {"answer": r.get("answer_model"), "verifier": r.get("verifier_model")}
        comp = None
        if r.get("shown_text") is not None:
            comp = f"{r['formula']} = {r['shown_text']}  where " + ", ".join(
                f"{v['name']} = {v['raw']} ({v['scale']}, {v['period']})" for v in r["values"])
        return {**base, "status": "ANSWER", "answer": r["answer"], "computation": comp, "doc": r["doc"],
                "provenance": r["provenance"], "models": models, "reason": ""}
    if len(ans) == 1:
        return row(ans[0])
    shown = [a.get("shown") for a in ans]
    if all(s is not None for s in shown):
        agree = all(abs(s - shown[0]) <= max(1e-9, 0.005 * abs(shown[0])) for s in shown)
    else:
        words = {_first_word(a["answer"]) for a in ans}
        agree = len(words) == 1 and "" not in words
    if agree:
        out = row(ans[0])
        out["reason"] = f"{len(ans)} candidate filings agree"
        return out
    return {**base, "status": "AMBIGUOUS", "answer": None,
            "alternatives": [{"doc": a["doc"], "answer": a["answer"], "provenance": a["provenance"]} for a in ans],
            "provenance": [], "reason": "candidate filings give different answers"}
