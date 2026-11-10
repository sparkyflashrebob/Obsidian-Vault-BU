---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

**Compete in HackAPrompt 2.0, the world's largest AI Red-Teaming competition!**
Check it out →Explore CoursesAI Courses
Master AI and prompt engineering
Live Courses
Interactive expert-led sessions
Certification Exams
Get Certified in AI

##### DIFFICULTY LEVEL

##### Beginner CoursesIntermediate CoursesAdvanced CoursesView All CoursesRECOMMENDED COURSES

NEW

###### ChatGPT for Everyone

Master ChatGPT fundamentals and advanced techniques
Start LearningNEW

###### Introduction to Prompt Engineering

Learn the fundamentals of crafting effective prompts
Start LearningLIVE

###### Live Courses

Interactive masterclasses with expert instructors

* Explore Live Courses
* Docs
* Blog
  Resources
* CommunityHackAPrompt7-Day Free CoursePrompt Hacking GuideVocabularyHelp Center
* Pricing
* For BusinessLive AI WorkshopsOn Demand AI CoursesSolutions
* About

### Start Learning for FreeLearn PromptingPrompt Engineering Guide 😃 Basics 💼 Applications 🧙‍♂️ Intermediate 🧠 Advanced Special Topics ⚖️ Reliability 🔓 Prompt Hacking 🖼️ Image Prompting 🌱 New Techniques 🔧 Models 🗂️ RAG 🤖 Agents 💪 Prompt Tuning 🔁 Language Model Inversion 🔨 Tooling 🎲 Miscellaneous Resources 📚 Bibliography 📦 Prompted Products 🛸 Additional Resources 🔥 Hot Topics ✨ Credits English🖼️ Image Prompting[🟢 Introduction](https://learnprompting.org/docs/image_prompting/introduction)Introduction

🟢 This article is rated [easy](https://learnprompting.org/docs/introduction#header-4)Reading Time: 4 minutes Last updated on August 7, 2024
[Sander Schulhoff](https://learnprompting.org/docs/introduction#header-4)
Takeaways

* **Image Prompting Techniques** : This chapter outlines how to create consistent, high-quality images with AI models like [DALLE](https://learnprompting.org/docs/tooling/IDEs/DALLE) and Stable Diffusion, focusing on effective image prompting techniques.
  Figuring out the best prompt to create a perfect image is a particular challenge. Research into methods to do so is not quite as developed as text prompting. This may be due to inherent challenges in creating objects that are fundamentally subjective and often lack good accuracy metrics. However, fear not, as the image prompting community has made great discoveries about how to prompt various image models.
  This guide covers basic image-prompting techniques, and we highly encourage that you look at the great resources at the end of the chapter. Additionally, we provide an example of the end-to-end image prompting process below.

#### An Example of Image Prompting

Here I will go through an example of how I created the images for the front page of this course. I had been experimenting with a low poly style for a deep [reinforcement learning](https://learnprompting.org/vocabulary/reinforcement_learning) neural radiance field project. I liked the low poly style and wanted to use it for this course's images.
I wanted an astronaut, a rocket, and a computer for the images on the front page.
I did a bunch of research into how to create low poly images, on [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/) and other sites, but couldn't find anything super helpful.
I decided to just start with DALLE and the following prompt, and see what happened.

###### Prompt

Low poly white and blue rocket shooting to the moon in front of a sparse green meadow
I thought these results were pretty decent for a first try; I particularly liked the bottom left rocket.
Next, I wanted a computer in the same style:

###### Prompt

Low poly white and blue computer sitting in a sparse green meadow
Finally, I needed an astronaut! This prompt seemed to do the trick:

###### Prompt

Low poly white and blue astronaut sitting in a sparse green meadow with low poly mountains in the background
I thought the second one was decent.
Now I had an astronaut, a rocket, and a computer. I was happy with them, so I put them on the front page. After a few days and input from my friends I realized the style just wasn't consistent 😔.
I did some more research on [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/) and found people using the word isometric. I decided to try that out, using Stable Diffusion instead of DALLE. I also realized that I needed to add more modifiers to my prompt to constrain the style. I tried this prompt:

###### Prompt

A low poly world, with an astronaut in a white suit and blue visor sitting in a sparse green meadow with low poly mountains in the background. Highly detailed, isometric, 4K
These weren't great, so I decided to start on the rocket instead

###### Prompt

A low poly world, with a white and blue rocket blasting off from a sparse green meadow with low poly mountains in the background. Highly detailed, isometric, 4K
These are not particularly good, but after a bit of iterating around here, I ended up with
Now I needed a better laptop:

###### Prompt

A low poly world, with a white and blue laptop sitting in a sparse green meadow with low poly mountains in the background. The screen is completely blue. Highly detailed, isometric, 4K
I got some inconsistent results; I like the bottom right one, but I decided to go in a different direction.

###### Prompt

A low poly world, with a glowing white and blue gemstone sitting in a sparse green meadow with low poly mountains in the background. Highly detailed, isometric, 4K
This wasn't quite right. Let's try something magical and glowing.

###### Prompt

A low poly world, with a glowing white and blue gemstone magically floating in the middle of the screen above a sparse green meadow with low poly mountains in the background. Highly detailed, isometric, 4K
I liked these, but wanted the stone in the middle of the screen.

###### Prompt

A low poly world, with a glowing blue gemstone magically floating in the middle of the screen above a sparse green meadow with low poly mountains in the background. Highly detailed, isometric, 4K
Somewhere around here, I used SD's ability to have a previous image provide some influence for future images. Thus I arrived at:
Finally, I was on to the astronaut.

###### Prompt

A low poly world, with an astronaut in a white suite and blue visor is sitting in a sparse green meadow with low poly mountains in the background. Highly detailed, isometric, 4K
At this point, I was sufficiently happy with the style consistency between my three images to use them on the website. The main takeaways for me were that this was a very iterative, research-heavy process, and I had to modify my expectations and ideas as I experimented with different prompts and models.

##### Sander Schulhoff

Sander Schulhoff is the CEO of HackAPrompt and Learn Prompting. He created the first Prompt Engineering guide on the internet, two months before ChatGPT was released, which has taught 3 million people how to prompt ChatGPT. He also partnered with OpenAI to run the first AI Red Teaming competition, HackAPrompt, which was 2x larger than the White House's subsequent AI Red Teaming competition. Today, HackAPrompt partners with the Frontier AI labs to produce research that makes their models more secure. Sander's background is in Natural Language Processing and deep reinforcement learning. He recently led the team behind The Prompt Report, the most comprehensive study of prompt engineering ever done. This 76-page survey, co-authored with OpenAI, Microsoft, Google, Princeton, Stanford, and other leading institutions, analyzed 1,500+ academic papers and covered 200+ prompting techniques.

##### 🟢 Fix Deformed Generations

##### 🟢 Midjourney

##### 🟢 Quality Boosters

##### 🟢 Repetition

##### 🟢 Resources

##### 🟢 Shot type

##### 🟢 Style Modifiers

##### 🟢 Weighted Terms

#### Footnotes

Parsons, G. (2022). The DALLE 2 Prompt Book. <https://dallery.gallery/the-dalle-2-prompt-book/>[↩](https://dallery.gallery/the-dalle-2-prompt-book/)
Rombach, R., Blattmann, A., Lorenz, D., Esser, P., & Ommer, B. (2021). High-Resolution Image Synthesis with Latent Diffusion Models. [↩](https://learnprompting.org#user-content-fnref-2)
Ramesh, A., Dhariwal, P., Nichol, A., Chu, C., & Chen, M. (2022). Hierarchical Text-Conditional Image Generation with CLIP Latents. [↩](https://learnprompting.org#user-content-fnref-3)
On this page

* An Example of Image Prompting