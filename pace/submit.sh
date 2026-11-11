#!/bin/bash
# Submit one stage of the experiment plan as a dependency chain (A21). From ~/scratch/finqa on ICE:
#   bash pace/submit.sh dev      # dev split: embeddings, pass 0, sweep runs, verifier, judge, E3
#   bash pace/submit.sh final    # all questions with the chosen configuration (set ARM, GLOSS, THINK)
set -euo pipefail
cd "$(dirname "$0")/.."
STAGE="${1:?dev or final}"
BIG="H100|H200|A100-80GB"                          # 27B bf16 and gpt-oss-120b need 80 GB
ANY="H100|H200|A100-80GB|A100-40GB|L40S|A40"       # 2B, 9B, embedding
Q2=Qwen/Qwen3.5-2B; Q9=Qwen/Qwen3.5-9B; Q27=Qwen/Qwen3.5-27B
JUDGE=openai/gpt-oss-120b; EMB=Qwen/Qwen3-Embedding-8B
VL='--limit-mm-per-prompt {"image":8}'
sub() {  # sub NAME CONSTRAINT MODEL "CMD" [DEPS] [EXTRA SERVE ARGS] [MAXLEN] [TIME]
  local dep=""; [ -n "${5:-}" ] && dep="--dependency=afterany:$5"
  sbatch --parsable -J "$1" --constraint="$2" -t "${8:-4:00:00}" $dep \
    --export=ALL,MODEL="$3",CMD="$4",SERVE_ARGS="${6:-}",MAXLEN="${7:-32768}" pace/job.sbatch
}
P1="python -m finqa.cli pass1"
if [ "$STAGE" = dev ]; then
  e=$(sub emb "$ANY" $EMB "python -m finqa.cli embed --set all" "" "--runner pooling" 8192 2:00:00)
  a=$(sub q27-dev "$BIG" $Q27 "python -m finqa.cli pass0 --what plan --set all && python -m finqa.cli pass0 --what route --set all && \
$P1 --run dev-27b-full-r0 --set dev && $P1 --run dev-27b-bare-r0 --set dev --mode bare && \
$P1 --run dev-27b-oracle --set dev --mode oracle && $P1 --run dev-27b-oracle-img --set dev --mode oracle --images" "" "$VL")
  b=$(sub q9-dev "$ANY" $Q9 "$P1 --run dev-9b-full-r0 --set dev && $P1 --run dev-9b-bare-r0 --set dev --mode bare" "" "$VL")
  c=$(sub q2-dev "$ANY" $Q2 "$P1 --run dev-2b-full-r0 --set dev && $P1 --run dev-2b-full-r0-gloss --set dev --glossary && \
$P1 --run dev-2b-bare-r0 --set dev --mode bare" "" "$VL")
  V="python -m finqa.cli pass2"
  v=$(sub v27-dev "$BIG" $Q27 "for r in dev-27b-full-r0 dev-27b-oracle dev-27b-oracle-img dev-9b-full-r0 dev-2b-full-r0 dev-2b-full-r0-gloss; do $V --run \$r; done; \
for r in dev-27b-full-r0 dev-9b-full-r0 dev-2b-full-r0; do $V --run \$r --thinking; done; \
for r in dev-27b-bare-r0 dev-9b-bare-r0 dev-2b-bare-r0; do python -m finqa.cli finalize --run \$r; done" "$a:$b:$c" "$VL")
  J="python -m finqa.evals.judge run"
  j=$(sub judge-dev "$BIG" $JUDGE "python -m finqa.evals.judge paper; \
for r in dev-27b-full-r0 dev-27b-bare-r0 dev-27b-oracle dev-27b-oracle-img dev-9b-full-r0 dev-9b-bare-r0 dev-2b-full-r0 dev-2b-full-r0-gloss dev-2b-bare-r0; do $J --run \$r; done; \
for r in dev-27b-full-r0 dev-9b-full-r0 dev-2b-full-r0; do $J --run \$r --thinking; done" "$v" "" 32768 6:00:00)
  echo "emb $e | q27 $a | q9 $b | q2 $c | verifier $v | judge $j"
elif [ "$STAGE" = final ]; then
  ARM="${ARM:-r0}"; G="${GLOSS:+--glossary}"; T="${THINK:+--thinking}"
  run() { echo "$P1 --run all-$1-full --set all --arm $ARM $G && $P1 --run all-$1-bare --set all --mode bare --arm $ARM && \
$P1 --run all-$1-oracle --set all --mode oracle $G && $P1 --run unans-$1-full --set all --unans --arm $ARM $G && \
$P1 --run unans-$1-bare --set all --unans --mode bare --arm $ARM"; }
  a=$(sub q27-all "$BIG" $Q27 "$(run 27b) && $P1 --run pathb-27b-full --set all --path B --arm $ARM $G" "${DEP:-}" "$VL" 32768 8:00:00)
  b=$(sub q9-all "$ANY" $Q9 "$(run 9b)" "${DEP:-}" "$VL" 32768 8:00:00)
  c=$(sub q2-all "$ANY" $Q2 "$(run 2b)" "${DEP:-}" "$VL" 32768 8:00:00)
  RUNS="all-27b-full all-27b-oracle unans-27b-full pathb-27b-full all-9b-full all-9b-oracle unans-9b-full all-2b-full all-2b-oracle unans-2b-full"
  BARE="all-27b-bare unans-27b-bare all-9b-bare unans-9b-bare all-2b-bare unans-2b-bare"
  v=$(sub v27-all "$BIG" $Q27 "for r in $RUNS; do python -m finqa.cli pass2 --run \$r $T; done; for r in $BARE; do python -m finqa.cli finalize --run \$r; done" "$a:$b:$c" "$VL" 32768 8:00:00)
  j=$(sub judge-all "$BIG" $JUDGE "for r in $RUNS $BARE; do python -m finqa.evals.judge run --run \$r $T; done" "$v" "" 32768 8:00:00)
  echo "q27 $a | q9 $b | q2 $c | verifier $v | judge $j"
fi
