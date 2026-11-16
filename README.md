# HENAI ✦ AI Image Studio

Local-first AI image generator built for XNVIDI Tech with Gradio and Hugging Face Diffusers.

## Features
- FLUX.1-schnell and SDXL Turbo text-to-image models
- Prompt, seed, resolution, steps and guidance controls
- PNG download with JSON generation metadata
- Local-only UI; no paid API or AWS required
- Lazy model loading: weights download on first generation

**Status:** Early developer release. Configuration tests are provided; image inference is not yet verified on the user's hardware. GPU performance and output quality are not guaranteed.

## Windows installation (PowerShell)

Install Python 3.11 and an NVIDIA CUDA-compatible driver first. Run `nvidia-smi` to check the GPU.

```powershell
git clone https://github.com/ALIXTECH-co/henai.git
cd henai
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
# Install the CUDA-compatible PyTorch wheel from https://pytorch.org/get-started/locally/
python -m pip install -r requirements.txt
python -m pytest -q
python app.py
```

Visit http://127.0.0.1:7860. Model weights download from Hugging Face on first generation and can require many GB.

## Model guidance

- **FLUX.1-schnell:** strong prompt adherence; start with 4 steps and guidance 0; substantial memory requirements. Check the Apache-2.0 model license.
- **SDXL Turbo:** fast drafts; start with 1–4 steps and guidance 0. Review Stability AI's model license for your intended use.

## Security
This app binds to localhost only. Do not expose it to the public internet without authentication and rate limits. No content moderation or user accounts are implemented. Generated files are saved to the ignored `outputs/` directory.

## Tests
`python -m pytest -q` tests configuration validation, not actual GPU generation.

## Roadmap
GPU smoke tests, model presets, inference diagnostics, image-to-image, stronger safety controls, and authenticated deployment.
