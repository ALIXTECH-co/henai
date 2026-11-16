# Security policy

HENAI is an early developer prototype and **must not be exposed directly to the public internet**. It lacks authentication, content safety enforcement, per-user quotas, billing and abuse prevention.

Never commit tokens, cloud credentials, private images, or model access tokens. Report vulnerabilities privately to the repository owner rather than opening a public issue with exploit details.

The Gradio app binds to localhost by default. Future hosted versions require an authenticated frontend, isolated GPU workers, rate limits, monitoring and a data retention policy.
