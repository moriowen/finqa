# Sourced by setup.sh and every job (A14, A21).
# Scratch is nearly full from other projects, so model weights go to the node-local disk of each job.
set -eo pipefail
PROJECT_DIR="${PROJECT_DIR:-$HOME/scratch/finqa}"
VENV="${VENV:-$HOME/scratch/finqa-venv}"
export PIP_CACHE_DIR="${PIP_CACHE_DIR:-$HOME/scratch/pip-cache}"
if [ -n "${SLURM_JOB_ID:-}" ] && [ -z "${HF_HOME:-}" ]; then
  LOCAL="${TMPDIR:-/tmp}"
  export HF_HOME="$LOCAL/finqa-hf-$SLURM_JOB_ID"
fi
export HF_HOME="${HF_HOME:-$HOME/scratch/finqa-hf}"
export HF_XET_HIGH_PERFORMANCE=1
export PYTHONUNBUFFERED=1 TOKENIZERS_PARALLELISM=false
export FINQA_ROOT="$PROJECT_DIR"
if command -v module >/dev/null 2>&1; then module load python/3.12.5 >/dev/null 2>&1 || true; fi
[ -f "$VENV/bin/activate" ] && source "$VENV/bin/activate"
set -u
cd "$PROJECT_DIR"
mkdir -p pace/logs runs

# per-job vLLM compile cache on node-local disk: parallel jobs sharing it on NFS crashed with "Stale file handle"
export VLLM_CACHE_ROOT="${TMPDIR:-/tmp}/vllm-cache-${SLURM_JOB_ID:-0}"
