---
tags:
  - notebooklm-import
notebook: "FFmpeg"
category: "research"
---

How to compress video files while maintaining quality with ffmpeg | Mux
[Skip to content](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#skip-nav)
[Mux Logo Toggle Mux Brand Popover](https://www.mux.com/)
Toggle navigation menu X
\* Product Caret
\* Solutions Caret
\* Developers Caret
\* [Pricing](https://www.mux.com/pricing)
\* [Blog](https://www.mux.com/blog)
[Talk to us Talk to us](https://www.mux.com/sales-contact)
[Log in Log in](https://dashboard.mux.com/login)

#### Table of Contents

```
*  [Why compress video files? Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#why-compress-video-files)
*  [Understanding video compression fundamentals Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#understanding-video-compression-fundamentals)
*  [Codecs Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#codecs)
*  [Bitrate Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#bitrate)
*  [Resolution Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#resolution)
*  [Frame rate Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#frame-rate)
*  [Basic video compression with FFmpeg Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#basic-video-compression-with-ffmpeg)
*  [Advanced techniques for quality preservation Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#advanced-techniques-for-quality-preservation)
*  [Two-pass encoding Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#two-pass-encoding)
*  [Adjusting the encoding preset Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#adjusting-the-encoding-preset)
*  [Using more efficient codecs Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#using-more-efficient-codecs)
*  [Adaptive quality targeting Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#adaptive-quality-targeting)
*  [Video scaling techniques Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#video-scaling-techniques)
*  [Reducing resolution Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#reducing-resolution)
*  [Reducing frame rate Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#reducing-frame-rate)
*  [Balancing compression strategies for different scenarios Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#balancing-compression-strategies-for-different-scenarios)
*  [Web delivery Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#web-delivery)
*  [Archival quality Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#archival-quality)
*  [Low bandwidth environments Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#low-bandwidth-environments)
*  [Mux tips for evaluating compression results Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#mux-tips-for-evaluating-compression-results)
*  [Choosing the right compression approach Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#choosing-the-right-compression-approach)
*  [CRF-based compression: Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#crf-based-compression)
*  [Bitrate-based compression: Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#bitrate-based-compression)
*  [Resolution reduction: Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#resolution-reduction)
*  [Final recommendations Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#final-recommendations)
*  [Video compression FAQs Arrow Right](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#video-compression-faqs)
```

Mux Video is an API-first platform, powered by data and designed by video experts to make beautiful video possible for every development team.
[Get Started With Mux Get Started With Mux](https://dashboard.mux.com/signup)

### How to compress video files while maintaining quality with ffmpeg

Video compression is an essential skill for content creators, filmmakers, and anyone who works with digital video. While high-quality raw footage can produce stunning results, the large file sizes are impractical for storage, sharing, and streaming. Fortunately, FFmpeg provides powerful tools to compress video files while preserving visual quality. This guide will walk you through effective compression techniques that minimize file size without sacrificing the viewing experience.
If you're looking for somewhere to host and stream your videos for you, Mux's [Video API](https://mux.com/video-api) has everything you need to manage video for your application.

#### [Link Why compress video files?](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#why-compress-video-files)

There are numerous reasons to compress your video files:
\* **Storage optimization** : Reduce the space required on hard drives and cloud storage.
\* **Faster uploads** : Send compressed files to clients or upload to hosting platforms more quickly.
\* **Improved streaming** : Smaller files lead to smoother playback and less buffering.
\* **Reduced bandwidth costs** : Pay less for hosting and content delivery.
\* **Email and messaging** : Meet size limits for video attachments.
\* **Mobile viewing** : Create mobile-friendly versions that consume less data.
\* **Archive management** : Store more content in the same amount of space.
Let's explore how to use FFmpeg to compress videos while maintaining visual quality.

#### [Link Understanding video compression fundamentals](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#understanding-video-compression-fundamentals)

Before diving into FFmpeg commands, it's helpful to understand some basic concepts that affect video quality and file size:

##### [Link Codecs](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#codecs)

A codec (encoder-decoder) is the algorithm used to compress and decompress video data. Modern codecs like H.264, H.265 (HEVC), VP9, and AV1 offer increasingly efficient compression. H.264 remains the most widely compatible, while H.265 and AV1 provide better compression but may have compatibility or processing limitations.

##### [Link Bitrate](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#bitrate)

Bitrate is the amount of data processed per unit of time, typically measured in kilobits per second (kbps) or megabits per second (Mbps). Higher bitrates generally mean better quality but larger files.

##### [Link Resolution](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#resolution)

The dimensions of your video (width × height) significantly impact file size. Common resolutions include:
\* 3840×2160 (4K)
\* 1920×1080 (1080p)
\* 1280×720 (720p)

##### [Link Frame rate](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#frame-rate)

Frame rate is the number of frames displayed per second (fps). Common frame rates are 24, 25, 30, 50 and 60 fps. Higher frame rates create smoother motion but increase file size.

#### [Link Basic video compression with FFmpeg](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#basic-video-compression-with-ffmpeg)

The simplest way to compress a video file is to re-encode it with a lower bitrate:
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libx264 -crf 23 \
  -c:a aac -b:a 128k \
  output_video.mp4
```

Breakdown of the command:
\* -i input\_video.mp4: Specifies the input video file
\* -c:v libx264: Uses the H.264 video codec
\* -crf 23: Sets the Constant Rate Factor (quality level) to 23 (lower = better quality, higher = smaller file)
\* -c:a aac: Uses AAC for audio
\* -b:a 128k: Sets the audio bitrate to 128 kbps
\* output\_video.mp4: Name of the compressed output file
The CRF value is the most important parameter for quality control. The range is 0-51, where:
\* 0 is lossless (largest files)
\* 18-23 is considered "visually lossless" (good balance)
\* 23-28 is standard range for online content
\* 28+ shows noticeable quality loss (smallest files)
If you're delivering your video over the internet, then you will likely want to use an [adaptive bitrate format like HLS](https://www.mux.com/articles/a-guide-to-http-live-streaming-hls-overview-definition-and-considerations). Mux can do that for you.
[Learn more about Mux Video Learn more about Mux Video](https://mux.com/video)

#### [Link Advanced techniques for quality preservation](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#advanced-techniques-for-quality-preservation)

##### [Link Two-pass encoding](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#two-pass-encoding)

Two-pass encoding analyzes the video in the first pass, then uses that information in the second pass for more efficient compression:
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libx264 -b:v 1000k \
  -pass 1 \
  -f mp4 /dev/null

ffmpeg -i input_video.mp4 \
  -c:v libx264 -b:v 1000k \
  -pass 2 \
  -c:a aac \
  -b:a 128k \
  output_video.mp4
```

For Windows, replace /dev/null with NUL.

##### [Link Adjusting the encoding preset](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#adjusting-the-encoding-preset)

FFmpeg provides presets that balance encoding speed against compression efficiency:
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libx264 \
  -crf 23 \
  -preset slower \
  -c:a aac -b:a 128k \
  output_video.mp4
```

Presets from fastest to slowest (and increasing compression efficiency):
\* ultrafast
\* superfast
\* veryfast
\* faster
\* fast
\* medium (default)
\* slow
\* slower
\* veryslow
\* placebo (rarely used due to diminishing returns)
Slower presets produce smaller files at the same quality level but take longer to encode.

##### [Link Using more efficient codecs](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#using-more-efficient-codecs)

H.265 (HEVC) typically offers about 50% better compression than H.264 at the same quality level:
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libx265 \
  -crf 28 \
  -c:a aac \
  -b:a 128k \
  output_video.mp4
```

Note that HEVC typically requires a CRF value about 4-6 points higher than H.264 to achieve similar visual quality.
For VP9 codec (used by YouTube and supported by most browsers):
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libvpx-vp9 \
  -crf 30 \
  -b:v 0 \
  -c:a libopus \
  -b:a 128k \
  output_video.webm
```

##### [Link Adaptive quality targeting](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#adaptive-quality-targeting)

To target a specific file size while maintaining the best possible quality:
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libx264
  -b:v 1000k
  -maxrate 1500k
  -bufsize 2000k \
  -c:a aac \
  -b:a 128k \
  output_video.mp4
```

This approach uses:
\* -b:v 1000k: Target average bitrate
\* -maxrate 1500k: Peak bitrate limit
\* -bufsize 2000k: Controls how quickly the bitrate can vary

#### [Link Video scaling techniques](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#video-scaling-techniques)

##### [Link Reducing resolution](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#reducing-resolution)

Lowering the resolution is one of the most effective ways to reduce file size:
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libx264 \
  -crf 23 \
  -vf "scale=1280:720" \
  -c:a aac \
  -b:a 128k \
  output_720p.mp4
```

Use -2 to maintain the aspect ratio while ensuring even dimensions:
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libx264 \
  -crf 23 \
  -vf "scale=1280:-2" \
  -c:a aac \
  -b:a 128k \
  output_720p.mp4
```

##### [Link Reducing frame rate](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#reducing-frame-rate)

If your original video is 60fps, reducing to 30fps can significantly decrease file size:
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libx264 \
  -crf 23 \
  -r 30 \
  -c:a aac \
  -b:a 128k \
  output_30fps.mp4
```

#### [Link Balancing compression strategies for different scenarios](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#balancing-compression-strategies-for-different-scenarios)

##### [Link Web delivery](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#web-delivery)

For online video that needs to load quickly:
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libx264 \
  -crf 23 \
  -r 30 \
  -c:a aac \
  -b:a 128k \
  output_30fps.mp4
```

The -tune fastdecode option optimizes for playback on devices with limited processing power.

##### [Link Archival quality](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#archival-quality)

For long-term storage where quality preservation is critical:
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libx264 \
  -crf 18 \
  -preset veryslow \
  -c:a aac \
  -b:a 192k \
  archive_quality.mp4
```

##### [Link Low bandwidth environments](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#low-bandwidth-environments)

For users with slow internet connections:
bash
Check Copied Copy Copy Check Copied Copy Copy

```
ffmpeg -i input_video.mp4 \
  -c:v libx264 \
  -crf 27 \
  -vf "scale=854:480" \
  -c:a aac \
  -b:a 96k \
  low_bandwidth.mp4
```

#### [Link Mux tips for evaluating compression results](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#mux-tips-for-evaluating-compression-results)

```
*   **A/B comparison** : Always compare the original and compressed videos side by side.
*   **Check dark scenes** : Compression artifacts are most visible in dark or gradient-heavy scenes.
*   **Watch for banding** : Look for color banding in skies or other smooth gradients.
*   **Motion test** : Fast-moving scenes often show compression issues more readily.
*   **Various devices** : Test your compressed video on multiple devices and screen sizes.
*  [Use Mux Data for measuring performance in the wild.](https://www.mux.com/data)
```

#### [Link Choosing the right compression approach](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#choosing-the-right-compression-approach)

Different compression strategies have various benefits and drawbacks:

##### [Link CRF-based compression:](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#crf-based-compression)

```
*   **Benefits** :
    *  Maintains consistent quality throughout the video
    *  Simpler command syntax
    *  Automatically adjusts bitrate based on content complexity
*   **Drawbacks** :
    *  File size can be unpredictable
    *  Not ideal when targeting specific file sizes
```

##### [Link Bitrate-based compression:](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#bitrate-based-compression)

```
*   **Benefits** :
    *  More predictable output file sizes
    *  Better for streaming with bandwidth constraints
*   **Drawbacks** :
    *  Quality may vary across different scenes
    *  Complex scenes may look worse than simple ones
    *  Often requires two-pass encoding for best results
```

##### [Link Resolution reduction:](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#resolution-reduction)

```
*   **Benefits** :
    *  Dramatic file size reduction
    *  Often unnoticeable on smaller screens
*   **Drawbacks** :
    *  Visible quality loss on large displays
    *  Not ideal for content with fine details
```

#### [Link Final recommendations](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#final-recommendations)

For most general-purpose video compression needs:
1. Start with H.264 and CRF 23
1. Use the "medium" or "slow" preset
1. Keep the original resolution if possible
1. Adjust audio to 128-192 kbps AAC
This approach typically yields a good balance between quality and file size for most content.
For more advanced requirements:
\* Use H.265 for about 50% better compression if compatibility isn't an issue
\* Consider two-pass encoding for more predictable file sizes
\* Experiment with different presets to find your ideal quality/time tradeoff
Remember that the quality of your output depends on the quality of your input files and the compression choices you make. Always test your compressed videos thoroughly before distributing them.
If you're looking for an API to handle video compression and optimization automatically, check out the [Mux Video API](https://mux.com/video-api), which handles transcoding, storage, and delivery.

#### [Link Video compression FAQs](https://www.mux.com/articles/how-to-compress-video-files-while-maintaining-quality-with-ffmpeg#video-compression-faqs)

**What CRF value should I use for different quality needs?**
CRF 18-20 for near-lossless archival quality, CRF 23 for high-quality web video (YouTube/Vimeo standard), CRF 28 for acceptable quality at smaller file sizes, and CRF 32+ only when file size is critical and quality loss is acceptable. Start with CRF 23 and adjust based on results—lower values if quality suffers, higher if file size needs reduction. Remember that H.265 needs CRF values 4-6 points higher than H.264 for equivalent quality.
**How much can I compress a video before quality becomes unacceptable?**
This depends heavily on content complexity and viewing conditions. Videos with lots of motion or detail compress less efficiently than static scenes. As a rule of thumb, you can typically achieve 50-70% file size reduction with CRF 23-25 H.264 before quality degradation becomes noticeable on most displays. Test compressions at different CRF values and compare side-by-side to find your threshold.
**Should I reduce resolution or increase compression for smaller files?**
Both approaches work, but resolution reduction has more dramatic impact. Dropping from 1080p to 720p typically reduces file size by 50-60% and is barely noticeable on smaller screens. Increasing CRF from 23 to 28 might reduce size by 30-40% but affects quality on all display sizes. For mobile-first content, resolution reduction is often the better choice. For large-screen viewing, stick with native resolution and adjust CRF.
**What's the difference between H.264 and H.265 for compression?**
H.265 (HEVC) achieves approximately 50% better compression than H.264 at equivalent quality—a 1080p video that's 100MB in H.264 would be roughly 50MB in H.265. However, H.265 encoding takes 2-3x longer and isn't supported on all devices, especially older hardware. Use H.264 for maximum compatibility, H.265 when file size is critical and you know viewer devices support it.
**Why does slower preset create smaller files?**
Slower presets allow the encoder more time to analyze each frame and make better compression decisions—finding optimal motion vectors, reference frames, and partition modes. The actual video quality at a given CRF stays similar, but slower presets achieve that quality with fewer bits. The tradeoff is encoding time: "veryslow" might take 5-10x longer than "fast" but produces 10-20% smaller files at the same CRF.
**Can I compress an already compressed video further?**
Yes, but each compression pass introduces additional quality loss (generation loss). If the source is already heavily compressed, further compression will make artifacts more visible. Check the source bitrate with ffprobe—if it's already low (under 2 Mbps for 1080p), further compression will significantly degrade quality. When possible, always compress from the highest quality source available rather than re-compressing compressed videos.
**How do I compress video for specific file size limits?**
Use two-pass encoding with target bitrate calculated from desired file size: (target\_size\_MB × 8192) / duration\_seconds = bitrate\_kbps. For example, for a 50MB file of a 60-second video: (50 × 8192) / 60 = 6827 kbps. Subtract audio bitrate (typically 128-192 kbps) from this to get video bitrate. Two-pass encoding ensures you hit the target size while maximizing quality within that constraint.
**Does audio compression significantly affect overall file size?**
Audio typically represents only 5-10% of total file size for video. Reducing audio from 192 kbps to 128 kbps might save 2-3% overall. Focus compression efforts on video first. However, for very short clips or audio-heavy content (podcasts with minimal video), audio bitrate matters more. For speech-only content, 96 kbps AAC or even 64 kbps is often acceptable and helps with file size.
[Arrow Right Back to Articles](https://www.mux.com/articles)
No credit card required to start using Mux.
[Start building for free Start building for free](https://dashboard.mux.com/signup)
[Docs Explore our APIs Read the docs Docs Explore our APIs Read the docs](https://www.mux.com/docs)
[Demo Get a demo Let's chat Demo Get a demo Let's chat](https://www.mux.com/sales-contact)

##### Product

```
*  [Video API](https://www.mux.com/video-api)
*  [Features](https://www.mux.com/features)
*  [On-Demand](https://www.mux.com/on-demand)
*  [Live](https://www.mux.com/live)
*  [Interactive](https://www.mux.com/interactive-live-streaming)
*  [Encoding](https://www.mux.com/encoding)
*  [Player](https://www.mux.com/player)
*  [Pricing](https://www.mux.com/pricing)
```

##### Resources

```
*  [Video glossary](https://www.mux.com/video-glossary)
*  [Learn about video](https://www.mux.com/articles)
*  [Demuxed Arrow Up Right](https://demuxed.com/)
*  [HowVideo.Works Arrow Up Right](https://howvideo.works/)
*  [Mux vs. Cloudflare Stream](https://www.mux.com/compare/cloudflare-stream)
*  [Mux vs. Vimeo](https://www.mux.com/compare/vimeo)
```

##### Developers

```
*  [Documentation](https://www.mux.com/docs)
*  [API reference](https://www.mux.com/docs/api-reference)
*  [Webhook reference](https://www.mux.com/docs/webhook-reference)
*  [Changelog](https://www.mux.com/docs/changelog)
*  [Open source software](https://www.mux.com/oss)
*  [Beta features](https://www.mux.com/beta)
*  [Contact support](https://www.mux.com/support)
```

##### Integrations

```
*  [Node](https://www.mux.com/video-for/node)
*  [Ruby](https://www.mux.com/video-for/ruby)
*  [PHP](https://www.mux.com/video-for/php)
*  [Python](https://www.mux.com/video-for/python)
*  [Elixir](https://www.mux.com/video-for/elixir)
*  [Go](https://www.mux.com/video-for/go)
*  [Astro](https://www.mux.com/video-for/astro)
*  [SvelteKit](https://www.mux.com/video-for/sveltekit)
*  [Flutter](https://www.mux.com/video-for/flutter)
*  [WordPress](https://www.mux.com/video-for/wordpress)
*  [Next.js](https://www.mux.com/video-for/next-js)
*  [React Native](https://www.mux.com/video-for/react-native)
*  [Remix.js](https://www.mux.com/video-for/remix-js)
*  [Laravel](https://www.mux.com/video-for/laravel)
```

##### Solutions

```
*  [Video platform](https://www.mux.com/solutions/video-infra-for-your-video-platform)
*  [User generated content](https://www.mux.com/solutions/video-for-ugc)
*  [Connected fitness](https://www.mux.com/solutions/video-for-fitness)
*  [Generative AI](https://www.mux.com/solutions/video-for-generative-ai)
*  [Vercel users](https://www.mux.com/solutions/video-for-vercel)
```

##### Company

```
*  [Blog](https://www.mux.com/blog)
*  [Team](https://www.mux.com/team)
*  [Customers](https://www.mux.com/customers)
*  [Partners](https://www.mux.com/partners)
*  [Jobs](https://www.mux.com/jobs)
*  [Startup Program](https://www.mux.com/startups)
*  [Powered by Mux Program](https://www.mux.com/powered-by-mux)
*  [Sign up for our newsletter](https://www.mux.com/newsletter/signup)
*  [Download press kit](https://www.mux.com/files/mux-press-kit.zip)
```

[Mux on Twitter Twitter, or I guess it's called X now](https://twitter.com/muxhq) [Mux on LinkedIn LinkedIn](https://www.linkedin.com/company/mux/) [Mux on GitHub GitHub](https://www.github.com/muxinc/) [Mux on YouTube YouTube](https://www.youtube.com/channel/UCGaddSlVSK83POSytkL21rQ)
Looking for standalone Mux Data?
[Go to Mux Data Go to Mux Data](https://www.mux.com/data)
© Mux, Inc. 2026 [Terms](https://www.mux.com/terms) [Security](https://www.mux.com/security) [Privacy](https://www.mux.com/privacy) [Cookies](https://www.mux.com/cookies) [Sitemap](https://www.mux.com/sitemap)
[Status: Good](https://status.mux.com/)