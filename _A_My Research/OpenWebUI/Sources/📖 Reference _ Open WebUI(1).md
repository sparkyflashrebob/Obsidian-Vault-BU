---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

📖 Reference / Open WebUI
[Skip to main content](https://docs.openwebui.com/reference/#__docusaurus_skipToContent_fallback)
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
\* 📖 Reference
On this page

### Reference

**The technical details behind every knob, endpoint, and configuration option.**
Open WebUI is highly configurable. This section is the canonical source of truth for environment variables, API endpoints, network architecture, reverse proxy setups, and production monitoring. Whether you're tuning a single setting or architecting a multi-node deployment, start here.

#### ⚙ Environment Variable Configuration

**Every flag, path, and secret Open WebUI reads at startup, in one place.**
Over 200 environment variables control authentication, model routing, storage, logging, and more. Understand PersistentConfig behavior, troubleshoot ignored settings, and find the exact variable you need.

|  |  |
| --- | --- |
| 🔐 **Authentication & signup** | ENABLE\_SIGNUP , ENABLE\_LOGIN\_FORM , WEBUI\_ADMIN\_EMAIL , OIDC/LDAP/SCIM |
| 🤖 **Model connections** | Ollama, OpenAI, direct pipeline URLs, timeouts, load balancing |
| 💾 **Storage & databases** | SQLite, PostgreSQL, S3/GCS/Azure Blob, Redis |
| 📊 **Logging & audit** | GLOBAL\_LOG\_LEVEL , JSON logging, audit log levels and paths |
| 🧠 **RAG & retrieval** | Chunk size, overlap, embedding engines, reranking, vector DB selection |

[Browse all environment variables →](https://docs.openwebui.com/reference/env-configuration)

#### 🔌 API Endpoints

**OpenAI-compatible and Anthropic-compatible APIs, plus RAG, file management, and Ollama proxy routes.**
Open WebUI exposes a full REST API authenticated via Bearer tokens or JWTs. Use the same endpoints the web UI uses to build automations, chatbots, and custom integrations.

|  |  |
| --- | --- |
| 💬 **Chat completions** | POST /api/chat/completions , OpenAI-compatible |
| 🔮 **Anthropic messages** | POST /api/v1/messages , works with the Anthropic SDK and Claude Code |
| 🦙 **Ollama proxy** | /ollama/api/\* , passthrough to native Ollama endpoints |
| 📄 **File & knowledge** | Upload files, build knowledge collections, query via RAG |
| 🔧 **Filters & outlets** | Inlet, stream, and outlet hooks for every request |

[Explore the API →](https://docs.openwebui.com/reference/api-endpoints)

#### 🔒 HTTPS Configuration

**Terminate TLS in front of Open WebUI with Nginx, Caddy, or HAProxy.**
Step-by-step reverse proxy configurations for securing your deployment with HTTPS. Each guide includes certificate handling, WebSocket support, and production-hardened settings.

|  |  |
| --- | --- |
| 🟢 **Nginx** | Full config with SSL termination, WebSocket proxying, and headers |
| ⚡ **Caddy** | Automatic HTTPS with minimal configuration |
| 🔄 **HAProxy** | Enterprise-grade load balancing with TLS offloading |
| ☁ **Cloudflare Tunnel** | Expose Open WebUI securely without opening ports |
| 🔒 **Tailscale** | Private encrypted access across your devices, no public exposure |
| 🧪 **ngrok** | Instant HTTPS tunnels for development and testing |

[Set up HTTPS →](https://docs.openwebui.com/reference/https)

#### 🔑 API Keys

**Programmatic access to Open WebUI for scripts, bots, and integrations.**
Generate personal access tokens that let external code call the same endpoints the web UI uses. Each key inherits the permissions of the user who created it.

|  |  |
| --- | --- |
| 🔐 **Bearer token auth** | Standard Authorization: Bearer header, works with any HTTP client |
| 🛡 **Scoped to user** | Key inherits your role and group permissions |
| 🚫 **Endpoint restrictions** | Optionally limit which API routes a key can access |

[Set up API keys →](https://docs.openwebui.com/features/authentication-access/api-keys)

#### 📊 Monitoring

**Observe your deployment with Uptime Kuma, OpenTelemetry, Prometheus, and Grafana.**
Production monitoring guides covering health checks, model connectivity verification, distributed tracing, metrics, and structured logs. Integrate with your existing observability stack or set up a new one from scratch.

|  |  |
| --- | --- |
| ✅ **Health checks** | Basic, model connectivity, and deep health checks with Uptime Kuma |
| 📡 **OpenTelemetry** | Traces, metrics, and logs piped to any OTLP-compatible backend |
| 📈 **Dashboards** | Prometheus + Grafana for real-time system and model metrics |

[Set up monitoring →](https://docs.openwebui.com/reference/monitoring)

#### 🌐 Network Diagrams

**See how Open WebUI, Ollama, and Docker communicate across different deployment topologies.**
Visual C4 diagrams covering host networking, Docker Compose stacks, separate networks, and platform-specific differences. Useful for debugging connectivity issues or planning your architecture.

|  |  |
| --- | --- |
| 🖥 **macOS / Windows** | Host Ollama, Compose stack, separate networks, host-network pitfalls |
| 🐧 **Linux** | Same topologies with Linux-specific networking behavior |

[View network diagrams →](https://docs.openwebui.com/reference/network-diagrams)
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/reference/index.md)
[Previous Developing Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/development)
[Next Environment Variable Configuration](https://docs.openwebui.com/reference/env-configuration)
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