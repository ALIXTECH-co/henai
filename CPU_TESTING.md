# Real CPU testing without renting a GPU

GitHub Actions can run a short-lived CPU diffusion smoke test, and upload a generated PNG as a workflow artifact.

1. Open https://github.com/ALIXTECH-co/henai/actions/workflows/cpu-smoke.yml
2. Select **Run workflow** on the `main` branch.
3. Wait for the job to complete, then download the `henai-cpu-smoke-image` artifact.

The test uses the publicly available `google/ddpm-cifar10-32` unconditional diffusion model. It generates a **real 32x32 image on CPU**, but **does not accept text prompts** and is **not a useful quality test** for FLUX or SDXL. It only proves that CPU diffusion inference can execute. The workflow may download hundreds of MB of dependencies and model files and consume GitHub Actions minutes.

For meaningful prompt-to-image quality testing, run a real text-to-image model on suitable hardware. The existing HENAI application still requires NVIDIA CUDA and is not served by GitHub Pages.

GitHub Actions is a CI system, not a persistent public CPU backend. Do not turn workflow dispatch into an unauthenticated user generation service.
