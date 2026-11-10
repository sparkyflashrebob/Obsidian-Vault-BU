---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Model Context Protocol (MCP) / Open WebUI
[Skip to main content](https://docs.openwebui.com/features/extensibility/mcp#__docusaurus_skipToContent_fallback)
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
\* [🔐 Authentication & Access](https://docs.openwebui.com/features/authentication-access/)
\* [🔧 Administration](https://docs.openwebui.com/features/administration/)
\* [💬 Chat & Conversations](https://docs.openwebui.com/features/extensibility/mcp)
\* [🧠 Workspace](https://docs.openwebui.com/features/extensibility/mcp)
\* [📝 Notes](https://docs.openwebui.com/features/notes/)
\* [📢 Channels](https://docs.openwebui.com/features/channels/)
\* [💻 Open Terminal](https://docs.openwebui.com/features/open-terminal/)
\* [🔌 Plugins & Extensibility](https://docs.openwebui.com/features/extensibility/)
\* [Tools & Functions (Plugins)](https://docs.openwebui.com/features/extensibility/plugin/)
\* [Model Context Protocol (MCP)](https://docs.openwebui.com/features/extensibility/mcp)
\* [Pipelines](https://docs.openwebui.com/features/extensibility/pipelines/)
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
\* [⭐ Features](https://docs.openwebui.com/features/)
\* [🔌 Plugins & Extensibility](https://docs.openwebui.com/features/extensibility/)
\* Model Context Protocol (MCP)
On this page

### Model Context Protocol (MCP)

Open WebUI natively supports **MCP (Model Context Protocol)** starting in **v0.6.31** . This page shows how to enable it quickly, harden it for production, and troubleshoot common snags.
info
Requires **Open WebUI v0.6.31+** .
Prerequisite: WEBUI\_SECRET\_KEY
You **MUST** set the WEBUI\_SECRET\_KEY environment variable in your Docker setup. Without it, **OAuth-connected MCP tools (like Notion)** will **break** every time you restart or recreate the container (Error: Error decrypting tokens ), forcing you to re-authenticate everything.

#### 🚀 Quick start

```
1. Open  **⚙ Admin Settings → External Tools** .
1. Click  **+ (Add Server)** .
1. Set  **Type**  to  **MCP (Streamable HTTP)** .
1. Enter your  **Server URL**  and  **Auth**  details (OAuth 2.1, if required).
1.  **Save** . If prompted, restart Open WebUI.
```

You can now call tools exposed by your MCP server from Open WebUI.
Common Mistake: Wrong Connection Type
If you are adding an MCP server, make sure **Type** is set to **MCP (Streamable HTTP)** , not **OpenAPI** .
Entering MCP-style configuration (with mcpServers in JSON) into an OpenAPI connection will cause the UI to crash or display an infinite loading screen. If you encounter this:
1. Disable the problematic tool connection via Admin Settings
1. Re-add it with the correct **Type** set to **MCP**

#### 🧭 When to use MCP vs OpenAPI

tip
For most deployments, **OpenAPI** remains the **preferred** integration path.
Choose **OpenAPI** if you want:
\* **Enterprise readiness** : deep SSO, API gateways, audit, quotas, typed SDKs.
\* **Operational resilience** : standard HTTP verbs, idempotency, caching, rich error codes.
\* **Observability** : first-class tracing and policy integration.
Choose **MCP (Streamable HTTP)** if you need:
\* A **common tool protocol** already used by your MCP servers/clients.
\* **Streamed** protocol communication over HTTP (Note: This refers to MCP's transport-level streaming, not Open WebUI's [UI event system](https://docs.openwebui.com/features/extensibility/plugin/development/events) which is only available for native Python tools).
You don't have to pick one: many teams expose OpenAPI internally and **wrap MCP** at the edge for specific clients.
warning
Browser-based, multi-user deployments increase the surface area (CORS/CSRF, per-user isolation, reconnects). Review your org's auth, proxy, and rate-limiting policies before exposing MCP externally.

#### ⚙ Configuration Best Practices

##### Authentication Modes

```
*   **None** : Use this for  **local MCP servers**  or internal networks where no token is required.
    *   **⚠ Important** : Default to "None" unless your server strictly requires a token. Selecting "Bearer" without providing a key sends an empty Authorization header ( Authorization: Bearer ), which causes many servers to reject the connection immediately.
*   **Bearer** : Use this  **only**  if your MCP server requires a specific API token. You  **must**  populate the "Key" field.
*   **OAuth 2.1** : Uses Dynamic Client Registration (DCR). Best when your MCP server supports registering OAuth clients automatically.
*   **OAuth 2.1 (Static)** : Uses a pre-created client ID/client secret. Best when your provider does not support DCR, or when your security team requires manually managed credentials.
```

Choosing Between OAuth 2.1 and OAuth 2.1 (Static)
\* Start with **OAuth 2.1** if your server supports DCR.
\* Use **OAuth 2.1 (Static)** when you already have credentials from your IdP and want Open WebUI to use those directly.

##### OAuth 2.1 (Static) Setup

Use this when you already have a client ID/client secret from your identity provider.
1. Open **Admin Settings → External Tools** .
1. Click **+ (Add Server)** .
1. Set **Type** to **MCP (Streamable HTTP)** .
1. Enter your MCP server **URL** .
1. In **Auth** , select **OAuth 2.1 (Static)** .
1. Enter **Client ID** and **Client Secret** .
1. Click **Register Client** .
1. Click **Save** .
After saving:
1. Open a chat.
1. Click **+ → Integrations → Tools** .
1. Enable your MCP tool.
1. Complete the OAuth consent/authorization flow in the browser redirect.
info Register Client is required for both oauth\_2.1 and oauth\_2.1\_static . With static auth, Open WebUI uses your provided credentials and server metadata discovery (no dynamic client registration).
OAuth 2.1 Tools Cannot Be Set as Default Tools
**Do not set OAuth 2.1 MCP tools as default/pre-enabled tools on a model.** The OAuth 2.1 authorization flow requires an interactive browser redirect (user consent, callback) that cannot happen transparently during a chat completion request.
If an OAuth 2.1 tool is set as a default and the user hasn't previously authenticated (or their refresh token has expired), the tool call will fail with **"Failed to connect to MCP server"** because the backend cannot initiate the browser-based auth flow mid-request.
**Workaround:** Users should manually enable OAuth 2.1 tools per-chat via the **➕** button in the chat input area. This triggers the auth flow before the tool is ever invoked. Token refresh works automatically once the initial authentication is complete.

##### Connection URLs

If you are running Open WebUI in **Docker** and your MCP server is on the **host machine** :
\* Use http://host.docker.internal:

##### Function Name Filter List

This field restricts which tools are exposed to the LLM.
\* **Default** : Leave empty to expose all tools (in most cases).
\* **Workaround** : If you encounter connection errors with an empty list, try adding a single comma ( , ) to this field. This forces the system to treat it as a valid (but empty) filter, potentially bypassing some parsing issues.

#### Troubleshooting

##### "Failed to connect to MCP server"

**Symptom** : The chat shows "Failed to connect to MCP server" when using a tool, even if the **Verify Connection** button in settings says "Connected".
**Solutions** :
1. **Check Authentication** : Ensure you haven't selected Bearer without a key. Switch to None if no token is needed.
1. **Filter List Bug** : If the "Function Name Filter List" is empty, try adding a comma ( , ) to it.
1. **OAuth 2.1 Default Tool** : If the failing tool uses OAuth 2.1 and is set as a default tool on the model, this is a known limitation. Remove it from the model's default tools and have users enable it manually per-chat.

##### Infinite loading screen after adding External Tool

**Symptom** : After adding an External Tool connection, the frontend gets stuck on a loading spinner. The browser console shows an error like Cannot convert undefined or null to object at Object.entries .
**Cause** : You likely configured an **MCP server** using the **OpenAPI** connection type, or entered MCP-style JSON (containing mcpServers ) into an OpenAPI connection.
**Solution** :
1. Open **Admin Settings → External Tools** (the sidebar still loads)
1. **Disable** or **delete** the problematic tool connection
1. Refresh the page (Ctrl+F5)
1. Re-add the connection with the correct **Type** set to **MCP (Streamable HTTP)**

#### ❓ FAQ

**Do you support stdio or SSE transports?**
Native MCP support in Open WebUI is **Streamable HTTP only** . This design choice reflects our architecture: Open WebUI is a **web-based, multi-tenant environment** , not a local desktop process.
Browsers operate within strict **sandboxed and event-driven HTTP constraints** , making long-lived stdio or SSE connections difficult to maintain securely across users and sessions.
If you need to bridge those other MCP transports, check out [mcpo](https://github.com/open-webui/mcpo) — an open-source proxy that translates **stdio or SSE-based MCP servers into OpenAPI-compatible endpoints** . It effectively lets you run traditional MCP tools inside Open WebUI without modifying their transport layer.
**Is MCP considered stable here?**
Supported and improving. The broader ecosystem is still evolving; expect occasional breaking changes.
**Can I mix OpenAPI and MCP tools?**
Yes. Many deployments do both.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/features/extensibility/mcp.mdx)
[Previous Migrating Tools & Functions: 0.4 to 0.5](https://docs.openwebui.com/features/extensibility/plugin/migration/)
[Next Pipelines](https://docs.openwebui.com/features/extensibility/pipelines/)
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