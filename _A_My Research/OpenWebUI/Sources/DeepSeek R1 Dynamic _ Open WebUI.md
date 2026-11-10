---
tags:
  - notebooklm-import
notebook: "OpenWebUI"
category: "research"
---

DeepSeek R1 Dynamic / Open WebUI
[Skip to main content](https://docs.openwebui.com/tutorials/integrations/llm-providers/deepseekr1-dynamic#__docusaurus_skipToContent_fallback)
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
\* [Integrations](https://docs.openwebui.com/tutorials/integrations/)
\* [LLM Providers](https://docs.openwebui.com/tutorials/integrations/llm-providers/deepseekr1-dynamic)
\* [Azure OpenAI with EntraID](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai/)
\* [DeepSeek R1 Dynamic](https://docs.openwebui.com/tutorials/integrations/llm-providers/deepseekr1-dynamic)
\* [Intel GPU (IPEX-LLM)](https://docs.openwebui.com/tutorials/integrations/llm-providers/ipex_llm)
\* [Monitoring](https://docs.openwebui.com/tutorials/integrations/llm-providers/deepseekr1-dynamic)
\* [Dev Tools](https://docs.openwebui.com/tutorials/integrations/llm-providers/deepseekr1-dynamic)
\* [LibreTranslate](https://docs.openwebui.com/tutorials/integrations/libre-translate)
\* [OneDrive & SharePoint](https://docs.openwebui.com/tutorials/integrations/onedrive-sharepoint)
\* [Notion MCP Integration](https://docs.openwebui.com/tutorials/integrations/mcp-notion)
\* [Redis Websocket Support](https://docs.openwebui.com/tutorials/integrations/redis)
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
\* [Integrations](https://docs.openwebui.com/tutorials/integrations/)
\* LLM Providers
\* DeepSeek R1 Dynamic
On this page

### DeepSeek R1 Dynamic

A huge shoutout to **UnslothAI** for their incredible efforts! Thanks to their hard work, we can now run the **full DeepSeek-R1** 671B parameter model in its dynamic 1.58-bit quantized form (compressed to just 131GB) on **Llama.cpp** ! And the best part? You no longer have to despair about needing massive enterprise-class GPUs or servers — it's possible to run this model on your personal machine (albeit slowly for most consumer hardware).
note
The only true **DeepSeek-R1** model on Ollama is the **671B version** available here: <https://ollama.com/library/deepseek-r1:671b>. Other versions are **distilled** models.
This guide focuses on running the **full DeepSeek-R1 Dynamic 1.58-bit quantized model** using **Llama.cpp** integrated with **Open WebUI** . For this tutorial, we'll demonstrate the steps with an **M4 Max + 128GB RAM** machine. You can adapt the settings to your own configuration.

#### Step 1: Install Llama.cpp

You can either:
\* [Download the prebuilt binaries](https://github.com/ggerganov/llama.cpp/releases)
\* **Or build it yourself** : Follow the instructions in the [Llama.cpp Build Guide](https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md)

#### Step 2: Download the Model Provided by UnslothAI

Head over to [Unsloth's Hugging Face page](https://huggingface.co/unsloth/DeepSeek-R1-GGUF) and download the appropriate **dynamic quantized version** of DeepSeek-R1. For this tutorial, we'll use the **1.58-bit (131GB)** version, which is highly optimized yet remains surprisingly functional.
tip
Know your "working directory" — where your Python script or terminal session is running. The model files will download to a subfolder of that directory by default, so be sure you know its path! For example, if you're running the command below in /Users/yourname/Documents/projects , your downloaded model will be saved under /Users/yourname/Documents/projects/DeepSeek-R1-GGUF .
To understand more about UnslothAI's development process and why these dynamic quantized versions are so efficient, check out their blog post: [UnslothAI DeepSeek R1 Dynamic Quantization](https://unsloth.ai/blog/deepseekr1-dynamic).
Here's how to download the model programmatically:

```
# Install Hugging Face dependencies before running this:

# pip install huggingface_hub hf_transfer

from huggingface_hub import snapshot_download

snapshot_download(
    repo_id = "unsloth/DeepSeek-R1-GGUF",  # Specify the Hugging Face repo
    local_dir = "DeepSeek-R1-GGUF",         # Model will download into this directory
    allow_patterns = ["*UD-IQ1_S*"],        # Only download the 1.58-bit version
)
```

Once the download completes, you'll find the model files in a directory structure like this:

```
DeepSeek-R1-GGUF/
├── DeepSeek-R1-UD-IQ1_S/
│   ├── DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf
│   ├── DeepSeek-R1-UD-IQ1_S-00002-of-00003.gguf
│   ├── DeepSeek-R1-UD-IQ1_S-00003-of-00003.gguf
```

info
🛠 Update paths in the later steps to **match your specific directory structure** . For example, if your script was in /Users/tim/Downloads , the full path to the GGUF file would be: /Users/tim/Downloads/DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1\_S/DeepSeek-R1-UD-IQ1\_S-00001-of-00003.gguf .

#### Step 3: Make Sure Open WebUI is Installed and Running

If you don't already have **Open WebUI** installed, no worries! It's a simple setup. Just follow the [Open WebUI documentation](https://docs.openwebui.com/). Once installed, start the application — we'll connect it in a later step to interact with the DeepSeek-R1 model.

#### Step 4: Serve the Model Using Llama.cpp

Now that the model is downloaded, the next step is to run it using **Llama.cpp's server mode** . Before you begin:
1. **Locate the llama-server binary.** If you built from source (as outlined in Step 1), the llama-server executable will be located in llama.cpp/build/bin . Navigate to this directory by using the cd command:

```
cd [path-to-llama-cpp]/llama.cpp/build/bin
```

Replace [path-to-llama-cpp] with the location where you cloned or built Llama.cpp. For example:

```
cd ~/Documents/workspace/llama.cpp/build/bin
```

```
1.  **Point to your model folder.**  Use the full path to the downloaded GGUF files created in Step 2. When serving the model, specify the first part of the split GGUF files (e.g., DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf ).
```

Here's the command to start the server:

```
./llama-server \
    --model /[your-directory]/DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1_S/DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf \
    --port 10000 \
    --ctx-size 1024 \
    --n-gpu-layers 40
```

tip
🔑 **Parameters to Customize Based on Your Machine:**
\* **--model :** Replace /[your-directory]/ with the path where the GGUF files were downloaded in Step 2.
\* **--port :** The server default is 8080 , but feel free to change it based on your port availability.
\* **--ctx-size :** Determines context length (number of tokens). You can increase it if your hardware allows, but be cautious of rising RAM/VRAM usage.
\* **--n-gpu-layers :** Set the number of layers you want to offload to your GPU for faster inference. The exact number depends on your GPU's memory capacity — reference Unsloth's table for specific recommendations.
For example, if your model was downloaded to /Users/tim/Documents/workspace , your command would look like this:

```
./llama-server \
    --model /Users/tim/Documents/workspace/DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1_S/DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf \
    --port 10000 \
    --ctx-size 1024 \
    --n-gpu-layers 40
```

Once the server starts, it will host a **local OpenAI-compatible API** endpoint at:

```
http://127.0.0.1:10000
```

info
🖥 **Llama.cpp Server Running**
After running the command, you should see a message confirming the server is active and listening on port 10000.
Be sure to **keep this terminal session running** , as it serves the model for all subsequent steps.

#### Step 5: Connect Llama.cpp to Open WebUI

```
1. Go to  **Admin Settings**  in Open WebUI.
1. Navigate to  **Connections > OpenAI Connections.**
1. Add the following details for the new connection:
*  URL: http://127.0.0.1:10000/v1 (or http://host.docker.internal:10000/v1 when running Open WebUI in docker)
    *  API Key: none
```

info
🖥 **Adding Connection in Open WebUI**
After running the command, you should see a message confirming the server is active and listening on port 10000.
Once the connection is saved, you can start querying **DeepSeek-R1** directly from Open WebUI! 🎉

#### Example: Generating Responses

You can now use Open WebUI's chat interface to interact with the **DeepSeek-R1 Dynamic 1.58-bit model** .

#### Notes and Considerations

```
*   **Performance:**  Running a massive 131GB model like DeepSeek-R1 on personal hardware will be  **slow** . Even with our M4 Max (128GB RAM), inference speeds were modest. But the fact that it works at all is a testament to UnslothAI's optimizations.
*   **VRAM/Memory Requirements:**  Ensure sufficient VRAM and system RAM for optimal performance. With low-end GPUs or CPU-only setups, expect slower speeds (but it's still doable!).
```

Thanks to **UnslothAI** and **Llama.cpp** , running one of the largest open-source reasoning models, **DeepSeek-R1** (1.58-bit version), is finally accessible to individuals. While it's challenging to run such models on consumer hardware, the ability to do so without massive computational infrastructure is a significant technological milestone.
⭐ Big thanks to the community for pushing the boundaries of open AI research.
Happy experimenting! 🚀
[Edit this page](https://github.com/open-webui/docs/blob/main/docs/tutorials/integrations/llm-providers/deepseekr1-dynamic.md)
[Previous Workload Identity Authentication](https://docs.openwebui.com/tutorials/integrations/llm-providers/azure-openai/workload-identity-auth)
[Next Intel GPU (IPEX-LLM)](https://docs.openwebui.com/tutorials/integrations/llm-providers/ipex_llm)
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