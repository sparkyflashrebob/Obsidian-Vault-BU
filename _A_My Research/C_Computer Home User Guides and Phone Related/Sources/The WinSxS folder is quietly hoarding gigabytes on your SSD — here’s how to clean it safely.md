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

### Follow Followed [Threads 12](https://www.makeuseof.com#threads) More Action Sign in now [Windows 11](https://www.makeuseof.com/tag/windows-11/) [ChatGPT](https://www.makeuseof.com/tag/windows-11/) [iPhone Help](https://www.makeuseof.com/tag/windows-11/) [Facebook Help](https://www.makeuseof.com/tag/windows-11/) [Avoiding Scams](https://www.makeuseof.com/tag/windows-11/) [Emojis Explained](https://www.makeuseof.com/tag/windows-11/) [Free Movie Streaming](https://www.makeuseof.com/tag/windows-11/) The WinSxS folder is quietly hoarding gigabytes on your SSD — here’s how to clean it safely

Pankil Shah / MakeUseOfCredit: Pankil Shah / MakeUseOfBy [Yasir Mahmood](https://www.makeuseof.com/author/yasir-mahmood/)Published Jan 29, 2026, 9:00 AM EST Yasir is a Mechanical Engineer who writes about tech at MUO, covering Windows, Productivity, Security, and the Internet. His interest in autonomous systems keeps him constantly tinkering with both hardware and software.
His tech writing journey began during his junior year of engineering, leading him to [Android Police](http://www.androidpolice.com/author/yasir-m/) before joining MUO. He focuses on making technology accessible, whether he's troubleshooting Windows issues, exploring productivity tools, or explaining security risks in plain English. For Yasir, the best way to do this is to actually use the tools and run into the same problems readers face.
When he's not writing or engineering, you'll find Yasir watching Impractical Jokers and genuinely laughing at pranks he's seen a dozen times before. Sign in to your MUO account Add Us On follow Follow followed Followed  [Thread 12](https://www.makeuseof.com#threads)  Here is a fact-based summary of the story contents: Try something different:
If you've ever dug through your Windows installation drive looking for space hogs, you've probably stumbled upon the WinSxS folder. It's one of those system folders that quietly balloons to 10GB or more without you noticing, and your first instinct might be to delete it. Don't—Windows needs it to function, and removing files manually will break your system.
The WinSxS folder stores system components, including older versions that Windows keeps for updates and rollbacks. The good news is that you can safely trim it down using built-in tools rather than manually hunting for the [largest files and folders on your Windows PC](https://www.makeuseof.com/easily-find-large-files-windows/).

#### File Explorer makes the folder size misleading

##### The hard links make the component store look bigger than it is

Screenshot by Yasir Mahmood
Right-click the WinSxS folder, check its properties, and you'll likely see a number that makes you want to nuke the whole thing. On my system, File Explorer reports it at 14GB. That's a lot of space for a folder most people have never heard of—but that number is misleading.
Windows uses something called hard links to make files appear in multiple locations without actually duplicating data. The operating system counts these hard-linked files multiple times when calculating folder size, which inflates the WinSxS number. The actual disk space it occupies is usually smaller than what File Explorer shows. You can check the real size using a simple command.

1. Open PowerShell as administrator and type Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore , then press **Enter** .
2. Wait for the analysis to complete. It takes a minute or two.
3. Look for the **Actual Size of Component Store** in the output.
   That "Actual Size of Component Store" figure is what the folder actually takes up on your drive. On most systems, you'll find it's 5-10GB, which is normal for a healthy Windows installation. If it's significantly larger, cleaning makes sense.
   Now, even if the folder is bloated, you can't just delete files from it manually. WinSxS stores critical components that Windows needs for system stability, updates, and rollbacks. The operating system keeps older versions of DLLs and other files so it can undo problematic updates or maintain compatibility with certain applications.
   If you delete the wrong file, you'll corrupt your installation—potentially making Windows unbootable. This is why built-in cleanup tools exist. They know which files are safe to remove and which ones Windows still needs.

#### Disk Cleanup is the safest way to reclaim space

##### It targets the old files your system no longer needs

For most people, Disk Cleanup is all you need. It's built into Windows, requires no technical knowledge, and won't let you break anything. I've used it for years as part of regular maintenance, and it consistently frees up a few gigabytes without any fuss.
The key is accessing the system file options, which aren't visible by default. Here's how to do it:

1. Press the Windows key, type **Disk Cleanup** , and open it.
2. Select your system drive (usually **C:** ) and click **OK** .
3. Click **Clean up system files** at the bottom of the window.
4. Select your system drive again and wait for the scan to finish.
5. Check **Windows Update Cleanup** ,and also **Previous Windows installations** if they appear.
6. Click **OK** , then confirm the deletion.
   The Windows Update Cleanup option targets old update files stored in WinSxS that your system no longer needs. When I performed this process on my own machine, I freed up 3GB of space. If you recently upgraded from an older Windows version, previous Windows installations can reclaim even more space—sometimes 10GB or more.
   This process isn't instant. It can take several minutes, and Windows might ask you to restart afterward. Don't panic if your system seems slow during the process, as it's working through a lot of files.

#### DISM commands offer deeper cleaning

##### It gives you more control, but one flag removes your rollback options

Screenshot by Yasir Mahmood
Disk Cleanup is great for routine maintenance, but sometimes it doesn't go far enough. If you've run it and your WinSxS folder still seems bloated—or you just want more control over the process—you can use the Deployment Image Servicing and Management (DISM) tool via Terminal. This utility is also handy for other system repairs, so knowing [how to use DISM commands to repair Windows 11 system images](https://www.makeuseof.com/how-to-use-dism-commands/) is a great skill to have.
Open PowerShell as administrator by right-clicking the Start button and selecting **Terminal (Admin)** . Then run the standard cleanup command:

1. Type Dism.exe /Online /Cleanup-Image /StartComponentCleanup and press **Enter** .
2. Wait for the process to complete; it can take a few minutes depending on your system.
   This command removes older versions of updated components that Windows has kept around. It's more thorough than Disk Cleanup but still plays it safe, preserving your ability to uninstall recent updates if something goes wrong.
   There's also a more aggressive option. Adding the /ResetBase flag removes all superseded versions of components permanently:
3. Type Dism.exe /Online /Cleanup-Image /StartComponentCleanup /ResetBase and press **Enter** .
4. Let it run—this one takes longer.
   Once you run /ResetBase , you lose the ability to uninstall any previously installed updates. Windows can't roll back what it no longer has files for. I recommend using this when your system has been stable for a while, and you're confident you won't need to undo anything.

#### Windows automatically cleans the component store

##### It handles maintenance in the background—when it gets the chance

Screenshot by Yasir Mahmood
Windows already handles WinSxS maintenance on its own. A scheduled task runs in the background during idle time, cleaning up old component files without your input. You can even [automate fixes or maintenance that keep your PC running smoothly](https://www.makeuseof.com/automate-these-tasks-on-every-windows-installation-keeps-things-running/) for other parts of the OS using similar methods.

##### Subscribe for safe Windows cleanup tips and WinSxS guidance

*Looking for more practical, step-by-step Windows maintenance? Subscribe to the newsletter for clear guidance on safe WinSxS cleanup and other focused Windows-care walkthroughs that help you reclaim disk space without breaking your system.* By subscribing, you agree to receive newsletter and marketing emails, and accept Valnet’s [Terms of Use](https://www.valnetinc.com/en/terms-of-use) and [Privacy Policy](https://www.valnetinc.com/en/privacy-policy). You can unsubscribe anytime.
However, the problem with that scheduled task is that it's conservative; it won't reclaim as much space as manual methods, and you never know when it actually runs. You can find this task in Task Scheduler if you're curious:

1. Press the **Windows key** , type **Task Scheduler** , then open it.
2. Navigate to **Task Scheduler Library > Microsoft > Windows > Servicing** .
3. Look for the task named **StartComponentCleanup** .
   This task performs basic cleanup similar to the DISM command, but it waits for your system to be idle before running. If you use your PC constantly or shut it down when you're done, the task might rarely get a chance to execute. That's why manual cleanup still matters.
   You can right-click the task and select **Run** to trigger it immediately. It's a middle ground between Disk Cleanup and DISM commands.
   Don't obsess over WinSxS size—checking it every few months is plenty. The folder will always take up several gigabytes because Windows genuinely needs those files to remain stable. The goal isn't to minimize the folder to zero; it's simply to keep it from growing out of control and eating your SSD. If you're still tight on space after cleaning WinSxS, [other ways to slim down your Windows installation](https://www.makeuseof.com/ran-one-windows-command-and-got-back-space/), like auditing your installed programs or moving large files to a secondary drive, can help you reclaim even more space.

* [Windows](https://www.makeuseof.com/ran-one-windows-command-and-got-back-space/)
* [Storage](https://www.makeuseof.com/ran-one-windows-command-and-got-back-space/)
* [Windows Tips](https://www.makeuseof.com/ran-one-windows-command-and-got-back-space/)

##### Follow Followed Share [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) [X](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) [WhatsApp](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) [Threads](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) [Bluesky](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) [LinkedIn](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) [Reddit](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) [Flipboard](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) [Copy link](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) [Email](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) Technology Explained

##### PC & Mobile

###### [I turned off 2G—and it’s my best security upgrade](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse)

###### [I changed one router setting and my Gigabit Wi-Fi 6E setup finally felt fast](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse)

###### [I regret ignoring this BIOS setting for years — this tweak changed everything](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse)

###### [See More](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) [I didn’t realize my phone was tracking this by default](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse)

###### [You can still run old programs on Windows 11 if you know this trick](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse)

###### [I moved my Windows user folders to another drive and my PC got faster](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse)

###### [See More](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse) [5 Android subscriptions you can easily replace with free apps](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse)

###### [I had no idea Windows had a built-in copy tool this fast](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse)

###### [I’ve used Samsung for years, but these 5 features make me feel like a pro](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwinsxs-folder-quietly-hoarding-gigabytes-ssd%2F%2F&src=sdkpreparse)

Reply / Post Attachment(s) Please respect our [community guidelines](https://www.valnetinc.com/en/terms-of-use#community-guidelines). No links, inappropriate language, or spam.
Your comment has not been saved
[Send confirmation email](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
Chris [Chris](https://www.makeuseof.com/profile/OH876966/)[Chris](https://www.makeuseof.com/profile/OH876966/)#OH876966 Member since 2023-10-18 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/OH876966/)In Win 11, there is no such option as stated: "3. Click **Clean up system files** at the bottom of the window."
I did see this option listed taking up over 3GB. "System error memory dump files". I checked online and it says safe to delete. Did that. That was the only significant space hog for me in this folder, using Disk Cleanup.

* 2026-01-30 11:52:45
  Lshismp [Lshismp](https://www.makeuseof.com/profile/ZZ454799/)[Lshismp](https://www.makeuseof.com/profile/ZZ454799/)#ZZ454799 Member since 2025-07-14 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/ZZ454799/)You have to click
* 2026-01-30 17:13:56
  Greywulff [Greywulff](https://www.makeuseof.com/profile/IZ710616/)[Greywulff](https://www.makeuseof.com/profile/IZ710616/)#IZ710616 Member since 2025-12-11 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/IZ710616/)My Win 11 Pro system (24H2) has the **Clean up system files** option. No idea why yours doesn't.
* 2026-01-30 17:37:07
  Oliver [Oliver](https://www.makeuseof.com/profile/RA214423/)[Oliver](https://www.makeuseof.com/profile/RA214423/)#RA214423 Member since 2026-01-30 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/RA214423/)Interesting. Hard links were a first-class concept in the earliest versions of UNIX to appear more than fifty years ago, and continue to this day in Linux and FreeBSD in that status. You want to delete a file, you remove the last hard link to it, and the space it takes is freed up. Inodes, they’re called.
  Microsoft bodged hard links into Windows much more recently, and still haven’t gotten it quite right. Hence this tech tip.
* 2026-01-30 18:19:07
  SHIVANGI [SHIVANGI](https://www.makeuseof.com/profile/PK082743/)[SHIVANGI](https://www.makeuseof.com/profile/PK082743/)#PK082743 Member since 2026-01-31 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/PK082743/)Bruh why will anyone have a storage issue in 2026?
* 2026-01-30 22:55:23
  Georg [Georg](https://www.makeuseof.com/profile/IC386593/)[Georg](https://www.makeuseof.com/profile/IC386593/)#IC386593 Member since 2025-11-23 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/IC386593/)Interesting. Thanks for the article.
  I did the "Properties" of the WinSxS folder on my Win11-Pro.
  Interestingly there are two hugely different sizes reported, and I have the feeling that solves the issue you mention about the hardlinks being double+ counted.
  a) "Size:" 16.4 GB (17,692,387,729 bytes)
  b) "Size on disk:" 9.77 GB (10,496,663,552 bytes)
  And here's the info displayed by dism.exe
  Windows Explorer Reported Size of Component Store : 10.33 GB
  Actual Size of Component Store : 9.86 GB
  Shared with Windows : 4.30 GB
  Backups and Disabled Features : 5.55 GB
  Cache and Temporary Data : 0 bytes
  So ... the "Size on disk:" from File Explorer Properties is pretty close :-)
* 2026-01-31 04:31:26
  Jon [Jon](https://www.makeuseof.com/profile/WK948705/)[Jon](https://www.makeuseof.com/profile/WK948705/)#WK948705 Member since 2025-09-13 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/WK948705/)I cleaned it safely by installing Linux instead
* 2026-01-29 21:46:54
  Scooby [Scooby](https://www.makeuseof.com/profile/UE674744/)[Scooby](https://www.makeuseof.com/profile/UE674744/)#UE674744 Member since 2026-01-30 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/UE674744/)You people still having the linux vs Windows arguments in 2026? This article is exaggerated btw. I still have the same nvme drive on windows 11 that I had on 10, and still have the space that I had on 10. Hasn't increased at all. Maybe it's the junk these "tweakers" use thinking it's making it better, when in reality, it's creating the problems the cry about on here. I don't care who uses what. Use what suits you. The linux vs Windows garbage is the same childish argument as the Intel vs AMD shit. Use what you like. Not sure why people get their panties in a bunch over what someone else uses. I have Windows 11 on one PC, Linux on another, and each for what I have them setup for. It's 2026 people, stop arguing over nonsense that has no merit. Use what you like and move on. Society really going backwards......
* 2026-01-30 00:44:38
  DinoSaurus [DinoSaurus](https://www.makeuseof.com/profile/DD758012/)[DinoSaurus](https://www.makeuseof.com/profile/DD758012/)#DD758012 Member since 2025-10-09 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/DD758012/)And here comes the Linux fanboy. This article is not for you, so why do you have to drop a useless comment?
  Ah, yes... That ever failing year of the Linux desktop surely stings hard, doesn't it?
* 2026-01-30 02:34:19
  MUOMember [MUOMember](https://www.makeuseof.com/profile/AQ338022/)[MUOMember](https://www.makeuseof.com/profile/AQ338022/)#AQ338022 Member since 2026-01-15 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/AQ338022/)The final cleanup
* 2026-01-30 04:34:48
  Jon [Jon](https://www.makeuseof.com/profile/WK948705/)[Jon](https://www.makeuseof.com/profile/WK948705/)#WK948705 Member since 2025-09-13 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/WK948705/)I'm not even a Linux fanboy. I've used windows most of my adult working life and still do. However, the amount of problems, frustration and idiotic decisions Microslop has made lately has turned even me away. Constant broken updates, my old Windows install hasn't have a successful windows update since they broke updates Jan 2025, the constant nagging you to login to your Microsoft account, sign in to onedrive, co-pilot crammed down our thoats.... notepad, paint, dedicated co-pilot button on keyboards. Internet and Microsoft account required just to install Windows I'm done.
  You're me, you just don't know it yet. Keep fanboying for your favorite company and saying "Yes, please may i have another!" as they bend you over a barrel.
* 2026-01-30 13:41:29
  Taras [Taras](https://www.makeuseof.com/profile/EA991507/)[Taras](https://www.makeuseof.com/profile/EA991507/)#EA991507 Member since 2025-08-19 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/EA991507/)Scooby Linux with AMD, avoid Windows and Intel :D
* 2026-01-30 15:35:09
* [Terms](https://www.makeuseof.com/profile/EA991507/)
* [Privacy](https://www.makeuseof.com/profile/EA991507/)
* [Feedback](https://www.makeuseof.com/profile/EA991507/)

##### Recommended [This tiny Windhawk tweak solved a problem Windows never fixed](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)

##### [Please stop using the wrong Ethernet cables](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)

##### [Please don't ignore firmware updates on these devices](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)

##### [Here's how I deep clean my Windows PC](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)

* [Join Our Team](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)
* [Our Audience](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)
* [About Us](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)
* [Press & Events](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)
* [Media Coverage](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)
* [Contact Us](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)
* Follow Us
* [Advertising](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)
* [Careers](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)
* [Terms](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)
* [Privacy](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)
* [Policies](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/)
  [MUO](https://www.makeuseof.com/windhawk-tweak-fixes-file-folder-size-issue-windows/) is part of the [Valnet Publishing Group](https://www.valnetinc.com/en/) Copyright © 2026 Valnet Inc.