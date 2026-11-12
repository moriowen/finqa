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
- 2026-11-11 12:50: 27B waits for an 80 GB GPU; user decision: keep it queued, continue with the rest. New stage `submit.sh now`: 2B and 9B final pass 1 on any GPU now (arm r1 from the recall rule, glossary on and off); 27B dev and final, verifier, judge and publishing wait for 80 GB GPUs. Verifier thinking and call-1 images are OFF in the final runs (both still measured on dev).
- 2026-11-11 13:00: 2B dev 2 showed two more harness problems: (1) G4 flagged numbers that come from the checked quotes ("Flight 610", "364 Day Credit Agreement", vote counts) and page references in the answer; (2) 2B degenerated in call 1 (endless value lists, 17 calls hit 4000 tokens). Fixes: numbers inside checked quotes are allowed, page/note references are skipped, the call-1 schema caps values at 12 and names at 64 characters, repeated names get a suffix. 2B and 9B dev runs rerun with the fixes inside the final jobs.
- 2026-11-11 14:00: user decision (A23): verifier for the 2B/9B runs = `google/gemma-4-12B-it` (other family, fits 47 GB; a Phi-4 job was cancelled before it ran, user rejected Microsoft models); judge = `openai/gpt-oss-20b`, calibrated on the 2,400 paper labels. Results use file suffixes `_gemma4` and `_gemma4_oss20b` / `_oss20b`, so they never mix with 27B / 120b results. Every output row now has a `models` field (answering model, verifier) next to `provenance`.

### 2026-11-11: 27B dropped (user decision)
The 27B jobs waited more than a day for an 80 GB GPU. The user chose to skip 27B. Cancelled jobs: q27-dev 6962456, q27-all 6962502, v27 6962503, judge (gpt-oss-120b) 6962504, publish 6962505. The experiment now compares Qwen3.5 2B and 9B only. The verifier is Gemma 4 12B and the judge is gpt-oss-20b, both on the Blackwell partition. A larger answer model (27B or more), a larger verifier and the 120b judge go to future scope. Dev round 1 27B results (already graded) stay in the interim report as a reference point only.

### 2026-11-11: 27B back in, as FP8 on Blackwell (user request)
- First try: Qwen3.5-27B bf16 with tensor parallel 2 on two Blackwell GPUs. Failed with an NCCL error: ICE Blackwell GPUs are MIG partitions (47 GB each), and NCCL cannot join two MIG instances.
- Switched to the official `Qwen/Qwen3.5-27B-FP8` (31 GB), one partition. Six pass-1 runs in parallel jobs (full, bare, oracle, unans full, unans bare, Path B). Two crashed at server start with "Stale file handle" from a shared vLLM compile cache on NFS. Fix: `VLLM_CACHE_ROOT` on node-local disk (`pace/env.sh`), reran.
- Then Gemma 4 12B verifier and gpt-oss-20b judge, same as 2B/9B. Official config stays 9B full (dev wrong count 5 vs 10 for 27B).

### 2026-11-11: experiments 2 and 3, latency benchmark (user request)
- Results are organized as experiment 1 (filing given: 2B, 9B, 27B), experiment 2 (filing not given: 9B, 27B), experiment 3 (router vs reader: 9B and 27B in a 2x2 grid; the cell "9B router, 27B reader" was not run), and a latency benchmark. 2B is out of experiments 2 and 3.
- 9B router output: `runs/pass0/route_9b.jsonl`. Runs `pathb-9b-full` (9B routes, 9B reads) and `pathb-9b-r27` (27B routes, 9B reads). `--routes` on pass1 selects the router output.
- Latency: `finqa/bench.py` + `pace/bench.sbatch` (answering model and Gemma on two MIG partitions, streaming for time to first token). 20 dev questions, single and batch. Results in `runs/bench/`.

### 2026-11-11: cleanup before the code walkthrough
Removed code that no result depends on: `finqa/evals/interim.py`, `dev_analysis.py`, `autopilot.py`, `finqa/smoke.py`, `pace/smoke/`, `pace/cpu.sbatch`, `pace/submit.sh` (replaced by `pace/experiments.sh`, which lists the jobs actually run), the old hand-drawn architecture diagram (replaced by `docs/diagrams/system-flow.svg`). All of it stays in git history.
