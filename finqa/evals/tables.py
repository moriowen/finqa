"""Markdown tables for the README and the write-up, from results/summary.json and runs/*. No number is typed by hand.

  python -m finqa.evals.tables > results/tables.md
"""
from __future__ import annotations
import json

from .. import paths
from ..cli import read_jsonl
from .report import files


def pct(x) -> str:
    return "n/a" if x is None else f"{100 * x:.0f}%"


def ci(t) -> str:
    return "" if not t else f" [{100 * t[0]:.0f} to {100 * t[1]:.0f}]"


def main():
    s = json.loads((paths.ROOT / "results" / "summary.json").read_text())
    runs = s["runs"]
    out = []

    out.append("### Model size × harness (150 questions, Path A; verifier Gemma 4 12B, judge gpt-oss-20b)\n")
    out.append("| Model | Setting | Correct | Wrong | Refused | Wrong-answer rate [95% CI] | Coverage | Selective accuracy | Page hit | Test only (99): wrong / correct |")
    out.append("|---|---|---|---|---|---|---|---|---|---|")
    for size in ("27b", "9b", "2b"):
        for setting in ("bare", "full", "full-gloss", "oracle"):
            r = runs.get(f"all-{size}-{setting}")
            if not r or not r.get("real"):
                continue
            x = r["real"]
            ph = (r.get("provenance") or {}).get("page_hit_rate") if setting != "bare" else None
            out.append(f"| Qwen3.5-{size.upper()}{' (FP8)' if size == '27b' else ''} | {setting} | {x['correct']} | {x['incorrect']} | {x['refusal']} | "
                       f"{pct(x['wrong_rate'])}{ci(x.get('wrong_ci'))} | {pct(x['coverage'])} | {pct(x['selective_acc'])} | {pct(ph)} | "
                       f"{pct((r.get('test') or {}).get('wrong_rate'))} / {pct((r.get('test') or {}).get('accuracy'))} |")

    out.append("\n### Questions with no answer in the filing (E6, 290 per model)\n")
    out.append("| Model | Setting | False answers | Wrong filing | Shifted year |")
    out.append("|---|---|---|---|---|")
    for size in ("27b", "9b", "2b"):
        for setting in ("bare", "full", "full-gloss"):
            r = runs.get(f"unans-{size}-{setting}")
            if not r or not r.get("unanswerable"):
                continue
            u = r["unanswerable"]
            out.append(f"| Qwen3.5-{size.upper()}{' (FP8)' if size == '27b' else ''} | {setting} | {u['false_answer']}/{u['n']} ({pct(u['false_answer_rate'])}) | "
                       f"{pct(u.get('wrongdoc'))} | {pct(u.get('shiftyear'))} |")

    pb = runs.get("pathb-27b-full")
    if pb and pb.get("real"):
        x = pb["real"]
        out.append("\n### Path B: no filing given (27B, full harness)\n")
        out.append("| Correct | Wrong | Refused | Wrong-answer rate | Coverage |\n|---|---|---|---|---|")
        out.append(f"| {x['correct']} | {x['incorrect']} | {x['refusal']} | {pct(x['wrong_rate'])} | {pct(x['coverage'])} |")

    out.append("\n### FinanceBench paper baselines (human labels, same 150 questions)\n")
    out.append("| Paper configuration | Correct | Wrong | Refused | Wrong-answer rate | Coverage |")
    out.append("|---|---|---|---|---|---|")
    for b in s["paper_baselines"]:
        if any(k in b["config"] for k in ("singleStore", "sharedStore", "oracle")) and "reverse" not in b["config"]:
            out.append(f"| {b['config']} | {b['correct']} | {b['incorrect']} | {b['refusal']} | {pct(b['wrong_rate'])} | {pct(b['coverage'])} |")

    vc = s.get("verifier_check") or {}
    if vc:
        out.append("\n### Verifier (Gemma 4 12B) vs judge, on answers that passed the code checks\n")
        out.append("| Run | Checked | Accepted correct | Accepted wrong (leaks) | Rejected correct (lost) | Rejected wrong (caught) |")
        out.append("|---|---|---|---|---|---|")
        for k, v in vc.items():
            out.append(f"| {k} | {v['n']} | {v['accept_correct']} | {v['accept_wrong']} | {v['reject_correct']} | {v['reject_wrong']} |")

    for key, name in (("judge_calibration", "gpt-oss-20b (used)"), ("judge_calibration_120b", "gpt-oss-120b (reference)")):
        jc = s.get(key) or {}
        if not jc.get("n"):
            continue
        out.append(f"\n### Judge calibration (E3): {name} vs the paper's 2,400 human labels\n")
        out.append(f"Agreement {pct(jc['agreement'])}. Judge says *correct* when humans say *incorrect*: "
                   f"{pct(jc['false_correct_rate'])}. Judge says *incorrect* when humans say *correct*: {pct(jc['false_incorrect_rate'])}.\n")
        out.append("| Human \\ Judge | correct | incorrect | refusal |\n|---|---|---|---|")
        for h, row in jc["confusion_human_rows"].items():
            out.append(f"| {h} | {row['correct']} | {row['incorrect']} | {row['refusal']} |")

    out.append("\n### Cost per question (pass 1 only)\n")
    out.append("| Run | LLM calls | LLM seconds | Tokens |\n|---|---|---|---|")
    for k, r in runs.items():
        c = r.get("cost") or {}
        if k.startswith("all-") and c:
            out.append(f"| {k} | {c['calls_per_q']:.1f} | {c['llm_seconds_per_q']:.1f} | {c['tokens_per_q']:,.0f} |")
    main_run = s["main"]
    out.append(f"\n### Where answers are lost ({main_run}, 150 questions)\n")
    out.append("| Stage outcome | Questions |\n|---|---|")
    for k, n in funnel(main_run):
        out.append(f"| {k} | {n} |")
    print("\n".join(out))


def funnel(run: str) -> list[tuple[str, int]]:
    from collections import Counter
    c = Counter()
    for r in read_jsonl(paths.RUNS / run / files(run)[0]):
        if "__" in r["qid"]:
            continue
        why = r.get("reason") or ""
        if r["status"] == "ANSWER":
            k = "answered (all checks passed)"
        elif r["status"] == "AMBIGUOUS":
            k = "ambiguous"
        elif "extractor" in why:
            k = "extractor: evidence not in the pages"
        elif "verifier" in why:
            k = "verifier rejected"
        elif "G4" in why:
            k = "number check (G4) failed twice"
        elif "quote" in why:
            k = "quote check (G3) failed twice"
        elif "formula" in why:
            k = "formula check (G5) failed twice"
        else:
            k = "other code check failed twice"
        c[k] += 1
    return c.most_common()


if __name__ == "__main__":
    main()
