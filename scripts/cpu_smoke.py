"""Generate one real image on CPU with a small diffusion model.

Run: python scripts/cpu_smoke.py
This script downloads model weights on first run and never exposes a web service.
"""
import os
from pathlib import Path

def main():
    import torch
    from diffusers import DDPMPipeline

    model_id = os.environ.get("HENAI_CPU_MODEL", "google/ddpm-cifar10-32")
    output = Path(os.environ.get("HENAI_CPU_OUTPUT", "outputs/cpu-smoke.png"))
    output.parent.mkdir(parents=True, exist_ok=True)
    print(f"Loading CPU diffusion model: {model_id}", flush=True)
    pipe = DDPMPipeline.from_pretrained(model_id).to("cpu")
    generator = torch.Generator(device="cpu").manual_seed(42)
    image = pipe(batch_size=1, generator=generator, num_inference_steps=20).images[0]
    image.save(output)
    print(f"Saved actual generated image: {output}", flush=True)
    print("NOTE: This is an unconditional 32x32 model used only to verify CPU inference.")
    print("It is NOT a text-to-image quality benchmark or a production HENAI model.")

if __name__ == "__main__":
    main()
