---
title: "Battery 4: Push2, Rename Piano Roll, Routing, Preview - Ableton Forum"
source: "https://forum.ableton.com/viewtopic.php?t=244078"
author:
published:
created: 2025-03-29
description:
tags:
  - "clippings"
---
## [Battery 4: Push2, Rename Piano Roll, Routing, Preview](https://forum.ableton.com/viewtopic.php?t=244078&sid=93fd46da18084b3f733093523ae1dbbe)

[Post Reply](https://forum.ableton.com/posting.php?mode=reply&t=244078&sid=93fd46da18084b3f733093523ae1dbbe "Post a reply")

- [Print view](https://forum.ableton.com/viewtopic.php?t=244078&sid=93fd46da18084b3f733093523ae1dbbe&view=print "Print view")

  [Advanced search](https://forum.ableton.com/search.php?sid=93fd46da18084b3f733093523ae1dbbe "Advanced search")   

1 post • Page **1** of **1**

[SteddieBop](https://forum.ableton.com/memberlist.php?mode=viewprofile&u=307515&sid=93fd46da18084b3f733093523ae1dbbe)

**Posts:** [1](https://forum.ableton.com/search.php?author_id=307515&sr=posts&sid=93fd46da18084b3f733093523ae1dbbe)

**Joined:** Sat Nov 06, 2021 3:05 am

### [Battery 4: Push2, Rename Piano Roll, Routing, Preview](https://forum.ableton.com/?t=244078#p1796285)

- [Quote](https://forum.ableton.com/posting.php?mode=quote&p=1796285&sid=93fd46da18084b3f733093523ae1dbbe "Reply with quote")
- [Post](https://forum.ableton.com/viewtopic.php?p=1796285&sid=93fd46da18084b3f733093523ae1dbbe#p1796285 "Post") by **[SteddieBop](https://forum.ableton.com/memberlist.php?mode=viewprofile&u=307515&sid=93fd46da18084b3f733093523ae1dbbe)** » Sat Nov 06, 2021 4:05 am

Hey everyone,  
  
First post here! Id like to share this with you all. I made a rack that allows you to use a drum rack to trigger a third party plug-in like Battery, Kontakt, Reaktor, Slate Drums. Through this setup I was able to accomplish the following:  
  
1.) "Full" Integration with Push's usual drum rack work flow. (sequencer, 64 pad)  
2.) You can rename the piano roll to the specific samples in each notes drum rack cell.  
3.) You can trigger third party plugins through the drum rack note cell play button.  
4.) Sets up channel's receiving all of Battery Drum's individual output. This setup is nice because if you want to send the kick, snare to an individual track for post processing.. It is there and ready.  
  
**Initial Setup**  
Create a Midi Channel with a drum rack on it, and drop an instance of whatever plugin you want to do this to in C1.  
Show your chain list from the left side of drum rack, the click the IO button that appears under it.  
Once your Chains & IO is showing, go to the "Receive" box to the right of your plugin, click on it and select "All Notes"  
  
Now you have prepped the drum rack to start assigning each cell an individual note. This lets you preview the sample in a specific note in the third party plugin.  
  
**Configuring Each Individual Pad To Send 1 MIDI Note To The Plug-In**  
Drop an external Instrument on C1. Before we configure the instrument, go into the new external instrument chain. We see that "Receive" Is Set to the note of the cell you're configuring, but the "Play" Parameter most likely shows C3. Make The "Play" Parameter match the "Receive" parameter. Lastly, Rename that chain the note in the cell you just set up (C1).  
  
Now back to the external instrument... for "MIDI To" select the track you're working in from the drop down. Leave the "Audio From" to 3/4 but **make SURE you turn the gain all the way down.** Leaving the gain turned up will negatively affect the routing portion that is coming up.  
  
The setup for this note is complete. Copy that cell using option+click drag to the cell C#1. The only change you need to make is to make the "Play" value match the "Receive" parameter in the chain list and rename it to the new note (C#1).  
  
Do this for everything C1 and Higher.  
  
**Prepping Audio Tracks To Accept Routed Audio Out Of Battery**  
In the drum rack instrument itself, on the overview grid on the left, I selected the unused cells under all of the cells I just set up.  
Then I dropped an External instrument on G#-1. Set The "Midi To" to the track You're currently on. and the "Audio From" Will be a pair of outputs from your plugin. Leave the gain at 0.00dB. Repeat this process on another drum rack cell and switch the "Audio From" to the next pair of outputs from your plugin. Continue repeating until you've prepped tracks for all the available outputs from your plug-in.  
  
This was long winded, but I really hope it helps. If anyone likes this and has ideas on how to improve it.. please respond to this thread or message me! This solution has made working with Third Party Plugs in Push2 so much more inspiring.  
  
Here is a video to supplement everything I just typed and should bring it full circle:  
[https://www.dropbox.com/s/w5h9pggv8o1xi ... M.mov?dl=0](https://www.dropbox.com/s/w5h9pggv8o1xisu/Video%20Nov%2002%2C%204%2017%2030%20PM.mov?dl=0)  
  
Hope this helps!  
Ed Rudnesky ![8)](https://forum.ableton.com/images/smilies/icon_cool.gif "Cool")