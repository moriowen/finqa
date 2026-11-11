# Implementation log

Status and runbook for the build. Design is in `architecture.md` and `assumptions.md`.

## Runbook

```
# Mac
.venv/bin/python -c "from finqa import corpus, parse; parse.parse_all(list(corpus.filings()))"   # parse once (about 6 min)
.venv/bin/python -m pytest -q tests
./pace/sync.sh                      # code + PDFs + parsed pages -> ICE
# ICE (~/scratch/finqa)
bash pace/setup.sh                  # once: venv with vLLM 0.32.0
bash pace/submit.sh dev             # dev experiments, as a dependency chain
ARM=r0 bash pace/submit.sh final    # all questions with the chosen configuration
# Mac
./pace/sync.sh pull
.venv/bin/python -m finqa.evals.report run <run names>
```

## Deviations from the design

- **`number` is not an LLM output.** Code parses `raw` ("(1,577)" -> -1577). One less field the model can get wrong (A16).
- **Layout text is compacted.** Runs of 3+ spaces become ` | ` column separators to save tokens. The quote check ignores `|` (A12, A18).
- **5 duplicate PDFs removed** by identical extracted text (`corpus.DUPLICATES`). Universe: 363 filings, 42 companies (A6).
- **Model weights go to the GPU node's local disk** in each job: ICE scratch is 92% full from other projects (A14).
- **vLLM 0.32.0**, own venv `~/scratch/finqa-venv` (not the splice venv).
- **Unanswerable set: 290 questions** (150 wrong filing, 140 shifted year; 10 questions name no year) (A22).

## Log

- 2026-11-11: parsed 368 PDFs (99 MB cache). Retrieval r0 on dev: recall 0.80 at about 12 pages. 27 tests pass.
- 2026-11-11: ICE fair-share factor 0.012 (heavy recent usage on the account), so jobs wait. Jobs accept any GPU type that fits.
