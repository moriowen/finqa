"""Write results/answers.md (every question: answer + provenance, or the abstention reason) and results/summary.json.

  python -m finqa.evals.publish --main all-27b-full --runs all-27b-full all-9b-full ...
"""
from __future__ import annotations
import argparse
import json

from .. import paths
from ..cli import read_jsonl
from .gold import gold
from .report import files, paper_baselines, paper_calibration, run_metrics, verifier_check

OUT = paths.ROOT / "results"


def _cell(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def answers_md(run: str) -> str:
    g = gold()
    fin, jud = files(run)
    rows = {r["qid"]: r for r in read_jsonl(paths.RUNS / run / fin)}
    labs = {r["key"]: r["label"] for r in read_jsonl(paths.RUNS / run / jud)}
    lines = [f"# Answers with provenance\n",
             f"Configuration: `{run}`. One section per question, in dataset order. "
             "Status ANSWER = all checks passed; NOT_FOUND / AMBIGUOUS = the system abstained (the reason says which check failed). "
             "PDF page numbers are 1-based. `Judge` is the eval label against the gold answer (not visible to the system).\n"]
    for i, (qid, gd) in enumerate(g.items(), 1):
        r = rows.get(qid)
        lines.append(f"## {i}. {_cell(gd['question'])}\n")
        lines.append(f"`{qid}` · filing `{gd['doc_name']}` · {gd['question_type']}\n")
        if r is None:
            lines.append("_Not run._\n")
            continue
        m = r.get("models") or {}
        lines.append(f"**Status:** {r['status']} · **Judge:** {labs.get(qid, 'n/a')} · "
                     f"**Models:** answer `{m.get('answer')}`, verifier `{m.get('verifier')}`\n")
        if r["status"] == "ANSWER":
            lines.append(f"**Answer:** {_cell(r['answer'])}\n")
            if r.get("computation"):
                lines.append(f"**Computation:** `{_cell(r['computation'])}`\n")
            for p in r.get("provenance", []):
                lines.append(f"- **{p['id']}** · `{p['doc']}` · PDF page **{p['pdf_page']}** · column {p.get('column')} "
                             f"· {p.get('scale')}\n  - Quote: \"{_cell(p['quote'])}\"\n")
                lines.append("  <details><summary>Passage</summary>\n\n  ```\n" +
                             "\n".join("  " + l for l in (p.get("passage") or "").splitlines()) + "\n  ```\n  </details>\n")
        else:
            lines.append(f"**Reason:** {_cell(r.get('reason'))}\n")
            searched = "; ".join(f"`{s['doc']}` pages {', '.join(map(str, s['pages']))}" for s in r.get("pages_searched", []))
            lines.append(f"**Pages searched:** {searched or 'none'}\n")
        lines.append(f"<details><summary>Gold answer</summary>\n\n{_cell(str(gd['answer']))}\n</details>\n")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--main", required=True)
    ap.add_argument("--runs", nargs="*", default=[])
    a = ap.parse_args(argv)
    OUT.mkdir(exist_ok=True)
    (OUT / "answers.md").write_text(answers_md(a.main))
    summary = {"main": a.main, "runs": {r: run_metrics(r) for r in [a.main] + a.runs},
               "paper_baselines": paper_baselines()}
    summary["verifier_check"] = {r: v for r in [a.main] + a.runs if (v := verifier_check(r))}
    try:
        summary["judge_calibration"] = paper_calibration()
        summary["judge_calibration_120b"] = paper_calibration("judge_paper.jsonl")
    except Exception as e:  # noqa: BLE001
        summary["judge_calibration"] = {"error": repr(e)}
    (OUT / "summary.json").write_text(json.dumps(summary, indent=1, default=str))
    print("wrote results/answers.md and results/summary.json")


if __name__ == "__main__":
    main()
