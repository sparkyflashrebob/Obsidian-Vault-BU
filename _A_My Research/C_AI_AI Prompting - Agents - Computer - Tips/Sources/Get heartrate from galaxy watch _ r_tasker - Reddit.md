---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

Get heartrate from galaxy watch : r/tasker
[Skip to main content](https://www.reddit.com/r/tasker/comments/1m3d33n/get_heartrate_from_galaxy_watch/#main-content) Get heartrate from galaxy watch : r/tasker
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
[Skip to Sign up](https://www.reddit.com/r/tasker/comments/1m3d33n/get_heartrate_from_galaxy_watch/#left-sidebar-container) [Skip to Right Sidebar](https://www.reddit.com/r/tasker/comments/1m3d33n/get_heartrate_from_galaxy_watch/#right-sidebar-container)
Back
[Go to tasker](https://www.reddit.com/r/tasker/)
[r/tasker](https://www.reddit.com/r/tasker/) â€¢ 1y ago
[RobAanDeTop](https://www.reddit.com/user/RobAanDeTop/)
Locked post
Stickied post
Archived post
\* Award this post
\* Report

### Get heartrate from galaxy watch

Hey!
For a project i'm working on i need my heartrate to be flashed every 2 minutes or so. I have no idea how i would access my heartrate, and everything i've tried so far hasnt been very successful. I have autowear installed on both my phone and my watch.
thanks in advance!
Read more
2 Â· 10

### Comments Section

[Sate\_Hen](https://www.reddit.com/user/Sate_Hen/)
â€¢ [1y ago](https://www.reddit.com/r/tasker/comments/1m3d33n/comment/n3vs5d2/)

```
Task: Test

A1: AutoWear App [
     Configuration: Execute Now: true
     Trigger Event: true
     Haptic Feedback: true
     Name: App
     Command: 
     Timeout (Seconds): 60
     Structure Output (JSON, etc): On ]

A2: Flash [
     Text: %awmessage
     Continue Task Immediately: On
     Dismiss On Click: On ]
```

3
[RobAanDeTop](https://www.reddit.com/user/RobAanDeTop/)
OP â€¢ [1y ago](https://www.reddit.com/r/tasker/comments/1m3d33n/comment/n3vveze/)
Thank you for the quick reply!
i've tried this and sadly it ends up just flashing "". Do happen to know how to fix this?
1
[Sate\_Hen](https://www.reddit.com/user/Sate_Hen/)
â€¢ [1y ago](https://www.reddit.com/r/tasker/comments/1m3d33n/comment/n3vvrdy/)
Does it work for any of the other commands like ?
2
4 more replies
[Continue this thread](https://www.reddit.com/r/tasker/comments/1m3d33n/comment/n3vvrdy/?force-legacy-sct=1)
[Continue this thread](https://www.reddit.com/r/tasker/comments/1m3d33n/comment/n3vveze/?force-legacy-sct=1)
[Continue this thread](https://www.reddit.com/r/tasker/comments/1m3d33n/comment/n3vs5d2/?force-legacy-sct=1)
[fishofchaos](https://www.reddit.com/user/fishofchaos/)
â€¢ [1y ago](https://www.reddit.com/r/tasker/comments/1m3d33n/comment/n3ysoeo/)
Has AutoWear got all the permissions and settings on your watch? For example, physical activity, and can you get heart rate on your watch without using Tasker? You might need long timeouts on the Tasker action. What is your watch...?
1
[fishofchaos](https://www.reddit.com/user/fishofchaos/)
â€¢ [1y ago](https://www.reddit.com/r/tasker/comments/1m3d33n/comment/n408mbv/)
Just tried it on my Galaxy Watch 6 Classic, and it worked but was quite unreliable. I used a two-minute timeout, and if errmsg was set or awmessage wasn't set, I repeated the action up to three times. So far, this has always worked, but it is messy.
1
[fishofchaos](https://www.reddit.com/user/fishofchaos/)
â€¢ [1y ago](https://www.reddit.com/r/tasker/comments/1m3d33n/comment/n40fnvv/)
Curiously, sometimes errmsg is set to timeout, but awmessage is set to a value which might be correct (it seems to be). Even though before the action, I deliberately cleared awmessage.
1
[Continue this thread](https://www.reddit.com/r/tasker/comments/1m3d33n/comment/n408mbv/?force-legacy-sct=1)
[Continue this thread](https://www.reddit.com/r/tasker/comments/1m3d33n/comment/n3ysoeo/?force-legacy-sct=1)

### People also ask about section

People also ask about
[Most useful Tasker profiles for beginners](https://www.reddit.com/answers/1c612ed0-b84d-4385-bcfc-d8e76ae4b709/?q=Most+useful+Tasker+profiles+for+beginners&source=PDP&ep=pdp_unit&relatedPostId=t3_1m3d33n)
[Creative ways to automate daily tasks](https://www.reddit.com/answers/e6d4d59a-2ca0-4615-b2b5-086aba403c4a/?q=Creative+ways+to+automate+daily+tasks&source=PDP&ep=pdp_unit&relatedPostId=t3_1m3d33n)
[Best plugins to enhance Tasker functionality](https://www.reddit.com/answers/4fd1c498-4791-4e8e-a584-15e559aeed27/?q=Best+plugins+to+enhance+Tasker+functionality&source=PDP&ep=pdp_unit&relatedPostId=t3_1m3d33n)
[Unique Tasker projects to inspire automation](https://www.reddit.com/answers/282cd674-89e3-4c12-b2ef-aebf3a9c54c6/?q=Unique+Tasker+projects+to+inspire+automation&source=PDP&ep=pdp_unit&relatedPostId=t3_1m3d33n)
[Tips for troubleshooting common Tasker issues](https://www.reddit.com/answers/c3dbfbf4-498a-4f06-9d47-d4cd48eaac24/?q=Tips+for+troubleshooting+common+Tasker+issues&source=PDP&ep=pdp_unit&relatedPostId=t3_1m3d33n)

### More posts you may like

Related posts
\* [First time Galaxy Watch owner. I'm impressed how accurate the blood pressure measuring is. - Series 9](https://www.reddit.com/r/GalaxyWatch/comments/1vhag0i/first_time_galaxy_watch_owner_im_impressed_how/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 5d ago [

##### First time Galaxy Watch owner. I'm impressed how accurate the blood pressure measuring is. - Series 9

](https://www.reddit.com/r/GalaxyWatch/comments/1vhag0i/first\_time\_galaxy\_watch\_owner\_im\_impressed\_how/) 548 upvotes Â· 90 comments
\* [It's official: Galaxy Watch Users can now measure Blood Pressure in the US](https://www.reddit.com/r/GalaxyWatch/comments/1s8ouwb/its_official_galaxy_watch_users_can_now_measure/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 4mo ago [

##### It's official: Galaxy Watch Users can now measure Blood Pressure in the US

](https://www.reddit.com/r/GalaxyWatch/comments/1s8ouwb/its\_official\_galaxy\_watch\_users\_can\_now\_measure/) 265 upvotes Â· 111 comments
\* [Watch recording HR on the table](https://www.reddit.com/r/GalaxyWatch/comments/1sxagfu/watch_recording_hr_on_the_table/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 4mo ago [

##### Watch recording HR on the table

](https://www.reddit.com/r/GalaxyWatch/comments/1sxagfu/watch\_recording\_hr\_on\_the\_table/) 114 upvotes Â· 30 comments
\* [Heart Rate Sensor Test - Galaxy Watch Ultra 2025 vs Pixel Watch 3.](https://www.reddit.com/r/GalaxyWatch/comments/1ncm3bv/heart_rate_sensor_test_galaxy_watch_ultra_2025_vs/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 1y ago [

##### Heart Rate Sensor Test - Galaxy Watch Ultra 2025 vs Pixel Watch 3.

](https://www.reddit.com/r/GalaxyWatch/comments/1ncm3bv/heart\_rate\_sensor\_test\_galaxy\_watch\_ultra\_2025\_vs/) 3 51 upvotes Â· 36 comments
\* [Samsung enables blood pressure monitoring for US Customers.](https://www.reddit.com/r/GalaxyWatch/comments/1sgje1u/samsung_enables_blood_pressure_monitoring_for_us/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 4mo ago [

##### Samsung enables blood pressure monitoring for US Customers.

](https://www.reddit.com/r/GalaxyWatch/comments/1sgje1u/samsung\_enables\_blood\_pressure\_monitoring\_for\_us/) cnet 106 upvotes Â· 68 comments
\* [Heart rate monitoring freezes on Galaxy Watch 8](https://www.reddit.com/r/GalaxyWatch/comments/1qea1z8/heart_rate_monitoring_freezes_on_galaxy_watch_8/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 7mo ago [

##### Heart rate monitoring freezes on Galaxy Watch 8

](https://www.reddit.com/r/GalaxyWatch/comments/1qea1z8/heart\_rate\_monitoring\_freezes\_on\_galaxy\_watch\_8/) 8 upvotes Â· 2 comments
\* [Has anyone tried checking someone else's blood pressure with a device calibrated to your own arm? Does it still give accurate measurements?](https://www.reddit.com/r/GalaxyWatch/comments/1qefxau/has_anyone_tried_checking_someone_elses_blood/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 7mo ago [

##### Has anyone tried checking someone else's blood pressure with a device calibrated to your own arm? Does it still give accurate measurements?

](https://www.reddit.com/r/GalaxyWatch/comments/1qefxau/has\_anyone\_tried\_checking\_someone\_elses\_blood/) 32 upvotes Â· 36 comments
\* [Resting Heart Rate Calculation Is Actually Incorrect.](https://www.reddit.com/r/GalaxyWatch/comments/1rchvxd/resting_heart_rate_calculation_is_actually/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 6mo ago [

##### Resting Heart Rate Calculation Is Actually Incorrect.

](https://www.reddit.com/r/GalaxyWatch/comments/1rchvxd/resting\_heart\_rate\_calculation\_is\_actually/) 3 upvotes Â· 13 comments
\* [Blood Pressure feature](https://www.reddit.com/r/GalaxyWatch/comments/1suhui3/blood_pressure_feature/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 4mo ago [

##### Blood Pressure feature

](https://www.reddit.com/r/GalaxyWatch/comments/1suhui3/blood\_pressure\_feature/) 2 28 upvotes Â· 78 comments
\* [Question for Sport Person. How well are you satisfied with your Galaxy Watch Heart Rate Data?](https://www.reddit.com/r/GalaxyWatch/comments/1ntcxcc/question_for_sport_person_how_well_are_you/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 1y ago [

##### Question for Sport Person. How well are you satisfied with your Galaxy Watch Heart Rate Data?

](https://www.reddit.com/r/GalaxyWatch/comments/1ntcxcc/question\_for\_sport\_person\_how\_well\_are\_you/) 3 12 upvotes Â· 34 comments
\* [Just got my LightPhone III!](https://www.reddit.com/r/LightPhone/comments/1m2dhm6/just_got_my_lightphone_iii/) [r/LightPhone](https://www.reddit.com/r/LightPhone/) â€¢ 1y ago [

##### Just got my LightPhone III!

](https://www.reddit.com/r/LightPhone/comments/1m2dhm6/just\_got\_my\_lightphone\_iii/) 18 upvotes Â· 15 comments
\* [Blood Pressure Review on Galaxy Watch 7](https://www.reddit.com/r/GalaxyWatch/comments/1pxjtgr/blood_pressure_review_on_galaxy_watch_7/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 8mo ago [

##### Blood Pressure Review on Galaxy Watch 7

](https://www.reddit.com/r/GalaxyWatch/comments/1pxjtgr/blood\_pressure\_review\_on\_galaxy\_watch\_7/) 4 upvotes Â· 8 comments
\* [Today Blood Pressure is now available to ALL Galaxy watch and phone users in US](https://www.reddit.com/r/GalaxyWatch/comments/1shcpx5/today_blood_pressure_is_now_available_to_all/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 4mo ago [

##### Today Blood Pressure is now available to ALL Galaxy watch and phone users in US

](https://www.reddit.com/r/GalaxyWatch/comments/1shcpx5/today\_blood\_pressure\_is\_now\_available\_to\_all/) 55 upvotes Â· 34 comments
\* [What do you do with health data from your galaxy watch?](https://www.reddit.com/r/GalaxyWatch/comments/1tfx04z/what_do_you_do_with_health_data_from_your_galaxy/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 3mo ago [

##### What do you do with health data from your galaxy watch?

](https://www.reddit.com/r/GalaxyWatch/comments/1tfx04z/what\_do\_you\_do\_with\_health\_data\_from\_your\_galaxy/) 12 upvotes Â· 15 comments
\* [Heart Rate Monitor on Watch Ultra sucks](https://www.reddit.com/r/GalaxyWatch/comments/1touegw/heart_rate_monitor_on_watch_ultra_sucks/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 3mo ago [

##### Heart Rate Monitor on Watch Ultra sucks

](https://www.reddit.com/r/GalaxyWatch/comments/1touegw/heart\_rate\_monitor\_on\_watch\_ultra\_sucks/) 12 comments
\* [Has anyone found their energy score to be a good indicator of how they actually feel?](https://www.reddit.com/r/GalaxyWatch/comments/1qbqfv8/has_anyone_found_their_energy_score_to_be_a_good/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 7mo ago [

##### Has anyone found their energy score to be a good indicator of how they actually feel?

](https://www.reddit.com/r/GalaxyWatch/comments/1qbqfv8/has\_anyone\_found\_their\_energy\_score\_to\_be\_a\_good/) 5 upvotes Â· 12 comments
\* [Why does Samsung insist on not letting us use the Galaxy Watch with a heart rate monitor band?](https://www.reddit.com/r/GalaxyWatch/comments/1sn1b7w/why_does_samsung_insist_on_not_letting_us_use_the/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 4mo ago [

##### Why does Samsung insist on not letting us use the Galaxy Watch with a heart rate monitor band?

](https://www.reddit.com/r/GalaxyWatch/comments/1sn1b7w/why\_does\_samsung\_insist\_on\_not\_letting\_us\_use\_the/) 2 upvotes Â· 9 comments
\* [What version of Samsung health monitor has the blood pressure?](https://www.reddit.com/r/GalaxyWatch/comments/1sdl2l0/what_version_of_samsung_health_monitor_has_the/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 4mo ago [

##### What version of Samsung health monitor has the blood pressure?

](https://www.reddit.com/r/GalaxyWatch/comments/1sdl2l0/what\_version\_of\_samsung\_health\_monitor\_has\_the/) 12 upvotes Â· 39 comments
\* [So, what's the point of having continuous heart rate monitoring if the graph is by hour?](https://www.reddit.com/r/GalaxyWatch/comments/1q0mfsx/so_whats_the_point_of_having_continuous_heart/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 7mo ago [

##### So, what's the point of having continuous heart rate monitoring if the graph is by hour?

](https://www.reddit.com/r/GalaxyWatch/comments/1q0mfsx/so\_whats\_the\_point\_of\_having\_continuous\_heart/) 7 upvotes Â· 10 comments
\* [I've been using the Moto G Stylus 2025 for a week. AMA!](https://www.reddit.com/r/motorola/comments/1l4comg/ive_been_using_the_moto_g_stylus_2025_for_a_week/) [r/motorola](https://www.reddit.com/r/motorola/) â€¢ 1y ago [

##### I've been using the Moto G Stylus 2025 for a week. AMA!

](https://www.reddit.com/r/motorola/comments/1l4comg/ive\_been\_using\_the\_moto\_g\_stylus\_2025\_for\_a\_week/) 21 upvotes Â· 8 comments
\* [\[US Model\] we finally getting blood pressure monitor](https://www.reddit.com/r/GalaxyWatch/comments/1vh8i4r/us_model_we_finally_getting_blood_pressure_monitor/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 5d ago [

##### [US Model] we finally getting blood pressure monitor

](https://www.reddit.com/r/GalaxyWatch/comments/1vh8i4r/us\_model\_we\_finally\_getting\_blood\_pressure\_monitor/) 2 2 upvotes Â· 42 comments
\* [Blood pressure monitor in the US. Anyone actually get it?](https://www.reddit.com/r/GalaxyWatch/comments/1scck9r/blood_pressure_monitor_in_the_us_anyone_actually/) [r/GalaxyWatch](https://www.reddit.com/r/GalaxyWatch/) â€¢ 4mo ago [

##### Blood pressure monitor in the US. Anyone actually get it?

](https://www.reddit.com/r/GalaxyWatch/comments/1scck9r/blood\_pressure\_monitor\_in\_the\_us\_anyone\_actually/) 17 upvotes Â· 80 comments
\* [Best smartwatch for cardiac monitoring?](https://www.reddit.com/r/smartwatch/comments/1v0vmkr/best_smartwatch_for_cardiac_monitoring/) [r/smartwatch](https://www.reddit.com/r/smartwatch/) â€¢ 23d ago [

##### Best smartwatch for cardiac monitoring?

](https://www.reddit.com/r/smartwatch/comments/1v0vmkr/best\_smartwatch\_for\_cardiac\_monitoring/) 6 upvotes Â· 16 comments
\* [Is there any watch that can help track heart health for a heart attack survivor?](https://www.reddit.com/r/smartwatch/comments/1t3axjs/is_there_any_watch_that_can_help_track_heart/) [r/smartwatch](https://www.reddit.com/r/smartwatch/) â€¢ 3mo ago [

##### Is there any watch that can help track heart health for a heart attack survivor?

](https://www.reddit.com/r/smartwatch/comments/1t3axjs/is\_there\_any\_watch\_that\_can\_help\_track\_heart/) 6 upvotes Â· 8 comments
\* [Something to track heart rate that doesn't break the bank, but will last more than a few months?](https://www.reddit.com/r/smartwatch/comments/1u8adr4/something_to_track_heart_rate_that_doesnt_break/) [r/smartwatch](https://www.reddit.com/r/smartwatch/) â€¢ 2mo ago [

##### Something to track heart rate that doesn't break the bank, but will last more than a few months?

](https://www.reddit.com/r/smartwatch/comments/1u8adr4/something\_to\_track\_heart\_rate\_that\_doesnt\_break/) 5 upvotes Â· 17 comments

#### View Post in

See more See fewer
[EspaÃ±ol (LatinoamÃ©rica)](https://www.reddit.com/r/tasker/comments/1m3d33n/get_heartrate_from_galaxy_watch/?tl=es-419)

### Community Info Section

[r/tasker](https://www.reddit.com/r/tasker/)
Join
Tasker: Total Automation for Android
Public
Anyone can view, post, and comment to this community

#### Top Posts

```
*  [Reddit reReddit: Top posts of July 18, 2025](https://www.reddit.com/posts/2025/july-18-1/global/)
*  [Reddit reReddit: Top posts of July 2025](https://www.reddit.com/posts/2025/july/global/)
*  [Reddit reReddit: Top posts of 2025](https://www.reddit.com/posts/2025/global/)
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
0cAFcWeA7dzPtzJt8UXbepyF1ObX2OWrM9pyznFs00kIpoXragBsZpFR6m6vOV1zyPrfqWFRTV3cTXoPG\_5ej8cpm28ffXfPyzUXNQ\_BMMFEGYqChqCOtH\_eTCTrIRmETrSWcCkSUabvig\_IR8PXpKtlXzJDKGfc7NvZniZ4PVlNk6lGmb4hxiMKQw8rUc9IXL0QQ7izKMOIGLkQ4GwpCkFKtDhlVB7NxTH0lLQgFz325iVG0LEDaCWd3YdoskyJowPa9KCzNJt8GKmtfiQ2Ln5NeiISSnqOc4ccdgKlp3SyuW-yvKb3oY7W\_0U9PIO6VWpV6F\_Vv0vZ4CV0it\_p7xKPn\_0XypEoG6sGk5AeERVyL4WbatQzo3\_NLvmaiuF8nytLUuWf7MK1diVJWC9hSTAmiH7ZmVgLfIRRiGP6WAfPP5OGLpoK2JIwF1nNKFbqauJKxXIObnl1JQ-6kUtXfv4xCAOTG4NCNIFCJHavbusVh37sR6zVP\_maGEAOJKuu05a0gHteoNMWJZXk7cZPTLPi4LEDj\_5qCoey1aFGLz\_Kc0MOq5A4-y7FBBud2-IuWB1gRRPpZ1qwhl-8lTqCdSftsq1fUQUSUKykClt94iDM7tXhXdS58TUtFb8rGdntXUOaYuzsCsIruxwQKF47Ty72U6ILxyraTOl620pj-KM9gLt2coK-Y7jnbHegngwaphQR2AFv7wUt2dREH4LkzJBgi10yvye-yaITxF4cjCMRsjSvChKPA5hT8Y71D35ajK28Ywzr7WGEpiAsvS\_hE8Kj3MPrWqYxYBnbWF5ZUQFegJ6OShZ3gcSisOVx2M3soU4ZgWDH2-9Xlk9aDqraLFXKEVVoJfUDPkAig3h\_0ELyWy\_qdnR9SQCtDB2tXgll3AOdcJZWXjuqFRvc6VqzHQm08jn4GPTWPrOmRnxQx8vvqEMcbnvZL3Q5C-hzJ\_\_1An5q\_qiOkpFM9F7pQOJu2-vHcv\_5IwEZG7tqSkx9GeQk7PWFCvIv8Q-JQS9jKIVFlbyPaogPaXNf0uf\_tEduNM9kaBiL7mQzOu6OKiMdVe-DjI7D5\_1qGt5HwbmMLjtEGaH-Blp9IhmKaQ7BOIdpt8wd01yECc0Tp\_-Vo281ff4blI8epS3Ut6GDJD\_MoiHuiSsHwlG-vwiVFSTGUFJmh5joKTgAdPGvocLAIUO-gybn\_z2G1vje50LegVb8FHTawFTm\_IrJrIYFW0rQfFnSWEgAuPlzqoitw2RMA4gMhtv-Ugz8R0rh1MR18KVetFPSKI73wx9IlV3TQwLkk903SmClU9bjv8ODt-zktibT2ERKfWOuXKP\_xqMbn35OIrTW0paV0rLwy6pu\_sw\_ovdbmFqUs3kI-sak7gZolB0qEV4vODP9pU50-iD13\_8iSG85DwHKghui4rU7dB89kK-ikBN90Lb8SA9ERn\_wuUm1zZ2qKWHe8SHHIRB9SfVRv2iF9m4M6iwzBy5YVpBjCV\_-OSJpbegrwf4vbG1E-93w8MzFSZsaeVUiQBNA4N\_lAqtk42VqinM0iRzdDfyuLT2E5jVDuif\_84AD9RuIrsqv3aQVWxunIyGFzmqYFxup-K-P\_Ol2iXNDsVAzNZF7CBRyJDo4gRF55wo8lg\_VlX3NGk-iQs6fGX7U\_m6mkckwh\_0Ww8b4wKgIczLupJOwVh1aKY9mejOJ1V8SFGMHgtxcrbNcjkpIEcb2DUB20eAmQp9Wmz9QMZqVW1xQw979yPt0cfV11BTxVYgStEBbJrxnVa\_ii7jjjRmq81kx8dGddHcZv2JBPhicbCo6cyWdlMouUNVJ0P1I17MJQ233bnXp7pn6171aVNeTE8leKpcGYdzTDmD6zd4br\_jInK9dPrJUGQi44ZvxgebUQ3EM6DOUiES3PZ1Qj\_uryaCyjdqEHW6\_bMpWgmBpYcf1oKdocSISnfLd3W8LZZpQRkV7bwM5K3aECiZjbsUB6ZtCA8rkyOb7OJVi5eWDXeYFZ8BTkY-LCz-FZo8h\_L1OBntITm57oX77vo5Mszinfq53ixmmgJuFIWTeAptxIQCB-lBQvwbqWGDAKMlTS\_plH017Hbk0VatBG8T59QGff8pYi85yyp\_ocal\_8pfnPiS\_Png1kLWLmji6fTHtBtHF2-ahmk8czELrA-51rNjJ4oK5vdNKnpVZ8pITkOQXK5BbHEn8BT9MShcCkA2nl0t1o6F7KlASb8Ozbmjj9DlmCzC30