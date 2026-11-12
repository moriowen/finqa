#!/bin/bash
# Generic job: serve one model with vLLM, run one command against it, stop (A21).
#   sbatch --export=ALL,MODEL=Qwen/Qwen3.5-9B,CMD="python -m finqa.cli pass1 --run all-9b-full --set all --arm r1" pace/job.sbatch
# Optional: SERVE_ARGS (extra vllm flags), MAXLEN (default 16384), NO_SERVE=1 (run CMD only).
#SBATCH -J finqa
#SBATCH -p ice-gpu
#SBATCH -N1 -c 8
#SBATCH --gres=gpu:1
#SBATCH --constraint=H100|H200|A100-80GB
#SBATCH --mem=96G
#SBATCH -t 4:00:00
#SBATCH -o pace/logs/%x-%j.out
source pace/env.sh
echo "node $(hostname) job $SLURM_JOB_ID start $(date)"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
df -h "${TMPDIR:-/tmp}" | tail -1
export FINQA_MODEL="$MODEL"
if [ -z "${NO_SERVE:-}" ]; then
  PORT=$(( 20000 + SLURM_JOB_ID % 20000 ))
  export FINQA_BASE_URL="http://localhost:$PORT/v1"
  t0=$(date +%s)
  python -c "from huggingface_hub import snapshot_download as s; p=s('$MODEL'); print('downloaded', p)"
  echo "download $(( $(date +%s) - t0 )) s, size $(du -sh "$HF_HOME" | cut -f1)"
  setsid vllm serve "$MODEL" --port "$PORT" --seed 0 --max-model-len "${MAXLEN:-16384}" \
      --gpu-memory-utilization 0.90 --max-num-seqs "${MAXSEQS:-64}" ${SERVE_ARGS:-} > "pace/logs/vllm-$SLURM_JOB_ID.log" 2>&1 &
  pid=$!
  trap 'kill -- -$pid 2>/dev/null || true; rm -rf "$HF_HOME"' EXIT
  for _ in $(seq 1 240); do
    curl -sf "localhost:$PORT/health" >/dev/null && break
    kill -0 "$pid" 2>/dev/null || { echo "server died"; tail -60 "pace/logs/vllm-$SLURM_JOB_ID.log"; exit 1; }
    sleep 5
  done
  curl -sf "localhost:$PORT/health" >/dev/null || { echo "server not up"; tail -60 "pace/logs/vllm-$SLURM_JOB_ID.log"; exit 1; }
  echo "server up $(( $(date +%s) - t0 )) s after start"
fi
eval "$CMD"
echo "done $(date)"
