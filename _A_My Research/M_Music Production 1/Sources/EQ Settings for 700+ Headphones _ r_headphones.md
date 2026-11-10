---
tags:
  - notebooklm-import
notebook: "M_Music Production 1"
category: "research"
---

# WebSync metadata

* title: EQ Settings for 700+ Headphones : r/headphones
* url: https://www.reddit.com/r/headphones/comments/92b08s/eq\_settings\_for\_700\_headphones/
* date: 2025-06-28T04:13:30.964Z

EQ Settings for 700+ Headphones: r/headphones

[image: r/headphones icon] Go to headphones

EQ Settings for 700+ Headphones

Cool!

I started lurking here about a year ago and got pretty soon excited about possibilities of using equalizer to improve headphones. Then I got very disappointed of the lack of existing headphone eq settings. Disappointment turned into resolution and this <https://78.media.tumblr.com/61490213cf0047d301c706ac1b3538c9/tumblr_inline_p8qgenVgOK1uc537a_500.gif> was my reaction.

Now I'm exited to present to you equalization settings for over 700 headphones: https://github.com/jaakkopasanen/AutoEq. This includes all on-ear headphone measurements from Innerfidelity and Headphone.com with 4 different target curves. Combined with EqualizerAPO <https://sourceforge.net/projects/equalizerapo/> this is essentially a free alternative to Sonarworks True-Fi <https://www.sonarworks.com/truefi> with almost 5 times as many headphone models. Full details on how to use the eq settings and what else you can do with this can be found in the Github page.

This is not supposed to be the be-all and end-all of headphone equalization. Especially the target curve is a tricky thing to nail down because Innerfidelity and Headphone.com measurements are not directly comparable with the measurement system used by Sean Olive and others for their Harman target response research. I would love to hear feedback from you fellow headphone enthusiasts. Do you think this makes your headphones sound better and what kind of problems do you have with these eq settings?

I hope this makes equalization a bit more approachable for people who feel intimidated by it. Also keep in mind that you are allowed to tune the eq for example with HeSuVi <https://sourceforge.net/projects/hesuvi/> to make it more to your liking.

*Updates*

We are currently at over 2500 headphones!

1.

Settled for SBAF-Serious target curve for Innerfidelity and Headphone.com

2.

Innerfidelity and Headphone.com IEMs and earbuds equalized.

3.

Rtings measurements added.

4.

oratory1990 measurements added.

5.

Parametric equalizers are now supported. Every headphone has settings for peak filters.

6.

Convolution equalizers supported with minimum phase and linear phase impulse response filters. All pre-computed results have minimum phase filter for 44.1 kHz and 48 kHz.

7.

Fixed band (also known as graphic) equalizers supported. All pre-computed results have standard 10-band equalizer levels.

8.

Added Reference Audio Analyzer measurements.

9.

Added Crinacle's IEM measurements.

*FAQ*

*Do you have*  If you can't find it in the results then the measurement is missing and I cannot produce the eq curve, sorry. However you can create the eq settings yourself if you find the frequence response graph by following this guide https://medium.com/@jaakkopasanen/make-your-headphones-sound-supreme-1cbd567832a9.

*Does it work with Mac?* AutoEQ produces settings for parametric eqs. Any parametric eq which has at least 5 bands available should be able to use them.

*Can I use*  If the raw frequency responses are close to each other then yes otherwise it might do more harm. Give it a listen and judge for yourself.

Sort by:

Best

Open comment sort options

Best

Top

New

Controversial

Old

Q&A

[image: u/verifitting avatar] u/verifitting avatar

verifitting

•

Amp:A20h, DAC:PecanPi, Audial | HD600Mod, AD2000, SINE w/MSR7pad

All I can say is "Wow!".

[image: u/demevalos avatar] u/demevalos avatar

demevalos

•

T1 2nd Gen | Element II

What a play!

7maniAlkhalaf

•

Modi>Magni,CTH,LCX>x00,DT1990,HD800

I understand this reference

hvperRL

•

Clear Pro || Cascade || Andromeda

Calculated

bunkbail

•

🎧HD660S

No problem.

More replies  More replies  More replies  [image: u/PCisLife avatar] u/PCisLife avatar

PCisLife

•

Sorry!

More replies  [image: u/earllemongilbs avatar] u/earllemongilbs avatar

earllemongilbs

•

Fiio E17K -> Sony WH1000XM2/Custom Grado GS Clones/CA Orion

Obligatory Owen Wilson Woooow <https://i.imgur.com/9bkrhtG.gif>

More replies  [image: u/GalantisX avatar] u/GalantisX avatar

GalantisX

•

iFi Nano/DX3Pro >Elex|Sundara|AD2000|Andromeda|Final E5000

Holy shit this is awesome

However, I would definitely love support for peace gui. Using peace apo feels much more intuitive than the graphic eq.

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Yeah, I know. Unfortunately that would require me to create a optimizer which fits several peak filters to the equalization curve. Nothing impossible but quite a bit of work to do. I might do it at some point but no promises.

[image: u/oxtoacart avatar] u/oxtoacart avatar

oxtoacart

•

Verum One | CCA CRA | TempoTec V6

It's not quite the same, but there is a Python program that can generate convolution files for room correction, so perhaps there's something that can be reused there - https://www.minidsp.com/applications/advanced-tools/python-open-room-correction

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Thank you so much! I'm sure I can use PORC for convolution filters. Needs a little work to plug it into my code though but nevertheless precious find.

More replies  [image: u/GalantisX avatar] u/GalantisX avatar

GalantisX

•

iFi Nano/DX3Pro >Elex|Sundara|AD2000|Andromeda|Final E5000

Completely understandable. Hope other peace gui users speak up so there is enough of a demand to make it worthwhile:)

More replies  More replies  [image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Parametric equalizers are now supported. Every headphone has settings for peak filters. See instructions for usage <https://github.com/jaakkopasanen/AutoEq#peace-and-other-parametric-equalizers>.

More replies  More replies

[deleted] •

I have added this to the sidebar. If you would like it removed please let us know. Thanks for the hard work.

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Thanks a lot. This is a great honor.

More replies  [image: u/Fuzzwy avatar] u/Fuzzwy avatar

Fuzzwy

•

M40x

Can this go in the sidebar? This is amazing, thanks!

[deleted] •

Done.

More replies  [image: u/GalantisX avatar] u/GalantisX avatar

GalantisX

•

iFi Nano/DX3Pro >Elex|Sundara|AD2000|Andromeda|Final E5000

I'd recommend people with M50Xs to try this

Never "hated" them to begin with, but they did sound a little "off" with some types of music, like vocal heavy music.

After using these EQ settings for the past hour, they sound so much more natural and flat out "better"

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Awesome to hear this!

[deleted] •

Is there any way for an android to work for this?

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Not yet. Android doesn't have EqualizerAPO and AutoEQ only produces EqualizerAPO configs. In the future there might be impulse responses generated which would make it possible to run them with Viper4Android. That requires a root though.

[deleted] •

Tried Viper4Android but it just dont seem to work with my S7 Edge rooted with custom rom.

bunkbail

• • Edited

🎧HD660S

You'll need Magisk root, and install V4A directly from the repo on the Magisk app. Works a charm with my S7 Flat.

Optionally, you can also install "Ainur Sauron", "Audio Compatibility Patch" and "Audio Modification Library" stuff from the repo for further sound quality improvements.

More replies  More replies  More replies  More replies  More replies  More replies  [image: u/Businassman avatar] u/Businassman avatar

Businassman

•

Any plans to include the results of this website <https://www.rtings.com/headphones/1-2/graph#628/2031> as well?

Just asking because the DT1990 sadly isn't included anywhere else so far...

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

As a matter of fact yes. However I decided to release first just with Innerfidelity and Headphone.com results and get some feedback before going on with crawling more sites.

[image: u/Businassman avatar] u/Businassman avatar

Businassman

•

That's great! Thanks for your work so far:)

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

It's your lucky day. I'm on a good mood https://github.com/jaakkopasanen/AutoEq/tree/master/results/custom/Beyerdynamic%20DT%201990

Parsed the compensated frequency response with this tool: https://apps.automeris.io/wpd/.

[image: u/Businassman avatar] u/Businassman avatar

Businassman

•

:O

Awesome! Did not expect that, I appreciate it:D

More replies  More replies  More replies  More replies,

[image: u/oratory1990 avatar] u/oratory1990 avatar

oratory1990

• • Edited

acoustic engineer

[image: Profile Badge for the Achievement Top 1% Commenter] Profile Badge for the Achievement Top 1% Commenter

While I do appreciate the effort in programming this tool one has to keep in mind that the Innerfidelity measurements are not directly compatible with the Harman Target.

Innerfidelity/Tyll used a *HeadAcoustics HMSII.3*, but the Harman Target was derived using a *Gras 43AG* coupler to measure the headphones.

So keep that in mind, especially when using EQ above 2 kHz, where the two systems will begin to differ from each other.

Maybe we can find a way for OP to use the measurements that I make - those *are* compatible to the Harman Target, as I use a 43AG and 43AC coupler.

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

This is precisely why there is no Harman target as one of the available target curves. I think especially the SBAF-Serious might be close for Innerfidelity measurements what Harman target is for Gras 43AG. Technical Challenges <https://github.com/jaakkopasanen/AutoEq#technical-challenges> section opens up this issue further. You are probably way more knowledgeable about these matters so if there are any mistakes I would appreciate feedback.

Where would I find your measurements? I would like produce (or at least try to) similar calibration curve as I have between Innerfidelity and Headphone.com as explained in the Calibration <https://github.com/jaakkopasanen/AutoEq#calibration> section.

[image: u/oratory1990 avatar] u/oratory1990 avatar

oratory1990

•

acoustic engineer

[image: Profile Badge for the Achievement Top 1% Commenter] Profile Badge for the Achievement Top 1% Commenter

I think especially the SBAF-Serious might be close for Innerfidelity measurements what Harman target is for Gras 43AG.

The thing is that due to the differing acoustic impedance of the two measurement rigs (HeadAcoustics vs GRAS) they will always produce differing results - and you can not simply add a static calibration curve to transfer one set of measurements to another. This would require a different calibration curve for every headphone.

Rtings.com (who use the same measurement rig as Innerfidelity) tried this by measuring a few headphones that were previously measured by Sean Olive and his team and see if they could come up with a transfer calibration curve, but it turned out to be impossible due to the differing acoustic impedances of the measurement rigs.

Where would I find your measurements?

we should continue this discussion via PM

More replies  More replies

catmeowstoomany

•

I use sonarworks in my DAW and my headphones only mixes are coming out better then the bigger studio mixes I have done. It’s partly I can spend more time at home with the headphones but I feel more confidant about the mixes sounding good elsewhere on the eq’d cans. Sonarworks settings is set to flat, so nothing is hyped and I can get a even mix. I’ll defenetly check out the other app because I want to be able to use this feature outside of my daw. Thanks for posting!

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Be sure to share your opinions how AutoEQ compares to Sonarworks.

More replies  [image: u/Nico777 avatar] u/Nico777 avatar

Nico777

•

Sennheiser HD 800

Super stupid question that will definitely highlight how little I know about this stuff: let's say I like the bass of my 770s as it is, can I use these settings and just remove every negative adjustment below 250Hz?

[image: u/BuggyCat avatar] u/BuggyCat avatar

BuggyCat

•

,

Yup! I suggest playing around with it so you get a better idea of what part of your music changes when you tweak different frequencies and then you’ll know which signatures better fit your taste.

[image: u/Nico777 avatar] u/Nico777 avatar

Nico777

•

Sennheiser HD 800

I will play around a bit then, thank you!

More replies  More replies  [image: u/oxtoacart avatar] u/oxtoacart avatar

oxtoacart

•

Verum One | CCA CRA | TempoTec V6

Very cool! I'll put a vote in for generating parametric EQ, with the ability to cap the number of bands (I use a lot of mobile apps that can only do 5 or 6 bands of parametric).

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Thanks. This little might be a small number for a general case but we'll see how well it turns out when/if I implement the peak filter optimizer. Could also be that I'll create 5+5 bands where the first 5 can be used as standalone and the rest 5 just improve it if they are available.

[image: u/gepardcv avatar] u/gepardcv avatar

gepardcv

•

That would be killer. 5 bands would make thus usable with hardware PEQ, like the RME ADI-2 series.

[image: u/oxtoacart avatar] u/oxtoacart avatar

oxtoacart

•

Verum One | CCA CRA | TempoTec V6

I generate corrections with Room EQ wizard and for the headphones I’ve tried you can get a pretty decent result with 5 or 6 bands.

More replies  More replies

[deleted] •

Well that was convienent the hd 650 eq was in the description itself lol

TY, the accurate subbass + added boost in the 6khz region sounds very tame yet good

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Very good.

More replies  More replies  [image: u/thebigzor avatar] u/thebigzor avatar

thebigzor

•

Man this is so awesome, until you find out your "fancy" headphones you have are not on the list....

Thank you for your work, I will save for when I have some real headphones

GZoST

[image: Cake icon] • • Edited

HE-60, DCA E3, HD800, HD580, Focal Clear, B2Dusk, Hexa

Thanks for this! Hope I can find the time soon to play around with this (and compare it to True-Fi as well, which I find really useful).

Equalization should be an essential part of audio today, and it should be driven by measurements. Efforts like yours are a great help.

I find that I can listen to low-end headphones and enjoy the music as long as they are tonally accurate. There are real and absolutely worthwhile improvements with better hardware, but even tonal response to me is the basis for real headphone quality.

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

I agree, frequency response is the most important part of sound quality but eq doesn't turn low-end headphones into high-end headphones. Eq however can turn intolerable headphones into pleasant headphones. If headphones have major sonic problems they are mostly in the frequency response.

More replies

catmeowstoomany

•

Mac version?

[deleted] •

Comment deleted by user

More replies  [image: u/RainofOranges avatar] u/RainofOranges avatar

RainofOranges

•

Sundara | 6XX | DT990 | SRH840

Maybe I'm just used to the sound my DT990s make without EQ, but to me they sound almost lifeless with these EQ settings. Definitely admire the work put into this program though, it seems others are finding it wonderful!

More replies  [image: u/t4tris avatar] u/t4tris avatar

t4tris

• • Edited

AFO | K371 | DT770 | HD6XX | WH-1000XM3 | SMSL M500

How is this different from the bot at the Headphone Headquarters Discord server?

http://suuupslave.com/

bot\_measurebaiting channel, "GETEQ:hd800,hd800s:20" (:20 to limit the amount of EQ sliders to something reasonable for APO to handle) for example. There are also commands for different targets like "diffuse" and I assume whatever target curve you'd like.

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

I wasn't aware of this, looks cool! AutoEQ has different target curves which might better match human perception on Innerfidelity measurement system. Also AutoEQ has Headphone.com measurements which don't seem be available at suupslave. And of course AutoEQ has tools for making new eq settings while playing with different parameters such as tilt and bass boost and different targets, even other headphones.

More replies

docdaa008

•

hifime UH1>Lyr 2>HD600|AKG K7XX|Momentum|

Holy crap, good stuff!

bunkbail

• • Edited

🎧HD660S

No M1060 EQ FeelsBadMan.

But so far I'm digging the EQ settings for HD660S, I like it a lot compared to the Discord bot Harman Target settings.

EDIT: Holy shit! These EQ settings are awesome af! It feels like I'm using a HD600, neutral sounding but with the clarity, imaging and instrument separation of HD660S! It feels like the veil in high freqs is lifted off. Great job OP!

More replies  [image: u/letho2 avatar] u/letho2 avatar

letho2

•

HD600/HD6XX/HD58X/Momentums V1/ATH-M50S/Meze Noir/Kanas Pro

Amazing. Thank you.

[image: u/MathiasBoegebjerg avatar] u/MathiasBoegebjerg avatar

MathiasBoegebjerg

•

discord.me/headphones

Heh, I made the same thing half a year ago. Guess I should fire my marketing department..

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

That's the Discord bot right? Do you have a public git repo for it somewhere? Honestly I find it quite interesting choice to have the results only in Discord, or is there some other sink for them?

I would love to hear your feedback about AutoEQ and if there are any tips about equalization I might have omitted while building this. And of course if there is something you could use from my project you are more than welcome to do so, MIT licence and all.

Getting things noticed by people is really hard. It's sad that your thing didn't get the attention it deserves. Honestly I have been thinking about that title for weeks now. Sometimes it's quite small things.

More replies

hideonsink

•

BR07BE

Wow this is huge

[image: u/Mine\_Fuhrer avatar] u/Mine\_Fuhrer avatar

Mine\_Fuhrer

•

HYPERCLAP <https://i.redd.it/ijutvac3o0811.gif>

new\_to\_edc

•

RME ADI-2/HE-6/Stax L700/Stax 353x

A word of warning. A frequency response doesn't tell the whole story, a more accurate approach would be to use a CSD / waterfall. A waterfall graph shows the resonance of each frequency, as well as the amplitude.

Real-world example - a Monoprice M1060 has a dip at 5kHz. This headphone is also pretty resonant at this frequency - if music hits this note, the note will "last" for a while. The cumulative energy (or perceived loudness) of this frequency might actually be fairly high, despite looking like a dip in the frequency response. EQing it up is the wrong thing to do in this case.

Check out the graph here = https://www.superbestaudiofriends.org/index.php?threads/monoprice-m1060-measurements-and-stream-of-consciousness-review.4318/ - left to right axis is the frequency, front-to-back axis is the decay (measures in milliseconds).

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Wise words indeed. Unfortunately there are very few waterfall measurements available. In the end the responsibility is with the user, if eq doesn't make the headphones sound better then it should not be used or the equalization should be changed somehow.

More replies

[deleted] •

I'm new to equalizerapo..

Do I download it and use the code you provided on GitHub, then find my dt880's in the find headphones?

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

• • Edited

That's right. Download and install EqualizerAPO, and replace contents of *C:\Program Files\EqualizerAPO\config\config.txt* with this

Preamp: -6.0dB

GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.7; 32 5.4; 35 5.1; 37 4.8; 40 4.5; 42 4.4; 45 4.2; 49 3.8; 52 3.6; 56 3.3; 59 3.1; 64 3.2; 68 3.5; 73 3.3; 78 2.7; 83 2.1; 89 1.7; 95 1.2; 102 0.7; 109 0.3; 117 -0.1; 125 -0.6; 134 -1.0; 143 -1.3; 153 -1.6; 164 -1.5; 175 -1.6; 188 -1.7; 201 -1.8; 215 -1.8; 230 -1.8; 246 -1.8; 263 -1.8; 282 -1.7; 301 -1.6; 323 -1.6; 345 -1.5; 369 -1.5; 395 -1.4; 423 -1.1; 452 -0.7; 484 -0.7; 518 -0.8; 554 -0.7; 593 -0.5; 635 -0.5; 679 -0.4; 726 -0.3; 777 -0.1; 832 -0.3; 890 -0.5; 952 -0.2; 1019 0.0; 1090 0.3; 1167 0.3; 1248 0.7; 1336 0.7; 1429 0.5; 1529 0.2; 1636 0.0; 1751 -0.4; 1873 -0.3; 2004 -0.0; 2145 0.4; 2295 1.0; 2455 1.6; 2627 2.0; 2811 2.0; 3008 1.7; 3219 1.0; 3444 0.3; 3685 -0.4; 3943 -0.2; 4219 -0.4; 4514 -0.2; 4830 -0.1; 5168 -1.0; 5530 -2.1; 5917 -2.5; 6331 -2.2; 6775 -2.0; 7249 -3.7; 7756 -5.6; 8299 -7.3; 8880 -7.5; 9502 -5.8; 10167 -2.8; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -0.9; 15258 -0.7; 16326 -0.5; 17469 -1.5; 18692 -3.4; 20000 -5.4

This is equalization result for 250 ohm DT 880 with SBAF-Serious target and measured by Innerfidelity. See here: https://github.com/jaakkopasanen/AutoEq/tree/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%20250%20ohm

32 ohm version <https://github.com/jaakkopasanen/AutoEq/tree/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%2032%20ohm>

EDIT: Fixed links, they were pointing to Sonoma Model One target results, now they point to SBAF-Serious.

More replies  More replies  [image: u/RedMosquitoMM avatar] u/RedMosquitoMM avatar

RedMosquitoMM

•

FiiO Q5 > HD-6XX / Nighthawk + EQ / 64 Audio A6

Any idea if these EQ settings can be utilized as-is in an external app that has its own DSP, like Roon <https://kb.roonlabs.com/DSP_Engine>?

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Unfortunately it's not possible at the moment. Roon has parametric EQ so it would be possible AutoEQ had peak filter optimizer. Another thing I have been thinking about is to produce impulse responses from the equalization frequency response. That would work with Roon also as well as Pulseaudio on Linux.

More replies  More replies

Purish

• • Edited

Will this Beyerdynamic DT990 <https://github.com/jaakkopasanen/AutoEq/tree/master/results/SBAF-Serious/headphoncecom/onear/Beyerdynamic%20DT990> sound proper on the DT990 250 ohm?

Edit: Fixed the link to the EQ settings.

More replies  [image: u/Hifimanz avatar] u/Hifimanz avatar

Hifimanz

•

Sorry if this is an odd question but is there a reason why over all volume has decreased? I have dt770's and since I've been using the EAPO I have to turn my magni 2 uber to like 2pm instead of 11am. Thanks for any help.

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

There is a negative digital preamp to counteract the positive eq gain on some frequencies. So in practice what happens is that the maximum gain is at 0dB and everything else is attenuated. Maximum gain *should be* at 0dB or there will be clipping.

[image: u/Hifimanz avatar] u/Hifimanz avatar

Hifimanz

•

Thank you

More replies  More replies

DigitSubversion

•

DT770 \ HD 558 \ Philips SHB4405 \ Xiaomi 3.5 ANC

The github page has a typo: vevn instead of venv.

More replies

AFAIX

•

Wow!

Would it be possible to use it with anything Linux though?

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Sorry, not at the moment. There might be impulse responses produced at some point and Pulseaudio can use those.

More replies

[deleted] •

Nice! I like the change it has made to my AKG240 Studio 'phones (I used the config for the MKII). Thanks!

More replies

[deleted] • • Edited

The EQ adjustments for the ZMF Atticus just aren't really doing it for me. It doesn't sound quite right. If compared to the HD650 adjustments towards the 2018 harman target by u/oratory1990  these are just not that great at increasing clarity. I had to tone down the bass a little and the treble boosts for the HD650 due to my own treble sensitivity, but it improves the HD650. Unfortunately the stock Atticus sound is better than with this EQ. My DAC/amp has 1db steps for volume control, so adjusting 6db to match the negative preamp is easy enough for a fair comparison. I wonder if the wood type or pair to pair variance and the use of different measurement rigs impacts this disparity between the two EQ cases of oratorys HD650 EQ and the ZMF Atticus EQ settings here. Kudos for all the work though. I'm thinking other cans might fare better.

I'm going to spend some more time adjusting and see how I feel...

edit... Listening to some Adele's Send My Love (To Your New Lover) (one of my old reference songs) with the EQ, the additional treble brings out some of the echo/reverb on her vocals, but overall I think it sounds better without. It just seems more balanced.

[image: u/oratory1990 avatar] u/oratory1990 avatar

oratory1990

•

acoustic engineer

[image: Profile Badge for the Achievement Top 1% Commenter] Profile Badge for the Achievement Top 1% Commenter

wonder if the wood type or pair to pair variance and the use of different measurement rigs impacts this

It's the latter.

Wood type has a big influence on how the headphone looks (obviously), but little to no influence on how the headphone sounds. (Unless we're talking about balsa wood vs ebony, but even then it's more about the physical weight then the actual wood type.)

No, what you are experiencing is that the measurements made by Innerfidelity are made on a slightly outdated measurement rig. The value of these measurements lies in their huge numbers - you can compare measurements of different headphones and get a good idea of how they sound, even though the measurements don't necessarily reflect what you are hearing in absolute numbers, they can be judged in a "relative" way.

More modern (and sadly, more expensive) measurement rigs like the one that I'm using better reproduce the various parameters of an actual human ear (I've written about this matter here <https://www.reddit.com/r/DIEMs/comments/75pfaq/frequency_response_testing/do7wka1/> and here <https://www.reddit.com/r/headphones/comments/7szpqm/199_minidsp_ears_vs_judes_gras_a_quick_comparison/dt9pm7d/>. Sean Olive used such a measurement rig to derive what became known as the " Harman Target <https://www.reddit.com/r/headphones/comments/78x77b/initial_impressions_of_2016_audeze_lcd2f_with/doyj84e/> ", which is - for all we know - the best suited target response for headphones. There's a bunch of research behind it that conclusively shows that (while not perfect) this target is better sounding (to the majority of people) than anything else we currently know of (like the various diffuse-field curves, independent-of-direction, free-field and other proprietary target curves).

And I can't stress this enough: It's not one person's random guess at what sounds good. There's actual, conclusive, peer-reviewed, hard science behind it. About 7 years worth of scientific papers have been published by his research group.

To sum it up:

Why do "my" EQ settings sound "better"?

a) I'm working from better data that more accurately reflects how human ears perceive a headphone

b) this data enables me to use the most state-of-the-art target curves, which is more likely to sound "good" to you.

and maybe c): I fine-tune my EQ settings by hand. I am a musician (non-professional), audio engineer (semi-professional) and acoustic engineer (professional), which means I have had extensive listening training and generally have a somewhat good idea of whether things sound right or not.:)

(but mostly a) and b) )

More replies  [image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Thanks for the feedback, I appreciate it. It's hard to know what causes this, there might be multiple reasons. u/oratory1990  is using the same measurement system as which was used to develop Harman target so that's spot on. Maybe the target responses for AutoEQ are not quite right yet. I have difficulties adjusting the targets because I only have one unmodded pair of headphones and have no training in listening to frequency responses. Also some headphones have large variations between individual units, maybe yours and the ones measured by Innerfidelity are far apart.

More replies  More replies  [image: u/raptyo avatar] u/raptyo avatar

raptyo

•

Thank you for your work! I am currently using the HD58X and I think the HD600 EQ softens them up a bit which I like, less grainy sound. How difficult would it be to make an EQ for the HD58X?

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Since I don't have frequency response measurement for HD58X, very.

[image: u/raptyo avatar] u/raptyo avatar

raptyo

•

I think diyaudioheaven did a review on them and posted this graph: https://i.imgur.com/f5A3hC5.png, I tried to EQ them myself based on this graph, but couldnt get very good results, only slightly clearer highs. I was going for a smoother sound but I need to do some more research first I guess. Are these the kind of graphs you would use for your equalization?

More replies  More replies  More replies

Memesmakemememe

•

Damn, I couldn’t find mine.

More replies  [image: u/squirrelthetire avatar] u/squirrelthetire avatar

squirrelthetire

•

DT770 Studio 80ohm | HE-4XX | HD518 ||| FX-Audio DAC-X6

Neat.

I tried this out with my HD518, and they sound a lot thinner. I'm not sure how I feel about it, since the baseline with these headphones is already pretty thin. The bass is less punchy, and there is much less reverb.

Definitely an interesting idea!

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Interesting. HD 518 has a very pronounced accentuation at upper bass / lower midrange which is tuned down by this eq. This is probably why you feel like they sound thin. In the end it comes down to personal preferences but if you listen to your headphones eq'd for some time (hours or even days) without switching back your brains will get adjusted. After that you might not want to go back and non-eq'd might sound very muddy. Try it out and see what happens.

[image: u/squirrelthetire avatar] u/squirrelthetire avatar

squirrelthetire

•

DT770 Studio 80ohm | HE-4XX | HD518 ||| FX-Audio DAC-X6

Definitely going to give it a try for a few days at least.

More replies  More replies

Parmenidesides

•

Are the Hifiman HE-400 2014 measurements supposed to be for the 400i? On Innerfidelity they have HiFiMAN HE-400i 2014 listed as a link that takes you to headphone measurements labeled as HiFiMAN HE400 2014.

[image: u/TrptJim avatar] u/TrptJim avatar

TrptJim

•

Thanks you for putting together and posting this. That's a lot of headphones.

I don't see the Hifiman HE-400i in there, unfortunately. Would the HE400 be close enough to use those settings?

[deleted] •

Comment removed by moderator

More replies  [image: u/Axaion avatar] u/Axaion avatar

Axaion

•

Hd598 feels really bassy with this

Maybe I'm weird..

[deleted] •

If you've become accustomed to the 598 sound then you're used to the bass light sound signature, this will sound bass heavy by comparison but it really isn't that much in the grand scheme of things.

More replies  More replies  [image: u/commonsense34 avatar] u/commonsense34 avatar

commonsense34

• • Edited

First of all, I would like to congratulate jaakkopasanen on his elaborate work.

Dear Jaakko and fellow redditors, there is also a free and easy way....

I know what you mean so I deleted the rest of my post.

More replies  [image: u/virusavatar avatar] u/virusavatar avatar

virusavatar

•

K7xx|SHP9600|6xx|1MoreTriple|Elegia|SMSL SP200|Topping D50s

As a complete novice to the headphone scene, and having never done any equalization before, I thought it wouldn't be worth the effort to even try for very little discernible difference.

Oh boy, I was wrong...

Using the HD 6xx EQ settings, I was *completely* taken aback by the stark difference in the low end! From now on, I'll always be wondering about the depths of what else I was missing out on. Thanks a ton dude!

Also, your 1More Triple Over Ear EQ page is broken and I want it!

More replies

bagajohny

•

Tin T2 | Porta Pro | ER2XR | KSC75

It looks like you have updated(re-computed) all the GraphicEq files. May I ask what changes in general did you make? Also, will there be any difference in sound with previous vs new Eq? What really changed?

More replies

MalayGhost

•

Hey there, any update on getting Impulse Responses with Viper4Android? Still waiting for a system-wide eq, hope you have good news

More replies

[deleted] •

Comment deleted by user

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Glad to hear you like it.

ubiquitous\_raven

•

StaxL300|Eclair|Ananda|HD6XX|Oracle|Variations|Starfield

Every time I come back to this thread, after buying a new headphone, I feel ever so grateful to u/jaakkopasanen  for this amazing repository. This is a priceless resource for us headphone audiophiles.

And contributions from u/oratory1990  and the sites are invaluable, giving us the much needed data that this repository is comprised of.

I feel fortunate to be a part of such a community:)

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

Thanks for the kind words. I'm glad my little creation serves you well.

More replies

RuRRuR

•

Is there an option to apply something similar to this on Android?

[image: u/jaakkopasanen avatar] u/jaakkopasanen avatar

jaakkopasanen

•

USB Audio Player PRO has parametric EQ and works with local files and many streaming services though not Spotify. Viper4Android is system wide solution but requires rooting of the device. Some phones have built in system wide equalizer with limited number of fixed (Q and center frequency) filters but this requires you to find appropriate gain values manually so that it would match as close as possible to the desired eq curve.

More replies  More replies

Promoted

[image: sidebar promoted post thumbnail]

---

---

Promoted

[image: sidebar promoted post thumbnail]