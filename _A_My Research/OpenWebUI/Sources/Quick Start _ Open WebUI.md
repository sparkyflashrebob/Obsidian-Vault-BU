---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Quick Start / Open WebUI
[Skip to main content](https://docs.openwebui.com/getting-started/quick-start#__docusaurus_skipToContent_fallback)
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
\* [Connect a Provider](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/)
\* [Connect an Agent](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent/)
\* [Understanding Settings](https://docs.openwebui.com/getting-started/quick-start/settings)
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
\* Quick Start
On this page

### Quick Start

Get Open WebUI running on your machine. Pick your preferred method below.
Open WebUI works on **macOS, Linux** (x86\_64 and ARM64, including Raspberry Pi and NVIDIA DGX Spark), and **Windows** .
\* **Docker:** Officially supported and recommended for most users. Requires [Docker](https://docs.docker.com/get-docker/) installed.
\* **Python:** Suitable for low-resource environments or manual setups
\* **Kubernetes:** Ideal for enterprise deployments requiring scaling and orchestration
\* Docker
\* Python
\* Kubernetes
\* Desktop
\* Third Party
\* Docker
\* Docker Compose
\* Extension
\* Podman
\* Quadlets
\* Kube Play
\* Swarm
\* WSL

#### Quick Start with Docker

info
**WebSocket** support is required. Ensure your network configuration allows WebSocket connections.
Docker Hub Now Available
Open WebUI images are published to **both** registries:
\* **GitHub Container Registry:** ghcr.io/open-webui/open-webui
\* **Docker Hub:** openwebui/open-webui
Both contain identical images. Replace ghcr.io/open-webui/open-webui with openwebui/open-webui in any command below.

##### 1. Pull the image

```
docker pull ghcr.io/open-webui/open-webui:main
```

##### 2. Run the container

```
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

| Flag | Purpose |
| --- | --- |
| -v open-webui:/app/backend/data | Persistent storage. Prevents data loss between restarts. |
| -p 3000:8080 | Exposes the UI on port 3000 of your machine. |

##### 3. Open the UI

Visit [http://localhost:3000](http://localhost:3000/).

#### Image Variants

| Tag | Use case |
| --- | --- |
| :main | Standard image (recommended) |
| :main-slim | Smaller image, downloads Whisper and embedding models on first use |
| :cuda | Nvidia GPU support (add --gpus all to docker run ) |
| :ollama | Bundles Ollama inside the container for an all-in-one setup |

##### Specific release versions

For production environments, pin a specific version instead of using floating tags:

```
docker pull ghcr.io/open-webui/open-webui:v0.8.6
docker pull ghcr.io/open-webui/open-webui:v0.8.6-cuda
docker pull ghcr.io/open-webui/open-webui:v0.8.6-ollama
```

#### Common Configurations

##### GPU support (Nvidia)

```
docker run -d -p 3000:8080 --gpus all -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:cuda
```

##### Bundled with Ollama

A single container with Open WebUI and Ollama together:
**With GPU:**

```
docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

**CPU only:**

```
docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

##### Connecting to Ollama on a different server

```
docker run -d -p 3000:8080 -e OLLAMA_BASE_URL=https://example.com -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

##### Single-user mode (no login)

```
docker run -d -p 3000:8080 -e WEBUI_AUTH=False -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

warning
You cannot switch between single-user mode and multi-account mode after this change.

#### Using the Dev Branch

tip
Testing dev builds is one of the most valuable ways to contribute. Run it on a test instance and report issues on [GitHub](https://github.com/open-webui/open-webui/issues).
The :dev tag contains the latest features before they reach a stable release.

```
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:dev
```

warning
**Never share your data volume between dev and production.** Dev builds may include database migrations that are not backward-compatible. Always use a separate volume (e.g., -v open-webui-dev:/app/backend/data ).
If Docker is not your preference, follow the [Developing Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/development).

#### Uninstall

```
1.  **Stop and remove the container:**
```

```
docker rm -f open-webui
```

```
1.  **Remove the image (optional):**
```

```
docker rmi ghcr.io/open-webui/open-webui:main
```

```
1.  **Remove the volume (optional, deletes all data):**
```

```
docker volume rm open-webui
```

#### Updating

To update your local Docker installation to the latest version, you can either use **Watchtower** or manually update the container.

##### Option 1: Using Watchtower

With [Watchtower](https://github.com/nicholas-fedor/watchtower), you can automate the update process:

```
docker run --rm --volume /var/run/docker.sock:/var/run/docker.sock nickfedor/watchtower --run-once open-webui
```

*(Replace open-webui with your container's name if it's different.)*

##### Option 2: Manual Update

```
1. Stop and remove the current container:
```

```
docker rm -f open-webui
```

```
1. Pull the latest version:
```

```
docker pull ghcr.io/open-webui/open-webui:main
```

```
1. Start the container again:
```

```
docker run -d -p 3000:8080 -v open-webui:/app/backend/data \
  -e WEBUI_SECRET_KEY="your-secret-key" \
  --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:main
```

Set WEBUI\_SECRET\_KEY
Without a persistent WEBUI\_SECRET\_KEY , you'll be logged out every time the container is recreated. Generate one with openssl rand -hex 32 .
For version pinning, rollback, automated update tools, and backup procedures, see the [full update guide](https://docs.openwebui.com/getting-started/updating).

### Docker Compose Setup

Using Docker Compose simplifies the management of multi-container Docker applications.
Docker Compose requires an additional package, docker-compose-v2 .
warning
**Warning:** Older Docker Compose tutorials may reference version 1 syntax, which uses commands like docker-compose build . Ensure you use version 2 syntax, which uses commands like docker compose build (note the space instead of a hyphen).

#### Example docker-compose.yml

Here is an example configuration file for setting up Open WebUI with Docker Compose:

```
services:
  openwebui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "3000:8080"
    volumes:
      - open-webui:/app/backend/data
volumes:
  open-webui:
```

##### Using Slim Images

For environments with limited storage or bandwidth, you can use the slim image variant that excludes pre-bundled models:

```
services:
  openwebui:
    image: ghcr.io/open-webui/open-webui:main-slim
    ports:
      - "3000:8080"
    volumes:
      - open-webui:/app/backend/data
volumes:
  open-webui:
```

note
**Note:** Slim images download required models (whisper, embedding models) on first use, which may result in longer initial startup times but significantly smaller image sizes.

#### Starting the Services

To start your services, run the following command:

```
docker compose up -d
```

#### Helper Script

A useful helper script called run-compose.sh is included with the codebase. This script assists in choosing which Docker Compose files to include in your deployment, streamlining the setup process.
note
**Note:** For Nvidia GPU support, you change the image from ghcr.io/open-webui/open-webui:main to ghcr.io/open-webui/open-webui:cuda and add the following to your service definition in the docker-compose.yml file:

```
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          count: all
          capabilities: [gpu]
```

This setup ensures that your application can leverage GPU resources when available.

#### Uninstall

To uninstall Open WebUI running with Docker Compose, follow these steps:
1. **Stop and Remove the Services:** Run this command in the directory containing your docker-compose.yml file:

```
docker compose down
```

```
1.  **Remove the Volume (Optional, WARNING: Deletes all data):**  If you want to completely remove your data (chats, settings, etc.):
```

```
docker compose down -v
```

Or manually:

```
docker volume rm _open-webui
```

```
1.  **Remove the Image (Optional):**
```

```
docker rmi ghcr.io/open-webui/open-webui:main
```

### Docker Desktop Extension

Docker has released an Open WebUI Docker extension that uses Docker Model Runner for inference. You can read their getting started blog here: [Run Local AI with Open WebUI + Docker Model Runner](https://www.docker.com/blog/open-webui-docker-desktop-model-runner/)
You can find troubleshooting steps for the extension in their Github repository: [Open WebUI Docker Extension - Troubleshooting](https://github.com/rw4lll/open-webui-docker-extension?tab=readme-ov-file#troubleshooting)
While this is an amazing resource to try out Open WebUI with little friction, it is not an officially supported installation method - you may run into unexpected bugs or behaviors while using it. For example, you are not able to log in as different users in the extension since it is designed to be for a single local user. If you run into issues using the extension, please submit an issue on the extension's [Github repository](https://github.com/rw4lll/open-webui-docker-extension).

### Using Podman

Podman is a daemonless container engine for developing, managing, and running OCI Containers.

#### Basic Commands

```
*   **Run a Container:**
```

```
podman run -d --name openwebui -p 3000:8080 -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main
```

```
*   **List Running Containers:**
```

```
podman ps
```

#### Networking with Podman

If networking issues arise (specifically on rootless Podman), you may need to adjust the network bridge settings.
Slirp4netns Deprecation
Older Podman instructions often recommended slirp4netns . However, slirp4netns is being **deprecated** and will be removed in **Podman 6** .
The modern successor is **pasta** , which is the default in Podman 5.0+.

##### Accessing the Host (Local Services)

If you are running Ollama or other services directly on your host machine, use the special DNS name **host.containers.internal** to point to your computer.

###### Modern Approach (Pasta - Default in Podman 5+)

No special flags are usually needed to access the host via host.containers.internal .

###### Legacy Approach (Slirp4netns)

If you are on an older version of Podman and pasta is not available:
1. Ensure you have [slirp4netns installed](https://github.com/rootless-containers/slirp4netns).
1. Start the container with the following flag to allow host loopback:

```
podman run -d --network=slirp4netns:allow_host_loopback=true --name openwebui -p 3000:8080 -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:main
```

##### Connection Configuration

Once inside Open WebUI, navigate to **Settings > Admin Settings > Connections** and set your Ollama API connection to: http://host.containers.internal:11434
Refer to the Podman [documentation](https://podman.io/) for advanced configurations.

#### Uninstall

To uninstall Open WebUI running with Podman, follow these steps:
1. **Stop and Remove the Container:**

```
podman rm -f openwebui
```

```
1.  **Remove the Image (Optional):**
```

```
podman rmi ghcr.io/open-webui/open-webui:main
```

```
1.  **Remove the Volume (Optional, WARNING: Deletes all data):**  If you want to completely remove your data (chats, settings, etc.):
```

```
podman volume rm open-webui
```

### Podman Quadlets (systemd)

Podman Quadlets allow you to manage containers as native systemd services. This is the recommended way to run production containers on Linux distributions that use systemd (like Fedora, RHEL, Ubuntu, etc.).

#### 🛠 Setup

```
1.  **Create the configuration directory:**  For a rootless user deployment:
```

```
mkdir -p ~/.config/containers/systemd/
```

```
1.  **Create the container file:**  Create a file named ~/.config/containers/systemd/open-webui.container with the following content:
```

```
[Unit]
Description=Open WebUI Container
After=network-online.target

[Container]
Image=ghcr.io/open-webui/open-webui:main
ContainerName=open-webui
PublishPort=3000:8080
Volume=open-webui:/app/backend/data

# Networking: Pasta is used by default in Podman 5+
# If you need to access host services (like Ollama on the host):
AddHost=host.containers.internal:host-gateway

[Service]
Restart=always

[Install]
WantedBy=default.target
```

```
1.  **Reload systemd and start the service:**
```

```
systemctl --user daemon-reload
systemctl --user start open-webui
```

```
1.  **Enable auto-start on boot:**
```

```
systemctl --user enable open-webui
```

#### 📊 Management

```
*   **Check status:**
```

```
systemctl --user status open-webui
```

```
*   **View logs:**
```

```
journalctl --user -u open-webui -f
```

```
*   **Stop service:**
```

```
systemctl --user stop open-webui
```

Updating
To update the image, simply pull the new version ( podman pull ghcr.io/open-webui/open-webui:main ) and restart the service ( systemctl --user restart open-webui ).

### Podman Kube Play Setup

Podman supports Kubernetes like-syntax for deploying resources such as pods, volumes without having the overhead of a full Kubernetes cluster. [More about Kube Play](https://docs.podman.io/en/latest/markdown/podman-kube-play.1.html).
If you don't have Podman installed, check out [Podman's official website](https://podman.io/docs/installation).

#### Example play.yaml

Here is an example of a Podman Kube Play file to deploy:

```
apiVersion: v1
kind: Pod
metadata:
  name: open-webui
spec:
  containers:
    - name: container
      image: ghcr.io/open-webui/open-webui:main
      ports:
        - name: http
          containerPort: 8080
          hostPort: 3000
      volumeMounts:
        - mountPath: /app/backend/data
          name: data
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName:  open-webui-pvc
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: open-webui-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```

#### Starting

To start your pod, run the following command:

```
podman kube play ./play.yaml
```

#### Using GPU Support

For Nvidia GPU support, you need to replace the container image with ghcr.io/open-webui/open-webui:cuda and need to specify the device (GPU) required in the pod resources limits as followed:

```
      [...]
      resources:
        limits:
          nvidia.com/gpu=all: 1
      [...]
```

important
To successfully have the open-webui container access the GPU(s), you will need to have the Container Device Interface (CDI) for the GPU you wish to access installed in your Podman Machine. You can check [Podman GPU container access](https://podman-desktop.io/docs/podman/gpu).

#### Docker Swarm

This installation method requires knowledge on Docker Swarms, as it utilizes a stack file to deploy 3 seperate containers as services in a Docker Swarm.
It includes isolated containers of ChromaDB, Ollama, and OpenWebUI. Additionally, there are pre-filled [Environment Variables](https://docs.openwebui.com/reference/env-configuration) to further illustrate the setup.
Why ChromaDB Runs as a Separate Container
This stack correctly deploys ChromaDB as a **separate HTTP server** container, with Open WebUI connecting to it via CHROMA\_HTTP\_HOST and CHROMA\_HTTP\_PORT . This is **required** for any multi-worker or multi-replica deployment.
The default ChromaDB mode (without CHROMA\_HTTP\_HOST ) uses a local SQLite-backed PersistentClient that is **not fork-safe** — concurrent writes from multiple worker processes will crash workers instantly. Running ChromaDB as a separate server avoids this by using HTTP connections instead of direct SQLite access.
If you plan to scale the openWebUI service to multiple replicas, you should also switch to PostgreSQL for the main database and set up Redis. See the [Scaling & HA guide](https://docs.openwebui.com/troubleshooting/multi-replica) for full requirements.
Choose the appropriate command based on your hardware setup:
\* **Before Starting** : Directories for your volumes need to be created on the host, or you can specify a custom location or volume. The current example utilizes an isolated dir data , which is within the same dir as the docker-stack.yaml .
\* **For example** :

```
mkdir -p data/open-webui data/chromadb data/ollama
```

```
*   **With GPU Support** :
```

###### Docker-stack.yaml

```
version: '3.9'

services:
  openWebUI:
    image: ghcr.io/open-webui/open-webui:main
    depends_on:
        - chromadb
        - ollama
    volumes:
      - ./data/open-webui:/app/backend/data
    environment:
      DATA_DIR: /app/backend/data
      OLLAMA_BASE_URLS: http://ollama:11434
      CHROMA_HTTP_PORT: 8000
      CHROMA_HTTP_HOST: chromadb
      CHROMA_TENANT: default_tenant
      VECTOR_DB: chroma
      WEBUI_NAME: Awesome ChatBot
      CORS_ALLOW_ORIGIN: "*" # This is the current Default, will need to change before going live
      RAG_EMBEDDING_ENGINE: ollama
      RAG_EMBEDDING_MODEL: nomic-embed-text-v1.5
      RAG_EMBEDDING_MODEL_TRUST_REMOTE_CODE: "True"
    ports:
      - target: 8080
        published: 8080
        mode: overlay
    deploy:
      replicas: 1
      restart_policy:
        condition: any
        delay: 5s
        max_attempts: 3

  chromadb:
    hostname: chromadb
    image: chromadb/chroma:0.5.15
    volumes:
      - ./data/chromadb:/chroma/chroma
    environment:
      - IS_PERSISTENT=TRUE
      - ALLOW_RESET=TRUE
      - PERSIST_DIRECTORY=/chroma/chroma
    ports:
      - target: 8000
        published: 8000
        mode: overlay
    deploy:
      replicas: 1
      restart_policy:
        condition: any
        delay: 5s
        max_attempts: 3
    healthcheck:
      test: ["CMD-SHELL", "curl localhost:8000/api/v1/heartbeat || exit 1"]
      interval: 10s
      retries: 2
      start_period: 5s
      timeout: 10s

  ollama:
    image: ollama/ollama:latest
    hostname: ollama
    ports:
      - target: 11434
        published: 11434
        mode: overlay
    deploy:
      resources:
        reservations:
          generic_resources:
            - discrete_resource_spec:
                kind: "NVIDIA-GPU"
                value: 0
      replicas: 1
      restart_policy:
        condition: any
        delay: 5s
        max_attempts: 3
    volumes:
      - ./data/ollama:/root/.ollama
```

```
*   **Additional Requirements** :
    1. Ensure CUDA is Enabled, follow your OS and GPU instructions for that.
    1. Enable Docker GPU support, see [Nvidia Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
    1. Follow the [Guide here on configuring Docker Swarm to with with your GPU](https://gist.github.com/tomlankhorst/33da3c4b9edbde5c83fc1244f010815c#configuring-docker-to-work-with-your-gpus)
*  Ensure  *GPU Resource*  is enabled in /etc/nvidia-container-runtime/config.toml and enable GPU resource advertising by uncommenting the swarm-resource = "DOCKER_RESOURCE_GPU" . The docker daemon must be restarted after updating these files on each node.
*   **With CPU Support** : Modify the Ollama Service within docker-stack.yaml and remove the lines for generic_resources:
```

```
    ollama:
  image: ollama/ollama:latest
  hostname: ollama
  ports:
    - target: 11434
      published: 11434
      mode: overlay
  deploy:
    replicas: 1
    restart_policy:
      condition: any
      delay: 5s
      max_attempts: 3
  volumes:
    - ./data/ollama:/root/.ollama
```

```
*   **Deploy Docker Stack** :
```

```
docker stack deploy -c docker-stack.yaml -d super-awesome-ai
```

#### Using Docker with WSL (Windows Subsystem for Linux)

This guide provides instructions for setting up Docker and running Open WebUI in a Windows Subsystem for Linux (WSL) environment.

##### Step 1: Install WSL

If you haven't already, install WSL by following the official Microsoft documentation:
[Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

##### Step 2: Install Docker Desktop

Docker Desktop is the easiest way to get Docker running in a WSL environment. It handles the integration between Windows and WSL automatically.
1. **Download Docker Desktop:** <https://www.docker.com/products/docker-desktop/>
1. **Install Docker Desktop:** Follow the installation instructions, making sure to select the "WSL 2" backend during the setup process.

##### Step 3: Configure Docker Desktop for WSL

```
1.  **Open Docker Desktop:**  Start the Docker Desktop application.
1.  **Enable WSL Integration:**
*  Go to  **Settings > Resources > WSL Integration** .
    *  Make sure the "Enable integration with my default WSL distro" checkbox is selected.
    *  If you are using a non-default WSL distribution, select it from the list.
```

##### Step 4: Run Open WebUI

Now you can run Open WebUI by following the standard Docker instructions from within your WSL terminal.

```
docker pull ghcr.io/open-webui/open-webui:main
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

##### Important Notes

```
*   **Run Docker Commands in WSL:**  Always run docker commands from your WSL terminal, not from PowerShell or Command Prompt.
*   **File System Access:**  When using volume mounts ( -v ), make sure the paths are accessible from your WSL distribution.
*  pip
*  uv
*  Conda
*  Venv
```

##### Installation with pip

The simplest way to install Open WebUI with Python.

###### 1. Install Open WebUI

```
pip install open-webui
```

###### 2. Start the server

```
open-webui serve
```

Open WebUI is now running at [http://localhost:8080](http://localhost:8080/).
'open-webui: command not found'?
1. If you used a virtual environment, make sure it's activated.
1. Try running directly: python -m open\_webui serve
1. To store data in a specific location: DATA\_DIR=./data open-webui serve

#### Uninstall

```
1.  **Uninstall the package:**
```

```
pip uninstall open-webui
```

```
1.  **Remove data (optional, deletes all data):**
```

```
rm -rf ~/.open-webui
```

### Updating with Python

To update your locally installed **Open-WebUI** package to the latest version using pip , follow these simple steps:

```
pip install -U open-webui
```

The -U (or --upgrade ) flag ensures that pip upgrades the package to the latest available version.
After upgrading, restart the server and verify it starts correctly:

```
open-webui serve
```

Multi-Worker Environments
If you run Open WebUI with UVICORN\_WORKERS > 1 (e.g., in a production environment), you **MUST** ensure the update migration runs on a single worker first to prevent database schema corruption.
**Steps for proper update:**
1. Update open-webui using pip .
1. Start the application with UVICORN\_WORKERS=1 environment variable set.
1. Wait for the application to fully start and complete migrations.
1. Stop and restart the application with your desired number of workers.
For version pinning, rollback, and backup procedures, see the [full update guide](https://docs.openwebui.com/getting-started/updating).

##### Installation with uv

The uv runtime manager ensures seamless Python environment management for applications like Open WebUI. Follow these steps to get started:

###### 1. Install uv

Pick the appropriate installation command for your operating system:
\* **macOS/Linux** :

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```
*   **Windows** :
```

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

###### 2. Run Open WebUI

Once uv is installed, running Open WebUI is a breeze. Use the command below, ensuring to set the DATA\_DIR environment variable to avoid data loss. Example paths are provided for each platform:
\* **macOS/Linux** :

```
DATA_DIR=~/.open-webui uvx --python 3.11 open-webui@latest serve
```

```
*   **Windows**  (PowerShell):
```

```
$env:DATA_DIR="C:\open-webui\data"; uvx --python 3.11 open-webui@latest serve
```

Why set DATA\_DIR?
Setting DATA\_DIR ensures your chats and settings are saved in a predictable location. If you don't set it, uvx might store it in a temporary folder that gets deleted when the process ends.

#### Uninstall

To remove Open WebUI when running with uvx :
1. **Stop the Server:** Press Ctrl+C in the terminal where it's running.
1. **Uninstall from UV:** Enter uv tool uninstall open-webui
1. **Available cleanup commands:** The uvx command runs the application ephemerally or from cache. To remove cached components:

```
uv cache clean
```

```
1.  **Remove Data (WARNING: Deletes all data):**  Delete your data directory (default is ~/.open-webui or the path set in DATA_DIR ):
```

```
rm -rf ~/.open-webui
```

### Updating with Python

To update your locally installed **Open-WebUI** package to the latest version using pip , follow these simple steps:

```
pip install -U open-webui
```

The -U (or --upgrade ) flag ensures that pip upgrades the package to the latest available version.
After upgrading, restart the server and verify it starts correctly:

```
open-webui serve
```

Multi-Worker Environments
If you run Open WebUI with UVICORN\_WORKERS > 1 (e.g., in a production environment), you **MUST** ensure the update migration runs on a single worker first to prevent database schema corruption.
**Steps for proper update:**
1. Update open-webui using pip .
1. Start the application with UVICORN\_WORKERS=1 environment variable set.
1. Wait for the application to fully start and complete migrations.
1. Stop and restart the application with your desired number of workers.
For version pinning, rollback, and backup procedures, see the [full update guide](https://docs.openwebui.com/getting-started/updating).

### Install with Conda

```
1.  **Create a Conda Environment:**
```

```
conda create -n open-webui python=3.11
```

```
1.  **Activate the Environment:**
```

```
conda activate open-webui
```

```
1.  **Install Open WebUI:**
```

```
pip install open-webui
```

```
1.  **Start the Server:**
```

```
open-webui serve
```

'open-webui: command not found'?
If your terminal says the command doesn't exist:
1. Ensure your conda environment is **activated** ( conda activate open-webui ).
1. If you still get an error, try running it via Python directly: python -m open\_webui serve
1. If you want to store your data in a specific place, use (Linux/Mac): DATA\_DIR=./data open-webui serve or (Windows): $env:DATA\_DIR=".\data"; open-webui serve

#### Uninstall

```
1.  **Remove the Conda Environment:**
```

```
conda remove --name open-webui --all
```

```
1.  **Remove Data (WARNING: Deletes all data):**  Delete your data directory (usually ~/.open-webui unless configured otherwise):
```

```
rm -rf ~/.open-webui
```

### Updating with Python

To update your locally installed **Open-WebUI** package to the latest version using pip , follow these simple steps:

```
pip install -U open-webui
```

The -U (or --upgrade ) flag ensures that pip upgrades the package to the latest available version.
After upgrading, restart the server and verify it starts correctly:

```
open-webui serve
```

Multi-Worker Environments
If you run Open WebUI with UVICORN\_WORKERS > 1 (e.g., in a production environment), you **MUST** ensure the update migration runs on a single worker first to prevent database schema corruption.
**Steps for proper update:**
1. Update open-webui using pip .
1. Start the application with UVICORN\_WORKERS=1 environment variable set.
1. Wait for the application to fully start and complete migrations.
1. Stop and restart the application with your desired number of workers.
For version pinning, rollback, and backup procedures, see the [full update guide](https://docs.openwebui.com/getting-started/updating).

### Using Virtual Environments

Create isolated Python environments using venv .

#### Venv Steps

```
1.  **Create a Virtual Environment:**
```

```
python3 -m venv venv
```

```
1.  **Activate the Virtual Environment:**
*  On Linux/macOS:
```

```
source venv/bin/activate
```

```
*  On Windows:
```

```
venv\Scripts\activate
```

```
1.  **Install Open WebUI:**
```

```
pip install open-webui
```

```
1.  **Start the Server:**
```

```
open-webui serve
```

'open-webui: command not found'?
If your terminal says the command doesn't exist:
1. Ensure your virtual environment is **activated** (Step 2).
1. If you still get an error, try running it via Python directly: python -m open\_webui serve
1. If you want to store your data in a specific place, use: DATA\_DIR=./data open-webui serve

#### Uninstall

```
1.  **Delete the Virtual Environment:**  Simply remove the venv folder:
```

```
rm -rf venv
```

```
1.  **Remove Data (WARNING: Deletes all data):**  Delete your data directory (usually ~/.open-webui unless configured otherwise):
```

```
rm -rf ~/.open-webui
```

### Updating with Python

To update your locally installed **Open-WebUI** package to the latest version using pip , follow these simple steps:

```
pip install -U open-webui
```

The -U (or --upgrade ) flag ensures that pip upgrades the package to the latest available version.
After upgrading, restart the server and verify it starts correctly:

```
open-webui serve
```

Multi-Worker Environments
If you run Open WebUI with UVICORN\_WORKERS > 1 (e.g., in a production environment), you **MUST** ensure the update migration runs on a single worker first to prevent database schema corruption.
**Steps for proper update:**
1. Update open-webui using pip .
1. Start the application with UVICORN\_WORKERS=1 environment variable set.
1. Wait for the application to fully start and complete migrations.
1. Stop and restart the application with your desired number of workers.
For version pinning, rollback, and backup procedures, see the [full update guide](https://docs.openwebui.com/getting-started/updating).
\* Helm

### Helm Setup for Kubernetes

Helm helps you manage Kubernetes applications.

#### Prerequisites

```
*  Kubernetes cluster is set up.
*  Helm is installed.
```

#### Helm Steps

```
1.  **Add Open WebUI Helm Repository:**
```

```
helm repo add open-webui https://open-webui.github.io/helm-charts
helm repo update
```

```
1.  **Install Open WebUI Chart:**
```

```
helm install openwebui open-webui/open-webui
```

```
1.  **Verify Installation:**
```

```
kubectl get pods
```

warning
If you intend to scale Open WebUI using multiple nodes/pods/workers in a clustered environment, you need to setup a NoSQL key-value database (Redis). There are some [environment variables](https://docs.openwebui.com/reference/env-configuration/) that need to be set to the same value for all service-instances, otherwise consistency problems, faulty sessions and other issues will occur!
**Important:** The default vector database (ChromaDB) uses a local SQLite-backed client that is **not safe for multi-replica or multi-worker deployments** . SQLite connections are not fork-safe, and concurrent writes from multiple processes will crash workers instantly. You **must** switch to an external vector database (PGVector, Milvus, Qdrant) via [VECTOR\_DB](https://docs.openwebui.com/reference/env-configuration#vector_db) , or run ChromaDB as a separate HTTP server via [CHROMA\_HTTP\_HOST](https://docs.openwebui.com/reference/env-configuration#chroma_http_host) .
For the complete step-by-step scaling walkthrough, see [Scaling Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/scaling). For troubleshooting multi-replica issues, see the [Scaling & HA guide](https://docs.openwebui.com/troubleshooting/multi-replica).
Critical for Updates
If you run Open WebUI with multiple replicas/pods ( replicaCount > 1 ) or UVICORN\_WORKERS > 1 , you **MUST** scale down to a single replica/pod during updates.
1. Scale down deployment to 1 replica.
1. Apply the update (new image version).
1. Wait for the pod to be fully ready (database migrations complete).
1. Scale back up to your desired replica count.
**Failure to do this can result in database corruption due to concurrent migrations.**

#### Access the WebUI

You can access Open WebUI by port-forwarding or configuring an Ingress.

##### Ingress Configuration (Nginx)

If you are using the **NGINX Ingress Controller** , you can enable session affinity (sticky sessions) to improve WebSocket stability. Add the following annotation to your Ingress resource:

```
metadata:
  annotations:
    nginx.ingress.kubernetes.io/affinity: "cookie"
    nginx.ingress.kubernetes.io/session-cookie-name: "open-webui-session"
    nginx.ingress.kubernetes.io/session-cookie-expires: "172800"
    nginx.ingress.kubernetes.io/session-cookie-max-age: "172800"
```

This ensures that a user's session remains connected to the same pod, reducing issues with WebSocket connections in multi-replica setups (though correct Redis configuration makes this less critical).

#### Uninstall

```
1.  **Uninstall the Helm Release:**
```

```
helm uninstall openwebui
```

```
1.  **Remove Persistent Volume Claims (WARNING: Deletes all data):**  Helm does not automatically delete PVCs to prevent accidental data loss. You must delete them manually if you want to wipe everything.
```

```
kubectl delete pvc -l app.kubernetes.io/instance=openwebui
```

##### Desktop App

Download the desktop app from [github.com/open-webui/desktop](https://github.com/open-webui/desktop). It runs Open WebUI natively on your system without Docker or manual setup.
Experimental
The desktop app is a **work in progress** and is not yet stable. For production use, install via **Docker** or **Python** .
\* Pinokio.computer

##### Pinokio.computer Installation

For installation via Pinokio.computer, visit their website:
<https://pinokio.computer/>
Support for this installation method is provided through their website.

#### After You Install

First Login
\* **Admin account:** The first account created gets **Administrator privileges** and controls user management and system settings.
\* **New sign-ups:** Subsequent registrations start with **Pending** status and require Administrator approval.
\* **Privacy:** All data, including login details, is stored locally on your device. Open WebUI makes no external requests. All models are private by default and must be explicitly shared.

##### Connect a Model Provider

Open WebUI needs at least one model provider to start chatting. Choose yours:

| Provider | Guide |
| --- | --- |
| **Ollama** (local models) | [Starting with Ollama →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-ollama) |
| **OpenAI** | [Starting with OpenAI →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai) |
| **Any OpenAI-compatible API** | [OpenAI-Compatible Providers →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible) |
| **Anthropic** | [Starting with Anthropic →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-anthropic) |
| **llama.cpp** | [Starting with llama.cpp →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-llama-cpp) |
| **vLLM** | [Starting with vLLM →](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-vllm) |

##### Connect an Agent

Want more than a model? AI agents can execute terminal commands, read and write files, search the web, maintain memory, and chain complex workflows — all through Open WebUI's familiar chat interface.

| Agent | Description | Guide |
| --- | --- | --- |
| **Hermes Agent** | Autonomous agent by Nous Research with terminal, file ops, web search, memory, and extensible skills | [Set up Hermes Agent →](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent/hermes-agent) |
| **OpenClaw** | Open-source self-hosted agent with shell access, file operations, web browsing, and messaging integrations | [Set up OpenClaw →](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent/openclaw) |

Learn more about how agents differ from providers in the [Connect an Agent overview →](https://docs.openwebui.com/getting-started/quick-start/connect-an-agent)

##### Explore Features

Once connected, explore what Open WebUI can do: [Features Overview →](https://docs.openwebui.com/features)

##### Experimental: Open Responses

Open WebUI has experimental support for the [Open Responses](https://www.openresponses.org/) specification. See the [Starting with Open Responses Guide](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-open-responses) to learn more.

#### Community

```
*  [Discord](https://discord.gg/5rJgQTnV4s) for questions, discussion, and support
*  [GitHub Issues](https://github.com/open-webui/open-webui/issues) for bug reports and feature requests
*   **Want to help?**  Test the [development branch](https://docs.openwebui.com/contributing) and report issues. No code required.
```

[Edit this page](https://github.com/open-webui/docs/blob/main/docs/getting-started/quick-start/index.mdx)
[Previous 🚀 Getting Started](https://docs.openwebui.com/getting-started/)
[Next Connect a Provider](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/)
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