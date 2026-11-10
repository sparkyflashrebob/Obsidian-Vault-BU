---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

Skip to main content Open navigation Go to Reddit Home [Log In](https://www.reddit.com/login/) Log in to Reddit Open settings menu

* [Log In / Sign Up](https://www.reddit.com/login/)
* [Advertise on Reddit](https://www.reddit.com/login/)
* [Try Reddit Pro BETA](https://www.reddit.com/login/)
* [Shop Collectible Avatars](https://www.reddit.com/login/) 
  Copy link
  Copy link
   [Go to PromptEngineering](https://www.reddit.com/login/) [r/PromptEngineering](https://www.reddit.com/login/)[r/PromptEngineering](https://www.reddit.com/login/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

### Members Online • [peridotqueens](https://www.reddit.com/user/peridotqueens/) AI Prompting Tips from a Power User: How to Get Way Better Responses

### [Tips and Tricks](https://www.reddit.com/user/peridotqueens/) 1. Stop Asking AI to “Write X” and Start Giving It a Damn Framework

AI is great at filling in blanks. It’s bad at figuring out what you actually want. So, make it easy for the poor thing.
🚫 Bad prompt: “Write an essay about automation.”
✅ Good prompt:
Title: [Insert Here] Thesis: [Main Argument] Arguments: - [Key Point #1] - [Key Point #2] - [Key Point #3] Counterarguments: - [Opposing View #1] - [Opposing View #2] Conclusion: [Wrap-up Thought]
Now AI actually has a structure to follow, and you don’t have to spend 10 minutes fixing a rambling mess.
Or, if you’re making characters, force it into a structured format like JSON:
{ "name": "John Doe", "archetype": "Tragic Hero", "motivation": "Wants to prove himself to a world that has abandoned him.", "conflicts": { "internal": "Fear of failure", "external": "A rival who embodies everything he despises." }, "moral\_alignment": "Chaotic Good" }
Ever get annoyed when AI contradicts itself halfway through a story? This fixes that.

### 2. The “Lazy Essay” Trick (or: How to Get AI to Do 90% of the Work for You)

If you need AI to actually write something useful instead of spewing generic fluff, use this four-part scaffolded prompt:
Assignment: [Short, clear instructions] Quotes: [Any key references or context] Notes: [Your thoughts or points to include] Additional Instructions: [Structure, word limits, POV, tone, etc.]
🚫 Bad prompt: “Tell me how automation affects jobs.”
✅ Good prompt:
Assignment: Write an analysis of how automation is changing the job market. Quotes: “AI doesn’t take jobs; it automates tasks.” - Economist Notes: - Affects industries unevenly. - High-skill jobs benefit; low-skill jobs get automated. - Government policy isn’t keeping up. Additional Instructions: - Use at least three industry examples. - Balance positives and negatives.
Why does this work? Because AI isn’t guessing what you want, it’s building off your input.

### 3. Never Accept the First Answer—It’s Always Mid

Like any writer, AI’s first draft is never its best work. If you’re accepting whatever it spits out first, you’re doing it wrong.
How to fix it:
First Prompt: “Explain the ethics of AI decision-making in self-driving cars.”
Refine: “Expand on the section about moral responsibility—who is legally accountable?”
Refine Again: “Add historical legal precedents related to automation liability.”
Each round makes the response better. Stop settling for autopilot answers.

### 4. Make AI Pick a Side (Because It’s Too Neutral Otherwise)

AI tries way too hard to be balanced, which makes its answers boring and generic. Force it to pick a stance.
🚫 Bad: “Explain the pros and cons of universal basic income.”
✅ Good: “Defend universal basic income as a long-term economic solution and refute common criticisms.”
Or, if you want even more depth:
✅ “Make a strong argument in favor of UBI from a socialist perspective, then argue against it from a libertarian perspective.”
This forces AI to actually generate arguments, instead of just listing pros and cons like a high school essay.

### 5. Fixing Bad Responses: Change One Thing at a Time

If AI gives a bad answer, don’t just start over—fix one part of the prompt and run it again.
Too vague? Add constraints.
Mid: “Tell me about the history of AI.”
Better: “Explain the history of AI in five key technological breakthroughs.”
Too complex? Simplify.
Mid: “Describe the implications of AI governance on international law.”
Better: “Explain how AI laws differ between the US and EU in simple terms.”
Too shallow? Ask for depth.
Mid: “What are the problems with automation?”
Better: “What are the five biggest criticisms of automation, ranked by impact?”
Tiny tweaks = way better results.

### Final Thoughts: AI Is a Tool, Not a Mind Reader

If you’re getting boring or generic responses, it’s because you’re giving AI boring or generic prompts.
✅ Give it structure (frameworks, templates)
✅ Refine responses (don’t accept the first answer)
✅ Force it to take a side (debate-style prompts)
AI isn’t magic. It’s just really good at following instructions. So if your results suck, change the instructions.
Got a weird AI use case or a frustrating prompt that’s not working? Drop it in the comments, and I’ll help you tweak it. I have successfully created a CYOA game that works with minimal hallucinations, a project that has helped me track and define use cases for my autistic daughter's gestalts, and almost no one knows when I use AI unless I want them to.
For example, this guide is obviously (mostly) AI-written, and yet, it's not exactly generic, is it?
 [Share](https://www.reddit.com/user/peridotqueens/)  Sort by: Best Open comment sort options Best
Top
New
Controversial
Old
Q&A
 [mmistermeh](https://www.reddit.com/user/peridotqueens/) • I strongly agree that frameworks make a huge difference. One of my favorite prompting techniques is to have the AI reference or write a framework first, then use that framework to generate the content. This is especially helpful if you don't know a good framework yourself.
Example: I want to generate great song lyrics, but have no idea how.
Prompt:
Choose a well known and effective framework for writing song lyrics, like how John Truby’s Anatomy of a Story is great for writing fiction. Describe the framework in detail in such a way that it could be used as a guide to write amazing song lyrics.
Often this is enough to get a great framework, but you can always edit yourself or tell the AI what you want changed. (Searching the web for a framework works well if you aren't getting a good one.)
When you're happy with the framework description, you can generate the content you actually want, and it will be of much higher quality.
Smart people have already figured out a framework for 99.99% of everything you could want.
}  [peridotqueens](https://www.reddit.com/user/peridotqueens/) • • Edited
Having the AI generate the framework and then editing it myself is something I do often. I tend to use DeepSeek to create structured content, edit that myself, and then use ChatGPT or Claude to produce whatever content. If Claude adds a project feature, I will likely switch to Claude entirely.
}  [staerne](https://www.reddit.com/user/staerne/) • Claude has projects... With project knowledge and instructions. You can even make it reference Google drive files and all.
}  [peridotqueens](https://www.reddit.com/user/peridotqueens/) • • Edited
Can you upload files into the project to function as instructions? My only other reservation is the sheer amount of time I've put into pruning gippity's various features & that I (so far) prefer it for creative projects.
}  [noonecudsaveme](https://www.reddit.com/user/noonecudsaveme/) • Yes, Claude Pro has all that! You can add instructions and upload files to separate projects.
This [demonstration](https://youtu.be/gj8oM8Z4FI8?si=-YbqZJcQlOOQHVPn) shows it all. Thanks for the quality post, appreciate it!
}  [more replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mh28aio/) [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mh28aio/)  [ContributionFun3037](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mh28aio/) • Hey! Can you drop some sample frameworks for me too? I'm terrible at prompting, and most of the time, I end up fighting with AI responses.
Also, thanks for the insights!
} [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mgxlo0p/) [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mgxlo0p/) [deleted] • Comment removed by moderator
}  [peridotqueens](https://www.reddit.com/user/peridotqueens/) • it depends on what you're trying to achieve! so, for example, i have a framework for reasoning through a philosophical theory i've put together; i have a framework for analyzing US politics that i update; i have a framework for essays to make them sound more like me; etcetera.
for most of these frameworks, i explained what i was setting out to do to DeepSeek ((DeepSeek is really good at structured logic)), asked it to create an AI-friendly framework, and then edited the frameworks myself to optimize them. if you message me, i can send you a sample of a framework to give you idea or help you come up with prompts for the framework you are looking to make.
} [deleted] • I messaged you, thanks in advance!
}  [Ok-Neighborhood7237](https://www.reddit.com/user/Ok-Neighborhood7237/) • This is great .. Thanks for sharing. Can you also share it with me? Much appreciated
}  [Pixel1999](https://www.reddit.com/user/Pixel1999/) • I'm starting to dive deeper into AI; I'd love a framework sample! Ty!
}  [4Jazbo69](https://www.reddit.com/user/4Jazbo69/) • I'm realy new to AI and would love to get proficient with frameworks
}  [desijays](https://www.reddit.com/user/desijays/) • COuld you please share with me as well. I'm still trying to grapple with a AI approach based on frameworks. Whatever you share could help me as well.
} [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mgnbnvx/) [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mgnbnvx/) [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mgnbnvx/) [deleted] • Comment removed by moderator
}  [Learning-2-Prompt](https://www.reddit.com/user/Learning-2-Prompt/) • Nice one! Now built a template which matches a deck of persona prompts with the framework you want to use, use that sophisticated verson of the persona prompt, initiate the framework and watch the magic happen.
} [deleted] • This is so damn smart
}  [Glittering-Koala-750](https://www.reddit.com/user/Glittering-Koala-750/) • do this on 3 different AIs - then get them to compare - rinse and repeat
} [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mgn7oa0/) [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mgn7oa0/)  [SeesAem](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mgn7oa0/) • i love your tips. i m using your technic and i also try some other. i use the structure framework as a start, for instance if i have a task A:
Who are the expert or most suited person to help me accomplish Task A?
You are now Expert A with expertise [context]. You help me accomplish Task A. Everytime I give you [input] you give me [output structure].
Repeat process I found that most important is to have short prompt and structured result like you said with the JSON schema for example. I use many of these framework / structure as a specific tool that I can use everytime i need to perform specific tasks that are recurring. I hit the wall when i want to have a split within one of my "tools" (i call them uselet) that is to take the result and tinker with it outside of my chat. I dont know if one of you is doing it this way but i think we all know that the more you mix various "roles" and the more you exchange with your chat the more we get hallucination and non-sense results.
}  [lionelhutz-](https://www.reddit.com/user/lionelhutz-/) • I'll often write a draft and tell GPT to "make it better". I've tried going into more detail but find sometimes letting it take the reigns works pretty well. These are sales outreach emails I write for work.
}  [peridotqueens](https://www.reddit.com/user/peridotqueens/) • I think for something like an email, "please improve this," can work well. I primarily use AI for creative projects & essays.
} [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mgy7jtb/)  [laterral](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mgy7jtb/) • The thing I struggle with is your 5. Sounds good to tweak one thing at a time, but won’t you run out of context if the AI repeats the essay so many times for all little tweaks? How do you deal with that?
}  [kra73ace](https://www.reddit.com/user/kra73ace/) • I do it by dictation, title, argument, several data points I can think of, instructions to stick to my stuff and not get creative on this one...
I do ask for creativity occasionally and occasionally it works but more often it will be just a list of tropes and cliches. So not very original.
}  [zankalony](https://www.reddit.com/user/zankalony/) • I like this approach, will give it a try
} [deleted] • Comment removed by moderator
}  [AutoModerator](https://www.reddit.com/user/AutoModerator/) • Hi there! Your post was automatically removed because your account is less than 3 days old. We require users to have an account that is at least 3 days old before they can post to our subreddit.
Please take some time to participate in the community by commenting and engaging with other users. Once your account is older than 3 days, you can try submitting your post again.
If you have any questions or concerns, please feel free to message the moderators for assistance.
*I am a bot, and this action was performed automatically. Please* *contact the moderators of this subreddit* *if you have any questions or concerns.*
} [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mosk3dh/)  [focuslife](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mosk3dh/) • Frameworks, specifics and contextual nuance are everything.
Thanks for this.
}  [bot-psychology](https://www.reddit.com/user/bot-psychology/) • Thanks for the tips.
One question: do you have a sense for why JSON helps for character definition (and, presumably, in few other places)? It's a bit counterintuitive because the models are trained on natural language. I'd expect the json to be harder to "understand".
}  [peridotqueens](https://www.reddit.com/user/peridotqueens/) • because they aren't just trained on natural language! they're also trained on structured text formats like JSON and YAML. these structures reduce ambiguity & offer high tokenization optimization - which basically just means a lower chance of hallucination.
for example, you can check out my structured CYOA chatgame & how I used JSONs to scaffold a consistent gameplay structure and world with minimal error.
also, if you personally don't know how to structure text into JSON, deepseek is pretty damn good at it. better than any of the other models besides claude, but claude has a low limit for free users/latest version often isn't available for free users.
} [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mglou22/)  [Ronin\_74](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mglou22/) • The more frameworks, the more AI delerium. Give context, explain what you want. Unless u stated it shall act more human like, the result will be a perfect mirror of your input.
}  [peridotqueens](https://www.reddit.com/user/peridotqueens/) • frameworks help *reduce* hallucination. what are you on about?
}  [cheaphomemadeacid](https://www.reddit.com/user/cheaphomemadeacid/) • any source for that? I'm curios if this is actually the case
}  [peridotqueens](https://www.reddit.com/user/peridotqueens/) • i don't think you really need a source. it's common sense. providing context produces better responses because AI do not inherently know what context to draw from. but here: [https://www.miquido.com/ai-glossary/ai-prompt-frameworks/#:~:text=Key%20benefits%20of%20AI%20prompt%20frameworks%20\*,for%20different%20industries%2C%20audiences%2C%20or%20content%20types](https://www.miquido.com/ai-glossary/ai-prompt-frameworks/#:~:text=Key%20benefits%20of%20AI%20prompt%20frameworks%20*,for%20different%20industries%2C%20audiences%2C%20or%20content%20types).
this is a new field, so there aren't exactly an abundance of sources. i've learned most of these tips through trial and error. what i can do, if you message me, is show you things i've written using my frameworks (particularly that 'lazy essay' framework) and demonstrate how it improves responses.
}  [Glittering-Koala-750](https://www.reddit.com/user/Glittering-Koala-750/) • also stating do not guess, assume, hallucinate helps but not infallible

### } [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mh8isdb/) [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mh8isdb/) [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mh8isdb/) [More replies](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mh8isdb/) More posts you may like

[This is going around today’AI is making prompt engineering obsolete’. What do you think?](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mh8isdb/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/comment/mh8isdb/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online This is going around today’AI is making prompt engineering obsolete’. What do you think?

* upvotes · comments
   [Tips from 177-ville: how to overcome a plateau](https://www.reddit.com/r/PromptEngineering/comments/1kgy8f0/this_is_going_around_todayai_is_making_prompt/) [r/LSAT](https://www.reddit.com/r/PromptEngineering/comments/1kgy8f0/this_is_going_around_todayai_is_making_prompt/) • [r/LSAT](https://www.reddit.com/r/LSAT/) The Reddit LSAT Forum. The best place on Reddit for LSAT advice. The Law School Admission Test (LSAT) is the test required to get into an ABA law school. Check out the sidebar for intro guides. Post any questions you have, there are lots of redditors with LSAT knowledge waiting to help.

##### Members Online Tips from 177-ville: how to overcome a plateau

* upvotes · comments
   [Anyone else feel like more than 50% of using AI is just writing the right prompt?](https://www.reddit.com/r/LSAT/comments/1hoyik7/tips_from_177ville_how_to_overcome_a_plateau/) [r/PromptEngineering](https://www.reddit.com/r/LSAT/comments/1hoyik7/tips_from_177ville_how_to_overcome_a_plateau/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online Anyone else feel like more than 50% of using AI is just writing the right prompt?

* upvotes · comments
   [AI Prompting (4/10): Controlling AI Outputs—Techniques Everyone Should Know](https://www.reddit.com/r/PromptEngineering/comments/1kojd0v/anyone_else_feel_like_more_than_50_of_using_ai_is/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1kojd0v/anyone_else_feel_like_more_than_50_of_using_ai_is/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online AI Prompting (4/10): Controlling AI Outputs—Techniques Everyone Should Know

* upvotes · comments
   [Prompt Engineering an AI Therapist](https://www.reddit.com/r/PromptEngineering/comments/1igline/ai_prompting_410_controlling_ai_outputstechniques/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1igline/ai_prompting_410_controlling_ai_outputstechniques/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online Prompt Engineering an AI Therapist

* upvotes · comments
   [What is the best prompt you've used or created to humanize AI text.](https://www.reddit.com/r/PromptEngineering/comments/1kraux3/prompt_engineering_an_ai_therapist/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1kraux3/prompt_engineering_an_ai_therapist/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online What is the best prompt you've used or created to humanize AI text.

* upvotes · comments
   [Using AI to give prompts for an AI.](https://www.reddit.com/r/PromptEngineering/comments/1kx7izd/what_is_the_best_prompt_youve_used_or_created_to/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1kx7izd/what_is_the_best_prompt_youve_used_or_created_to/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online Using AI to give prompts for an AI.

* upvotes · comments
   [Tricks I Found for Writing Better AI Prompts](https://www.reddit.com/r/PromptEngineering/comments/1kem941/using_ai_to_give_prompts_for_an_ai/) [r/ChatGPTPromptGenius](https://www.reddit.com/r/PromptEngineering/comments/1kem941/using_ai_to_give_prompts_for_an_ai/) • [r/ChatGPTPromptGenius](https://www.reddit.com/r/ChatGPTPromptGenius/) Welcome to r/ChatGPTPromptGenius, the subreddit where you can find and share the best AI prompts! Our community is dedicated to curating a collection of high-quality & standardized prompts that can be used to generate creative and engaging AI conversations. Whether you're looking for inspiration or just want to see what others are doing with AI, this is the place to be! This subreddit has a companion browser extension called AI Prompt Genius.

##### Members Online Tricks I Found for Writing Better AI Prompts

* upvotes
   [Tired of Manual Influencer Searches? Get a Curated List By Just… Describing It (Feedback Needed)](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1j2uovz/tricks_i_found_for_writing_better_ai_prompts/) [r/influencermarketing](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1j2uovz/tricks_i_found_for_writing_better_ai_prompts/) • [r/influencermarketing](https://www.reddit.com/r/influencermarketing/) Share popular threads and discussions around influencer marketing. Learn how to work with popular social media creators and bloggers to promote your brand.

##### Members Online Tired of Manual Influencer Searches? Get a Curated List By Just… Describing It (Feedback Needed)

* comments
   [Question. How long until prompt engineering is obsolete because AI is so good at interpreting what you mean that it's no longer required?](https://www.reddit.com/r/influencermarketing/comments/1j5j9ap/tired_of_manual_influencer_searches_get_a_curated/) [r/PromptEngineering](https://www.reddit.com/r/influencermarketing/comments/1j5j9ap/tired_of_manual_influencer_searches_get_a_curated/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online Question. How long until prompt engineering is obsolete because AI is so good at interpreting what you mean that it's no longer required?

* upvotes · comments
   [AI Prompting (2/10): Chain-of-Thought Prompting—4 Methods for Better Reasoning](https://www.reddit.com/r/PromptEngineering/comments/1ittdkx/question_how_long_until_prompt_engineering_is/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1ittdkx/question_how_long_until_prompt_engineering_is/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online AI Prompting (2/10): Chain-of-Thought Prompting—4 Methods for Better Reasoning

* upvotes · comments
   [5 prompting principles I learned after 1 year using AI to create content](https://www.reddit.com/r/PromptEngineering/comments/1if2dlo/ai_prompting_210_chainofthought_prompting4/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1if2dlo/ai_prompting_210_chainofthought_prompting4/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online 5 prompting principles I learned after 1 year using AI to create content

* upvotes · comments
   [How to turn AI into your personal code tutor](https://www.reddit.com/r/PromptEngineering/comments/1km46r7/5_prompting_principles_i_learned_after_1_year/) [r/AIAssisted](https://www.reddit.com/r/PromptEngineering/comments/1km46r7/5_prompting_principles_i_learned_after_1_year/) • [r/AIAssisted](https://www.reddit.com/r/AIAssisted/) r/AIAssisted is for people who actually use AI—not just talk about it. We swap prompts, expose broken tools, share wins (and fails), and post the stuff no one's putting in tutorials. If you're tired of the hype and want real insight, welcome.

##### Members Online How to turn AI into your personal code tutor

* upvotes · comment
   [I got tired of losing and re-writing AI prompts—so I built a CLI tool](https://www.reddit.com/r/AIAssisted/comments/1hckpmj/how_to_turn_ai_into_your_personal_code_tutor/) [r/PromptEngineering](https://www.reddit.com/r/AIAssisted/comments/1hckpmj/how_to_turn_ai_into_your_personal_code_tutor/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online I got tired of losing and re-writing AI prompts—so I built a CLI tool

* upvotes · comments
   [Self-analysis prompt I made to test with AI. works surprisingly well.](https://www.reddit.com/r/PromptEngineering/comments/1k4pvfj/i_got_tired_of_losing_and_rewriting_ai_promptsso/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1k4pvfj/i_got_tired_of_losing_and_rewriting_ai_promptsso/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online Self-analysis prompt I made to test with AI. works surprisingly well.

* upvotes · comments
   [What's the best way to ask AI (e.g. ChatGPT, Claude) to create an AI prompt?](https://www.reddit.com/r/PromptEngineering/comments/1kwcqo5/selfanalysis_prompt_i_made_to_test_with_ai_works/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1kwcqo5/selfanalysis_prompt_i_made_to_test_with_ai_works/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online What's the best way to ask AI (e.g. ChatGPT, Claude) to create an AI prompt?

* upvotes · comments
   [AI Prompting (7/10): Data Analysis — Methods, Frameworks & Best Practices Everyone Should Know](https://www.reddit.com/r/PromptEngineering/comments/1jjdg3k/whats_the_best_way_to_ask_ai_eg_chatgpt_claude_to/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1jjdg3k/whats_the_best_way_to_ask_ai_eg_chatgpt_claude_to/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online AI Prompting (7/10): Data Analysis — Methods, Frameworks & Best Practices Everyone Should Know

* upvotes · comments
   [I Created 50 Different AI Personalities - Here's What Made Them Feel 'Real'](https://www.reddit.com/r/PromptEngineering/comments/1iiye3s/ai_prompting_710_data_analysis_methods_frameworks/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1iiye3s/ai_prompting_710_data_analysis_methods_frameworks/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online I Created 50 Different AI Personalities - Here's What Made Them Feel 'Real'

* upvotes · comments
   [Advice needed: Logic vs Code, how to use Gemini more effectively](https://www.reddit.com/r/PromptEngineering/comments/1l6bbmc/i_created_50_different_ai_personalities_heres/) [r/GoogleGeminiAI](https://www.reddit.com/r/PromptEngineering/comments/1l6bbmc/i_created_50_different_ai_personalities_heres/) • [r/GoogleGeminiAI](https://www.reddit.com/r/GoogleGeminiAI/) Google Gemini is a family of multimodal large language models developed by Google DeepMind, serving as the successor to LaMDA and PaLM 2. Comprising Gemini Ultra, Gemini Pro, and Gemini Nano, it was announced on December 6, 2023, positioned as a contender to OpenAI's GPT-4. This sub reddit is not affiliated with Google.

##### Members Online Advice needed: Logic vs Code, how to use Gemini more effectively

* upvotes · comments
   [What prompts do AI text “humanizing” tools like bypass gpt and unaimytext use?](https://www.reddit.com/r/GoogleGeminiAI/comments/1hj3x35/advice_needed_logic_vs_code_how_to_use_gemini/) [r/PromptEngineering](https://www.reddit.com/r/GoogleGeminiAI/comments/1hj3x35/advice_needed_logic_vs_code_how_to_use_gemini/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online What prompts do AI text “humanizing” tools like bypass gpt and unaimytext use?

* upvotes · comments
   [Advanced prompt to summarize chats](https://www.reddit.com/r/PromptEngineering/comments/1jtge8o/what_prompts_do_ai_text_humanizing_tools_like/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1jtge8o/what_prompts_do_ai_text_humanizing_tools_like/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online Advanced prompt to summarize chats

* upvotes · comments
   [I've come up with a new Prompting Method and its Blowing my Mind](https://www.reddit.com/r/PromptEngineering/comments/1kqdrf9/advanced_prompt_to_summarize_chats/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1kqdrf9/advanced_prompt_to_summarize_chats/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online I've come up with a new Prompting Method and its Blowing my Mind

* upvotes · comments
   [I'm struggling to motivate my team to use AI, how do you deal with this?](https://www.reddit.com/r/PromptEngineering/comments/1kktm1z/ive_come_up_with_a_new_prompting_method_and_its/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1kktm1z/ive_come_up_with_a_new_prompting_method_and_its/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online I'm struggling to motivate my team to use AI, how do you deal with this?

* upvotes · comments
   [Make AI write good articles that people want to read with this prompt system](https://www.reddit.com/r/PromptEngineering/comments/1kmielg/im_struggling_to_motivate_my_team_to_use_ai_how/) [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/comments/1kmielg/im_struggling_to_motivate_my_team_to_use_ai_how/) • [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) Prompt engineering is the application of engineering practices to the development of prompts - i.e., inputs into generative models like GPT or Midjourney.

##### Members Online Make AI write good articles that people want to read with this prompt system

* upvotes · comments
   [How to Get the Right AI to Respond in a Dual AI Conversation](https://www.reddit.com/r/PromptEngineering/comments/1l1i5oz/make_ai_write_good_articles_that_people_want_to/) [r/ChatFAI](https://www.reddit.com/r/PromptEngineering/comments/1l1i5oz/make_ai_write_good_articles_that_people_want_to/) • [r/ChatFAI](https://www.reddit.com/r/ChatFAI/) ChatFAI is an AI-powered chatbot application that allows you to chat with your favorite characters from movies, TV shows, books, history, and more.

##### Members Online How to Get the Right AI to Respond in a Dual AI Conversation

* upvotes · comments

###### Related discussion

[Best Way to Prompt ChatGPT](https://www.reddit.com/r/ChatFAI/comments/1ib78hx/how_to_get_the_right_ai_to_respond_in_a_dual_ai/) 
[Reddit Rules](https://www.reddit.com/r/ChatFAI/comments/1ib78hx/how_to_get_the_right_ai_to_respond_in_a_dual_ai/)[Privacy Policy](https://www.reddit.com/r/ChatFAI/comments/1ib78hx/how_to_get_the_right_ai_to_respond_in_a_dual_ai/)[User Agreement](https://www.reddit.com/r/ChatFAI/comments/1ib78hx/how_to_get_the_right_ai_to_respond_in_a_dual_ai/)[Reddit, Inc. © 2025. All rights reserved.](https://www.reddit.com/r/ChatFAI/comments/1ib78hx/how_to_get_the_right_ai_to_respond_in_a_dual_ai/)

* [Log In / Sign Up](https://www.reddit.com/r/ChatFAI/comments/1ib78hx/how_to_get_the_right_ai_to_respond_in_a_dual_ai/)
* [Advertise on Reddit](https://www.reddit.com/r/ChatFAI/comments/1ib78hx/how_to_get_the_right_ai_to_respond_in_a_dual_ai/)
* [Try Reddit Pro BETA](https://www.reddit.com/r/ChatFAI/comments/1ib78hx/how_to_get_the_right_ai_to_respond_in_a_dual_ai/)
* [Shop Collectible Avatars](https://www.reddit.com/r/ChatFAI/comments/1ib78hx/how_to_get_the_right_ai_to_respond_in_a_dual_ai/)