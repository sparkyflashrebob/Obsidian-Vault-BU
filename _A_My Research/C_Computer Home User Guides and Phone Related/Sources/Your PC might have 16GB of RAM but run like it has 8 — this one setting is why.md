---
tags:
  - notebooklm-import
notebook: "C_Computer Home User Guides and Phone Related"
category: "research"
---

* Sign in now Windows2
* Linux
* Android
* Apple
* Tech Explained
* Security
* Productivity
* Internet
* Creative
* ScreenEntertainment
* Streaming
* HomeSmart Home
* Home
  News
* Sign in
* Newsletter

### Follow Followed [Threads 1](https://www.makeuseof.com#threads) More Action Summary Sign in now [Productivity](https://www.makeuseof.com/tag/productivity/) [Android](https://www.makeuseof.com/tag/productivity/) [Smart TVs](https://www.makeuseof.com/tag/productivity/) [Networking](https://www.makeuseof.com/tag/productivity/) [Windows 11](https://www.makeuseof.com/tag/productivity/) [Entertainment](https://www.makeuseof.com/tag/productivity/) Your PC might have 16GB of RAM but run like it has 8 — this one setting is why

Digvijay Kumar / MakeUseOfCredit: Digvijay Kumar / MakeUseOfBy [Digvijay Kumar](https://www.makeuseof.com/author/digvijay-kumar/)Published Apr 25, 2026, 3:00 PM EDT Digvijay is a Computer Science graduate with a deep passion for technology. His journey into tech writing began in 2018 with software and product reviews, and he’s been exploring the digital space ever since.
He joined MUO as a full-time writer in 2022, where he covers how-tos, explainers, and tech guides focused on Android, entertainment, and the internet.
Digvijay has previously contributed to several reputable publications, including [Alphr](https://www.alphr.com/author/digvijay/), [GuidingTech](https://www.guidingtech.com/author/digvijay/), [TheWindowsClub](https://www.thewindowsclub.com/what-is-a-504-gateway-timeout-error), and [MakeTechEasier](https://www.maketecheasier.com/author/digvijaykumar/).
Outside of writing, he enjoys traveling and learning about different cultures, as he believes new experiences spark creativity. Sign in to your MakeUseOf account Add Us On Summary follow Follow followed Followed  [Thread 1](https://www.makeuseof.com#threads)  Here is a fact-based summary of the story contents: Try something different:
A few years back, I upgraded my PC to 16GB of RAM. [Chrome had been choking around twenty tabs](https://www.makeuseof.com/this-setting-is-why-chrome-is-so-slow-on-your-windows-11-pc/), and launching a game on top of that would make the whole thing stutter. The extra memory was supposed to fix that. Months later, nothing had changed. I blamed Windows, then figured the PC was just too old to keep up. Turns out neither was the issue.
The RAM I paid for was running well below its rated speed, throttled by a single setting that stays switched off by default. Sixteen gigs on the spec sheet, performing like eight. And unless you've gone into your BIOS and turned it on, yours is doing the same thing.

#### Signs your fast RAM is crawling

##### One quick check tells you everything

Digvijay Kumar / MakeUseOf
Before you go near the BIOS, it's worth knowing [what speed your RAM is actually running at](https://www.makeuseof.com/how-to-check-ram-speed/). Task Manager will tell you in a few seconds.
[Open Task Manager](https://www.makeuseof.com/how-to-check-ram-speed/), click the **Performance** tab, and select **Memory** on the left. Look for the number labeled **Speed** . Recent builds of Windows 11 display it in **MT/s** , which stands for "Megatransfers per second" — the modern label for data transfer speed. Older systems may still display it in MHz. Either way, that's your current speed.
Compare that number with what's printed on the RAM sticker or original packaging. If Task Manager shows a lower number, your RAM is running slower than what you purchased. A common case is a 3600 MT/s kit showing 2400 in Task Manager. DDR5 kits rated at 6000 often show up as 4800.
Credit: Shimul Sood / MakeUseOf If you've tossed the box and don't remember the rated speed, a free tool called [CPU-Z](https://cpuid.com/softwares/cpu-z.html) will show it to you. Open the **SPD** tab and look at the Timings Table at the bottom. Alongside the **JEDEC** columns, you'll see a column labeled **XMP** (or EXPO on AMD DDR5 kits) with the rated speed right in its header, for example, XMP-3200 or XMP-3600.

###### There's a hidden spec on SSDs that lets me pick the fastest every time

DRAM decides how your drive actually performs under pressure.

#### By [Yasir Mahmood](https://www.makeuseof.com/author/yasir-mahmood/) Meet XMP, the speed your RAM isn't using

##### Your motherboard is playing it safe

If Task Manager shows your RAM running below its rated speed, [one setting is nearly always responsible: XMP](https://www.makeuseof.com/your-ram-is-slower-than-you-think-unless-you-enable-this-setting/). Most new PCs ship with it turned off.
XMP stands for Extreme Memory Profile, Intel's standard for running RAM at the speed listed on the box. Other manufacturers use their own labels for the same feature. AMD calls their version EXPO. ASUS labels it DOCP, while MSI identifies it as A-XMP on AMD boards. All of them do the same job.
Every RAM stick ships with two speeds built in. The first is a safe default set by an industry standard called JEDEC, which any motherboard can run reliably. The second is the faster-rated speed you paid for, stored as the XMP profile. Motherboards boot to the JEDEC default, so reaching the rated speed means enabling XMP.
Technically, that's a form of overclocking, since anything above the JEDEC default qualifies. But the profile was tested and approved by your RAM manufacturer, so switching it on doesn't put your hardware at risk. You're running at the speed your memory was built for.

#### Flip the switch hiding in your BIOS

##### No tech skills required for this one

Screenshot by Jayric Maning --no attributions required
The XMP setting lives in your BIOS, not in Windows. That means restarting your PC and pressing a key as it boots to open the BIOS. The key varies by manufacturer. Delete and F2 are the most common, though some systems use F10 or F12.
Once inside, your view depends on your motherboard brand. Newer boards open in EZ or Easy Mode, which puts the main settings on one screen. XMP is usually a button or toggle on this page. If your board opens to Advanced Mode instead, look for a tab called AI Tweaker, OC, or Tweaker — that's where memory and CPU tuning live.

##### Subscribe to the newsletter for XMP RAM speed tips

*Get practical PC hardware help by subscribing to the newsletter. Expect clear, step-by-step BIOS guidance, reliable memory speed checks, and straightforward XMP explanations so your RAM runs at the performance you paid for.* By subscribing, you agree to receive newsletter and marketing emails, and accept our [Terms of Use](https://www.valnetinc.com/en/terms-of-use) and [Privacy Policy](https://www.valnetinc.com/en/privacy-policy). You can unsubscribe anytime.
Find the **XMP** option and switch it from **Disabled** to **Profile 1** . Some kits include a **Profile 2** with different timings, but stick with Profile 1. Save the change and exit. **F10** is the standard shortcut on most boards, and the screen will ask you to confirm before rebooting.
When the PC comes back up, the rated speed is active. In rare cases, the board will fail to boot once or twice. Modern BIOSes automatically fall back to the safe JEDEC default after a few failed attempts. You can try the profile again, or contact the RAM manufacturer if it repeats.

##### Check again after Windows loads

Once XMP is active, open Task Manager again and confirm the speed now matches your kit's rating. If your system feels stable after a day or two of normal use, you're set. Worth knowing: BIOS updates can reset XMP back to off, so check your RAM speed after any firmware update. There's nothing left to tweak. The speed was already there; you just weren't using it.

###### CPU-Z

CPU-Z is a lightweight Windows utility that shows detailed information about your PC’s hardware. It can identify your processor, motherboard, RAM type, memory speed, channel mode, and other system details in one place. It is especially useful when checking whether your RAM is running at its advertised speed, confirming XMP/EXPO settings, or quickly verifying hardware specs without opening your PC.

* Find at CPUIDTechnology Explained
* BIOS
* Intel

##### Follow Followed Share [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) [X](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) [WhatsApp](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) [Threads](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) [Bluesky](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) [LinkedIn](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) [Reddit](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) [Flipboard](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) [Copy link](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) [Email](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) Technology Explained

##### PC & Mobile

###### [Your PC might have 16GB of RAM but run like it has 8 — this one setting is why](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse)

###### [I stopped using my PS5 after discovering these Steam Big Picture features](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse)

###### [These 6 games will destroy your 8GB GPU, and here's how to survive them](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse)

###### [See More](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) [There's a Linux command that shows you exactly what any running process is doing](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse)

###### [I got all the benefits of a tiling WM without ever leaving GNOME](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse)

###### [I kept deleting files but my phone storage kept filling up — here's what was actually eating it](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse)

###### [See More](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse) [I found a Windows 11 log that shows exactly what's making my PC slow — and most people don't know it exists](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse)

###### [ChatGPT refused to help me vibe code my project and it led me somewhere better](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse)

###### [The USB trick that bypasses your smart TV's 100Mbps Ethernet limit](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fpc-have-16gb-ram-but-run-like-8-this-one-setting-is-why%2F%2F&src=sdkpreparse)

Reply / Post Attachment(s) Please respect our [community guidelines](https://www.valnetinc.com/en/terms-of-use#community-guidelines). No links, inappropriate language, or spam.
Your comment has not been saved
[Send confirmation email](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
angus [angus](https://www.makeuseof.com/profile/JT077347/)[angus](https://www.makeuseof.com/profile/JT077347/)#JT077347 Member since 2023-07-17 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/JT077347/)I don't see **XMP** on CPU-Z, Only 4x JEDEC.

* 2026-04-25 18:11:58
* Terms
* Privacy
* Feedback

##### Recommended [I ran a DNS speed test and Google's 8.8.8.8 wasn't even in the top two](https://www.makeuseof.com/run-dns-speed-test/)

##### [5 USB-C tricks that feel wrong until you try them](https://www.makeuseof.com/run-dns-speed-test/)

##### [Google issues Pixel battery optimization tips that solve overnight drain](https://www.makeuseof.com/run-dns-speed-test/)

##### [I've had an Alexa speaker for years — these 5 commands are the only ones I actually use](https://www.makeuseof.com/run-dns-speed-test/)

* [Join Our Team](https://www.makeuseof.com/run-dns-speed-test/)
* [Our Audience](https://www.makeuseof.com/run-dns-speed-test/)
* [About Us](https://www.makeuseof.com/run-dns-speed-test/)
* [Press & Events](https://www.makeuseof.com/run-dns-speed-test/)
* [Media Coverage](https://www.makeuseof.com/run-dns-speed-test/)
* [Contact Us](https://www.makeuseof.com/run-dns-speed-test/)
* Follow Us
* [Advertising](https://www.makeuseof.com/run-dns-speed-test/)
* [Careers](https://www.makeuseof.com/run-dns-speed-test/)
* [Terms](https://www.makeuseof.com/run-dns-speed-test/)
* [Privacy](https://www.makeuseof.com/run-dns-speed-test/)
* [Policies](https://www.makeuseof.com/run-dns-speed-test/)
  [MakeUseOf](https://www.makeuseof.com/run-dns-speed-test/) is part of the [Valnet Publishing Group](https://www.valnetinc.com/en/) Copyright © 2026 Valnet Inc.