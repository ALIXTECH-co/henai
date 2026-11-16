"""Local image inference with lazy model loading and reproducible seeds."""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
import secrets
from typing import Literal

ModelName = Literal["FLUX.1-schnell", "SDXL Turbo"]
MODELS = {
    "FLUX.1-schnell": "black-forest-labs/FLUX.1-schnell",
    "SDXL Turbo": "stabilityai/sdxl-turbo",
}

@dataclass(frozen=True)
class Settings:
    model: ModelName
    width: int
    height: int
    steps: int
    guidance: float
    seed: int

def validate(model: str, width: int, height: int, steps: int, guidance: float, seed: int) -> Settings:
    if model not in MODELS:
        raise ValueError("Unsupported model")
    if width not in range(256, 1537, 64) or height not in range(256, 1537, 64):
        raise ValueError("Width and height must be multiples of 64 between 256 and 1536")
    if not 1 <= steps <= 50:
        raise ValueError("Steps must be between 1 and 50")
    if not 0 <= guidance <= 20:
        raise ValueError("Guidance must be between 0 and 20")
    if seed < -1 or seed > 2**32 - 1:
        raise ValueError("Seed out of range")
    return Settings(model, width, height, steps, guidance, secrets.randbelow(2**32) if seed == -1 else seed)

@lru_cache(maxsize=1)
def load_pipeline(model: ModelName):
    import torch
    from diffusers import FluxPipeline, AutoPipelineForText2Image
    if not torch.cuda.is_available():
        raise RuntimeError("A CUDA NVIDIA GPU is required. No cloud service will be used.")
    if model == "FLUX.1-schnell":
        pipe = FluxPipeline.from_pretrained(MODELS[model], torch_dtype=torch.bfloat16)
    else:
        pipe = AutoPipelineForText2Image.from_pretrained(
            MODELS[model], torch_dtype=torch.float16, variant="fp16")
    pipe.enable_model_cpu_offload()
    return pipe

def generate(prompt: str, negative_prompt: str, settings: Settings):
    import torch
    if not prompt.strip():
        raise ValueError("Please enter a prompt")
    pipe = load_pipeline(settings.model)
    generator = torch.Generator(device="cpu").manual_seed(settings.seed)
    kwargs = dict(prompt=prompt.strip(), width=settings.width, height=settings.height,
                  num_inference_steps=settings.steps, guidance_scale=settings.guidance,
                  generator=generator)
    if settings.model == "SDXL Turbo":
        kwargs["negative_prompt"] = negative_prompt.strip() or None
    return pipe(**kwargs).images[0]
