---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Updating Open WebUI / Open WebUI
[Skip to main content](https://docs.openwebui.com/getting-started/updating#__docusaurus_skipToContent_fallback)
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
\* [Quick Start](https://docs.openwebui.com/getting-started/quick-start/)
\* [Sharing Open WebUI](https://docs.openwebui.com/getting-started/sharing)
\* [Updating Open WebUI](https://docs.openwebui.com/getting-started/updating)
\* [Advanced Topics](https://docs.openwebui.com/getting-started/advanced-topics/)
\* [📖 Reference](https://docs.openwebui.com/reference/)
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
\* [🚀 Getting Started](https://docs.openwebui.com/getting-started/)
\* Updating Open WebUI
On this page

### Updating Open WebUI

**Stay current without losing your data.**
Your data (chats, users, settings, uploads) lives in a Docker volume or local database, not inside the container. Updating Open WebUI means swapping the container image for a newer one. Your data stays exactly where it is.

#### Choose Your Update Strategy

Before running any commands, decide how you want to track releases. The right choice depends on how you use Open WebUI.

| Scenario | Recommended approach |
| --- | --- |
| **Personal / homelab** | Use the :main tag and pull manually when you want the latest |
| **Shared / team instance** | Pin a specific version (e.g. :v0.8.6 ) and use [Diun](https://docs.openwebui.com/getting-started/updating#diun) for update notifications |
| **Production / critical** | Pin a version, review [release notes](https://github.com/open-webui/open-webui/releases) before upgrading, test in staging first |

##### :main vs. Pinned Versions

The :main tag always points to the **latest build** . It's convenient but can include breaking changes without warning.
For stability, pin a specific release tag:

```
ghcr.io/open-webui/open-webui:v0.8.6
ghcr.io/open-webui/open-webui:v0.8.6-cuda
ghcr.io/open-webui/open-webui:v0.8.6-ollama
```

Browse all available tags on the [GitHub releases page](https://github.com/open-webui/open-webui/releases).

#### Before You Update

```
1.  **Back up your data**  (see [Backup & Restore](https://docs.openwebui.com/getting-started/updating#backup--restore) below). Especially important before releases with database migrations, which can be hard to undo.
1.  **Check the release notes**  for breaking changes.
1.  **Clear your browser cache**  after updating ( Ctrl+F5 / Cmd+Shift+R ) to avoid stale frontend assets.
```

Running multiple workers or replicas?
Run migrations on a single instance first: set UVICORN\_WORKERS=1 or ENABLE\_DB\_MIGRATIONS=false on all but one instance. See the [Scaling guide](https://docs.openwebui.com/getting-started/advanced-topics/scaling) for details.

#### Manual Update

```
*  Docker Run
*  Docker Compose
*  Python (pip)
```

```
# 1. Stop and remove the container (data in the volume is preserved)
docker rm -f open-webui

# 2. Pull the latest image (or replace :main with a pinned version)
docker pull ghcr.io/open-webui/open-webui:main

# 3. Recreate the container
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  -e WEBUI_SECRET_KEY="your-secret-key" \
  --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:main
```

For NVIDIA GPU support, add --gpus all to the docker run command.

```
docker compose pull
docker compose up -d
```

Make sure your docker-compose.yml includes WEBUI\_SECRET\_KEY :

```
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "3000:8080"
    volumes:
      - open-webui:/app/backend/data
    environment:
      - WEBUI_SECRET_KEY=your-secret-key
    restart: unless-stopped

volumes:
  open-webui:
```

```
pip install -U open-webui
```

The -U flag upgrades to the latest version. Then restart the server:

```
open-webui serve
```

Set WEBUI\_SECRET\_KEY to avoid logout on every update
Without a persistent WEBUI\_SECRET\_KEY , a new key is generated each time the container is recreated, invalidating all sessions. Generate one with openssl rand -hex 32 and keep it across updates. See the [Environment Variable Reference](https://docs.openwebui.com/reference/env-configuration) for details.

##### Verify the Update

After updating, confirm everything is working:
1. **Check version in logs:**

```
docker logs open-webui 2>&1 | head -20
```

```
1.  **Load the UI**  at [http://localhost:3000](http://localhost:3000/). You should see the login page.
1.  **If the UI looks broken** , clear your browser cache ( Ctrl+F5 / Cmd+Shift+R ).
1.  **If you see migration errors**  in the logs, check the [release notes](https://github.com/open-webui/open-webui/releases) for known issues and the [Connection Errors](https://docs.openwebui.com/troubleshooting/connection-error) troubleshooting page.
```

#### Rolling Back

If an update causes problems, you can go back to a previous version by pinning its tag.
\* Docker Run
\* Docker Compose
\* Python (pip)

```
docker rm -f open-webui
docker pull ghcr.io/open-webui/open-webui:v0.8.3
docker run -d -p 3000:8080 -v open-webui:/app/backend/data \
  -e WEBUI_SECRET_KEY="your-secret-key" \
  --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:v0.8.3
```

Change the image tag in your docker-compose.yml :

```
image: ghcr.io/open-webui/open-webui:v0.8.3
```

Then:

```
docker compose pull
docker compose up -d
```

```
pip install open-webui==0.8.3
open-webui serve
```

Database migrations are one-way
If the version you updated to ran a database migration, rolling back the container **does not** undo the migration. The older version may not work with the newer database schema. In that case, you need to restore from a backup taken **before** the update. For database-specific recovery, see the [Manual Database Migration](https://docs.openwebui.com/troubleshooting/manual-database-migration) guide.

#### Stay Notified About Updates

Instead of checking manually, use a tool to monitor for new releases. Options are listed from safest to most hands-on.
Recommendation
\* **Production / critical systems:** Diun (notification-only) + manual updates
\* **Managed environments:** WUD (visual dashboard + manual trigger)
\* **Homelabs / personal use:** Watchtower (fully automated)

| Feature | Diun | WUD | Watchtower |
| --- | --- | --- | --- |
| **Auto-updates containers** | ❌ | ❌ (manual via UI) | ✅ |
| **Web interface** | ❌ | ✅ | ❌ |
| **Notifications** | ✅ | ✅ | ✅ |
| **Docker 29+** | ✅ | ✅ | ✅ (forks) |
| **Resource usage** | Very Low | Medium | Low |

##### Diun

Notification-only. Alerts you when updates are available (email, Slack, Discord, Telegram, etc.) without touching your containers. You decide when and how to update.

```
services:
  diun:
    image: crazymax/diun:latest
    container_name: diun
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./data:/data
    environment:
      - TZ=America/New_York
      - LOG_LEVEL=info
      - DIUN_WATCH_WORKERS=10
      - DIUN_WATCH_SCHEDULE=0 */6 * * *  # Every 6 hours
      - DIUN_PROVIDERS_DOCKER=true
      - DIUN_NOTIF_MAIL_HOST=smtp.gmail.com
      - DIUN_NOTIF_MAIL_PORT=587
      - DIUN_NOTIF_MAIL_USERNAME=your-email@gmail.com
      - DIUN_NOTIF_MAIL_PASSWORD=your-app-password
      - DIUN_NOTIF_MAIL_FROM=your-email@gmail.com
      - DIUN_NOTIF_MAIL_TO=your-email@gmail.com
    restart: unless-stopped
```

See [Diun documentation](https://crazymax.dev/diun/) for full setup and notification options.

##### What's Up Docker (WUD)

Web UI for monitoring container updates and triggering them manually. See [WUD documentation](https://getwud.github.io/wud/) for setup.

##### Watchtower

Fully automated. Pulls new images and recreates containers without intervention.
warning
The original containrrr/watchtower is **no longer maintained** and fails with Docker 29+. Use the [nicholas-fedor/watchtower](https://watchtower.nickfedor.com/) fork instead.
warning
Automated updates can break your deployment if a release includes breaking changes or database migrations. Review release notes before auto-updating production systems, and always have a backup.
**One-time update:**

```
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  nickfedor/watchtower --run-once open-webui
```

**Continuous (check every 6 hours):**

```
docker run -d --name watchtower --restart unless-stopped \
  -v /var/run/docker.sock:/var/run/docker.sock \
  nickfedor/watchtower --interval 21600 open-webui
```

Set WATCHTOWER\_CLEANUP=true to auto-remove old images. See [Watchtower docs](https://watchtower.nickfedor.com/) for scheduling, notifications, and monitor-only mode.

#### Backup & Restore

All data lives in the open-webui Docker volume, including:
\* **Database** : chats, users, settings, admin configuration
\* **Uploaded files** : documents, images, knowledge base content
\* **Generated content** : image generation outputs, exported data

##### Backup

```
docker run --rm -v open-webui:/data -v $(pwd):/backup \
  alpine tar czf /backup/openwebui-$(date +%Y%m%d).tar.gz /data
```

Back up **before every update** and on a regular schedule (daily or weekly, depending on how actively you use Open WebUI).

##### Restore

caution
The restore command **deletes everything in the volume** before extracting the backup. Make sure you're restoring the right file.

```
docker stop open-webui
docker run --rm -v open-webui:/data -v $(pwd):/backup \
  alpine sh -c "rm -rf /data/* && tar xzf /backup/openwebui-YYYYMMDD.tar.gz -C /"
docker start open-webui
```

Replace YYYYMMDD with the actual date of your backup file.
For database-specific recovery, see the [Manual Database Migration](https://docs.openwebui.com/troubleshooting/manual-database-migration) guide.

#### Related Guides

```
*  [Scaling Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/scaling): multi-worker and multi-instance deployments
*  [Connection Errors](https://docs.openwebui.com/troubleshooting/connection-error): troubleshooting post-update connectivity issues
*  [Environment Variable Reference](https://docs.openwebui.com/reference/env-configuration): all configuration options including WEBUI_SECRET_KEY
*  [Release Notes](https://github.com/open-webui/open-webui/releases): changelog for every version
```

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/getting-started/updating.mdx)
[Previous Sharing Open WebUI](https://docs.openwebui.com/getting-started/sharing)
[Next Advanced Topics](https://docs.openwebui.com/getting-started/advanced-topics/)
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