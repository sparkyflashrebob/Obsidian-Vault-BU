Getting the most understanding inputs and outputs
- output
	- what you want to get out
- prompt
	- that is the input
- TCREI
	- THOUGHTFULLY
	- CREATE
	- REALLY
	- EXCELLENT
	- INPUTS
- OR
	- TASK
	- CONTEXT
	- REFERENCES
	- EVALUATE
	- ITERATE

![[Pasted image 20250515164401.png]]

# Specify the task
- describe the [[task]]
- foundation of any prompt
- what do you want it to do for you
- like writing a sentence asking someone to do something for you

i.e.
- write a list
- draft a speech
- create an image

NEED TO BE CLEAR AND SPECIFIC
- Includes providing a [[persona]] and a format
- persona is the expertise you want the gen AI to draw from
	- science expert or industry analyst
	- or create an output geared to a specific audience like a manager or your team

- [[format]] is what you expect the output to look like
	- bulleted list?
	- Table

i.e. Movie Critic - specialize in Italian film
- create a table
- greatest italian films of the 1970's
- separate into genres, like
	- thrillers
	- dramas
	- comedies
- include 100-word summary of each movie
	- also details about the production
		- director
		- release year


# Include necessary context
- oversharing can be good
- the more relevant the details the better
- provide [[background information]]
	- goals
	- reason for the task
	- what you have tried before
- this rounds out the model
- this is called [[context]]
- vital for creating great prompts


i.e. HOW WAS DNA DISCOVERED?
- science expert
- new curriculum for a local college
- tell me in a couple of "engaging" pargraphs how DNA discovered
	- impact on the world
- write for those unfamiliar with science 
	- try not to be dry or unintelligible
- grab the students attention to make a good first impression

[[Context]] provides potiential for the longest piece of theprompt
- as you add, consider [[delimiters]]
	- add extra context & differentiate parts of your inputs
	- delimiters are special symbols
		- keep prompts tidy
		- increase likelyhood of a useful output
		- like labels or guardrails

## Popular Delimiters
- Triple quotes (""") 
	- distinction between different elements of the prompt
		- task & context
	- use to clearly separate and signify different
		- meanings
		- purposes

- XLM tags
	- labels
		- (" < task > ") start
		- (" < /task> ") end

- Markdown tags
	- These are symbols you can use in prompts to add formatting. For example, if you were to use a gen AI tool to copy-edit your work, you could surround text with “_” to italicize it or “**” to bold it. This preserves your formatting as you move it into a gen AI tool, which generally uses plain, or unformatted text.

# Provide References
- examples or additional resources 
	- might resemble your output
	- i.e.
		- show your hairstylist an image of what you would like
- can include
		- text
		- images
		- audio references
- show how they fit your objective
	- AI can try to emulate
	- a few should be enough

i.e. write product description for a watch - like it is in a magazine
- instead 
	- write a prompt that provide relevant detail, references two external resources and identifies a format

- _Sunglasses: Our latest collection of handcrafted, heritage-inspired sunglasses features details like UV-protective lenses in shades specifically chosen to complement each frame—all at a price that won't break the bank. Plus, we made these sunglasses with vintage-inspired acetate frames and a keyhole bridge._
    
- _Cardholder: Crafted in smooth Italian leather, this double-sided cardholder is designed to carry your cash and credit cards without the bulk of a full wallet. Fun fact: this cardholder is made in Naples, Italy, and will look great when you treat your friends to a round of summer spritzes._


## **Evaluate your output** 

Different AI models are trained on unique data and rely on different programming techniques. 

Some models may be better suited to specific uses like writing code or brainstorming ideas, while others might have limited outputs because of their training sets. 

No matter the model, running the same prompt multiple times will likely render different results because of how gen AI tools process data. 

That’s why it’s so important to evaluate your output. 

Before you use any AI-generated information, text, or materials, critically evaluate that the output is accurate, unbiased, relevant, and consistent before incorporating it into your workflows. 

If the output isn’t what you’re looking for, you should iterate on your prompt.

## **Take an iterative approach** 

There will be times when your prompt simply isn’t leading to the output you need. 

That’s where our **ABI** advice comes in: **A**lways **B**e **I**terating. 

If you find an output lacking, continue clarifying what you need until it’s just right.

The prompting framework sets you up to give gen AI tools the information they need to generate useful outputs—and it’s designed to apply across all kinds of tools and models. 

So whatever your gen AI tool of choice, make sure you specify your task, provide context and references, evaluate your outputs, and iterate your inputs.



