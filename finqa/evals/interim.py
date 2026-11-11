"""Interim results while 27B, the verifier and the judge wait for 80 GB GPUs. Prints Markdown tables.

Fully graded (verifier + judge): dev round 1 (runs/devv1-*), the bare dev runs, judge calibration (E3).
Not yet verified or judged: the new 2B/9B runs. For them we report pass-1 outcomes, code-graded accuracy on
questions with a numeric gold answer (no LLM involved), and an upper bound on false answers for E6.

  python -m finqa.evals.interim > results/interim_tables.md
"""
from __future__ import annotations
import collections
import json
import re

from .. import paths
from ..cli import read_jsonl
from .gold import gold
from .judge import gold_number, number_match
from .report import paper_baselines, paper_calibration, rates
from .retrieval import recall

R = paths.RUNS


def pct(x, d=0):
    return "n/a" if x is None else f"{100 * x:.{d}f}%"


def stage(r) -> str:
    if r["status"] == "CANDIDATE":
        return "reached the verifier"
    if r["status"] == "BARE":
        return "bare answer"
    w = r.get("reason", "")
    if w.startswith("extractor"):
        return "extractor: evidence not found"
    if "G4" in w:
        return "number check (G4)"
    if "quote" in w:
        return "quote check (G3)"
    if "formula" in w:
        return "formula check (G5)"
    if "JSON" in w:
        return "invalid output (cut off)"
    return "other check"


def judged(run, file="judge.jsonl"):
    return {r["key"]: r["label"] for r in read_jsonl(R / run / file)}


def main():
    g = gold()
    out = []

    # 1. Dev round 1, fully graded
    out.append("## 1. Dev round 1, end to end (51 dev questions, verifier + judge)\n")
    out.append("| Model | Setting | Correct | Wrong | Refused | Wrong-answer rate | Coverage | Selective accuracy |")
    out.append("|---|---|---|---|---|---|---|---|")
    rows = [("27B", "bare", "dev-27b-bare-r0"), ("27B", "full harness", "devv1-27b-full-r0"),
            ("27B", "oracle pages", "devv1-27b-oracle"), ("27B", "oracle + images", "devv1-27b-oracle-img"),
            ("9B", "bare", "dev-9b-bare-r0"), ("9B", "full harness", "devv1-9b-full-r0"),
            ("2B", "bare", "dev-2b-bare-r0"), ("2B", "full harness", "devv1-2b-full-r0"),
            ("2B", "full + glossary", "devv1-2b-full-r0-gloss")]
    for m, s, run in rows:
        labs = [v for k, v in judged(run).items() if "__" not in k]
        if not labs:
            continue
        x = rates(labs)
        out.append(f"| {m} | {s} | {x['correct']} | {x['incorrect']} | {x['refusal']} | {pct(x['wrong_rate'])} | "
                   f"{pct(x['coverage'])} | {pct(x['selective_acc'])} |")

    # 2. Bare vs full, question by question
    out.append("\n## 2. What the harness did to each bare answer (dev round 1)\n")
    out.append("| Model | Bare wrong → harness refused | → harness wrong | → harness correct | Bare correct → harness refused | → harness correct | → harness wrong |")
    out.append("|---|---|---|---|---|---|---|")
    for size in ("27b", "9b", "2b"):
        b, f = judged(f"dev-{size}-bare-r0"), judged(f"devv1-{size}-full-r0")
        c = collections.Counter((b[k], f[k]) for k in b if k in f)
        out.append(f"| {size.upper()} | {c[('incorrect', 'refusal')]} | {c[('incorrect', 'incorrect')]} | {c[('incorrect', 'correct')]} | "
                   f"{c[('correct', 'refusal')]} | {c[('correct', 'correct')]} | {c[('correct', 'incorrect')]} |")

    # 3. Where dev-1 answers were lost
    out.append("\n## 3. Where dev round 1 lost answers (27B, 51 questions)\n")
    p1 = read_jsonl(R / "devv1-27b-full-r0" / "pass1.jsonl")
    p2 = {r["key"]: r for r in read_jsonl(R / "devv1-27b-full-r0" / "pass2.jsonl")}
    jc = judged("devv1-27b-full-r0", "judge_cands.jsonl")
    c = collections.Counter()
    for r in p1:
        s = stage(r)
        if s == "reached the verifier":
            ok = p2.get(r["key"], {}).get("pass")
            s = f"verifier {'accepted' if ok else 'rejected'} (judge: {jc.get(r['key'], 'not graded')})"
        c[s] += 1
    out.append("| Outcome | Questions |\n|---|---|")
    for k, n in c.most_common():
        out.append(f"| {k} | {n} |")
    empty = sum(1 for r in p1 for a in r["attempts"] if a["call"] == 2 and not a["out"].get("answer"))
    calls2 = sum(1 for r in p1 for a in r["attempts"] if a["call"] == 2)
    out.append(f"\nCall 2 returned an empty answer in {empty} of {calls2} calls (all at the 800-token limit).")

    # 4. Verifier errors in round 1
    out.append("\n## 4. Verifier vs judge on pre-verifier candidates (dev round 1)\n")
    out.append("| Model | Verifier | Accepted correct | Accepted wrong | Rejected correct | Rejected wrong |")
    out.append("|---|---|---|---|---|---|")
    for size in ("27b", "9b", "2b"):
        run = f"devv1-{size}-full-r0"
        lab = judged(run, "judge_cands.jsonl")
        for think, fname in ((False, "pass2.jsonl"), (True, "pass2_think.jsonl")):
            ver = {r["key"]: r["pass"] for r in read_jsonl(R / run / fname)}
            ks = [k for k in ver if k in lab]
            if not ks:
                continue
            q = lambda a, b: sum(ver[k] == a and (lab[k] == "correct") == b for k in ks)  # noqa: E731
            out.append(f"| {size.upper()} | {'thinking' if think else 'no thinking'} | {q(True, True)} | {q(True, False)} | "
                       f"{q(False, True)} | {q(False, False)} |")

    # 5. Judge calibration
    jc = paper_calibration()
    out.append("\n## 5. Judge calibration (E3): gpt-oss-120b on the paper's 2,400 human-labeled answers\n")
    out.append(f"Agreement {pct(jc['agreement'])}. Judge says correct where humans say incorrect: "
               f"{pct(jc['false_correct_rate'], 1)}. Judge says incorrect where humans say correct: {pct(jc['false_incorrect_rate'], 1)}.\n")
    out.append("| Human label \\ judge | correct | incorrect | refusal |\n|---|---|---|---|")
    for h, row in jc["confusion_human_rows"].items():
        out.append(f"| {h} | {row['correct']} | {row['incorrect']} | {row['refusal']} |")

    # 6. Retrieval
    out.append("\n## 6. Retrieval: page recall on the dev questions (budget 12 pages)\n")
    out.append("| Arm | Recall | Metrics-generated | Domain-relevant | Novel-generated |\n|---|---|---|---|---|")
    names = {"r0": "R0 statement pack + BM25", "r1": "R1 + dense embeddings", "r2": "R2 + LLM query planning", "r3": "R3 all"}
    for a in ("r0", "r1", "r2", "r3"):
        x = recall(a)
        bt = x["by_type"]
        out.append(f"| {names[a]} | {pct(x['recall'])} | {pct(bt.get('metrics-generated'))} | {pct(bt.get('domain-relevant'))} | "
                   f"{pct(bt.get('novel-generated'))} |")

    # 7. New 2B / 9B runs: pass 1 only
    out.append("\n## 7. New 2B and 9B runs with all fixes: pass 1 only (not yet verified or judged)\n")
    out.append("| Run | Questions | Reached the verifier | Evidence not found | G3 quote | G4 number | G5 formula | Cut-off output |")
    out.append("|---|---|---|---|---|---|---|---|")
    for run in ("dev-9b-full-r0", "all-9b-full", "all-9b-full-gloss", "all-9b-oracle",
                "dev-2b-full-r0", "dev-2b-full-r0-gloss", "all-2b-full", "all-2b-full-gloss", "all-2b-oracle"):
        rs = [r for r in read_jsonl(R / run / "pass1.jsonl") if "__" not in r["qid"]]
        if not rs:
            continue
        c = collections.Counter(stage(r) for r in rs)
        n = len(rs)
        out.append(f"| {run} | {n} | {c['reached the verifier']} ({pct(c['reached the verifier'] / n)}) | {c['extractor: evidence not found']} | "
                   f"{c['quote check (G3)']} | {c['number check (G4)']} | {c['formula check (G5)']} | {c['invalid output (cut off)']} |")

    # 8. Code-graded numeric questions (no LLM judge)
    num_ids = {k for k, v in g.items() if gold_number(v["answer"])}
    out.append(f"\n## 8. Code-graded accuracy on the {len(num_ids)} questions with a numeric gold answer (no LLM involved)\n")
    out.append("For the harness this is **before** the verifier: the verifier can only remove answers, so the wrong ones here are an upper bound.\n")
    out.append("| Run | Answered | Gold number found in the answer | Not found |\n|---|---|---|---|")
    for run in ("all-9b-bare", "all-9b-full", "all-9b-full-gloss", "all-2b-bare", "all-2b-full", "all-2b-full-gloss"):
        rs = {r["qid"]: r for r in read_jsonl(R / run / "pass1.jsonl") if r["qid"] in num_ids}
        if not rs:
            continue
        ans = [r for r in rs.values() if r["status"] in ("CANDIDATE", "BARE")]
        ok = sum(number_match(g[r["qid"]]["answer"], r.get("answer") or "") for r in ans)
        out.append(f"| {run} | {len(ans)} of {len(rs)} | {ok} | {len(ans) - ok} |")

    # 9. Unanswerable questions, upper bound before the verifier
    out.append("\n## 9. Questions with no answer in the filing (E6): answers that reach the verifier\n")
    out.append("The correct output is always NOT_FOUND. Pass 1 alone already refuses most of them; the verifier can only refuse more. "
               "Bare answers are classified with a simple phrase rule (\"not provided\", \"does not contain\", ...), not with the judge.\n")
    out.append("| Run | Questions | Answered (upper bound of false answers) | Wrong filing | Shifted year |\n|---|---|---|---|---|")
    refuse = re.compile(r"not (provided|available|included|contain|present|found|disclosed|mentioned|specified)|does not (contain|include|provide|state)|cannot (be )?(determine|answer|find)|no (information|data)|unable to", re.I)
    for run in ("unans-9b-bare", "unans-9b-full", "unans-9b-full-gloss", "unans-2b-bare", "unans-2b-full", "unans-2b-full-gloss"):
        rs = read_jsonl(R / run / "pass1.jsonl")
        if not rs:
            continue

        def answered(r):
            if r["status"] == "BARE":
                return not refuse.search(r.get("answer") or "")
            return r["status"] == "CANDIDATE"
        a = [r for r in rs if answered(r)]
        wd = [r for r in rs if r["qid"].endswith("wrongdoc")]
        sy = [r for r in rs if r["qid"].endswith("shiftyear")]
        out.append(f"| {run} | {len(rs)} | {len(a)} ({pct(len(a) / len(rs))}) | {pct(sum(answered(r) for r in wd) / max(1, len(wd)))} | "
                   f"{pct(sum(answered(r) for r in sy) / max(1, len(sy)))} |")

    # 10. Paper baselines
    out.append("\n## 10. FinanceBench paper baselines (human labels, same 150 questions)\n")
    out.append("| Paper configuration | Correct | Wrong | Refused | Wrong-answer rate | Coverage |\n|---|---|---|---|---|---|")
    for b in paper_baselines():
        if "reverse" not in b["config"] and "claude" not in b["config"]:
            out.append(f"| {b['config']} | {b['correct']} | {b['incorrect']} | {b['refusal']} | {pct(b['wrong_rate'])} | {pct(b['coverage'])} |")
    print("\n".join(out))


if __name__ == "__main__":
    main()
