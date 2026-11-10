---
tags:
  - notebooklm-import
notebook: "C_Computer Home User Guides and Phone Related"
category: "research"
---

* Sign in now Windows
* Linux
* Android
* Apple
* Internet
* Tech Explained
* Security
* Productivity
* Creative
* EntertainmentEntertainment
* Streaming
* HomeSmart Home
* Home
  News
* Sign in
* Newsletter

### Follow Followed [Threads 8](https://www.makeuseof.com#threads) More Action Sign in now [Windows 11](https://www.makeuseof.com/tag/windows-11/) [ChatGPT](https://www.makeuseof.com/tag/windows-11/) [iPhone Help](https://www.makeuseof.com/tag/windows-11/) [Facebook Help](https://www.makeuseof.com/tag/windows-11/) [Avoiding Scams](https://www.makeuseof.com/tag/windows-11/) [Emojis Explained](https://www.makeuseof.com/tag/windows-11/) [Free Movie Streaming](https://www.makeuseof.com/tag/windows-11/) This Windows command shows exactly what's slowing down your PC

By [Gavin Phillips](https://www.makeuseof.com/author/gavin/)Published Feb 15, 2026, 6:00 AM EST Gavin is the Segment Lead for the Technology Explained, Security, Internet, Streaming, and Entertainment verticals, former co-host on the Really Useful Podcast, and a frequent product reviewer. He has a degree in Contemporary Writing pillaged from the hills of Devon, more than a decade of professional writing experience, and his work has appeared on [How-To Geek](https://www.howtogeek.com/author/gavin-phillips/), [Expert Reviews](https://www.expertreviews.co.uk/author/gavin-phillips), [Trusted Reviews](https://www.trustedreviews.com/author/gavinphillips), [Online Tech Tips](https://www.online-tech-tips.com/author/gphilips/), and [Help Desk Geek](https://helpdeskgeek.com/author/gphilips/), among others. Gavin has attended CES, IFA, MWC, and other tech-trade shows to report directly from the floor, racking up hundreds of thousands of steps in the process. He's reviewed more headphones, earbuds, and mechanical keyboards than he cares to remember, and enjoys copious amounts of tea, board games, and football. Sign in to your MUO account Add Us On follow Follow followed Followed  [Thread 8](https://www.makeuseof.com#threads)  Here is a fact-based summary of the story contents: Try something different:
Is your PC crawling along at a snail's pace, but you can't figure out why? You're not alone—millions of Windows users deal with sluggish performance without understanding the root cause.
While Task Manager gives you a quick snapshot of what's happening right now, there's a more powerful diagnostic tool hiding in plain sight. Windows includes a built-in command that runs a comprehensive 60-second analysis of your system and generates a detailed report pinpointing exactly what's dragging down your performance.
Best of all, you don't need to be a tech expert to use it or understand the results, and it's already lurking in the background on your computer.

#### When your computer slows down, you need perfmon

##### The Performance Monitor knows all

The secret performance weapon hidden in Windows is the Performance Monitor, with its integrated Performance Report. Performance Monitor analyzes everything taking place on your entire system over a 60-second period, examining everything from startup programs and driver issues to disk performance and network activity, and presenting it in an easy-to-read report.
Unlike Task Manager, which shows you what's happening at this exact moment, this report gives you a holistic view of your system's health and identifies patterns that might be causing slowdowns, with detailed information on performance, software, hardware, network, memory, and other important metrics.
Opening and running the Performance Monitor is part of what makes this tool so useful. There is no complicated setup or fiddling with settings to capture the right data. You just punch in the command, and off your computer goes.

1. Press **Win + R** to open the Run dialog, and input **perfmon /report** .
2. Alternatively, press **Win + X** , open the **Terminal (Admin)** , and input **perfmon /report** .
   Once you execute the command, Windows will display a message saying it's collecting data for 60 seconds. Don't close the window or start doing intensive tasks during this period—let it run in the background while your PC operates normally.
   After the minute is up, a comprehensive report will appear with color-coded warnings and detailed information about the potential performance bottlenecks slowing down your computer. It looks a little confusing at first, but it's broken down into some easy-to-read sections.

###### This Small Change Gave My Slow Windows PC a Huge Speed Boost

I can’t believe I ignored this simple trick for so long.

#### By [Pankil Shah](https://www.makeuseof.com/author/pankil-shah/) What the Performance Monitor report is telling you

##### It's all in the data

The level of information you receive from the Performance Monitor Report will vary depending on your system. I'm currently working from a very modern laptop, manufactured in 2025 and just a few months old. That means most of the performance metrics in my Performance Monitor Report are straightforward, and the report is also helped by the clear sections.
Report Section
What You'll Find
What to Look Out For
**Diagnostic Results**
Color-coded summary (green/yellow/red) of overall system health
Red or yellow warnings indicating critical issues; common problems include too many startup programs or insufficient resources
**Software Configuration**
Details about installed programs, startup items, and Windows settings
Long list of startup programs (more than 10-15); programs you don't recognize; outdated Windows version
**Hardware Configuration**
Overview of CPU, RAM, disk type, and network adapter specifications
Total RAM below 8GB; using an HDD instead of SSD; outdated hardware that doesn't meet modern standards
**CPU**
Processor utilization, speed, and performance during the test period
Consistent usage above 80-90%; CPU running slower than its rated speed; thermal throttling indicators
**Network**
Network adapter performance and bandwidth usage
Unusual network activity when you're not downloading; slow connection speeds; network adapter errors
**Disk**
Hard drive or SSD performance, response times, and usage patterns
Average response time above 25ms (for SSDs) or 15ms (for HDDs); disk usage constantly at 100%; fragmentation warnings on HDDs
**Memory**
RAM usage, available memory, and page file activity
Used memory consistently above 90%; high page file usage (means your RAM is maxed out); memory errors or warnings
**Report Statistics**
Summary of data collection, including duration and timestamps
This is mostly informational about the report itself
As said, at first, these sections seem quite full on, but they're easy to understand once you start opening and reading through them.

#### So, what's really slowing down your PC?

##### Figuring out the results

Of course, your Performance Monitor Report is going to differ from mine; we're using different computers, after all. Some of the fixes and tips are more universal than others, while some are actually general computing and Windows optimization tips—it's just good to see them laid out.
The top-level report is a good starting place. It gives you a quick overview of what might be wrong with your hardware, with a handy traffic light system to show what's wrong. Obviously, anything with an amber icon should be checked, and anything in red needs immediate attention.
For example, one of the most common culprits for slow performance is simply over-exerting your system. If you have heaps of programs open and your browser is full of memory-sucking tabs, Performance Monitor will advise that your system is running slowly.
That one is on the more obvious end of fixes, as are other issues like "you don't have enough RAM" or "your storage is running out."
But other performance issues highlighted can be more specific and much more useful. Under the **Disk > Physical Disk** section, you can see your overall disk usage, illustrating just how much you've used it in terms of read time, write time, and so on.

##### MUO Report: Subscribe and never miss what matters

*Stay updated with the latest tech trends, expert tips, and product reviews in the world of technology with MUO's Newsletters.* By subscribing, you agree to receive newsletter and marketing emails, and accept our [Terms of Use](https://www.valnetinc.com/en/terms-of-use) and [Privacy Policy](https://www.valnetinc.com/en/privacy-policy). You can unsubscribe anytime.
The report can also highlight driver issues, which shouldn't be ignored, as outdated drivers can lead to other issues.
Sometimes the report will show "no issues detected," but your PC still feels sluggish—this can be frustrating, but it isn't uncommon. In these cases, the slowdown might be caused by a specific application rather than a system-wide issue, or your expectations might not match your hardware's capabilities.
Try running the report while experiencing the slowdown, or consider other factors like a nearly-full hard drive (Windows needs at least 10-20% free space to operate efficiently), browser extensions hogging resources, or malware that's evading detection.

###### [I finally disabled these Windows services and my PC is happier for it](https://www.valnetinc.com/en/privacy-policy)

Your PC might be secretly working harder than you are, and not always in ways that benefit you.

#### [17](https://www.valnetinc.com/en/privacy-policy) By [Pankil Shah](https://www.makeuseof.com/author/pankil-shah/) Performance Monitor is free, so give it a try

##### You might just figure out what's slowing down your PC

The Performance Monitor and Performance Report is one of Windows' most underutilized diagnostic tools, offering insights that go far beyond what casual monitoring can reveal. It's not perfect, mind, but it makes understanding your system issues just that little bit easier.

* [Windows](https://www.makeuseof.com/author/pankil-shah/)
* [Windows Tips](https://www.makeuseof.com/author/pankil-shah/)
* [Troubleshooting](https://www.makeuseof.com/author/pankil-shah/)

##### Follow Followed Share [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-command-shows-exactly-whats-slowing-down-your-pc%2F%2F&src=sdkpreparse) [X](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-command-shows-exactly-whats-slowing-down-your-pc%2F%2F&src=sdkpreparse) [WhatsApp](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-command-shows-exactly-whats-slowing-down-your-pc%2F%2F&src=sdkpreparse) [Threads](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-command-shows-exactly-whats-slowing-down-your-pc%2F%2F&src=sdkpreparse) [Bluesky](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-command-shows-exactly-whats-slowing-down-your-pc%2F%2F&src=sdkpreparse) [LinkedIn](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-command-shows-exactly-whats-slowing-down-your-pc%2F%2F&src=sdkpreparse) [Reddit](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-command-shows-exactly-whats-slowing-down-your-pc%2F%2F&src=sdkpreparse) [Flipboard](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-command-shows-exactly-whats-slowing-down-your-pc%2F%2F&src=sdkpreparse) [Copy link](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-command-shows-exactly-whats-slowing-down-your-pc%2F%2F&src=sdkpreparse) [Email](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-command-shows-exactly-whats-slowing-down-your-pc%2F%2F&src=sdkpreparse) MUO Report: Subscribe and never miss what matters

*Stay updated with the latest tech trends, expert tips, and product reviews in the world of technology with MUO's Newsletters.* By subscribing, you agree to receive newsletter and marketing emails, and accept our [Terms of Use](https://www.valnetinc.com/en/terms-of-use) and [Privacy Policy](https://www.valnetinc.com/en/privacy-policy). You can unsubscribe anytime.

##### Technology Explained

##### PC & Mobile

###### [Your SSD is getting slower, and here's how to fix it](https://www.valnetinc.com/en/privacy-policy)

###### [3 cheap gadgets that saved me hours of tech troubleshooting](https://www.valnetinc.com/en/privacy-policy)

###### [My Wi-Fi was acting up — here's how I fixed it](https://www.valnetinc.com/en/privacy-policy)

###### [See More](https://www.valnetinc.com/en/privacy-policy) [Yes, you can turn your old iPad into a dedicated PC monitor](https://www.valnetinc.com/en/privacy-policy)

###### [I finally removed every trace of Copilot and Recall from Windows — here's how](https://www.valnetinc.com/en/privacy-policy)

###### [Your old Android phone can become a free security camera in 5 minutes](https://www.valnetinc.com/en/privacy-policy)

###### [See More](https://www.valnetinc.com/en/privacy-policy) [5 signs that mean your PC parts are failing](https://www.valnetinc.com/en/privacy-policy)

###### [6 free apps that make your old Windows laptop feel new again](https://www.valnetinc.com/en/privacy-policy)

Reply / Post Attachment(s) Please respect our [community guidelines](https://www.valnetinc.com/en/terms-of-use#community-guidelines). No links, inappropriate language, or spam.
Your comment has not been saved
[Send confirmation email](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
Charles [Charles](https://www.makeuseof.com/profile/FV299326/)[Charles](https://www.makeuseof.com/profile/FV299326/)#FV299326 Member since 2023-07-17 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/FV299326/)Just a warning. If you have an ARM64 system as I do with a Snapdragon processor, this report will generate several false warnings.

* 2026-02-15 13:06:08
  Gavin\_Phillips [Gavin\_Phillips](https://www.makeuseof.com/profile/GD724389/)[Gavin\_Phillips](https://www.makeuseof.com/profile/GD724389/)#GD724389 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/GD724389/)That's great information - I didnt know that.
* 2026-02-15 16:55:05
  Roger [Roger](https://www.makeuseof.com/profile/WR451229/)[Roger](https://www.makeuseof.com/profile/WR451229/)#WR451229 Member since 2026-02-16 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/WR451229/)Computer simply said it could not find the command
* 2026-02-16 03:19:52
  Derp [Derp](https://www.makeuseof.com/profile/VN086559/)[Derp](https://www.makeuseof.com/profile/VN086559/)#VN086559 Member since 2026-02-15 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/VN086559/)I guess whatever is slowing my pc is slowing this program as well. I left it on the "collecting data" screen for a full 10 minutes before shutting it down...
* 2026-02-15 13:21:48
  mrmks [mrmks](https://www.makeuseof.com/profile/CE186014/)[mrmks](https://www.makeuseof.com/profile/CE186014/)#CE186014 Member since 2026-02-15 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/CE186014/)Performance Monitor sounded like what I needed to run on my ACER laptop, so I ran it.
  After 60 seconds, the report was blank. Hmmm...
  Ran it again. After 20 minutes the report was still blank.
  The only conclusion I can draw from this exercise is that my laptop must be in amazingly tip-top shape!
  Unfortunately, I'm painfully aware that this laptop isn't anywhere near being in top performing shape.
  Would anyone like to tender a reason why perfmon produced a blank report?
* 2026-02-15 15:43:22
  Bill [Bill](https://www.makeuseof.com/profile/LH836754/)[Bill](https://www.makeuseof.com/profile/LH836754/)#LH836754 Member since 2024-09-19 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/LH836754/)Yeah, well, the app runs, but i keep getting an error that something is already running, preventing perfmon from gathering the information. What is the workaround?
* 2026-02-16 11:38:43
  Don [Don](https://www.makeuseof.com/profile/WN170211/)[Don](https://www.makeuseof.com/profile/WN170211/)#WN170211 Member since 2026-02-15 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/WN170211/)That tool, despite it will tell you whats slowing up your computer. I think it's pretty safe to say at this juncture, especially since i got rid of ALL my windows OS's & went to Linux Exclusively. Never been happier for 1, a few decades of hardware that the newer windows OS would not have a driver for, thus making it so you gotta buy new hardware, and being a musician studio engineer, that gets quite expensive. VERY FRUSTRATING!! What sold me was it runs faster, cooler, AND every single piece of old hardware i had and plugged in, LINUX HAD DRIVERS and i use them all again now! My Ability to sound engineer just increased in terms of flexibility one hundred fold having all the old sound cards and interface mixers, midi controllers, and drum pads ALL work again! If your smart, You'd switch too. Use Google Ai to help you do it as i am a total noob with Linux. . 2 months later, i am happier than i ever been with my pc's and can do things windows only wished it could do. I would recommend as a noob to start out on something like Zorin OS Or Linux Mint. Yes its a little confusing at first but once ya get the hang of the common commands you use to do things, its a piece of cake and you will be thanking yourselves. ONLY negative thing about going to Linux is if you have a windows exclusive program, like for example Hallmark Card Maker, well then your stuck running virtual Box and loading windows on that but it's isolated from your Linux side so your safe. I would not browse the web or use any programs in the windows virtual box that use the internet. I would use it for local programs that do not have a Linux alternative. I find the easiest way to install something by simply asking the google AI in the browser and ask it to give you the terminal command line to install. gives a copy button copy the command and you can run more than one command in succession. If you have a error copy/paste it and it ALWAYS gives you the command line fix. It has never failed me yet!
* 2026-02-15 17:04:12
  LESM [LESM](https://www.makeuseof.com/profile/CS839859/)[LESM](https://www.makeuseof.com/profile/CS839859/)#CS839859 Member since 2025-10-13 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/CS839859/)Great thanks.
* 2026-02-15 12:53:14
  Marconelli [Marconelli](https://www.makeuseof.com/profile/AB403153/)[Marconelli](https://www.makeuseof.com/profile/AB403153/)#AB403153 Member since 2023-10-18 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/AB403153/)When I tried to do this by using the Run command **perfmon /report** , it just stalled. It said that it was "running for 60 seconds" -- for 5 minutes, until I gave up. No report ever appeared. Instead, I got it to work through Control Panel > Administrative Tools > Performance Monitor. The report appeared instantly.
* 2026-02-15 17:55:59
* Terms
* Privacy
* Feedback

##### Recommended [I stopped using the Start Menu—and I don’t miss it at all](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)

##### [This tiny Windhawk tweak solved a problem Windows never fixed](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)

##### [Please don't ignore firmware updates on these devices](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)

##### [Here's how I deep clean my Windows PC](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)

* [Join Our Team](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)
* [Our Audience](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)
* [About Us](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)
* [Press & Events](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)
* [Media Coverage](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)
* [Contact Us](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)
* Follow Us
* [Advertising](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)
* [Careers](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)
* [Terms](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)
* [Privacy](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)
* [Policies](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/)
  [MUO](https://www.makeuseof.com/stopped-using-start-menu-dont-miss-it/) is part of the [Valnet Publishing Group](https://www.valnetinc.com/en/) Copyright © 2026 Valnet Inc.