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

### Follow Followed [Threads 9](https://www.makeuseof.com#threads) More Action Sign in now [Windows 11](https://www.makeuseof.com/tag/windows-11/) [ChatGPT](https://www.makeuseof.com/tag/windows-11/) [iPhone Help](https://www.makeuseof.com/tag/windows-11/) [Facebook Help](https://www.makeuseof.com/tag/windows-11/) [Avoiding Scams](https://www.makeuseof.com/tag/windows-11/) [Emojis Explained](https://www.makeuseof.com/tag/windows-11/) [Free Movie Streaming](https://www.makeuseof.com/tag/windows-11/) The weird Windows 11 setting that finally let me uninstall Edge and Bing

Tashreef Shareef / MakeUseOfCredit: Tashreef Shareef / MakeUseOfBy [Tashreef Shareef](https://www.makeuseof.com/author/tashreef-shareef/)Published Mar 15, 2026, 6:00 AM EDT
Tashreef's fascination with consumer technology began in the school library when he stumbled upon a tech magazine, CHIP, which ultimately inspired him to pursue a degree in Computer Science. Since 2012, Tashreef has professionally authored over a thousand how-to articles, contributing to [Windows Report](https://windowsreport.com/author/tashreefshareef/) and [How-To Geek.](https://www.howtogeek.com/author/tashreef-shareef/) He currently focuses on Microsoft Windows content at MakeUseOf, which he has been using since 2007.
With hands-on experience building websites and technology blogs, he brings practical developer insights to his technical writing. You can view his complete work portfolio at itashreef.com.
You might also stumble upon his short how-to video explainers, simplifying complex topics. Beyond writing, Tashreef enjoys creating short explainer videos, gaming, and exploring animated shows.
[Sign in to your MakeUseOf account](https://www.howtogeek.com/author/tashreef-shareef/) [Add Us On](https://www.howtogeek.com/author/tashreef-shareef/) follow Follow followed Followed  [Thread 9](https://www.makeuseof.com#threads)  Here is a fact-based summary of the story contents: Try something different:
Vanilla Windows 11 has a lot of pre-installed apps. [Some of these pre-installed apps are excellent](https://www.makeuseof.com/excellent-pre-installed-windows-11-apps-and-tools/), but others are not so much. Regardless of how useful these apps are, Microsoft doesn't offer an easy way to get rid of them, even if you don't want them.
Case in point: Microsoft Edge. While I personally prefer Edge over Chrome, you can't uninstall the browser without doing all kinds of gymnastics. Ironically, the uninstall option for Edge in the Settings app is greyed out, which means Microsoft chose to disable the option, at least for my region. That's how I figured out that if I change the region to a European Economic Area (EEA) country and enable the Digital Markets Act, the uninstall option magically appears and lets me remove Edge.

#### What's the Digital Markets Act (DMA)?

##### EU regulations that give users more control

Tashreef Shareef / MakeUseOfCredit: Tashreef Shareef / MakeUseOfThe Digital Markets Act is a set of regulations that the European Union enforces on large tech companies, including Microsoft. Under DMA rules, companies classified as "gatekeepers" must give users the freedom to uninstall pre-installed apps, choose their own default browser, and opt out of data collection practices that are otherwise forced on users in other regions.
For Windows, this means PCs set up in an EEA country behave differently. Edge becomes fully uninstallable, and third-party browsers can be set as the default for all file types, including PDFs, in one step. You can also disable Bing in Windows Search without needing enterprise policies, and Microsoft apps are required to respect your default browser choice instead of overriding it with Edge.
Interestingly, Windows decides whether to apply DMA rules based on a single registry value called **DeviceRegion** . When you pick an EEA country like Ireland during setup, Windows sets this value and activates DMA mode. And since this is just a registry entry, you can change it after installation, too.

#### Remove Edge using Wintoys

##### A free app makes this a one-click process

The easiest way to enable the Digital Markets Act on your PC is to use Wintoys. [It's a free Windows utility that offers a centralized space for a lot of power-user tweaks in one place](https://www.makeuseof.com/manage-windows-settings-with-wintoys/), allowing you to configure, optimize, and customize your system from a single interface instead of digging through scattered Settings menus and command-line tools.
After installing [Wintoys from the Microsoft Store](https://apps.microsoft.com/detail/9p8ltpgcbzxd), launch the app and open the **Tweaks** tab. Expand the **System** section, and you'll see a **Digital Markets Act** toggle near the bottom. Turn it on.
This automatically sets your **Device setup region** to Ireland, which is an EEA country. You can verify the change by going to **Settings > Time & language > Language & region** and checking the **Device setup region** field. It should now show **Ireland** , even if your **Country or region** still shows your actual location. Your country setting stays untouched, so things like currency format and local content won't be affected.
Once DMA mode is active, head to **Settings > Apps > Installed apps** . You'll notice that **Microsoft Edge** and **Microsoft Bing** now have working uninstall options that were greyed out before. Just make sure you install your preferred browser and set it as the default before removing Edge, so you're not left without a way to browse the web.

#### Manually enable DMA

##### A PowerShell workaround if you prefer doing it yourself

If you'd rather not install a third-party app, you can enable DMA manually through PowerShell. The process is a bit more involved, but it works just as well.
The reason you can't simply edit the registry value in the normal way is that Windows has a **User Choice Protection Driver (UCPD)** that blocks changes to protected settings, including **DeviceRegion** . But there's a simple way around it. To do this, navigate to C:\Windows\System32\WindowsPowerShell\v1.0 in **File Explorer** , and create a copy of **powershell.exe** in the same folder. You should see a new file named something like **powershell - Copy.exe** .
Now double-click the copied file to open it. Because UCPD monitors the original PowerShell binary but doesn't recognize the copy, you can run registry commands without being blocked. In the PowerShell window, paste this command and press Enter:
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Control Panel\DeviceRegion" -Name "DeviceRegion" -Value 0x0000044
This sets the **DeviceRegion** to Ireland, which is the same thing that happens when you choose an EEA country during a fresh Windows setup. Once done, close the PowerShell window and delete the copied file from the folder to clean up.
To verify it worked, go to **Settings > Time & language > Language & region** and check that **Device setup region** shows **Ireland** . If it does, DMA mode is active, and you can uninstall Edge and Bing from **Settings > Apps > Installed apps** just like you would with the Wintoys method.
If you ever want to revert, you can change the DeviceRegion value back to your actual country code. For the US, for example, the value is **0xf4** . Microsoft maintains a full list of geographic region codes in its documentation.

##### A useful trick with a small trade-off

Enabling DMA mode is probably the cleanest way to remove Edge and Bing without [running a debloating script that could break your system](https://www.makeuseof.com/free-windows-11-debloating-script-makes-pc-better/). The end result is a system state that is identical to what you'd get if you originally set up Windows in an EU country, so it's not a hack that Microsoft can easily patch out.
That said, keep in mind that your Device setup region will show an EEA country, which is a cosmetic change but one worth knowing about. It shouldn't affect day-to-day functionality since your actual Country or region setting stays the same. If you're comfortable with that, this is an easy way to take back control over what stays on your PC and what doesn't.

* [Windows](https://www.makeuseof.com/free-windows-11-debloating-script-makes-pc-better/)
* [Microsoft Edge](https://www.makeuseof.com/free-windows-11-debloating-script-makes-pc-better/)
* [Windows 11](https://www.makeuseof.com/free-windows-11-debloating-script-makes-pc-better/)

##### Follow Followed Share [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) [X](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) [WhatsApp](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) [Threads](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) [Bluesky](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) [LinkedIn](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) [Reddit](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) [Flipboard](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) [Copy link](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) [Email](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) Technology Explained

##### PC & Mobile

###### [I turned off this Windows 11 background setting and instantly felt better about my PC](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse)

###### [Your router and phone are probably fighting over DNS without you realizing it](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse)

###### [I don’t trust free backup apps, but this open-source one changed my mind](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse)

###### [See More](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) [I ditched Android’s app drawer for this, and now I find my apps instantly](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse)

###### [My laptop fans were driving me crazy until I changed this overlooked setting](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse)

###### [I have been waiting years for AirPods Max 2 — Apple finally gave me a reason to buy](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse)

###### [See More](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse) [Windows 11 has a new Start menu — here's how to unlock it](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse)

###### [I debloated my Android phone without root and it finally feels clean again](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse)

###### [How to Enable or Disable the SmartScreen Filter in Windows](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwindows-11-setting-to-uninstall-edge-bing%2F%2F&src=sdkpreparse)

Reply / Post Attachment(s) Please respect our [community guidelines](https://www.valnetinc.com/en/terms-of-use#community-guidelines). No links, inappropriate language, or spam.
Your comment has not been saved
[Send confirmation email](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
Thiago [Thiago](https://www.makeuseof.com/profile/HB112032/)[Thiago](https://www.makeuseof.com/profile/HB112032/)#HB112032 Member since 2026-03-15 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/HB112032/)Just ask Gemini, it will tell you straight away lol.

* 2026-03-15 16:19:25
  Send money [Send money](https://www.makeuseof.com/profile/AP186107/)[Send money](https://www.makeuseof.com/profile/AP186107/)#AP186107 Member since 2026-02-05 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/AP186107/)thank you! I can't stand Bing and hate when the computer uses it by default. Edge not so much but I prefer chrome
* 2026-03-16 12:42:25
  Isura [Isura](https://www.makeuseof.com/profile/DI808933/)[Isura](https://www.makeuseof.com/profile/DI808933/)#DI808933 Member since 2025-11-06 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/DI808933/)been using edge browser over 5 years. im just a casual user and edge has essential features to drive though like gestures, save high quality images, installing apps on websites etc.
* 2026-03-16 00:32:53
  Sean [Sean](https://www.makeuseof.com/profile/VT533677/)[Sean](https://www.makeuseof.com/profile/VT533677/)#VT533677 Member since 2025-11-24 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/VT533677/)Bing, fine. But edge? And use what? Chrome? FF? Brave? Pfft no thanks.
* 2026-03-15 11:29:28
  Kasey [Kasey](https://www.makeuseof.com/profile/UP887946/)[Kasey](https://www.makeuseof.com/profile/UP887946/)#UP887946 Member since 2025-10-10 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/UP887946/)Literally anything is better than Edge. Plus if you're using Edge you're using Chrome lmfao
* 2026-03-15 12:35:30
  Sean [Sean](https://www.makeuseof.com/profile/VT533677/)[Sean](https://www.makeuseof.com/profile/VT533677/)#VT533677 Member since 2025-11-24 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/VT533677/)Kasey well no. The data proves otherwise. And chrome and chromium are not the same thing. One is a browser, the other is the render engine. Chrome and Edge are browsers. Both use the chromium engine for page rendering. There's a difference
* 2026-03-16 02:40:18
  Thiago [Thiago](https://www.makeuseof.com/profile/HB112032/)[Thiago](https://www.makeuseof.com/profile/HB112032/)#HB112032 Member since 2026-03-15 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/HB112032/)Yeah turns out edge is actually better and faster than Chrome, also has better memory management.
* 2026-03-15 16:14:51
  Ray [Ray](https://www.makeuseof.com/profile/WS761866/)[Ray](https://www.makeuseof.com/profile/WS761866/)#WS761866 Member since 2025-09-01 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/WS761866/)Why install Chrome? Edge is actually better. Chrome is a conduit for Google advertising.
* 2026-03-16 01:23:19
  Jim [Jim](https://www.makeuseof.com/profile/WH569886/)[Jim](https://www.makeuseof.com/profile/WH569886/)#WH569886 Member since 2026-03-16 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/WH569886/)So you're implying that Edge is *not* a conduit for advertising? M365? Copilot? Teams?
* 2026-03-16 02:41:49
* Terms
* Privacy
* Feedback

##### Recommended [Windows widgets are great... but only if you change these 5 settings](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)

##### [5 Linux terminal commands that fix most of my system problems](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)

##### [Microsoft is finally fixing the "white flash" issue plaguing Windows users](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)

##### [I tweaked these 3 Windows settings and my gaming lag disappeared](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)

* [Join Our Team](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)
* [Our Audience](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)
* [About Us](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)
* [Press & Events](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)
* [Media Coverage](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)
* [Contact Us](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)
* Follow Us
* [Advertising](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)
* [Careers](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)
* [Terms](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)
* [Privacy](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)
* [Policies](https://www.makeuseof.com/windows-widgets-great-if-change-settings/)
  [MakeUseOf](https://www.makeuseof.com/windows-widgets-great-if-change-settings/) is part of the [Valnet Publishing Group](https://www.valnetinc.com/en/) Copyright © 2026 Valnet Inc.