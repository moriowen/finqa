"""Build the local answer viewer: viewer/data.js (every row of the shown runs) and viewer/pages/*.jpg (cited pages).

Open viewer/index.html in a browser. No server needed.

  python -m finqa.evals.viewer
"""
from __future__ import annotations
import json

import pymupdf

from .. import paths
from ..cli import read_jsonl
from .gold import gold
from .report import files

OUT = paths.ROOT / "viewer"
RUNS = [  # (run, label)
    ("all-9b-full", "Qwen3.5-9B, full pipeline, filing given"),
    ("all-27b-full", "Qwen3.5-27B FP8, full pipeline, filing given"),
    ("pathb-27b-full", "Qwen3.5-27B FP8, full pipeline, no filing given (Path B)"),
    ("pathb-9b-full", "Qwen3.5-9B, full pipeline, no filing given (Path B)"),
    ("all-2b-full", "Qwen3.5-2B, full pipeline, filing given"),
    ("all-9b-bare", "Qwen3.5-9B, bare: same pages, one prompt, no checks"),
    ("all-27b-bare", "Qwen3.5-27B FP8, bare: same pages, one prompt, no checks"),
]


def page_img(doc: str, pdf_page: int) -> str:
    name = f"{doc}_p{pdf_page}.jpg"
    f = OUT / "pages" / name
    if not f.exists():
        d = pymupdf.open(paths.PDFS / f"{doc}.pdf")
        f.write_bytes(d[pdf_page - 1].get_pixmap(dpi=85).tobytes("jpeg", jpg_quality=62))
    return f"pages/{name}"


def prov(ps):
    return [{"id": p.get("id"), "doc": p["doc"], "page": p["pdf_page"], "quote": p.get("quote"), "column": p.get("column"),
             "scale": p.get("scale"), "passage": p.get("passage"), "img": page_img(p["doc"], p["pdf_page"])} for p in ps or []]


PRESETS = {
    "Answered correctly": [("all-9b-full", "financebench_id_00394"), ("all-9b-full", "financebench_id_00995")],
    "Answered wrongly": [("all-9b-full", "financebench_id_00005")],
    "No answer in the filing": [("unans-9b-full", "financebench_id_00005__wrongdoc")],
}


def simplify(att: dict) -> dict:
    o = att.get("out") or {}
    if str(att.get("call")) == "1":
        return {"call": 1, "status": o.get("status"), "formula": o.get("formula"), "reason": o.get("reason"),
                "values": [{k: v.get(k) for k in ("name", "raw", "scale", "period", "column_header", "page", "quote")}
                           for v in o.get("values") or []], "errors": att.get("errors") or []}
    if str(att.get("call")) == "2":
        return {"call": 2, "answer": o.get("answer"), "errors": att.get("errors") or []}
    return {"call": str(att.get("call"))}


def presets(g) -> list[dict]:
    routes = {r["qid"]: r for r in read_jsonl(paths.RUNS / "pass0" / "route.jsonl")}
    out = []
    for cat, items in PRESETS.items():
        for run, qid in items:
            d = paths.RUNS / run
            if not (d / "pass1.jsonl").exists():
                continue
            fin, jud = files(run)
            final = next((r for r in read_jsonl(d / fin) if r["qid"] == qid), None)
            if final is None:
                continue
            ver = {r["key"]: {"pass": r["pass"], **(r.get("verdict") or {})} for r in read_jsonl(d / "pass2_gemma4.jsonl")}
            cfg = json.loads((d / "config.json").read_text())
            p1 = [r for r in read_jsonl(d / "pass1.jsonl") if r["qid"] == qid]
            filings = [{"doc": r["doc"], "pages": r.get("pages_shown", []), "status": r["status"], "reason": r.get("reason"),
                        "steps": [simplify(a) for a in r.get("attempts", [])], "computation": r.get("formula") and
                        f"{r.get('formula')} = {r.get('shown_text')}", "verifier": ver.get(r["key"])} for r in p1]
            base = qid.split("__")[0]
            pre = {"category": cat, "qid": qid, "question": final["question"], "path_b": cfg.get("path") == "B",
                   "route": (routes.get(qid) or {}).get("route") if cfg.get("path") == "B" else None,
                   "candidates": final.get("candidates"), "filings": filings, "models": final.get("models"),
                   "final": {"status": final["status"], "answer": final.get("answer"), "computation": final.get("computation"),
                             "reason": final.get("reason"), "provenance": prov(final.get("provenance")),
                             "alternatives": [{"doc": a["doc"], "answer": a["answer"], "provenance": prov(a["provenance"])}
                                              for a in final.get("alternatives") or []]}}
            if "__" in qid:
                pre["truth"] = {"answer": "No answer. The correct output is NOT_FOUND.",
                                "source": "this question was paired with " + ("a filing of another company" if qid.endswith("wrongdoc")
                                                                             else "the right company but a year the filing does not cover"),
                                "note": ""}
            else:
                labs = {r["key"]: r["label"] for r in read_jsonl(d / jud)}
                pre["truth"] = {"answer": str(g[base]["answer"]), "source": "FinanceBench gold answer", "judge": labs.get(qid),
                                "note": ""}
            out.append(pre)
    return out


def main():
    (OUT / "pages").mkdir(parents=True, exist_ok=True)
    g = gold()
    split = json.loads(paths.SPLIT.read_text())
    test = set(split["test"])
    data = {"runs": [], "questions": []}
    for qid, gd in g.items():
        data["questions"].append({"qid": qid, "question": gd["question"], "doc": gd["doc_name"], "type": gd["question_type"],
                                  "split": "test" if qid in test else "dev", "gold_answer": str(gd["answer"]),
                                  "gold_justification": gd["justification"], "gold_pages": [p + 1 for p in gd["pages"]]})
    for run, label in RUNS:
        fin, jud = files(run)
        d = paths.RUNS / run
        labs = {r["key"]: r["label"] for r in read_jsonl(d / jud)}
        ver = {}
        for vf in ("pass2_gemma4.jsonl",):
            for r in read_jsonl(d / vf):
                ver[r["key"]] = {"pass": r["pass"], **(r.get("verdict") or {})}
        rows = {}
        for r in read_jsonl(d / fin):
            if "__" in r["qid"]:
                continue
            key = f"{r['qid']}|{r.get('doc')}" if r.get("doc") else None
            rows[r["qid"]] = {
                "status": r["status"], "answer": r.get("answer"), "computation": r.get("computation"),
                "reason": r.get("reason"), "doc": r.get("doc"), "provenance": prov(r.get("provenance")),
                "alternatives": [{"doc": a["doc"], "answer": a["answer"], "provenance": prov(a["provenance"])}
                                 for a in r.get("alternatives") or []],
                "searched": r.get("pages_searched"), "candidates": r.get("candidates"), "models": r.get("models"),
                "verifier": ver.get(key), "judge": labs.get(r["qid"])}
        data["runs"].append({"id": run, "label": label, "rows": rows})
        print(run, len(rows))
    data["presets"] = presets(g)
    print("presets", len(data["presets"]))
    for name in ("system-flow.svg", "harness-detail.svg"):
        (OUT / name).write_text((paths.ROOT / "docs" / "diagrams" / name).read_text())
    (OUT / "data.js").write_text("window.DATA = " + json.dumps(data, separators=(",", ":")) + ";\n")
    print("pages", len(list((OUT / "pages").glob("*.jpg"))))


if __name__ == "__main__":
    main()
