---
tags:
  - notebooklm-import
notebook: "M_Music Production 1"
category: "research"
---

# WebSync metadata

* title: Cloning A Voice for Vocal Synth | ACE Studio Docs
* url: https://docs.acestudio.ai/voice-cloning/cloning-a-voice-for-vocal-synth
* date: 2026-02-22T21:57:02.609Z

hashtag

This is a feature to customize your own vocal synth model by uploading your vocal samples. AI will learn the timbre and singing style based on the samples you upload, and clone a digital version of your voice.

After the customization, you can use your voice to generate vocals from MIDI and lyrics just like our pre-made AI voices in ACE Studio.

circle-check

Your cloned AI voice is private under your account, no one else can access it without your authorization.

hashtag hashtag chevron-right Clean Dry Vocals hashtag <#clean-dry-vocals>

High-quality voices require clean and dry vocal samples:

Without any reverb, delay, chorus effects

Without background noise

Without instrumentals or any non-human sounds

Without any harmonies or vocal doubles

30-100 mins of singing vocal samples are recommended for a voice. The more samples you provide, the more singing details AI can learn, but it brings fewer benefits when you reach over 120 minutes.

Room Reflections

Vocals recorded with big room reflections might cause error recognitions and result in unexpected model performances.

Vocals from stem splitter

When you are using vocal remover or stem splitter for vocals, the output quality might be damaged too low for training. For a higher quality voice model, please optionally use vocals from stem splitter.

chevron-right Recording Samples hashtag <#recording-samples>

*Quality microphone with audio interface*

Professional microphones with audio interfaces bring high-quality vocals. You'll need recording software to connect to your interface, record, edit, and mix your vocals.

When recording for a voice model, avoid microphones that are not built for singing:

Phone or laptop mics

Lapel or headset mics

Karaoke mics

Earphone mics or bluetooth earphones like air pods (these are usually for phone talks)

*Recording environment*

1.

Unwanted background noises can include people talking, electrical hums and buzzes, traffic and outdoor noise, as well as movements of accessories or objects. To prevent these noises from interfering with your recording, it is important to select a quiet location. Choose a place where you can minimize or eliminate unexpected noise disturbances.

2.

Sound reflections can occur due to the presence of hard, level surfaces, resulting in reverberation or echoes in your recordings. This can give your tracks a hollow or distant quality, detracting from the desired intimacy and clarity.

3.

Try clapping your hands sharply in the room and listen carefully. If you perceive a fluttering sound or a prolonged echo, it indicates the presence of reverb issues.

4.

To address this, incorporate soft materials that can absorb sound. Consider using carpets, rugs, or thick curtains to significantly reduce reflections. Covering hard floors and, if possible, hanging curtains over windows, as well as placing furniture with fabric coverings in the room, can be beneficial.

5.

Avoid using hard surfaces as they contribute to the problem. If you cannot afford professional acoustic panels, you can utilize everyday items such as canvas paintings, tapestries, or foam tiles to break up these surfaces.

6.

When setting up your microphone, be mindful of its placement. Avoid positioning it too close to walls or in corners. Instead, aim for the center of the room or experiment with different locations to find the optimal spot with minimal reverb.

*Headphone bleed*

During recordings, particularly when capturing vocals, it is common for the audio from headphones to bleed into the microphone. This issue arises when the volume of the headphones is set too high or when open-back headphones are being used. This might be acceptable when recording for a song, but try to avoid this bleeding when recording for your voice model.

*Microphone placement*

For regular volume, it is recommended to position yourself about 2 inches away from the microphone. However, for louder phrases or when belting, it is advisable to increase the distance to around 4-6 inches. It is important to note that you should always stay closer than 12 inches from the microphone to maintain optimal audio capture.

Creating Space for Belting

When engaging in belting techniques, it's important to allow yourself ample space, both in terms of microphone distance and the size of the room you're in. Excessive sound isolation, such as being confined in a closet or booth, or surrounding your microphone with foam, can easily result in overloading the microphone capsule. If you're unsure, it's advisable to incorporate more room sound when performing belted phrases.

chevron-right Singing Languages hashtag <#singing-languages>

*Basic custom slot*

Only one singing language will be supported in your voice model trained under basic custom slot.

*Pro custom slot*

Your voice trained under pro custom slot can go multilingual.

*Languages in your samples*

During the training process, each sample file will be processed individually and treated as a single-language file. It is important to avoid mixing phrases from different languages within the same sample file.

When uploading samples, please ensure that you place them under the appropriate language tab. Even if you are uploading samples for a basic custom slot, you have the flexibility to upload samples in different languages if needed. Keeping the samples organized by language will help maintain clarity and improve the training process.

*Upcoming languages*

We are continuously working on developing new singing languages for the custom voice feature.

For your new voice:

New languages will be supported by new pro custom slots.

New languages will be one of the options to be supported by new basic custom slots.

For your existing voice:

New languages will be supported when retraining your pro custom slots.

New languages will be optional when retraining your basic custom slots.

chevron-right Singing or Speech hashtag <#singing-or-speech>

Singing samples and speech samples can both be accepted for training your singing voice model.

Your voice can learn:

Timbre from your singing samples and speech samples, but plase note: for a person, timbre of speaking can be different to singing, which usually can not represent the true performance of singing.

Singing style from your singing samples

Your voice can't learn:

Singing style from your speech samples

chevron-right File Quality Settings hashtag <#file-quality-settings>

The audio quality of your samples directly impacts the quality of your voice.

We recommend you to set your audio quality in:

Bit Depth = 16-bit

Sample Rate = 44.1khz or 48khz

Lossless file format (.wav or.flac)

chevron-right Post-Processing hashtag <#post-processing>

To maintain the natural character and clarity of your target voice:

*No overlaps:* multi-layered vocals can complicate AI's analysis. Place the overlapped takes at back and stick to a single vocal track to ensure the AI can accurately process and learn from your samples.

*No hard cuts:* hard cuts can create abrupt starts or ends, which are not normal in a natural singing sound and can introduce clicks or pops. Use smooth fades at the beginning and end of the vocal clip for a more natural transition.

*No duplicating sections:* Duplicated sections don't help for the training. Your voice model benefits from the natural variation of performance.

*Control the volume:* Make sure your samples stay around 30-50% of your meter. Use a volume rider or automation to make sure volume levels are consistent across your entire dataset. The aim is to create a consistent volume level across the recording while keeping the dynamics within sections.

hashtag

After preparing your datasets, you can go to browser Custom Voice Page <https://acestudio.ai/app/custom-voice/vocal-synth> to select a Custom Slot, upload your vocal samples, and start the training.

A Basic Custom Slots brings you a monolingual voice with 5 versions.

A Pro Custom Slot brings you a multilingual voice with 5 versions.

Click on a slot to start uploading your samples.

After all samples being uploaded, the training will start automatically. You can check the status by refreshing the webpage.

When you see the training page turns into the voice cloning management page, your voice is all set up. It will be shown in your voice library in ACE Studio. If you cannot see it, try to relaunch ACE Studio.

circle-info

*Pro Tips*

If you are seeking exclusive performance and character for a voice, like the best results in different vocal ranges or emotions. It would be better to divide samples for several voices.

Here is an example:

Mike is a professional singer and would like to customize his own voice. He can both do well as tenor and bass. So it would be better to train 2 voice voices:

Train a high-tone&powerful voice based on samples that are mostly high-tone and powerful performances.

Train a bass voice based on samples that are mostly low-tone phrases.

hashtag

Click on the Retrain button to retrain your voice.

Retraining will remove your previous voice under this slot and take down any deployed singers associated with the voice. AI will start training a completely new voice from scratch using the new dataset. Prior to initiating the retraining process, you have the option to either retain the historical samples within this slot and upload additional new samples, or you can choose to clear the historical samples and only use the newly uploaded samples.

When preparing new samples, please note:

If the duration of newly added samples is significantly smaller than the already uploaded samples, for example, adding 1 min of new sample to a dataset of 30 mins, retraining may not bring about significant changes in the performance of the voice.

Retraining will not change the type of your slot.

You can switch the supported language of your basic custom slot by retraining.

circle-info

*When should I retrain my voice?*

When your datasets has better quality or larger amount, you can use them to iteratively improve your voice

When you are not satisfied with the current result and want to adjust your datasets

When a new singing language skill being released

hashtag chevron-right Versions hashtag <#versions>

AI learns incrementally from your data, analyzing each sample in a step-by-step process. As learning deepens, the number of steps increases. Training with a small or limited-quality dataset, such as one not designed for singing but for speech, may require only a few steps. In contrast, a larger and more diverse dataset might necessitate additional steps for a thorough fit. However, excessive training steps can lead to overfitting, potentially degrading the performance of your voice with unpredictable outcomes.

By the end of training, you will get several versions based on different training steps from Rare to Well-done. You can find the best version by switching deployment and comparing each other.

chevron-right Blend Voices hashtag <#blend-voices>

Blending voices results in a hybrid voice. You can customize your voice to sound more like your target voice by adjusting the ratios of the blended voices. To do this, navigate to the slots management page and click the ‘blend voices’ button located under each version.

After blending, your voice will adopt the new voice characteristics. To apply these changes, you will need to refresh your voice by restarting ACE Studio.

chevron-right Deploy to ACE Studio hashtag <#deploy-to-ace-studio>

For Basic custom slots and Pro custom slots, after deploying a version, you can switch deployment from one version to another. You need to re-launch ACE Studio after each deployment to refresh your voice library.

Last updated