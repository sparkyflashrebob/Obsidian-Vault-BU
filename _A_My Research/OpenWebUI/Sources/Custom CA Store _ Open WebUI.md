---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Custom CA Store / Open WebUI
[Skip to main content](https://docs.openwebui.com/troubleshooting/custom-ca#__docusaurus_skipToContent_fallback)
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
\* Custom CA Store

### Custom CA Store

warning
This tutorial is a community contribution and is not supported by the Open WebUI team. It serves only as a demonstration on how to customize Open WebUI for your specific use case. Want to contribute? Check out the contributing tutorial.
If you get an [SSL: CERTIFICATE\_VERIFY\_FAILED] error when trying to run OI, most likely the issue is that you are on a network which intercepts HTTPS traffic (e.g., a corporate network).
To fix this, you will need to add the new cert into OI's truststore.
**For pre-built Docker image** :
1. Mount the certificate store from your host machine into the container by passing --volume=/etc/ssl/certs/ca-certificates.crt:/etc/ssl/certs/ca-certificates.crt:ro as a command-line option to docker run
1. Force python to use the system truststore by setting SSL\_CERT\_FILE=/etc/ssl/certs/ca-certificates.crt (see <https://docs.docker.com/reference/cli/docker/container/run/#env>)
Example compose.yaml from [@KizzyCode](https://github.com/open-webui/open-webui/issues/1398#issuecomment-2258463210):

```
services:
  openwebui:
    image: ghcr.io/open-webui/open-webui:main
    volumes:
      - /var/containers/openwebui:/app/backend/data:rw
      - /etc/containers/openwebui/compusrv.crt:/etc/ssl/certs/ca-certificates.crt:ro
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    environment:
      - WEBUI_NAME=compusrv
      - ENABLE_SIGNUP=False
      - ENABLE_COMMUNITY_SHARING=False
      - WEBUI_SESSION_COOKIE_SAME_SITE=strict
      - WEBUI_SESSION_COOKIE_SECURE=True
      - ENABLE_OLLAMA_API=False
      - SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
```

The ro flag mounts the CA store as read-only and prevents accidental changes to your host CA store **For local development** :
You can also add the certificates in the build process by modifying the Dockerfile . This is useful if you want to make changes to the UI, for instance. Since the build happens in [multiple stages](https://docs.docker.com/build/building/multi-stage/), you have to add the cert into both
1. Frontend ( build stage):

```
COPY package.json package-lock.json .crt ./
ENV NODE_EXTRA_CA_CERTS=/app/.crt
RUN npm ci
```

```
1. Backend ( base stage):
```

```
COPY  /usr/local/share/ca-certificates/
RUN update-ca-certificates
ENV PIP_CERT=/etc/ssl/certs/ca-certificates.crt \
    REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/troubleshooting/custom-ca.md)
[Previous Performance & RAM](https://docs.openwebui.com/troubleshooting/performance)
[Next Image Generation](https://docs.openwebui.com/troubleshooting/image-generation)
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