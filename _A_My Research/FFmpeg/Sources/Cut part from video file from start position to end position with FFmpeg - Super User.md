---
tags:
  - notebooklm-import
notebook: "FFmpeg"
category: "research"
---

Cut part from video file from start position to end position with FFmpeg - Super User
By clicking “Sign up”, you agree to our [terms of service](https://superuser.com/legal/terms-of-service/public) and acknowledge you have read our [privacy policy](https://superuser.com/legal/privacy-policy).
Sign up with Google

### OR

Email
Password
Sign up
Already have an account? [Log in](https://superuser.com/users/login)
[Skip to main content](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#content)
1.

```
1. [Home](https://superuser.com/)
2. [Questions](https://superuser.com/questions)
3. [Unanswered](https://superuser.com/unanswered)
4. [AI Assist](https://stackoverflow.com/ai-assist)
5. [Tags](https://superuser.com/tags)
6.
7. [Chat](https://chat.stackexchange.com/)
8. [Users](https://superuser.com/users)
9.
10. [Companies](https://stackoverflow.com/jobs/companies?so_medium=superuser&so_source=SiteNav)
```

```
1. Stack Internal Stack Overflow for Teams is now called  **Stack Internal** . Bring the best of human thought and AI automation together at your work. [Try for free](https://stackoverflowteams.com/teams/create/free/?utm_medium=referral&utm_source=superuser-community&utm_campaign=side-bar&utm_content=explore-teams) [Learn more](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=superuser-community&utm_campaign=side-bar&utm_content=explore-teams)
1. [Stack Internal](javascript:void(0))
1. Bring the best of human thought and AI automation together at your work. [Learn more](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=superuser-community&utm_campaign=side-bar&utm_content=explore-teams-compact)
```

**Stack Internal**
Knowledge at work
Bring the best of human thought and AI automation together at your work.
[Explore Stack Internal](https://stackoverflow.co/internal/?utm_medium=referral&utm_source=superuser-community&utm_campaign=side-bar&utm_content=explore-teams-compact-popover)

###### Stack Exchange Network

Stack Exchange network consists of 183 Q&A communities including [Stack Overflow](https://stackoverflow.com/), the largest, most trusted online community for developers to learn, share their knowledge, and build their careers.
[Visit Stack Exchange](https://stackexchange.com/)
Loading…
\* [Tour Start here for a quick overview of the site](https://superuser.com/tour)
\* [Help Center Detailed answers to any questions you might have](https://superuser.com/help)
\* [Meta Discuss the workings and policies of this site](https://meta.superuser.com/)
\* [About Us Learn more about Stack Overflow the company, and our products](https://stackoverflow.co/)

##### [current community](https://superuser.com/)

```
*  [Super User](https://superuser.com/) [help](https://superuser.com/help) [chat](https://chat.stackexchange.com?tab=site&host=superuser.com)
    *  [Meta Super User](https://meta.superuser.com/)
```

##### your communities

[Sign up](https://superuser.com/users/signup?ssrc=site_switcher&returnurl=https%3a%2f%2fsuperuser.com%2fquestions%2f377343%2fcut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg) or [log in](https://superuser.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fsuperuser.com%2fquestions%2f377343%2fcut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg) to customize your list.

##### [more stack exchange communities](https://stackexchange.com/sites)

[company blog](https://stackoverflow.blog/) 4. 5. [Log in](https://superuser.com/users/login?ssrc=head&returnurl=https%3a%2f%2fsuperuser.com%2fquestions%2f377343%2fcut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg) 6. [Sign up](https://superuser.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fsuperuser.com%2fquestions%2f377343%2fcut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg)

### [Cut part from video file from start position to end position with FFmpeg \[duplicate\]](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg)

[Ask Question](https://superuser.com/questions/ask)
Asked 14 years, 3 months ago
Modified [6 months ago](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg?lastactivity)
Viewed 510k times
This question shows research effort; it is useful and clear
268
Save this question. 
Show activity on this post.
**This question already has answers here** :
[How to use FFmpeg to cut up a video?](https://superuser.com/questions/138331/how-to-use-ffmpeg-to-cut-up-a-video) (11 answers)
Closed 9 years ago.
I have a video file of 30 minutes, but I want to extract a video from 00:09:23 to 00:25:33.
I can define the startposition with -ss , but I couldn't find one for the end position. Any help please?
\* [ffmpeg](https://superuser.com/questions/tagged/ffmpeg)
\* [video-editing](https://superuser.com/questions/tagged/video-editing)
[Share](https://superuser.com/q/377343)
Share a link to this question https://superuser.com/q/377343
Copy link [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
[Improve this question](https://superuser.com/posts/377343/edit)
Follow
Follow this question to receive notifications
[edited Oct 9, 2012 at 16:19](https://superuser.com/posts/377343/revisions)
[slhck](https://superuser.com/users/48078/slhck)
237k 73 73 gold badges 640 640 silver badges 611 611 bronze badges
asked Jan 11, 2012 at 17:59
[x74x61](https://superuser.com/users/113191/x74x61)
3,101 4 4 gold badges 19 19 silver badges 7 7 bronze badges
0
[Add a comment](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg) |

#### 6 Answers 6

Sorted by: [Reset to default](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg?answertab=scoredesc#tab-top)
Highest score (default)
Date modified (newest first)
Date created (oldest first)
This answer is useful
424
Save this answer. 
Show activity on this post.

##### Install ffmpeg

Make sure you [download a recent version of ffmpeg](http://ffmpeg.org/download.html) , and don't use the one that comes with your distribution (e.g. Ubuntu). Packaged versions from various distributions are often outdated and do not behave as expected.
Or [compile it yourself](https://trac.ffmpeg.org/wiki/CompilationGuide). Under macOS, you can [use Homebrew](https://brew.sh/) and brew install ffmpeg .

##### How to cut a video, without re-encoding

Use this to cut video from [start] for [duration] :

```
ffmpeg -ss [start] -i in.mp4 -t [duration] -map 0 -c copy out.mp4
```

Use this to cut video from [start] to [end] :

```
ffmpeg -copyts -ss [start] -i in.mp4 -to [end] -map 0 -c copy out.mp4
```

##### Explaining the options

The options mean the following:
\* [-ss](http://ffmpeg.org/ffmpeg-all.html#Main-options) specifies the start time, e.g. 00:01:23.000 or 83 (in seconds)
\* [-t](http://ffmpeg.org/ffmpeg-all.html#Main-options) specifies the duration of the clip. The format of the time is the same.
\* Instead of -t , you can also use [-to](http://ffmpeg.org/ffmpeg-all.html#Main-options) , which specifies the end time.
\* -map 0 maps all streams: audio, video and subtitles
\* [-copyts](http://ffmpeg.org/ffmpeg-all.html#Main-options) preserves the original timestamps from the input file
\* [-c copy](http://ffmpeg.org/ffmpeg-all.html#Main-options) copies the first video, audio, and subtitle bitstream from the input to the output file without re-encoding them. This won't harm the quality and make the command run within seconds.
**Important note about -copyts :** By default, ffmpeg resets timestamps to start from 0 after seeking with -ss . When you use -copyts , the original timestamps are preserved, which makes -to work as expected (specifying the absolute end time from the original file). Without -copyts , the -to parameter behaves unexpectedly because it operates on the reset timeline.
For example:

```
ffmpeg -ss 5 -i in.mp4 -t 30 -map 0 -c copy out.mp4
```

This seeks forward in the input by 5 seconds and generates a 30-second long output file. In other words, you get the input video's part from 5–35 seconds.
**Without -copyts (timestamps reset to 0):**

```
ffmpeg -ss 5 -i in.mp4 -to 30 -map 0 -c copy out.mp4
```

This does NOT give you 5–35 seconds as you might expect. Instead, it gives you a 30-second output because the timestamps are reset to 0 after the initial seek, making -to 30 equivalent to -t 30 .
**With -copyts (preserves original timestamps):**

```
ffmpeg -copyts -ss 5 -i in.mp4 -to 35 -map 0 -c copy out.mp4
```

This correctly gives you the part from 5–35 seconds (30 seconds total) because -copyts preserves the original timeline, allowing -to 35 to work intuitively.
**Do you need timestamps starting at 0?** The -copyts approach creates output files where timestamps don't start at 0 (they preserve the original timeline). For most playback scenarios, this works fine. However, if you need timestamps starting exactly at 0 (for editing workflows, concatenation, or certain streaming platforms), you can add a second pass:

```
ffmpeg -copyts -ss 5 -i in.mp4 -to 35 -map 0 -c copy temp.mp4
ffmpeg -i temp.mp4 -c copy out.mp4
rm temp.mp4
```

For more info on seeking, see <https://trac.ffmpeg.org/wiki/Seeking>

##### How to cut a video, with re-encoding

Sometimes, using -c copy leads to output files that some players cannot process (they'll show a black frame or have audio-video sync errors).
If you leave out the -c copy option, ffmpeg will automatically re-encode the output video and audio according to the format you chose. For high quality video and audio, read the [x264 Encoding Guide](https://ffmpeg.org/trac/ffmpeg/wiki/x264EncodingGuide) and the [AAC Encoding Guide](http://ffmpeg.org/trac/ffmpeg/wiki/AACEncodingGuide), respectively.
For example:

```
ffmpeg -ss [start] -i in.mp4 -t [duration] -c:v libx264 -crf 23 -c:a aac -b:a 192k out.mp4
```

You can change the CRF and audio bitrate parameters to vary the output quality. Lower CRF means better quality, and vice-versa. Sane values are between 18 and 28.
[Share](https://superuser.com/a/377407)
Share a link to this answer https://superuser.com/a/377407
Copy link [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
[Improve this answer](https://superuser.com/posts/377407/edit)
Follow
Follow this answer to receive notifications
[edited Sep 15, 2025 at 9:57](https://superuser.com/posts/377407/revisions)
answered Jan 11, 2012 at 21:02
[slhck](https://superuser.com/users/48078/slhck)
237k 73 73 gold badges 640 640 silver badges 611 611 bronze badges
38
\* 1 On ubuntu 12:10, -c:v and -c:a didn't work. I had to use "-acodec copy and -vcodec copy" instead. Samuel Lampa – [Samuel Lampa](https://superuser.com/users/83959/samuel-lampa) 2013-04-02 14:21:47 +00:00 [Commented Apr 2, 2013 at 14:21](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment705290_377407)
\* 2 Thanks for this! if you don't specify a duration, will it go to the end? Jeff – [Jeff](https://superuser.com/users/113575/jeff) 2014-03-31 17:03:07 +00:00 [Commented Mar 31, 2014 at 17:03](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment945554_377407)
\* 8 @Prateek When copying the video bitstream (instead of re-encoding), you can only cut at [keyframes](https://en.wikipedia.org/wiki/Video_compression_picture_types#Intra_coded_frames.2Fslices_.28I.E2.80.91frames.2Fslices_or_Key_frames.29). If there are keyframes at seconds 1, 2, and 3, but you want to cut at second 1.5, then ffmpeg will wait until second 2 before it can start cutting. That makes it inaccurate. slhck – [slhck](https://superuser.com/users/48078/slhck) 2015-07-03 12:36:36 +00:00 [Commented Jul 3, 2015 at 12:36](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment1270628_377407)
\* 7 -to does not always "start from" -ss even without -copyts , @Maggyero I use to move the -to option to configure the input instead of the output so it is just another solution. ffmpeg -ss [start] -to [stop] -i in.mp4 -c copy out.mp4 Like this my stop time is correct despite the start time. I wonder if it is also the reason why @lustig moved -ss to the output while they did not know why. The answer does not even mention -copyts ! It should, as it is the simplest solution here ! I prefer reordering the arguments, but i guess it is not simpler. Link-akro – [Link-akro](https://superuser.com/users/549957/link-akro) 2020-08-23 08:54:49 +00:00 [Commented Aug 23, 2020 at 8:54](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment2406698_377407)
\* 2 I'm still getting a clip that is of duration length unfortunately. For example, when I try ffmpeg -copyts -ss 00:00:03.633 -i input.mp4 -to 00:00:04.166 -c:v libx264 -crf 23 -c:a aac -b:a 192k output.mp4 - I get a clip that is 4.166 seconds long and I want the duration to be the difference between 4.166 - 3.633, which is about half a second. In addition the clip is blank, but I'm trying to get the length correct first kraftydevil – [kraftydevil](https://superuser.com/users/379229/kraftydevil) 2023-04-14 21:27:46 +00:00 [Commented Apr 14, 2023 at 21:27](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment2776604_377407)
| [Show 33 more comments](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg)
This answer is useful
55
Save this answer. 
Show activity on this post.
I think you can use the following command now.

```
ffmpeg -i inputFile -vcodec copy -acodec copy -ss 00:09:23 -to 00:25:33 outputFile
```

Have a look also [ffmpeg Doc](https://ffmpeg.org/ffmpeg.html), or [this wiki page](https://trac.ffmpeg.org/wiki/Seeking#Cuttingsmallsections).
[Share](https://superuser.com/a/911725)
Share a link to this answer https://superuser.com/a/911725
Copy link [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
[Improve this answer](https://superuser.com/posts/911725/edit)
Follow
Follow this answer to receive notifications
[edited Aug 21, 2016 at 4:14](https://superuser.com/posts/911725/revisions)
[rsalmond](https://superuser.com/users/528744/rsalmond)
103 3 3 bronze badges
answered May 7, 2015 at 2:30
[sflee](https://superuser.com/users/327808/sflee)
651 5 5 silver badges 4 4 bronze badges
8
\* 16 ffmpeg -i inputFile -c copy -ss 00:09:23 -to 00:25:33 outputFile simpler version nwgat – [nwgat](https://superuser.com/users/89515/nwgat) 2016-11-20 16:37:57 +00:00 [Commented Nov 20, 2016 at 16:37](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment1649870_911725)
\* 6 I had to use ffmpeg -ss 00:01:00 -i video.mp4 -to 00:02:00 -c copy -copyts cut.mp4 version (with -copyts ), otherwise it cut incorrectly (with black screen in the beginning). Thanks for the 2nd link though. Necronomicron – [Necronomicron](https://superuser.com/users/278537/necronomicron) 2018-01-12 15:51:55 +00:00 [Commented Jan 12, 2018 at 15:51](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment1900215_911725)
\* 3 This is great, the last thing I wanted was calculating the duration from endpoints. Tomasz Gandor – [Tomasz Gandor](https://superuser.com/users/269542/tomasz-gandor) 2018-05-11 09:50:02 +00:00 [Commented May 11, 2018 at 9:50](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment1969969_911725)
\* 2 The -to option answers the question that was actually asked. The rest of the answers are either impertinent or obsolete. James Bowery – [James Bowery](https://superuser.com/users/780183/james-bowery) 2018-05-15 15:35:35 +00:00 [Commented May 15, 2018 at 15:35](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment1972078_911725)
\* @Necronomicron but timestamps may not be appropriate with that variant. jarno – [jarno](https://superuser.com/users/490855/jarno) 2020-04-02 23:33:50 +00:00 [Commented Apr 2, 2020 at 23:33](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment2335982_911725)
| [Show 3 more comments](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg)
This answer is useful
28
Save this answer. 
Show activity on this post.
This is odd that no-one suggested the trim [filter](https://ffmpeg.org/ffmpeg-filters.html#trim).
Drop everything except the second minute of input:

```
ffmpeg -i INPUT -vf trim=60:120
```

Keep only the first second:

```
ffmpeg -i INPUT -vf trim=duration=1
```

Drop everything except from second 13 to second 58:

```
ffmpeg -i INPUT -vf trim=13:58 OUTPUT
```

[Share](https://superuser.com/a/898765)
Share a link to this answer https://superuser.com/a/898765
Copy link [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
[Improve this answer](https://superuser.com/posts/898765/edit)
Follow
Follow this answer to receive notifications
answered Apr 7, 2015 at 15:10
[malat](https://superuser.com/users/106444/malat)
1,384 2 2 gold badges 18 18 silver badges 39 39 bronze badges
5
\* 29 Yes, good to mention trim and atrim . I usually use these when filtering, but users should note that **filtering requires re-encoding** . llogan – [llogan](https://superuser.com/users/110524/llogan) 2015-04-07 17:28:14 +00:00 [Commented Apr 7, 2015 at 17:28](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment1204315_898765)
\* You are my hero. I badly needed a filter that did this. fahadash – [fahadash](https://superuser.com/users/341154/fahadash) 2016-12-24 05:55:14 +00:00 [Commented Dec 24, 2016 at 5:55](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment1670696_898765)
\* Is this losless or does this re-encode the video? fap – [fap](https://superuser.com/users/669906/fap) 2021-12-08 19:10:54 +00:00 [Commented Dec 8, 2021 at 19:10](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment2601655_898765)
\* 1 @fap The comment above yours literally answers this. Hashim Aziz – [Hashim Aziz](https://superuser.com/users/323079/hashim-aziz) 2022-07-22 15:44:22 +00:00 [Commented Jul 22, 2022 at 15:44](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment2681315_898765)
\* The trim filter also takes named arguments start and end . Using named arguments lets you omit the others, as in trim=end=X (from start to X) and trim=start=X (from X to end). If you want a colon in X (e.g., the time 5:39), you need to escape it, as in trim=end=5:39 so that it doesn't get interpreted as the field separator. BallpointBen – [BallpointBen](https://superuser.com/users/587619/ballpointben) 2023-06-22 20:31:38 +00:00 [Commented Jun 22, 2023 at 20:31](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment2801782_898765)
[Add a comment](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg) |
This answer is useful
11
Save this answer. 
Show activity on this post.
You can use these [two methods which work for Windows and Linux.](http://www.compmiscellanea.com/en/split-video-file-ffmpeg.htm)
There are two ways how to split video files by ffmpeg. The first one is good in itself, more than that - it is faster, but sometimes creates output files with certain flaws. So for those cases there is the second way of splitting video files: it is considerably slower, the output files are bigger, but it seems they are always of the same quality level as input files used.
**Way 1:**

```
ffmpeg -ss  -i in1.avi -t  -c copy out1.avi
```

**Way 2:**

```
ffmpeg -ss  -i in1.avi -t  out1.avi
```

```
*   – the beginning of the part of a video ffmpeg is to cut out. Format: 00:00:00.0000 , meaning hours:minutes:seconds:milliseconds.
*   – the duration of the part of a video ffmpeg is to cut out. Same format as above.
```

**Examples:**

```
ffmpeg -ss 01:19:00 -i in1.avi -t 00:05:00 -c copy out1.avi
ffmpeg -ss 01:19:00 -i in1.avi -t 00:05:00 out1.avi
```

ffmpeg cuts out a part of the video file starting from 1 hour 19 minutes 0 seconds. The duration of the video sequence cut out is 5 minutes 0 seconds.
[Share](https://superuser.com/a/654048)
Share a link to this answer https://superuser.com/a/654048
Copy link [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
[Improve this answer](https://superuser.com/posts/654048/edit)
Follow
Follow this answer to receive notifications
[edited Jun 12, 2020 at 13:48](https://superuser.com/posts/654048/revisions)
[Community](https://superuser.com/users/-1/community) Bot
1
answered Oct 3, 2013 at 19:08
[Christian](https://superuser.com/users/255659/christian)
7,225 1 1 gold badge 28 28 silver badges 39 39 bronze badges
3
\* Ok, thnx. Will check out the docs and give it a try tomorrow. juGGaKNot – [juGGaKNot](https://superuser.com/users/259638/juggaknot) 2013-10-03 19:18:00 +00:00 [Commented Oct 3, 2013 at 19:18](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment823767_654048)
\* 3 [-sameq does not mean "same quality"](http://superuser.com/a/478550/110524) and has been removed from ffmpeg. Use -codec copy instead. Also, don't forget about the -to option. llogan – [llogan](https://superuser.com/users/110524/llogan) 2013-10-03 20:47:52 +00:00 [Commented Oct 3, 2013 at 20:47](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment823836_654048)
\* 1 I corrected the commands in your quote, as they were quite outdated. Please don't copy-paste information without properly quoting it. slhck – [slhck](https://superuser.com/users/48078/slhck) 2013-10-04 10:08:00 +00:00 [Commented Oct 4, 2013 at 10:08](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment824088_654048)
[Add a comment](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg) |
This answer is useful
-3
Save this answer. 
Show activity on this post.
I use the following syntax to cut video with ffmpef: ffmpeg -sameq -ss [start\_seconds] -t [duration\_seconds] -i [input\_file] [outputfile]
-t is used to set the duration in seconds - you can't specify the end time but this should work for you.
[Share](https://superuser.com/a/377350)
Share a link to this answer https://superuser.com/a/377350
Copy link [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
[Improve this answer](https://superuser.com/posts/377350/edit)
Follow
Follow this answer to receive notifications
answered Jan 11, 2012 at 18:27
[Michael Banzon](https://superuser.com/users/108612/michael-banzon)
115 2 2 bronze badges
1
\* 1 Why are you setting FFmpeg to re-encode the file? Note that -sameq does not mean "same quality" at all. slhck – [slhck](https://superuser.com/users/48078/slhck) 2012-01-11 21:18:01 +00:00 [Commented Jan 11, 2012 at 21:18](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment423090_377350)
[Add a comment](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg) |
This answer is useful
-3
Save this answer. 
Show activity on this post.
You can use this

```
ffmpeg -sameq -ss clip_start -t duration  -i  original.ogg  clip.ogg
```

Here you have to give duration of video. ie. 00:25:33-00:09:23
[Share](https://superuser.com/a/377352)
Share a link to this answer https://superuser.com/a/377352
Copy link [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
[Improve this answer](https://superuser.com/posts/377352/edit)
Follow
Follow this answer to receive notifications
answered Jan 11, 2012 at 18:29
[daya](https://superuser.com/users/112568/daya)
2,629 19 19 silver badges 19 19 bronze badges
1
\* 1 As I mentioned on the other answer: With your command, you're re-encoding the file, which is absolutely not necessary and results in reduced quality and increased processing time. slhck – [slhck](https://superuser.com/users/48078/slhck) 2012-01-11 21:18:49 +00:00 [Commented Jan 11, 2012 at 21:18](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg#comment423092_377352)
[Add a comment](https://superuser.com/questions/377343/cut-part-from-video-file-from-start-position-to-end-position-with-ffmpeg) |
Start asking to get answers
Find the answer to your question by asking.
[Ask question](https://superuser.com/questions/ask)
Explore related questions
\* [ffmpeg](https://superuser.com/questions/tagged/ffmpeg)
\* [video-editing](https://superuser.com/questions/tagged/video-editing)
See similar questions with these tags.
\* The Overflow Blog
\* [Gen Z needs a knowledge base (and so do you)](https://stackoverflow.blog/2026/04/09/gen-z-needs-a-knowledge-base-and-so-do-you/?cb=1)
\* [He designed C++ to solve your code problems](https://stackoverflow.blog/2026/04/07/he-designed-c-to-solve-your-code-problems/?cb=1)
Report this ad

###### Linked

[625](https://superuser.com/questions/138331/how-to-use-ffmpeg-to-cut-up-a-video?lq=1)
[How to use FFmpeg to cut up a video?](https://superuser.com/questions/138331/how-to-use-ffmpeg-to-cut-up-a-video?noredirect=1&lq=1)
[1](https://superuser.com/questions/1347383/why-is-ffmpeg-video-splitting-of-595-600-seconds-slow-compared-to-0-5-seconds?lq=1)
[Why is FFmpeg video splitting of 595-600 seconds slow compared to 0-5 seconds?](https://superuser.com/questions/1347383/why-is-ffmpeg-video-splitting-of-595-600-seconds-slow-compared-to-0-5-seconds?noredirect=1&lq=1)
[1](https://superuser.com/questions/1389019/ffmpeg-how-to-extract-frames-of-a-video-at-a-certain-time-frame?lq=1)
[FFMPEG How to extract frames of a video at a certain time frame?](https://superuser.com/questions/1389019/ffmpeg-how-to-extract-frames-of-a-video-at-a-certain-time-frame?noredirect=1&lq=1)
[66](https://superuser.com/questions/459313/how-to-cut-at-exact-frames-using-ffmpeg?lq=1)
[How to cut at exact frames using ffmpeg?](https://superuser.com/questions/459313/how-to-cut-at-exact-frames-using-ffmpeg?noredirect=1&lq=1)
[32](https://superuser.com/questions/478549/what-is-the-sameq-or-same-quant-option-in-ffmpeg-does-it-mean-same-quality?lq=1)
[What is the "sameq" or "same\_quant" option in FFmpeg? Does it mean "same quality"?](https://superuser.com/questions/478549/what-is-the-sameq-or-same-quant-option-in-ffmpeg-does-it-mean-same-quality?noredirect=1&lq=1)
[4](https://superuser.com/questions/722247/how-can-i-remove-multiple-segments-from-a-video-while-keeping-the-audio?lq=1)
[How can I remove multiple segments from a video while keeping the audio?](https://superuser.com/questions/722247/how-can-i-remove-multiple-segments-from-a-video-while-keeping-the-audio?noredirect=1&lq=1)
[4](https://superuser.com/questions/1298954/how-to-split-video-files-upon-detected-change-in-resolution-ie-recorded-strea?lq=1)
[How to split video files upon detected change in resolution? (ie. recorded streams containing multiple widths)](https://superuser.com/questions/1298954/how-to-split-video-files-upon-detected-change-in-resolution-ie-recorded-strea?noredirect=1&lq=1)
[2](https://superuser.com/questions/1845652/trimming-a-video-using-ffmpeg-leads-to-black-screen?lq=1)
[Trimming a video using FFmpeg leads to black screen](https://superuser.com/questions/1845652/trimming-a-video-using-ffmpeg-leads-to-black-screen?noredirect=1&lq=1)
[1](https://superuser.com/questions/1844789/cutting-a-part-from-a-video-should-ss-be-before-i-or-after?lq=1)
[Cutting a part from a video: Should '-ss' be before 'i' or after?](https://superuser.com/questions/1844789/cutting-a-part-from-a-video-should-ss-be-before-i-or-after?noredirect=1&lq=1)
[0](https://superuser.com/questions/1042313/which-program-i-can-edit-video-cut-some-scenes-without-increasing-the-videos?lq=1)
[Which program I can edit video (cut some scenes) without increasing the video's size](https://superuser.com/questions/1042313/which-program-i-can-edit-video-cut-some-scenes-without-increasing-the-videos?noredirect=1&lq=1)
[See more linked questions](https://superuser.com/questions/linked/377343?lq=1)

###### Related

[3](https://superuser.com/questions/385303/unable-to-cut-out-part-of-video-with-ffmpeg?rq=1)
[Unable to cut out part of video with ffmpeg](https://superuser.com/questions/385303/unable-to-cut-out-part-of-video-with-ffmpeg?rq=1)
[2](https://superuser.com/questions/549316/linux-cut-video-from-end-position?rq=1)
[Linux - Cut video from end position](https://superuser.com/questions/549316/linux-cut-video-from-end-position?rq=1)
[5](https://superuser.com/questions/663731/find-video-file-position-using-an-image-match?rq=1)
[Find video file position using an image match](https://superuser.com/questions/663731/find-video-file-position-using-an-image-match?rq=1)
[0](https://superuser.com/questions/883378/how-do-i-cut-clips-using-its-position-from-a-video?rq=1)
[How do I cut clips using its position from a video?](https://superuser.com/questions/883378/how-do-i-cut-clips-using-its-position-from-a-video?rq=1)
[0](https://superuser.com/questions/1101557/cut-video-with-ffmpeg?rq=1)
[Cut Video with FFmpeg](https://superuser.com/questions/1101557/cut-video-with-ffmpeg?rq=1)
[3](https://superuser.com/questions/1167958/video-cut-with-missing-frames-in-ffmpeg?rq=1)
[Video cut with missing frames in FFmpeg](https://superuser.com/questions/1167958/video-cut-with-missing-frames-in-ffmpeg?rq=1)
[5](https://superuser.com/questions/1697664/cut-off-from-beginning-to-key-frame-using-ffmpeg?rq=1)
[Cut off from beginning to key frame using FFMPEG](https://superuser.com/questions/1697664/cut-off-from-beginning-to-key-frame-using-ffmpeg?rq=1)
[3](https://superuser.com/questions/1768985/ffmpeg-cut-video-from-the-beginning-until-a-certain-pixel-is-colored-at-a-spec?rq=1)
[FFmpeg - Cut video from the beginning until a certain pixel is colored at a specific color](https://superuser.com/questions/1768985/ffmpeg-cut-video-from-the-beginning-until-a-certain-pixel-is-colored-at-a-spec?rq=1)

###### [Hot Network Questions](https://stackexchange.com/questions?tab=hot)

```
*  [Bayes Factor for a contingency table analysis with an independent multinomial sampling plan: how do I decide whether to fix columns or rows?](https://stats.stackexchange.com/questions/675518/bayes-factor-for-a-contingency-table-analysis-with-an-independent-multinomial-sa)
*  [Segmentation of titles and demonyms](https://chinese.stackexchange.com/questions/64046/segmentation-of-titles-and-demonyms)
*  [Old TV episode in which a young man acquires a magic amulet that allows him to become the object of his desire](https://scifi.stackexchange.com/questions/303990/old-tv-episode-in-which-a-young-man-acquires-a-magic-amulet-that-allows-him-to-b)
*  [Under the Canadian Charter of Rights and Freedoms, what makes an "analogous ground" on which discrimination would be an infringement?](https://law.stackexchange.com/questions/114552/under-the-canadian-charter-of-rights-and-freedoms-what-makes-an-analogous-grou)
*  [Improvements to code used for a special heading](https://tex.stackexchange.com/questions/761700/improvements-to-code-used-for-a-special-heading)
*  [Is it irrationally arrogant to think that no reasonable evidence for god is possible?](https://philosophy.stackexchange.com/questions/137548/is-it-irrationally-arrogant-to-think-that-no-reasonable-evidence-for-god-is-poss)
*  [Dennis trace for Efimov K-theory](https://mathoverflow.net/questions/510029/dennis-trace-for-efimov-k-theory)
*  [Need help answering Melboure University Schools Competion questions about the periodicity of a triangular sequence.](https://math.stackexchange.com/questions/5132155/need-help-answering-melboure-university-schools-competion-questions-about-the-pe)
*  [When to use std::vector reserve](https://softwareengineering.stackexchange.com/questions/461079/when-to-use-stdvector-reserve)
*  [What to do about a no win situation of performance punishment?](https://workplace.stackexchange.com/questions/203342/what-to-do-about-a-no-win-situation-of-performance-punishment)
*  [Was the departure, of AmE from BrE, primarily - or even solely - due to Noah Webster?](https://english.stackexchange.com/questions/639437/was-the-departure-of-ame-from-bre-primarily-or-even-solely-due-to-noah-web)
*  [Are there code issues with this bathroom wiring?](https://diy.stackexchange.com/questions/329924/are-there-code-issues-with-this-bathroom-wiring)
*  [How do I block all outbound connections by PoE IP cameras I don't fully trust?](https://superuser.com/questions/1936483/how-do-i-block-all-outbound-connections-by-poe-ip-cameras-i-dont-fully-trust)
*  [Starting maths postdoc later than sooner](https://academia.stackexchange.com/questions/226426/starting-maths-postdoc-later-than-sooner)
*  [What should one do when the paper is rejected with a wrong quick report?](https://academia.stackexchange.com/questions/226415/what-should-one-do-when-the-paper-is-rejected-with-a-wrong-quick-report)
*  [What is state citizenship under the 14th Amendment, and how come you never hear much about it?](https://politics.stackexchange.com/questions/94495/what-is-state-citizenship-under-the-14th-amendment-and-how-come-you-never-hea)
*  [Why do all the symbiotes have a spiral on their face?](https://gaming.stackexchange.com/questions/418378/why-do-all-the-symbiotes-have-a-spiral-on-their-face)
*  ['Offend' and 'Hinder' in Mark 9](https://hermeneutics.stackexchange.com/questions/115801/offend-and-hinder-in-mark-9)
*  [Is the timestamp of dash cam videos that important?](https://law.stackexchange.com/questions/114537/is-the-timestamp-of-dash-cam-videos-that-important)
*  [How to plot y = x^{2/3} + 0.8 cos(kx) √(3-x²) in LaTeX TikZ](https://tex.stackexchange.com/questions/761671/how-to-plot-y-x2-3-0-8-coskx-%e2%88%9a3-x%c2%b2-in-latex-tikz)
*  [Turn a shark egg case into a tetrahedron](https://puzzling.stackexchange.com/questions/137596/turn-a-shark-egg-case-into-a-tetrahedron)
*  [What is the relationship between wearing, holding, and carrying an item?](https://rpg.stackexchange.com/questions/219070/what-is-the-relationship-between-wearing-holding-and-carrying-an-item)
*  [Fibonacci - Memento pattern with recursion and some utilities](https://codereview.stackexchange.com/questions/301774/fibonacci-memento-pattern-with-recursion-and-some-utilities)
*  [In Romans 1:5, is Paul saying that his apostleship to the Gentiles is the LORD leading him in the path of righteousness?](https://hermeneutics.stackexchange.com/questions/115791/in-romans-15-is-paul-saying-that-his-apostleship-to-the-gentiles-is-the-lord-l)
```

### Why are you flagging this comment?

[-] 20
It contains harassment, bigotry or abuse.
This comment attacks a person or group. Learn more in our [Abusive behavior policy](https://superuser.com/conduct/abusive-behavior). [-] 40
It's unfriendly or unkind.
This comment is rude or condescending. Learn more in our [Code of Conduct](https://superuser.com/conduct/abusive-behavior). [-] 39
Not needed.
This comment is not relevant to the post.

```

```

Enter at least 6 characters [-] 19
Something else.
A problem not listed above. Try to be as specific as possible.

```

```

Enter at least 6 characters
Flag comment Cancel
You have 0 flags left today

### Hang on, you can't upvote just yet.

You'll need to complete a few actions and gain 15 reputation points before being able to upvote. **Upvoting** indicates when questions and answers are useful. [What's reputation and how do I get it?](https://stackoverflow.com/help/whats-reputation)
Instead, you can save this post to reference later.
Save this post for later Not now

###### [Super User](https://superuser.com/)

```
*  [Tour](https://superuser.com/tour)
*  [Help](https://superuser.com/help)
*  [Chat](https://chat.stackexchange.com?tab=site&host=superuser.com)
*  [Contact](https://superuser.com/contact)
*  [Feedback](https://meta.superuser.com/)
```

###### [Company](https://stackoverflow.co/)

```
*  [Stack Overflow](https://stackoverflow.com/)
*  [Stack Internal](https://stackoverflow.co/internal/)
*  [Stack Data Licensing](https://stackoverflow.co/data-licensing/)
*  [Stack Ads](https://stackoverflow.co/advertising/)
*  [About](https://stackoverflow.co/)
*  [Press](https://stackoverflow.co/company/press/)
*  [Legal](https://stackoverflow.com/legal)
*  [Privacy Policy](https://stackoverflow.com/legal/privacy-policy)
*  [Terms of Service](https://stackoverflow.com/legal/terms-of-service/public)
*  Your Privacy Choices
*  [Cookie Policy](https://policies.stackoverflow.co/stack-overflow/cookie-policy)
```

###### [Stack Exchange Network](https://stackexchange.com/)

```
*  [Technology](https://stackexchange.com/sites#technology)
*  [Culture & recreation](https://stackexchange.com/sites#culturerecreation)
*  [Life & arts](https://stackexchange.com/sites#lifearts)
*  [Science](https://stackexchange.com/sites#science)
*  [Professional](https://stackexchange.com/sites#professional)
*  [Business](https://stackexchange.com/sites#business)
*  [API](https://api.stackexchange.com/)
*  [Data](https://data.stackexchange.com/)
*  [Blog](https://stackoverflow.blog?blb=1)
*  [Facebook](https://www.facebook.com/officialstackoverflow/)
*  [Twitter](https://twitter.com/stackoverflow)
*  [LinkedIn](https://linkedin.com/company/stack-overflow)
*  [Instagram](https://www.instagram.com/thestackoverflow)
```

Site design / logo © 2026 Stack Exchange Inc; user contributions licensed under [CC BY-SA](https://stackoverflow.com/help/licensing) . rev 2026.4.8.41877
By continuing to use this website, you agree Stack Exchange can store cookies on your device and disclose information in accordance with our [Cookie Policy](https://policies.stackoverflow.co/stack-overflow/cookie-policy/). By exiting this window, default cookies will be accepted. To reject cookies, select an option from below.
Necessary cookies only
Customize settings