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

### Follow Followed [Threads](https://www.makeuseof.com#threads) More Action Summary Sign in now I use this simple workflow to turn my random web reading into a library I can actually use

Image by Jayric Maning --no attributions required By [Jayric Maning](https://www.makeuseof.com/author/jayric-maning/)Published 12 hours ago
Jayric is a Forensic Science graduate with over five years of writing experience and a passion for reverse engineering and hardware.

His tech journey kicked off in childhood with an old hand-me-down Nokia N91, where he repackaged Java games like a Symbian port of Pokémon Blue to tweak TMs and Poké Dollars. By high school, he was flashing custom Android ROMs and trading modded games for lunch money, and in college, he learned C/C++ and electronics on a TI Tiva C LaunchPad, then went on to create DIY projects ranging from USB security keys to home automation devices.

Jayric now enjoys writing at MUO to keep sharing and learning about tech while honing his own craft. Outside of tech, he enjoys grinding CS2 and Dragon Nest, lifting weights, running daily 5Ks, and reading in his greenhouse.
[Sign in to your MUO account](https://www.makeuseof.com/author/jayric-maning/) Summary follow Follow followed Followed  [Thread](https://www.makeuseof.com#threads)  Here is a fact-based summary of the story contents: Try something different:
Like most knowledge workers, I spend hours reading articles, blog posts, and research online. For years, this felt like pouring water through a sieve. I'd read something fascinating, bookmark it, then never find it again when I needed it. My browser bookmarks basically became a digital graveyard.
Everything changed when I set up Obsidian's Web Clipper properly. Instead of saving links that might break, I capture full text and context in a format I control. The key principle is "clip once, reuse often”. Every article becomes part of a growing library where I can surface old insights for new projects and build connections across different domains.

#### Why traditional bookmarking fails

Screenshot by Jayric Maning --no attributions required
Most people treat online content as disposable. We read, maybe bookmark, and move on. But knowledge compounds when you build connections between ideas, which is impossible when everything lives in isolated browser tabs or forgotten bookmark folders.
I realized this when I kept re-reading the same articles because I couldn't remember the key insights. Even worse, I'd find perfect supporting material for projects buried in bookmark folders with unhelpful titles like "Interesting AI article."
Another big problem with bookmarks is reliability. Websites disappear, move URLs, or hide content behind paywalls. I've lost count of bookmarked articles that returned "404 Not Found" errors when I actually needed them.
The Web Clipper changes this dynamic. When I save a machine learning article, it doesn't sit in isolation. Obsidian's search helps me rediscover that content and connect it to new ideas. I can annotate and extend clipped articles over time, creating compounding knowledge where each addition becomes more valuable by connecting to everything saved before. This combination is one of the [reasons why people stop looking for other note-taking apps after trying Obsidian](https://www.makeuseof.com/stop-switching-note-apps-choose-obsidian/).

#### How I set up my Obsidian Web Clipper library

##### Simple and effective clipper setup

First, install the [Obsidian Web Clipper](https://obsidian.md/clipper) extension from your browser's store. Once installed, open Obsidian and create a folder in the root of your vault. I’ll name mine “Web Clips”, but you can name it anything you want.
Screenshot by Jayric Maning --no attributions required
Then go back and open the Obsidian Web Clipper extension. Click the Obsidian icon in your toolbar and hit the gear icon for settings. In the **General** tab, add your vault name exactly as it appears in Obsidian. This is case-sensitive and must match precisely.
Screenshot by Jayric Maning --no attributions required
If your vault is "Main Knowledge Base", or “My vault” type exactly that. Wrong spelling means nothing saves properly.

##### Setting up the default template

Templates control how web content gets formatted in Obsidian. The default template works but isn't optimized for research workflows. Click on **Templates** in the sidebar, then select **Default** to edit it.
For the **Note name** format, I use:
{{published|date:"YYYY-MM-DD"}} {{title|safe\_name}}

Screenshot by Jayric Maning --no attributions required
This creates titles like "2024-03-15 How AI Transforms Knowledge Management" with publication date first for easy chronological sorting.
Set **Note location** to a dedicated folder like "Web Clips" to keep everything organized. This separation makes weekly review sessions much easier.

##### Configuring properties and metadata

After setting Note location, continue scrolling down until your reach the **Properties** section. Properties define what metadata gets captured with each article. Here are the typical properties I like adding to my web clippings:

* **source\_url:** Captures original URL for citations and returning to source
* **author** : Automatically pulls article author when available
* **publication\_date** : Tracks when content was published
* **status** : Defaults to "unprocessed" for tracking review progress
* **tags:** Starts with "web-clip" but I add specific tags during clipping
  Screenshot by Jayric Maning --no attributions required
  After adding all the properties, we still need to define how it is formatted during clipping. Here’s what I use with the set properties:

# {{title}}

**Author:** {{author}}
**Published:** {{published|date:"YYYY-MM-DD"}}
**Source:** [{{title}}](%7B%7Burl%7D%7D)
**Status:** #unprocessed

## Content

{{content}}

## My Notes

*Add your thoughts and connections here*
You can pretty much add any properties you want depending on the style of content you typically read. I stick to a simple format so as not to make things more complicated than they should.

#### Using my clipper setup

##### The quick clip process

Once configured, clipping takes seconds. When reading an article worth saving, I click the Web Clipper icon. The extension analyzes the page and populates all configured fields automatically.
The interface shows exactly what will be saved: cleaned article content, metadata properties, and note name preview. If everything looks good, click **Add to Obsidian** and the article saves in just a second.
Screenshot by Jayric Maning --no attributions required
You can then open it in Obsidian. As you can see, it’s formatted closely to the original site, complete with links, images, and all the properties defined within the extension.
Obsidian’s powerful search and tagging functionality is what makes this setup so convenient to use. One way I like to use my web clip library is by changing the status property to "processed" after reading. This allows me to easily find unread articles simply by clicking on the magnifying glass button on the toolbar and searching for “unprocessed”.
Screenshot by Jayric Maning --no attributions required
Aside from finding unread web clipping, Obsidian's search also works across all saved text, so I can find articles by searching phrases, concepts, or vague recollections. The linking system is even more powerful. Whenever I see a trend in the articles I’m clipping, I always fill out the tag properties to link web clips together. And when working on a project, I can even add my clipped sources to a canvas just like [how I configure Obsidian note charts to a single dashboard](https://www.makeuseof.com/turned-my-obsidian-notes-into-charts-love-tracking-progress/) for easy viewing and tracking.
Screenshot by Jayric Maning --no attributions required
I use tags to resurface old content. Weekly, I search clipped articles on specific topics and create summary notes pulling together related insights. This reveals patterns and connections that weren't obvious initially.

##### From scattered reading to systematic knowledge

Web Clipper completely changed how I read online. Instead of losing great articles in messy bookmark folders, I finally found a way to actually use what I save. Articles I clipped randomly started popping up in my work research. Now my casual browsing feeds my professional work instead of vanishing into a bookmark graveyard. Every article I save makes my knowledge base stronger, and I can find exactly what I need when I need it.

* [Productivity](https://www.makeuseof.com/turned-my-obsidian-notes-into-charts-love-tracking-progress/)
* [Internet](https://www.makeuseof.com/turned-my-obsidian-notes-into-charts-love-tracking-progress/)
* [Obsidian](https://www.makeuseof.com/turned-my-obsidian-notes-into-charts-love-tracking-progress/) 
  Follow Followed Share [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Forganize-random-web-reading-obsidian%2F%2F&src=sdkpreparse) [X](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Forganize-random-web-reading-obsidian%2F%2F&src=sdkpreparse) [LinkedIn](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Forganize-random-web-reading-obsidian%2F%2F&src=sdkpreparse) [Reddit](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Forganize-random-web-reading-obsidian%2F%2F&src=sdkpreparse) [Flipboard](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Forganize-random-web-reading-obsidian%2F%2F&src=sdkpreparse) [Copy link](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Forganize-random-web-reading-obsidian%2F%2F&src=sdkpreparse) [Email](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Forganize-random-web-reading-obsidian%2F%2F&src=sdkpreparse) 
  Be the first to post Attachment(s) Please respect our [community guidelines](https://www.valnetinc.com/en/terms-of-use#community-guidelines). No links, inappropriate language, or spam.
  Your comment has not been saved
  [Send confirmation email](https://www.valnetinc.com/en/terms-of-use#community-guidelines)This thread is open for discussion.
  Be the first to post your thoughts.
* [Terms](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
* [Privacy](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
* [Feedback](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
  Recommended 4 days ago

##### [I tweaked 10 settings and now my Kindle feels even more like paper](https://www.makeuseof.com/settings-make-kindle-like-paper/)

6 days ago

##### [Using this Google Sheets function to visualize my data is oddly satisfying](https://www.makeuseof.com/settings-make-kindle-like-paper/)

6 days ago

##### [This Power Automate workflow keeps my Windows desktop spotless](https://www.makeuseof.com/settings-make-kindle-like-paper/)

6 days ago

##### [Google just solved Windows 11’s biggest headache in one move](https://www.makeuseof.com/settings-make-kindle-like-paper/)

##### Technology Explained

##### PC & Mobile

###### [Why does every device I buy want me to pay monthly?](https://www.makeuseof.com/settings-make-kindle-like-paper/)

###### 6 hours ago [Your portable power station won’t last long if you do these 6 things](https://www.makeuseof.com/portable-power-station-wont-last-long-if-you-do-these-things/)

###### 1 day ago [I turned my broken laptop into the most useful device in my home without fixing it](https://www.makeuseof.com/turn-broken-laptop-into-home-server-without-fixing/)

###### 2 days ago [See More](https://www.makeuseof.com/category/technology-explained/) [This open-source tool takes the pain out of Windows updates](https://www.makeuseof.com/category/technology-explained/)

###### 57 minutes ago [8 underrated Windows features I wish I’d started using sooner](https://www.makeuseof.com/try-these-underrated-windows-features/)

###### 2 hours ago [This free open source file explorer beats Windows at its own game](https://www.makeuseof.com/double-commander-file-explorer-alternative-windows/)

###### 4 hours ago [See More](https://www.makeuseof.com/category/pc-mobile/) [The one Windows feature everyone should turn off immediately for privacy](https://www.makeuseof.com/category/pc-mobile/)

###### [Bookmarks were pointless for me until this free app completely changed them](https://www.makeuseof.com/category/pc-mobile/)

###### [My old Android was laggy until I toggled this setting](https://www.makeuseof.com/category/pc-mobile/)

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