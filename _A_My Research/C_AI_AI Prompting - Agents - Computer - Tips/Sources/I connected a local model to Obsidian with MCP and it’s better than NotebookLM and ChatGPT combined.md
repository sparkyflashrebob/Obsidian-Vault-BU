---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

Sign in now

* Windows
* Android
* iPhone
* Tech Explained
* Security
* Productivity
* Creative
* EntertainmentStreaming
* Internet
  Home
  News
  Free Cheat Sheets
* Sign in
* Newsletter

### Follow Followed [Threads](https://www.makeuseof.com#threads) More Action Summary Sign in now I connected a local model to Obsidian with MCP and it’s better than NotebookLM and ChatGPT combined

By [Jayric Maning](https://www.makeuseof.com/author/jayric-maning/)Published 3 days ago
Jayric is a Forensic Science graduate with over five years of writing experience and a passion for reverse engineering and hardware.

His tech journey kicked off in childhood with an old hand-me-down Nokia N91, where he repackaged Java games like a Symbian port of Pokémon Blue to tweak TMs and Poké Dollars. By high school, he was flashing custom Android ROMs and trading modded games for lunch money, and in college, he learned C/C++ and electronics on a TI Tiva C LaunchPad, then went on to create DIY projects ranging from USB security keys to home automation devices.

Jayric now enjoys writing at MUO to keep sharing and learning about tech while honing his own craft. Outside of tech, he enjoys grinding CS2 and Dragon Nest, lifting weights, running daily 5Ks, and reading in his greenhouse.
[Sign in to your MUO account](https://www.makeuseof.com/author/jayric-maning/) Summary follow Follow followed Followed  [Thread](https://www.makeuseof.com#threads)  Here is a fact-based summary of the story contents: Try something different:
Using cloud-based AI tools can be frustrating. Since I primarily use Obsidian for note-taking, whenever I wanted to ask ChatGPT or NotebookLM about something, I had to copy my notes into a separate window. My personal knowledge base felt locked away from the AI that could actually help me synthesize it. I also worried about my private notes being sent to servers I don't control. Then I discovered MCP, and everything changed.
MCP stands for Model Context Protocol. It’s a general protocol for connecting AI models to external tools, but what makes it transformative for me is how well it integrates with Obsidian and LM Studio. Instead of copying and pasting, my local AI model can now read, search, and even write to my vault automatically. By using an MCP layer with my local tools, everything is now completely free, all my data stays on my computer, and AI is now integrated with my notes in ways cloud tools simply cannot.

#### Here's what I can do with my local Obsidian MCP setup

##### Direct AI to Obsidian vault integration

With my local Obsidian MCP setup, my tools now interact seamlessly. Instead of treating my vault as a collection of static files, MCP turns it into something my AI assistant can actively work with. It gives me a full set of Obsidian-specific tools that allow the model to read, search, modify, and organize my notes directly on my computer. Also, there are [benefits to running offline LLMs on your machine](https://www.makeuseof.com/i-now-use-this-offline-ai-assistant-instead-of-cloud-chatbots/) over using a paid AI service API, such as better privacy and free unlimited use.
My setup allows me to fetch the contents of any file instantly, whether I need to reference an old idea or pull details from a project note. If I want to gather multiple notes at once, I can batch-read entire folders. I can run simple or complex searches whenever I need to find something buried deep in my vault. I can also list recent changes, access my periodic notes, or browse entire directories when I need an overview of my work.
For more complex tasks, such as writing and editing. I can also set model reasoning to **High,** which should produce better results for tasks that require better context understanding and reasoning. The results can then be sent to the Obsidian MCP to directly append the new content to a specific note in my vault. All of this happens seamlessly without switching windows, copying text, or manually managing files. My local LLM can interact with my vault directly.
While it is possible to use Retrieval-Augmented Generation (RAG) as [a simpler and faster way to connect your Obsidian vault to your local LLM](https://www.makeuseof.com/obsidian-local-llm-integration/), it is limited to data retrieval only. This works if you only need to give context to your LLM from your notes, but if you want your model to directly interact with your Obsidian vault, you will need an MCP layer.

#### Setting it up was surprisingly simple

##### It only took a few minutes!

[The term MCP may sound intimidating at first](https://www.makeuseof.com/obsidian-local-llm-integration/), but the actual process of setting it up is actually pretty straightforward. You'll need to install a few things, connect them together, and everything should just work.
Start by installing Docker Desktop on your PC from the [official site](https://www.docker.com/products/docker-desktop/). Docker handles the backend infrastructure, so you don't have to manage servers or complicated configurations. Then, install the Obsidian MCP server inside Docker from the **MCP Toolkit** section.
Obsidian MCP will ask for your Obsidian API. To get the API, you’ll need to open Obsidian and install the **Local REST API** community plugin. This plugin lets external tools talk to your vault securely. Go to **Options** and grab your Obsidian **API key** from the plugin settings, add it to the Obsidian MCP API field, and hit check.
Now it's time to connect your local LLM to the MCP. Install LM Studio from their [official download site](https://lmstudio.ai/), and download your preferred AI model from the app. Then go back to the Docker **MCP Toolkit** , click on **Clients** , and download **LM Studio** . This will automatically connect the Obsidian MCP to LM Studio.
To start using the setup, launch LM Studio and host an AI model in the **Developer** tab. Once it's running, go to the **Chat** tab, click the plug icon at the bottom of the prompt box, and enable **mcp/mcp-docker** . Your chat interactions should now connect directly to your Obsidian vault!
While most chat models should work with this setup, I found that smaller 8B models did not comprehend the idea of directly interacting with the MCP and often gave instructions instead of actually doing the work. In my testing, models with reasoning capabilities, such as the OpenAI/gpt-oss-20b model, were able to interact with my Obsidian vault through the MCP server. So, I recommend starting with openai/gpt-oss-20b when first testing this setup.

##### Try it today

Give this a shot. If you already use Obsidian and have a decent PC, you have everything you need to start. The setup process only takes a few minutes, and once it is running, you will immediately notice how different this feels compared to cloud AI tools. You get an AI that actually understands your vault because it works directly inside it; you get your privacy back, and you gain real control over your tools. That combination saves time and makes your workflow feel smoother and more personal. Start setting it up today and see how it transforms the way you work with your notes.

* **Love MUO? We have so much more.** image/svg+xml Follow us on Google Discover! Productivity
* NotebookLM
* Obsidian
  Follow Followed Share [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fconnected-local-model-obsidian-mcp-better-than-notebooklm-chatgpt%2F%2F&src=sdkpreparse) [X](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fconnected-local-model-obsidian-mcp-better-than-notebooklm-chatgpt%2F%2F&src=sdkpreparse) [WhatsApp](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fconnected-local-model-obsidian-mcp-better-than-notebooklm-chatgpt%2F%2F&src=sdkpreparse) [Threads](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fconnected-local-model-obsidian-mcp-better-than-notebooklm-chatgpt%2F%2F&src=sdkpreparse) [Bluesky](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fconnected-local-model-obsidian-mcp-better-than-notebooklm-chatgpt%2F%2F&src=sdkpreparse) [LinkedIn](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fconnected-local-model-obsidian-mcp-better-than-notebooklm-chatgpt%2F%2F&src=sdkpreparse) [Reddit](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fconnected-local-model-obsidian-mcp-better-than-notebooklm-chatgpt%2F%2F&src=sdkpreparse) [Flipboard](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fconnected-local-model-obsidian-mcp-better-than-notebooklm-chatgpt%2F%2F&src=sdkpreparse) [Copy link](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fconnected-local-model-obsidian-mcp-better-than-notebooklm-chatgpt%2F%2F&src=sdkpreparse) [Email](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fconnected-local-model-obsidian-mcp-better-than-notebooklm-chatgpt%2F%2F&src=sdkpreparse) 
  Be the first to post Attachment(s) Please respect our [community guidelines](https://www.valnetinc.com/en/terms-of-use#community-guidelines). No links, inappropriate language, or spam.
  Your comment has not been saved
  [Send confirmation email](https://www.valnetinc.com/en/terms-of-use#community-guidelines)This thread is open for discussion.
  Be the first to post your thoughts.
* [Terms](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
* [Privacy](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
* [Feedback](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
  Recommended 6 days ago

##### [Don’t buy more RAM yet — try these Windows tweaks first](https://www.makeuseof.com/i-figured-out-why-my-windows-updates-kept-failing/)

5 days ago

##### [I reply to texts way faster now, and it's thanks to this brilliant app](https://www.makeuseof.com/i-figured-out-why-my-windows-updates-kept-failing/)

7 days ago

##### [This free audio tool made my cheap speakers sound dramatically better](https://www.makeuseof.com/i-figured-out-why-my-windows-updates-kept-failing/)

Nov 23, 2025

##### [These Android features make your phone a nightmare to steal — I enable them all](https://www.makeuseof.com/i-figured-out-why-my-windows-updates-kept-failing/)

##### Technology Explained

##### PC & Mobile

###### [The easiest way to rip lossless audio from CDs isn’t software — it’s this accessory](https://www.makeuseof.com/i-figured-out-why-my-windows-updates-kept-failing/)

###### 2 hours ago [I never expected smart glasses to replace my workout earbuds — but they did](https://www.makeuseof.com/i-never-expected-smart-glasses-to-replace-my-workout-earbuds-but-they-did/)

###### 4 hours ago [You don’t need to wait for the Steam Machine — you can build your own today](https://www.makeuseof.com/you-dont-need-to-wait-for-steam-machine-build-your-own-today/)

###### 21 hours ago [See More](https://www.makeuseof.com/category/technology-explained/) [Samsung’s Now bar is the best One UI feature in years — here’s why](https://www.makeuseof.com/category/technology-explained/)

###### 3 hours ago [I can't live without these 8 Android gestures](https://www.makeuseof.com/underrated-android-phone-gestures/)

###### 6 hours ago [I added a real web browser to Android Auto, and it changed everything](https://www.makeuseof.com/browser-on-android-auto/)

###### 6 hours ago [See More](https://www.makeuseof.com/category/pc-mobile/) [I didn’t expect USB-C AA batteries to be this good, but here we are](https://www.makeuseof.com/category/pc-mobile/)

###### [I tested 5 open-source Figma replacements — one absolutely crushed the rest](https://www.makeuseof.com/category/pc-mobile/)

###### [Want two displays? An HDMI splitter isn’t the answer](https://www.makeuseof.com/category/pc-mobile/)

* [Join Our Team](https://www.makeuseof.com/category/pc-mobile/)
* [Our Audience](https://www.makeuseof.com/category/pc-mobile/)
* [About Us](https://www.makeuseof.com/category/pc-mobile/)
* [Press & Events](https://www.makeuseof.com/category/pc-mobile/)
* [Media Coverage](https://www.makeuseof.com/category/pc-mobile/)
* [Contact Us](https://www.makeuseof.com/category/pc-mobile/)
* Follow Us
* [Advertising](https://www.makeuseof.com/category/pc-mobile/)
* [Careers](https://www.makeuseof.com/category/pc-mobile/)
* [Terms](https://www.makeuseof.com/category/pc-mobile/)
* [Privacy](https://www.makeuseof.com/category/pc-mobile/)
* [Policies](https://www.makeuseof.com/category/pc-mobile/)
  [MUO](https://www.makeuseof.com/category/pc-mobile/) is part of the [Valnet Publishing Group](https://www.valnetinc.com/en/) Copyright © 2025 Valnet Inc.