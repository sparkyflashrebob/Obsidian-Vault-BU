---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

Idea Informer » Feedback 2.0
[About](https://idea.informer.com/static/about) [News](https://idea.informer.com/news/) [FAQ](https://idea.informer.com/faq/)
[Sign up](javascript: void(0);) [Sign in](javascript: void(0);)
30 place
**WatchMaker Bug Tracking** [All the ideas and discussions](https://watchmaker-bugs.idea.informer.com/)
27 votes [Vote](javascript: void(0);)

### Tap Actions Not Working on Wear OS 6 / One UI 8.0

**Bug Report: Tap Actions Not Working on Wear OS 6 / One UI 8.0**
**Environment:**
\* Device: Samsung Galaxy Watch 7
\* Wear OS Version: 6.0
\* One UI Version: 8.0
\* Watchmaker Version: 8.6.3
\* AutoWear: Latest (with accessibility service enabled)
**Problem:**
All tap actions are completely non-functional on Wear OS 6. This includes:
\* Built-in actions (vibrate, color\_switch\_select, widget\_weather)
\* App launching (w\_app:...)
\* Script execution (script:...)
\* Tasker integration (wm\_action)
Watch faces display correctly, and all other Watchmaker features work normally - only tap actions are broken.
**Technical Details:**
Through ADB analysis, I've identified that tap events are being intercepted by Wear OS 6's native Watch Face Framework (AndroidXWatchFaceEngine / DWF:GestureDetector) before reaching Watchmaker's tap handler. AutoWear's accessibility service is properly enabled but never receives the tap events.
**Steps to Reproduce:**
1. Install Watchmaker 8.6.3 on Galaxy Watch 7 (Wear OS 6)
1. Create or load any watch face with tap actions
1. Tap on elements with defined tap actions
1. Result: Nothing happens - tap actions do not execute
**Impact:**
Complete loss of interactive watch face functionality on Wear OS 6. No user workaround available.
**Additional Information Available:**
I have detailed ADB logs, package dumps, accessibility service status reports, and sample watch faces that demonstrate the issue. Please PM me if you need these files for debugging.
This appears to be a breaking change in Wear OS 6's Watch Face Framework that will affect all Galaxy Watch 7 users who update.
[lwoods2004](https://idea.informer.com/users/lwoods2004), 20.10.2025, 22:09
Idea status: **under consideration**

#### Comments

Alvaro Gonzalez, 03.11.2025, 10:50
Me too !!
In fact, phone app version is 8.6.3 (36863001) Premium
watch version is 8.6.3(3686304) Premium
Watch us Galaxy Watch7 (6G6V) SM-L310
Wear OS 6.0
OneUI 8.0 Watch
version. L310XXU1BYI4
Google Play version 25.42.32
System version 16
[Reply](javascript: ShowReply( '52460' );)
Alvaro Gonzalez, 08.11.2025, 13:59
Additionally, it's also eviden the LUA scripts don't work anymore.
All complications depending on them are stuck at the moment and status when you send the face from watchmaker to the watch.
[Reply](javascript: ShowReply( '52465' );)
Ric Kosiba, 05.12.2025, 19:00
Same here-- GW6 Classic. Just updated to OneUI 8.
Also, only one watch can be added to watchmaker at a time-- there is no "customize" feature for the watches and some of the elements in the watch are messed up (fonts, colors).
[Reply](javascript: ShowReply( '52475' );)
[Dankees](https://idea.informer.com/users/Dankees), 29.12.2025, 04:28
I have similar issues on my Galaxy Watch4 Classic.
I cannot change any features on the watch faces on my watch. I.must make the changes on my phone and then transfer.
Also, I cannot switch to recent and/or favorite watch faces on my watch. Only one watch face will appear.
[Reply](javascript: ShowReply( '52486' );)

#### [Leave a comment](javascript: void(0);)

Without registration
[Without registration](javascript: RegInlShb(1);)
Sign in
[Sign in](javascript: RegInlShb(2);)
Sign up
[Sign up](javascript: RegInlShb(3);)

| Name |  | Required |
| --- | --- | --- |
| e-mail |  | Required |

| Login |  |  |
| --- | --- | --- |
| Password |  | [Forgot your password?](javascript: void(0);) |
|  | [x] Remember me |  |
|  | [Sign in](javascript: SignIn( 'auth\_login\_err', 'auth\_login\_wait', \_v('auth\_login').value, \_v('auth\_pass').value, (\_v('auth\_remember\_me').checked ? 1 : 0), 'watchmaker-bugs' );) |  |

| Login |  | Use 3 to 18 characters, Latin characters or numbers | This login is not available This login is available |
| --- | --- | --- | --- |
| e-mail |  |  |  |
| Password |  | Use 3 to 18 characters, Latin characters or numbers |  |
| Re-type password |  |  |  |
|  | [x] Remember me |  |  |
|  | [Sign up](javascript: Reg('inline\_reg\_err', 'inline\_reg\_wait', \_v('reg\_login').value, \_v('reg\_email').value, \_v('reg\_pass').value, \_v('reg\_pass2').value, (\_v('reg\_remember\_me').checked ? 1 : 0), \_vs('#recaptcha-progreg [name=g-recaptcha-response]').value , 'watchmaker-bugs');) |  |  |
| Leave a comment |  |  |  |

```
*  [What is Idea Informer?](https://idea.informer.com/static/about)
*  [RSS feed](https://watchmaker-bugs.idea.informer.com/proj/rss?ia=143978)
```

Sign up

| Login |  | This login is not available This login is available |
| --- | --- | --- |
|  | Use 3 to 18 characters, Latin characters or numbers |  |
| E-mail |  |  |
| Password |  |  |
|  | Use 3 to 18 characters, Latin characters or numbers |  |
| Re-type password |  |  |
|  | [-] 1 Remember me |  |
|  | Register |  |

Already registered? [Sign in!](javascript: void(0);)
Sign in

| Login |  |  |
| --- | --- | --- |
| Password |  | [Forgot your password?](javascript: void(0);) |
|  | [-] 1 Remember me |  |
|  | Enter |  |
| [](javascript: openid.signin('openid');) [](javascript: openid.signin('google');) [](javascript: openid.signin('yandex');) [](javascript: openid.signin('vkontakte');) [](javascript: openid.signin('myopenid');) [](javascript: openid.signin('mail');) [](javascript: openid.signin('livejournal');) [](javascript: openid.signin('wordpress');) [](javascript: openid.signin('blogger');) [](javascript: openid.signin('flickr');) [](javascript: openid.signin('technorati');) [](javascript: openid.signin('verisign');) [](javascript: openid.signin('vidoop');) [](javascript: openid.signin('claimid');) |  |  |

First time here? [Register now. It's very easy!](javascript: void(0);) [OpenID](https://watchmaker-bugs.idea.informer.com/proj/?ia=143978) [Simple Sign In](https://watchmaker-bugs.idea.informer.com/proj/?ia=143978)
Sign in
Enter your email, and we'll send a link to reset your password.

|  |  |  |
| --- | --- | --- |
| E-mail |  |  |
|  |  |  |

Have you arrived here by mistake? [Sign in](javascript: void(0);) or [Register](javascript: void(0);)