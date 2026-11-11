#!/bin/bash
# CPU job for steps that need no model: the autopilot, metrics, publishing.
#   sbatch --export=ALL,CMD="python -m finqa.evals.autopilot" pace/cpu.sbatch
#SBATCH -J finqa-cpu
#SBATCH -p ice-cpu
#SBATCH -N1 -c 4
#SBATCH --mem=16G
#SBATCH -t 1:00:00
#SBATCH -o pace/logs/%x-%j.out
source pace/env.sh
echo "node $(hostname) job $SLURM_JOB_ID start $(date)"
eval "$CMD"
echo "done $(date)"
