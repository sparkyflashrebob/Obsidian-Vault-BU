---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

notify from smartphone to android wear with autowear and tasker : r/tasker
[Skip to main content](https://www.reddit.com/r/tasker/comments/y8b17r/notify_from_smartphone_to_android_wear_with/#main-content) notify from smartphone to android wear with autowear and tasker : r/tasker
Open menu
Open navigation 
Go to Reddit Home
[Ask](https://www.reddit.com/answers/)
Find anything
[Sign Up](https://www.reddit.com/register/)
Sign up for Reddit
[Log In](https://www.reddit.com/login/)
Log in to Reddit
Expand user menu
Open settings menu
[Skip to Sign up](https://www.reddit.com/r/tasker/comments/y8b17r/notify_from_smartphone_to_android_wear_with/#left-sidebar-container) [Skip to Right Sidebar](https://www.reddit.com/r/tasker/comments/y8b17r/notify_from_smartphone_to_android_wear_with/#right-sidebar-container)
Back
[Go to tasker](https://www.reddit.com/r/tasker/)
[r/tasker](https://www.reddit.com/r/tasker/) â€¢ 4y ago
[marco-1234](https://www.reddit.com/user/marco-1234/)
Locked post
Stickied post
Archived post
\* Award this post
\* Report

### notify from smartphone to android wear with autowear and tasker

Hello, I would like that my smartphone notify to my smartwatch (android OS wear) if the charge of smartphone's battery is 15%. Can someone help me? Thanks
Read more
1 Â· 4

### Comments Section

[Thetechguru\_net](https://www.reddit.com/user/Thetechguru_net/)
â€¢ [4y ago](https://www.reddit.com/r/tasker/comments/y8b17r/comment/it0w182/)

```
Profile: Phone Is Low
Settings: Restore: yes Notification: no
	State: Battery Level [ From:0 To:15]

Enter Task: Low

A1: AutoWear Notification [
     Configuration: Title: Your phone battery is low.
     Show Now: true
     Vibration Pattern: 0,191,198,234,232,200
     Trigger Event: true
     Haptic Feedback: true
     Name: Phone is Low
     Timeout (Seconds): 20 ]
```

1
[marco-1234](https://www.reddit.com/user/marco-1234/)
OP â€¢ [4y ago](https://www.reddit.com/r/tasker/comments/y8b17r/comment/it1bcl1/)
Thank you, it was just the part with autowear that I couldn't create. I am not an expert on this plug in. I'll try this task.
1
[Continue this thread](https://www.reddit.com/r/tasker/comments/y8b17r/comment/it0w182/?force-legacy-sct=1)
[lefthand\_thread](https://www.reddit.com/user/lefthand_thread/)
â€¢ [4y ago](https://www.reddit.com/r/tasker/comments/y8b17r/comment/it0ilpe/)
Simple. You can do the following: Profile > State > Battery Level 0,15 Task > Send an SMS to yourself. Which will notify you on your watch.
3
[Babaorum](https://www.reddit.com/user/Babaorum/)
â€¢ [4y ago](https://www.reddit.com/r/tasker/comments/y8b17r/comment/it1qgeu/)
Hi! Here is my simple profile (French language for me):

```
Profile: Charge batterie <20%
	State: Battery Level [ From:0 To:20 ]

Enter Task: Anon

A1: Beep [
     Frequency: 8000
     Duration: 1000
     Amplitude: 50
     Stream: 2 ]

A2: Notify [
     Title: Batterie <20%
     Icon: hd_aaa_nixx_plug
     Number: 0
     Priority: 5
     LED Colour: Red
     LED Rate: 1000
     Category: super_tasker_notifications_created_by_me_the_developer ]

A3: AutoWear Notification [
     Configuration: Title: Batterie tÃ©lÃ©phone faible
     Text: < 20% !
     Icon: android.resource://net.dinglisch.android.taskerm/hl_aaa_nixx_plug
     Show Now: true
     Vibration Pattern: 0,107,2620,823,1504,203
     Trigger Event: true
     Haptic Feedback: true
     Command to show: lowphonebatterynotif
     Name: lowphonebattery
     Timeout (Seconds): 20
     Structure Output (JSON, etc): On ]
```

1

### People also ask about section

People also ask about
Most useful Tasker profiles for beginners
For beginners, Tasker's **AI Automation Generator and the Tasky interface** simplify creating useful profiles, moving beyond manual setup.

##### Getting Started with Tasker

```
*   **Utilize the AI Automation Generator** : You can tell Tasker in natural language what you want to automate, and it will generate the profile for you, serving as a learning tool to see how automations are built. "Just tell Tasker what you want to automate and it'll create it for you!"
*   **Explore Tasky for simplified routines** : Tasky provides a new UI that hides complexity, allowing new users to easily enable pre-built routines from a curated list without needing to understand all the intricate Tasker settings. "It's a totally new UI for Tasker that hides a lot about how Tasker works and makes it very simple for a newcomer to get started with it."
*   **Leverage TaskerNet for examples** : TaskerNet offers shared profiles and tasks from other users, which can be imported directly or used as inspiration. "Also taskernet can provide examples or full projects by other tasker users, but someone else can chime in there as I'm not the type to use it."
```

##### Common and Useful Beginner Profiles

```
*   **Location-based actions** : Automate tasks like sending an SMS when entering or leaving a specific GPS location. "Use a location based profile, and make the task that sends the SMS as an  *exit task* ."
*   **Connectivity checks** : Create a profile to test for an internet connection before performing actions that require it. "I am trying to implement a task. The task tests for internet connection, if there is the performs an action."
*   **Bluetooth-triggered actions** : Automatically play music or change settings when connecting to car Bluetooth or other devices. "Play songs on Spotify when connected to car bluetooth"
```

##### Troubleshooting for Beginners

```
*   **Check Tasker logs for errors** : If a profile isn't triggering, review the logs for errors that might be causing Tasker to disable it. "This happens, when the profile and related task have a error in it, what causes the profile or the related task to crash again and again, what causes Tasker to disable it!"
*   **Ensure proper app permissions** : Verify that Tasker has all necessary permissions and is excluded from battery optimization to prevent profiles from becoming inactive. "I'm pretty sure that I've disabled battery optimization and Tasker is not being put into deep sleep."
```

Are you looking for specific types of automations, such as those related to notifications or app usage?
[Show More](https://www.reddit.com/answers/0a22b2d1-14b1-42e3-8662-a9cbd0005775/?q=Most+useful+Tasker+profiles+for+beginners&source=PDP&ep=pdp_unit&relatedPostId=t3_y8b17r)
[Creative ways to automate daily tasks](https://www.reddit.com/answers/161316b0-efc8-4064-a6dc-da72acf67b75/?q=Creative+ways+to+automate+daily+tasks&source=PDP&ep=pdp_unit&relatedPostId=t3_y8b17r)
[Best plugins to enhance Tasker functionality](https://www.reddit.com/answers/d344b5ea-523b-497c-bd24-039b6bd64109/?q=Best+plugins+to+enhance+Tasker+functionality&source=PDP&ep=pdp_unit&relatedPostId=t3_y8b17r)
[Unique Tasker projects to inspire automation](https://www.reddit.com/answers/135ed0eb-5216-4d6e-9ed0-3ce330c9c68f/?q=Unique+Tasker+projects+to+inspire+automation&source=PDP&ep=pdp_unit&relatedPostId=t3_y8b17r)
[Tips for troubleshooting common Tasker issues](https://www.reddit.com/answers/78b4aea3-5a9d-4782-89cc-8ac647b5538b/?q=Tips+for+troubleshooting+common+Tasker+issues&source=PDP&ep=pdp_unit&relatedPostId=t3_y8b17r)

### More posts you may like

Related posts
\* [Widgets on iOS 27 Public Beta](https://www.reddit.com/r/CARROTweather/comments/1vci58b/widgets_on_ios_27_public_beta/) [r/CARROTweather](https://www.reddit.com/r/CARROTweather/) â€¢ 10d ago [

##### Widgets on iOS 27 Public Beta

](https://www.reddit.com/r/CARROTweather/comments/1vci58b/widgets\_on\_ios\_27\_public\_beta/) 11 upvotes Â· 6 comments
\* [What is the use of this Add device option we see when clicking on a wifi name in the settings? (OOS 10)](https://www.reddit.com/r/oneplus/comments/x4pr3w/what_is_the_use_of_this_add_device_option_we_see/) [r/oneplus](https://www.reddit.com/r/oneplus/) â€¢ 4y ago [

##### What is the use of this Add device option we see when clicking on a wifi name in the settings? (OOS 10)

](https://www.reddit.com/r/oneplus/comments/x4pr3w/what\_is\_the\_use\_of\_this\_add\_device\_option\_we\_see/) 46 upvotes Â· 20 comments
\* [I made Tablo4U â€” a browser front-end for Tablo 4th Gen (guide + live player + DVR), free & open source](https://www.reddit.com/r/tablotv/comments/1uwtpcp/i_made_tablo4u_a_browser_frontend_for_tablo_4th/) [r/tablotv](https://www.reddit.com/r/tablotv/) â€¢ 28d ago [

##### I made Tablo4U â€” a browser front-end for Tablo 4th Gen (guide + live player + DVR), free & open source

](https://www.reddit.com/r/tablotv/comments/1uwtpcp/i\_made\_tablo4u\_a\_browser\_frontend\_for\_tablo\_4th/) 4 55 upvotes Â· 17 comments
\* [Smartwatch](https://www.reddit.com/r/NiagaraLauncher/comments/1rbsydn/smartwatch/) [r/NiagaraLauncher](https://www.reddit.com/r/NiagaraLauncher/) â€¢ 6mo ago [

##### Smartwatch

](https://www.reddit.com/r/NiagaraLauncher/comments/1rbsydn/smartwatch/) 3 51 upvotes Â· 9 comments
\* [\[Dev\] I added native Tasker integration to my terminal-style Android launcher. Looking for feedback from actual Tasker users](https://www.reddit.com/r/tasker/comments/1v4ails/dev_i_added_native_tasker_integration_to_my/) [r/tasker](https://www.reddit.com/r/tasker/) â€¢ 19d ago [

##### [Dev] I added native Tasker integration to my terminal-style Android launcher. Looking for feedback from actual Tasker users

](https://www.reddit.com/r/tasker/comments/1v4ails/dev\_i\_added\_native\_tasker\_integration\_to\_my/) 4 25 upvotes Â· 8 comments
\* [First glimpse on our native Android app](https://www.reddit.com/r/CraftDocs/comments/1r0aetl/first_glimpse_on_our_native_android_app/) [r/CraftDocs](https://www.reddit.com/r/CraftDocs/) â€¢ 6mo ago [

##### First glimpse on our native Android app

](https://www.reddit.com/r/CraftDocs/comments/1r0aetl/first\_glimpse\_on\_our\_native\_android\_app/) 1:04 45 upvotes Â· 19 comments
\* [Display step-count on Apple Watch Face](https://www.reddit.com/r/AppleWatch/comments/xpf9dg/display_stepcount_on_apple_watch_face/) [r/AppleWatch](https://www.reddit.com/r/AppleWatch/) â€¢ 4y ago [

##### Display step-count on Apple Watch Face

](https://www.reddit.com/r/AppleWatch/comments/xpf9dg/display\_stepcount\_on\_apple\_watch\_face/) 49 upvotes Â· 42 comments
\* [Android app to get to know your SOD (Screen On Time)](https://www.reddit.com/r/androidapps/comments/xwdev5/android_app_to_get_to_know_your_sod_screen_on_time/) [r/androidapps](https://www.reddit.com/r/androidapps/) â€¢ 4y ago [

##### Android app to get to know your SOD (Screen On Time)

](https://www.reddit.com/r/androidapps/comments/xwdev5/android\_app\_to\_get\_to\_know\_your\_sod\_screen\_on\_time/) 4 upvotes Â· 9 comments
\* [WidgetRelay, a Tasker Plugin to read & click Android widgets](https://www.reddit.com/r/tasker/comments/1v9b89s/widgetrelay_a_tasker_plugin_to_read_click_android/) [r/tasker](https://www.reddit.com/r/tasker/) â€¢ 14d ago [

##### WidgetRelay, a Tasker Plugin to read & click Android widgets

](https://www.reddit.com/r/tasker/comments/1v9b89s/widgetrelay\_a\_tasker\_plugin\_to\_read\_click\_android/) 34 upvotes Â· 19 comments
\* [Try out my Themes on StressWatch :) \[OC\]](https://www.reddit.com/r/applewatchfaces/comments/1rzolk0/try_out_my_themes_on_stresswatch_oc/) [r/applewatchfaces](https://www.reddit.com/r/applewatchfaces/) â€¢ 5mo ago [

##### Try out my Themes on StressWatch :) [OC]

](https://www.reddit.com/r/applewatchfaces/comments/1rzolk0/try\_out\_my\_themes\_on\_stresswatch\_oc/) 8 17 upvotes Â· 25 comments
\* [Poor signals on P7pro: Is this what P6 users complained about?](https://www.reddit.com/r/GooglePixel/comments/y3zx33/poor_signals_on_p7pro_is_this_what_p6_users/) [r/GooglePixel](https://www.reddit.com/r/GooglePixel/) â€¢ 4y ago [

##### Poor signals on P7pro: Is this what P6 users complained about?

](https://www.reddit.com/r/GooglePixel/comments/y3zx33/poor\_signals\_on\_p7pro\_is\_this\_what\_p6\_users/) 8 upvotes Â· 22 comments
\* [Power failure detection and Alert through SMS](https://www.reddit.com/r/homeautomation/comments/xfnjik/power_failure_detection_and_alert_through_sms/) [r/homeautomation](https://www.reddit.com/r/homeautomation/) â€¢ 4y ago [

##### Power failure detection and Alert through SMS

](https://www.reddit.com/r/homeautomation/comments/xfnjik/power\_failure\_detection\_and\_alert\_through\_sms/) 4 upvotes Â· 22 comments
\* [View iPad battery % on iPhone](https://www.reddit.com/r/shortcuts/comments/y4z6mc/view_ipad_battery_on_iphone/) [r/shortcuts](https://www.reddit.com/r/shortcuts/) â€¢ 4y ago [

##### View iPad battery % on iPhone

](https://www.reddit.com/r/shortcuts/comments/y4z6mc/view\_ipad\_battery\_on\_iphone/) 8 upvotes Â· 5 comments
\* [No Background Sync On Android - Almost lost 6+ weeks of un-backed up photos/videos](https://www.reddit.com/r/enteio/comments/1vdfguw/no_background_sync_on_android_almost_lost_6_weeks/) [r/enteio](https://www.reddit.com/r/enteio/) â€¢ 9d ago [

##### No Background Sync On Android - Almost lost 6+ weeks of un-backed up photos/videos

](https://www.reddit.com/r/enteio/comments/1vdfguw/no\_background\_sync\_on\_android\_almost\_lost\_6\_weeks/) 29 upvotes Â· 20 comments
\* [Android app](https://www.reddit.com/r/yikyak/comments/1udu634/android_app/) [r/yikyak](https://www.reddit.com/r/yikyak/) â€¢ 2mo ago [

##### Android app

](https://www.reddit.com/r/yikyak/comments/1udu634/android\_app/) 7 upvotes Â· 6 comments
\* [Cannot use the app, i can't select Battery Optimization Flag](https://www.reddit.com/r/tasker/comments/x8d3dw/cannot_use_the_app_i_cant_select_battery/) [r/tasker](https://www.reddit.com/r/tasker/) â€¢ 4y ago [

##### Cannot use the app, i can't select Battery Optimization Flag

](https://www.reddit.com/r/tasker/comments/x8d3dw/cannot\_use\_the\_app\_i\_cant\_select\_battery/) 3 upvotes Â· 11 comments
\* [Issue with wireless (IOS) Devices connectivity to Unifi AP](https://www.reddit.com/r/Ubiquiti/comments/xule7g/issue_with_wireless_ios_devices_connectivity_to/) [r/Ubiquiti](https://www.reddit.com/r/Ubiquiti/) â€¢ 4y ago [

##### Issue with wireless (IOS) Devices connectivity to Unifi AP

](https://www.reddit.com/r/Ubiquiti/comments/xule7g/issue\_with\_wireless\_ios\_devices\_connectivity\_to/) 5 upvotes Â· 15 comments
\* [Suggested way for mobile phone presence detection?](https://www.reddit.com/r/homeassistant/comments/y78mez/suggested_way_for_mobile_phone_presence_detection/) [r/homeassistant](https://www.reddit.com/r/homeassistant/) â€¢ 4y ago [

##### Suggested way for mobile phone presence detection?

](https://www.reddit.com/r/homeassistant/comments/y78mez/suggested\_way\_for\_mobile\_phone\_presence\_detection/) 6 comments
\* [Help! Can longer send or receive calls on unlocked S20 FE 5G.](https://www.reddit.com/r/ATT/comments/wwurbp/help_can_longer_send_or_receive_calls_on_unlocked/) [r/ATT](https://www.reddit.com/r/ATT/) â€¢ 4y ago [

##### Help! Can longer send or receive calls on unlocked S20 FE 5G.

](https://www.reddit.com/r/ATT/comments/wwurbp/help\_can\_longer\_send\_or\_receive\_calls\_on\_unlocked/) 4 upvotes Â· 65 comments
\* [Attaching Apple Watch Cellular Plan to Watch](https://www.reddit.com/r/freedommobile/comments/y57qkr/attaching_apple_watch_cellular_plan_to_watch/) [r/freedommobile](https://www.reddit.com/r/freedommobile/) â€¢ 4y ago [

##### Attaching Apple Watch Cellular Plan to Watch

](https://www.reddit.com/r/freedommobile/comments/y57qkr/attaching\_apple\_watch\_cellular\_plan\_to\_watch/) 2 upvotes Â· 10 comments
\* [Qt Widgets in 10 years?](https://www.reddit.com/r/QtFramework/comments/1qr0s6d/qt_widgets_in_10_years/) [r/QtFramework](https://www.reddit.com/r/QtFramework/) â€¢ 6mo ago [

##### Qt Widgets in 10 years?

](https://www.reddit.com/r/QtFramework/comments/1qr0s6d/qt\_widgets\_in\_10\_years/) 34 upvotes Â· 75 comments
\* [Tool Quality Inc - a simple code mode that makes tools do more](https://www.reddit.com/r/SoftwareInc/comments/1ve2h05/tool_quality_inc_a_simple_code_mode_that_makes/) [r/SoftwareInc](https://www.reddit.com/r/SoftwareInc/) â€¢ 9d ago [

##### Tool Quality Inc - a simple code mode that makes tools do more

](https://www.reddit.com/r/SoftwareInc/comments/1ve2h05/tool\_quality\_inc\_a\_simple\_code\_mode\_that\_makes/) 2 44 upvotes Â· 6 comments
\* [Back at work on my motion tracker app](https://www.reddit.com/r/alienrpg/comments/1thj1e1/back_at_work_on_my_motion_tracker_app/) [r/alienrpg](https://www.reddit.com/r/alienrpg/) â€¢ 3mo ago [

##### Back at work on my motion tracker app

](https://www.reddit.com/r/alienrpg/comments/1thj1e1/back\_at\_work\_on\_my\_motion\_tracker\_app/) 31 upvotes Â· 7 comments
\* [Android](https://www.reddit.com/r/blockheads/comments/1urkth9/android/) [r/blockheads](https://www.reddit.com/r/blockheads/) â€¢ 1mo ago [

##### Android

](https://www.reddit.com/r/blockheads/comments/1urkth9/android/) 6 upvotes Â· 5 comments
\* [Best way to get phone to ring when I receive an e-mail alert?](https://www.reddit.com/r/Forex/comments/x4xhtm/best_way_to_get_phone_to_ring_when_i_receive_an/) [r/Forex](https://www.reddit.com/r/Forex/) â€¢ 4y ago [

##### Best way to get phone to ring when I receive an e-mail alert?

](https://www.reddit.com/r/Forex/comments/x4xhtm/best\_way\_to\_get\_phone\_to\_ring\_when\_i\_receive\_an/) 7 upvotes Â· 13 comments

#### View Post in

[ç¹ é«”ä¸ æ–‡](https://www.reddit.com/r/tasker/comments/y8b17r/notify_from_smartphone_to_android_wear_with/?tl=zh-hant)
See more See fewer
[Magyar](https://www.reddit.com/r/tasker/comments/y8b17r/notify_from_smartphone_to_android_wear_with/?tl=hu)
[Ø§Ù„Ø¹Ø±Ø¨ÙŠØ©](https://www.reddit.com/r/tasker/comments/y8b17r/notify_from_smartphone_to_android_wear_with/?tl=ar)
[Deutsch](https://www.reddit.com/r/tasker/comments/y8b17r/notify_from_smartphone_to_android_wear_with/?tl=de)
[Norsk (BokmÃ¥l)](https://www.reddit.com/r/tasker/comments/y8b17r/notify_from_smartphone_to_android_wear_with/?tl=no)

### Community Info Section

[r/tasker](https://www.reddit.com/r/tasker/)
Join
Tasker: Total Automation for Android
Public
Anyone can view, post, and comment to this community

#### Top Posts

```
*  [Reddit reReddit: Top posts of October 19, 2022](https://www.reddit.com/posts/2022/october-19-1/global/)
*  [Reddit reReddit: Top posts of October 2022](https://www.reddit.com/posts/2022/october/global/)
*  [Reddit reReddit: Top posts of 2022](https://www.reddit.com/posts/2022/global/)
*  [Home](https://www.reddit.com/?feed=home)
*  [Popular](https://www.reddit.com/r/popular/)
*  [News](https://www.reddit.com/news/)
*  [Explore](https://www.reddit.com/explore/)
*  [Best of Reddit](https://www.reddit.com/posts/2026/global/)
*  [Best of Reddit in Portuguese](https://www.reddit.com/posts/2026/tl-pt-BR/)
*  [Best of Reddit in German](https://www.reddit.com/posts/2026/tl-de/)
*  [Reddit Rules](https://www.redditinc.com/policies/content-policy)
*  [Privacy Policy](https://www.reddit.com/policies/privacy-policy)
*  [User Agreement](https://www.redditinc.com/policies/user-agreement)
*  [Your Privacy Choices](https://support.reddithelp.com/hc/articles/43980704794004)
*  [Accessibility](https://support.reddithelp.com/hc/sections/38303584022676-Accessibility)
*  [Reddit, Inc. Â© 2026. All rights reserved.](https://redditinc.com/)
```

Join the most real place on the internet
Continue with Apple
ï£¿â€…Sign in with Apple
[Continue with Phone Number](https://www.reddit.com/login/)
[Continue with Email](https://www.reddit.com/register/)
By continuing, you agree to our [User Agreement](https://www.redditinc.com/policies/user-agreement) and acknowledge that you understand the [Privacy Policy](https://www.redditinc.com/policies/privacy-policy).
0cAFcWeA481e2dfdiPcEJ2hL7BNnHz22311RvQlrHCc2JoxosUe5aZgB\_oYYKocPTS5eIsTGjuvYLORFYevu1LvivWiiQkmxWE-w54KX5oJkGLGDY6HSyL26jsrDK4gH6ZatuIskKNZoRuMhR5NkfIQAKtvkCzMxiIYykvRof7uqYTlLRQYo793HNjF8mHzTBrKiWp7PVMGKA7su4qA4P0wstIJ0P5Xxo3lN0\_HrKUscszrQw3V0Lry7pIJ5ncTJ8ISLmNnqE4Q4SU3IQp8W9wk3V5W2V2xtolXapMl07PFpwWROCjAqk3g009d8U26En4akwEd6gUiJPZd2lY4h7s7u6YLdOP1Yhz9PjVwgKwxzKYQgBh2Xk6\_DA4kAaZkDlPK9ztZw9CVw-2bOikkzVH8baPkmHtPg9qu7g5L5pxbDkyRJr-0ZXjNHK3GldhY8jY7fjsT4Tgkr297U2LPnwDYhjvAdofQkGDDaJZVm5DCN9lA8sVBbMMjJVkA3mm-Ii-bA3AOzH-Bqda-oagNLYtPOoFlmiI8RipZYoTqgPcsh6iG6QMZpo5AnfA1Yd3mgp3Rcmo8JtJellx7QQYHPa6\_lu8oPC8bPpqBY\_HjWY8vt\_aRzDuMH1BCh3KtKUl5EVsgWCwyxc6hr7qvh12EZ82AyG7sssCYhHQeJhhBe3okxcEdoLvyQIQIksABLl2-eLBqoR66jHYlzHMC5r5bnj41-\_RoKhR\_XSeRVbDmXqfywmQcO4bt0Dr4uJZkhasnR68TvY4leq0aaqMx8pSkNUOXGQydGAuNsM1K-Kb\_C9BFgA3jGsJx83J\_X-EPACGmpmaRxQmPOeMDhALtBHXhJQKwYzGTs6A07Gpa6F0BuHrVd7R3su4JvvZzwydXJf\_B\_MQmJN-gAOldWNCmfLgH5bxvEkM8AtQMvYU9NmnL1KB88P-S6MglC6nxwIOGQbaP50HU58Hslg-tKTEDYyyhxL62QbEKzG0Ia1tSQdpyk3q1mCfMmCxYXZsBaZ1uz51gBXS0vkhTlv13yqhZ5AfZyejCRBwHeMiYD32rSTNIu7pkOzw2-\_VuYqAH8FN6OyOziclw27h1j0zPvD6sGgekaUN\_5VGvz41VNN1LgG6zkzGdzU9u5BCRxV5xwNnXIBR9COKhvEyv3-u\_wTYUpuyj8mz9gK5m\_ms4vdfPqYIKxWdCHffAl\_yUfvfBF\_zW5HOmtVuypHSIRlqwTCebVILGBI4M3TJ4Y6pQh5VloecS2rt3XWmAzHyByMabCjfqWx3y9YrdlQu7QJH92lYIW-1GiCCLRz3FwNIg8IM3U9Pw38sSQtVI3E-F842OblONRjKIM9Gf1dTn9royHcSnXyGzqMTk4ysNvVhln2fPGIPqY1t4evrB2QEsEBgQYkunrEmf\_ps57AdWBibIX4rLFhBg0eyaK3uEg9nm\_G-XYTp4b7mjBJG3Du\_JuVD1AW7P4Xg1OuqXAH14lzovuRIkG0sKwm0fDzIlRInXNDdJ-FGsYhhQgvO8rlutHHyfc8Gq0w4xtgQ0c1bPent0YAI6rYBOG3dQwPJmTWQslF4TWSFoeeKj\_bQeLM6tHzcuzFItpSeVy0gpjzzrHu4o8O3f5X2OAJ\_kZZjx-WwqLsNn8Fmt2F1uPSlVuO\_dW2RX0-eM8Z7QSujNz4-owxOAKCZL5z3OSqGA9JCQVtKVEzACVO-CdGSd65wdWdg5XTn-8Xs9-7RbYhxpnjOy738EbLAUqFocw-iaLEkvX0n6iF\_m5qyvWPMi\_6smAO27pKq3CEgnNHzQVfoDi9QLoCieRPNTw3P2c2rYr7umDhNMpPIiQgGXbTrgCHCqEHkp934kqQXRgCgpyF7tcE5dEKOosj49gYIM3xjO-RMT6YPRtWywkEnUwhIR8qwHlrn2Dtj7BiB-vGzIS3ehrfsNDBB7-eYwyxVSRQwbQc1p9E41pkyqk\_97haAHht9nUFCJtMoT4GvYXcza7ZkVcdhusaH5Xx\_1BK0pOZq1bLWQz92h4EEvnhONDV-LaRK01cjcsw5M4xOjqO9T\_t\_Y12M42z392XdGP01oCwMZZqRGmCxvjJZxEBv1W3z2-xChvH2moRcNp3\_wDx7cXLbt4PM62UhgEla1kxTCyDvngvBAIkkfme2gFDGXB91wlUKJt53yoKU3eLHfPpxQ6oaIVQJSpkms8akBG9inJvr\_1GUPzMqFa-JAA