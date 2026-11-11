"""Choose the final configuration from the dev results with rules fixed BEFORE the dev results were seen
(written 2026-11-11 while the dev jobs were queued), then print the environment for `pace/submit.sh final`.

Rules (A12, A16, A18, A19):
  R-arm   retrieval: the cheapest arm (r0 < r1 < r2 < r3) whose dev recall is within 0.05 of the best arm.
          (A19 said "within noise, about 0.1"; 0.05 is stricter, so a clearly better arm still wins.)
  R-gloss glossary: on only if dev-2b-full-r0-gloss has higher accuracy than dev-2b-full-r0
          AND a wrong-answer rate that is not higher.
  R-think verifier thinking: on only if, on the three dev full runs together, it gives a lower wrong-answer rate
          with no more than 0.05 lower coverage. Otherwise off (cheaper).
  R-img   page images in call 1: on only if dev-27b-oracle-img has accuracy at least 0.05 higher than dev-27b-oracle.
  R-main  official answers (R3 in architecture.md): among 27b, 9b, 2b, the size with the highest dev accuracy
          whose dev wrong-answer rate is within 0.03 of the lowest. Ties -> the larger model.
Missing data for a rule -> the default (r0, off, off, off, 27b).

Change made 2026-11-11 12:50, while 27B waited for an 80 GB GPU (logged in docs/IMPLEMENTATION.md):
  - The final runs use arm r1, the result of R-arm on the dev recall (recall needs no judge, so it was known).
  - The final runs use verifier thinking OFF and page images OFF regardless of R-think and R-img, to finish without
    waiting for the 27B dev results. Both experiments still run on dev and are reported.
  - The final runs exist with and without the glossary; R-gloss picks which one is official.

  python -m finqa.evals.autopilot     # writes runs/decisions.json and prints KEY=VALUE lines
"""
from __future__ import annotations
import json

from .. import paths
from .report import labels, rates
from .retrieval import recall


def _r(run, thinking=False):
    try:
        labs = [v for k, v in labels(run, thinking).items() if "__" not in k]
        return rates(labs) if labs else None
    except Exception:  # noqa: BLE001
        return None


def decide() -> dict:
    d = {"evidence": {}}
    arms = ["r0", "r1", "r2", "r3"]
    rec = {}
    for a in arms:
        try:
            rec[a] = recall(a)["recall"]
        except Exception:  # noqa: BLE001
            pass
    d["evidence"]["recall"] = rec
    best = max(rec.values()) if rec else 0
    d["arm"] = next((a for a in arms if a in rec and rec[a] >= best - 0.05), "r0")

    g0, g1 = _r("dev-2b-full-r0"), _r("dev-2b-full-r0-gloss")
    d["evidence"]["glossary"] = {"off": g0, "on": g1}
    d["glossary"] = bool(g0 and g1 and g1["accuracy"] > g0["accuracy"] and g1["wrong_rate"] <= g0["wrong_rate"])

    off, on = [], []
    for r in ("dev-27b-full-r0", "dev-9b-full-r0", "dev-2b-full-r0"):
        off += [v for k, v in labels(r).items() if "__" not in k] if _r(r) else []
        on += [v for k, v in labels(r, True).items() if "__" not in k] if _r(r, True) else []
    t0, t1 = (rates(off) if off else None), (rates(on) if on else None)
    d["evidence"]["thinking"] = {"off": t0, "on": t1}
    d["thinking"] = bool(t0 and t1 and t1["wrong_rate"] < t0["wrong_rate"] and t1["coverage"] >= t0["coverage"] - 0.05)

    o0, o1 = _r("dev-27b-oracle"), _r("dev-27b-oracle-img")
    d["evidence"]["images"] = {"text": o0, "images": o1}
    d["images"] = bool(o0 and o1 and o1["accuracy"] >= o0["accuracy"] + 0.05)

    sizes = {s: _r(f"dev-{s}-full-r0") for s in ("27b", "9b", "2b")}
    d["evidence"]["sizes"] = sizes
    ok = {s: v for s, v in sizes.items() if v}
    if ok:
        low = min(v["wrong_rate"] for v in ok.values())
        cand = [s for s, v in ok.items() if v["wrong_rate"] <= low + 0.03]
        d["main"] = max(cand, key=lambda s: (ok[s]["accuracy"], {"27b": 3, "9b": 2, "2b": 1}[s]))
    else:
        d["main"] = "27b"
    return d


def main():
    d = decide()
    (paths.RUNS / "decisions.json").write_text(json.dumps(d, indent=1))
    print(f"ARM={d['arm']}")
    print(f"GLOSS={'1' if d['glossary'] else ''}")
    print(f"THINK={'1' if d['thinking'] else ''}")
    print(f"IMAGES={'1' if d['images'] else ''}")
    print(f"MAIN={d['main']}")


if __name__ == "__main__":
    main()
