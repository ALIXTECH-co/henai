"""Hardware-aware generation presets; these do not load model weights."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Preset:
    model: str
    width: int
    height: int
    steps: int
    guidance: float
    description: str

PRESETS = {
    "Fast preview (SDXL Turbo)": Preset(
        "SDXL Turbo", 512, 512, 1, 0.0, "Low-latency preview on a compatible CUDA GPU"),
    "Balanced (SDXL Turbo)": Preset(
        "SDXL Turbo", 768, 768, 3, 0.0, "Higher-resolution SDXL Turbo draft"),
    "Quality (FLUX schnell)": Preset(
        "FLUX.1-schnell", 1024, 1024, 4, 0.0, "Higher-resource FLUX generation"),
}

def get_preset(name: str) -> Preset:
    try:
        return PRESETS[name]
    except KeyError as exc:
        raise ValueError("Unknown preset") from exc
