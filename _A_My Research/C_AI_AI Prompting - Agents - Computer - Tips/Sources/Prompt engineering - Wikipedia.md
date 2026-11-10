---
tags:
  - notebooklm-import
notebook: "C_AI_AI Prompting - Agents - Computer - Tips"
category: "research"
---

Jump to contentMain menu Navigation

* Main page
* Contents
* Current events
* Random article
* About Wikipedia
* Contact us
  Contribute
* Help
* Learn to edit
* Community portal
* Recent changes
* Upload file
* Special pages
* Search Donate
* Create account
* Log in
* Donate
* Create account
* Log in
* Pages for logged out editors [learn more](https://en.wikipedia.org/wiki/Help:Introduction)[Contributions](https://en.wikipedia.org/wiki/Help:Introduction)
* [Talk](https://en.wikipedia.org/wiki/Help:Introduction)
* [(Top)](https://en.wikipedia.org/wiki/Help:Introduction) 
  [1 History](https://en.wikipedia.org/wiki/Help:Introduction) 
  [2 Text-to-text](https://en.wikipedia.org/wiki/Help:Introduction) [2.1 Chain-of-thought](https://en.wikipedia.org/wiki/Help:Introduction) 
  [2.2 In-context learning](https://en.wikipedia.org/wiki/Help:Introduction) 
  [2.3 Self-consistency decoding](https://en.wikipedia.org/wiki/Help:Introduction) 
  [2.4 Tree-of-thought](https://en.wikipedia.org/wiki/Help:Introduction) 
  [2.5 Prompting to estimate model sensitivity](https://en.wikipedia.org/wiki/Help:Introduction) 
  [2.6 Automatic prompt generation](https://en.wikipedia.org/wiki/Help:Introduction) [2.6.1 Retrieval-augmented generation](https://en.wikipedia.org/wiki/Help:Introduction) 
  [2.6.2 Graph retrieval-augmented generation](https://en.wikipedia.org/wiki/Help:Introduction) 
  [2.6.3 Using language models to generate prompts](https://en.wikipedia.org/wiki/Help:Introduction) 
  [3 Text-to-image](https://en.wikipedia.org/wiki/Help:Introduction) [3.1 Prompt formats](https://en.wikipedia.org/wiki/Help:Introduction) 
  [3.2 Artist styles](https://en.wikipedia.org/wiki/Help:Introduction) 
  [4 Non-text prompts](https://en.wikipedia.org/wiki/Help:Introduction) [4.1 Textual inversion and embeddings](https://en.wikipedia.org/wiki/Help:Introduction) 
  [4.2 Image prompting](https://en.wikipedia.org/wiki/Help:Introduction) 
  [4.3 Using gradient descent to search for prompts](https://en.wikipedia.org/wiki/Help:Introduction) 
  [5 Limitations](https://en.wikipedia.org/wiki/Help:Introduction) 
  [6 Prompt injection](https://en.wikipedia.org/wiki/Help:Introduction) 
  [7 References](https://en.wikipedia.org/wiki/Help:Introduction)

### Prompt engineering

* [العربية](https://en.wikipedia.org/wiki/Help:Introduction)
* [বাংলা](https://en.wikipedia.org/wiki/Help:Introduction)
* [Bosanski](https://en.wikipedia.org/wiki/Help:Introduction)
* [Català](https://en.wikipedia.org/wiki/Help:Introduction)
* [Čeština](https://en.wikipedia.org/wiki/Help:Introduction)
* [Deutsch](https://en.wikipedia.org/wiki/Help:Introduction)
* [Español](https://en.wikipedia.org/wiki/Help:Introduction)
* [Esperanto](https://en.wikipedia.org/wiki/Help:Introduction)
* [Euskara](https://en.wikipedia.org/wiki/Help:Introduction)
* [فارسی](https://en.wikipedia.org/wiki/Help:Introduction)
* [Français](https://en.wikipedia.org/wiki/Help:Introduction)
* [한국어](https://en.wikipedia.org/wiki/Help:Introduction)
* [Հայերեն](https://en.wikipedia.org/wiki/Help:Introduction)
* [IsiZulu](https://en.wikipedia.org/wiki/Help:Introduction)
* [עברית](https://en.wikipedia.org/wiki/Help:Introduction)
* [Magyar](https://en.wikipedia.org/wiki/Help:Introduction)
* [मराठी](https://en.wikipedia.org/wiki/Help:Introduction)
* [Nederlands](https://en.wikipedia.org/wiki/Help:Introduction)
* [日本語](https://en.wikipedia.org/wiki/Help:Introduction)
* [Norsk nynorsk](https://en.wikipedia.org/wiki/Help:Introduction)
* [Polski](https://en.wikipedia.org/wiki/Help:Introduction)
* [Português](https://en.wikipedia.org/wiki/Help:Introduction)
* [Русский](https://en.wikipedia.org/wiki/Help:Introduction)
* [Slovenščina](https://en.wikipedia.org/wiki/Help:Introduction)
* [Suomi](https://en.wikipedia.org/wiki/Help:Introduction)
* [Svenska](https://en.wikipedia.org/wiki/Help:Introduction)
* [ไทย](https://en.wikipedia.org/wiki/Help:Introduction)
* [Türkçe](https://en.wikipedia.org/wiki/Help:Introduction)
* [Українська](https://en.wikipedia.org/wiki/Help:Introduction)
* [Tiếng Việt](https://en.wikipedia.org/wiki/Help:Introduction)
* [粵語](https://en.wikipedia.org/wiki/Help:Introduction)
* [中文](https://en.wikipedia.org/wiki/Help:Introduction)
  [Edit links](https://en.wikipedia.org/wiki/Help:Introduction)
  Tools Actions
* [Read](https://en.wikipedia.org/wiki/Help:Introduction)
* [Edit](https://en.wikipedia.org/wiki/Help:Introduction)
* [View history](https://en.wikipedia.org/wiki/Help:Introduction)
  General
* [What links here](https://en.wikipedia.org/wiki/Help:Introduction)
* [Related changes](https://en.wikipedia.org/wiki/Help:Introduction)
* [Upload file](https://en.wikipedia.org/wiki/Help:Introduction)
* [Permanent link](https://en.wikipedia.org/wiki/Help:Introduction)
* [Page information](https://en.wikipedia.org/wiki/Help:Introduction)
* [Cite this page](https://en.wikipedia.org/wiki/Help:Introduction)
* [Get shortened URL](https://en.wikipedia.org/wiki/Help:Introduction)
* [Download QR code](https://en.wikipedia.org/wiki/Help:Introduction)
  Print/export
* [Download as PDF](https://en.wikipedia.org/wiki/Help:Introduction)
* [Printable version](https://en.wikipedia.org/wiki/Help:Introduction)
  In other projects
* [Wikimedia Commons](https://en.wikipedia.org/wiki/Help:Introduction)
* [Wikidata item](https://en.wikipedia.org/wiki/Help:Introduction)
  From Wikipedia, the free encyclopedia Structuring text as input to generative artificial intelligence The neutrality of this article is [disputed](https://en.wikipedia.org/wiki/Wikipedia:NPOV_dispute). Relevant discussion may be found on the [talk page](https://en.wikipedia.org/wiki/Talk:Prompt_engineering). Please do not remove this message until [conditions to do so are met](https://en.wikipedia.org/wiki/Template:POV#When_to_remove). *( May 2025 )* (Learn how and when to remove this message *)* **Prompt engineering** is the process of structuring or crafting an instruction in order to produce the best possible output from a [generative artificial intelligence](https://en.wikipedia.org/wiki/Generative_artificial_intelligence) (AI) model.[ 1 ]
  A *prompt* is [natural language](https://en.wikipedia.org/wiki/Natural_language) text describing the task that an AI should perform.[ 2 ] A prompt for a text-to-text [language model](https://en.wikipedia.org/wiki/Large_language_model) can be a query, a command, or a longer statement including context, instructions, and conversation history. Prompt engineering may involve phrasing a query, specifying a style, choice of words and grammar,[ 3 ] providing relevant context, or describing a character for the AI to mimic.[ 1 ]
  When communicating with a [text-to-image](https://en.wikipedia.org/wiki/Text-to-image) or a text-to-audio model, a typical prompt is a description of a desired output such as "a high-quality photo of an astronaut riding a horse"[ 4 ] or "Lo-fi slow BPM electro chill with organic samples".[ 5 ] Prompting a text-to-image model may involve adding, removing, or emphasizing words to achieve a desired subject, style, layout, lighting, and aesthetic.[ 6 ]

#### History

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=1)]
In 2018, researchers first proposed that all previously separate tasks in [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing) (NLP) could be cast as a question-answering problem over a context. In addition, they trained a first single, joint, multi-task model that would answer any task-related question like "What is the sentiment" or "Translate this sentence to German" or "Who is the president?"[ 7 ]
The [AI boom](https://en.wikipedia.org/wiki/AI_boom) saw an increase in the amount of "prompting technique" to get the model to output the desired outcome and avoid [nonsensical output](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)), a process characterized by [trial-and-error](https://en.wikipedia.org/wiki/Trial_and_error).[ 8 ] After the release of [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT) in 2022, prompt engineering was soon seen as an important business skill, albeit one with an uncertain economic future.[ 1 ]
A repository for prompts reported that over 2,000 public prompts for around 170 datasets were available in February 2022.[ 9 ] In 2022, the *chain-of-thought* prompting technique was proposed by [Google](https://en.wikipedia.org/wiki/Google) researchers.[ 10 ][ 11 ] In 2023, several text-to-text and text-to-image prompt databases were made publicly available.[ 12 ][ 13 ] The Personalized Image-Prompt (PIP) dataset, a generated image-text dataset that has been categorized by 3,115 users, has also been made available publicly in 2024.[ 14 ]

#### Text-to-text

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=2)]
Multiple distinct prompt engineering techniques have been published.

##### Chain-of-thought

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=3)] See also: [Reflection (artificial intelligence)](https://en.wikipedia.org/wiki/Reflection_(artificial_intelligence))According to Google Research, *chain-of-thought* (CoT) prompting is a technique that allows [large language models](https://en.wikipedia.org/wiki/Large_language_models) (LLMs) to solve a problem as a series of intermediate steps before giving a final answer. In 2022, [Google Brain](https://en.wikipedia.org/wiki/Google_Brain) reported that chain-of-thought prompting improves reasoning ability by inducing the model to answer a multi-step problem with steps of reasoning that mimic a [train of thought](https://en.wikipedia.org/wiki/Train_of_thought).[ 10 ][ 15 ] Chain-of-thought techniques were developed to help LLMs handle multi-step reasoning tasks, such as [arithmetic](https://en.wikipedia.org/wiki/Arithmetic) or [commonsense reasoning](https://en.wikipedia.org/wiki/Commonsense_reasoning) questions.[ 16 ][ 17 ]
For example, given the question, "Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?", Google claims that a CoT prompt might induce the LLM to answer "A: The cafeteria had 23 apples originally. They used 20 to make lunch. So they had 23 - 20 = 3. They bought 6 more apples, so they have 3 + 6 = 9. The answer is 9."[ 10 ] When applied to [PaLM](https://en.wikipedia.org/wiki/PaLM), a 540 billion parameter [language model](https://en.wikipedia.org/wiki/Language_model), according to Google, CoT prompting significantly aided the model, allowing it to perform comparably with task-specific [fine-tuned](https://en.wikipedia.org/wiki/Fine-tuning_(machine_learning)) models on several tasks, achieving [state-of-the-art](https://en.wikipedia.org/wiki/State_of_the_art) results at the time on the GSM8K [mathematical reasoning](https://en.wikipedia.org/wiki/Mathematical_reasoning)[benchmark](https://en.wikipedia.org/wiki/Mathematical_reasoning).[ 10 ] It is possible to fine-tune models on CoT reasoning datasets to enhance this capability further and stimulate better [interpretability](https://en.wikipedia.org/wiki/Interpretability).[ 18 ][ 19 ]
An example of a CoT prompting:[ 20 ]
Q: {question} A: Let's think step by step.
As originally proposed by Google,[ 10 ] each CoT prompt included a few Q&A examples. This made it a *few-shot* prompting technique. However, according to researchers at Google and the [University of Tokyo](https://en.wikipedia.org/wiki/University_of_Tokyo), simply appending the words "Let's think step-by-step"[ 20 ] was also effective, which makes CoT a *zero-shot* prompting technique. [OpenAI](https://en.wikipedia.org/wiki/OpenAI) claims that this prompt allows for better scaling as a user no longer needs to formulate many specific CoT Q&A examples.[ 21 ]

##### In-context learning

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=4)]
*In-context learning* , refers to a model's ability to temporarily learn from prompts. For example, a prompt may include a few examples for a model to learn from, such as asking the model to complete " *maison* → house, *chat* → cat, *chien* →" (the expected response being *dog* ),[ 22 ] an approach called *few-shot learning* .[ 23 ]
In-context learning is an [emergent ability](https://en.wikipedia.org/wiki/Large_language_model_emergent_abilities)[\[ 24 \]](https://en.wikipedia.org/wiki/Large_language_model_emergent_abilities) of large language models. It is an emergent property of model scale, meaning that [breaks](https://en.wikipedia.org/wiki/Broken_Neural_Scaling_Law)[\[ 25 \]](https://en.wikipedia.org/wiki/Broken_Neural_Scaling_Law) in downstream scaling laws occur, leading to its efficacy increasing at a different rate in larger models than in smaller models.[ 24 ][ 10 ] Unlike training and [fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)), which produce lasting changes, in-context learning is temporary.[ 26 ] Training models to perform in-context learning can be viewed as a form of [meta-learning](https://en.wikipedia.org/wiki/Meta-learning_(computer_science)), or "learning to learn".[ 27 ]

##### Self-consistency decoding

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=5)]
*Self-consistency decoding* performs several chain-of-thought rollouts, then selects the most commonly reached conclusion out of all the rollouts.[ 28 ][ 29 ]

##### Tree-of-thought

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=6)]
*Tree-of-thought* prompting generalizes chain-of-thought by generating multiple lines of reasoning in parallel, with the ability to backtrack or explore other paths. It can use [tree search algorithms](https://en.wikipedia.org/wiki/Tree_search_algorithm) like [breadth-first](https://en.wikipedia.org/wiki/Breadth-first_search), [depth-first](https://en.wikipedia.org/wiki/Depth-first_search), or [beam](https://en.wikipedia.org/wiki/Beam_search).[ 29 ][ 30 ]

##### Prompting to estimate model sensitivity

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=7)]
Research consistently demonstrates that LLMs are highly sensitive to subtle variations in prompt formatting, structure, and linguistic properties. Some studies have shown up to 76 accuracy points across formatting changes in few-shot settings.[ 31 ] Linguistic features significantly influence prompt effectiveness—such as morphology, syntax, and lexico-semantic changes—which meaningfully enhance task performance across a variety of tasks.[ 3 ][ 32 ] Clausal syntax, for example, improves consistency and reduces uncertainty in knowledge retrieval.[ 33 ] This sensitivity persists even with larger model sizes, additional few-shot examples, or instruction tuning.
To address sensitivity of models and make them more robust, several methods have been proposed. FormatSpread facilitates systematic analysis by evaluating a range of plausible prompt formats, offering a more comprehensive performance interval.[ 31 ] Similarly, PromptEval estimates performance distributions across diverse prompts, enabling robust metrics such as performance quantiles and accurate evaluations under constrained budgets.[ 34 ]

##### Automatic prompt generation

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=8)]

###### Retrieval-augmented generation

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=9)] Main article: [Retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)Retrieval-augmented generation (RAG) is a technique that enables [generative artificial intelligence](https://en.wikipedia.org/wiki/Generative_artificial_intelligence) (Gen AI) models to retrieve and incorporate new information. It modifies interactions with a [large language model](https://en.wikipedia.org/wiki/Large_language_model) (LLM) so that the model responds to user queries with reference to a specified set of documents, using this information to supplement information from its pre-existing [training data](https://en.wikipedia.org/wiki/Training_data). This allows LLMs to use domain-specific and/or updated information.[ 35 ]
RAG improves large language models (LLMs) by incorporating [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval) before generating responses. Unlike traditional LLMs that rely on static training data, RAG pulls relevant text from databases, uploaded documents, or web sources. According to *Ars* *Technica* , "RAG is a way of improving LLM performance, in essence by blending the LLM process with a web search or other document look-up process to help LLMs stick to the facts." This method helps reduce [AI hallucinations](https://en.wikipedia.org/wiki/AI_hallucinations), which have led to real-world issues like chatbots inventing policies or lawyers citing nonexistent legal cases. By dynamically retrieving information, RAG enables AI to provide more accurate responses without frequent retraining.[ 36 ]

###### Graph retrieval-augmented generation

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=10)] GraphRAG with a knowledge graph combining access patterns for unstructured, structured, and mixed data
GraphRAG (coined by [Microsoft Research](https://en.wikipedia.org/wiki/Microsoft_Research)) is a technique that extends RAG with the use of a knowledge graph (usually, LLM-generated) to allow the model to connect disparate pieces of information, synthesize insights, and holistically understand summarized semantic concepts over large data collections. It was shown to be effective on datasets like the Violent Incident Information from News Articles (VIINA).[ 37 ][ 38 ]
Earlier work showed the effectiveness of using a [knowledge graph](https://en.wikipedia.org/wiki/Knowledge_graph) for question answering using text-to-query generation.[ 39 ] These techniques can be combined to search across both unstructured and structured data, providing expanded context, and improved ranking.

###### Using language models to generate prompts

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=11)]
Large language models (LLM) themselves can be used to compose prompts for large language models.[ 40 ] The *automatic prompt engineer* algorithm uses one LLM to [beam search](https://en.wikipedia.org/wiki/Beam_search) over prompts for another LLM:[ 41 ][ 42 ]

* There are two LLMs. One is the target LLM, and another is the prompting LLM.
* Prompting LLM is presented with example input-output pairs, and asked to generate instructions that could have caused a model following the instructions to generate the outputs, given the inputs.
* Each of the generated instructions is used to prompt the target LLM, followed by each of the inputs. The log-probabilities of the outputs are computed and added. This is the score of the instruction.
* The highest-scored instructions are given to the prompting LLM for further variations.
* Repeat until some stopping criteria is reached, then output the highest-scored instructions.
  CoT examples can be generated by LLM themselves. In "auto-CoT", a library of questions are converted to vectors by a model such as [BERT](https://en.wikipedia.org/wiki/BERT_(language_model)). The question vectors are [clustered](https://en.wikipedia.org/wiki/Cluster_analysis). Questions close to the [centroid](https://en.wikipedia.org/wiki/Centroid) of each cluster are selected, in order to have a subset of diverse questions. An LLM does zero-shot CoT on each selected question. The question and the corresponding CoT answer are added to a dataset of demonstrations. These diverse demonstrations can then added to prompts for few-shot learning.[ 43 ]

#### Text-to-image

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=12)] See also: [Artificial intelligence art § Prompt engineering and sharing](https://en.wikipedia.org/wiki/Artificial_intelligence_art#Prompt_engineering_and_sharing), and [Artificial intelligence art](https://en.wikipedia.org/wiki/Artificial_intelligence_art)Example of prompt engineering for text-to-image generation, with [Fooocus](https://en.wikipedia.org/wiki/Fooocus)In 2022, [text-to-image](https://en.wikipedia.org/wiki/Text-to-image) models like [DALL-E 2](https://en.wikipedia.org/wiki/DALL-E_2), [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion), and [Midjourney](https://en.wikipedia.org/wiki/Midjourney) were released to the public. These models take text prompts as input and use them to generate images.[ 44 ][ 6 ]

* Demonstration of the effect of negative prompts on images generated with [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion) **Top** : no negative prompt
* **Centre** : "green trees"
* **Bottom** : "round stones, round rocks"

##### Prompt formats

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=13)]
Early text-to-image models typically don't understand negation, grammar and sentence structure in the same way as [large language models](https://en.wikipedia.org/wiki/Large_language_models), and may thus require a different set of prompting techniques. The prompt "a party with no cake" may produce an image including a cake.[ 45 ] As an alternative, *negative prompts* allow a user to indicate, in a separate prompt, which terms should *not* appear in the resulting image.[ 46 ] Techniques such as framing the normal prompt into a [sequence-to-sequence](https://en.wikipedia.org/wiki/Seq2seq) language modeling problem can be used to automatically generate an output for the negative prompt.[ 47 ]
A text-to-image prompt commonly includes a description of the subject of the art, the desired medium (such as *digital painting* or *photography* ), style (such as *hyperrealistic* or *pop-art* ), lighting (such as *rim lighting* or *crepuscular rays* ), color, and texture.[ 48 ] Word order also affects the output of a text-to-image prompt. Words closer to the start of a prompt may be emphasized more heavily.[ 49 ]
The [Midjourney](https://en.wikipedia.org/wiki/Midjourney) documentation encourages short, descriptive prompts: instead of "Show me a picture of lots of blooming California poppies, make them bright, vibrant orange, and draw them in an illustrated style with colored pencils", an effective prompt might be "Bright orange California poppies drawn with colored pencils".[ 45 ]

##### Artist styles

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=14)]
Some text-to-image models are capable of imitating the style of particular artists by name. For example, the phrase *in the style of Greg Rutkowski* has been used in Stable Diffusion and Midjourney prompts to generate images in the distinctive style of Polish digital artist [Greg Rutkowski](https://en.wikipedia.org/w/index.php?title=Greg_Rutkowski&action=edit&redlink=1).[ 50 ] Famous artists such as [Vincent van Gogh](https://en.wikipedia.org/wiki/Vincent_van_Gogh) and [Salvador Dalí](https://en.wikipedia.org/wiki/Salvador_Dal%C3%AD) have also been used for styling and testing.[ 51 ]

#### Non-text prompts

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=15)]
Some approaches augment or replace natural language text prompts with non-text input.

##### Textual inversion and embeddings

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=16)]
For text-to-image models, *textual inversion* performs an optimization process to create a new [word embedding](https://en.wikipedia.org/wiki/Word_embedding) based on a set of example images. This embedding vector acts as a "pseudo-word" which can be included in a prompt to express the content or style of the examples.[ 52 ]

##### Image prompting

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=17)]
In 2023, [Meta](https://en.wikipedia.org/wiki/Meta_Platforms)'s AI research released Segment Anything, a [computer vision](https://en.wikipedia.org/wiki/Computer_vision) model that can perform [image segmentation](https://en.wikipedia.org/wiki/Image_segmentation) by prompting. As an alternative to text prompts, Segment Anything can accept bounding boxes, segmentation masks, and foreground/background points.[ 53 ]

##### Using gradient descent to search for prompts

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=18)]
In "prefix-tuning",[ 54 ] "prompt tuning", or "soft prompting",[ 55 ] floating-point-valued vectors are searched directly by [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) to maximize the log-likelihood on outputs.
Formally, let E = { e 1 , … , e k } {\displaystyle \mathbf {E} ={\mathbf {e\_{1}} ,\dots ,\mathbf {e\_{k}} }} be a set of soft prompt tokens (tunable embeddings), while X = { x 1 , … , x m } {\displaystyle \mathbf {X} ={\mathbf {x\_{1}} ,\dots ,\mathbf {x\_{m}} }} and Y = { y 1 , … , y n } {\displaystyle \mathbf {Y} ={\mathbf {y\_{1}} ,\dots ,\mathbf {y\_{n}} }} be the token embeddings of the input and output respectively. During training, the tunable embeddings, input, and output tokens are concatenated into a single sequence concat ( E ; X ; Y ) {\displaystyle {\text{concat}}(\mathbf {E} ;\mathbf {X} ;\mathbf {Y} )} , and fed to the LLMs. The [losses](https://en.wikipedia.org/wiki/Loss_function) are computed over the Y {\displaystyle \mathbf {Y} } tokens; the gradients are [backpropagated](https://en.wikipedia.org/wiki/Backpropagation) to prompt-specific parameters: in prefix-tuning, they are parameters associated with the prompt tokens at each layer; in prompt tuning, they are merely the soft tokens added to the vocabulary.[ 56 ]
More formally, this is prompt tuning. Let an LLM be written as L L M ( X ) = F ( E ( X ) ) {\displaystyle LLM(X)=F(E(X))} , where X {\displaystyle X} is a sequence of linguistic tokens, E {\displaystyle E} is the token-to-vector function, and F {\displaystyle F} is the rest of the model. In prefix-tuning, one provides a set of input-output pairs { ( X i , Y i ) } i {\displaystyle {(X^{i},Y^{i})}\_{i}} , and then use gradient descent to search for arg ⁡ max Z ~ ∑ i log ⁡ P r [ Y i | Z ~ ∗ E ( X i ) ] {\displaystyle \arg \max \_{\tilde {Z}}\sum \_{i}\log Pr[Y^{i}|{\tilde {Z}}\ast E(X^{i})]} . In words, log ⁡ P r [ Y i | Z ~ ∗ E ( X i ) ] {\displaystyle \log Pr[Y^{i}|{\tilde {Z}}\ast E(X^{i})]} is the log-likelihood of outputting Y i {\displaystyle Y^{i}} , if the model first encodes the input X i {\displaystyle X^{i}} into the vector E ( X i ) {\displaystyle E(X^{i})} , then prepend the vector with the "prefix vector" Z ~ {\displaystyle {\tilde {Z}}} , then apply F {\displaystyle F} . For prefix tuning, it is similar, but the "prefix vector" Z ~ {\displaystyle {\tilde {Z}}} is pre-appended to the hidden states in every layer of the model.[citation needed]
An earlier result uses the same idea of gradient descent search, but is designed for masked language models like BERT, and searches only over token sequences, rather than numerical vectors. Formally, it searches for arg ⁡ max X ~ ∑ i log ⁡ P r [ Y i | X ~ ∗ X i ] {\displaystyle \arg \max \_{\tilde {X}}\sum \_{i}\log Pr[Y^{i}|{\tilde {X}}\ast X^{i}]} where X ~ {\displaystyle {\tilde {X}}} is ranges over token sequences of a specified length.[ 57 ]

#### Limitations

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=19)]
While the process of writing and refining a prompt for an LLM or generative AI shares some parallels with an iterative engineering design process, such as through discovering 'best principles' to reuse and discovery through reproducible experimentation, the actual learned principles and skills depend heavily on the specific model being learned rather than being generalizable across the entire field of prompt-based generative models. Such patterns are also volatile and exhibit significantly different results from seemingly insignificant prompt changes.[ 58 ][ 59 ] According to The Wall Street Journal in 2025, the job of prompt engineer was one of the hottest in 2023, but has become obsolete due to models that better intuit user intent and to company trainings.[ 60 ]

#### Prompt injection

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=20)] Main article: [Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection)See also: [SQL injection](https://en.wikipedia.org/wiki/SQL_injection), [Cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting), and [Social engineering (security)](https://en.wikipedia.org/wiki/Social_engineering_(security))Prompt injection is a [cybersecurity](https://en.wikipedia.org/wiki/Cybersecurity) exploit in which adversaries craft inputs that appear legitimate but are designed to cause unintended behavior in [machine learning models](https://en.wikipedia.org/wiki/Machine_learning_model), particularly [large language models](https://en.wikipedia.org/wiki/Large_language_model) (LLMs). This attack takes advantage of the model's inability to distinguish between developer-defined prompts and user inputs, allowing adversaries to bypass safeguards and influence model behaviour. While LLMs are designed to follow trusted instructions, they can be manipulated into carrying out unintended responses through carefully crafted inputs.[ 61 ][ 62 ]

#### References

[[edit](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&action=edit&section=21)]

1. ^ **a** **b** **c** Genkina, Dina (March 6, 2024). ["AI Prompt Engineering is Dead: Long live AI prompt engineering"](https://spectrum.ieee.org/prompt-engineering-is-dead). IEEE Spectrum. Retrieved January 18, 2025 .
2. ^Radford, Alec; Wu, Jeffrey; Child, Rewon; Luan, David; [Amodei, Dario](https://en.wikipedia.org/wiki/Dario_Amodei); [Sutskever, Ilya](https://en.wikipedia.org/wiki/Ilya_Sutskever) (2019). ["Language Models are Unsupervised Multitask Learners"](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)(PDF) . OpenAI. We demonstrate language models can perform down-stream tasks in a zero-shot setting – without any parameter or architecture modification
3. ^ **a** **b** Wahle, Jan Philip; Ruas, Terry; Xu, Yang; Gipp, Bela (2024). ["Paraphrase Types Elicit Prompt Engineering Capabilities"](https://aclanthology.org/2024.emnlp-main.617/). In Al-Onaizan, Yaser; Bansal, Mohit; Chen, Yun-Nung (eds.). *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing* . Miami, Florida, USA: Association for Computational Linguistics. pp. 11004– 11033. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2406.19898](https://arxiv.org/abs/2406.19898). [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.18653/v1/2024.emnlp-main.617](https://doi.org/10.18653%2Fv1%2F2024.emnlp-main.617).
4. [^](https://doi.org/10.18653%2Fv1%2F2024.emnlp-main.617)Heaven, Will Douglas (April 6, 2022). ["This horse-riding astronaut is a milestone on AI's long road towards understanding"](https://www.technologyreview.com/2022/04/06/1049061/dalle-openai-gpt3-ai-agi-multimodal-image-generation/). *MIT Technology Review* . Retrieved August 14, 2023 .
5. ^Wiggers, Kyle (June 12, 2023). ["Meta open sources an AI-powered music generator"](https://techcrunch.com/2023/06/12/meta-open-sources-an-ai-powered-music-generator/). TechCrunch . Retrieved August 15, 2023 . Next, I gave a more complicated prompt to attempt to throw MusicGen for a loop: "Lo-fi slow BPM electro chill with organic samples."
6. ^ **a** **b** Mittal, Aayush (July 27, 2023). ["Mastering AI Art: A Concise Guide to Midjourney and Prompt Engineering"](https://www.unite.ai/mastering-ai-art-a-concise-guide-to-midjourney-and-prompt-engineering/). *Unite.AI* . Retrieved May 9, 2025 .
7. ^ *The Natural Language Decathlon: Multitask Learning as Question Answering* . ICLR. 2018. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[1806.08730](https://arxiv.org/abs/1806.08730).
8. [^](https://arxiv.org/abs/1806.08730)Knoth, Nils; Tolzin, Antonia; Janson, Andreas; Leimeister, Jan Marco (June 1, 2024). ["AI literacy and its implications for prompt engineering strategies"](https://doi.org/10.1016%2Fj.caeai.2024.100225). *Computers and Education: Artificial Intelligence* . **6** : 100225. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1016/j.caeai.2024.100225](https://doi.org/10.1016%2Fj.caeai.2024.100225). [ISSN](https://en.wikipedia.org/wiki/ISSN_(identifier))[2666-920X](https://en.wikipedia.org/wiki/ISSN_(identifier)).
9. [^](https://en.wikipedia.org/wiki/ISSN_(identifier)) *PromptSource: An Integrated Development Environment and Repository for Natural Language Prompts* . Association for Computational Linguistics. 2022.
10. ^ **a** **b** **c** **d** **e** **f** Wei, Jason; Wang, Xuezhi; Schuurmans, Dale; Bosma, Maarten; Ichter, Brian; Xia, Fei; Chi, Ed H.; Le, Quoc V.; Zhou, Denny (October 31, 2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* . Advances in Neural Information Processing Systems (NeurIPS 2022). Vol. 35. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2201.11903](https://arxiv.org/abs/2201.11903).
11. [^](https://arxiv.org/abs/2201.11903)Brubaker, Ben (March 21, 2024). ["How Chain-of-Thought Reasoning Helps Neural Networks Compute"](https://www.quantamagazine.org/how-chain-of-thought-reasoning-helps-neural-networks-compute-20240321/). *Quanta Magazine* . Retrieved May 9, 2025 .
12. ^Chen, Brian X. (June 23, 2023). ["How to Turn Your Chatbot Into a Life Coach"](https://www.nytimes.com/2023/06/23/technology/ai-chatbot-life-coach.html). *The New York Times* .
13. ^Chen, Brian X. (May 25, 2023). ["Get the Best From ChatGPT With These Golden Prompts"](https://www.nytimes.com/2023/05/25/technology/ai-chatbot-chatgpt-prompts.html). *The New York Times* . [ISSN](https://en.wikipedia.org/wiki/ISSN_(identifier))[0362-4331](https://en.wikipedia.org/wiki/ISSN_(identifier)). Retrieved August 16, 2023 .
14. [^](https://en.wikipedia.org/wiki/ISSN_(identifier))Chen, Zijie; Zhang, Lichao; Weng, Fangsheng; Pan, Lili; Lan, Zhenzhong (June 16, 2024). ["Tailored Visions: Enhancing Text-to-Image Generation with Personalized Prompt Rewriting"](https://doi.org/10.1109/cvpr52733.2024.00738). *2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* . IEEE. pp. 7727– 7736. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2310.08129](https://arxiv.org/abs/2310.08129). [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1109/cvpr52733.2024.00738](https://doi.org/10.1109%2Fcvpr52733.2024.00738). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier))[979-8-3503-5300-6](https://en.wikipedia.org/wiki/ISBN_(identifier)).
15. [^](https://en.wikipedia.org/wiki/ISBN_(identifier))Narang, Sharan; Chowdhery, Aakanksha (April 4, 2022). ["Pathways Language Model (PaLM): Scaling to 540 Billion Parameters for Breakthrough Performance"](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html). *ai.googleblog.com* .
16. ^Dang, Ekta (February 8, 2023). ["Harnessing the power of GPT-3 in scientific research"](https://venturebeat.com/ai/harnessing-the-power-of-gpt-3-in-scientific-research/). *VentureBeat* . Retrieved March 10, 2023 .
17. ^Montti, Roger (May 13, 2022). ["Google's Chain of Thought Prompting Can Boost Today's Best Algorithms"](https://www.searchenginejournal.com/google-chain-of-thought-prompting/450106/). *Search Engine Journal* . Retrieved March 10, 2023 .
18. ^"Scaling Instruction-Finetuned Language Models"(PDF) . *Journal of Machine Learning Research* . 2024.
19. ^Wei, Jason; Tay, Yi (November 29, 2022). ["Better Language Models Without Massive Compute"](https://ai.googleblog.com/2022/11/better-language-models-without-massive.html). *ai.googleblog.com* . Retrieved March 10, 2023 .
20. ^ **a** **b** Kojima, Takeshi; Shixiang Shane Gu; Reid, Machel; Matsuo, Yutaka; Iwasawa, Yusuke (2022). "Large Language Models are Zero-Shot Reasoners". *NeurIPS* . [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2205.11916](https://arxiv.org/abs/2205.11916).
21. [^](https://arxiv.org/abs/2205.11916)Dickson, Ben (August 30, 2022). ["LLMs have not learned our language — we're trying to learn theirs"](https://venturebeat.com/ai/llms-have-not-learned-our-language-were-trying-to-learn-theirs%EF%BF%BC/). *VentureBeat* . Retrieved March 10, 2023 .
22. ^Garg, Shivam; Tsipras, Dimitris; Liang, Percy; Valiant, Gregory (2022). "What Can Transformers Learn In-Context? A Case Study of Simple Function Classes". *NeurIPS* . [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2208.01066](https://arxiv.org/abs/2208.01066).
23. [^](https://arxiv.org/abs/2208.01066)Brown, Tom; Mann, Benjamin; Ryder, Nick; Subbiah, Melanie; Kaplan, Jared D.; Dhariwal, Prafulla; Neelakantan, Arvind (2020). "Language models are few-shot learners". *Advances in Neural Information Processing Systems* . **33** : 1877– 1901. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2005.14165](https://arxiv.org/abs/2005.14165).
24. ^ **a** **b** Wei, Jason; Tay, Yi; Bommasani, Rishi; Raffel, Colin; Zoph, Barret; Borgeaud, Sebastian; Yogatama, Dani; Bosma, Maarten; Zhou, Denny; Metzler, Donald; Chi, Ed H.; Hashimoto, Tatsunori; Vinyals, Oriol; Liang, Percy; Dean, Jeff; Fedus, William (October 2022). "Emergent Abilities of Large Language Models". *Transactions on Machine Learning Research* . [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2206.07682](https://arxiv.org/abs/2206.07682). In prompting, a pre-trained language model is given a prompt (e.g. a natural language instruction) of a task and completes the response without any further training or gradient updates to its parameters... The ability to perform a task via few-shot prompting is emergent when a model has random performance until a certain scale, after which performance increases to well-above random
25. [^](https://arxiv.org/abs/2206.07682)Caballero, Ethan; Gupta, Kshitij; Rish, Irina; Krueger, David (2023). "Broken Neural Scaling Laws". *ICLR* . [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2210.14891](https://arxiv.org/abs/2210.14891).
26. [^](https://arxiv.org/abs/2210.14891)[Musser, George](https://arxiv.org/abs/2210.14891). ["How AI Knows Things No One Told It"](https://www.scientificamerican.com/article/how-ai-knows-things-no-one-told-it/). Scientific American. Retrieved May 17, 2023 . By the time you type a query into ChatGPT, the network should be fixed; unlike humans, it should not continue to learn. So it came as a surprise that LLMs do, in fact, learn from their users' prompts—an ability known as in-context learning.
27. ^Garg, Shivam; Tsipras, Dimitris; Liang, Percy; Valiant, Gregory (2022). "What Can Transformers Learn In-Context? A Case Study of Simple Function Classes". *NeurIPS* . [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2208.01066](https://arxiv.org/abs/2208.01066). Training a model to perform in-context learning can be viewed as an instance of the more general learning-to-learn or meta-learning paradigm
28. [^](https://arxiv.org/abs/2208.01066) *Self-Consistency Improves Chain of Thought Reasoning in Language Models* . ICLR. 2023. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2203.11171](https://arxiv.org/abs/2203.11171).
29. ^ **a** **b** Mittal, Aayush (May 27, 2024). ["Latest Modern Advances in Prompt Engineering: A Comprehensive Guide"](https://www.unite.ai/latest-modern-advances-in-prompt-engineering-a-comprehensive-guide/). *Unite.AI* . Retrieved May 8, 2025 .
30. ^ *Tree of Thoughts: Deliberate Problem Solving with Large Language Models* . NeurIPS. 2023. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2305.10601](https://arxiv.org/abs/2305.10601).
31. ^ **a** **b** *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting* . ICLR. 2024. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2310.11324](https://arxiv.org/abs/2310.11324).
32. [^](https://arxiv.org/abs/2310.11324)Leidinger, Alina; van Rooij, Robert; Shutova, Ekaterina (2023). Bouamor, Houda; Pino, Juan; Bali, Kalika (eds.). ["The language of prompting: What linguistic properties make a prompt successful?"](https://aclanthology.org/2023.findings-emnlp.618/). *Findings of the Association for Computational Linguistics: EMNLP 2023* . Singapore: Association for Computational Linguistics: 9210– 9232. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2311.01967](https://arxiv.org/abs/2311.01967). [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.18653/v1/2023.findings-emnlp.618](https://doi.org/10.18653%2Fv1%2F2023.findings-emnlp.618).
33. [^](https://doi.org/10.18653%2Fv1%2F2023.findings-emnlp.618)Linzbach, Stephan; Dimitrov, Dimitar; Kallmeyer, Laura; Evang, Kilian; Jabeen, Hajira; Dietze, Stefan (June 2024). ["Dissecting Paraphrases: The Impact of Prompt Syntax and supplementary Information on Knowledge Retrieval from Pretrained Language Models"](https://aclanthology.org/2024.naacl-long.201/). In Duh, Kevin; Gomez, Helena; Bethard, Steven (eds.). *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)* . Mexico City, Mexico: Association for Computational Linguistics. pp. 3645– 3655. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2404.01992](https://arxiv.org/abs/2404.01992). [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.18653/v1/2024.naacl-long.201](https://doi.org/10.18653%2Fv1%2F2024.naacl-long.201).
34. [^](https://doi.org/10.18653%2Fv1%2F2024.naacl-long.201) *Efficient multi-prompt evaluation of LLMs* . NeurIPS. 2024. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2405.17202](https://arxiv.org/abs/2405.17202).
35. [^](https://arxiv.org/abs/2405.17202)["Why Google's AI Overviews gets things wrong"](https://arxiv.org/abs/2405.17202). *MIT Technology Review* . May 31, 2024 . Retrieved March 7, 2025 .
36. ^"Can a technology called RAG keep AI models from making stuff up?". *Ars Technica* . June 6, 2024 . Retrieved March 7, 2025 .
37. ^Larson, Jonathan; Truitt, Steven (February 13, 2024), *GraphRAG: Unlocking LLM discovery on narrative private data* , Microsoft
38. [^](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)["An Introduction to Graph RAG"](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/). *KDnuggets* . Retrieved May 9, 2025 .
39. ^Sequeda, Juan; Allemang, Dean; Jacob, Bryon (2023). "A Benchmark to Understand the Role of Knowledge Graphs on Large Language Model's Accuracy for Question Answering on Enterprise SQL Databases". *Grades-Nda* . [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2311.07509](https://arxiv.org/abs/2311.07509).
40. [^](https://arxiv.org/abs/2311.07509) *Explaining Patterns in Data with Language Models via Interpretable Autoprompting* (PDF) . BlackboxNLP Workshop. 2023. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2210.01848](https://arxiv.org/abs/2210.01848).
41. [^](https://arxiv.org/abs/2210.01848) *Large Language Models are Human-Level Prompt Engineers* . ICLR. 2023. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2211.01910](https://arxiv.org/abs/2211.01910).
42. [^](https://arxiv.org/abs/2211.01910)Pryzant, Reid; Iter, Dan; Li, Jerry; Lee, Yin Tat; Zhu, Chenguang; Zeng, Michael (2023). ["Automatic Prompt Optimization with "Gradient Descent" and Beam Search"](https://aclanthology.org/2023.emnlp-main.494/). *Conference on Empirical Methods in Natural Language Processing* : 7957– 7968. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2305.03495](https://arxiv.org/abs/2305.03495). [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.18653/v1/2023.emnlp-main.494](https://doi.org/10.18653%2Fv1%2F2023.emnlp-main.494).
43. [^](https://doi.org/10.18653%2Fv1%2F2023.emnlp-main.494) *Automatic Chain of Thought Prompting in Large Language Models* . ICLR. 2023. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2210.03493](https://arxiv.org/abs/2210.03493).
44. [^](https://arxiv.org/abs/2210.03493)Goldman, Sharon (January 5, 2023). ["Two years after DALL-E debut, its inventor is "surprised" by impact"](https://venturebeat.com/ai/two-years-after-dall-e-debut-its-inventor-is-surprised-by-impact/). *VentureBeat* . Retrieved May 9, 2025 .
45. ^ **a** **b** ["Prompts"](https://en.wikipedia.org#cite_ref-Prompts_45-0). *docs.midjourney.com* . Retrieved August 14, 2023 .
46. ^"Why Does This Horrifying Woman Keep Appearing in AI-Generated Images?". *VICE* . September 7, 2022 . Retrieved May 9, 2025 .
47. ^Goldblum, R.; Pillarisetty, R.; Dauphinee, M. J.; Talal, N. (1975). ["Acceleration of autoimmunity in NZB/NZW F1 mice by graft-versus-host disease"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1538084). *Clinical and Experimental Immunology* . **19** (2): 377– 385. [ISSN](https://en.wikipedia.org/wiki/ISSN_(identifier))[0009-9104](https://en.wikipedia.org/wiki/ISSN_(identifier)). [PMC](https://en.wikipedia.org/wiki/PMC_(identifier))[1538084](https://en.wikipedia.org/wiki/PMC_(identifier)). [PMID](https://en.wikipedia.org/wiki/PMID_(identifier))[2403](https://en.wikipedia.org/wiki/PMID_(identifier)).
48. [^](https://en.wikipedia.org/wiki/PMID_(identifier))["Stable Diffusion prompt: a definitive guide"](https://en.wikipedia.org/wiki/PMID_(identifier)). May 14, 2023 . Retrieved August 14, 2023 .
49. [^](https://en.wikipedia.org/wiki/PMID_(identifier))Diab, Mohamad; Herrera, Julian; Chernow, Bob (October 28, 2022). ["Stable Diffusion Prompt Book"](https://cdn.openart.ai/assets/Stable%20Diffusion%20Prompt%20Book%20From%20OpenArt%2011-13.pdf)(PDF) . Retrieved August 7, 2023 . Prompt engineering is the process of structuring words that can be interpreted and understood by a *text-to-image* model. Think of it as the language you need to speak in order to tell an AI model what to draw.
50. ^Heikkilä, Melissa (September 16, 2022). ["This Artist Is Dominating AI-Generated Art and He's Not Happy About It"](https://www.technologyreview.com/2022/09/16/1059598/this-artist-is-dominating-ai-generated-art-and-hes-not-happy-about-it/). *MIT Technology Review* . Retrieved August 14, 2023 .
51. ^Solomon, Tessa (August 28, 2024). ["The AI-Powered Ask Dalí and Hello Vincent Installations Raise Uncomfortable Questions about Ventriloquizing the Dead"](https://www.artnews.com/art-news/issue/salvador-dali-vincent-van-gogh-ai-installations-ethics-1234714954/). *ARTnews.com* . Retrieved January 10, 2025 .
52. ^Gal, Rinon; Alaluf, Yuval; Atzmon, Yuval; Patashnik, Or; Bermano, Amit H.; Chechik, Gal; Cohen-Or, Daniel (2023). "An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion". *ICLR* . [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2208.01618](https://arxiv.org/abs/2208.01618). Using only 3-5 images of a user-provided concept, like an object or a style, we learn to represent it through new "words" in the embedding space of a frozen text-to-image model.
53. [^](https://arxiv.org/abs/2208.01618) *Segment Anything* (PDF) . ICCV. 2023.
54. [^](https://arxiv.org/abs/2208.01618)Li, Xiang Lisa; Liang, Percy (2021). "Prefix-Tuning: Optimizing Continuous Prompts for Generation". *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)* . pp. 4582– 4597. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.18653/V1/2021.ACL-LONG.353](https://doi.org/10.18653%2FV1%2F2021.ACL-LONG.353). [S2CID](https://en.wikipedia.org/wiki/S2CID_(identifier))[230433941](https://en.wikipedia.org/wiki/S2CID_(identifier)). In this paper, we propose prefix-tuning, a lightweight alternative to fine-tuning... Prefix-tuning draws inspiration from prompting
55. [^](https://en.wikipedia.org/wiki/S2CID_(identifier))Lester, Brian; Al-Rfou, Rami; Constant, Noah (2021). "The Power of Scale for Parameter-Efficient Prompt Tuning". *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing* . pp. 3045– 3059. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2104.08691](https://arxiv.org/abs/2104.08691). [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.18653/V1/2021.EMNLP-MAIN.243](https://doi.org/10.18653%2FV1%2F2021.EMNLP-MAIN.243). [S2CID](https://en.wikipedia.org/wiki/S2CID_(identifier))[233296808](https://en.wikipedia.org/wiki/S2CID_(identifier)). In this work, we explore "prompt tuning," a simple yet effective mechanism for learning "soft prompts"...Unlike the discrete text prompts used by GPT-3, soft prompts are learned through back-propagation
56. [^](https://en.wikipedia.org/wiki/S2CID_(identifier)) *How Does In-Context Learning Help Prompt Tuning?* . EACL. 2024. [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2302.11521](https://arxiv.org/abs/2302.11521).
57. [^](https://arxiv.org/abs/2302.11521)Shin, Taylor; Razeghi, Yasaman; Logan IV, Robert L.; Wallace, Eric; Singh, Sameer (November 2020). ["AutoPrompt: Eliciting Knowledge from Language Models with Automatically Generated Prompts"](https://aclanthology.org/2020.emnlp-main.346). *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)* . Online: Association for Computational Linguistics. pp. 4222– 4235. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.18653/v1/2020.emnlp-main.346](https://doi.org/10.18653%2Fv1%2F2020.emnlp-main.346). [S2CID](https://en.wikipedia.org/wiki/S2CID_(identifier))[226222232](https://en.wikipedia.org/wiki/S2CID_(identifier)).
58. [^](https://en.wikipedia.org/wiki/S2CID_(identifier))Meincke, Lennart and Mollick, Ethan R. and Mollick, Lilach and Shapiro, Dan, Prompting Science Report 1: Prompt Engineering is Complicated and Contingent (March 04, 2025). Available at SSRN: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5165270>
59. [^](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5165270)[" 'AI is already eating its own': Prompt engineering is quickly going extinct"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5165270). *Fast Company* . May 6, 2025.
60. ^Bousquette, Isabelle (April 25, 2025). ["The Hottest AI Job of 2023 Is Already Obsolete"](https://www.wsj.com/articles/the-hottest-ai-job-of-2023-is-already-obsolete-1961b054). *Wall Street Journal* . [ISSN](https://en.wikipedia.org/wiki/ISSN_(identifier))[0099-9660](https://en.wikipedia.org/wiki/ISSN_(identifier)). Retrieved May 7, 2025 .
61. [^](https://en.wikipedia.org/wiki/ISSN_(identifier))Vigliarolo, Brandon (September 19, 2022). ["GPT-3 'prompt injection' attack causes bot bad manners"](https://www.theregister.com/2022/09/19/in_brief_security/). The Register. Retrieved February 9, 2023 .
62. ^"What is a prompt injection attack?". *IBM* . March 26, 2024 . Retrieved March 7, 2025 .
    Scholia has a *topic* profile for Prompt engineering.

* v
* t
* e
  Generative AIConcepts
* Autoencoder
* Deep learning
* Fine-tuning
* Foundation model
* Generative adversarial network
* Generative pre-trained transformer
* Large language model
* Model Context Protocol
* Neural network
* Prompt engineering
* Reinforcement learning from human feedback
* Retrieval-augmented generation
* Self-supervised learning
* Stochastic parrot
* Synthetic data
* Top-p sampling
* Transformer
* Variational autoencoder
* Vibe coding
* Vision transformer
* Waluigi effect
* Word embedding
  Models Text
* Character.ai
* Claude
* DBRX
* DeepSeek
* ERNIE
* Gemini
* GPT1
* 2
* 3
* J
* ChatGPT
* 4
* 4o
* o1
* o3
* 4.5
* 4.1
* o4-mini
  Granite
  Grok
  Hunyuan
  Kimi
  Llama
  Microsoft Copilot
  Mistral Large
  PanGu-Σ
  Qwen
  YandexGPT
* ImageAurora
* DALL-E
* Firefly
* Flux
* GPT Image 1
* Ideogram
* Imagen
* Leonardo
* Midjourney
* Stable Diffusion
* VideoDream Machine
* Runway Gen
* Hailuo AI
* Kling
* Sora
* Veo
* VideoPoet
  Music
* Endel
* Lyria
* Suno AI
* Udio
  Speech
* 15.ai
* ElevenLabs
* WaveNet
  Coding
* Claude Code
* Cursor
* GitHub Copilot
* Granite Code
* Replit
* Xcode
* AgentsAutoGLM
* AutoGPT
* Devin AI
* Manus
* OpenAI Codex
* Operator
* Companies01.AI
* Aleph Alpha
* Alibaba
* Anthropic
* Baichuan
* Baidu
* Canva
* Cognition AI
* Cohere
* Contextual AI
* DeepL
* DeepSeek
* ElevenLabs
* Google DeepMind
* Hugging Face
* Krikey AI
* Kuaishou
* Meta AI
* MiniMax
* Mistral AI
* Moonshot AI
* OpenAI
* Runway
* Scale AI
* Stability AI
* Synthesia
* Tencent
* xAI
* Yandex
* Zhipu AI
* Category
* Commons
* v
* t
* e
  Artificial intelligence (AI)[History](https://en.wikipedia.org/wiki/History_of_artificial_intelligence) ([timeline](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)) Concepts
* [Parameter](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Hyperparameter](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Loss functions](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Regression](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Bias–variance tradeoff](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Double descent](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Overfitting](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Clustering](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Gradient descent](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[SGD](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Quasi-Newton method](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Conjugate gradient method](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Backpropagation](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Attention](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Convolution](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Normalization](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Batchnorm](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Activation](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Softmax](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Sigmoid](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Rectifier](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Gating](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Weight initialization](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Regularization](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Datasets](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Augmentation](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Prompt engineering](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Reinforcement learning](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Q-learning](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [SARSA](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Imitation](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Policy gradient](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Diffusion](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Latent diffusion model](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Autoregression](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Adversary](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [RAG](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Uncanny valley](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [RLHF](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Self-supervised learning](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Reflection](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Recursive self-improvement](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Hallucination](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Word embedding](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Vibe coding](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  Applications
* [Machine learning](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[In-context learning](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Artificial neural network](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Deep learning](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Language model](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Large language model](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [NMT](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Reasoning language model](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Model Context Protocol](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Intelligent agent](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Artificial human companion](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Humanity's Last Exam](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Artificial general intelligence (AGI)](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  Implementations Audio–visual
* [AlexNet](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [WaveNet](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Human image synthesis](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [HWR](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [OCR](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Speech synthesis](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[15.ai](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [ElevenLabs](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Speech recognition](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Whisper](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Facial recognition](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [AlphaFold](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Text-to-image models](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Aurora](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [DALL-E](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Firefly](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Flux](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Ideogram](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Imagen](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Midjourney](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Stable Diffusion](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Text-to-video models](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Dream Machine](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Runway Gen](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Hailuo AI](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Kling](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Sora](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Veo](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Music generation](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Suno AI](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Udio](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  Text
* [Word2vec](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Seq2seq](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [GloVe](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [BERT](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [T5](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Llama](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Chinchilla AI](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [PaLM](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [GPT](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[1](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [2](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [3](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [J](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [ChatGPT](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [4](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [4o](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [o1](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [o3](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [4.5](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [4.1](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [o4-mini](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Claude](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Gemini](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[chatbot](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Grok](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [LaMDA](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [BLOOM](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Project Debater](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [IBM Watson](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [IBM Watsonx](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Granite](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [PanGu-Σ](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [DeepSeek](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Qwen](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  Decisional
* [AlphaGo](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [AlphaZero](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [OpenAI Five](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Self-driving car](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [MuZero](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Action selection](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[AutoGPT](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Robot control](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  People
* [Alan Turing](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Warren Sturgis McCulloch](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Walter Pitts](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [John von Neumann](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Claude Shannon](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Marvin Minsky](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [John McCarthy](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Nathaniel Rochester](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Allen Newell](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Cliff Shaw](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Herbert A. Simon](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Oliver Selfridge](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Frank Rosenblatt](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Bernard Widrow](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Joseph Weizenbaum](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Seymour Papert](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Seppo Linnainmaa](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Paul Werbos](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Jürgen Schmidhuber](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Yann LeCun](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Geoffrey Hinton](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [John Hopfield](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Yoshua Bengio](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Lotfi A. Zadeh](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Stephen Grossberg](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Alex Graves](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Andrew Ng](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Fei-Fei Li](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Alex Krizhevsky](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Ilya Sutskever](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Demis Hassabis](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [David Silver](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Ian Goodfellow](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Andrej Karpathy](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [James Goodnight](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  Architectures
* [Neural Turing machine](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Differentiable neural computer](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Transformer](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Vision transformer (ViT)](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Recurrent neural network (RNN)](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Long short-term memory (LSTM)](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Gated recurrent unit (GRU)](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Echo state network](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Multilayer perceptron (MLP)](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Convolutional neural network (CNN)](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Residual neural network (RNN)](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Highway network](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Mamba](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Autoencoder](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Variational autoencoder (VAE)](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Generative adversarial network (GAN)](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  [Graph neural network (GNN)](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  Portals
* [Technology](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Category](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)[Artificial neural networks](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Machine learning](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  List
* [Companies](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
* [Projects](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence)
  Retrieved from "<https://en.wikipedia.org/w/index.php?title=Prompt_engineering&oldid=1294334364>" [Categories](https://en.wikipedia.org/wiki/Help:Category):
* [Deep learning](https://en.wikipedia.org/wiki/Help:Category)
* [Machine learning](https://en.wikipedia.org/wiki/Help:Category)
* [Natural language processing](https://en.wikipedia.org/wiki/Help:Category)
* [Unsupervised learning](https://en.wikipedia.org/wiki/Help:Category)
* [2022 neologisms](https://en.wikipedia.org/wiki/Help:Category)
* [Linguistics](https://en.wikipedia.org/wiki/Help:Category)
* [Generative artificial intelligence](https://en.wikipedia.org/wiki/Help:Category)
  Hidden categories:
* [Articles with short description](https://en.wikipedia.org/wiki/Help:Category)
* [Short description is different from Wikidata](https://en.wikipedia.org/wiki/Help:Category)
* [Wikipedia neutral point of view disputes from May 2025](https://en.wikipedia.org/wiki/Help:Category)
* [All Wikipedia neutral point of view disputes](https://en.wikipedia.org/wiki/Help:Category)
* [Use mdy dates from January 2025](https://en.wikipedia.org/wiki/Help:Category)
* [Pages using multiple image with auto scaled images](https://en.wikipedia.org/wiki/Help:Category)
* [All articles with unsourced statements](https://en.wikipedia.org/wiki/Help:Category)
* [Articles with unsourced statements from May 2025](https://en.wikipedia.org/wiki/Help:Category)