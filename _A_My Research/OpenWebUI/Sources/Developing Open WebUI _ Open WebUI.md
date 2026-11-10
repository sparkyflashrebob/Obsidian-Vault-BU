---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Developing Open WebUI / Open WebUI
[Skip to main content](https://docs.openwebui.com/getting-started/advanced-topics/development#__docusaurus_skipToContent_fallback)
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
\* [Scaling Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/scaling)
\* [Hardening Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening)
\* [Logging Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/logging)
\* [Developing Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/development)
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
\* [Advanced Topics](https://docs.openwebui.com/getting-started/advanced-topics/)
\* Developing Open WebUI
On this page

### Developing Open WebUI

**Run Open WebUI from source for development and testing.**
This guide covers setting up a local development environment with the frontend (SvelteKit) and backend (Python/FastAPI) running side by side. You will need two terminal sessions, one for each.
Don't need a full dev environment?
You can test the latest changes by running the [dev Docker image](https://docs.openwebui.com/getting-started/quick-start) instead: docker run -d -p 3000:8080 -v open-webui-dev:/app/backend/data --name open-webui-dev ghcr.io/open-webui/open-webui:dev

#### Prerequisites

| Requirement | Version |
| --- | --- |
| **Python** | 3.11+ |
| **Node.js** | 22.10+ |
| **Git** | Any recent version |

Separate your data
Never share your database or data directory between dev and production. Dev builds may include database migrations that are not backward-compatible.

#### 1. Clone the repository

```
git clone https://github.com/open-webui/open-webui.git
cd open-webui
```

#### 2. Frontend setup

In your **first terminal** , from the project root:

```
cp -RPp .env.example .env
npm install
npm run build
npm run dev
```

npm run build compiles the frontend and catches build-time errors early. npm run dev then starts the dev server at [http://localhost:5173](http://localhost:5173/). It will show a waiting screen until the backend is running.
tip
If npm install fails with compatibility warnings, run npm install --force .

#### 3. Backend setup

In your **second terminal** :

```
cd backend
```

Create and activate a virtual environment (Conda or venv):

```
# Option A: Conda
conda create --name open-webui python=3.11
conda activate open-webui

# Option B: venv
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

Install dependencies and start the server:

```
pip install -r requirements.txt -U
sh dev.sh
```

The backend starts at [http://localhost:8080](http://localhost:8080/). API docs are available at <http://localhost:8080/docs>.
Refresh the frontend at [http://localhost:5173](http://localhost:5173/) and you should see the full application.

#### Testing from another device

To access your dev instance from a phone or another computer on the same network:
1. Find your machine's LAN IP (e.g., 192.168.1.42 )
1. Add the origin to CORS in backend/dev.sh :

```
export CORS_ALLOW_ORIGIN="http://localhost:5173;http://localhost:8080;http://192.168.1.42:5173"
```

```
1. Restart the backend and browse to http://192.168.1.42:5173
```

#### Troubleshooting

##### "FATAL ERROR: Reached Heap Limit"

Node.js is running out of memory during the build. Increase the heap size before running frontend commands:

```
export NODE_OPTIONS="--max-old-space-size=4096"
npm run dev
```

Ensure at least 4 GB of RAM is available.

##### Port conflicts

If port 5173 or 8080 is already in use, find the conflicting process:

```
# macOS/Linux
lsof -i :5173

# Windows (PowerShell)
Get-Process -Id (Get-NetTCPConnection -LocalPort 5173).OwningProcess
```

Terminate the process or change the port in vite.config.js (frontend) or dev.sh (backend).

##### Icons not loading (CORS)

If static assets fail to load, configure CORS\_ALLOW\_ORIGIN in backend/dev.sh to include your frontend URL. See [CORS configuration](https://docs.openwebui.com/reference/env-configuration#cors_allow_origin) for details.

##### Hot reload not working

```
1. Verify both dev servers are running without errors
1. Hard refresh the browser (Ctrl+Shift+R / Cmd+Shift+R)
1. Reinstall frontend dependencies: rm -rf node_modules && npm install
1. Backend changes may require manually restarting sh dev.sh
```

#### Contributing workflow

```
1.  **Open a discussion first**  at [GitHub Discussions](https://github.com/open-webui/open-webui/discussions/new/choose) before writing code
1.  **Create a branch**  from dev for your work. Never commit directly to dev .
```

```
git checkout dev
git pull origin dev
git checkout -b my-feature-branch
```

```
1.  **Keep your branch synced**  by periodically merging from dev
1.  **Submit a pull request**  to the dev branch with a clear title and description
```

For contribution guidelines, see [Contributing](https://docs.openwebui.com/contributing).
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/getting-started/advanced-topics/development.md)
[Previous Logging Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/logging)
[Next 📖 Reference](https://docs.openwebui.com/reference/)
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