# HENAI deployment readiness

**Do not deploy publicly yet.** The application is a single-user development prototype. It has no user accounts, billing, content moderation, quotas, or abuse controls. The Dockerfile is a packaging baseline, not a production GPU deployment image.

## Acceptance gates before spending AWS credits
1. Verify the desired model's license permits the intended commercial use.
2. Run a real CUDA GPU smoke test and record peak VRAM, latency, quality and failures.
3. Add authenticated API access, per-user quotas, request size limits, content moderation, and abuse reporting.
4. Separate the web frontend from a GPU worker; place the worker behind a private queue.
5. Set AWS budget alerts, hard application quotas, and an explicit stop procedure.
6. Ensure generated images and metadata have a documented retention/deletion policy.
7. Review privacy policy, terms, payment processor requirements, and image model attribution.
8. Load test, secure storage, secrets, TLS, logs and health checks.

## GPU smoke test (only on a GPU host)
Install a CUDA-compatible PyTorch build following https://pytorch.org/get-started/locally/ and requirements.txt. Check `python -c "import torch; print(torch.cuda.is_available())"` is True. Start with SDXL Turbo, 512x512, 1 step, guidance 0. Then try FLUX.1-schnell if the GPU has sufficient resources.

## AWS architecture for a future paid service
Browser -> authenticated web/API service -> durable job queue -> GPU worker -> private object storage -> signed download URL. Use separate billing and usage ledger. Do not expose Gradio directly to customers or put AWS keys in the repo.

## Cost model
Per-image GPU compute cost = (instance hourly rate * average job seconds / 3600) plus storage, transfer, queue, idle capacity and payment fees. Benchmark before pricing; do not promise profit from unmeasured costs.
