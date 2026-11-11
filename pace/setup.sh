#!/bin/bash
# One-time, on the ICE login node, from the project directory:  bash pace/setup.sh
source "$(dirname "$0")/env.sh"
[ -f "$VENV/bin/activate" ] || python3 -m venv "$VENV"
set +u; source "$VENV/bin/activate"; set -u
pip install -q --upgrade pip
pip install -q "vllm==0.32.0" hf_transfer
pip install -q pymupdf rank-bm25 numpy pandas tqdm openai python-dotenv pytest pillow
python -c "import vllm, torch, transformers; print('vllm', vllm.__version__, 'torch', torch.__version__, 'transformers', transformers.__version__)"
python -c "from vllm import ModelRegistry; a=ModelRegistry.get_supported_archs(); print('Qwen3_5ForConditionalGeneration' in a, 'GptOssForCausalLM' in a)"
echo SETUP-OK
