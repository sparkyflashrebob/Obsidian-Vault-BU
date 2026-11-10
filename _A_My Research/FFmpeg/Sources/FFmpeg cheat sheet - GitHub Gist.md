---
tags:
  - notebooklm-import
notebook: "FFmpeg"
category: "research"
---

FFmpeg cheat sheet · GitHub
[Skip to content](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730#start-of-content) 
Search Gists
Search Gists
[All gists](https://gist.github.com/discover) [Back to GitHub](https://github.com/) [Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fsteven2358%2Fba153c642fe2bb1e47485962df07c730) [Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fsteven2358%2Fba153c642fe2bb1e47485962df07c730&source=header-gist) 
[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fsteven2358%2Fba153c642fe2bb1e47485962df07c730) [Sign up](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2Fsteven2358%2Fba153c642fe2bb1e47485962df07c730&source=header-gist)
You signed in with another tab or window. [Reload](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730) to refresh your session. You signed out in another tab or window. [Reload](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730) to refresh your session. You switched accounts on another tab or window. [Reload](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730) to refresh your session. Dismiss alert
Instantly share code, notes, and snippets.

### [steven2358](https://gist.github.com/steven2358)/ **ffmpeg.md**

Last active yesterday
Show Gist options
\* [Download ZIP](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730/archive/a449423df1890628e5e2dc5df30ff784b33cc6a9.zip)
\* [Star 1,490 ( 1,490)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fsteven2358%2Fba153c642fe2bb1e47485962df07c730) You must be signed in to star a gist
\* [Fork 159 ( 159)](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fsteven2358%2Fba153c642fe2bb1e47485962df07c730) You must be signed in to fork a gist
\* Embed

### Select an option

```
*  Embed Embed this gist in your website.
    *  Share Copy sharable link for this gist.
    *  Clone via HTTPS Clone using the web URL.
```

#### No results found

[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use) Clone this repository at
\* Save steven2358/ba153c642fe2bb1e47485962df07c730 to your computer and use it in GitHub Desktop.
[Code](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730) [Revisions 19](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730/revisions) [Stars 1,487](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730/stargazers) [Forks 159](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730/forks)
Embed

### Select an option

```
*  Embed Embed this gist in your website.
*  Share Copy sharable link for this gist.
*  Clone via HTTPS Clone using the web URL.
```

#### No results found

[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)
Clone this repository at
Save steven2358/ba153c642fe2bb1e47485962df07c730 to your computer and use it in GitHub Desktop.
[Download ZIP](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730/archive/a449423df1890628e5e2dc5df30ff784b33cc6a9.zip)
FFmpeg cheat sheet
[Raw](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730/raw/a449423df1890628e5e2dc5df30ff784b33cc6a9/ffmpeg.md)
[ffmpeg.md](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730#file-ffmpeg-md)

### FFmpeg cheat sheet

A list of useful commands for the FFmpeg command line tool.
Download FFmpeg: <https://www.ffmpeg.org/download.html>
Full documentation: <https://www.ffmpeg.org/ffmpeg.html>

#### Basic conversion

```
ffmpeg -i in.mp4 out.avi
```

##### Remux an MKV file into MP4

```
ffmpeg -i in.mkv -c:v copy -c:a copy out.mp4
```

##### High-quality encoding

Use the crf (Constant Rate Factor) parameter to control the output quality. The lower crf, the higher the quality (range: 0-51). The default value is 23, and visually lossless compression corresponds to -crf 18 . Use the preset parameter to control the speed of the compression process. Additional info: <https://trac.ffmpeg.org/wiki/Encode/H.264>

```
ffmpeg -i in.mp4 -preset slower -crf 18 out.mp4
```

#### Trimming

Without re-encoding:

```
ffmpeg -ss [start] -i in.mp4 -t [duration] -c copy out.mp4
```

```
*  [-ss](http://ffmpeg.org/ffmpeg-all.html#Main-options) specifies the start time, e.g. 00:01:23.000 or 83 (in seconds)
*  [-t](http://ffmpeg.org/ffmpeg-all.html#Main-options) specifies the duration of the clip (same format).
*  Recent ffmpeg also has a flag to supply the end time with -to .
*  [-c](http://ffmpeg.org/ffmpeg-all.html#Main-options) copy copies the first video, audio, and subtitle bitstream from the input to the output file without re-encoding them. This won't harm the quality and make the command run within seconds.
```

With re-encoding:
If you leave out the -c copy option, ffmpeg will automatically re-encode the output video and audio according to the format you chose. For high quality video and audio, read the [x264 Encoding Guide](https://ffmpeg.org/trac/ffmpeg/wiki/x264EncodingGuide) and the [AAC Encoding Guide](http://ffmpeg.org/trac/ffmpeg/wiki/AACEncodingGuide), respectively.
For example:

```
ffmpeg -ss [start] -i in.mp4 -t [duration] -c:v libx264 -c:a aac -strict experimental -b:a 128k out.mp4
```

#### Mux video and audio from another video

To copy the video from in0.mp4 and audio from in1.mp4:

```
ffmpeg -i in0.mp4 -i in1.mp4 -c copy -map 0:0 -map 1:1 -shortest out.mp4
```

```
*  With [-c copy](http://ffmpeg.org/ffmpeg.html#Stream-copy) the streams will be stream copied , not re-encoded, so there will be no quality loss. If you want to re-encode, see [FFmpeg Wiki: H.264 Encoding Guide](https://trac.ffmpeg.org/wiki/Encode/H.264).
*  The -shortest option will cause the output duration to match the duration of the shortest input stream.
*  See the [-map option documentation](http://ffmpeg.org/ffmpeg.html#Advanced-options) for more info.
```

#### Concat demuxer

First, make a text file.

```
file 'in1.mp4'
file 'in2.mp4'
file 'in3.mp4'
file 'in4.mp4'
```

Then, run ffmpeg :

```
ffmpeg -f concat -i list.txt -c copy out.mp4
```

#### Delay audio/video

Delay video by 3.84 seconds:

```
ffmpeg -i in.mp4 -itsoffset 3.84 -i in.mp4 -map 1:v -map 0:a -vcodec copy -acodec copy out.mp4
```

Delay audio by 3.84 seconds:

```
ffmpeg -i in.mp4 -itsoffset 3.84 -i in.mp4 -map 0:v -map 1:a -vcodec copy -acodec copy out.mp4
```

#### Burn subtitles

Use the [libass](http://ffmpeg.org/ffmpeg.html#ass) library (make sure your ffmpeg install has the library in the configuration --enable-libass ).
First convert the subtitles to .ass format:

```
ffmpeg -i sub.srt sub.ass
```

Then add them using a video filter:

```
ffmpeg -i in.mp4 -vf ass=sub.ass out.mp4
```

#### Extract the frames from a video

To extract all frames from between 1 and 5 seconds, and also between 11 and 15 seconds:

```
ffmpeg -i in.mp4 -vf select='between(t,1,5)+between(t,11,15)' -vsync 0 out%d.png
```

To extract one frame per second only:

```
ffmpeg -i in.mp4 -fps=1 -vsync 0 out%d.png
```

#### Rotate a video

Rotate 90 clockwise:

```
ffmpeg -i in.mov -vf "transpose=1" out.mov
```

For the transpose parameter you can pass:

```
0 = 90CounterCLockwise and Vertical Flip (default)
1 = 90Clockwise
2 = 90CounterClockwise
3 = 90Clockwise and Vertical Flip
```

Use -vf "transpose=2,transpose=2" for 180 degrees.

#### Download "Transport Stream" video streams

```
1. Locate the playlist file, e.g. using Chrome > F12 > Network > Filter: m3u8
1. Download and concatenate the video fragments:
```

```
ffmpeg -i "path_to_playlist.m3u8" -c copy -bsf:a aac_adtstoasc out.mp4
```

If you get a "Protocol 'https not on whitelist 'file,crypto'!" error, add the protocol\_whitelist option:

```
ffmpeg -protocol_whitelist "file,http,https,tcp,tls" -i "path_to_playlist.m3u8" -c copy -bsf:a aac_adtstoasc out.mp4
```

#### Mute some of the audio

To replace the first 90 seconds of audio with silence:

```
ffmpeg -i in.mp4 -vcodec copy -af "volume=enable='lte(t,90)':volume=0" out.mp4
```

To replace all audio between 1'20" and 1'30" with silence:

```
ffmpeg -i in.mp4 -vcodec copy -af "volume=enable='between(t,80,90)':volume=0" out.mp4
```

#### Deinterlace

Deinterlacing using "yet another deinterlacing filter".

```
ffmpeg -i in.mp4 -vf yadif out.mp4
```

#### Create a video slideshow from images

Parameters: -r marks the image framerate (inverse time of each image); -vf fps=25 marks the true framerate of the output.

```
ffmpeg -r 1/5 -i img%03d.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p out.mp4
```

#### Extract images from a video

```
*  Extract all frames: ffmpeg -i input.mp4 thumb%04d.jpg -hide_banner
*  Extract a frame each second: ffmpeg -i input.mp4 -vf fps=1 thumb%04d.jpg -hide_banner
*  Extract only one frame: ffmpeg -i input.mp4 -ss 00:00:10.000 -vframes 1 thumb.jpg
```

#### Display the frame number on each frame

```
ffmpeg -i in.mov -vf "drawtext=fontfile=arial.ttf: text=%{n}: x=(w-tw)/2: y=h-(2*lh): fontcolor=white: box=1: boxcolor=0x00000099: fontsize=72" -y out.mov
```

#### Metadata: Change the title

```
ffmpeg -i in.mp4 -map_metadata -1 -metadata title="My Title" -c:v copy -c:a copy out.mp4
```

#### Tools

<https://ffmpeg.lav.io/> is an interactive resource to compose FFmpeg actions.
Load earlier comments...
Copy link
Copy Markdown

##### **acnhia** commented [on Mar 28, 2021](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=3684821#gistcomment-3684821) • edited Loading

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Hi I am looking for commands for these 2 use cases, could you please help
1. If a Prores has baked in Video+audio (5.1, mono, downmix) -. output a clean prores video + 5.1 audio tracks only.
1. if a prores stereo L&R are in single track need a clean output with L and R on different tracks
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **dcambria** commented [on Apr 22, 2021](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=3716848#gistcomment-3716848)

how to start a video from X frame, like -ss?
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **paulschreiber** commented [on Apr 24, 2021](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=3718779#gistcomment-3718779)

```
ffmpeg -i in.mkv -c:v copy -c:a copy out.mp4
```

You can simplify to:

```
ffmpeg -i in.mkv -c copy out.mp4
```

Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **jugshaurya** commented [on May 13, 2021](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=3741080#gistcomment-3741080) • edited Loading

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
I am using

```
ffmpeg -f concat -safe 0 -protocol_whitelist file,http,https,tcp,tls,crypto -i ${args.fileList} -c copy ${outputFileName}
```

and fileList is a file in /tmp/tmp-65420oJVGcsBokCX.txt file with data

```
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/1.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/2.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/3.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/4.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/5.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/6.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/7.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/8.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/9.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/10.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/11.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/12.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/13.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/14.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/15.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/16.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/17.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/18.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/19.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/20.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/21.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/22.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/23.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/24.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/25.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/26.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/27.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/28.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/29.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/30.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/31.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/32.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/33.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/34.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/35.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/36.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/37.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/38.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/39.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/40.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/41.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/42.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/43.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/44.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/45.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/46.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/47.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/48.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/49.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/50.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/51.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/52.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/53.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/54.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/55.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/56.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/57.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/58.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/59.mp4'
file '/home/shaurya/dev/git_repos/merge-videos/assets/course/60.mp4'
```

and I am trying to merge these videos into a single video, but this error is coming and only the initial 21 videos are merging, and the rest just not!
can you please look into it ( Invalid data found when processing input **below image** ) and let me know if I need to change something in the above command?
Github Repo for the same: <https://github.com/jugshaurya/merge-videos>
[@steven2358](https://github.com/steven2358)
Thank you in advance
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown
Author

##### **steven2358** commented [on May 13, 2021](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=3741476#gistcomment-3741476)

[@jugshaurya](https://github.com/jugshaurya) I don't see the error at first glance. I suggest you start with a minimal working example and extend it until you hit an error.
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **jugshaurya** commented [on May 13, 2021](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=3741670#gistcomment-3741670)

I am trying to merge 60 videos in a folder. and I got the `file 'paths/to/file' for each mp4 file as pasted above.
Following your advice, I tried to merge the initial 30 videos then the initial 15 videos, and so on...(using binary search) and found out because of video 22 error was coming. If I deleted 22.mp4 all rest 59 are merging correctly. I played 22.mp4 and found that It is quitting after the 4th minute even when the video is 9 min.
So I understand that the video has some error, not the FFmpeg command. Thanks for the advice [@steven2358](https://github.com/steven2358)
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **MarvusMedia** commented [on Aug 8, 2021](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=3850483#gistcomment-3850483) • edited Loading

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Thanks so much for this - it's very useful!
I realise you probably get inundated with questions, but if you can spare a moment, could you tell me if it's possible to use a CD's 'frame' numbers (as shown by ffprobe) rather than seconds (often with recurring decimals) as start and end points when extracting individual tracks with libcdio? Thanks. :)
Marcus
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **nikk-ca** commented [on Aug 12, 2021](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=3859716#gistcomment-3859716)

Super handy!
Just one quick thing, under **Extract the frames from a video** : ffmpeg -i in.mp4 -fps=1 -vsync 0 out%d.png should be ffmpeg -i in.mp4 -vf fps=1 -vsync 0 out%d.png , yes?
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **Ghayas-cyber** commented [on Nov 11, 2021](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=3959595#gistcomment-3959595)

Hello. I have a Reference video in YUV format. I have encoded video (Encoded in MPEG4) .mp4.
Now My task is to calculate VMAF for YUV (Reference video) and MPEG4 (Distorted).
Can you please help me out. Thanks
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **MarvusMedia** commented [on Nov 11, 2021](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=3959625#gistcomment-3959625)

Super handy!
Just one quick thing, under **Extract the frames from a video** : ffmpeg -i in.mp4 -fps=1 -vsync 0 out%d.png should be ffmpeg -i in.mp4 -vf fps=1 -vsync 0 out%d.png , yes?
No, -fps sets the framerate. It's not a video filter.
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **Ghayas-cyber** commented [on Nov 12, 2021](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=3960330#gistcomment-3960330)

Hello
I have two files Reference (YUV) & distorted (YUV). I am calculating the VMAF score. When I run the command I get following output.
Option video\_size not found.
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **nikk-ca** commented [on Jan 23, 2022](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4039165#gistcomment-4039165)

No, -fps sets the framerate. It's not a video filter.
[@MarvusMedia](https://github.com/MarvusMedia)
It's documented as a video filter [here](https://ffmpeg.org/ffmpeg-filters.html#fps-1). Maybe you mean -r ?
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **MarvusMedia** commented [on Jan 24, 2022](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4039588#gistcomment-4039588) • edited Loading

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
It's documented as a video filter here. Maybe you mean -r ?
[@nikk-ca](https://github.com/nikk-ca)
Sorry, yes, I was thinking of -r . -fps is indeed used to force a new framerate.
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **JirkaSulkov** commented [on Feb 7, 2022](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4056886#gistcomment-4056886)

#### Hi, I'm trying to save AAC audio from video to WAV, but it still reports an error on file size. Don't know what it can be?

D:>ffmpeg.exe -i D.mkv D.wav
Output #0, wav, to 'D.wav':
Stream #0:0(cze): Audio: pcm\_s16le ([1][0][0][0] / 0x0001), 44100 Hz, stereo, s16, 1411 kb/s (default)

#### [wav @ 00000151cf2a98c0] Filesize 10.880.815.182 invalid for wav, output file will be broken size=10.625.796kB time=17:08:02.62 bitrate=1411.2kbits/s speed= 328x

JirkaS
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **MarvusMedia** commented [on Feb 7, 2022](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4056985#gistcomment-4056985)

Is D.mkv really 17 hours long? If not, then it may be a malformed file (maybe an incomplete download) and ffmpeg is misreading the duration.
Can you do "D:>ffprobe D.mkv" and post the results?
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **JirkaSulkov** commented [on Feb 9, 2022](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4060059#gistcomment-4060059)

The D.mkv file is not downloaded. I created it in the VideoPad program. I combined 24 parts. This is due to incorrect playback on the smartTV. According to the playlist, all parts will be played at once, but the Subtitle must be set for each.
After linking to a large file, I needed to sync the subtitles in the SubtitleEdit program. But the Waveform soundtrack will only be created by 12:25:29. In consultation with the author of the SE, I found out that it will terminate FFmpeg earlier.
Here is the output of ffprobe.
D:\FF>ffprobe d.mkv
ffprobe version N-90707-g01170e9db0 Copyright (c) 2007-2018 the FFmpeg developers
built with gcc 7.1.0 (GCC)
configuration: --arch=x86\_64 --target-os=mingw32 --cross-prefix=/home/jacek/ffenv/04/jpff/cross\_compilers/mingw-w64-x86\_64/bin/x86\_64-w64-mingw32- --pkg-config=pkg-config --pkg-config-flags=--static --enable-gray --enable-version3 --disable-debug --disable-doc --disable-htmlpages --disable-manpages --disable-podpages --disable-txtpages --disable-w32threads --extra-cflags=-DPTW32\_STATIC\_LIB --extra-libs=-lstdc++ --enable-gpl --enable-version3 --enable-libx264 --enable-libx265 --enable-libxvid --enable-libmp3lame --enable-libfdk-aac --enable-libopus --enable-zlib --enable-fontconfig --enable-libass --enable-iconv --enable-libfreetype --extra-cflags=-DLIBTWOLAME\_STATIC --extra-cflags=-DMODPLUG\_STATIC --extra-cflags=-DCACA\_STATIC --extra-cflags='-mtune=generic' --extra-cflags=-O3 --enable-shared --disable-static --prefix=/home/jacek/ffenv/04/jpff/win64/ffmpeg\_git\_with\_fdk\_aac\_xp\_compat\_shared
libavutil 56. 13.100 / 56. 13.100
libavcodec 58. 17.100 / 58. 17.100
libavformat 58. 11.101 / 58. 11.101
libavdevice 58. 2.100 / 58. 2.100
libavfilter 7. 15.100 / 7. 15.100
libswscale 5. 0.102 / 5. 0.102
libswresample 3. 0.101 / 3. 0.101
libpostproc 55. 0.100 / 55. 0.100
Input #0, matroska,webm, from 'd.mkv':
Metadata:
encoder : libebml v1.4.2 + libmatroska v1.6.4
creation\_time : 2022-01-31T22:57:04.000000Z
Duration: 17:08:02.92, start: 0.000000, bitrate: 874 kb/s
Stream #0:0: Video: h264 (Main), yuv420p(progressive), 800x600 [SAR 1:1 DAR 4:3], 25 fps, 25 tbr, 1k tbn, 50 tbc (default)
Metadata:
BPS : 712784
DURATION : 17:08:02.920000000
NUMBER\_OF\_FRAMES: 1542073
NUMBER\_OF\_BYTES : 5495827574
\_STATISTICS\_WRITING\_APP: mkvmerge v64.0.0 ('Willows') 64-bit
\_STATISTICS\_WRITING\_DATE\_UTC: 2022-01-31 22:57:04
\_STATISTICS\_TAGS: BPS DURATION NUMBER\_OF\_FRAMES NUMBER\_OF\_BYTES
Stream #0:1(cze): Audio: ac3, 44100 Hz, stereo, fltp, 160 kb/s (default)
Metadata:
BPS : 160000
DURATION : 17:08:02.625000000
NUMBER\_OF\_FRAMES: 1770966
NUMBER\_OF\_BYTES : 1233652506
\_STATISTICS\_WRITING\_APP: mkvmerge v64.0.0 ('Willows') 64-bit
\_STATISTICS\_WRITING\_DATE\_UTC: 2022-01-31 22:57:04
\_STATISTICS\_TAGS: BPS DURATION NUMBER\_OF\_FRAMES NUMBER\_OF\_BYTES
D:\FF>
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **MarvusMedia** commented [on Feb 10, 2022](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4060493#gistcomment-4060493)

Other than suggesting a compressed audio format instead of WAV, I don't really know how to help you. Sorry.
Maybe someone else can answer.
Good luck.
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **JayRugMan** commented [on Dec 1, 2022](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4388381#gistcomment-4388381)

This is great. Thanks for compiling this. Here is a bash script I wrote for easily adding metadata tags to audio files. Feel free to crack it open and add functionality for video files or adding more tags.
My Script <https://github.com/JayRugMan/fun_with_bash/blob/master/metatag.sh>
list of ffmpeg metadata tags: <https://wiki.multimedia.cx/index.php/FFmpeg_Metadata>
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **fufatujuba** commented [on Dec 21, 2022](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4409679#gistcomment-4409679)

**Your list is very useful. But I have question.**
How to use two filters to extract frames from .h265 at the same time? ffmpeg -i input.h265 -vf "select=not(mod(n,10))" -vsync 0 frame-%04d.png works fine to extract stepped frames . But later I realized that it always outputs frames with constant size which is **1920x1080** . I have to add an other filter to scale the size like this: ffmpeg -i input.h265 -vf "select=not(mod(n,10))" "scale=w=3840:h=2160" -vsync 0 frame-%04d.png for **4k** resolution and etc... then the extraction started producing **0** frames
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **laurentlbm** commented [on May 4, 2023](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4557993#gistcomment-4557993)

One issue I've had on Plex is videos with closed captioning. I use this little snippet to remove them:

```
ffmpeg -i in.mp4 -codec copy -bsf:v "filter_units=remove_types=6" out.mp4
```

If you want to extract those captions first, you can run:

```
ffmpeg -f lavfi -i "movie='in.mp4'[out0+subcc]" -map s out.srt
```

Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **AlkisPis** commented [on Aug 26, 2023](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4672729#gistcomment-4672729)

Great ref for exploring ffmpeg! Thanks for sharing!
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **debuti** commented [on Aug 27, 2023](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4673371#gistcomment-4673371)

<https://ffmpeg.lav.io/> is a great interactive resource to compose ffmpeg actions
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown
Author

##### **steven2358** commented [on Aug 29, 2023](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4674905#gistcomment-4674905)

<https://ffmpeg.lav.io/> is a great interactive resource to compose ffmpeg actions
Excellent. Added.
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **AlkisPis** commented [on Aug 29, 2023](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4675007#gistcomment-4675007)

<https://ffmpeg.lav.io/> is a great interactive resource to compose ffmpeg actions
Great interactive tool! Thanks [@debuti](https://github.com/debuti) for bringing this up!
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **asifajrof** commented [on Dec 23, 2023](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4805088#gistcomment-4805088) • edited Loading

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
i once used this (found from some StackOverflow answer, can't find the link now) to convert a video to gif ffmpeg -i in.mp4 -vf "fps=10,scale=720:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
Edit: found the original stack post. [here](https://superuser.com/a/556031/1656514)
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **AlkisPis** commented [on Dec 24, 2023](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4806465#gistcomment-4806465)

[@asifajrof](https://github.com/asifajrof), nice setup. But what's the use? It creates a huge GIF file. (It can be 15 to 50 times larger, depending on the scale.) The reverse process is more useful. The resulted MP4 file can be about 20 times smaller. (I tested all that with a small MP4 file.)
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **asifajrof** commented [on Dec 25, 2023](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4806627#gistcomment-4806627) • edited Loading

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
But what's the use? It creates a huge GIF file.
You are right. It does output a larger file. The one time when I used it was for a very small video file, so the size of the GIF also didn't bother me much. I mentioned it here because I didn't see any process of converting a video to GIF in this cheat sheet.
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **AlkisPis** commented [on Dec 25, 2023](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=4806896#gistcomment-4806896)

[@asifajrof](https://github.com/asifajrof), you did very well posting this FFMPEG setup. It's a very useful just by itself. I have worked for a while with FFMPEG, both with the S/W itself (i.e. using console commands) and and with programming, using a Python FFMPEG library. Yet, I couldn't master --actually, I didn't even try-- its too complicated, highly compacted and symbolic commands, an example of which you offered yourself.
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **MAZ01001** commented [on Jun 8, 2025](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=5609787#gistcomment-5609787)

Nice cheat sheet
I also made a list of different FFmpeg/FFplay/FFprobe functionality/commands over at <https://github.com/MAZ01001/FFmpeg-resource>
Although that list is a lot longer and a bit less descriptive, it *was* mostly for myself as a reminder of how to do certain commands...
If you want to add some stuff from there to this list here (or add things to my list), feel free to do so :D
Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
Copy link
Copy Markdown

##### **fatihdeveci05-creator** commented [on Oct 26, 2025](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730?permalink_comment_id=5829995#gistcomment-5829995)

FFMPEG- m3u8 to mpeg1video
Hello,
I want to synchronously convert a live broadcast in m3u8 format to mpeg1video format and broadcast it on my site, and I'm doing so. However, I'm having a problem: the stream isn't smooth, and I'm experiencing constant lag. Unfortunately, I can't change the codec. I think I'm using some incorrect settings, and I hope you can help me with this. I've read many forums and articles, but they've all been inconclusive.
You can check it out yourself. My website: <https://sefirox.com/>
Thank you.

```
ffmpeg -re
-i [STREAM_URL]
-f mpegts
-codec:v mpeg1video
-s 854x480
-b:v 700k
-maxrate 700k
-bf 0
-g 25
-r 25
-qmin 3
-qmax 5
-preset ultrafast
-threads 2
-muxdelay 0.1
-muxpreload 0.1
-codec:a mp2
-b:a 96k
-ar 44100
-ac 1
[http://127.0.0.1:8081/supersecret/[CHANNEL_ID]](http://127.0.0.1:8081/supersecret/%5BCHANNEL_ID%5D)
```

Sorry, something went wrong.

##### Uh oh!

There was an error while loading. [Please reload this page](https://gist.github.com/steven2358/ba153c642fe2bb1e47485962df07c730).
[Sign up for free](https://gist.github.com/join?source=comment-gist) **to join this conversation on GitHub** . Already have an account? [Sign in to comment](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2Fsteven2358%2Fba153c642fe2bb1e47485962df07c730)

#### Footer

© 2026 GitHub, Inc.

##### Footer navigation

```
*  [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
*  [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
*  [Security](https://github.com/security)
*  [Status](https://www.githubstatus.com/)
*  [Community](https://github.community/)
*  [Docs](https://docs.github.com/)
*  [Contact](https://support.github.com?tags=dotcom-footer)
*  Manage cookies
*  Do not share my personal information
```

You can't perform that action at this time.