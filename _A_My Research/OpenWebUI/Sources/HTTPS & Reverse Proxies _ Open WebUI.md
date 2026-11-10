---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

HTTPS & Reverse Proxies / Open WebUI
[Skip to main content](https://docs.openwebui.com/reference/https#__docusaurus_skipToContent_fallback)
[Open WebUI](https://docs.openwebui.com/) [Blog](https://openwebui.com/blog)
[GitHub](https://github.com/open-webui/open-webui) [Discord](https://discord.com/invite/5rJgQTnV4s)

```

```

[Open WebUI](https://docs.openwebui.com/)
\* [Blog](https://openwebui.com/blog)
\* [GitHub](https://github.com/open-webui/open-webui)
\* [Discord](https://discord.com/invite/5rJgQTnV4s)
← Back to main menu
\* [🏡 Home](https://docs.openwebui.com/)
\* [🚀 Getting Started](https://docs.openwebui.com/getting-started/)
\* [📖 Reference](https://docs.openwebui.com/reference/)
\* [Environment Variable Configuration](https://docs.openwebui.com/reference/env-configuration)
\* [HTTPS & Reverse Proxies](https://docs.openwebui.com/reference/https/)
\* [HTTPS using Cloudflare Tunnel](https://docs.openwebui.com/reference/https/cloudflare-tunnel)
\* [HTTPS using ngrok](https://docs.openwebui.com/reference/https/ngrok)
\* [HTTPS using Tailscale](https://docs.openwebui.com/reference/https/tailscale)
\* [HTTPS using Nginx](https://docs.openwebui.com/reference/https/nginx)
\* [HTTPS using HAProxy](https://docs.openwebui.com/reference/https/haproxy)
\* [HTTPS using Caddy](https://docs.openwebui.com/reference/https/caddy)
\* [Monitoring](https://docs.openwebui.com/reference/monitoring/)
\* [Backend-Controlled API Flow](https://docs.openwebui.com/reference/api-flow)
\* [Database Schema](https://docs.openwebui.com/reference/database-schema)
\* [Network Diagrams](https://docs.openwebui.com/reference/network-diagrams)
\* [API Endpoints](https://docs.openwebui.com/reference/api-endpoints)
\* [⭐ Features](https://docs.openwebui.com/features/)
\* [🛠 Troubleshooting](https://docs.openwebui.com/troubleshooting/)
\* [🏢 Open WebUI for Enterprise](https://docs.openwebui.com/enterprise/)
\* [🎓 Tutorials](https://docs.openwebui.com/tutorials/)
\* [❓ FAQ](https://docs.openwebui.com/faq)
\* [🛣 Roadmap](https://docs.openwebui.com/roadmap)
\* [🛡 Security Policy](https://docs.openwebui.com/security)
\* [🤝 Contributing](https://docs.openwebui.com/contributing)
\* [💖 Sponsorships](https://docs.openwebui.com/sponsorships)
\* [🎨 Brand Guidelines](https://docs.openwebui.com/brand)
\* [⚖ Open WebUI License](https://docs.openwebui.com/license)
\* [🎯 Our Mission](https://docs.openwebui.com/mission)
\* [👥 Our Team](https://docs.openwebui.com/team)
\* [📖 Reference](https://docs.openwebui.com/reference/)
\* HTTPS & Reverse Proxies
On this page

### HTTPS & Reverse Proxies

**Secure your Open WebUI deployment with TLS encryption, reverse proxies, or managed tunnels.**
HTTPS encrypts all traffic between users and Open WebUI, protecting chat history, credentials, and uploaded files. It is also **required** for browser features like Voice Calls, which need a secure context to access the microphone.
Voice Calls require HTTPS
Modern browsers block microphone access on non-HTTPS origins. **Voice Calls will not work** over plain http:// unless you are on localhost .

#### Choose your approach

| Method | Best for | TLS management |
| --- | --- | --- |
| [Cloudflare Tunnel](https://docs.openwebui.com/reference/https/cloudflare-tunnel) | Production without open ports | Automatic (Cloudflare edge) |
| [ngrok](https://docs.openwebui.com/reference/https/ngrok) | Development and testing | Automatic (ngrok edge) |
| [Tailscale](https://docs.openwebui.com/reference/https/tailscale) | Private access across devices | Automatic (tailscale serve) |
| [Nginx](https://docs.openwebui.com/reference/https/nginx) | Self-hosted production with full control | Manual or Let's Encrypt |
| [Caddy](https://docs.openwebui.com/reference/https/caddy) | Self-hosted production, minimal config | Automatic (Let's Encrypt) |
| [HAProxy](https://docs.openwebui.com/reference/https/haproxy) | High-availability / load balancing | Manual or Let's Encrypt |
| **Cloud load balancers** | AWS ALB, GCP LB, Azure App Gateway | Managed by cloud provider |

#### Quick recommendations

```
*   **Just want HTTPS fast?**  Use [Cloudflare Tunnel](https://docs.openwebui.com/reference/https/cloudflare-tunnel) (production) or [ngrok](https://docs.openwebui.com/reference/https/ngrok) (development). No certificates to manage, no ports to open.
*   **Running a reverse proxy already?**  Add [Caddy](https://docs.openwebui.com/reference/https/caddy) for automatic certs or [Nginx](https://docs.openwebui.com/reference/https/nginx) for maximum control.
*   **Need load balancing?**  Use [HAProxy](https://docs.openwebui.com/reference/https/haproxy) or your cloud provider's load balancer.
```

#### Key configuration notes

Regardless of which approach you choose, keep these in mind:

| Setting | Why it matters |
| --- | --- |
| WEBUI\_URL | Set this to your public HTTPS URL so OAuth callbacks and internal links resolve correctly |
| CORS\_ALLOW\_ORIGIN | Must match your public URL, or WebSocket connections will fail silently |
| Proxy buffering **off** | Required for SSE streaming. Buffering breaks markdown rendering in chat responses |
| WebSocket support | Ensure your proxy passes Upgrade and Connection headers for real-time features |
| Extended timeouts | LLM responses can take minutes. Set proxy read timeouts to at least 300s |

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/reference/https/index.md)
[Previous Environment Variable Configuration](https://docs.openwebui.com/reference/env-configuration)
[Next HTTPS using Cloudflare Tunnel](https://docs.openwebui.com/reference/https/cloudflare-tunnel)
Docs
\* [Getting Started](https://docs.openwebui.com/getting-started)
\* [FAQ](https://docs.openwebui.com/faq)
\* [Help Improve The Docs](https://github.com/open-webui/docs)
Community
\* [GitHub](https://github.com/open-webui/open-webui)
\* [Discord](https://discord.gg/5rJgQTnV4s)
\* [Reddit](https://www.reddit.com/r/OpenWebUI/)
\* [𝕏](https://x.com/OpenWebUI)
More
\* [Release Notes](https://github.com/open-webui/open-webui/blob/main/CHANGELOG.md)
\* [About](https://openwebui.com/)
\* [Report a Vulnerability / Responsible Disclosure](https://github.com/open-webui/open-webui/security)