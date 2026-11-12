#!/bin/bash
# The GPU jobs behind every result, in order. Run from ~/scratch/finqa on PACE ICE.
# Each job serves one model with vLLM (pace/job.sbatch), runs one command against it, and stops.
# Every step appends JSONL under runs/ and skips finished rows, so a stopped job can be resubmitted.
#   bash pace/experiments.sh <step>
set -euo pipefail
cd "$(dirname "$0")/.."
GPU="H100|H200|A100-80GB|A100-40GB|L40S|A40|RTX-Pro-Blackwell"
job() {  # job NAME MODEL "CMD" [extra vllm args]
  sbatch --parsable -J "$1" -p ice-gpu,ice-bw-gpu --constraint="$GPU" -t 4:00:00 \
    --export=ALL,MODEL="$2",CMD="$3",SERVE_ARGS="${4:-}",MAXLEN=32768 pace/job.sbatch
}
P1="python -m finqa.cli pass1 --set all --arm r1"
VL='--limit-mm-per-prompt {"image":4}'

case "${1:?step}" in
  embed)   # page and question vectors for retrieval
    job emb Qwen/Qwen3-Embedding-8B "python -m finqa.cli embed --set all" "--runner pooling" ;;
  answer)  # experiment 1 (filing given) and the unanswerable set, per model size
    for m in 2B 9B; do s=$(echo $m | tr A-Z a-z)
      job q$s Qwen/Qwen3.5-$m "$P1 --run all-$s-full && $P1 --run all-$s-bare --mode bare && $P1 --run all-$s-oracle --mode oracle && $P1 --run unans-$s-full --unans && $P1 --run unans-$s-bare --unans --mode bare"
    done
    job q27b Qwen/Qwen3.5-27B-FP8 "$P1 --run all-27b-full && $P1 --run all-27b-bare --mode bare && $P1 --run all-27b-oracle --mode oracle && $P1 --run unans-27b-full --unans && $P1 --run unans-27b-bare --unans --mode bare" ;;
  find)    # experiments 2 and 3: filing not given; --routes picks whose router output is used
    job q27b-route Qwen/Qwen3.5-27B-FP8 "python -m finqa.cli pass0 --what route --set all && $P1 --run pathb-27b-full --path B"
    job q9b-route Qwen/Qwen3.5-9B "python -m finqa.cli pass0 --what route --set all --out route_9b.jsonl && $P1 --run pathb-9b-full --path B --routes route_9b.jsonl && $P1 --run pathb-9b-r27 --path B --routes route.jsonl" ;;
  verify)  # Gemma 4 12B checks every full-pipeline answer; bare runs are finalized without it
    job verify google/gemma-4-12B-it "for r in runs/all-*-full runs/all-*-oracle runs/unans-*-full runs/pathb-*; do python -m finqa.cli pass2 --run \$(basename \$r) --suffix _gemma4; done; for r in runs/*-bare; do python -m finqa.cli finalize --run \$(basename \$r); done" "$VL" ;;
  judge)   # gpt-oss-20b grades against the gold answers; first calibrated on the paper's 2,400 human labels
    job judge openai/gpt-oss-20b "python -m finqa.evals.judge paper --out _oss20b; for r in runs/all-* runs/unans-* runs/pathb-*; do n=\$(basename \$r); if [[ \$n == *bare ]]; then python -m finqa.evals.judge run --run \$n --src '' --out _oss20b; else python -m finqa.evals.judge run --run \$n --src _gemma4 --out _gemma4_oss20b; fi; done" ;;
  latency) # one question at a time and a batch of 20, every stage timed (two GPUs: model + verifier)
    sbatch -J bench-9b --export=ALL,MODEL=Qwen/Qwen3.5-9B,TAG=9b pace/bench.sbatch
    sbatch -J bench-27b --export=ALL,MODEL=Qwen/Qwen3.5-27B-FP8,TAG=27b pace/bench.sbatch ;;
  *) echo "steps: embed answer find verify judge latency"; exit 1 ;;
esac
