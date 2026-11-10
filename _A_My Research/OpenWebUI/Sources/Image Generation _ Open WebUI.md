---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

Image Generation / Open WebUI
[Skip to main content](https://docs.openwebui.com/troubleshooting/image-generation#__docusaurus_skipToContent_fallback)
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
\* Image Generation
On this page

### Image Generation

#### 🎨 Image Generation Troubleshooting

##### General Issues

```
*   **Image Not Generating**  (clicking generate produces no result, or an error appears in the chat):
    *  Check the  **Images**  settings in the  **Admin Panel**  >  **Settings**  >  **Images** . Ensure "Image Generation" is toggled  **ON** .
    *  Verify your  **API Key**  and  **Base URL**  (for OpenAI, ComfyUI, Automatic1111) are correct.
    *  Ensure the selected model is available and loaded in your backend service (e.g., check the ComfyUI or Automatic1111 console for activity).
    *   **Azure OpenAI** : If you see [ERROR: azure-openai error: Unknown parameter: 'response_format'.] , ensure you are using API version 2025-04-01-preview or later.
```

##### ComfyUI Issues

```
*   **Incompatible Workflow / JSON Errors**  (you see Invalid workflow or JSON parse errors after uploading a workflow):
    *   **API Format Required** : Open WebUI requires workflows to be in the  **API Format** .
    *  In ComfyUI:
        1. Click the "Settings" (gear icon).
        1. Enable "Enable Dev mode Options".
        1. Click "Save (API Format)" in the menu.
*   **Do not**  use the standard "Save" button or standard JSON export.
*   **Image Editing / Image Variation Fails**  (generating from text works, but editing or image-to-image fails silently):
    *  If you are using Image Editing or Image+Image generation, your custom workflow  **must**  have nodes configured to accept an input image (usually a LoadImage node replaced/linked effectively).
    *  Check the default "Image Editing" workflow in the Open WebUI settings for the required node structure to ensure compatibility.
```

##### Automatic1111 Issues

```
*   **Connection Refused / "Api Not Found"**  (Automatic1111 is running, but Open WebUI reports connection errors):
    *  Ensure you are running Automatic1111 with the --api flag enabled in your command line arguments.
*   **Docker Connectivity**  (Open WebUI can't reach Automatic1111 on localhost ):
    *  If Open WebUI is running in Docker and Automatic1111 is on your host machine:
        *  Use http://host.docker.internal:7860 as the Base URL.
        *  Ensure host.docker.internal is resolvable (added via --add-host=host.docker.internal:host-gateway in your Docker run command).
```

##### Environment Variables & Configuration

For advanced configuration, you can set the following environment variables.

###### General Image Generation

```
*  ENABLE_IMAGE_GENERATION : Set to true to enable image generation.
*  IMAGE_GENERATION_ENGINE : The engine to use (e.g., openai , comfyui , automatic1111 , gemini ).
*  IMAGE_GENERATION_MODEL : The model ID to use for generation.
*  IMAGE_SIZE : Default image size (e.g., 512x512 ).
```

###### Engine Specifics

**OpenAI / Compatible**
\* IMAGES\_OPENAI\_API\_BASE\_URL : Base URL for OpenAI-compatible image generation API.
\* IMAGES\_OPENAI\_API\_KEY : API Key for the image generation service.
**ComfyUI**
\* COMFYUI\_BASE\_URL : Base URL for your ComfyUI instance.
\* COMFYUI\_API\_KEY : API Key (if authentication is enabled).
\* COMFYUI\_WORKFLOW : Custom workflow JSON (must be API format).
**Automatic1111**
\* AUTOMATIC1111\_BASE\_URL : Base URL for your Automatic1111 instance.
\* AUTOMATIC1111\_API\_AUTH : Authentication credentials (username:password).
**Gemini**
\* IMAGES\_GEMINI\_API\_KEY : API Key for Gemini.
\* [View Gemini Configuration Guide](https://docs.openwebui.com/features/chat-conversations/image-generation-and-editing/gemini)
tip
For a complete list of environment variables and detailed configuration options, please refer to the [Environment Configuration Guide](https://docs.openwebui.com/reference/env-configuration).
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/troubleshooting/image-generation.md)
[Previous Custom CA Store](https://docs.openwebui.com/troubleshooting/custom-ca)
[Next Manual Migration](https://docs.openwebui.com/troubleshooting/manual-database-migration)
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