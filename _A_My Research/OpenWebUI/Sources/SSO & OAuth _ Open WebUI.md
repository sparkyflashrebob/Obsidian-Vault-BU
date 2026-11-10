---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

SSO & OAuth / Open WebUI
[Skip to main content](https://docs.openwebui.com/troubleshooting/sso#__docusaurus_skipToContent_fallback)
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
\* [🛠 Troubleshooting](https://docs.openwebui.com/troubleshooting/)
\* SSO & OAuth
On this page

### SSO & OAuth

OAuth and Single Sign-On (SSO) provide secure authentication for Open WebUI. When login problems occur, one of these common issues is usually the cause.

#### Common OAuth/SSO Issues

##### 1. WebUI URL Not Configured

Most OAuth flows require the application's external URL ("redirect URI") so the provider knows where to send users after login. If this is missing, OAuth cannot complete.
**Solution:**
\* Navigate to: **Admin Settings > General**
\* Ensure your **WebUI URL** field is filled in and points to your deployed instance (e.g., https://yourwebui.yourdomain.com )
tip
Check for typos — OAuth is strict. URLs must match exactly, including https:// .

##### 2. Incorrect Environment Variable Configuration

This is the **most common cause** of OAuth breakage. A misspelled, omitted, or incorrect environment variable will prevent authentication from working.
**Common Environment Variable Mistakes:**

###### ❌ Non-Existent Variables People Often Use:

```
*  OIDC_CONFIG → Use OPENID_PROVIDER_URL instead
*  WEBUI_OIDC_CLIENT_ID → Use OAUTH_CLIENT_ID instead
*  WEBUI_ENABLE_SSO → Use ENABLE_OAUTH_SIGNUP instead
*  WEBUI_AUTH_TYPE → This doesn't exist - configure provider-specific variables instead
*  OPENID_CLIENT_ID → Use OAUTH_CLIENT_ID instead
*  OPENID_CLIENT_SECRET → Use OAUTH_CLIENT_SECRET instead
```

###### ✅ Correct OIDC Variables:

```
# Required for OIDC
OAUTH_CLIENT_ID=your_client_id
OAUTH_CLIENT_SECRET=your_client_secret
OPENID_PROVIDER_URL=https://your-provider/.well-known/openid-configuration
ENABLE_OAUTH_SIGNUP=true

# Optional but recommended
OAUTH_PROVIDER_NAME=Your Provider Name
OAUTH_SCOPES=openid email profile
OPENID_REDIRECT_URI=https://your-domain/oauth/oidc/callback

# Optional: pass provider-specific authorize params (JSON object)
# e.g. force consent screen, prefill user/email hint
OAUTH_AUTHORIZE_PARAMS={"prompt":"consent","login_hint":"user@example.com"}
```

###### ✅ Google-specific optional authorize params:

```
# Optional: extra Google /authorize params as JSON
GOOGLE_OAUTH_AUTHORIZE_PARAMS={"prompt":"consent","login_hint":"user@example.com","hd":"example.com"}
```

###### ✅ Correct Microsoft Variables:

```
# Use these for Microsoft Entra ID
MICROSOFT_CLIENT_ID=your_client_id
MICROSOFT_CLIENT_SECRET=your_client_secret
MICROSOFT_CLIENT_TENANT_ID=your_tenant_id
OPENID_PROVIDER_URL=https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0/.well-known/openid-configuration
ENABLE_OAUTH_SIGNUP=true
```

**Solutions:**
\* **Always reference the official environment configuration documentation** for exact variable names
\* Double-check your deployment environment:
\* Ensure all required environment variables are set exactly as documented
\* If self-hosting, confirm these variables are present in your Docker Compose, Kubernetes manifest, or .env file
\* Restart your backend/app after changing variables so the new values are loaded
info
If your provider needs extra parameters at the /authorize step (for example prompt , login\_hint , domain\_hint , or resource ), set them via OAUTH\_AUTHORIZE\_PARAMS as a JSON object.
For Google-specific customization, you can also use GOOGLE\_OAUTH\_AUTHORIZE\_PARAMS .
tip
Most OAuth errors (loops, 401s, unresponsiveness) are due to an environment variable that is incorrectly named, missing entirely, or using an outdated variable name.
warning
**Kubernetes/YAML users:** Watch out for **trailing spaces in environment variable names!** In YAML, quoting a key like 'OAUTH\_CLIENT\_ID ' (with a trailing space inside the quotes) will set a variable named OAUTH\_CLIENT\_ID (with a space at the end), which Open WebUI will **not** recognize. Always ensure your env var names have no trailing whitespace:

```
# ❌ Wrong — trailing space inside quotes:
- name: 'OAUTH_CLIENT_ID '
  value: your_client_id

# ✅ Correct — no trailing space:
- name: OAUTH_CLIENT_ID
  value: your_client_id
```

##### 3. Missing Required Variables

###### OPENID\_PROVIDER\_URL is Mandatory for OIDC

Many users forget this critical variable. Without it, OIDC authentication cannot work.
✅ **For Microsoft Entra ID:**

```
OPENID_PROVIDER_URL=https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0/.well-known/openid-configuration
```

✅ **For Google:**

```
OPENID_PROVIDER_URL=https://accounts.google.com/.well-known/openid-configuration
```

✅ **For Authentik:**

```
OPENID_PROVIDER_URL=https://your-authentik-domain/application/o/your-app-name/.well-known/openid-configuration
```

###### Other Required Variables by Provider:

```
*   **All OAuth providers:**  WEBUI_URL , ENABLE_OAUTH_SIGNUP=true
*   **Microsoft:**  MICROSOFT_CLIENT_ID , MICROSOFT_CLIENT_SECRET , MICROSOFT_CLIENT_TENANT_ID
*   **Google:**  GOOGLE_CLIENT_ID , GOOGLE_CLIENT_SECRET
*   **OIDC:**  OAUTH_CLIENT_ID , OAUTH_CLIENT_SECRET , OPENID_PROVIDER_URL
```

##### 4. Persistent Configuration Conflicts

**Important:** Open WebUI has **two** persistence settings that affect OAuth:
1. **ENABLE\_PERSISTENT\_CONFIG** (defaults to **true** ) — Controls whether *all* settings (including OAuth) are loaded from the database rather than environment variables, once they've been saved to the DB.
1. **ENABLE\_OAUTH\_PERSISTENT\_CONFIG** (defaults to **false** ) — An *additional* gate specifically for OAuth settings. When set to false , OAuth settings with a config path starting with oauth. are **not** loaded from the database, even if ENABLE\_PERSISTENT\_CONFIG is true .
By default, OAuth env vars **will** take priority over database values because ENABLE\_OAUTH\_PERSISTENT\_CONFIG defaults to false . However, if you previously configured OAuth through the Admin Panel, those DB values may have been saved, and they will be loaded if ENABLE\_OAUTH\_PERSISTENT\_CONFIG is later set to true .

###### Symptoms:

```
*  Changes to environment variables don't take effect after restart
*  Authentication worked once but broke after configuration changes
*  "No token found in localStorage" errors after reconfiguration
```

**Solutions:**
1. **For Development/Testing:** Ensure ENABLE\_OAUTH\_PERSISTENT\_CONFIG=false (this is already the default) to always read from environment variables
1. **For Production:** Either:
\* Configure settings through Admin Panel instead of environment variables, OR
\* Keep ENABLE\_OAUTH\_PERSISTENT\_CONFIG=false (default) so that env vars always take priority for OAuth settings
1. **Fresh Start:** Delete the database volume and restart with correct configuration
📌 **Example for Docker Compose:**

```
environment:
  - ENABLE_OAUTH_PERSISTENT_CONFIG=false  # Forces reading from env vars (this is the default)
  - OAUTH_CLIENT_ID=your_client_id
  - OAUTH_CLIENT_SECRET=your_secret
  - OPENID_PROVIDER_URL=your_provider_url
```

##### 5. OAuth Misconfiguration on the Provider Side

Sometimes the issue is with the identity provider (e.g., Google, Okta, Auth0, Azure AD) not aligning with your WebUI's setup.
**Solutions:**
\* Verify your application is correctly registered with the OAUTH provider. Confirm:
\* **Redirect URIs exactly match your deployed WebUI address**
\* OIDC: https://your-domain/oauth/oidc/callback
\* Microsoft: https://your-domain/oauth/microsoft/callback
\* Google: https://your-domain/oauth/google/callback
\* Client ID and secret match the values given in your environment settings
\* Scopes and allowed grant types (e.g., authorization\_code ) are set as required by Open WebUI
\* Check the provider's logs—misconfigured apps will often show clear error messages there
📌 **Redirect URI Format Examples:**

```
✅ Correct: https://ai.company.com/oauth/oidc/callback
❌ Wrong: https://ai.company.com/oauth/callback/oidc
❌ Wrong: https://ai.company.com/callback
```

tip
When in doubt, recheck your provider registration and regenerate client secrets if needed.

##### 6. Server-Side Caching Issues

If you use Nginx (or another reverse proxy) with server-side caching, OAuth endpoints can misbehave. This often manifests as random or intermittent login bugs that are difficult to debug.
**Solutions:**
\* In your NGINX (or proxy) configuration:
\* Make sure to **exclude** the following endpoints from server-side caching:
\* /api , /oauth , /callback , /login , /ws , /websocket
\* Any critical login/auth endpoint must remain uncached!
\* Reload the proxy config after making changes
**Example NGINX Configuration:**

```
# Disable caching for login / OAuth / websockets endpoints
location ~* ^/(api|oauth|callback|login|ws|websocket) {
    proxy_no_cache 1;
    proxy_cache_bypass 1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_read_timeout 3600s;
    proxy_send_timeout 3600s;
    proxy_set_header Accept-Encoding "";
}
```

warning
Never cache OAuth or login endpoints. Caching can deliver stale tokens or corrupt sessions, causing unpredictable auth errors.

##### 7. Cookie Configuration Issues

**Common Problem:** Reverse proxy cookie settings can interfere with OAuth authentication, especially the HttpOnly and SameSite settings.

###### Symptoms:

```
*  "No token found in localStorage" errors
*  Redirect loops after successful authentication
*  Authentication works but immediately redirects to login page
```

**Solutions:**

###### For NGINX Proxy Manager:

```
# Remove or adjust problematic cookie settings

# ❌ Problematic:

# proxy_cookie_path / "/; Secure; HttpOnly; SameSite=None";

# ✅ Better:
proxy_cookie_flags ~ secure samesite=lax;

# or remove cookie manipulation entirely
```

###### Environment Variable Cookie Settings:

```
# Recommended cookie settings for OAuth
WEBUI_SESSION_COOKIE_SAME_SITE=lax
WEBUI_AUTH_COOKIE_SAME_SITE=lax
WEBUI_SESSION_COOKIE_SECURE=true  # Set to false if using HTTP
WEBUI_AUTH_COOKIE_SECURE=true     # Set to false if using HTTP
```

##### 8. Network Timeout Issues

OAuth providers may be slow to respond, causing timeout errors during the authentication handshake.

###### Symptoms:

```
*  httpcore.ReadTimeout errors in logs
*  CSRF Warning! State not equal in request and response errors
*  OAuth login fails intermittently
```

**Solutions:**

```
# Increase OAuth timeouts
AIOHTTP_CLIENT_TIMEOUT=600         # Very high number is needed here, since model responses that take a lot of time also rely on this timeout variable (e.g., a model that is reasoning for 5+ minutes)
AIOHTTP_CLIENT_TIMEOUT_OPENAI_MODEL_LIST=30
```

##### 9. Session State Mismatch (CSRF Errors)

Session cookies may not be properly maintained across the OAuth redirect flow.

###### Symptoms:

```
*  CSRF Warning! State not equal in request and response
*  mismatching_state errors in logs
*  Authentication appears successful but redirects to login
```

**Solutions:**
1. **Check Cookie Domain Configuration:**

```
# Ensure cookies are set for the correct domain
WEBUI_URL=https://your-exact-domain.com  # Must match exactly - check if you have a different value set in the admin panel
```

```
1.  **Session Configuration:**
```

```
# Ensure session handling is properly configured
WEBUI_SECRET_KEY=your_very_secure_random_key_here
OAUTH_SESSION_TOKEN_ENCRYPTION_KEY=another_secure_key_here
```

##### 10. Load Balancer and Multi-Instance Issues

In multi-instance deployments, OAuth sessions can fail if not properly synchronized.

###### Required Configuration for Clusters:

```
# Redis for session synchronization (required for multi-instance)
REDIS_URL=redis://your-redis:6379/0
WEBSOCKET_REDIS_URL=redis://your-redis:6379/0

# Shared secrets across all instances
WEBUI_SECRET_KEY=same_on_all_instances
OAUTH_SESSION_TOKEN_ENCRYPTION_KEY=same_on_all_instances

# WebSocket support for clusters
ENABLE_WEBSOCKET_SUPPORT=true
WEBSOCKET_MANAGER=redis
```

##### 11. Provider-Specific Configuration Issues

###### Microsoft Entra ID Common Issues:

**Problem:** Using generic OIDC variables instead of Microsoft-specific ones.
✅ **Correct Microsoft Setup:**

```
# Use Microsoft-specific variables, not generic OIDC
MICROSOFT_CLIENT_ID=your_azure_app_id
MICROSOFT_CLIENT_SECRET=your_azure_app_secret
MICROSOFT_CLIENT_TENANT_ID=your_tenant_id
MICROSOFT_OAUTH_SCOPE=openid email profile
MICROSOFT_REDIRECT_URI=https://your-domain/oauth/microsoft/callback

# Also required for a working Microsoft setup
OPENID_PROVIDER_URL=https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0/.well-known/openid-configuration
ENABLE_OAUTH_SIGNUP=true
```

###### Authentik Common Issues:

**Problem:** Incorrect provider URL format.
✅ **Correct Authentik Setup:**

```
OAUTH_CLIENT_ID=your_authentik_client_id
OAUTH_CLIENT_SECRET=your_authentik_client_secret
OPENID_PROVIDER_URL=https://your-authentik-domain/application/o/your-app-slug/.well-known/openid-configuration
OAUTH_PROVIDER_NAME=Authentik
OAUTH_SCOPES=openid email profile
```

#### Advanced Troubleshooting Tips

##### Check Token Storage Method

Recent versions of Open WebUI moved from URL-based tokens to cookie-based tokens. If you have authentication issues:
1. **Clear browser cookies and cache completely**
1. **Check browser Developer Tools:**
\* Look for oauth\_session\_id cookie (new method)
\* Check for any oauth\_id\_token cookie (legacy method)
\* Verify cookies have correct domain and path settings

##### Debugging OAuth Flow

Enable debug logging and trace the OAuth flow:

```
# Enable detailed logging
GLOBAL_LOG_LEVEL=DEBUG

# Check logs for these key steps:

# 1. GET /oauth/{provider}/login - Should return 302 redirect

# 2. User authenticates with provider

# 3. GET /oauth/{provider}/callback?code=... - Should return 200 or redirect

# 4. User should be logged in
```

##### Database Debugging

Check if user accounts are being created:

```
# Access your container
docker exec -it your-openwebui-container sh

# Check if users are created (adjust path to your data directory)
ls -la /app/backend/data/
```

##### Test Without Reverse Proxy

If using a reverse proxy, test OAuth directly against Open WebUI:
1. Temporarily expose Open WebUI port directly
1. Update OAuth provider redirect URI to point to direct port
1. Test authentication without proxy
1. If it works, the issue is in your proxy configuration

#### Pro Tip: Check the Logs

```
*  Look at backend logs and browser network errors. The first error usually points to the misconfiguration.
*  If unsure which side is the problem, try logging in from an incognito browser window and watch for blocked or failed requests.
```

##### Key Log Messages to Watch For:

```
*  OAuth callback error: mismatching_state → Session/cookie issue
*  httpcore.ReadTimeout → Network timeout issue
*  The email or password provided is incorrect → Often means OAuth completed but session wasn't established
*  404 on callback URLs → Redirect URI misconfiguration
```

#### Summary Checklist ✅

| Problem | Fix |
| --- | --- |
| 🔗 WebUI URL missing or wrong | Set correct WebUI URL in admin panel |
| 📝 Env var typo or missing | Double-check against official docs - avoid non-existent vars like OIDC\_CONFIG |
| 🚨 Missing OPENID\_PROVIDER\_URL | Always required for OIDC - set to provider's .well-known/openid-configuration |
| 🔄 Persistent config conflicts | Set ENABLE\_OAUTH\_PERSISTENT\_CONFIG=false or use admin panel |
| 🏢 Provider misconfigured | Confirm app registration, URIs & client IDs/secrets |
| 🧊 Proxy caching interfering | Exclude OAuth endpoints from all server-side caches |
| 🍪 Cookie configuration issues | Check reverse proxy cookie settings and env vars |
| ⏱ Timeout problems | Increase AIOHTTP\_CLIENT\_TIMEOUT values |
| 🔐 CSRF/session issues | Verify WEBUI\_SECRET\_KEY and session configuration |
| 🔀 Multi-instance problems | Configure Redis and shared secrets |
| Still stuck? | Check debug logs, test without proxy, verify provider setup |

By carefully configuring both your OAuth provider and your Open WebUI environment — and keeping critical login endpoints immune from caching — you can eliminate nearly all SSO/OAuth login problems.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/troubleshooting/sso.mdx)
[Previous RAG](https://docs.openwebui.com/troubleshooting/rag)
[Next Web Search](https://docs.openwebui.com/troubleshooting/web-search)
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