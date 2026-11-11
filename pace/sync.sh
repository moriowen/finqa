#!/bin/bash
# Mac -> ICE: code, PDFs, parsed pages.  Pull results:  ./pace/sync.sh pull
set -euo pipefail
cd "$(dirname "$0")/.."
source .env 2>/dev/null || true
H="${ICE_USER:?set ICE_USER in .env}@login-ice.pace.gatech.edu"
if [ "${1:-}" = pull ]; then
  rsync -az "$H:~/scratch/finqa/runs/" runs/
  rsync -az "$H:~/scratch/finqa/pace/logs/" pace/logs/
  rsync -az "$H:~/scratch/finqa/artifacts/vectors/" artifacts/vectors/ 2>/dev/null || true
else
  rsync -az --exclude '.git' --exclude '.venv' --exclude '__pycache__' --exclude 'runs/' --exclude 'pace/logs/' \
    --exclude 'data/financebench/.git' --exclude 'data/financebench/results' ./ "$H:~/scratch/finqa/"
  rsync -az data/financebench/results/ "$H:~/scratch/finqa/data/financebench/results/"
  rsync -az --ignore-existing runs/ "$H:~/scratch/finqa/runs/"
fi
