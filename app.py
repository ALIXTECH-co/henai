"""HENAI local Gradio UI. Model weights download only when generation is requested."""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import threading
import uuid
import gradio as gr
from henai.core import generate, validate

OUTPUT_DIR = Path(os.environ.get("HENAI_OUTPUT_DIR", "outputs"))
GENERATION_LOCK = threading.Lock()

def create_image(prompt, negative_prompt, model, width, height, steps, guidance, seed):
    if not GENERATION_LOCK.acquire(blocking=False):
        raise gr.Error("A generation is already running. Please wait.")
    try:
        try:
            settings = validate(model, int(width), int(height), int(steps), float(guidance), int(seed))
            image = generate(prompt, negative_prompt, settings)
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            name = f"henai-{uuid.uuid4().hex[:12]}"
            path = OUTPUT_DIR / f"{name}.png"
            image.save(path)
            metadata = dict(prompt=prompt, negative_prompt=negative_prompt, model=model,
                            width=settings.width, height=settings.height, steps=settings.steps,
                            guidance=settings.guidance, seed=settings.seed,
                            generated_at=datetime.now(timezone.utc).isoformat())
            (OUTPUT_DIR / f"{name}.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
            return image, str(path), f"Seed: {settings.seed} · Model: {model}"
        except Exception as exc:
            raise gr.Error(f"Generation failed: {exc}") from exc
    finally:
        GENERATION_LOCK.release()

with gr.Blocks(title="HENAI · AI Image Studio", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# HENAI ✦ AI Image Studio\nCreate images locally with open-weight diffusion models. No paid API required.")
    with gr.Row():
        with gr.Column(scale=2):
            prompt = gr.Textbox(label="Describe your image", lines=5, placeholder="Cinematic portrait of an astronaut in a glowing rainforest…")
            negative = gr.Textbox(label="Negative prompt (SDXL Turbo only)", lines=2)
            model = gr.Dropdown(choices=["FLUX.1-schnell", "SDXL Turbo"], value="FLUX.1-schnell", label="Model")
            with gr.Row():
                width = gr.Slider(256, 1536, value=1024, step=64, label="Width")
                height = gr.Slider(256, 1536, value=1024, step=64, label="Height")
            with gr.Row():
                steps = gr.Slider(1, 50, value=4, step=1, label="Inference steps")
                guidance = gr.Slider(0, 20, value=0, step=0.5, label="Guidance")
                seed = gr.Number(value=-1, precision=0, label="Seed (-1 = random)")
            button = gr.Button("Generate image", variant="primary")
        with gr.Column(scale=3):
            result = gr.Image(label="Generated image", type="pil", interactive=False)
            download = gr.File(label="Download PNG")
            status = gr.Textbox(label="Generation details", interactive=False)
    gr.Markdown("**Hardware:** CUDA NVIDIA GPU required. FLUX may need substantial VRAM/RAM and disk. First generation downloads model weights. Review model licenses before commercial use.")
    button.click(create_image, [prompt, negative, model, width, height, steps, guidance, seed],
                 [result, download, status], concurrency_limit=1)

if __name__ == "__main__":
    demo.queue(max_size=5).launch(server_name="127.0.0.1", server_port=7860, share=False)
