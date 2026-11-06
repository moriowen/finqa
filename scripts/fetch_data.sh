#!/bin/sh
# Download the FinanceBench dataset at the commit that this project uses.
set -eu
COMMIT=cc39aeb4afdf33909ee1412188bf89035950c2eb
DEST="$(dirname "$0")/../data/financebench"
if [ ! -d "$DEST/.git" ]; then
  git clone --depth 1 https://github.com/patronus-ai/financebench.git "$DEST"
fi
test "$(git -C "$DEST" rev-parse HEAD)" = "$COMMIT" || { echo "Unexpected dataset commit" >&2; exit 1; }
