---
tags:
  - notebooklm-import
notebook: "M_Music Production 1"
category: "research"
---

# WebSync metadata

* title: ASIO Problem? | Trouble Shooting | ACE Studio Docs
* url: https://docs.acestudio.ai/trouble-shooting
* date: 2026-02-22T21:57:02.608Z

hashtag

Whether ACE Studio or any DAW, playback works perfectly under ASIO mode when it's the only application that output sounds. But things may become unexpected when two applications both want to use an ASIO device at the same time.

Most ASIO drivers can only serve one application at the same time due to the purpose of low latency. That means ACE Studio may fail to initialize ASIO driver and not be able to playback when your DAW has been using it, conversely, your DAW may fail to playback when ACE Studio already launched under ASIO mode.

Solutions hashtag

ACE Bridge 2 is a VST3 instrument plugin for building an audio bridge between ACE Studio and your DAW. It can be installed together with ACE Studio.

With ACE Bridge 2 connected between ACE Studio and your DAW, ACE Studio's playback will be sent directlly to the track in your DAW where ACE Bridge 2 lies, and no audio device will be used by ACE Studio until ACE Bridge 2 is off. In this case, you can hear all sounds come from your DAW with any configured ASIO device.

circle-info

Please note:If you launch ACE Studio first and select an ASIO device for its audio device before launching your DAW, your DAW may still have problem with playback even the ACE Bridge 2 is on. In this case, you could change the audio device into None in ACE Studio before launching your DAW.

Try ASIO4ALL

ASIO4ALL is an universal ASIO driver, which utilizes low-level WDM drivers to achieve low-latency while keeping a wide compatibility device range. It implements a multi-client ASIO device, a.k.a ASIO4ALL can be used simultaneously by different DAWs.

For how to install and use ASIO4ALL, and more general information on it, please consult their official website: https://asio4all.org/ arrow-up-right <https://asio4all.org/>

circle-info

Please note:ASIO4ALL in general can bring you a low-latency experience, but it may have less-capable performance or a tighter feature set compared to the native ASIO driver provided by your sound card vendor. If ASIO4ALL is not suitable for your case, use ACE Bridge will always be a viable solution.

Next Can’t launch ACE Studio?

Last updated