---
tags:
  - notebooklm-import
notebook: "C_Obsidian info"
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

### Follow Followed [Threads](https://www.makeuseof.com#threads) More Action Summary Sign in now I let my local LLM organize my chaotic Obsidian vault and it and it nailed it

By [Jayric Maning](https://www.makeuseof.com/author/jayric-maning/)Published 1 day ago
Jayric is a Forensic Science graduate with over five years of writing experience and a passion for reverse engineering and hardware.

His tech journey kicked off in childhood with an old hand-me-down Nokia N91, where he repackaged Java games like a Symbian port of Pokémon Blue to tweak TMs and Poké Dollars. By high school, he was flashing custom Android ROMs and trading modded games for lunch money, and in college, he learned C/C++ and electronics on a TI Tiva C LaunchPad, then went on to create DIY projects ranging from USB security keys to home automation devices.

Jayric now enjoys writing at MUO to keep sharing and learning about tech while honing his own craft. Outside of tech, he enjoys grinding CS2 and Dragon Nest, lifting weights, running daily 5Ks, and reading in his greenhouse.
[Sign in to your MUO account](https://www.makeuseof.com/author/jayric-maning/) Summary follow Follow followed Followed  [Thread](https://www.makeuseof.com#threads)  Here is a fact-based summary of the story contents: Try something different:
Most Obsidian users start with perfect organizational habits. Every note goes into its designated folder, tags are applied consistently, and everything looks pristine. But life gets busy, and those habits quickly break down. Notes start piling up in random places, tags become inconsistent, and that beautiful vault transforms into a digital mess.
This is the reality for most personal knowledge management apps. They work great when you maintain perfect discipline, but the moment your organizational habits slip, chaos quickly takes over. We've all been there—promising ourselves that we'll organize everything properly this time, only to find hundreds of scattered notes a few months later.
It's completely normal to fall behind on organizing notes from time to time. The problem is that reorganizing a messy vault with hundreds or even thousands of notes is incredibly time-consuming. So, I started looking for AI-powered solutions and found a system that works. By using an AI-powered note tagger and an automated note-moving plugin, I can easily reorganize my notes whenever my vault gets messy.

#### My simple system for organizing messy vaults

##### How the AI-powered organization works

My system uses [Auto Note Mover](https://github.com/farux/obsidian-auto-note-mover) and [AI Tagger Universe](https://github.com/niehu2018/obsidian-ai-tagger-universe) running on Gemma 3, which I locally host using LM Studio.
The setup uses AI Tagger Universe to analyze the content of my notes and suggest relevant tags. After tagging each note, Auto Note Mover then automatically files the notes into pre-defined folders.
This simple two-step process means I always have a way to organize my notes whenever my vaults get messy. I can dump thoughts, notes, and random ideas anywhere in my vault. The AI reads through everything, understands its context, and applies consistent tags. Then those tags trigger automatic rules that move notes to their proper folders.

#### How I set up my AI-powered auto-sorting system in Obsidian

##### Setting up tools and plugins

You can grub the plugins from Obsidian's community plugins store. I searched for **Auto Note Mover** by faru and installed it first. This plugin automatically moves notes based on tags or titles I specify. Next, I installed **AI Tagger Universe** by Hu Nie. This plugin is a [smart way to link your notes in Obsidian](https://www.makeuseof.com/auto-link-notes-obsidian/). It uses AI to do the heavy lifting by analyzing my note content and suggesting tags, making sorting possible for this setup.
While AI Tagger Universe can run using an OpenAI API key, I always opt to [host my own offline AI using LM studio to keep my privacy](https://www.makeuseof.com/i-now-use-this-offline-ai-assistant-instead-of-cloud-chatbots/). So, I downloaded [LM Studio from the official site](https://lmstudio.ai/). With this free tool, I can have my own AI running on my own computer in just a couple of minutes.

##### Setting up the system

I started by configuring AI Tagger Universe first. [Hooking up a local LLM to my Obsidian vault](https://www.makeuseof.com/obsidian-local-llm-integration/) was a pretty straightforward process. After launching the app, I downloaded a chat model (Gemma 3 12B), clicked the **Developer** panel on the right sidebar with the terminal icon, loaded my LLM by selecting **Gemma 3 12B** from the dropdown menu, then enabled **CORS** in the model settings. Once the model was loaded, I went to AI Tagger Universe's options menu, selected **Local LLM** as my service type, then copied the **Local LLM Endpoint** and **Model Name** from LM Studio. Next, I hit **Test Connection** to confirm that the local AI and the Obsidian plugin were working together properly.
Now that the connection was established, I configured the AI's tagging behavior. Based on testing I've done, I found that predefining tags ensures consistency when filing notes into folders. So, I created a new note named "Tag List" in the root folder of my vault and filled it with all the tags I wanted the AI to use.
Then I went back to the plugin's options menu and set:

* **Tagging Mode** → **Use predefined tags only**
* **Tag Source** → **From predefined tags file**
* **Tag List Path** → (path to the Tag List note I just created)
  Before configuring Auto Note Mover, I created all the folders where I wanted my notes to be organized. Since I had already predefined my tags, I created one folder for each tag. This ensures that all notes with similar tags get filed into the same folder.
  Once I finished creating the folders, I configured **Auto Note Mover** . I opened the plugin options and created rules that matched my desired organization. For example, I have a rule that automatically moves any note tagged with **#technology** to my **00 - Technology** folder.
  I added as many rules as I wanted by clicking the plus ( **+** ) icon. The plugin supports both tags and title patterns, so I got creative with my sorting rules.

#### Organizing my entire vault

##### Cleaning up hundreds of my scattered notes

Before you start organizing, make sure to back up your vault. AI tools are powerful, but they can also be unpredictable at times. I always have a backup just in case something goes wrong.
To organize my entire vault, I pressed **Ctrl** **+** **P** and searched for "Generate tags for vault". Once I run that command, the AI begins tagging all my notes automatically. Depending on how many notes you have, this process may take a while, so grab a coffee and let the AI do its job. Once it starts, I get notifications as Auto Note Mover kicks in and begins filing my notes into their respective folders.
AI Tagger Universe isn't limited to my whole vault either. I can also use it to clear, collect, or generate tags for specific folders or even individual notes when needed.
Once everything is neatly organized, I usually turn off AI Tagger Universe and LM Studio to free up system resources. I still keep Auto Note Mover to automatically file new notes whenever I tag them to certain folders they belong in. This way, I can focus entirely on writing while the plugins keep everything in order. It’s a simple, hands-off setup that stays organized without any extra effort.

##### Start organizing your vault today

Overall, this system completely changed how I approach note-taking. Instead of stressing about perfect organization, I focus on capturing ideas and let the AI handle the cleanup. The setup takes less than an hour, but the time savings are massive. Don't be afraid to experiment with different models, tag systems, and folder structures until you find what works best for you. Your future self will thank you when finding an important note takes seconds instead of minutes.

* Productivity
* Obsidian
* Artificial Intelligence
  Follow Followed Share [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fletting-local-llm-organize-obsidian-notes%2F%2F&src=sdkpreparse) [X](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fletting-local-llm-organize-obsidian-notes%2F%2F&src=sdkpreparse) [LinkedIn](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fletting-local-llm-organize-obsidian-notes%2F%2F&src=sdkpreparse) [Reddit](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fletting-local-llm-organize-obsidian-notes%2F%2F&src=sdkpreparse) [Flipboard](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fletting-local-llm-organize-obsidian-notes%2F%2F&src=sdkpreparse) [Copy link](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fletting-local-llm-organize-obsidian-notes%2F%2F&src=sdkpreparse) [Email](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fletting-local-llm-organize-obsidian-notes%2F%2F&src=sdkpreparse) 
  Be the first to post Attachment(s) Please respect our [community guidelines](https://www.valnetinc.com/en/terms-of-use#community-guidelines). No links, inappropriate language, or spam.
  Your comment has not been saved
  [Send confirmation email](https://www.valnetinc.com/en/terms-of-use#community-guidelines)This thread is open for discussion.
  Be the first to post your thoughts.
* [Terms](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
* [Privacy](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
* [Feedback](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
  Recommended 4 days ago

##### [Adding in-wall USB outlets was the best upgrade I've made](https://www.makeuseof.com/in-wall-usb-outlets-best-upgrade/)

3 days ago

##### [This app makes Android Auto’s messaging finally usable](https://www.makeuseof.com/in-wall-usb-outlets-best-upgrade/)

2 days ago

##### [Android’s sideloading limits are its most anti-consumer move yet](https://www.makeuseof.com/in-wall-usb-outlets-best-upgrade/)

5 days ago

##### [I read bestsellers on Kindle for free thanks to my library](https://www.makeuseof.com/in-wall-usb-outlets-best-upgrade/)

##### Technology Explained

##### PC & Mobile

###### [Your power bank won’t last long if you keep doing these 6 things](https://www.makeuseof.com/in-wall-usb-outlets-best-upgrade/)

###### 7 hours ago [I built a 1500 Wh portable power station for half the price](https://www.makeuseof.com/i-built-a-1500-wh-portable-power-station-for-half-the-price/)

###### 16 hours ago [I solved my laptop’s CPU throttling in under an hour and it runs cooler now](https://www.makeuseof.com/solved-laptops-cpu-throttling-runs-cooler/)

###### 17 hours ago [See More](https://www.makeuseof.com/category/technology-explained/) [Windows 11 is great on paper — so why does everyone hate it?](https://www.makeuseof.com/category/technology-explained/)

###### 13 hours ago [These classic Windows programs are somehow still thriving in 2025](https://www.makeuseof.com/these-classic-windows-programs-still-thriving-in-2025/)

###### 1 day ago [These free tools make Windows File Explorer finally bearable](https://www.makeuseof.com/these-apps-make-file-explorer-better/)

###### 2 days ago [See More](https://www.makeuseof.com/category/pc-mobile/) [5 free apps I always install first on a new iPhone](https://www.makeuseof.com/category/pc-mobile/)

###### [This Netflix show is getting slammed — but I can't wait for the new season](https://www.makeuseof.com/category/pc-mobile/)

###### [ChatGPT’s new app integrations will change how you use it](https://www.makeuseof.com/category/pc-mobile/)

* [Join Our Team](https://www.makeuseof.com/category/pc-mobile/)
* [Our Audience](https://www.makeuseof.com/category/pc-mobile/)
* [About Us](https://www.makeuseof.com/category/pc-mobile/)
* [Press & Events](https://www.makeuseof.com/category/pc-mobile/)
* [Contact Us](https://www.makeuseof.com/category/pc-mobile/)
* Follow Us
* [Advertising](https://www.makeuseof.com/category/pc-mobile/)
* [Careers](https://www.makeuseof.com/category/pc-mobile/)
* [Terms](https://www.makeuseof.com/category/pc-mobile/)
* [Privacy](https://www.makeuseof.com/category/pc-mobile/)
* [Policies](https://www.makeuseof.com/category/pc-mobile/)
  [MUO](https://www.makeuseof.com/category/pc-mobile/) is part of the [Valnet Publishing Group](https://www.valnetinc.com/en/) Copyright © 2025 Valnet Inc.