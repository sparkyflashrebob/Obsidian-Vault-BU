---
tags:
  - notebooklm-import
notebook: "M_Music Production 1"
category: "research"
---

Mixing is a fundamental process in electronic music composition and production, involving the alignment of independent tracks in time and blending them into a cohesive composite [1, 2]. From an aesthetic perspective, the core challenge in mixing is to balance the opposing processes of fusion (melding sounds into a unified whole) and fission (keeping sounds perceptually distinct) [3]. The goal of any good mix is to achieve **transparency**, where each instrument occupies its own space within the soundstage and can be clearly heard, thus avoiding clutter—a jumble of simultaneous sounds that obscure each other [4, 5].

Here are the most common suggestions for mixing tracks:

* **Understanding Aesthetic Dimensions**
  The key to mixing lies in the efficient use of aesthetic dimensions, including **Time, Amplitude, Spectrum, Space, and Motion**, to optimize content by balancing diverse elements [6].
* **Setting Levels and Volume**

  + **Prioritize Volume:** Volume is considered the most powerful mixing tool [7]. Adjusting volume sliders is crucial for establishing the relative importance of each track [8].
  + **Reference the Kick Drum:** The kick drum is nearly always the track with the highest level and should ideally reach an optimum output of 0 decibels (0dB), with all other track levels adjusted relative to it [8]. Avoid pushing everything to the highest level, which can result in a "total mess" [9].
  + **Foreground, Middle Ground, Background:** Clearly define which elements should be in the foreground (loudest, most prominent), middle ground, and background, and mix other elements down accordingly [10-13]. Listeners can only truly focus on about three main elements at any given moment [10].
  + **Gain Staging:** Use a trim plugin on every mix channel and adjust the gain to peak between -6 and -20dBFS [14]. This helps maintain signal integrity and provides headroom for processing [14, 15].
  + **Avoid "Slideritis":** Resist the urge to constantly creep up volume sliders, as this leads to a cluttered, incomprehensible mix [9, 16].
* **Equalization (EQ)**

  + **Clarity and Frequency Masking:** EQ is essential for addressing frequency masking, where two instruments with similar tones compete for space, making them hard to distinguish [17, 18].
  + **Cut First, Boost Carefully:** Generally, it's better to **cut problematic frequencies** first to create space and clarity, as cuts often sound more natural [19, 20]. Boosts should be discrete, gentle, and applied to enhance the character of an instrument [19, 21].
  + **High-Pass/Low-Pass Filters:** Use high-pass filters (or low cuts) at 120Hz or higher on instruments other than the kick or bass to remove unneeded low frequencies [20, 22, 23]. Low-pass filters can be used on sounds that might compete with hi-hats, often around 7-8kHz [20].
  + **Common Problem Frequencies:**
    - **Mud:** Often found between 350-650Hz (or 100-400Hz for the whole mix) [20, 24, 25].
    - **Harshness:** Often around 1.6kHz to 2kHz [25].
    - **Nasal Quality:** Can be reduced around 500Hz [25].
    - **Presence/Definition:** 3kHz to 10kHz can enhance presence; 6kHz to 15kHz adds brightness and "air" [26, 27].
  + **Identify Offending Frequencies:** Boost the gain on a narrow frequency band and sweep from low to high to find frequencies that sound harsh, then lower their gain [20].
  + **Automation of EQ:** Automate filters and EQs to create dynamic movement and interest [28-32].
* **Panning and Stereo Field**

  + **Create Space:** Panning separates elements in space, giving the mix a three-dimensional quality and allowing more simultaneous elements [33, 34].
  + **Center Placement:** Kick drums, bass, snare, and lead vocals are typically panned to the center [22, 35-39]. Other elements are often panned to the sides [22, 37].
  + **Mono vs. Stereo:** Mono sources collapse to a point, while stereo sources occupy a field [33]. Use mono sounds for central elements to ensure energy is shared by both speakers [40, 41]. Many virtual instruments are stereo, but using too many stereo signals can lead to a mix lacking definition [42].
  + **Avoid Clashing Frequencies:** Pan instruments with similar frequency ranges away from each other (e.g., piano left, guitar right) to promote clarity [34, 35, 43].
  + **Balance:** Maintain a balanced stereo field, avoiding too much information on one side [44].
  + **Sub-bass in Mono:** Keep sub-frequencies mono, even if upper frequencies are stereo, for solidity and shared energy [39, 41, 45, 46].
  + **Width:** Stereo widening can be applied during mastering, but overuse can create a "hole" in the middle of the mix [47, 48].
* **Effects (Reverb, Delay, Compression, Sidechaining)**

  + **Return Tracks:** Use return tracks (also known as aux tracks) for effects like reverb, delay, compression, or distortion, allowing multiple tracks to send to the same effect [49]. Make sure effects on return tracks are 100% wet [50].
  + **Sidechain Compression:**
    - **Kick and Bass:** Essential in electronic music to prevent the kick and bass from competing for low-end space [51-55]. The bass's volume is automatically ducked down when the kick plays, creating a "pumping" sound and helping the kick cut through [55].
    - **Vocals and Instruments:** Can be used to duck instruments (e.g., lead guitar) when vocals play to ensure vocal clarity [53, 56-59].
    - **Avoiding Clicks/Pops:** Adjust the amp envelope's attack and release, or the compressor's release time, look-ahead value, or ratio [60]. Use "anti-click trigger smoothing" or the LFO's smooth control if available [60].
  + **Parallel Compression:** Send rhythm component tracks to a group, then send a small amount of that group to a compressor on an aux bus. Mix the uncompressed and compressed signals to achieve a thicker, more defined rhythm without increasing transients [61-64].
  + **Reverb and Delay:** Used to create a sense of width and space [50, 65, 66]. Use subtle reverb on main drums for a consistent "room" sound, but be careful with the kick [67]. Delays can add depth and complexity, especially triplet delays for melodies or percussion [68]. Remove low frequencies from delays to keep the mix clean [68].
* **Arrangement and Compositional Decisions**

  + **Less is More:** Many of the best music tracks use minimal material [45]. Avoid adding too many elements, which can lead to a cluttered, dense mix that lacks energy [69, 70].
  + **Layering:** Layering different timbres can create richer, fuller sounds (e.g., kick drums, snares, basslines) [71-75]. Ensure layers have their own frequency space [75, 76].
  + **Build-up, Breakdown, Drop:** Understand these common structural elements in dance music [77-79]. Use filter automation, particularly low-pass filters, to control energy during build-ups and drops [32, 80].
  + **Asynchronous/Polyrhythmic Loops:** Experiment with loops of differing lengths or offset from the grid to create interesting rhythmic effects and variations [81-85].
  + **Unique Events:** Insert single, unrepeated sounds or gestures to add unpredictability and mark transitions [86].
* **Monitoring and Workflow**

  + **Listen at Low Volume:** Mix at a relatively low level (below 80 dB C-weighted) to prevent ear fatigue, which affects perception of high frequencies [87-89].
  + **Check in Mono:** Frequently check your mix in mono to identify phase cancellation and accurately assess relative volume levels [36, 88, 89].
  + **Use Reference Tracks:** Listen to professionally mastered tracks of the same genre to train your ears and compare your mix [89-92].
  + **Start with Drums & Bass:** A common approach is to mix drums and bass first to establish the groove, then gradually introduce other instruments [89, 93, 94].
  + **Templates:** Create customized DAW templates with preferred tempos, output settings, and pre-loaded instruments/effects to save time and streamline workflow [95].
  + **Automation:** Use automation on filters, volume, reverb, and delays to create change over time and add emotion to robotic sounds [7, 96].
  + **"Sends Only" Routing:** In live performance, specific tracks (like metronomes or cues) can be routed to "sends only" so they are heard exclusively in headphone mixes and not through the main speakers [97].
  + **Submixing/Stems:** Mix groups of tracks (e.g., all drums) down to a stereo pair (a "stem") to simplify the final mix [98-100]. This divide-and-conquer strategy helps manage complex mixes [98].
  + **Record Practice Mixes:** Record your practice mixes and listen back with "fresh ears" to objectively analyze areas for improvement [101].
* **Avoiding Common Mistakes**

  + **"Fix it in the Mix" Mentality:** Avoid the mindset that problems can be fixed later in the mix. Poorly programmed timbres should be replaced or re-recorded [102-104].
  + **Over-Processing:** Don't apply effects to every instrument if only one or two are needed. Ask why an effect is being applied; if it's to fix a bad timbre, reconsider [20, 105, 106].
  + **Redlining the Mixer:** Excessively boosting EQs or volumes can cause clipping and distortion, reducing overall audio quality [15, 107, 108]. Ensure sufficient headroom [109].
  + **Notching out too much:** If you find you must use a narrow Q or cuts larger than 4dB to remove a problem area, the issue likely lies with a poor mix that needs to be revisited at the source [25].