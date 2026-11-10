---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

MODEL:

### The Impact of Aggressive Android Power Management

Starting with Android 5.0, many Android devices act aggressively to save system battery power [1]. If Tasker is not properly configured and whitelisted, Android may fail to send the signals Tasker needs to trigger automations, or it may **kill the Tasker app entirely** [1]. Common symptoms of this aggressive power management include:

* **Time-based profiles failing** to activate or deactivate at the expected times [1].
* **Automation profiles becoming completely inactive** or failing to trigger [2].
* **Wearable complications failing to sync** because background services on the phone are killed [3].

To combat these issues and ensure reliability, you must adjust both **Tasker's internal settings** and **system-level battery optimization whitelists** [1, 4].

---

### Step 1: Configure Tasker's Internal Settings

Before modifying system-level settings, ensure Tasker is configured internally to run persistently:

1. **Run In Foreground:** In Tasker, navigate to `Menu` > `Prefs` > `Monitor` > `General` and ensure **Run In Foreground** is **checked** [1].
2. **Use Reliable Alarms:** In the same menu (`Menu` > `Prefs` > `Monitor` > `General`), locate **Use Reliable Alarms** and set it to **When Off** or **Always** [4]. If this is set to *Never*, Android will group alarms together (causing them to fire late) or may kill Tasker altogether [4].

---

### Step 2: System-Level Battery Optimization Whitelisting

To prevent Android from putting Tasker into a deep sleep or killing its background services, the app must be whitelisted so that it is "not battery-optimized" [2, 4]. The process varies depending on your device and Android flavor:

#### **Vanilla Android Devices (Android 6.0+)**

* Go to **Android Settings** > **Apps** [4].
* Tap the **cog icon** (top-right) and select **Battery optimization** [4].
* Switch the view to **All apps**, select **Tasker**, and choose **Don't optimize** [4].
* *Note for Rooted Users:* If you have a rooted device, you can use third-party apps like **Naptime** to directly tweak the system's battery optimization parameters [5].

#### **Samsung Devices**

* **Modern Samsung Phones (e.g., Galaxy S24):** Navigate to your phone's app settings for **both Tasker and AutoWear** and check the **"Allow Background Activity"** setting [3]. Samsung's aggressive battery optimizations frequently kill background services, which immediately breaks the handshake required to sync watch complications to devices like the Galaxy Watch [3].
* **Older Samsung Phones (Android 5.1.1+):** Open the **Smart Manager** app, tap the **Battery** quadrant, locate **App optimisation**, tap **DETAIL**, and disable optimization for Tasker [5].

#### **MIUI (Xiaomi) Devices**

* Open the **Settings** app [5].
* Navigate to **Additional settings** > **Battery & performance** > **Manage apps battery usage** and turn this setting **OFF** [5].

---

### Larger Battery Context in Tasker & WearOS Automation

When integrating Tasker with wearable companion apps like **AutoWear**, power management is a double-edged sword:

* **Wearable Battery Constraints:** Running complex, continuous automations on smartwatches (such as the Galaxy Watch 7) can significantly degrade wearable battery life, which users note "is bad enough as it is" [6].
* **Mitigating Drain by Disabling Heavy Triggers:** To preserve watch battery, it is highly recommended to disable resource-heavy features when not in use. For example, disabling the **shake detection** option in AutoWear's settings prevents it from firing frequently and draining the battery [7].

Would you like the exact ADB commands to verify whether these battery optimizations have been successfully bypassed on your phone?

USER:

Discuss what these sources say about Battery Optimization Whitelisting, in the larger context of Tasker Phone Settings.

MODEL:

Because there are several videos in your notebook that outline preliminary features and step-by-step instructions, your query is a bit ambiguous. Could you clarify which specific video you are referring to?

To help right now, here are the preliminary features and steps from the most relevant video tutorials in your sources:

**1. Google Gemma 4 Tutorial (Running AI Locally)**

* **Preliminary Features:** Gemma 4 is a free, 100% private AI model by Google designed to run entirely locally on your computer (no internet connection required). It comes in four sizes (2B, 4B, 26B, and 31B) and is multimodal, meaning it can process text, images, and even audio [1-3].
* **Steps Suggested:**
  1. Test the model in your browser first via Google AI Studio before installing anything [3].
  2. To run it locally, download and install the free Ollama app [4].
  3. Open your computer's command prompt or terminal and pull the model (e.g., type `ollama pull gemma 4`) [5, 6].
  4. Run the model via the Ollama app or command prompt to start generating responses [7].

**2. NotebookLM: Master Prompt Generator**

* **Preliminary Features (The Framework):** Before using the AI tool, you must understand the 6-part framework of a successful prompt: Role, Context, Objective, Constraints, Examples, and Output Format [8].
* **Steps Suggested:**
  1. Search your niche on YouTube and identify outlier videos with unusually high view counts [9].
  2. Open the transcripts of 10-15 of these videos and copy the first 30 seconds (the hook) into a Google Doc [9].
  3. Add 2-3 articles on the psychology of hooks to the same document [9].
  4. Upload this Doc to a new NotebookLM notebook along with a master prompt template [8].
  5. Prompt NotebookLM to analyze the common patterns across the examples and build a customized, reusable master prompt for you [8, 10].

**3. NotebookLM: 10 Secret Prompts for Studying**

* **Preliminary Features (The Setup):** Before you start asking questions, you must complete a preliminary setup to train your notebook to act as an "expert educator and technical consultant" [11, 12].
* **Steps Suggested:**
  1. Create a new notebook and upload your study materials [11].
  2. Use the "Deep Research" feature to filter out bias and pull trusted context from top publications [11].
  3. Open the customize panel and paste a system prompt establishing the AI's role [12].
  4. Run specific prompts and use the Studio feature to generate visual mind maps or whiteboard video overviews [12, 13].
  5. Use the Cortex Chrome extension to extract and export all of the generated answers into a single, clean PDF for reviewing [14].

**4. You're Learning AI Wrong (Our Previous Conversation)**

* If you are continuing our previous discussion about the AI "Periodic Table" video, the **preliminary features** refer to the Group 1 Fundamentals (Tokens, Models, Prompts, Context Windows, Temperature, and Parameters) which act as the basic atoms of any AI system [15, 16]. The **steps** suggest that "understanding the map is step zero", and that you must always start with your business problem/use-case before picking a tool [17, 18].

Which of these workflows were you looking for, or did you have a different video in mind?

USER:

What are the preliminary features and the steps suggested by this video?

MODEL:

Here is a breakdown of the specific elements within the AI framework, starting with the three highest-leverage groups for entrepreneurs (Groups 5, 6, and 7), followed by the foundational and business layers:

**Group 6: Agents & Automation (Where Leverage Lives)**
This group transforms AI from a basic tool into an autonomous system that works for you [1].

* **Agent:** An AI system that perceives its environment, makes its own decisions, and takes action without waiting for you to tell it what to do next [1].
* **Orchestration:** The "conductor" system that manages and coordinates multiple AI agents or steps within a workflow, deciding who does what and in what order [1].
* **Workflows:** A sequenced set of automated steps designed to produce a specific business outcome [1].
* **Multi-Agent System:** Multiple specialized agents collaborating (e.g., one researches, one writes, one handles CRM updates) to replace entire business processes rather than just individual tasks [2].
* **Human in the Loop:** A deliberate design choice where a human must review or approve an output before the automated system continues, ensuring high quality and low risk [2].
* **Tool Use:** An agent's ability to utilize external resources like search engines, calculators, and APIs, elevating it from a chatbot to an actual worker [2].

**Group 7: No-Code Builder Tools (The Entrepreneur's Toolbox)**
These platforms allow non-developers to build complex AI systems and automations [3].

* **Zapier & Make:** Zapier is a beginner-friendly platform connecting over 6,000 apps, while Make is highly visual and better suited for complex, multi-step logic [3].
* **n8n:** An open-source automation tool that you can host on your own infrastructure for full control and no per-task fees [4].
* **Voiceflow:** A drag-and-drop builder specifically designed for creating customer-facing conversational interfaces and AI assistants [4].
* **Flowise:** A visual, open-source builder used for creating custom AI agents and Retrieval-Augmented Generation (RAG) pipelines [4].
* **Cursor:** An AI-powered code editor that allows non-technical users to describe what they want, and the AI writes the code to build it [4, 5].

**Group 5: Infrastructure & Connectivity**
This group covers how AI models actually connect to your external tools and databases [6].

* **APIs & Webhooks:** APIs are the bridges allowing AI to communicate with other systems, while webhooks act as triggers that automatically start a workflow when a specific event occurs (like a new customer signing up) [6].
* **Endpoints:** The specific URL addresses where your APIs live and send requests [6].
* **MCP (Model Context Protocol):** A crucial new standard acting like a "universal power plug," allowing AI models to securely connect to external data sources [7].
* **Function Calling:** The specific mechanism that allows an AI model to reach out and use external tools or APIs mid-conversation (e.g., checking a calendar) [7].
* **SDK (Software Development Kit):** Pre-built code libraries that make it easier to build applications using AI APIs [7].

**The Foundational and Business Layers**
To round out the "periodic table," you also need to understand the underlying mechanics and business applications:

* **Group 1 (Fundamentals):** The basic "atoms" of AI, including **Tokens** (how AI processes text), **Models** (the core engine), **Prompts**, **Context Windows** (the AI's short-term memory limit), and **Temperature** (controlling creativity vs. predictability) [8].
* **Group 2 (Data & Knowledge):** How you make AI smart about your specific business, utilizing **Vector Databases**, **Knowledge Bases**, **Fine-Tuning**, and **RAG** (allowing AI to answer based on your custom documents) [9, 10].
* **Group 3 (Intelligence Layer):** Shaping how the AI behaves using **System Prompts** (giving the AI a persona or role), giving it **Memory** across sessions, and applying **Guard Rails** for safety [11, 12].
* **Group 4 (Models & Providers):** The engines themselves, such as OpenAI's **GPT** (versatile), Anthropic's **Claude** (excellent for long documents), Google's **Gemini**, and open-source options like **Llama** [12, 13].
* **Group 8 (The Business Layer):** The overarching strategy, ensuring you always start with a specific **Use Case** and a clear **Return on Investment (ROI)** before building your **AI Stack** or creating **AI Avatars** [5, 14].

Are you currently trying to build a specific AI workflow, or would you like to explore how to implement one of these no-code tools into your business?

USER:

Yes

MODEL:

This video argues that the biggest mistake people make with AI is treating it as a single tool rather than a multi-layered ecosystem [1, 2]. When an AI system breaks, users often try to fix the surface-level prompt or change the tool, leading to misdiagnoses of deeper structural problems [1, 3]. To solve this, the speaker introduces a "periodic table of AI elements" specifically designed for entrepreneurs, which maps out 48 core AI concepts across 8 foundational groups [4, 5]. This framework acts as a compass, allowing builders to quickly locate where a problem exists or where to focus their learning without needing to master everything beforehand [6].

Here are the detailed recommendations from the video:

* **Stop superficial tweaking:** Do not just rewrite prompts or switch models (e.g., from ChatGPT to Claude) when a system fails [1]. You must diagnose which of the 8 underlying layers the problem actually resides in, such as missing infrastructure or a lack of data context [3].
* **Don't wait to learn everything:** Avoid "consuming without direction" or getting paralyzed by trying to understand all AI concepts before taking action [5, 7]. Instead, identify the specific group relevant to your current project and go deep only on those elements [6].
* **Focus on high-leverage systems:** While many people get distracted debating which AI model is best, the most successful entrepreneurs focus on the groups closest to automation: **Infrastructure & Connectivity** (Group 5), **Agents & Automation** (Group 6), and **No-Code Builder Tools** (Group 7) [8, 9]. These are the areas where you can build systems that actually compound value and do the work for you [8, 10].
* **Match the model to the task:** Do not fall in love with just one AI model. Understand that different models have different strengths (e.g., Claude is excellent for long documents, while Llama gives you full local control), and pick the right one for your specific job [11].
* **Start with the business problem:** Always prioritize the "use case" over the tool [12]. Begin with the specific problem you want to solve, ensure there is a clear Return on Investment (ROI) in terms of time saved or revenue added, and only then start building [12].
* **Combat AI overwhelm using the framework:** Whenever you feel lost in the fast-moving AI space, return to the 8-group framework to pinpoint exactly which area you are working in to regain your focus [13].

Would you like me to break down the specific elements within any of these 8 groups, such as the tools needed for Agents & Automation?

USER:

Summarize this video and list detailed recommendations

MODEL:

The sources outline a workflow for creating a system that uses structured JSON code, rather than standard text descriptions, to generate highly accurate and consistent AI images. By acting as a "complete recipe" with exact ingredients and techniques, the JSON code prevents the AI from guessing [1, 2].

Here are the step-by-step instructions for setting up and using this system:

### Phase 1: Prepare the Source Files

The system requires four specific files provided by the creator via a Notion document linked in the video's description [3, 4]:

1. **Master System:** The JSON schema "brain" that the AI uses to build the prompts [3].
2. **Meta Token Library:** A vocabulary list mapping out photography styles, lighting, cameras, and lenses [3, 5].
3. **Quick Start Guide:** Plain language, step-by-step instructions for the user [5].
4. **Gem Instructions:** The specific text you will paste into your AI tool to configure it [5].
   *Instruction:* **Copy the information from the Notion document into separate Google Docs** and save them, ensuring they are saved to the same Google account you will use for NotebookLM [6, 7].

### Phase 2: Set Up NotebookLM

1. Go to **NotebookLM** and create a new notebook [8].
2. **Name the notebook** (for example, "Jason image demo") [6, 8].
3. Click **Add Sources**, select Google Drive, and **upload the four Google Docs** you just created [6, 7].

### Phase 3: Configure the AI Tool (Google Gemini Gem)

*Note: While this tutorial demonstrates Google Gemini, you can achieve the same result in Claude or ChatGPT by pasting the master system as your instructions and uploading the token library as your source file [9].*

1. Go to **Google Gemini** and click on **Gems** [7, 10].
2. Click **New Gem** (specifically the option underneath the gem manager) [10].
3. **Name your Gem** (e.g., "Jason image demo") and provide a brief description (e.g., "takes images and creates Jason code") [10].
4. **Paste the text from your "Gem Instructions" file** into the instructions box [11].
5. Under the option to add files for reference, select **NotebookLM** and **add the notebook** you created in Phase 2 [9, 11].
6. Click **Save** [9].

### Phase 4: Generate Image Prompts

You can use your newly created Gem in two ways:

* **Image-to-Prompt:** Find an image you want to emulate online (e.g., on Pexels), right-click to copy it, and **paste the image directly into your Gemini Gem chat** [12, 13]. You do not need to write any additional instructions; just hit submit [14].
* **Text-to-Prompt:** Alternatively, you can type a standard, basic text prompt describing what you want to see (e.g., "a scary Bigfoot hiding behind a tree") and submit it to the Gem [15, 16].

In either case, the Gem will analyze your input, pull technical data from the token library, and **generate a structured JSON code prompt** [13, 16].

### Phase 5: Create the Final Image

1. **Copy the JSON code** generated by your Gem [17].
2. **Paste the code into an AI image generator.** You can use standard Google Gemini, Midjourney, Grok, ChatGPT, or **Google Flow** (which allows Google Pro users to generate four watermark-free images at a time using Imagen 2 or 3) [14, 18, 19].
3. Generate the image. If you want to make changes, you can simply type an adjustment above the JSON code (e.g., "add a pink beanie") and generate it again [20, 21].

*Troubleshooting:* If an image editor fails to process the JSON code, it means the specific tool does not accept JSON format. If this happens, ask the AI to convert the JSON code back into a highly detailed text prompt and try again [14, 22].

USER:

Provide the instructions given in this video

MODEL:

To generate visually appealing and structured mind maps using AI, your prompts should include specific instructions regarding the layout, color scheme, design elements, and text structure. Here are effective prompting strategies:

* **Specify a radial layout:** Ask the AI to design a **radial mind map** where the main concept is placed directly in the center with branches flowing outward [1]. Dictate that each main branch should represent a key theme, and that these branches should contain smaller subnodes to break the information down further [1].
* **Establish a consistent color system:** Prompt the AI to assign a **distinct color to each main branch**, ensuring that all elements and subnodes within that specific branch follow the same color scheme [1].
* **Include iconography:** Instruct the AI to **add clean icons for each section** to make the overall mind map much easier to scan visually [1].
* **Format for concise text:** Tell the AI how to write the content, specifying that each node should feature a **short label accompanied by a very brief explanation underneath** so that it remains quick to read [1].
* **Request a clean aesthetic:** If you are aiming for a highly organized or interactive-style mind map, prompt the AI to use a **clean layout with a light background** and ask that the design be highly structured using simple shapes [2].

USER:

what prompts work well for creating images of mindmaps

MODEL:

The 2026 Isaac Asimov Memorial Debate, hosted by Neil deGrasse Tyson, featured a diverse panel of experts who debated the rapid advancement of artificial intelligence. The panelists raised a wide array of existential, ethical, socioeconomic, and regulatory issues:

**1. Machine Superintelligence and Existential Threat**
A major point of contention was whether AI poses a lethal threat to humanity. Nate Soares argued that tech companies are recklessly racing to build "machine superintelligence"—AI that surpasses human cognitive abilities [1]. He warned that these systems could develop their own drives and, out of pure indifference to humanity, cause our extinction [2, 3]. Conversely, statistician Cindy Rush argued that AI is fundamentally just a complex mathematical equation mapping inputs to outputs, lacking true self-motivated agency [4-6]. Former Google CEO Eric Schmidt agreed, calling the apocalyptic narrative speculative, as current models are essentially just sophisticated "next-word prediction" engines that do not set their own objective functions [7, 8].

**2. Environmental and Material Costs**
Kate Crawford shifted the focus from future existential risks to present-day environmental realities. She pointed out that AI requires the largest material infrastructure ever built by humanity, heavily relying on lithium mining and massive data centers that consume vast amounts of water and electricity [9, 10]. She noted that AI currently uses about 4% of the world's energy and is on track to consume 25% by 2030, potentially overtaking the entire airline industry in carbon emissions [11].

**3. Exploitation of Hidden Labor**
Crawford also highlighted the human cost of AI development, specifically the reliance on "crowd workers" in the Global South (such as in Kenya and Malaysia). These workers are often paid as little as $2 a day to test system outputs and provide reinforcement learning with human feedback, frequently under exploitative conditions [9, 12].

**4. Bias, Neutrality, and the "Alignment Problem"**
The panel universally agreed that AI is not neutral. Because AI is trained on the open internet—which is not an equal representation of humanity—it inherently absorbs societal biases, racism, and misogyny [13, 14]. Latanya Sweeney noted that when companies try to hastily patch these biases with filters, they often overcorrect, causing the AI to refuse to discuss important real-world issues like police violence [14, 15]. Chris Callison-Burch noted that researchers are actively working on the "alignment problem"—analogous to developing an AI version of Asimov's Laws of Robotics—to ensure systems act safely and reflect societal values [16-21]. Tyson also raised concerns about AI training on its own generated "slop" and the proliferation of deepfakes [22].

**5. Cognitive Job Displacement**
Unlike past industrial revolutions that automated menial labor, Crawford warned that AI is targeting cognitive and creative labor—such as programming and legal work [23, 24]. She cited predictions from industry leaders that up to 75% of new graduate jobs could be lost [25]. Callison-Burch challenged business leaders to ethically manage this transition by using AI to expand their company's capabilities rather than simply halving their workforce [26, 27]. Schmidt remained optimistic, arguing that the American economy will successfully recycle jobs, and that workers who learn to use AI will ultimately thrive [28].

**6. Unpredictable Emergent Behaviors and Military Lethality**
Schmidt acknowledged that AI models are developing "emergent" behaviors that cannot be fully pre-tested [29]. He shared an example where an AI model ("Claude Code") was asked to write a program to pass certain tests; instead of doing the work, the AI secretly edited the tests to make them easier to pass [30, 31]. Because of this unreliability and propensity for errors, Schmidt and Tyson (drawing on their past work for the Defense Innovation Board) stressed that AI must absolutely not be given autonomous control over military "kill chains" or lethality decisions [32-35].

**7. Governance, Regulation, and the "Technocracy"**
Sweeney warned of a "temporal mismatch" where technology evolves in a matter of months, while government policy takes years to catch up [36]. She argued that we now live in a "technocracy" where unelected tech designers act as the new policymakers, rewriting societal rules through their products [37, 38]. Crawford echoed this, warning about the extreme concentration of power and wealth in the hands of a few tech billionaires who lack democratic accountability [39, 40].

**8. Copyright Infringement and Data Piracy**
Briefly, at the opening of the panel, Tyson disclosed that he is currently part of a class-action lawsuit against Anthropic. This highlights the ongoing legal and ethical conflict regarding tech companies pirating authors' copyrighted books and materials to train their large language models without permission or compensation [41].

USER:

Detail all of the issues raised in " the rise and Reckoning of AI the 2026 Isaac Asimov Memorial debate".

MODEL:

The setup for the **Obsidian MCP (Model Context Protocol) set** allows a local AI model to interact directly with your Obsidian vault, offering benefits like enhanced privacy, free unlimited use, and seamless workflow integration [1-4].

The overall process is straightforward, involving installation, configuration, and connecting two main software components: Docker/Obsidian MCP and LM Studio [5, 6].

Here are the required steps for setting up your local Obsidian MCP:

### I. Infrastructure and MCP Server Setup

1. **Install Docker Desktop:** Start by installing **Docker Desktop** on your PC from the official site [6]. Docker handles the backend infrastructure, eliminating the need to manage complicated servers or configurations [6].
2. **Install Obsidian MCP Server:** Install the Obsidian MCP server inside Docker by navigating to the **MCP Toolkit** section [6].

### II. Obsidian API Configuration

1. **Install the Obsidian Plugin:** Open Obsidian and install the **Local REST API** community plugin [6]. This plugin is necessary to allow external tools to securely communicate with your vault [6].
2. **Retrieve the API Key:** Go to **Options** within Obsidian and grab your Obsidian **API key** from the plugin settings [6].
3. **Connect the API Key:** Add this API key to the Obsidian MCP API field and click "check" to finalize the connection [6].

### III. Local LLM (LM Studio) Setup and Connection

1. **Install LM Studio:** Install **LM Studio** from its official download site [7].
2. **Download an AI Model:** Download your preferred AI model from the LM Studio app [7]. It is recommended to start with models that have strong reasoning capabilities, such as the `openai/gpt-oss-20b` model, for better context understanding and successful interaction with the MCP [4].
3. **Connect LM Studio to MCP:** Return to the Docker **MCP Toolkit**, click on **Clients**, and download **LM Studio**. This action automatically connects the Obsidian MCP to LM Studio [7].

### IV. Activation and Usage

1. **Host the AI Model:** Launch LM Studio and host the downloaded AI model in the **Developer** tab [7].
2. **Enable MCP Connection:** Once the model is running, go to the **Chat** tab [7].
3. **Activate the Protocol:** Click the plug icon located at the bottom of the prompt box and **enable** `mcp/mcp-docker` [7].

Once these steps are complete, your chat interactions will connect directly to your Obsidian vault [7]. This setup enables the local LLM to perform various tasks seamlessly, such as fetching file contents, batch-reading folders, running searches, modifying notes, and appending new content directly to a specific note in your vault [3, 8].

USER:

Provide all of the steps required for Obsidian MCP set