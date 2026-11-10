---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

Use AutoWear to capture triple button press (and remap it to your needs)! : r/tasker
[Skip to main content](https://www.reddit.com/r/tasker/comments/17eqvo6/use_autowear_to_capture_triple_button_press_and/#main-content) Use AutoWear to capture triple button press (and remap it to your needs)! : r/tasker
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
[Skip to Sign up](https://www.reddit.com/r/tasker/comments/17eqvo6/use_autowear_to_capture_triple_button_press_and/#left-sidebar-container) [Skip to Right Sidebar](https://www.reddit.com/r/tasker/comments/17eqvo6/use_autowear_to_capture_triple_button_press_and/#right-sidebar-container)
Back
[Go to tasker](https://www.reddit.com/r/tasker/)
[r/tasker](https://www.reddit.com/r/tasker/) â€¢ 3y ago
[ertmuirm](https://www.reddit.com/user/ertmuirm/)
Locked post
Stickied post
Archived post
\* Award this post
\* Report

### Use AutoWear to capture triple button press (and remap it to your needs)!

While searching for a way to remap the lower physical button on my GW4, I found a way to use accessibility + AutoWear to remap a triple button press on the upper physical button. Just sharing here for those who might find it useful:
1. GW4/5/6 Settings > Accessibility > Advanced > Triple press > (select Mute all)
1. In AutoWear, create action to monitor custom setting change (System, all\_sound\_off). Add a monitor prefix of your choice
1. Add a Profile with AutoWear event for the setting change you just created a monitor for (set command filter as monitor prefix=:=). Corresponding Task can be anything you want!
1. Triple press of upper physical button should now trigger your Task
[u/joaomgcd](https://www.reddit.com/user/joaomgcd/) I wonder if AutoWear can also listen to keyevents? That can allow us to remap the lower physical button so it's not just Samsung Pay / Back / Recents for the GW users
Read more
7 Â· 4

### Comments Section

[ertmuirm](https://www.reddit.com/user/ertmuirm/)
OP â€¢ [3y ago](https://www.reddit.com/r/tasker/comments/17eqvo6/comment/k6jpih1/)
ADD: This event also gets detected when screen is locked, so it means one can use Autowear to unlock the watch (by programmatically entering a passkey) on triple press. This solves the annoying issue of the watch sometimes getting locked when wrist off is detected
1
[Dpure1](https://www.reddit.com/user/Dpure1/)
â€¢ [3y ago](https://www.reddit.com/r/tasker/comments/17eqvo6/comment/k67txog/)
That's cool i will try that! Thanx for sharing!!!
2
[ConcentrateTime9542](https://www.reddit.com/user/ConcentrateTime9542/)
â€¢ [3y ago](https://www.reddit.com/r/tasker/comments/17eqvo6/comment/kfgifaq/)
This is a great idea.
Can you please explain 2nf and 3rd points, how can we create a monitor and use it as trigger ?
1
[Ok\_Smile6981](https://www.reddit.com/user/Ok_Smile6981/)
â€¢ [3y ago](https://www.reddit.com/r/tasker/comments/17eqvo6/comment/kid2wy3/)
Can you provide more detailed instructions? I can't figure out how to do this.
Thank you!!
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
[Show More](https://www.reddit.com/answers/b8eb1ed7-a2a6-4a68-b796-6dc1083d39c3/?q=Most+useful+Tasker+profiles+for+beginners&source=PDP&ep=pdp_unit&relatedPostId=t3_17eqvo6)
[Creative ways to automate daily tasks](https://www.reddit.com/answers/262ba18e-5cb1-4f26-8663-f55cb9bd0697/?q=Creative+ways+to+automate+daily+tasks&source=PDP&ep=pdp_unit&relatedPostId=t3_17eqvo6)
[Best plugins to enhance Tasker functionality](https://www.reddit.com/answers/5671efa5-d0b4-4b03-8d1d-1fb22d181ed1/?q=Best+plugins+to+enhance+Tasker+functionality&source=PDP&ep=pdp_unit&relatedPostId=t3_17eqvo6)
[Unique Tasker projects to inspire automation](https://www.reddit.com/answers/6cac7b7a-420e-4ea3-8b48-8ba5bcd630e8/?q=Unique+Tasker+projects+to+inspire+automation&source=PDP&ep=pdp_unit&relatedPostId=t3_17eqvo6)
[Tips for troubleshooting common Tasker issues](https://www.reddit.com/answers/c9699cf5-021f-45c5-b61a-5f41b1dc6b94/?q=Tips+for+troubleshooting+common+Tasker+issues&source=PDP&ep=pdp_unit&relatedPostId=t3_17eqvo6)

### More posts you may like

Related posts
\* [Push button starter that looks like the choke](https://www.reddit.com/r/projectcar/comments/1rb2iik/push_button_starter_that_looks_like_the_choke/) [r/projectcar](https://www.reddit.com/r/projectcar/) â€¢ 6mo ago [

##### Push button starter that looks like the choke

](https://www.reddit.com/r/projectcar/comments/1rb2iik/push\_button\_starter\_that\_looks\_like\_the\_choke/) 0:10 272 upvotes Â· 19 comments
\* [\[WIP\] Auto pointer layer switching when touching trackball](https://www.reddit.com/r/ErgoMechKeyboards/comments/1v9p0lq/wip_auto_pointer_layer_switching_when_touching/) [r/ErgoMechKeyboards](https://www.reddit.com/r/ErgoMechKeyboards/) â€¢ 13d ago [

##### [WIP] Auto pointer layer switching when touching trackball

](https://www.reddit.com/r/ErgoMechKeyboards/comments/1v9p0lq/wip\_auto\_pointer\_layer\_switching\_when\_touching/) 1:05 73 upvotes Â· 23 comments
\* [Why do I have to use Memory Manager with GHub to have by side buttons work? g604 Lightspeed (Button lag, button assignment)](https://www.reddit.com/r/logitech/comments/16zsn2l/why_do_i_have_to_use_memory_manager_with_ghub_to/) [r/logitech](https://www.reddit.com/r/logitech/) â€¢ 3y ago [

##### Why do I have to use Memory Manager with GHub to have by side buttons work? g604 Lightspeed (Button lag, button assignment)

](https://www.reddit.com/r/logitech/comments/16zsn2l/why\_do\_i\_have\_to\_use\_memory\_manager\_with\_ghub\_to/) 3 upvotes
\* [I built a oneâ€'wrist setup for my mechanical watch + Whoop. would you wear this?](https://www.reddit.com/r/whoop/comments/1ua51up/i_built_a_onewrist_setup_for_my_mechanical_watch/) [r/whoop](https://www.reddit.com/r/whoop/) â€¢ 2mo ago [

##### I built a oneâ€'wrist setup for my mechanical watch + Whoop. would you wear this?

](https://www.reddit.com/r/whoop/comments/1ua51up/i\_built\_a\_onewrist\_setup\_for\_my\_mechanical\_watch/) 0:42 42 upvotes Â· 36 comments
\* [use any length button sequences to trigger actions](https://www.reddit.com/r/homeassistant/comments/16h1lry/use_any_length_button_sequences_to_trigger_actions/) [r/homeassistant](https://www.reddit.com/r/homeassistant/) â€¢ 3y ago [

##### use any length button sequences to trigger actions

](https://www.reddit.com/r/homeassistant/comments/16h1lry/use\_any\_length\_button\_sequences\_to\_trigger\_actions/) 2 upvotes
\* [Use different actions for the Action Button based on focus](https://www.reddit.com/r/applewatchultra/comments/16tl5l2/use_different_actions_for_the_action_button_based/) [r/applewatchultra](https://www.reddit.com/r/applewatchultra/) â€¢ 3y ago [

##### Use different actions for the Action Button based on focus

](https://www.reddit.com/r/applewatchultra/comments/16tl5l2/use\_different\_actions\_for\_the\_action\_button\_based/) 12 upvotes Â· 11 comments
\* [Win + Shift + S snipping tool behavior changed (must click before crosshair shows)](https://www.reddit.com/r/WindowsHelp/comments/16y0dg9/win_shift_s_snipping_tool_behavior_changed_must/) [r/WindowsHelp](https://www.reddit.com/r/WindowsHelp/) â€¢ 3y ago [

##### Win + Shift + S snipping tool behavior changed (must click before crosshair shows)

](https://www.reddit.com/r/WindowsHelp/comments/16y0dg9/win\_shift\_s\_snipping\_tool\_behavior\_changed\_must/) 1 upvote Â· 6 comments
\* [help usingg shortcuts from actions app to toggle silent mode](https://www.reddit.com/r/shortcuts/comments/1766prt/help_usingg_shortcuts_from_actions_app_to_toggle/) [r/shortcuts](https://www.reddit.com/r/shortcuts/) â€¢ 3y ago [

##### help usingg shortcuts from actions app to toggle silent mode

](https://www.reddit.com/r/shortcuts/comments/1766prt/help\_usingg\_shortcuts\_from\_actions\_app\_to\_toggle/) 5 upvotes Â· 11 comments
\* [LPT: Windows virtual desktopsâ€”underrated feature that you should use and remap!](https://www.reddit.com/r/AutoHotkey/comments/16ktzac/lpt_windows_virtual_desktopsunderrated_feature/) [r/AutoHotkey](https://www.reddit.com/r/AutoHotkey/) â€¢ 3y ago [

##### LPT: Windows virtual desktopsâ€”underrated feature that you should use and remap!

](https://www.reddit.com/r/AutoHotkey/comments/16ktzac/lpt\_windows\_virtual\_desktopsunderrated\_feature/) 11 upvotes Â· 25 comments
\* [To those who seen the clicky counter, Im making a "auto count" version](https://www.reddit.com/r/3Dprinting/comments/1njchct/to_those_who_seen_the_clicky_counter_im_making_a/) [r/3Dprinting](https://www.reddit.com/r/3Dprinting/) â€¢ 1y ago [

##### To those who seen the clicky counter, Im making a "auto count" version

](https://www.reddit.com/r/3Dprinting/comments/1njchct/to\_those\_who\_seen\_the\_clicky\_counter\_im\_making\_a/) 0:16 227 upvotes Â· 8 comments
\* [Personal setup (Assembled rack/pulley/smith machine myself)](https://www.reddit.com/r/homegym/comments/1rst9hj/personal_setup_assembled_rackpulleysmith_machine/) [r/homegym](https://www.reddit.com/r/homegym/) â€¢ 5mo ago [

##### Personal setup (Assembled rack/pulley/smith machine myself)

](https://www.reddit.com/r/homegym/comments/1rst9hj/personal\_setup\_assembled\_rackpulleysmith\_machine/) 2 41 upvotes Â· 11 comments
\* [DIY Toothpick Support System](https://www.reddit.com/r/PoorHammer/comments/1qhtfym/diy_toothpick_support_system/) [r/PoorHammer](https://www.reddit.com/r/PoorHammer/) â€¢ 7mo ago [

##### DIY Toothpick Support System

](https://www.reddit.com/r/PoorHammer/comments/1qhtfym/diy\_toothpick\_support\_system/) 184 upvotes Â· 8 comments
\* [Quick-Launch Workshop Preset? It'd save me like 10 button presses.](https://www.reddit.com/r/Competitiveoverwatch/comments/1tqn5rh/quicklaunch_workshop_preset_itd_save_me_like_10/) [r/Competitiveoverwatch](https://www.reddit.com/r/Competitiveoverwatch/) â€¢ 2mo ago [

##### Quick-Launch Workshop Preset? It'd save me like 10 button presses.

](https://www.reddit.com/r/Competitiveoverwatch/comments/1tqn5rh/quicklaunch\_workshop\_preset\_itd\_save\_me\_like\_10/) 329 upvotes Â· 15 comments
\* [Pressing that button as a Solo dev feels awesome ðŸ˜](https://www.reddit.com/r/SoloDevelopment/comments/1ts5s4o/pressing_that_button_as_a_solo_dev_feels_awesome/) [r/SoloDevelopment](https://www.reddit.com/r/SoloDevelopment/) â€¢ 2mo ago [

##### Pressing that button as a Solo dev feels awesome ðŸ˜

](https://www.reddit.com/r/SoloDevelopment/comments/1ts5s4o/pressing\_that\_button\_as\_a\_solo\_dev\_feels\_awesome/) 119 upvotes Â· 15 comments
\* [Autohotkey, bind a shortcut key to quickly mute/unmute Valorant with a single press](https://www.reddit.com/r/VALORANT/comments/17dvyk1/autohotkey_bind_a_shortcut_key_to_quickly/) [r/VALORANT](https://www.reddit.com/r/VALORANT/) â€¢ 3y ago [

##### Autohotkey, bind a shortcut key to quickly mute/unmute Valorant with a single press

](https://www.reddit.com/r/VALORANT/comments/17dvyk1/autohotkey\_bind\_a\_shortcut\_key\_to\_quickly/) 3 upvotes Â· 10 comments
\* [3d Printed Watch Straps Organizer](https://www.reddit.com/r/functionalprint/comments/1tllr8z/3d_printed_watch_straps_organizer/) [r/functionalprint](https://www.reddit.com/r/functionalprint/) â€¢ 3mo ago [

##### 3d Printed Watch Straps Organizer

](https://www.reddit.com/r/functionalprint/comments/1tllr8z/3d\_printed\_watch\_straps\_organizer/) 3 76 upvotes Â· 8 comments
\* [\[Question\] 3d Printed Watch Straps Organizer](https://www.reddit.com/r/Watches/comments/1tllnq2/question_3d_printed_watch_straps_organizer/) [r/Watches](https://www.reddit.com/r/Watches/) â€¢ 3mo ago [

##### [Question] 3d Printed Watch Straps Organizer

](https://www.reddit.com/r/Watches/comments/1tllnq2/question\_3d\_printed\_watch\_straps\_organizer/) 3 77 upvotes Â· 13 comments
\* [\[Guide\] Splatoon-like recenter button using Steam Input](https://www.reddit.com/r/GyroGaming/comments/16qzrsc/guide_splatoonlike_recenter_button_using_steam/) [r/GyroGaming](https://www.reddit.com/r/GyroGaming/) â€¢ 3y ago [

##### [Guide] Splatoon-like recenter button using Steam Input

](https://www.reddit.com/r/GyroGaming/comments/16qzrsc/guide\_splatoonlike\_recenter\_button\_using\_steam/) 36 upvotes Â· 23 comments
\* [Manually machining a watch case from scratch Part 11!](https://www.reddit.com/r/watchmaking/comments/1qt36ui/manually_machining_a_watch_case_from_scratch_part/) [r/watchmaking](https://www.reddit.com/r/watchmaking/) â€¢ 6mo ago [

##### Manually machining a watch case from scratch Part 11!

](https://www.reddit.com/r/watchmaking/comments/1qt36ui/manually\_machining\_a\_watch\_case\_from\_scratch\_part/) 3:00 110 upvotes Â· 11 comments
\* [Manually machining a watch case from scratch Part 4!](https://www.reddit.com/r/watchmaking/comments/1omk7an/manually_machining_a_watch_case_from_scratch_part/) [r/watchmaking](https://www.reddit.com/r/watchmaking/) â€¢ 9mo ago [

##### Manually machining a watch case from scratch Part 4!

](https://www.reddit.com/r/watchmaking/comments/1omk7an/manually\_machining\_a\_watch\_case\_from\_scratch\_part/) 1:40 122 upvotes Â· 12 comments
\* [Hand-sewn push buttons](https://www.reddit.com/r/sewing/comments/1sq4ybz/handsewn_push_buttons/) [r/sewing](https://www.reddit.com/r/sewing/) â€¢ 4mo ago [

##### Hand-sewn push buttons

](https://www.reddit.com/r/sewing/comments/1sq4ybz/handsewn\_push\_buttons/) 170 upvotes Â· 47 comments
\* [Custom Trim Wheel Button Box](https://www.reddit.com/r/HotasDIY/comments/1nisuc2/custom_trim_wheel_button_box/) [r/HotasDIY](https://www.reddit.com/r/HotasDIY/) â€¢ 1y ago [

##### Custom Trim Wheel Button Box

](https://www.reddit.com/r/HotasDIY/comments/1nisuc2/custom\_trim\_wheel\_button\_box/) 88 upvotes Â· 13 comments
\* [Manually machining a watch case from scratch Part 6!](https://www.reddit.com/r/watchmaking/comments/1qpnfjy/manually_machining_a_watch_case_from_scratch_part/) [r/watchmaking](https://www.reddit.com/r/watchmaking/) â€¢ 6mo ago [

##### Manually machining a watch case from scratch Part 6!

](https://www.reddit.com/r/watchmaking/comments/1qpnfjy/manually\_machining\_a\_watch\_case\_from\_scratch\_part/) 1:07 126 upvotes Â· 24 comments
\* [GarlicOS autosaves when opening menu (press Menu + X) - how to disable?](https://www.reddit.com/r/RG35XX/comments/16s8qpu/garlicos_autosaves_when_opening_menu_press_menu_x/) [r/RG35XX](https://www.reddit.com/r/RG35XX/) â€¢ 3y ago [

##### GarlicOS autosaves when opening menu (press Menu + X) - how to disable?

](https://www.reddit.com/r/RG35XX/comments/16s8qpu/garlicos\_autosaves\_when\_opening\_menu\_press\_menu\_x/) 1 upvote Â· 7 comments
\* [Tip: Re-map a second input button to jump to enable boosting forwards](https://www.reddit.com/r/Starfield/comments/1700nho/tip_remap_a_second_input_button_to_jump_to_enable/) [r/Starfield](https://www.reddit.com/r/Starfield/) â€¢ 3y ago [

##### Tip: Re-map a second input button to jump to enable boosting forwards

](https://www.reddit.com/r/Starfield/comments/1700nho/tip\_remap\_a\_second\_input\_button\_to\_jump\_to\_enable/) 4 upvotes Â· 2 comments

#### View Post in

[ç®€ä½“ä¸ æ–‡](https://www.reddit.com/r/tasker/comments/17eqvo6/use_autowear_to_capture_triple_button_press_and/?tl=zh-hans)
See more See fewer
[í• œêµì–´](https://www.reddit.com/r/tasker/comments/17eqvo6/use_autowear_to_capture_triple_button_press_and/?tl=ko)
[PortuguÃªs (Portugal)](https://www.reddit.com/r/tasker/comments/17eqvo6/use_autowear_to_capture_triple_button_press_and/?tl=pt-pt)
[Ø§Ù„Ø¹Ø±Ø¨ÙŠØ©](https://www.reddit.com/r/tasker/comments/17eqvo6/use_autowear_to_capture_triple_button_press_and/?tl=ar)
[Magyar](https://www.reddit.com/r/tasker/comments/17eqvo6/use_autowear_to_capture_triple_button_press_and/?tl=hu)

### Community Info Section

[r/tasker](https://www.reddit.com/r/tasker/)
Join
Tasker: Total Automation for Android
Public
Anyone can view, post, and comment to this community

#### Top Posts

```
*  [Reddit reReddit: Top posts of October 23, 2023](https://www.reddit.com/posts/2023/october-23-1/global/)
*  [Reddit reReddit: Top posts of October 2023](https://www.reddit.com/posts/2023/october/global/)
*  [Reddit reReddit: Top posts of 2023](https://www.reddit.com/posts/2023/global/)
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
0cAFcWeA6Euep03anXD9Ot8VbXUC0DzB8rhy3Oklx9mFDk5lvXOCkkCblVIBLnZd0aAlyAKXV1rSeVlF21yohlpRRhPSYn033Kx55qNx7igunGatRIGCJ9FFkl2bO7fM9cneN6nhciNTsfom7\_mwfrB9yRMShpNMrD6QGnlWJRiCTCYYP5VM-Vwo2SwnwI1TtFKXsLwvoZ3Nk0rwjDKFecUyuqQM-WoctUhmHgzm3kiDZVZQ5JPThDwFoaCqQ-10OQdGOqTL-to8qWhYYmZmqXLoIXb3pOxKNWIlqeVlXXNE8sGvMXL3BY0A6uHbJWooqUcMd8z86nWkX44p4JgJG8L\_\_U5rVx9BfA4\_-EkPi79eiB9Q5QVBKKdQAQP3d3SFg\_asTAqNUbujizHXVfPHYfeBWcNeZdCWnyUadHybM8DorGAqF41pTQR0wr4fGYz2DGliXZxp2cHvTCgUYSLt0jqdQBEUZJFus1gmJjlJt-w\_yZAGytjjhj8F0QsZY8L97JroKeKHU8TLjV5Oft2Zqh05j5EPRv-qPa3RIj13iRV1tKXCL7fkZTVv9aSR6kUO53Jn5hQAORBKwxFdkydJkv3XXYTwLZJzjo7ykEzgZLLdn7DCZQhWawjrq09rHM2KeebdTfpW8GYbHWatRwJsAouEg-vYGScPWaTNWNRWcTCrrjo\_1fWQ7KOsO8Bz7FxKvQz\_SPfwHqRm9gXI9jrdJbdU6cUWwBFy30qlV9CKdEXXUZJp0Xc5hFKckRiltxJxQmgDl1hhMWd1Ux8DoZtrcC9hY5Uls60HcwllseUwDKt8IvOf3gSkX5gqkOZgIv0RFNRnhbbrkarNKJQsdsFJ942A8vUrpy5FDcZ\_wbh\_BSss6mL\_DuM4SskVMcrZhPHc7rrPGiZgXUXt6D38-1p-XOe0tDAvJ5hBSwj\_geBKr2lxYiZxkl\_x6ZAOjL3dfO52Q7kcw0uaFVkDLdpsiocp0ePFXv\_pmZr2VCocREAfGBM5hXS8Gn\_9aKWWQaxuohQSiZkhJ-zD5vrxx\_p-VFUnM6aOY8979ROhVHPrAlIi3PCG708vOFv2PIxRireqivvKtrBSWM0q91hrT7CkqT-PYxcxhM6fXET3dzPPCKELVwD6gxJV8k5bqusvvJAL\_-KMHBLrcO4G\_wmkC8Tt6wikJioc9RzLkAClA0ZRNvFY5WKbIjgmLYkCCNWk\_RibZVasoR1qNffgKnKFYHEC8cUsgaYDFrD9XnHI9-im9ld08CIXjjWy0VeEk9gQRi97\_iFkT0PsGhsvxS6eIknJV0J6JWZVBt7iMChnc6vP\_vID\_ssMugSZ9oeWB2Oit8RdDJQzbg7J0O4Bivx3ssWM5fqWUdkpceTJ7Y9WdMnWa4GCdwGUE7ce9oScUxi8N8EBOVR4mR0aN2cjgRwFdsY5TgY6T\_LwRcrowAX14\_LEblwrmMLX8GUCHpaD1kG5GFjE3IpxOyNpf-cvMWLuZkGdKfNVMcafFYMpDUeWvKu3uli1raZoaXFc1YlXB7Lz8kQqtvjQoIULq3M5fGk3AbASvsBbJE\_s1lSbLfHmneFgBoFOXlkgf\_F\_zYZ4hyvsSed27SdJV1JdFE5ee3VPKgqEMDU0iYm8vSMtWcijcQW3RGhCIb4qVrZT7srQIMpXAfj1ZS6AZiqRBTk0-ZNTDFqqAMEbfCCnOPD2xjbbEmjzQBn-P-G7qA0ziHtFRB1IpksyM472nA-\_OSL17e\_CTn3ZmDmjoYBptBCpWHmDWjdn57TmWm8fsoXtZ32zMhias08McN8Bdus5F2iFdD\_6wxmpmrfXNjgVobdIrQb6H7e3WpmJi\_4Q8ywO38EgYhxw3pIRfUUd1DilzMnmNwXfgnhlvsp7F0Z-i-05DZLGaNRw650C4BfjtPDaaTVqQ1-uWbernydpHWjWawzr1ksBxcDYo4qZs6c9pD31IiamuJrjTz1SPmbZdPvWhZMv6n4vOYMHg24tmYmAMuO9AF67JQ5Ke7rjlj698qrj\_95u4bFH0ClLWCAvVUIhmIVpGAMzb8DcIE4JCb-6\_fgb131YjeP8xAPuXMpG2IT5NX6mqoWslO7aIfClZqcRVAyY55opoxtWXeFiwRoig6\_cBYcsIWWPSAJ7750DtYWXK4Kv4JyHtvxHNmDuQuiV2j9fwGlogTQyIw8KRuyBC5AS2OSdgF5D1vjDKQ9aCHhc8n1\_BvvA