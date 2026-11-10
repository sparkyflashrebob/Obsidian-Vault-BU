---
tags:
  - notebooklm-import
notebook: "M_Music Production 1"
category: "research"
---

# WebSync metadata

* title: Local Rendering | ACE Studio Docs
* url: https://docs.acestudio.ai/ai-rendering/local-rendering
* date: 2026-02-22T21:57:02.608Z

Turbo Mode

Turbo Mode offloads the heavy synthesis steps of Verse25 to your local CPU/GPU, reducing cloud latency and accelerating the overall render time.

System requirements

To take advantage of Turbo Mode, which utilizes your GPU to accelerate rendering, we recommend having a capable graphics card:

windows *Windows:*

*NVIDIA:* GeForce RTX 2060 or newer

*AMD:* Radeon RX 6600 XT, RX 7600, or newer

*Intel:* Any dedicated GPU with Arc branding

*Laptops:* A dedicated GPU within the same performance class should work well. For optimal results, we recommend connecting to AC power and enabling your system's performance profile.

apple *macOS:*

*Apple Silicon:* M1 Max, M2, or newer

*Intel Macs:* Turbo Mode may work if your Mac has a dedicated GPU, though performance can vary. For the best experience, we recommend upgrading to an M-series Mac.

circle-info

*Note:*

For Macs that support the Power Mode feature, performance may decrease in Low Power mode. If you notice slower performance while using Turbo Mode, try switching to Automatic or High Power mode. For more information, see Apple's support article arrow-up-right <https://support.apple.com/en-us/101613>.

hashtag

Local rendering consumes a significant amount of local computing power, so it requires a certain level of computer configuration.

During the onboarding setup, ACE Studio will automatically test your device's performance. Turbo Mode will be enabled if your device is supported. You can also manage it in the [Rendering] tab of preferences window. To enable Turbo Mode manually, you must pass a performance test.

1

hashtag

In the [Rendering] preference  window, click the Run Test button to start the test.

Close other large programs to avoid misjudgment caused by performance consumption from other software.

2

hashtag

Don't close ACE Studio or launch other large programs.

3

Get result

Turbo Mode will be automatically enabled if your device passes the test. Otherwise, ACE Studio will stay in cloud rendering, which is still good.

hashtag

If local rendering tasks exceed acceptable time limits, users will be prompted to switch back to cloud rendering.

circle-exclamation

*For Windows Users with Multiple GPUs*

To ensure Turbo Mode runs with maximum performance, we strongly recommend assigning your dedicated (High-performance) GPU to ACE Studio in Windows settings. This is especially important for laptops.

1.

Find *ACE Studio* in the application list. If it's not there, add it manually.

2.

Click on ACE Studio, select *Options*, and set the GPU preference to *High performance*.

circle-exclamation

*Update Your Graphics Driver for the Best Experience*

To ensure optimal performance and stability on Windows, we recommend downloading the latest driver from your graphics card manufacturer's website.

Rendering Timing By Default

Local rendering starts when playback is triggered.

Pre-rendering

When pre-rendering is enabled, local rendering operates in real-time (after changes).

Rendering State

Un-rendered pieces are marked with a gray brace inside the time ruler.

Rendering Scope

The model dynamically detects the rendering range. When a small area is modified, only the modified area will be re-rendered.

Last updated