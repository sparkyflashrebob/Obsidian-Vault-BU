---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Tailscale / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/auth-sso/tailscale#__docusaurus_skipToContent_fallback)
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
\* [🏢 Open WebUI for Enterprise](https://docs.openwebui.com/enterprise/)
\* [🎓 Tutorials](https://docs.openwebui.com/tutorials/)
\* [Community Guides](https://docs.openwebui.com/tutorials/community/)
\* [Authentication & SSO](https://docs.openwebui.com/tutorials/auth-sso/)
\* [Okta SSO (OIDC)](https://docs.openwebui.com/tutorials/auth-sso/okta-oidc-sso)
\* [Dual OAuth Configuration](https://docs.openwebui.com/tutorials/auth-sso/dual-oauth-configuration)
\* [Entra ID Group Name Sync](https://docs.openwebui.com/tutorials/auth-sso/entra-group-name-sync)
\* [Tailscale](https://docs.openwebui.com/tutorials/auth-sso/tailscale)
\* [Azure AD LDAP](https://docs.openwebui.com/tutorials/auth-sso/azure-ad-ds-ldap)
\* [Integrations](https://docs.openwebui.com/tutorials/integrations/)
\* [Maintenance](https://docs.openwebui.com/tutorials/maintenance/)
\* [Contributing to Docs](https://docs.openwebui.com/tutorials/contributing-tutorial)
\* [❓ FAQ](https://docs.openwebui.com/faq)
\* [🛣 Roadmap](https://docs.openwebui.com/roadmap)
\* [🛡 Security Policy](https://docs.openwebui.com/security)
\* [🤝 Contributing](https://docs.openwebui.com/contributing)
\* [💖 Sponsorships](https://docs.openwebui.com/sponsorships)
\* [🎨 Brand Guidelines](https://docs.openwebui.com/brand)
\* [⚖ Open WebUI License](https://docs.openwebui.com/license)
\* [🎯 Our Mission](https://docs.openwebui.com/mission)
\* [👥 Our Team](https://docs.openwebui.com/team)
\* [🎓 Tutorials](https://docs.openwebui.com/tutorials/)
\* [Authentication & SSO](https://docs.openwebui.com/tutorials/auth-sso/)
\* Tailscale
On this page

### Tailscale Integration

**Private, encrypted access to Open WebUI from any device. No ports to open, no certificates to manage.**
[Tailscale](https://tailscale.com/) creates a WireGuard-based mesh VPN (a "tailnet") between your devices. Every device gets a stable hostname like my-server.tail1234.ts.net , and Tailscale can provision trusted HTTPS certificates automatically. Your Open WebUI instance stays completely private, accessible only to devices on your tailnet.
When to use Tailscale
Tailscale is ideal when you want **private, authenticated access** across devices without exposing Open WebUI to the public internet. Perfect for personal setups, small teams, or accessing a home server from your phone or laptop on the go.

#### Prerequisites

| Requirement | Details |
| --- | --- |
| **Open WebUI** | Running locally on port 8080 (default) |
| **Tailscale account** | Free for personal use at [tailscale.com](https://tailscale.com/) |
| **Tailscale installed** | On both the server running Open WebUI and any client devices |

#### Quick Start

##### 1. Install Tailscale

```
*  macOS
*  Linux
*  Windows
```

Download from the [Mac App Store](https://apps.apple.com/app/tailscale/id1475387142) or:

```
brew install tailscale
```

```
curl -fsSL https://tailscale.com/install.sh | sh
```

Download from [tailscale.com/download](https://tailscale.com/download/windows).

##### 2. Connect the server

On the machine running Open WebUI:

```
sudo tailscale up
```

Your machine gets a tailnet hostname like my-server.tail1234.ts.net . Find it with:

```
tailscale status
```

##### 3. Access Open WebUI

From any device on the same tailnet, open:

```
http://my-server.tail1234.ts.net:8080
```

This connection is already encrypted end-to-end by WireGuard. For browser features that require HTTPS (like Voice Calls), continue to the next section.

#### HTTPS with Tailscale

Tailscale can provision trusted Let's Encrypt certificates for your tailnet hostname, no reverse proxy required.
For the full step-by-step HTTPS setup (certificate generation, tailscale serve , configuring WEBUI\_URL ), see the dedicated reference guide:
👉 [HTTPS using Tailscale](https://docs.openwebui.com/reference/https/tailscale)
The short version:

```
# Proxy HTTPS traffic directly to Open WebUI
sudo tailscale serve https / http://localhost:8080
```

Your instance is now available at https://my-server.tail1234.ts.net with a valid TLS certificate.

#### Authentication via Tailscale (SSO)

[Tailscale Serve](https://tailscale.com/kb/1242/tailscale-serve) can act as an authenticating reverse proxy. When a request passes through tailscale serve , Tailscale automatically sets the Tailscale-User-Login header with the email address of the authenticated user. Open WebUI can trust this header as a single sign-on mechanism. Users on your tailnet are automatically logged in without needing a separate Open WebUI password.

##### How it works

```
1. A Tailscale sidecar container runs alongside Open WebUI
1. Tailscale Serve proxies HTTPS traffic to Open WebUI and injects identity headers
1. Open WebUI reads Tailscale-User-Login and Tailscale-User-Name to identify the user
1. Users are auto-registered and logged in on first visit
```

##### Docker Compose Setup

Create a tailscale/serve.json file that configures Tailscale Serve to proxy to Open WebUI:

```
{
    "TCP": {
        "443": {
            "HTTPS": true
        }
    },
    "Web": {
        "${TS_CERT_DOMAIN}:443": {
            "Handlers": {
                "/": {
                    "Proxy": "http://open-webui:8080"
                }
            }
        }
    }
}
```

Then set up the Docker Compose file with a Tailscale sidecar:

```
---
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    volumes:
      - open-webui:/app/backend/data
    environment:
      - WEBUI_AUTH_TRUSTED_EMAIL_HEADER=Tailscale-User-Login
      - WEBUI_AUTH_TRUSTED_NAME_HEADER=Tailscale-User-Name
    restart: unless-stopped
  tailscale:
    image: tailscale/tailscale:latest
    environment:
      - TS_AUTH_ONCE=true
      - TS_AUTHKEY=${TS_AUTHKEY}
      - TS_EXTRA_ARGS=--advertise-tags=tag:open-webui
      - TS_SERVE_CONFIG=/config/serve.json
      - TS_STATE_DIR=/var/lib/tailscale
      - TS_HOSTNAME=open-webui
    volumes:
      - tailscale:/var/lib/tailscale
      - ./tailscale:/config
      - /dev/net/tun:/dev/net/tun
    cap_add:
      - net_admin
      - sys_module
    restart: unless-stopped

volumes:
  open-webui: {}
  tailscale: {}
```

You will need to create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with **device write** permission in the Tailscale admin console and pass the key as TS\_AUTHKEY .
Your instance will be reachable at https://open-webui.TAILNET\_NAME.ts.net .
Restrict direct access with ACLs
If you run Tailscale in the same network context as Open WebUI, users could bypass the Serve proxy and reach Open WebUI directly, skipping the trusted header authentication. Use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to restrict access to only port 443.
For more details on trusted header authentication, see the [SSO documentation](https://docs.openwebui.com/features/authentication-access/auth/sso#tailscale-serve).

#### Tailscale Funnel (Optional Public Access)

If you want to share Open WebUI publicly without requiring Tailscale on the client, [Tailscale Funnel](https://tailscale.com/kb/1223/funnel) exposes your tailscale serve endpoint to the internet:

```
sudo tailscale funnel https / http://localhost:8080
```

Your Open WebUI is now publicly accessible at https://my-server.tail1234.ts.net with a valid TLS certificate. Funnel routes traffic through Tailscale's infrastructure, similar to Cloudflare Tunnel.
warning
Funnel makes your Open WebUI accessible to **anyone on the internet** . Make sure you have authentication configured in Open WebUI before enabling it.

#### Quick Reference

| What | Command / Value |
| --- | --- |
| Connect to tailnet | sudo tailscale up |
| Check hostname | tailscale status |
| Serve over HTTPS | sudo tailscale serve https / http://localhost:8080 |
| Public access (Funnel) | sudo tailscale funnel https / http://localhost:8080 |
| Generate cert manually | sudo tailscale cert my-server.tail1234.ts.net |
| Admin console | [login.tailscale.com/admin](https://login.tailscale.com/admin) |
| Set CORS origin | CORS\_ALLOW\_ORIGIN=https://my-server.tail1234.ts.net |
| Trusted email header | WEBUI\_AUTH\_TRUSTED\_EMAIL\_HEADER=Tailscale-User-Login |
| Trusted name header | WEBUI\_AUTH\_TRUSTED\_NAME\_HEADER=Tailscale-User-Name |

#### Related Pages

```
*  [HTTPS using Tailscale](https://docs.openwebui.com/reference/https/tailscale) - focused HTTPS/TLS reference
*  [SSO (Trusted Header)](https://docs.openwebui.com/features/authentication-access/auth/sso#tailscale-serve) - generic trusted header configuration
*  [Sharing Open WebUI](https://docs.openwebui.com/getting-started/sharing) - overview of all sharing approaches
```

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/auth-sso/tailscale.md)
[Previous Entra ID Group Name Sync](https://docs.openwebui.com/tutorials/auth-sso/entra-group-name-sync)
[Next Azure AD LDAP](https://docs.openwebui.com/tutorials/auth-sso/azure-ad-ds-ldap)
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