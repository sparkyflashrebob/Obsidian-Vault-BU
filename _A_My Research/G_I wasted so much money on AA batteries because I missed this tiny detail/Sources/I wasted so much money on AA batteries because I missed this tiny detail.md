---
tags:
  - notebooklm-import
notebook: "G_I wasted so much money on AA batteries because I missed this tiny detail"
category: "research"
---

Sign in now

* Windows
* Android
* iPhone
* Tech Explained
* Security
* Productivity
* Creative
* EntertainmentStreaming
* Internet
  Home
  News
  Free Cheat Sheets
* Sign in
* Newsletter

### Follow Followed [Threads 23](https://www.makeuseof.com#threads) More Action Summary Sign in now I wasted so much money on AA batteries because I missed this tiny detail

Amir Bohlooli / MUO By [Amir Bohlooli](https://www.makeuseof.com/author/amir-bohlooli/)Published 1 day ago Amir is the Segment Lead for Productivity and Creative at MUO. He's a PharmD student who's interested in clinical outcomes and Pharmacoeconomics. He loves looking at numbers and spreadsheets. His passion for data manipulation sparked during his early academic years, back when he used spreadsheets for lab reports.
Inspired by his father's hobbies, Amir developed a knack for DIY projects and built his first quadcopter in high school. At 18, he began writing about 3D printing, and now contributes to MUO where he writes and edits productivity, spreadsheets, photography, music, and more.
Amir also enjoys creating music, although its categorization as such remains open to interpretation. In addition to his academic pursuits, Amir is an avid gamer, car enthusiast, and proud owner of a 1993 Mitsubishi. Sign in to your MUO account Summary follow Follow followed Followed  [Thread 23](https://www.makeuseof.com#threads)  Here is a fact-based summary of the story contents: Try something different:
I pulled my camera out last week to shoot a few photos, and I instantly remembered why I don’t like using this thing: it takes AA batteries. My wireless mouse takes one AA. I have three Xbox controllers that all take AAs. Over time, constantly swapping dead batteries and watching devices chew through them has given me an actual “ick” for anything that relies on AA cells.
But, as it turns out, there’s a lot more going on with AA batteries than I ever assumed. I’d ignored the text and markings on the packaging for years, but when I finally paid attention, everything clicked — and all my battery-related problems basically solved themselves. Consider this my attempt at redemption, so no one else repeats the same mistakes I did.

#### Why did I ignore the battery markings for so long?

##### Please let me explain

Credit: Amir Bohlooli / MUO *Heavy Duty. Super Heavy Duty. Extra Heavy Duty. Pro Max Heavy Duty. Titanium. Long lasting. Lasts 10 years. “The last battery pack you ever buy.”* You’ve seen these. So have I. I dismissed them all as empty marketing fluff and assumed none of it meant anything. To be fair, I was right — those phrases do not mean anything. But their presence on the packaging was distracting enough that I ignored the text that *does* matter: the codes that tell you the chemistry and how the battery will actually perform.
I’d like to believe I’m not the only one who fell for this. Most people probably treat AA batteries as a single category (I say to myself). You grab whatever’s on the shelf and assume the only differences are “how long it lasts” or “whether it’s rechargeable.” That assumption is wrong. The markings on AA batteries matter — and once you understand them, the entire category stops feeling random.

#### AA batteries aren’t all the same

##### Not every piece of text is an advertisement

Credit: Amir Bohlooli / MUO Let me waste a few more seconds of your time, because this story is exactly what made the whole thing click for me. If you find it boring, scroll ahead — the AA battery guide table is waiting for you. But I'll make the story worth your time.
My camera takes four AA batteries. I used to have a set of rechargeable ones for it, but I hadn’t used the camera in so long that I couldn’t find them. So I bought a pack of cheap non-rechargeable AAs. The camera lasted for about ten shots, then shut off instantly. No low-battery warning. Nothing.
Surely, despite these batteries both being cheap non-rechargable AAs, there's a difference between LR6 and R6? What do they mean?
So I put in another pack of batteries, and the camera didn't even turn on. I could hear tiny relays clicking inside when I flipped the switch, but nothing else. No LCD, no beep, nothing. What happened? Did this guy sell me discharged batteries? Is this a scam? I grabbed my multimeter and it showed 1.5V. What’s going on?
Credit: Amir Bohlooli / MUO I swallowed the questions and instead I went scorching all my shelves and bags looking for my rechargables. I found a whole lot of AA batteries, and to find out if they're rechargable or not, I had to read what's on them. That's when I noticed codes like *LR6-BP4* or *R6P AA UM-3* . Surely, despite these batteries both being cheap non-rechargable AAs, there's a difference between *LR6* and *R6* ? What do they mean?

#### What the AA battery codes actually mean

##### Translating LR6, R6, HR6, and friends

Let’s decode something like *R6P AA UM-3* :
Code
Meaning
R
Round cell (cylindrical)
6
Size code for AA
P
“Power” or general-purpose zinc-carbon (the cheap stuff)
AA
Retail name (just repeats the size)
UM-3
Japanese JIS code for AA (again, the size)
Most of this is redundant. But the chemistry code is the key. And once you know the other codes too, you realize that “AA battery” is not one product. There are several chemistries, and they behave very differently.
Code
Chemistry
Internal resistance
Open voltage
High-current performance
Rechargable
R6
Zinc-Carbon
250–400 mΩ
1.5V
🟥Terrible
❌
LR6
Alkaline
80–150 mΩ
1.5V
🟧OK-ish
❌
HR6
NiMH Rechargeable
20–30 mΩ
1.3V
🟦Excellent
✅
FR6
Lithium (Li-FeS₂)
60–90 mΩ, very stable
1.8V
🟦Excellent
❌
KR6
NiCd Rechargeable
25–40 mΩ
1.3V
🟦Excellent
✅

#### Don’t use R6 batteries for your camera

##### You're throwing away money

Credit: Amir Bohlooli / MUO There you have it — AA batteries, demystified. But if you *really* want to put this topic to bed (like I did), we need to talk about why you shouldn’t use **R6** or **LR6** batteries in a camera or any other high-current device. Before I understood any of this, I assumed the only difference was capacity. Cheap batteries die faster, expensive ones last longer. Same voltage, so the camera should work either way. I was wrong.
High-drain devices like cameras, flashes, and game controllers, pull a lot of current. Batteries have internal resistance, and when you pull high current, voltage drops. This is exactly what my camera was doing. It would turn on with alkaline **LR6** cells, but the moment I used autofocus or flash, it would instantly shut off. And the batteries weren’t “dead” — they still worked fine in a mouse. The load just pulled the voltage below the camera’s minimum threshold.
Here’s an example at 5 amps (flash recharge spike):
Code
Open voltage
Internal resistance
Load voltage @ 5A
Load state
R6
1.5V
~300 mΩ
1.50 – (5×0.30) = **0.00 V**
🟥Full collapse
LR6
1.5V
~120 mΩ
1.50 – (5×0.12) = **0.90 V**
🟧Shutdown territory
KR6
1.3V
~35 mΩ
1.30 – (5×0.035)= **1.12 V**
🟨Stable-ish
HR6
1.3V
~25 mΩ
1.30 – (5×0.025)= **1.17 V**
🟩Stable
FR6
1.8V
~80 mΩ
1.80 – (5×0.08) = **1.40 V**
🟦Very stable
So yes, you save nothing by buying cheaper batteries. The device simply won’t function properly. This is why cameras love NiMH ( **HR6** ) and lithium ( **FR6** ). It's also why **R6** zinc-carbon shouldn’t be used for anything more demanding than a wall clock.
All of these standards and codes also aply for AAA batteries.

#### How to tell if you’ve got the right batteries

##### Ignore "Heavy Duty" and read the tiny code instead

Credit: Amir Bohlooli / MUO The next time you need AA batteries, consider the device you want to use it for. The degree of *duty* that's written on the batteries (like *Heavy duty* ) is arbitrary. Just look at the codes and numbers.
Code
Use case
R6
Just avoid them.They’re barely cheaper than LR6 and perform terribly.
LR6
For remotes, clocks, and low-drain devices.
HR6
For anything high-drain (cameras, controllers, flashes, toys).
FR6
For the best non-rechargeable performance.
KR6
Only if you own ancient equipment.
Some brands include icons to hint at intended use. A clock usually means zinc-carbon ( **R6** ). A flashlight means alkaline ( **LR6** ). A camera icon could mean lithium ( **FR6** ). These icons aren’t standardized, but they can help you spot the obvious garbage.
For cameras or anything that draws a lot of current, NiMH and FR6 (lithium) AAs are the right choice. NiMH has the bonus of being rechargeable, which makes it the best long-term deal. The only catch is you’ll need a proper charger if you don’t already have one. I use a Camelion 4-slot charger and a Sony 2-slot charger — both handle AA and AAA without issues.

###### Sony Cycle Energy NiMH Compact Charger

**Compatible Batteries** AA, AAA **Brand** Sony **Battery capacity** 1000 mAh **Battery Cell Type** NiMH
$64 at ElectroeshopIf you're going to use a charger, read the text on your charger. Unless it’s a proper smart charger (with temperature sensing, delta-V detection, or safe trickle at full), charging NiMH cells is vulnerable to the same [phone charging myths](https://www.makeuseof.com/battery-myths-ruining-phone-battery-life/) we’ve finally outgrown with phones. Leaving them overnight in a dumb charger will overheat them, degrade them, or even melt the casing.
FR6 lithium batteries are excellent for cameras. They offer high capacity and very low internal resistance, which means they can handle heavy bursts of current without choking. They’re not rechargeable, but a single pack will last a long time in most cameras.

###### Energizer Ultimate Lithium AA Batteries

**Battery Type(s)** Lithium **Brand** Energizer **Capacity** 3000 mAh [See at Amazon](https://www.amazon.com/Energizer-Ultimate-Lithium-Batteries-Pack/dp/B0023T8OUY/?tag=makeusw-20&ascsubtag=UUmuoUeUpU2038868&asc_refurl=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F&asc_campaign=Feed)A quick warning when shopping for lithium AAs: always check the voltage. Most lithium cells on the market are 3.7V, not 1.5V. Those 3.7V cells use a completely different chemistry, and putting them in your camera is a spectacularly bad idea. You want 1.5V lithium primaries like the Energizer Ultimate Lithium series. And remember: if it’s rechargeable, it’s the wrong lithium chemistry for AA devices. Only the non-rechargeable lithium AAs are safe replacements.

#### What about USB-rechargeable AA batteries?

##### They're cute, but not practical

Image by Amir Bohlooli. NAN.
On some shelves, you’ll see USB-C rechargeable AAs that advertise 1.5V lithium 2200mAh. You might think: wait, aren’t lithium AAs supposed to be 1.8V and not rechargeable? Correct. And these are not actually 1.5V lithium cells.
Inside these USB-rechargable AAs, there's a tiny 3.7 Li-ion cell, *plus* a buck converter to regulate output to 1.5V, *plus* a charging circuit. So you're basically buying a small battery + lots of circuitry. [The battery capacity (mAh)](https://www.makeuseof.com/what-is-battery-mah/) is never as high as advertised (because 2200mAh at 1.5V ≠ 2200mAh at 3.7V), and you’re paying for complexity, not performance. It's a cute idea, but a bad deal.
I went with [Panasonic Eneloop HR6 (NiMH)](https://www.amazon.com/Eneloop-8-Battery-Rechargeable-Batteries-Controllers/dp/B00JHKSN5I/?tag=makeusw-20&ascsubtag=UUmuoUeUpU2038868&asc_refurl=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F&asc_campaign=Feed) cells in the end, and they’ve been rock-solid — every photo you see here was taken on my camera without it collapsing mid-shot.

##### I changed my mind about AA batteries

I wasted so many R6 AAs on my camera that I don’t even want to think about it. But those days are over. I’m fully on board with AA-powered devices again.
I used to be annoyed that Microsoft wouldn't just stick a a proprietary Li-Po battery in its controllers, like Sony does. But now, no more. When a proprietary battery in a device dies, you’re stuck. When a device uses AAs, you just swap cells and move on. I proudly confess that AA batteries weren't the problem. I was.

* **Love MUO? We have so much more.** [image/svg+xml Follow us on Google Discover!](https://www.amazon.com/Eneloop-8-Battery-Rechargeable-Batteries-Controllers/dp/B00JHKSN5I/?tag=makeusw-20&ascsubtag=UUmuoUeUpU2038868&asc_refurl=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F&asc_campaign=Feed) [Technology Explained](https://www.amazon.com/Eneloop-8-Battery-Rechargeable-Batteries-Controllers/dp/B00JHKSN5I/?tag=makeusw-20&ascsubtag=UUmuoUeUpU2038868&asc_refurl=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F&asc_campaign=Feed)
* [Batteries](https://www.amazon.com/Eneloop-8-Battery-Rechargeable-Batteries-Controllers/dp/B00JHKSN5I/?tag=makeusw-20&ascsubtag=UUmuoUeUpU2038868&asc_refurl=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F&asc_campaign=Feed)
* [Hardware Tips](https://www.amazon.com/Eneloop-8-Battery-Rechargeable-Batteries-Controllers/dp/B00JHKSN5I/?tag=makeusw-20&ascsubtag=UUmuoUeUpU2038868&asc_refurl=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F&asc_campaign=Feed) 
  Follow Followed Share [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F%2F&src=sdkpreparse) [X](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F%2F&src=sdkpreparse) [WhatsApp](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F%2F&src=sdkpreparse) [Threads](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F%2F&src=sdkpreparse) [Bluesky](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F%2F&src=sdkpreparse) [LinkedIn](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F%2F&src=sdkpreparse) [Reddit](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F%2F&src=sdkpreparse) [Flipboard](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F%2F&src=sdkpreparse) [Copy link](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F%2F&src=sdkpreparse) [Email](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.makeuseof.com%2Fwasted-money-over-aa-battery-code-meaning%2F%2F&src=sdkpreparse) 
  Reply / Post Attachment(s) Please respect our [community guidelines](https://www.valnetinc.com/en/terms-of-use#community-guidelines). No links, inappropriate language, or spam.
  Your comment has not been saved
  [Send confirmation email](https://www.valnetinc.com/en/terms-of-use#community-guidelines)
  Randy J [Randy J](https://www.makeuseof.com/profile/VD816931/)[Randy J](https://www.makeuseof.com/profile/VD816931/)#VD816931 Member since 2025-11-14 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/VD816931/)We need to ban non-rechargeable batteries. The amount of disposable batteries going into the trash and then leaking the chemical composition into the soil and therefor water supply is unnecessary not to mention the battery body takes decades to decompose. I am not sure why people even purchase them, you can get decent rechargeables on Amazon for as cheap as budget non-rechargeable batteries now.
* 2025-11-17 09:33:58
  WR [WR](https://www.makeuseof.com/profile/RU042813/)[WR](https://www.makeuseof.com/profile/RU042813/)#RU042813 Member since 2023-10-03 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/RU042813/)"decent rechargeables on Amazon" don't work in all situations. high drain situations require Lithium or the equivalent; if you try to use rechargeables, you are recharging several times a day, so until rechargeables get a lot better, you still need non-rechargeable batteries.
* 2025-11-17 11:06:11
  Lee [Lee](https://www.makeuseof.com/profile/MP569583/)[Lee](https://www.makeuseof.com/profile/MP569583/)#MP569583 Member since 2024-06-09 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/MP569583/)Randy rechargeables aren't generally 1.5vdc they're more like 1.3-1.4 in many cases when fully charged. however IF a ni-cad actually works for your situ you should use them. Anyhow that's what I do because I already have them. And I don't care if they die because I must have a coupla dozen of them. I think proprietary lithium rechargeable is better for things like camCorders and such because they have heavy drain capability. But for mine the manufacturer sent 2 of them.
* 2025-11-17 13:28:48
  Randy J [Randy J](https://www.makeuseof.com/profile/VD816931/)[Randy J](https://www.makeuseof.com/profile/VD816931/)#VD816931 Member since 2025-11-14 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/VD816931/)Lee - I put rechargeables in everything including items requiring more power. I havent bought regular batteries in years and only end up with them since I liquidate estates and take out batteries before I ship so the dont explode in the mail (seriously, dont ship batteries if at all possible and if you do, seal them separately). I have yet to come across anything where rechargeables have not worked.
* 2025-11-18 01:24:46
  Linda [Linda](https://www.makeuseof.com/profile/KO225474/)[Linda](https://www.makeuseof.com/profile/KO225474/)#KO225474 Member since 2025-05-06 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/KO225474/)Outstanding article! This is a huge help.
  Your newletters are always well done.
* 2025-11-17 13:06:36
  sqstultz [sqstultz](https://www.makeuseof.com/profile/PL428924/)[sqstultz](https://www.makeuseof.com/profile/PL428924/)#PL428924 Member since 2025-11-17 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/PL428924/)Rats, I switched from NiMH rechargeable AAs to Li-ion USB-C rechargeable AAs and I thought I was on to something. I guess it's back to the NiMH rechargeables.
* 2025-11-17 10:39:27
  MUOMember [MUOMember](https://www.makeuseof.com/profile/AM016348/)[MUOMember](https://www.makeuseof.com/profile/AM016348/)#AM016348 Member since 2025-11-17 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/AM016348/)If your rechargeable li-ion batteries are working for you then use them. Despite what this article implies they are fine. The statement the 2200mAh @1.5v is not the same as 2200mAh @3.7v is obvious but of no consequence. Simply put the mAh rating is relative. 3000mAh still provides more storage capacity than 2000mAh. No one is measuring the power consumption of their devices. How long the battery lasts in your device is the only criteria. Non rechargeable lithium batteries capacity might be 3500mAh but that is measured down to a terminal voltage of 0.8v, a voltage that would not be reached before your device stops operating. The chargeable li-ion batteries will maintain a constant 1.5v until the li-ion cell at 3.7v drops to 1.5v+ drop out voltage for the regulator. Yes, they fail as soon as the li-ion cell drops below that threshold but unless you are using them in a flashlight, your device will fail as soon as the battery, no matter the technology drops below the required voltage. Think of all of the batteries that won't end up in the trash. You can recycle (who knows what actually happens to them) li-ion cells, not lithium non-rechargeable batteries.
* 2025-11-17 15:18:24
  sqstultz [sqstultz](https://www.makeuseof.com/profile/PL428924/)[sqstultz](https://www.makeuseof.com/profile/PL428924/)#PL428924 Member since 2025-11-17 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/PL428924/)MUOMember Great, thanks for the advice and explanation there. I'll surely keep them and use them, but probably switch back to NiMH when I need to buy more.
* 2025-11-17 16:34:08
  Henry [Henry](https://www.makeuseof.com/profile/MN779967/)[Henry](https://www.makeuseof.com/profile/MN779967/)#MN779967 Member since 2025-10-11 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/MN779967/)I'll note if you're stuck with some of these batteries that limp out in your cameras and etc. (either because you got the type that don't give it quite enough current, or because you did and they're running down), these work fantastic for remote controls and the non-high-current stuff. Set them aside for that rather than chucking them straight into the trash. I mean, maybe the used batteries will 'only' last 6 months instead of 2 years in the remote (the 'not high enough current for the camera' ones will probably last a full lifetime). But whatever, it's at 0 the cost when you're reusing batteries you were going to throw out otherwise.
* 2025-11-17 12:39:56
  JimmyMcGill [JimmyMcGill](https://www.makeuseof.com/profile/SX651123/)[JimmyMcGill](https://www.makeuseof.com/profile/SX651123/)#SX651123 Member since 2025-10-27 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/SX651123/)very comprehensive!!! And I didn't know that about the USB li-ion batteries. what a scam. I was wondering why major manufacturers don't make them
* 2025-11-17 11:06:52
  Oswaldo [Oswaldo](https://www.makeuseof.com/profile/OI055825/)[Oswaldo](https://www.makeuseof.com/profile/OI055825/)#OI055825 Member since 2023-10-18 Following 0 Topics 0 Users Follow Followed 1 Follower [View](https://www.makeuseof.com/profile/OI055825/)Also, there are plenty rechargeable batteries (not like the rechargeable AAs in the article) specially made for things like XBox game controllers.
* 2025-11-17 22:06:13
  Ken [Ken](https://www.makeuseof.com/profile/DR772955/)[Ken](https://www.makeuseof.com/profile/DR772955/)#DR772955 Member since 2025-11-17 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/DR772955/)I don't get the complaint about USB rechargeable AA batteries. OK, they do have some hidden internal complexities which is usually not good. I gave up on rechargeable batteries because the charger is another device, or worse set of devices, to keep track of (I have way too much crap in my life). My frustration with finding the correct charger when I need it to give up and start throwing them away. If it gives me the convenience of recharging using a universal standard (USB-C) then it provides rechargeable technology in a package that I can use -- or does it? I wish there was someone who could write an objective article about this technology :)
* 2025-11-17 11:48:08
  Amir [Amir](https://www.makeuseof.com/profile/SV534043/)[Amir](https://www.makeuseof.com/profile/SV534043/)#SV534043 Following 0 Topics 1 Users Follow Followed 1 Follower [View](https://www.makeuseof.com/profile/SV534043/)Accepted! I just ordered a pack and will review them soon.
* 2025-11-17 12:39:44
  Roger60 [Roger60](https://www.makeuseof.com/profile/KC495291/)[Roger60](https://www.makeuseof.com/profile/KC495291/)#KC495291 Member since 2023-10-18 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/KC495291/)I don't understand your concern with rechargeable li-Ion AA batteries.
  "The battery capacity (mAh) is never as high as advertised (because 2200mAh at 1.5V ≠ 2200mAh at 3.7V), and you’re paying for complexity, not performance."
  Your warning is at its place when buying power banks . If they advertise 10.000mAh it is for the internal 3.7V battery and this will not equal 10.000mAh at 5V output. 37Wh=5Vx 7400mAh. But in your example it cannot be worse than the advertised 2200mAh ,only better. The trick used with rechargeable Li-Ion batteries: they mention **not mAh** but **mWh** . 3000mWh=3000/1,5=2000 mAh at 1,5V.
* 2025-11-18 14:20:57
  Bouncedancer [Bouncedancer](https://www.makeuseof.com/profile/JA744234/)[Bouncedancer](https://www.makeuseof.com/profile/JA744234/)#JA744234 Member since 2025-03-09 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/JA744234/)I mostly use AA batteries for my microcurrent device, which is a medical device (amazing for pain relief!). I started to notice that when my device would tell me the batteries were expired, I would put them back in and they would keep performing for weeks and sometimes months afterwards! I don't know if that is the batteries or my device, but maybe there are a lot of alkaline batteries being thrown away prematurely?
  Then I switched to lithium alkaline batteries, and, although much more expensive than the regular alkaline ones, they provide impressive performance for months on end, even with daily use of my device. And they don't leak. But when they're dead, they're dead.
* 2025-11-17 14:05:46
  Jasom [Jasom](https://www.makeuseof.com/profile/AM261123/)[Jasom](https://www.makeuseof.com/profile/AM261123/)#AM261123 Member since 2023-11-03 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/AM261123/)Maybe the manufacturers should provide the "correct" rechargeable batteris with the device.
  All supporting USB A/c connectors.
  AND offer sale of spares.
  Less batteries being disposed of.
  No need for external battery chargers.
  Reducing overall cost to the customer.
* 2025-11-17 10:40:33
  JimmyMcGill [JimmyMcGill](https://www.makeuseof.com/profile/SX651123/)[JimmyMcGill](https://www.makeuseof.com/profile/SX651123/)#SX651123 Member since 2025-10-27 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/SX651123/)honestly the device should be able to charge the NiMH batteries on its own. that'd be perfect. like if I've put rechargable batteies in my camera, and ive connected a USB to the camera, it should charge the batteries too. what's stopping them?
* 2025-11-17 11:07:55
  ch [ch](https://www.makeuseof.com/profile/YW612383/)[ch](https://www.makeuseof.com/profile/YW612383/)#YW612383 Member since 2023-07-17 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/YW612383/)Any thoughts about AAAs ? Or are the codes the same?
* 2025-11-17 11:31:57
  Henry [Henry](https://www.makeuseof.com/profile/MN779967/)[Henry](https://www.makeuseof.com/profile/MN779967/)#MN779967 Member since 2025-10-11 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/MN779967/)Yeah, except the size code is 03 instead of 6, so LR03, R03, etc. instead of LR6, R6, etc.. (There'd also be a different JIS size so it's not a UM-3, per google it's UM-4, but (at least according to Google AI which may be full of it) UM-4 also specified carbon-zinc so they're also called AM-4s.)
* 2025-11-17 12:34:25
  Bill [Bill](https://www.makeuseof.com/profile/KA982220/)[Bill](https://www.makeuseof.com/profile/KA982220/)#KA982220 Member since 2025-11-07 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/KA982220/)I like eneloops for rechargeable AA and AAA batteries, but always go for the lithium primarys if there's any temperature concern. The backup flashlight in the car and outside temperature monitor are on the short list for lithium primarys, other batteries don't like running when it's bellow freezing out.
* 2025-11-18 13:18:21
  Tiffany [Tiffany](https://www.makeuseof.com/profile/BR140474/)[Tiffany](https://www.makeuseof.com/profile/BR140474/)#BR140474 Member since 2025-06-15 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/BR140474/)They do sell Lithium rechargeable AA batteries.. but they're not very common... That's why industry went LiPo and started making their own batteries... 18650 and 21700, are the answer.
* 2025-11-18 14:07:37
  Roger60 [Roger60](https://www.makeuseof.com/profile/KC495291/)[Roger60](https://www.makeuseof.com/profile/KC495291/)#KC495291 Member since 2023-10-18 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/KC495291/)The reason to use Li AA, rechargeable or not is because they deliver 1,5V like non rechargeable batteries and therefor are a better replacement in devices that do not function properly at lower voltages of NiMh (1,2V).Some devices simply expect 3V or 4,5V from 2 or 3 AA alkaline in series not 2,4 or 3,6V.
* 2025-11-18 13:05:14
  Lee [Lee](https://www.makeuseof.com/profile/XL155496/)[Lee](https://www.makeuseof.com/profile/XL155496/)#XL155496 Member since 2023-11-03 Following 0 Topics 0 Users Follow Followed 0 Followers [View](https://www.makeuseof.com/profile/XL155496/)I bought a ten pack of TCL rechargables been working for years - but where they go? Only 2 left!
* 2025-11-18 10:02:38
* [Terms](https://www.makeuseof.com/profile/XL155496/)
* [Privacy](https://www.makeuseof.com/profile/XL155496/)
* [Feedback](https://www.makeuseof.com/profile/XL155496/)
  Recommended 4 days ago

##### [I tried the Waze alternative no one talks about — and it’s great, up to a point](https://www.makeuseof.com/tried-waze-alternative-no-one-talks-about-and-its-great-up-to-a-point/)

5 days ago

##### [I riced Windows 11 and now every other setup feels boring](https://www.makeuseof.com/tried-waze-alternative-no-one-talks-about-and-its-great-up-to-a-point/)

5 days ago

##### [You should seriously give this lesser-known streaming app a try](https://www.makeuseof.com/tried-waze-alternative-no-one-talks-about-and-its-great-up-to-a-point/)

4 days ago

##### [Why does this harmless emoji make ChatGPT lose its mind?](https://www.makeuseof.com/tried-waze-alternative-no-one-talks-about-and-its-great-up-to-a-point/)

##### Technology Explained

##### PC & Mobile

###### [I've ignored these symbols on my USB ports for so long and now I regret it](https://www.makeuseof.com/tried-waze-alternative-no-one-talks-about-and-its-great-up-to-a-point/)

###### 1 day ago [I wasted so much money on AA batteries because I missed this tiny detail](https://www.makeuseof.com/wasted-money-over-aa-battery-code-meaning/)

###### 1 day ago [Don’t let Google drop support for your Chromebook — do this instead](https://www.makeuseof.com/dont-let-google-drop-chromebook-support/)

###### 3 days ago [See More](https://www.makeuseof.com/category/technology-explained/) [If your Android feels slow or cluttered, this open-source launcher fixes it](https://www.makeuseof.com/category/technology-explained/)

###### 3 hours ago [I tested 27 iPhone screen protectors and this is the one you should buy](https://www.makeuseof.com/tested-27-iphone-screen-protectors-this-the-one-you-should-buy/)

###### 8 hours ago [This is what I'm doing instead of getting a new iPhone this year](https://www.makeuseof.com/do-this-instead-of-getting-new-iphone-this-year/)

###### 11 hours ago [See More](https://www.makeuseof.com/category/pc-mobile/) [This under-the-radar Chrome extension saved me hours of work](https://www.makeuseof.com/category/pc-mobile/)

###### [I slept on this Samsung productivity feature for years but now I use it every day](https://www.makeuseof.com/category/pc-mobile/)

###### [I tested 4 open-source alternatives to Google's Gboard — they're much better than you think](https://www.makeuseof.com/category/pc-mobile/)

* [Join Our Team](https://www.makeuseof.com/category/pc-mobile/)
* [Our Audience](https://www.makeuseof.com/category/pc-mobile/)
* [About Us](https://www.makeuseof.com/category/pc-mobile/)
* [Press & Events](https://www.makeuseof.com/category/pc-mobile/)
* [Media Coverage](https://www.makeuseof.com/category/pc-mobile/)
* [Contact Us](https://www.makeuseof.com/category/pc-mobile/)
* Follow Us
* [Advertising](https://www.makeuseof.com/category/pc-mobile/)
* [Careers](https://www.makeuseof.com/category/pc-mobile/)
* [Terms](https://www.makeuseof.com/category/pc-mobile/)
* [Privacy](https://www.makeuseof.com/category/pc-mobile/)
* [Policies](https://www.makeuseof.com/category/pc-mobile/)
  [MUO](https://www.makeuseof.com/category/pc-mobile/) is part of the [Valnet Publishing Group](https://www.valnetinc.com/en/) Copyright © 2025 Valnet Inc.