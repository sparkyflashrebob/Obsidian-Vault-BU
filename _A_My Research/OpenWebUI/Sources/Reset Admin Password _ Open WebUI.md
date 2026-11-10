---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Reset Admin Password / Open WebUI
[Skip to main content](https://docs.openwebui.com/troubleshooting/password-reset#__docusaurus_skipToContent_fallback)
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
\* Reset Admin Password
On this page

### Resetting Your Admin Password

Step-by-step guides for resetting your admin password in Docker and local installations.

#### For Docker Deployments

##### Step 1: Generate a New Password Hash

Create a bcrypt hash of your new password. Replace your-new-password with the password you want to use:

```
htpasswd -bnBC 10 "" your-new-password | tr -d ':\n'
```

note
The output will include a bcrypt hash with special characters. Any $ characters in the hash must be triple-escaped (replaced with \\ ) when used in the Docker command in Step 2.

##### Step 2: Update the Password in Docker

Replace HASH with the bcrypt hash from Step 1 (triple-escaping any $ characters) and admin@example.com with your admin email:

```
docker run --rm -v open-webui:/data alpine/socat EXEC:"bash -c 'apk add sqlite && echo UPDATE auth SET password='\''HASH'\'' WHERE email='\''admin@example.com'\''; | sqlite3 /data/webui.db'", STDIO
```

If the above command fails, use the alternate method below.

###### Alternate Docker Method

The one-liner above can fail in some environments because the alpine/socat image does not include bash . Use this step-by-step approach instead:
1. **Start an Alpine container with the Open WebUI volume mounted:**

```
docker run -it --rm -v open-webui:/data alpine
```

```
1.  **Install required tools:**
```

```
apk add apache2-utils sqlite
```

```
1.  **Generate the bcrypt hash:**
```

```
htpasswd -bnBC 10 "" your-new-password | tr -d ':'
```

```
1.  **Update the password:**
```

```
sqlite3 /data/webui.db
```

```
UPDATE auth SET password='HASH' WHERE email='admin@example.com';
-- Exit sqlite: Ctrl+D
```

#### For Local Installations

##### Step 1: Generate a New Password Hash

```
htpasswd -bnBC 10 "" your-new-password | tr -d ':\n'
```

##### Step 2: Update the Password

Navigate to the open-webui directory and run:

```
sqlite3 backend/data/webui.db "UPDATE auth SET password='HASH' WHERE email='admin@example.com';"
```

Replace HASH with the bcrypt hash from Step 1 and admin@example.com with your admin email.

#### Resetting All Data

If you want to **completely reset** Open WebUI — including all user data, settings, and passwords — delete the webui.db file.

##### Step 1: Locate webui.db

If you're unsure where webui.db is located, find it with a Python shell:

```
import os
import open_webui

# Show where the Open WebUI package is installed
print("Open WebUI is installed at:", open_webui.__file__)

# Construct the expected database path
db_path = os.path.join(os.path.dirname(open_webui.__file__), "data", "webui.db")

if os.path.exists(db_path):
    print("webui.db found at:", db_path)
else:
    print("webui.db not found at:", db_path)
    print("Try: find / -name 'webui.db' 2>/dev/null")
```

##### Step 2: Delete webui.db

```
rm /path/to/webui.db
```

warning
Deleting webui.db removes **all** stored data — user accounts, settings, chat history, and passwords. Only do this if you need a complete fresh start.
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/troubleshooting/password-reset.mdx)
[Previous Connection Errors](https://docs.openwebui.com/troubleshooting/connection-error)
[Next Audio](https://docs.openwebui.com/troubleshooting/audio)
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