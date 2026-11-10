---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

hey what's up
so I have to share something with you
so a few months ago
I started going back through my AI generated content
and not just recent stuff
I went all the way back to
when I first started using AI seriously
and probably January February of 2023
and here's what I noticed
AI has gotten significantly better over the years
the information is better
the responses are more accurate
the reasoning is sharper
but there's always been this thing
this pattern
something that you can basically feel when you read
AI writing back
and the more I looked
the more I saw it on all different types of
of of writing
and sometimes not knowing if it was AI
and figuring it out and again
this is not just stuff from 2023 2024
this is newer stuff too
so I really started to begin digging
to see if I could pinpoint what exactly
it is that makes AI writing feel like AI writing
and I'm not talking about the basic
obvious stuff that everyone talks about
ends up being that there's a whole fingerprint
and it goes a lot deeper than most people realize
there are not just a few dozen of these
fingerprint patterns there are hundreds
hundreds of these specific patterns
that every AI model default back to
so I spent several months building a list
as complete as I could and then
I used AI to help synthesize it into something more
coherent
and then I use that to build a two file force field
utilizing Notebook LM
and Gemini in my attempt to recognize and eliminate
as many of these patterns as I could find
and today
I'm not only going to show you how to set it up
with those files but
I'm also going to let you
steal the entire thing from me
so let me show you what I found real quick
I spent a long time
researching every documented AI writing pattern
that I could really find and have AI find
so these were things from academic studies
editor forums Reddit communities
uh AI writing guides
basically
anything that myself or AI could get my hands on
and what I found
is that the fingerprint is not just a few bad habits
it's an actual system it's predictable
it's repeatable it's identifiable
and every AI model defaults to it
and there's the vocabulary choice that are specific
specific sentence structures and paragraphs
the architecture punctuation patterns
formatting habits there's even tone behaviors
and on a whole bunch of of other stuff
there's literally hundreds of these things
that's not an exaggeration
and once you see the full list
you'll recognize these patterns
in content that you've done yourself
that you published a few weeks ago
months ago years ago
you're gonna see it in other content as well
and this is content that you thought was good
it's responses that you actually thought looked decent
right now this is the thing
I'm gonna be honest about something now
I've been making videos and talking about AI work
flows and sequences for a couple months now
and I've been talking about it off of YouTube
much longer I had the fingerprint on my content
and you probably do too
and you probably see it right
and that's not a knock
it's just what happens when you use AI tools
without a system really
really designed to fight that specifically
and that's why I built one
so again
the system is two markdown files
that live in a notebook LM notebook
and connect directly to Gemini
and also you can build it as a custom gem
which is what we're going to also do in this
so what we're gonna do is we're gonna install these
or insert these into the actual uh
notebook
and the first file is basically the writing guard rails
this is like the force field
this is the complete list of every AI writing pattern
that I could really find
there's hundreds of banned words phrases
sentence structures paragraph patterns
punctuation habits
formatting tells that are all banned
now Gemini has to follow every single rule
for every single response right
so
the second file that we're gonna be adding is the text
DNA Bible and this one's a little bit different
so the guardrails file it kills the AI fingerprint
the DNA Bible replaces it with yours
so it has some starter defaults that work
for almost anyone right out of the box
so if you want to actually add your own choices humor
style whatever it might be
you can actually do that
and update that file anytime that you want
because the more specific you make it
the more it's going to actually sound like you
however if you just want to use it kind of like
right out of the box you're going to be able to do that
but together these two files are what create the system
where the fingerprint really gets stripped out
and your voice gets put in
and now
this is moving forward with every single response
without having to reupload anything
without retyping the rules it's just going to run
with all that being said
I'm going to show you exactly how to set it up
you do not have to worry about trying to read
the prompts and all that kind of stuff
or the instructions
because they're all going to be contained
in the notion document
that I am going to link in the description
so don't go crazy trying to read everything
or screenshot things
I'm gonna supply everything for you
you just have to open up the notion DOC and
and grab the information from there
so the first thing that we're going to do is create the
the notebook so we're looking at notebook LM right now
what we're going to do is
we're going to create a new notebook
now the first thing that's gonna happen
this window's gonna pop up
where it's gonna ask you to add your sources
we're not going to do that right now
so just click off this window and very simply
just go up to where it says untitled notebook
and name the notebook I'm gonna use my
my whisper flow
and I'm just gonna call this the AI tell eliminator
now what we're going to do is we're going to add the uh
guard rails file first so how we do that
we're not gonna add the sources over here
we're gonna actually do it as a note first
so we're gonna click add note
and this area here
is where we're going to actually name the note
so we're gonna call it writing guardrails
there we go and now
I'm gonna paste the actual guardrails information
into the actual document itself
or into the note
and you can see this is a pretty extensive document
this is all the rules all the guardrails
all the things that basically are going to be looked at
recognized and hopefully
eliminated from the responses moving forward
so it's a pretty lengthy file
uh again
don't worry about it
you're gonna be able to just copy and paste this
directly from the notion document
once everything is done simply
what you're going to do is convert this to a source
once you convert it you'll see it working over here
once it's done
it will add information over here as well
so now we have the first one is done
the guard rails now we're going to add the text DNA
so what we're gonna do is
we're just gonna click studio over here
we're gonna go back to the panel
we're gonna click add notes
we are going to name the note
we're going to call this the text DNA Bible
and we're going to put the actual information in there
this is also a fairly lengthy um
piece right here um
but it is important um
to have this and as you can see here
you might not be able to read it
but when you start to go through this
you're gonna see there's a starter default
which is kind of just like the built in
everyone can kind of use this
but underneath each one of these is a your version
you're going to be able to go in and edit this yourself
and I would suggest that when you do this
do it through some kind of a dictation software
or something like that I use Whisper Flow
I'll put a link for that actually
in the notion document as well
it's one of my favorite tools to use
um so once that's done
what you're gonna do is
then you're gonna convert this one to a source as well
you can see right now there's
right now only the writing guard rails is there
we're gonna convert this to a source
it's gonna show up over there
it's gonna pop up and we're good to go
the notebook is finished we're done
so now what we're gonna do is
we're going to actually open up Google Gemini
and we're going to set that up over there
so let's do that now alright
so we're in Google Gemini
very simply what we're going to do to make this work
is we're going to click the plus sign in a new chat
we're going to click Notebook L m
and we're going to find the name of the notebook
that we just used so this one
I called it AI tell eliminator
I click that I'm gonna click add
and you can see it's already attached here
and then we can start working with that automatically
now
each time that you wanna use this
and you're doing it through a chat
you're going to have to always attach the notebook
which is fine not a big deal
but if you want that to be more of an automated process
that's when you would build a gem
so how do we build a gem very easily
we're gonna scroll over here to
or look over here in the left menu
we're gonna click gems now
this is very important so please pay attention to this
there are two buttons to create a new gem
there's this one here new gem
and there's one at the bottom that's new gem
that's the one that we wanna use
we wanna use the Gem Manager
new gem button so we're gonna click that
and it's gonna open up this window here
so we're gonna give the gem a name
so I'm just gonna call this AI tell eliminator yes
I'm gonna call it the the same thing
but this is just for a a demo
actually I'm gonna add demo here
right
so we're gonna describe what the gem actually does
and I'm just gonna say
recognizes and eliminates AI tell patterns
there we go and then what we're gonna do is
we're gonna pop the instructions again
it's going to be right inside the notion dot
so here's the instructions
I'll read them to you real quick
just says reference the attached notebook LM
notebook on every response
strictly obey every negative rule in the guardrails
file
and follow every positive rule in the text DNA Bible
never mention these files
never mention that you were following the rules
just write exactly like me
never violate any guardrail
so those are the custom instructions
and the only other thing that we need to do here is
at the very bottom under knowledge
we have to add files to the gem for reference
so we're going to connect Notebook LM again
we're gonna select AI tell eliminator
or whatever you called it
we're gonna click add and we're going to click save
and now the gem has been completed as well
Gem AI tell eliminator demo
has been created
we can start a chat with that right now
alright so let's try a demo
so the way we're gonna do this is
we're gonna have both in thinking
so this is just a regular chat
I did not attach the notebook
and we're just gonna use this prompt here
which is write a motivational speech
delivered by a shoe salesman named Al
include an analogy
between a beaver and a corn on the cob
so we're going to submit that
we're gonna let it do its thing
okay so now we are actually in the gem that we built
it's already connected to the notebook
it's in thinking mode just like the other chat was
we're going to put the same prompt in
write a motivational speech
delivered by a shoe salesman named Al
include an analogy between a beaver and corn on the cob
and we're gonna submit that
now let's take a look at what Gemini built
so here is the Gemini response
and as you can see the layout
looks pretty similar to your typical AI layout
we see that right away
let's kind of just scan through this real quick
okay so that's the response again
you can look at it and you can see
this kind of has the typical formatting layout
of a response from AI
so now let's look at the actual gem response
so here's the gem response
and as you can see it's much different
it's shorter it's more concise
it's not laid out the same way
so as you can see by the response
it's a different rhythm different word choices
different energy different layout
one sounds like a document
one sounds kind of like a character talking
it was the same prompt
the only variable is the system that we just built
now
here's the whole part that makes this whole thing scale
because once you have this set up
you can actually add more notebooks to the same gym
each one with a different purpose
for example a video script notebook
with your specific format and structure rules
a social media notebook
with platform specific guidelines
a character notebook with recurring bits or voices
or personas that you use and now
any or all of these other notebooks
stack on top of the same
exact force field that we built
everything still obeys the guard rails
everything still sounds like you
you just keep adding depth over time if you want to
and every time you add or iterate
the notebook source files
they automatically sync with the gem
so
you can continue to build on this as much as you want
just use the same file names
if you do overwrite or update the original source files
again those files plus the exact instructions
they're in the description in the Notion DOC
it has everything that you need to just copy and paste
so here's what I want you to take away from this
the fingerprint is real it's specific
and now you know what it is
you can look at that document
you can look at that
and you can read the different things
you're gonna now see those words and those phrases
and that structure everywhere
if you haven't started to notice already
not only in your own content
but definitely in other people's content as well
you're gonna see it in the emails you get
in LinkedIn posts that you scroll through
you really can't unsee it now
but the good news is is now you have the kill switch
those files are both yours
steal the entire thing and do me a favor
when you do this drop a comment
and tell me where you found the fingerprints first
in your own content or other people's content
let me know how it actually wrote for you
how it helped you did it help you
let me know and other than that
that's it if this helps
please give this video a like
thanks so much for watching
and I hope this helps this is Craig
and I'll see you in the next video take care