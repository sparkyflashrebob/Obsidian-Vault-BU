---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

Tasker: Android System Power Management

#### Android System Power Management

Starting with Android 5.0, many devices will act aggressively to try and save system battery power. Unless certain steps are taken, Tasker may not function as expected, either because Android is not sending it the needed signals in order to save power or because Android is even killing Tasker.
A commonly noticed symptom is that profiles with Time contexts don't activate or deactivate at the expected time.

##### Tasker Run In Foreground Preference

Make sure that Menu / Prefs / Monitor / General / Run In Foreground is **checked** .

##### Tasker Reliable Alarms Preference (Android 5.0+)

In Menu / Prefs / Monitor / General / Use Reliable Alarms , make sure **When Off** or **Always** is selected.
If **Never** is selected, Android may group alarms together so they go off too late. On some devices, Android may even kill Tasker at times if **Never** is selected.

##### Android Battery Optimization Setting

If you have reliability problems, Tasker might need to be whitelisted so that it is not *battery-optimized* by Android.

###### Vanilla Android Devices (Android 6.0+)

The location of the setting may vary per device, but a common method is to launch the *Android Settings* app, select **Apps** , click the cog icon top-right, then **Battery optimization** . Click **All apps** , then Tasker, then **Don't optimize** .
On a rooted device, it may be possible to change the battery optimiation parameters depending on the functionality you need from Tasker. An example app for this purpose is [Naptime](https://play.google.com/store/apps/details?id=com.franco.doze).

###### Samsung (Android 5.1.1+)

Some Samsung devices have a *Smart Manager* app. Launch the app, press the battery quarter of the screen, under **App optimisation** press **DETAIL** where you can adjust the settings for each app. It's advisable to disable this for Tasker if you are having reliablity problems.

###### MIUI 7

Launch Settings app, select Additional settings -> Battery & performance -> Manage apps battery usage -> OFF