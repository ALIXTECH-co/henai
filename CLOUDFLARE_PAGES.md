# Deploy HENAI web preview on Cloudflare Pages

This deploys **only the static UI** from `site/`. It cannot run Python Diffusers or generate AI images without a separate GPU backend.

1. Visit https://dash.cloudflare.com/ and select **Workers & Pages → Create application → Pages → Connect to Git**.
2. Select GitHub repository `ALIXTECH-co/henai`.
3. Project name: `henai` (or another available name).
4. Production branch: `main`.
5. Framework preset: **None**.
6. Build command: `exit 0` (or leave blank if permitted).
7. Build output directory: `site`.
8. Select **Save and Deploy**.

Cloudflare will provide an actual `*.pages.dev` URL after successful deployment. Do not assume `henai.pages.dev` is available before Cloudflare confirms it.

## What this tests

Page load, layout, mobile responsiveness, GitHub-to-Cloudflare deployment and the public product concept. **It does not test model quality, image generation time, or unit economics.** For those, run an actual GPU inference benchmark first. No fake images or misleading generation claims are included.
