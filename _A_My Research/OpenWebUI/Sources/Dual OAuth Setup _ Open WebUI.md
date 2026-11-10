---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Dual OAuth Setup / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/auth-sso/dual-oauth-configuration#__docusaurus_skipToContent_fallback)
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
\* Dual OAuth Configuration
On this page

### 🔐 Dual OAuth Configuration (Microsoft & Google)

Unofficial Workaround
This configuration is a community-contributed workaround and is **not officially supported** by the Open WebUI team. While it works in current versions, behavior may change in future updates. This tutorial serves as a demonstration for advanced users.

#### Overview

While Open WebUI officially supports only one **OpenID Connect (OIDC)** provider at a time via the OPENID\_PROVIDER\_URL variable, it is possible to support both **Microsoft** and **Google** simultaneously.
The trick is to configure one provider (e.g., Microsoft) as the primary OIDC provider and the other (e.g., Google) as a standard OAuth provider by utilizing Open WebUI's built-in support for specific providers.

#### Prerequisites

```
*  Access to your Open WebUI environment variables (Docker or local).
*  Client IDs and Secrets from both [Google Cloud Console](https://console.cloud.google.com/) and [Microsoft Azure/Entra ID](https://entra.microsoft.com/).
*  OAUTH_MERGE_ACCOUNTS_BY_EMAIL=true must be enabled to ensure users are mapped to the same account regardless of the provider used.
```

#### Configuration logic

Open WebUI uses OPENID\_PROVIDER\_URL as a generic "catch-all" for OIDC. However, it also has native modules for Google and Microsoft. By leaving the OPENID\_PROVIDER\_URL for Microsoft and providing only the Client IDs for Google, the system can internalize both flows.

#### Environment Variables

Add the following to your docker-compose.yaml or environment config:

```
# Enable signup and account merging (CRITICAL)
ENABLE_OAUTH_SIGNUP=true
OAUTH_MERGE_ACCOUNTS_BY_EMAIL=true

# 1. Microsoft as the primary OIDC provider
# This uses the generic OIDC flow via the OPENID_PROVIDER_URL
MICROSOFT_CLIENT_ID=your_microsoft_client_id
MICROSOFT_CLIENT_SECRET=your_microsoft_client_secret
MICROSOFT_CLIENT_TENANT_ID=your_tenant_id
MICROSOFT_REDIRECT_URI=https://your-webui.com/oauth/microsoft/callback
OPENID_PROVIDER_URL=https://login.microsoftonline.com/your_tenant_id/v2.0/.well-known/openid-configuration

# Optional: Custom scope for Microsoft OAuth (required if using custom API scopes)
# MICROSOFT_OAUTH_SCOPE=openid email profile offline_access api:///

# Optional: Include scope in refresh token requests (required for some Azure AD configurations)
# OAUTH_REFRESH_TOKEN_INCLUDE_SCOPE=true

# 2. Google as a secondary OAuth provider
# Note: Do NOT provide an OPENID_PROVIDER_URL for Google.
# The system will use its internal Google OAuth implementation.
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```

#### Why This Works

```
1.  **Microsoft**  is handled via the generic OIDC flow because OPENID_PROVIDER_URL is set to the Microsoft endpoint.
1.  **Google**  is handled via the dedicated internal Google OAuth module because the system detects GOOGLE_CLIENT_ID but sees that the global OPENID_PROVIDER_URL is already "claimed" by Microsoft or simply isn't needed for the built-in Google module.
1.  **Account Merging** : Since both providers return the user's email, OAUTH_MERGE_ACCOUNTS_BY_EMAIL=true ensures the user logs into the same profile whether they click "Sign in with Google" or "Sign in with Microsoft."
```

#### Troubleshooting

```
*   **Redirect Mismatch** : Ensure your Redirect URIs in both consoles match your WEBUI_URL .
*   **Merge Failures** : Double-check that OAUTH_MERGE_ACCOUNTS_BY_EMAIL is set to true .
*   **Microsoft Logout** : Microsoft often requires the OPENID_PROVIDER_URL to handle the logout redirect correctly. If logout fails, ensure this URL is correct for your tenant.
*   **Azure AD Refresh Token Failures ( AADSTS90009 )** : If token refresh fails with the error "Application is requesting a token for itself", set OAUTH_REFRESH_TOKEN_INCLUDE_SCOPE=true . Azure AD requires the scope to be explicitly included in refresh token requests. You may also need to set MICROSOFT_OAUTH_SCOPE to include offline_access and any custom API scopes.
```

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/auth-sso/dual-oauth-configuration.mdx)
[Previous Okta SSO (OIDC)](https://docs.openwebui.com/tutorials/auth-sso/okta-oidc-sso)
[Next Entra ID Group Name Sync](https://docs.openwebui.com/tutorials/auth-sso/entra-group-name-sync)
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