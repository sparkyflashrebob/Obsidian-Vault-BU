---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

Tasker and WearOS – Sean's Technical Ramblings
*expand\_less*
**
[Sean's Technical Ramblings](https://seanb.co.uk/)
\* [About](https://seanb.co.uk/about/)
\* [Photos](https://seanb.co.uk/photos/)
\* [Contact](https://seanb.co.uk/contact/)
*search*
\* [About](https://seanb.co.uk/about/)
\* [Photos](https://seanb.co.uk/photos/)
\* [Contact](https://seanb.co.uk/contact/)

### Tasker and WearOS

Now that I've switched to WearOS for my watch, I've been looking for interesting apps.
There are a couple of automation options for WearOS. IFTTT has an app that can be used on WearOS but the more interesting option is the [AutoWear](https://play.google.com/store/apps/details?id=com.joaomgcd.autowear&hl=en_GB&gl=US) plugin for Tasker.
It's been a long time since I used Tasker, and it took me a while to get back up to speed. As I [wrote](https://seanb.co.uk/2016/08/tasker-for-android/) at the time, Tasker is incredibly powerful but has a user interface that can best be described as challenging. Once you get the hang of it, though, it does get easier… eventually.
The challenge extends to installing the plugins for Tasker. First of all you'll need to install Tasker. It's not free, but well worth the money. You can then install AutoWear. It's also a paid app, and to install it you'll first need to install AutoApps. AutoApps is just a helper application to licence various plugins for Tasker.
When you install AutoWear it will take you through a number of tutorial settings and confirm connection to your device. It will also install the companion app on your watch. Once it's installed, you'll find there are some settings that are managed through the watch app and some that require the phone app.
I've chosen to disable the shake detection option, as I don't think I'll use it and it was firing frequently enough to be a concern for battery life.
The “launcher apps” setting allows you to toggle the display of a number of predefined “apps”. These appear in the app list on your phone, but they're not really apps – they're quick links to trigger automations. When you tap on one of those apps, AutoWear sends the app name to Tasker as an event that you can act on. I'll come back to that in a future post.
So what can you do with Autowear?
My first use case was inspired by a question posted on [Reddit](https://www.reddit.com/r/GalaxyWatch/comments/px5hmt/is_there_any_automationmacro_app_that_can_connect/) asking whether there was a tool for WearOS that could change the phone volume when the watch was charging. I'd installed AutoWear at that point but hadn't really started playing with it, so I thought I'd see if it could be done. I liked the idea and it's one that I'd find useful myself.
I leave my phone on silent all the time, as I get notifications on my watch instead. There is, though, a window while the watch is charging when I might miss notifications. Obviously it would be a pain to have to switch the sound back on manually every time I charge the watch.
It's an easy one to automate with AutoWear, and it'll help to illustrate how AutoWear and Tasker interact.
First of all, a bit of terminology. Automations in Tasker are driven by profiles. Think of profiles as the triggers for running automations. Profiles then consist of tasks – the actions that are carried out when the trigger fires. You can also have conditions, and the logic can be as complex as you need it to be.
There are a number of different profile types. It's easy to see how an event or a specific time can be a trigger but the one we need here is state.
A state profile is active when its conditions are met. The tasks associated with a state run once when the state is first activated, and you can also have exit tasks that run when the state is no longer active. In other words, you can think of a state profile as consisting of two events – an entry event when the conditions are met and an exit event when they no longer hold.
So, for the watch charging automation, you start by defining a profile. Tap the plus icon to add a profile, select plugins, then the AutoWear plugin and then tap the pencil icon to select the state – in this case “plugged in.” Click the tick to accept and then go back to the profile screen.
Next, tap to add a task. You can choose to name the task, but it's not necessary for tasks that are connected directly to a profile. Click the plus button to add an action, select “audio”, then “sound mode”, and select the mode from the dropdown list.
This task will run when the profile is first activated – i.e. when the watch is placed on the charger.
Now you'll want to add an exit task. It's not immediately obvious, but to do so you long press on the existing task and select “Exit Task”. You can then create a task to reset the sound settings. The exit task will run when the watch is taken off of the charger.
The resulting profile makes the flow clear.
When you place your watch on the charger, you should see a notification on your phone to tell you that the profile is active:
That's one of the simplest examples of automation with AutoWear for Tasker and there is a lot more that you can do. Next time I'm going to look at how you can drive tasks from your watch…
[seanb](https://seanb.co.uk/author/seanb/) 23rd October 2021 0 comments [Automation](https://seanb.co.uk/tag/automation/), [mobile](https://seanb.co.uk/tag/mobile/), [Tasker](https://seanb.co.uk/tag/tasker/)
in [Mobile](https://seanb.co.uk/category/mobile/)
[Previous Post](https://seanb.co.uk/2021/10/galaxy-watch-4/)
[Next Post](https://seanb.co.uk/2021/11/wearos-custom-screens-with-tasker/)

##### 5 Comments

```
1. Michael 19th December 2021 Hi Sean, ist it also possible that the watch dies Tasks standalone? E.g. Turn on bluetooth every x minutes for y minutes? Greetings Michael
1. seanb Author 20th December 2021 Not as far as I know. The route to triggering actions on the watch is via the Tasker app on the phone – that's where the logic lives, and the watch app just sends events to the app and responds to actions. So you can automate some settings on the watch via triggers from the phone app, but turning off bluetooth wouldn't be one of them since the phone uses bluetooth to communicate with the watch.
1. RandomDude 30th December 2021 Hi Sean Very interesting writeup, thank you very much! Similar to Michael I was trying to set up a routine that only runs on the watch by triggering a command at given times which would then execute some settings that i defined in Autowear. I thought that as I could set up all the necessary parts straight in Autowear, i wouldn't need to go through tasker. Is that not the case then? I explained everything in detail in this reddit post for reference: https://www.reddit.com/r/tasker/comments/rrvsvg/how_to_use_commands_on_autowear/
1. seanb Author 31st December 2021 No, all of the logic is handled by Tasker on your phone. The watch can send events to the phone, and Tasker can respond to them, or Tasker can send commands to the watch in response to other events. For a time based event, the time would set a profile in Tasker, and the entry task for that profile could then send a command to the watch to change the settings.
1. Geofilho Ferreira Moraes 11th October 2022 how to create a task to activate power saving mode on watch4? Example: at 00:00 activate the clock's battery saver.
```

##### Related Posts

[A lesson in poor API design description](https://seanb.co.uk/2018/03/a-lesson-in-poor-api-design/)

###### [A lesson in poor API design](https://seanb.co.uk/2018/03/a-lesson-in-poor-api-design/)

4th March 2018 0
[Getting started part II description](https://seanb.co.uk/2017/12/getting-started-part-ii/)

###### [Getting started part II](https://seanb.co.uk/2017/12/getting-started-part-ii/)

10th December 2017 0
[The Home Assistant Android app description](https://seanb.co.uk/2020/10/the-home-assistant-android-app/)

###### [The Home Assistant Android app](https://seanb.co.uk/2020/10/the-home-assistant-android-app/)

17th October 2020 0
[What watts? description](https://seanb.co.uk/2020/05/what-watts/)

###### [What watts?](https://seanb.co.uk/2020/05/what-watts/)

10th May 2020 0

##### Recent Posts

###### [Hive's news](https://seanb.co.uk/2022/08/hives-news/)

7th August 2022

###### [Samsung's Strategy](https://seanb.co.uk/2022/03/samsungs-strategy/)

6th March 2022

###### [New website](https://seanb.co.uk/2022/02/new-website/)

13th February 2022

###### [Home automation upgrade woes](https://seanb.co.uk/2022/01/home-automation-upgrade-woes/)

30th January 2022

##### Categories

```
*  [Books](https://seanb.co.uk/category/books/) (7)
*  [Code](https://seanb.co.uk/category/code/) (1)
*  [Finance Project](https://seanb.co.uk/category/finance-project/) (11)
*  [Home Automation](https://seanb.co.uk/category/home-automation/) (84)
*  [Mobile](https://seanb.co.uk/category/mobile/) (31)
*  [Random Musings](https://seanb.co.uk/category/random-musings/) (51)
*  [Site news](https://seanb.co.uk/category/site-news/) (4)
*  [Uncategorised](https://seanb.co.uk/category/uncategorised/) (2)
*  [Web Design](https://seanb.co.uk/category/web-design/) (3)
```

##### Tags

[Alexa](https://seanb.co.uk/tag/alexa/) [Android](https://seanb.co.uk/tag/android/) [AppDaemon](https://seanb.co.uk/tag/appdaemon/) [Automation](https://seanb.co.uk/tag/automation/) [Cloud](https://seanb.co.uk/tag/cloud/) [django](https://seanb.co.uk/tag/django/) [ESB](https://seanb.co.uk/tag/esb/) [frigate](https://seanb.co.uk/tag/frigate/) [health](https://seanb.co.uk/tag/health/) [Home Assistant](https://seanb.co.uk/tag/home-assistant/) [Home Server](https://seanb.co.uk/tag/home-server/) [IFTTT](https://seanb.co.uk/tag/ifttt/) [Influx](https://seanb.co.uk/tag/influx/) [internet](https://seanb.co.uk/tag/internet/) [IoT](https://seanb.co.uk/tag/iot/) [mobile](https://seanb.co.uk/tag/mobile/) [Netatmo](https://seanb.co.uk/tag/netatmo/) [photography](https://seanb.co.uk/tag/photography/) [politics](https://seanb.co.uk/tag/politics/) [Programming](https://seanb.co.uk/tag/programming/) [Review](https://seanb.co.uk/tag/review/) [security cameras](https://seanb.co.uk/tag/security-cameras/) [SmartThings](https://seanb.co.uk/tag/smartthings/) [software](https://seanb.co.uk/tag/software/) [Tasker](https://seanb.co.uk/tag/tasker/) [Wordpress](https://seanb.co.uk/tag/wordpress/) [zato](https://seanb.co.uk/tag/zato/) [zoneminder](https://seanb.co.uk/tag/zoneminder/)
© Sean Buckley
Based on Realistic theme by [Themient](http://themient.com/)