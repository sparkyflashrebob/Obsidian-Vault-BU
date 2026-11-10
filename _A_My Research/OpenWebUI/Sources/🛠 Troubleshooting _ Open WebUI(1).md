---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

🛠 Troubleshooting / Open WebUI
[Skip to main content](https://docs.openwebui.com/troubleshooting#__docusaurus_skipToContent_fallback)
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
\* [⭐ Features](https://docs.openwebui.com/features/)
\* [🛠 Troubleshooting](https://docs.openwebui.com/troubleshooting/)
\* [Connection Errors](https://docs.openwebui.com/troubleshooting/connection-error)
\* [Reset Admin Password](https://docs.openwebui.com/troubleshooting/password-reset)
\* [Audio](https://docs.openwebui.com/troubleshooting/audio)
\* [RAG](https://docs.openwebui.com/troubleshooting/rag)
\* [SSO & OAuth](https://docs.openwebui.com/troubleshooting/sso)
\* [Web Search](https://docs.openwebui.com/troubleshooting/web-search)
\* [Scaling & HA](https://docs.openwebui.com/troubleshooting/multi-replica)
\* [Performance & RAM](https://docs.openwebui.com/troubleshooting/performance)
\* [Custom CA Store](https://docs.openwebui.com/troubleshooting/custom-ca)
\* [Image Generation](https://docs.openwebui.com/troubleshooting/image-generation)
\* [Manual Migration](https://docs.openwebui.com/troubleshooting/manual-database-migration)
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
\* 🛠 Troubleshooting
On this page

### Troubleshooting

Use this page to find the right guide for your issue. If you're unsure where to start, match your symptom in the table below.

#### Quick Symptom Lookup

| What you're seeing | Go to |
| --- | --- |
| Empty "{}" responses, garbled markdown, CORS errors in console | [Connection Errors → HTTPS/CORS/WebSocket](https://docs.openwebui.com/troubleshooting/connection-error#-https-tls-cors--websocket-issues) |
| WebSocket connection failed: 403 or chat hangs | [Connection Errors → WebSocket](https://docs.openwebui.com/troubleshooting/connection-error#websocket-troubleshooting) |
| Can't connect to Ollama from Open WebUI | [Connection Errors → Ollama](https://docs.openwebui.com/troubleshooting/connection-error#connection-to-ollama-server) |
| Model list takes forever to load / 500 on /api/models | [Connection Errors → Model List Loading](https://docs.openwebui.com/troubleshooting/connection-error#%EF%B8%8F-model-list-loading-issues-slow-ui--unreachable-endpoints) |
| [SSL: CERTIFICATE\_VERIFY\_FAILED] | [Connection Errors → SSL](https://docs.openwebui.com/troubleshooting/connection-error#-ssl-certificate-issues-with-internal-tools) |
| Login loops, 401 Unauthorized, token errors across replicas | [Scaling & HA → Login Loops](https://docs.openwebui.com/troubleshooting/multi-replica#1-login-loops--401-unauthorized-errors) |
| database is locked , data disappearing across instances | [Scaling & HA → Database](https://docs.openwebui.com/troubleshooting/multi-replica#4-database-corruption--locked-errors) |
| Worker crash: Child process [pid] died during upload | [RAG → Worker Crashes](https://docs.openwebui.com/troubleshooting/rag#12-worker-dies-during-document-upload) |
| Model ignores attached knowledge base | [RAG → Knowledge Base Not Working](https://docs.openwebui.com/troubleshooting/rag#13-knowledge-base-attached-to-model-not-working) |
| NoneType object has no attribute 'encode' | [RAG → Embedding Error](https://docs.openwebui.com/troubleshooting/rag#5-400-nonetype-object-has-no-attribute-encode) |
| CUDA out of memory during embedding | [RAG → CUDA OOM](https://docs.openwebui.com/troubleshooting/rag#10-cuda-out-of-memory-during-embedding) |
| OAuth redirect loops, CSRF state mismatch | [SSO & OAuth](https://docs.openwebui.com/troubleshooting/sso) |
| CSRF Warning! State not equal in request and response | [SSO → CSRF Errors](https://docs.openwebui.com/troubleshooting/sso#9-session-state-mismatch-csrf-errors) |
| TTS loading forever, Dataset scripts are no longer supported | [Audio → TTS Issues](https://docs.openwebui.com/troubleshooting/audio#tts-loading-forever--not-working) |
| Whisper int8 compute type error | [Audio → STT Issues](https://docs.openwebui.com/troubleshooting/audio#whisper-stt-not-working--compute-type-error) |
| Microphone not working (non-HTTPS) | [Audio → Microphone](https://docs.openwebui.com/troubleshooting/audio#microphone-access-issues) |
| Image not generating, ComfyUI workflow errors | [Image Generation](https://docs.openwebui.com/troubleshooting/image-generation) |
| Web search returns empty content or proxy errors | [Web Search](https://docs.openwebui.com/troubleshooting/web-search) |
| Slow performance, high RAM, OOM crashes | [Performance & RAM](https://docs.openwebui.com/troubleshooting/performance) |
| Forgot admin password | [Reset Admin Password](https://docs.openwebui.com/troubleshooting/password-reset) |
| no such table or table already exists on startup | [Database Migration](https://docs.openwebui.com/troubleshooting/manual-database-migration) |

#### All Troubleshooting Guides

| Guide | Covers |
| --- | --- |
| [Connection Errors](https://docs.openwebui.com/troubleshooting/connection-error) | HTTPS, CORS, WebSocket, reverse proxy, Ollama, SSL, Podman, MCP |
| [Performance & RAM](https://docs.openwebui.com/troubleshooting/performance) | Speed tuning, database optimization, scaling infrastructure, resource efficiency |
| [RAG](https://docs.openwebui.com/troubleshooting/rag) | Document ingestion, retrieval quality, embeddings, upload limits, worker crashes |
| [SSO & OAuth](https://docs.openwebui.com/troubleshooting/sso) | OIDC, Microsoft, Google, Authentik, cookie & session issues |
| [Audio](https://docs.openwebui.com/troubleshooting/audio) | Speech-to-Text, Text-to-Speech, microphone access, ElevenLabs |
| [Scaling & HA](https://docs.openwebui.com/troubleshooting/multi-replica) | Multi-replica, multi-worker, Redis, shared storage, database concurrency |
| [Image Generation](https://docs.openwebui.com/troubleshooting/image-generation) | OpenAI, ComfyUI, Automatic1111, Gemini |
| [Web Search](https://docs.openwebui.com/troubleshooting/web-search) | Proxy issues, SearXNG, empty results, timeouts |
| [Reset Admin Password](https://docs.openwebui.com/troubleshooting/password-reset) | Password reset for Docker and local installations |
| [Database Migration](https://docs.openwebui.com/troubleshooting/manual-database-migration) | Manual Alembic migrations, recovery from failed upgrades |

#### Before You Start

```
*   **Update first.**  Many issues are fixed in newer releases. Make sure you're on the latest version.
*   **Check PersistentConfig.**  Open WebUI stores some settings in its database, which take priority over environment variables. If an env var change seems ignored, see the [Environment Variable Configuration](https://docs.openwebui.com/reference/env-configuration#important-note-on-persistentconfig-environment-variables) page.
```

#### Browser Compatibility

Open WebUI requires a modern browser. Minimum supported versions:
\* **Chrome 111+** *(March 2023)*
\* **Safari 16.4+** *(March 2023)*
\* **Firefox 128+** *(July 2024)*
If you experience rendering or functionality issues, ensure your browser meets these requirements.

#### Community Support

If you're still stuck after following the relevant guide:
\* Search existing issues on [GitHub](https://github.com/open-webui/open-webui/issues)
\* Ask on [Discord](https://discord.com/invite/5rJgQTnV4s) or [Reddit](https://www.reddit.com/r/OpenWebUI/)
\* [Sponsors](https://docs.openwebui.com/sponsorships) get access to a dedicated support channel with faster response times
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/troubleshooting/index.mdx)
[Previous Tutorials](https://docs.openwebui.com/features/extensibility/pipelines/tutorials)
[Next Connection Errors](https://docs.openwebui.com/troubleshooting/connection-error)
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