---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Monitoring / Open WebUI
[Skip to main content](https://docs.openwebui.com/reference/monitoring#__docusaurus_skipToContent_fallback)
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
\* [OpenTelemetry](https://docs.openwebui.com/reference/monitoring/otel)
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
\* Monitoring
On this page

### 📊 Monitoring

**Know when something breaks before your users do.**
Open WebUI exposes health and model endpoints that make it straightforward to wire up uptime monitoring, model connectivity checks, and end-to-end response testing. Whether you're running a single instance or a multi-node deployment, these checks give you confidence that the service is up, models are reachable, and inference is actually working.

#### Why Monitor?

##### Catch outages instantly

A health check that runs every 60 seconds means you know about downtime within a minute, not when a user files a complaint.

##### Verify model connectivity

Open WebUI can be running fine while your model provider is down. Monitoring the /api/models endpoint catches that gap.

##### End-to-end confidence

The deepest check sends a real prompt and validates the response. If that passes, you know the entire pipeline works: API, backend, model provider, and inference.

#### Key Features

|  |  |
| --- | --- |
| ✅ **Health endpoint** | Unauthenticated /health check, returns 200 when the service is up |
| 🔗 **Model connectivity** | Authenticated /api/models check verifies provider connections |
| 🤖 **Deep health check** | Send a real chat completion and validate the response |
| 🐻 **Uptime Kuma recipes** | Ready-to-use configurations for each monitoring level |

#### Level 1: Basic Health Check

The /health endpoint is publicly accessible (no authentication required) and returns 200 OK when the service is running.

```
curl http://your-open-webui-instance:8080/health
```

This verifies web server availability, application initialization, and basic database connectivity.

##### Uptime Kuma Setup

```
1.  **Add New Monitor**  with type  **HTTP(s)**
1.  **URL:**  http://your-open-webui-instance:8080/health
1.  **Interval:**  60 seconds
1.  **Retries:**  3
```

#### Level 2: Model Connectivity Check

The /api/models endpoint **requires authentication** and confirms that Open WebUI can reach your model providers and list available models.

```
curl -H "Authorization: Bearer YOUR_API_KEY" \
  http://your-open-webui-instance:8080/api/models
```

You'll need an API key. See [API Keys](https://docs.openwebui.com/features/authentication-access/api-keys) for setup instructions.
Dedicated Monitoring Account
Create a **non-admin user** (e.g., monitoring-bot ), generate an API key from that account, and use it for all monitoring requests. This limits blast radius if the key is ever compromised.

##### Uptime Kuma Setup

```
1.  **Monitor Type:**  HTTP(s) - JSON Query
1.  **URL:**  http://your-open-webui-instance:8080/api/models
1.  **Method:**  GET
1.  **Header:**  Authorization: Bearer YOUR_API_KEY
1.  **JSON Query:**  $count(data[*])>0
1.  **Expected Value:**  true
1.  **Interval:**  300 seconds (5 minutes)
```

##### Advanced JSONata Queries

| Goal | Query |
| --- | --- |
| At least one Ollama model | $count(data[owned\_by='ollama'])>0 |
| Specific model exists | $exists(data[id='gpt-4o']) |
| Multiple models exist | $count(data[id in ['gpt-4o', 'gpt-4o-mini']]) = 2 |

Test queries at [jsonata.org](https://try.jsonata.org/) with a sample API response.

#### Level 3: Deep Health Check

Send a real chat completion to verify the entire inference pipeline end-to-end.

```
curl -X POST http://your-open-webui-instance:8080/api/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Respond with the word HEALTHY"}],
    "model": "llama3.1",
    "temperature": 0
  }'
```

A successful response returns 200 OK with a chat completion containing "HEALTHY". This catches model loading failures, backend processing errors, and provider-side issues that Levels 1 and 2 would miss.
info
Setting up Level 3 in Uptime Kuma requires an HTTP(s) monitor with a POST body, authentication headers, and a JSON query to validate the response. See [Uptime Kuma docs](https://github.com/louislam/uptime-kuma) for POST monitor configuration.

#### Next Steps

```
*   **OpenTelemetry**  - Distributed tracing, metrics, and logs with Grafana, Prometheus, Jaeger, and more
*   **API Keys**  - Full guide on enabling and generating API keys for programmatic access
```

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/reference/monitoring/index.md)
[Previous HTTPS using Caddy](https://docs.openwebui.com/reference/https/caddy)
[Next OpenTelemetry](https://docs.openwebui.com/reference/monitoring/otel)
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