---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

hey what's up
so listen
even if you've never created an AI image before
or you've been getting better and better at it
I have to share this with you right now
so listen my wife and I
run several different YouTube channels together
so we're always looking to do things
to help us manage these channels
as efficiently as we can
and one of the things that she loves about the process
is actually creating images with AI
and this wasn't something that we knew would happen
but after she saw like
all the incredible things that she could do with AI
and the images like
she was hooked
and once you see this process and system
you might be as well so several months back
she came to me with something
she had found an image online that she loved
she loved the style the lighting
the the feel of it
she wanted to recreate something very similar
utilizing AI but no matter what she tried
she just couldn't get it right
it was different every time
it was close sometimes
but never what she actually wanted
and after an hour or so she got frustrated
so she asked if I could help
and what I tried first
is maybe exactly what you might have tried too
so my first attempt was pretty simple
it was the obvious move to me
was take the image and have AI analyze it
and then describe it back to me as a prompt
and I don't know if you've ever done that or not
but that works right
and that's what I did and it helped
it was better
better than what she was getting on her own
but it still required like
a bunch of back and forth and iterations
it still wasn't quite there
it was a little bit inconsistent
it wasn't quite right and I kept thinking to myself
well why is it still off
why is it not getting to the point that she wants it to
I mean the AI could see the image right
it could describe it but
something was getting lost
between the description and the actual generation
it's like the AI was guessing
even with the slightly better information
that we gave it from AI looking at the prompt right
so this is kind of where it all changed
this was the this was the shift for me
so separately and completely unrelated to this
I realized something for a long time
I've used AI to help me write Javascript
Javascript for images for videos
for even AI music and and songs
and a lot of other workflows
and if you're thinking wait a second
I have no idea what Jason is
don't worry
I'm gonna get to that in just a quick moment
but you don't have to know anything about it right
so anyways I started thinking
if AI can look at the instructions that I give it
and give me back a Jason code to use as a prompt
could it actually look at an image
analyze an image and give me back a
based on prompt instead of just using a text prompt
not a description not a paragraph
but an actual structured profile
with every single decision kind of locked in
so I tried it and that was the answer it was
this is the results
it looked like what she actually wanted
on the actual first try so real quick
here's the simple version of what's happening
or what happened so
a normal prompt is like walking into a restaurant
and asking the chef to make something
tasty that has chicken sauce
some pasta but not chicken parm
so that chef right
he's gonna go out and do their best
but he's gonna be guessing
every time you order you get something that tastes good
but it's always a little bit different
but on the other hand Jason is like
handing that same chef the complete recipe
the exact ingredients the exact amounts
the exact technique and the chef
and when the chef follows that
now the meal is basically the same every time
and the best part
you don't actually have to write the recipe yourself
the system I'm sharing
with you today writes that Jason code for you
you simply just copy and paste it and boom
you get what you're looking for instantly
so eventually
what actually got built here was four total files
with instructions examples
modifiers and a bunch of other things
to create just really incredible AI images
and the first file is the master system
this is basically the brain
the complete Jason schema
the AI uses to build every single profile
every single prompt
the second file is the meta token library
think of it like a vocabulary list
it's specific photography styles
it's lighting setups it's cameras
it's lenses and everything's already mapped out
so
the AI pulls from this when it builds the final prompt
right
the third file is the Quick Start guide
and this is what you can look at in plain English
plain language it's step by step
there's no technical knowledge
so you can always just read that
and then
the fourth file is the instructions for the gem
or the instructions for whatever tool you wanna use
and this is what you just paste into Gemini
to turn the whole thing into an actual
dedicated tool for yourself
and again I'm giving you the entire system
which will be LinkedIn a Notion DOC in the description
so you can build this exactly how I'm going to
to show you here
and you can use it in other AI models as well
what's truly awesome is that you set this system up
just once in less than five minutes
even if you've never used AI before
right so
the Gemini Gem done
notebook L m what we're gonna use
it's gonna be done Claude
Project chat GPT it's the same files
same result every AI image tool
you already use one setup
and it's gonna pretty much work forever
and you can also add to this down the road
so let me show you how we're actually going to build it
so follow me along with this process
so first thing we're gonna do is
we're going to go to notebook LM
and I already have it open here
and what we're gonna do is
we're gonna create a new notebook
and we're gonna close this window here
right now uh
this is where you can add sources
we're not gonna add the sources right now
first
what we're gonna do is we're gonna name the notebook
so I'm just gonna call this Jason image demo right
so you can see that it populated here
and the next thing we're going to do is
we're going to add the sources
which is very simple we're going to go to add sources
we're going to click drive
and then we're going to select the actual Google Docs
the Google Docs all you need to do very simply
is go to the notion DOC
and just copy and paste the information
into a Google DOC save it
and then you're going to to upload
just make sure that you're saving the Google Docs
and the Notebook LM is in the same Google account
so real quick
we're going to upload those files real quick
alright so I've added the four files
you can see them over here as sources
now that they're all there
we're pretty much done setting up the notebook
we gave it a name we gave it the four files
now that the notebook is done
we now just need to go over to Google Gemini
and we need to
set up the gym now
this process is gonna be very similar
also if you're setting this up as a custom GPT
or projects in something like Claude or Chat GPT
or rock or something whatever you're gonna
whatever you're actually going to use
so we're gonna go over to Google Gemini
we're going to click gems
this window is going to pop up
and if you've seen my other videos doing this
you know that we are not going to click on new Gem here
we're actually gonna use this one at the bottom
underneath the gem manager
so once you click New Gem
it's gonna open up a window just like this
so you're gonna give your gem a name
so we're gonna call this one Jason image demo
describe the gem takes images and creates Jason code
perfect
and then the instructions that we're going to give it
live in the instructions file
and that's going to be in the notion document
but I'm just gonna copy it here
I'm gonna go back to Gemini
I'm going to paste those in right
so now we have those instructions in there
and again that's in the actual Notion DOC document
we're going to add
files to your gem for reference
and that's where we're gonna add the notebook
so then we're going to just click Notebook LM
we're gonna select that file
Jason image demo
and we're gonna click add
once we click add we hit save
we're done that's the whole setup
it might have taken me two minutes
so even if you're brand new to AI
this should take you no more than five minutes
to do exactly what I just did
it's very very simple
right and again
if you use Claude or Chat GPT
and you wanna create a new project
or a custom GPT you just paste the master system file
as your instructions
and then upload the token library as the source right
you're gonna get the same result
but you can use it with a different tool
alright so let's do a demo and see how this all works
let me share my screen alright
so we are in our actual Jason image demo
and what I'm gonna do is I'm gonna grab an image
I'm just going to go over to uh pexels.com
I found an image already that I really like
it's got a lot of cool colors in it
and all that kind of stuff
so that's the first thing I'm gonna do
I'm going to just I'm on pexels.com I found the image
I wanna use I'm just gonna right click
I'm gonna say copy image
we don't have to actually download it this time right
so I'm gonna just close this out
I'm gonna go over to Gemini
I'm in Gemini right now I'm gonna go to a new chat
I'm actually just gonna
paste this in here and I'm just gonna say
describe this image to me as a prompt
so I can recreate something like this
i'mma submit that
and it's gonna go through and it's going to analyze it
and it's gonna give me that actual image
so here we go here's the actual image prompt
now this is just regular text image prompt
but I'm gonna take this I'm gonna copy that
I'm gonna create a new chat in Gemini
I'm gonna go to create image
now I'm using this directly through Gemini
so this is going to use
Nana Banana to create this image
and I'm going to hit return
now
with this being said this is using Nana Banana
and what you're going to notice
is that there's going to be a little watermark
on the bottom right hand
now if you have the Pro account
you can create you know
quite a few of these images per day on Nana Banana
I'm sorry on
on Google Gemini
so this is the image that it created
based off of the prompt that we had
it just analyze that image
not through the gem just through regular Gemini
and this is what it created
and when I open that up you can kind of
you can see oops
hold on you can see right here
it's got the watermark created an image and uh
you know yes
it looks pretty good it's it's
is it exactly like like this no
but it's not bad right
it's not bad
it's not exactly what we wanted
so what we're going to do now is
we're going to actually do the same thing
with the same image but we're going to use our gem
so I grab the same image
I'm in the actual Jason image demo now
and all I'm gonna do is
I'm just going to paste that image in there
I like to put this on thinking mode
you can keep it on fast I like to keep it on thinking
um but anyway I'm going to hit
submit
and now what it's gonna do is gonna analyze this image
but it's going to give us back the Jason code
based off of what this image is
so after a little bit
you can see it starts to create the Jason code
you don't have to worry about this again
if you don't understand Jason
code no problem
if you do wanna just kind of
look around it a little bit
you can kind of get an idea of how it works
right so you have the source style
the overall aesthetic the mood
the subject the main subject description
so you have all these different things
and then you have a little bit of a description
but this is much more formatted
so what we're gonna do is
we're gonna take this exact prompt
we're gonna create a new chat in Gemini
and we're going to put uh
I'm sorry we're gonna create image
and we're just going to paste
the actual Jason prompt in there
and again I'm gonna put this on thinking
and I'm gonna hit go submit
and let's see how this comes out
alright
so this is the result based off of the Jason Code
and I think that this is a lot more similar
to this kind of style
compared to that other one that we saw earlier
and I'll put those both on the screen
so you can kind of compare them
but I want to show you something really cool
because if you have a Google Pro account
which is the 20 dollar a month plan
you can actually use Google Flow
and the benefit of using Google Flow
is that you can create v 0 3 videos there
or you can create images there using Nana Banana
however they do not have the watermark
and you can create up to four at a time
and it's completely free
so let me show you how to do that
so just simply just Google Flow
you're gonna enter flow
you're gonna Wanna make sure that you're
in your Google account that's your paid pro account
click New Project
and what you wanna make sure is that you are set to
Nana Banana Pro or
I'm sorry Nana Banana 2
you can click this and you can change it right
you can change it to Nana Banana Pro if you want
but Nana Banana 2 is the newer one
is the more modern one or
or the more current one I should say
and you have these different image sizes
I'm gonna keep on 16 by 9 landscape
and you can see it says 1 2 3 four
that means that you are able to create four images
so I'm gonna do that create four
I'm gonna paste that Jason prompt
and I'm going to hit go now
it's gonna create four versions of that same
exact prompt so there's gonna be
you're gonna see how similar they look
but they're also going to be
you might find one that you like better
which means
that you don't have to create four different images
four different times in Google Gemini
you can create four versions here
if you want to create more
you can create more they're free
so you can create more and they don't have the uh
they don't have the Gemini logo at the bottom right
so these are just about done
let's see how they came out
I like this one so far yep
you can see how very similar they are
right so the original image
it kind of came out from the side
if we if we look at that again
um
the
the dock or the deck or whatever you want to call it
comes out from kind of from the side
where in flow it's more straight ahead
but again it
it gets the skies
I think this is probably the closest to the sky that uh
that we wanted but you can kind of see like
how this looks and what's awesome about this as well
is that when you wanna download this
guess what you can actually download it
in 2K 4K if you have the Ultra plan
but the Ultra plan is like 250 bucks a month
so uh
if you don't have that plan
you can upscale to 2K just click that
it's gonna download it or it's gonna upscale it
and then it's gonna download it
and we'll take a look at the 2K version and just
and here's the 2K version
this is how it looks and look
there is no watermark so now this is great
because what you're able to do with this
and this is what I do is I'll take this image
and I'll use this as a starting image for a video
right so you can utilize
if you're doing a video or things like that
or utilizing something like video or clay
or things like that you can use a start image
and I like to create these start images first
or the or the reference image
that it's gonna use as the first frame
and a lot of them also allow you to add a uh
an end frame so it would be
whatever happens in those 5 to 8 to 10 to 15 seconds
depending on what tool you're utilizing
it's gonna have the start screen
which could be this and maybe the end screen is
is this exact picture
but maybe it's night time or something like that
so you can make the video a time lapse whatever
whatever it might be but
this is a really good way
to be able to get those types of images as well
especially when you find something
like let's say you're doing a Google image search
and you find something and you really like the image
but you wanna add something to it
and that's something that you can do here as well
um you can actually add stuff to this
so you know what let's do that actually real quick
I wanna add a sailboat going across the lake
alright add a sailboat in distance
so now what it's gonna do
or what it should do
is that it should recreate this image
very similar to this
but there should be a sailboat in this
now I didn't give it any descriptions of the sailboat
so who knows what it's going to actually do
but let's hit submit and see what happens
so again the image itself
should be very similar to how these are
I don't think it's gonna change too much there
but there should be a sailboat out here somewhere
now I said in the distance
so it should put it further out
it shouldn't be like
right up here next to the
next to the dock or whatever
it should be in the distance
but let's see what happens
and there we go we have very similar image
but now we have sailboat out there
right silhouette of a sailboat perfect
I didn't even say silhouette
I just said sailboat
here's another one that you can kind of see
and this looks really good
it looks really really good
like if I tried to
if I tried to prompt this to do this and all kinds of
I'm not sure it would come out this good
because again
remember this is based off of an actual photograph
that we had the gem create
the Jason code for this to be able to do this
and again you can always upscale this
you just click Download Upscale to 2K
once it's done upscaling it
you'll download it
and we can open that up and we can take a look at it
and this is gonna be the one with the sailboat
so it should be clearer than than this is currently
and here's the 2K file
very nice looks very good
I like it alright
so I think you have a pretty good understanding
of how to actually do this with the image
so you just all
you literally
all you have to do is just put the image in there
the image whatever image you want
you just put it right into the gem
paste the uh
paste copy the image
paste it in here you don't need to do anything else
just hit return enter whatever it is and submit it
and you're gonna get the prompt back
put that into anything that you want
you can put into grok uh
imagine
you can put it into chat GPT
you can put it into Google Flow
your Gemini whatever it is that you want to use
now if it does not work
the prompt does not work
it means that whatever image editor you're utilizing
does not accept Jason uh
code to to actually create it
if that's the case you can always ask another AI
or go back to the AI and say
can you please create this as a very extensive prompt
from this JSON code and then go
and then use it from there
now is it going to be as good as the JSON code
version of it probably not
it'll be close
but it probably won't be as good as the Jason
but it's probably going to be better than
if you were just going to
try to go and prompt it yourself
and try to get it in there
so with all that being said
you know that's that
so the other thing that we can do is
we can actually have this create a prompt in Jason
for an image that we actually want to see
so in that case I'm going to actually say
let's do something kind of interesting
no let's do this
a large ferocious
terrifying long haired Bigfoot is hiding behind a tree
looking at me trying to figure out what I am
as I am trying to take a picture of it from my camera
I don't know that's a pretty shh
crappy prompt
but let's just see what happens
so again I'm gonna put this back on thinking
doesn't need to be on thinking
I just like to use it on thinking
and I'm gonna hit submit so what's gonna do
is gonna analyze that pretty crappy prompt
but it's going to create an actual Jason code for that
so it's gonna go through its process
and this is also where it's gonna be
utilizing all those meta tokens
now the meta tokens are just a
a huge list of different photographic styles
different types of cameras that it could take it with
different type of lens for instance
like this one what did it choose for this one
for the camera so it chose a Sony A7R 5
which is a great camera I actually have an A7R 4
this is the A7R 5 that it
that it decided to choose an 85 millimeter lens
so let's take a look and see how this creates it
so let's copy this code
and remember this is from my simple prompt of a large
ferocious terrifying
long haired Bigfoot is hiding behind a tree
looking at me trying to figure out what I am
as I'm trying to take a picture of it from my camera
so we are going to go to Google Flow
we'll do it there why not get four versions of it
I'll do it right in the same project no big deal
and let's take a look
and just for all intents and purposes
let's take just that actual prompt that I wrote
and let's run it through here too
and let's let's compare how the basic prompt looks
compared to the Jason prompt
alright so here we go
and this is a perfect example of what happens
when you can do some prompting
and it puts things in the image that you don't want
for instance I said I'm taking a picture of it
the regular prompt which is
these top ones show the actual camera
this one here it actually shows like
an actual screen here um
this version here well
look at he's
he must have just gone in for a
a perm or something I'm not
I'm not quite sure what this big foot is doing um
but his hair is uh
yeah it's
it's killer um
but here I like I think I look at something like this
this is a much scarier
more terrifying looking Bigfoot
and there's no camera in the picture
and it followed
much closer
to what I actually wanted it to actually do
that's the difference
that Jason Code can provide you with
so I hope that was a good example
I hope that kind of gives you a
a better idea of how this Jason stuff actually works
why it's really cool
to be able to actually get Jason code
to do this kind of stuff for you
but more importantly
to be able to take images that you find
that you wanna emulate for your own purposes
or whatever it ends up being and
and again like we said
we took this one and we added the sailboat to it
we just said add a sailboat to the image
and then we pasted that original prompt
the original Jason code
that did not have the sailboat in there
and it did that um
so you're able to you're able to do that kind of stuff
so even if we wanted to take this image again
I'm gonna repeat it
but I'm just gonna go up to the very top
right above the entire prompt I'm just going to put
add a pink skully to the Bigfoot
with a colorful pom pom on top
let's see how this one looks
and honestly I wanna know
what are your thoughts on the difference
between the Jason version
and just the regular prompt version
um
because again
I think this is a good example to show you that
you know sometimes when you ask it to do something
and if you haven't used AI before
to actually create images
you may not have seen this
but I'm sure a lot of you
if you have you
you have where you put
and here's the the new images that it just came up with
um
yeah I have to say that's
that's still regardless of the hat
that's still if I saw that in the woods
I would uh
I would I
I would not be
I I would not be taking a picture of it
let's just let's just say there would not be any
any proof that I took a picture of it
I would I would be
I would be out of there right um
but yeah
let me know what you guys think
let me know what you guys think about the whole process
and again
for those of you that have messed around with AI and
and it adds in these things
like adds the camera in there
obviously
the camera wouldn't be there
if you were taking a picture of the Bigfoot right
you wouldn't see that
unless somebody was standing behind you
or somebody was standing in front of you
but that's not what we said right
we just said basically a
you know Bigfoot hiding behind a tree
that I'm taking a picture of it staring at me
right the Jason Code
got that both even with the hat
there's no camera in the picture
there's nothing and I think it looks better
I think it looks more real
I think it looks more like what I was expecting
and that's what you guys should also see
when you start to do this yourself
so here's what I want you to take away today
my wife didn't think much of AI image generation
at first right
she actually thought it was
it was a bit silly but once she saw what it could do
once her ideas actually started
coming out right
she did really kind of fall in love with it
and here's the thing whether or not
that you've been messing around with AI images
for a while or you're just getting started
this method is going to work either way
it's gonna give you better results it's gonna give you
more consistency
and you really should see the difference immediately
but again you don't have to take my word for it
I'm giving this to you you can try it yourself
and set it up in literally about two minutes from now
grab it from the Notion DOC
set it up try it out yourself
play around with it
let me know how your results come out
let me know in the description
tell me the tell me
I don't know I really do
but other than that I hope this helps
allows you to get some really cool stuff done
better results than what you've been getting now
with your image creation
thanks for checking out the video
hope it helps this is Craig
and I will see you in the next video take care