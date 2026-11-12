#!/bin/bash
# Latency benchmark: answering model on GPU 0, verifier (Gemma 4 12B) on GPU 1, then finqa.bench.
#   sbatch --export=ALL,MODEL=Qwen/Qwen3.5-9B,TAG=9b pace/bench.sbatch
#SBATCH -J bench
#SBATCH -p ice-bw-gpu,ice-gpu
#SBATCH --constraint=RTX-Pro-Blackwell
#SBATCH -N1 -c 16
#SBATCH --gres=gpu:2
#SBATCH --mem=160G
#SBATCH -t 2:00:00
#SBATCH -o pace/logs/%x-%j.out
source pace/env.sh
echo "node $(hostname) job $SLURM_JOB_ID start $(date)"
nvidia-smi -L
VMODEL=google/gemma-4-12B-it
P1=$(( 20000 + SLURM_JOB_ID % 20000 )); P2=$(( P1 + 1 ))
python -c "from huggingface_hub import snapshot_download as s; s('$MODEL'); s('$VMODEL')"
IFS=',' read -ra G <<< "${CUDA_VISIBLE_DEVICES:-0,1}"
CUDA_VISIBLE_DEVICES=${G[0]} VLLM_CACHE_ROOT="$VLLM_CACHE_ROOT/a" setsid vllm serve "$MODEL" --port $P1 --seed 0 --max-model-len 32768 \
  --gpu-memory-utilization 0.90 --max-num-seqs 64 > pace/logs/vllm-$SLURM_JOB_ID-a.log 2>&1 &
pa=$!
CUDA_VISIBLE_DEVICES=${G[1]} VLLM_CACHE_ROOT="$VLLM_CACHE_ROOT/b" setsid vllm serve "$VMODEL" --port $P2 --seed 0 --max-model-len 24576 \
  --gpu-memory-utilization 0.90 --max-num-seqs 64 --limit-mm-per-prompt '{"image":4}' > pace/logs/vllm-$SLURM_JOB_ID-b.log 2>&1 &
pb=$!
trap 'kill -- -$pa -$pb 2>/dev/null || true; rm -rf "$HF_HOME"' EXIT
for _ in $(seq 1 240); do
  curl -sf localhost:$P1/health >/dev/null && curl -sf localhost:$P2/health >/dev/null && break
  kill -0 $pa 2>/dev/null && kill -0 $pb 2>/dev/null || { echo "server died"; tail -40 pace/logs/vllm-$SLURM_JOB_ID-*.log; exit 1; }
  sleep 5
done
echo "servers up $(date)"
export FINQA_BASE_URL="http://localhost:$P1/v1" FINQA_MODEL="$MODEL" FINQA_STREAM=1
export VERIFIER_URL="http://localhost:$P2/v1" VERIFIER_MODEL="$VMODEL"
python -m finqa.bench --n 20 --out runs/bench/$TAG.jsonl
echo "done $(date)"
