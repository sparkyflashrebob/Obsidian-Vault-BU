---
tags:
  - notebooklm-import
notebook: "M_Music Production 1"
category: "research"
---

♪ (plinking) ♪
♪ (plinking morphs into unrecognizable sounds) ♪
Hey, it's Andrew Huang,
and I am thrilled to be partnering
with GRM Tools for the launch of Atelier,
an incredible new piece of software
for musical exploration and sound design.
Atelier is both a standalone application and a plugin,
so everything I'm going to show you,
you can either use it in its own program,
or you can have it loaded up in as many instances as your
computer can handle in a DAW.
It's the spiritual successor to GRM Tools, which is a
highly respected suite of plugins made by the GRM,
the pioneering experimental music
research institute founded by Pierre Schaeffer.
I've had early access to this for several months.
I was giving them some feedback, and I'm honored, honestly,
that they asked if I would do a little tour video for them.
So, let's check it out.
♪ (pinging, plonky beautiful sounds) ♪
There are two rows of modules, so at the top
it's Processors, and at the bottom it's Modulators.
You can add new modules by
clicking a plus icon and choosing one,
and it'll insert it right there in your left-to-right
signal flow here for the audio processors.
And for Modulators, it's just one plus here because it
doesn't matter what order modulators go in.
Let's look all the way over to
the left here at this Gen module.
As you can see, everything is
nicely, dynamically resizable.
It's a beautiful interface, honestly.
So, this module is generating the kind of droning pad chord
sound that you're hearing in the background,
and if I click anywhere here, I'm adding new tones to that
chord at the frequencies that I've picked.
These are called cursors, by the way, and I can
double-click to remove any of these.
If you select any cursor, you
can see its individual parameters,
whereas below you're looking at module-wide parameters.
You'll notice as I add
cursors, they can be different colors.
And this is one of the genius things about how Atelier
handles channels and routing.
It's all done with the spread parameter, which on this
module is also controlled by
the vertical position of cursors.
So, the more red or green a cursor is, the more that it
will be going to an individual channel.
For my setup right now, it's just green and red for stereo.
But as a quick example, let's turn
on some additional output channels,
and you can see now, I've got four possible colors,
because with each new cursor I'm adding, Atelier is
automatically routing them to all of my available outputs.
So, it's a super fast way to work with spatial audio,
and there actually is no limit on how
many different output channels you can have.
It's just up to your CPU.
One last cool thing about the
cursors is that they always sum to white.
So, I've got a red cursor here going to one channel.
As I move it up and it sounds spreads to more channels,
it turns more pink, and as I move it further up to white,
it becomes evenly spread to all channels.
So, you have a visual indication of
how spread or not each cursor's sound is.
A couple other things that apply to
most modules, if you click this icon,
all of your cursors snap to the nearest semitone,
and this slider at the top of any graph
will shift the ratios of all your cursors.
♪ (sounds pitch down) ♪
Modules also have snapshots, so I can go here:
♪ (sounds morph to a new snapshot) ♪
And get pre-saved configurations of, in this case,
the oscillators in my Gen module.
♪ (sounds morph to a new snapshot) ♪
And you can hear them gliding to their new values.
That's controlled by this Morph time, so I can set it to
instant and immediately jump to a new snapshot.
♪ (new sonic snapshots) ♪
The Morph time also affects my favorite
feature of Atelier, which is the randomization.
You can hit a die icon to randomize a module.
Before I do that, though, I'm
going to lock all the gain controls,
because I don't want gain to randomize.
Very easy to just blast your
ears when you randomize volume.
But now let's hit the die.
♪ (wildly different sound profiles) ♪
You can also hover over any individual parameter
and press R...
♪♪
to just instantly randomize it.
♪ (more randomization) ♪
Obviously, though, the most fun
is when you use the global random,
where literally all things can be randomized at once.
♪ (birds-in-a-jungle-like sounds) ♪
That's already a whole different thing.
I'm also going to turn up the morph time so we can have
some fun hearing it reach those changes.
And let's increase the randomization amount even further.
♪ (slowly morphing sound parameters with new soundscapes) ♪
Alright, let's do a shorter morph
time, and we'll go to 100% randomization.
♪ (randomizationnn) ♪
Aw yeah, we're in some alien insect territory.
I just wanna record this.
That's another feature.
Anytime you like something,
you can just hit record.
When you're done, hit it again.
Your recordings pop up here,
and if you're using Atelier as a plugin,
you can drag these audio files to your DAW
and if you're in the stand-alone,
you can just drag them in
and it will load them into a new Play module.
which is their sampler.
And it's also kind of granular and...we'll get to it later.
All right, before we go, I got to hit random one more time.
♪ (Andrew hits random 16,000 more times) ♪
♪ (chirpy whirly sounds) ♪
There are only three modulator options.
They've ingeniously crafted them to contain almost any type
of modulation that you might want.
Agitation is for random.
So if I drag this to the pitch of our cursor,
dial in the range.
This goes as high as plus or minus 200%, by the way.
And we get random modulation to the pitch.
You can have it more steppy:
♪ (slower stepping) ♪
Or more smoothed:
♪♪
Slant adjusts the ratio of time spent going up versus down.
And at 0%, of course, they're equal.
And this control for how cyclic it is basically turns it
into a repeatable LFO or, you know,
you can get more amounts of randomness.
♪ (changing cyclic pulse) ♪
And then jitter randomizes the amount of time
that you're going to have between two steps.
♪ (jittering pulse) ♪
Before I look at the other modulators,
now that we've seen how one works,
let me just talk about how amazing modulation is
in Atelier because they've come up
with some really clever ideas.
So first of all, modulation is polyadic.
And what that means is every single modulation routing
can have a unique signal.
So let me pull this one down here
and we'll add another cursor.
♪♪
So now we've got left and right.
Modulation is going to just one cursor.
If I drag the exact same modulation to pitch
on the second cursor, and let's rein that pitch in.
♪♪
You can see it's getting the same type of modulation,
but the signal itself is actually different.
If they were the same signal,
then these pitches would be jumping around
in exactly the same timing, which you can do, by the way,
you could turn off the polyadic response.
So now here, all modulations coming out
of this agitation module will be identical,
even though for each one,
you can still scale them individually.
♪♪
So as an example of how powerful polyadic patching is,
here I only have seven modulation modules.
I've used 30 wires
and I have over 150 unique modulation signals.
♪♪
Let's pull up a peak modulator.
We will again route this to the pitch of our cursor,
scale it back a bit.
♪♪
And now you can see I've got this one-shot modulation,
which of course you can assign to a MIDI controller
or whatever if you want, but I can also make it looping.
♪ (looping chirps) ♪
I can give it a sustain stage,
so whatever I'm triggering it with,
it stays on that high value until I let go.
♪♪
Let's go back to looping for a sec
and take a look at some extra controls.
You can set the delay between each repeat of a modulation.
So where time affects the timing
of that modulation shape itself,
delay can put space in between those.
♪ (pulse pitching up and down) ♪
And then you also have this repeats control.
So the time amount will stay constant,
but it will fit more repeats into that same amount of time.
♪ (beepy pulse increases speed) ♪
And then here, this die icon is not for randomization,
but it's for the chance that the modulation will fire.
♪ (more randomized pulsing) ♪
All right, now let's look at the last modulator,
which is control, which is basically a fader.
And you can map this to external hardware if you want,
but with some interesting added ideas for a fader,
you can smooth the response.
♪ (pitch sliding way up and way down...smoothly) ♪
So that is a little bit of lag when I drag it around.
♪ (pitch sliding way up and way down...smoothly) ♪
Now delay and loop are very odd.
So delay sets a lag between when you move the slider
and when it actually responds.
♪ (pitch sliding way up and way down) ♪
And then loop sets how much of your movements
will come back and be layered again on the output.
So I'll just move it once.
♪ (wobbling pulse) ♪
And then it'll kind of echo.
♪♪
More cool stuff about modulators,
you can sum and scale as many as you want
to the same destination.
So let's drag an agitation up here.
♪♪
And I forgot to show you earlier, actually,
you can scale all of the outgoing modulation
with this slider.
♪♪
Let's add to that this peak modulation.
So you can hear I've got my pitch slowly, randomly drifting
up and down while I'm also laser beaming it.
♪ (drifting pitch with laser beamy stabs) ♪
And you can combine as much
modulation as you want this way.
And of course you can hover over things
to adjust the individual amounts.
And I actually just realized I meant to drag these
to the pitch, but I dragged them to the cursor,
but that is great because I almost forgot
I wanted to show you.
Dragging something to a cursor means you're assigning
the modulation to all of that cursor's parameters.
I'll also mention there's a shortcut key W.
Anytime you hold that down, it shows all of your wires.
I'm assuming W is what that stands for.
And of course modulators themselves can be modulated.
And this is also polyadic.
So if you modulate a modulator,
which is modulating a bunch of things,
each of those outgoing modulations will be receiving
a different modulation to itself.
I've just said the word 'modulation' so many times,
but I hope you...get...what I mean.
♪ (clicky swishy sounds) ♪
I did a lot of the earlier demonstrating using GRMGen,
which is basically your oscillator.
And in a lot of ways it's a very standard oscillator.
You can mix your different waveforms
and each one has a timbre control.
♪ (muted wind-like sound) ♪
♪♪
You also get this combination slider
where you can either duck the oscillator
with incoming audio:
♪♪
Or you can have its volume
follow the volume of the incoming audio:
♪♪
And next let's look at this module GRMPlay
where you can load or record samples.
Moving the cursor around fluidly adjusts its pitch
and speed.
♪ (dynamic percussive sounds) ♪
Let's add another cursor:
♪ (percussion) ♪
Hit play on that:
♪ (faster percussion) ♪
Now we've got our stereo spread happening.
♪ (faster percussion) ♪
I feel like I can adjust a lot of this stuff
and you can understand what's going on
based on the very clear visualization.
♪♪
Zeroing in on a little window here:
♪♪
moving that window around.
♪♪
Now obviously I've got these looping,
but you can also just one shot them.
We can do them both at once up here.
I could play them individually
and we could throw a bunch of modulation at these
and see what happens.
♪ (changing, burbling percussive hits) ♪
Like do you see how fun this is and how wild it is
and how fluidly it all works?
♪ (sonic insanity) ♪
Next we have a comb filter, which is simple but powerful.
Cursors have pitch on the X axis and decay on the Y.
And then you have different ways
to adjust the response of the partials.
♪ (jittering sonic soup) ♪
So you can make anything resonate
like even these simple clicky sounds can become chords.
♪ (plucky notes) ♪
Or you can modulate it
and even simple clicky sounds can become this:
♪ (lasery, almost synth-like sounds) ♪
Let's look at GRMBand, basically an EQ.
Check this out though:
♪ (pulse drops out) ♪
You adjust the width of a notch or going this way,
you can narrow it down to a band.
♪♪
And then I think you can just visually see
what these controls are doing.
And of course, when you have multiple cursors,
then you're getting different processing
through different channels.
So like here's some interesting stereo effects happening
when my bands have different settings
or different modulation.
♪♪
Let's look at GRMPitch and for this one,
let's go to an individual pitch as our source sound.
And now each cursor will play back
a pitch shifted version of this signal.
And while pitch is on the Y axis,
on the X you get a delay.
So the input audio has to reach each cursor
for each of those pitch shifts to occur.
♪ (soft xylophone-like sounds) ♪
And there's feedback.
So the pitch shift keeps getting reapplied
and here I'm using the rotate parameter
to route each channel's feedback to the next channel.
♪♪
Pretty cool idea.
Can you imagine this with a multi-speaker setup
and tons of cursors each going to their own channel?
Just wild.
Adjusting the ratio is fun:
♪♪
Oh, and there are also freeze buttons
for individual play heads.
♪♪
And while frozen, some parameters
will still have some effect:
♪ (wobbling tone) ♪
GRMTime is next and this is basically a delay.
Let's change up our input sound again:
♪ (digital-sounding chord swooping up repeatedly) ♪
and I'll turn the delay mix up.
♪ (pulsing chord) ♪
♪ (pulsing chord...getting weirder) ♪
So you can hear I've got this nice stereo delay.
♪ (nice stereo delay) ♪
Let me show you the bandpassing:
♪♪
where of course you can adjust the cutoff:
♪♪
And if you have multiple
cursors, this can sound really nice.
♪♪
Speed adjusts kind of the virtual tape of the delay.
♪♪
So our tape can crawl all the way to a stop.
Now we have what appears to be
a very simple volume slider gain.
There's a cool thing that they've done here though
which is I'm adding these muffle and distance controls:
♪♪
which mean that as you turn down a track,
♪♪
it becomes darker.
Or with distance:
♪♪
It seems to get further away.
♪♪
So it's this interesting kind of naturalistic approach
to a fader.
♪♪
Because it's not just volume dropping.
♪ (fading away) ♪
It really can feel like something's getting quieter
which I know sounds like the exact same thing.
But having this option to have things fade out
in this more kind of real-world-sounding way
is just a brilliant little touch.
And then you additionally have a trim control.
And so that one is just always volume up or down
not affected by muffle and distance.
♪♪
And then last we have Viz.
A beautiful scope.
This one has elements that are resizable.
So you can really just see what you wanna see,
whether it's spatialization or frequency,
got a lot of different options.
You can turn on and off different channels.
Actually for funsies,
let's turn back on my additional output channels.
Look!
Colors!
So it really is one of those tools
that just makes you think why didn't this exist before?
All of the modules totally fit in the lineage
of experimental electronic music
but they've just been redesigned and rethought
for how people actually interact with software
and not wanting to recreate a vintage synthesizer
on your screen.
And it's just so much fun.
So congrats to GRM.
Check their link in the description
and I will see you in the next video.
(whoosh)
♪ (soft pulsing chord) ♪
I totally forgot one little thing that I wanna show:
If you hold the command key and move anything,
♪ (warpy sound) ♪
you get a little elastic band!
♪ (warpyyyyy) ♪