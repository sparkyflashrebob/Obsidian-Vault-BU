---
tags:
  - notebooklm-import
notebook: "C_Graphics and other Desktop Media Apps"
category: "research"
---

###### Skip to main contentStack Exchange Network

Stack Exchange network consists of 183 Q&A communities including [Stack Overflow](https://stackoverflow.com), the largest, most trusted online community for developers to learn, share their knowledge, and build their careers.
[Visit Stack Exchange](https://stackoverflow.com)[Loading…](https://stackoverflow.com)

* [Blender](https://stackoverflow.com) [help](https://stackoverflow.com)[chat](https://stackoverflow.com)
* [Blender Meta](https://stackoverflow.com)

##### your communities

[Sign up](https://stackoverflow.com) or [log in](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor) to customize your list.

##### [more stack exchange communities](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor)

[company blog](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor)
[Log in](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor)
[Sign up](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor)
[Tags](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor) 
[Chat](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor) 
[Users](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor) 
[Companies](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor) 
Teams
Ask questions, find answers and collaborate at work with Stack Overflow Internal.
[Try Teams for free](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor)[Explore Teams](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor)
[Teams](https://blender.stackexchange.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070%2fcannot-render-video-in-video-editor) 
Ask questions, find answers and collaborate at work with Stack Overflow Internal. [Explore Teams](https://stackoverflow.co/teams/?utm_medium=referral&utm_source=blender-community&utm_campaign=side-bar&utm_content=explore-teams-compact)
**Teams**
Q&A for work
Connect and share knowledge within a single location that is structured and easy to search.

### [Learn more about Teams](https://stackoverflow.co/teams/?utm_medium=referral&utm_source=blender-community&utm_campaign=side-bar&utm_content=explore-teams-compact) [Cannot render video in video editor](https://stackoverflow.co/teams/?utm_medium=referral&utm_source=blender-community&utm_campaign=side-bar&utm_content=explore-teams-compact)

[Ask Question](https://stackoverflow.co/teams/?utm_medium=referral&utm_source=blender-community&utm_campaign=side-bar&utm_content=explore-teams-compact) Asked 5 years, 6 months ago Modified [5 years, 4 months ago](https://blender.stackexchange.com/?lastactivity)Viewed 4k times 0 $\begingroup$
I am completely new to Blender so I'm sorry if I'm not able to ask this question articulately or with enough detail. I am using Blender to create a short video of me playing drums. There is audio of me playing, audio of someone else playing piano part of the song, and video synced with that of me playing the part. I just want to export the final product so that I can share with band-mates.
I followed all the steps in this YouTube tutorial about exporting / rendering <https://www.youtube.com/watch?v=xxeP3We4k-A>. But when I click 'Render Animation', it takes me to a blank render screen and nothing happens (there is no % in the bottom of the video editor screen). I have clicked 'Render Animation' many times now, and have not seen the file appear in the destination (my Desktop).
My only guess is that it is something to do with me created a Proxy for the video clip that I exported into Blender, as I couldn't watch it back properly without major lag issues while editing.
I have attached two screenshots of what I see when I click of the video editor window, and of the blank 'Render Animation' screen.
Again, sorry if I have failed to describe this with enough detail.
enter image description here

* [rendering](https://i.sstatic.net/Qeh8g.png)
* [export](https://i.sstatic.net/Qeh8g.png)
* [video](https://i.sstatic.net/Qeh8g.png)
  [Share](https://i.sstatic.net/Qeh8g.png)[Improve this question](https://i.sstatic.net/Qeh8g.png) asked Apr 27, 2020 at 13:22 [drieux](https://blender.stackexchange.com/users/94882/drieux)1 1 1 silver badge 1 1 bronze badge $\endgroup$

#### [Add a comment](https://blender.stackexchange.com/users/94882/drieux) | 2 Answers 2

[Reset to default](https://blender.stackexchange.com#)  2 $\begingroup$
I, too, am somewhat new to Blender, and this one has gotten me several times. If I'm guessing correctly, the problem lies in the order in which sources for rendering are processed. In the picture below, I show that the render output panel is selected in the properties window (upper left highlight).
Way down at the bottom of that panel is a flippy triangle marked Post Processing. I think rendering first looks for something in the Compositing timeline *if the Compositing box is checked* . Then it looks for something in the Sequencer (video editing) window *if the Sequencer box is checked* . If not checked or nothing there, it renders the viewport camera that's active directly. So, uncheck the Compositor box, check the Sequencer box and let me know whether this now works. HTH
ShareImprove this answer answered Apr 28, 2020 at 11:54 [PhysicsTeacher](https://blender.stackexchange.com/users/79491/physicsteacher)51 5 5 bronze badges $\endgroup$
 [Add a comment](https://blender.stackexchange.com/users/79491/physicsteacher)  | 0 $\begingroup$
I had the same issue even though those exact same settings from the tutorial you linked worked on my previous videos.
As PhysicsTeacher recommended, in *Post Processing* click *Sequencer* instead of *Compositing* .
ShareImprove this answeredited Jun 18, 2020 at 23:13Duarte Farrajota Ramos♦ 62.3k 43 43 gold badges 140 140 silver badges 196 196 bronze badges answered Jun 18, 2020 at 17:22 [yolosweg](https://blender.stackexchange.com/users/99351/yolosweg)1 $\endgroup$

#### [Add a comment](https://blender.stackexchange.com/users/99351/yolosweg) | You must [log in](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070) to answer this question.

Start asking to get answers
Find the answer to your question by asking.
[Ask question](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)Explore related questions

* [rendering](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [export](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [video](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
  See similar questions with these tags.
* The Overflow Blog
* [AI code means more critical thinking, not less](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* Featured on Meta
* [Results of the October 2025 Community Asks Sprint: copy button for code...](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Chat room owners can now establish room guidelines](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)

###### Related

###### [5](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070) [Is it possible to render video sequence animations with network render?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)[1](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070) [no video in video sequence window](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)[3](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070) [Audio/Video out of sync in rendered video](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)[2](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070) [Why doesn't Blender render from video editor according to settings?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)[1](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070) [Audio in Video Editor but not in rendered output](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)[2](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070) [Rendering Animation Video](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)[0](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070) [Export a Video with Transparency (Video Editor)](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070) [Hot Network Questions](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)

* [What should I do if I know my son (10) repeatedly searched "Boy dress as a girl" online?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [What is this obfuscation method called?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Defining an Inner product on the vector space of coffee cups](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [conflicting reports using mdadm RAID Level 5](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Number of factors of a polynomial through Newton polygon argument](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* ["Since first I saw you fresh, which yet are green" in Shakespeare's sonnet 104](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Refering to a variable-indexed argument of newcommand](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Counting to infinity in distance vector routing problem](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Etymology of 鄭重 / 郑重?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [How are people using the Notebook Assistant and how useful is it?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [What World Was Subject to Angels?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Is "the" needed here: "the almost 50 species of bumble bees ..."?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Implementation of a balanced binary tree](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Land pattern for TDK CAA573 Megacap](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Who are the three superheroes shown with Robert in Dispatch's banner image?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Is not pulling a massless spring after hanging it equivalent to pulling it from both sides?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [HuffmannEncoder.java - computing prefix codes for arbitrary (generic) alphabets](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Recessed receptacle for 14-50 range outlet](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [How did Edom become Rome?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [How does one choose between two possible meanings of the following followup bid?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Semantic proof of lambda calculus consistency?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Does the SPLC's citation of a quote from Dan Stein in his 1997 interview with Tucker Carlson accurately reflect his full remarks from said interview?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Building a class D amplifier from scratch for a 20 watt 4 Ω speaker](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Artificial Intelligence solving Philosophy?](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)

### [more hot questions](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070) [Question feed](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070) Subscribe to RSS

###### [lang-py](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)

[Cookie Policy](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)

###### [Stack Exchange Network](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)

* [Technology](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Culture & recreation](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Life & arts](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Science](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Professional](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Business](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [API](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Data](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Blog](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Facebook](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Twitter](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [LinkedIn](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
* [Instagram](https://blender.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fblender.stackexchange.com%2fquestions%2f176070)
  Site design / logo © 2025 Stack Exchange Inc; user contributions licensed under [CC BY-SA](https://stackoverflow.com/help/licensing). rev 2025.11.13.36769