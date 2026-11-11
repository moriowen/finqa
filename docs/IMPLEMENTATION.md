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
- 2026-11-11 02:52: **smoke test passed** (job 6952665, A100 80GB, Qwen3.5-2B @ 15852e8, vLLM 0.32.0): text `391`, enforced JSON schema valid, image of 3M 2018 10-K page 60 read as `(1,577)`. Node-local `/tmp` has 1.7 TB; 4.3 GB downloaded in 7 s; server start about 6 min. Log: `pace/smoke/smoke-qwen3.5-2b.log`.
- 2026-11-11 03:14: 27B server failed to start: Qwen3.5 is a hybrid model (linear-attention layers). vLLM's default `max_num_seqs` 1024 exceeds the 325 Mamba cache blocks left after the 51 GB of 27B weights on an 80 GB GPU. Fix: `--max-num-seqs 64` in `pace/job.sbatch` (the client never sends more than 32 requests at once).
- 2026-11-11 03:05: first 9B dev run exposed fixable failures (formula used row labels, quotes skipped columns, 365 in a question-defined formula, dates in the number check, statement pages dropped by text trimming, detector missed "INCOME STATEMENTS" and "NIKE, Inc. Consolidated ..."). Fixed; old dev results discarded. Retrieval r0 dev recall 0.80 -> 0.84 (metrics-generated 1.00).
- 2026-11-11: embeddings done (Qwen3-Embedding-8B, 158 filings, 290 query texts). Dev recall: r0 0.843, r1 (BM25 + dense) 0.873.
- 2026-11-11 04:10: **dev v1 results** (kept as `runs/devv1-*`). Harness cut the wrong-answer rate (bare -> full: 27B 0.22 -> 0.04, 9B 0.39 -> 0.02, 2B 0.55 -> 0.02) but coverage collapsed (27B: 27%). Causes found: (1) 27B call 2 in JSON mode hit the 800-token limit in 37 of 70 calls (empty answers -> G4 failure); (2) call 1 hit 3000 tokens in 7% of calls; (3) the verifier compared PDF page positions with printed page numbers and rejected 7 of 15 correct 27B candidates; (4) it misread small digits at 110 dpi. Fixes: call 2 in plain text with citations parsed from the text, call 1 limit 4000, verifier prompt states page = PDF position and that code already checked quotes, images at 150 dpi. Judge calibration (E3) on 2,400 paper answers: agreement 0.79, false-correct rate 0.053.
- 2026-11-11 12:37: the Blackwell partition (`ice-bw-gpu`) exposes each RTX PRO 6000 as two halves of 47.4 GB. 9B and 2B run there. 27B bf16 (51 GB of weights) and gpt-oss-120b do not fit, so 80 GB jobs stay on `ice-gpu` (H100, H200, A100-80GB). `pace/submit.sh` adds the Blackwell partition only for the small models.
