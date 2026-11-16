# Publish HENAI frontend with GitHub Pages

GitHub Pages hosts **static HTML/CSS/JS only**. It does not run Python, FastAPI, Gradio, Diffusers, background workers, or GPUs. GitHub paid plans do not change that.

A Pages workflow is committed at `.github/workflows/pages.yml`.

## Activate

1. Go to https://github.com/ALIXTECH-co/henai/settings/pages
2. Under **Build and deployment**, choose **Source: GitHub Actions**.
3. Open https://github.com/ALIXTECH-co/henai/actions/workflows/pages.yml and select **Run workflow** if it did not start automatically.
4. When deployment succeeds, the expected project address is https://alixtech-co.github.io/henai/ . Confirm the actual URL in the workflow deployment; this is not a verified live link yet.

The frontend will explicitly indicate that inference is unavailable until a GPU backend is connected. Do not sell image generation from this preview.

## Full-stack options

To generate images, deploy a GPU-capable backend on a GPU server or compatible inference service and connect the frontend to an authenticated API. GitHub Actions runners are CI jobs, not reliable always-on inference hosting; using them as a public image-generation backend would be insecure and unsuitable for customer traffic.
