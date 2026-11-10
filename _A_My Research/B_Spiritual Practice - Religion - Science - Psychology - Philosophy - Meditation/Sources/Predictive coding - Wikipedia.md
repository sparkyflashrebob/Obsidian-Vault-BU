---
tags:
  - notebooklm-import
notebook: "B_Spiritual Practice - Religion - Science - Psychology - Philosophy - Meditation"
category: "research"
---

https://en.wikipedia.org/wiki/Predictive\_coding

Jump to content

Main menu Navigation

Current events

Random article

About Wikipedia

Learn to edit

Community portal

Recent changes

Upload file

Special pages

Create account

Create account

Pages for logged out editors

https://en.wikipedia.org/wiki/Help:Introduction

Contributions

https://en.wikipedia.org/wiki/Help:Introduction

https://en.wikipedia.org/wiki/Help:Introduction

https://en.wikipedia.org/wiki/Help:Introduction

https://en.wikipedia.org/wiki/Help:Introduction

2 General framework

https://en.wikipedia.org/wiki/Help:Introduction

2.1 Precision weighting

https://en.wikipedia.org/wiki/Help:Introduction

2.2 Active inference

https://en.wikipedia.org/wiki/Help:Introduction

3 Neural theory in predictive coding

https://en.wikipedia.org/wiki/Help:Introduction

4 Applying predictive coding

https://en.wikipedia.org/wiki/Help:Introduction

4.1 Perception

https://en.wikipedia.org/wiki/Help:Introduction

4.2 Interoception

https://en.wikipedia.org/wiki/Help:Introduction

4.3 Computer science

https://en.wikipedia.org/wiki/Help:Introduction

4.4 Challenges

https://en.wikipedia.org/wiki/Help:Introduction

https://en.wikipedia.org/wiki/Help:Introduction

6 References

https://en.wikipedia.org/wiki/Help:Introduction

Predictive coding

https://en.wikipedia.org/wiki/Help:Introduction

https://en.wikipedia.org/wiki/Help:Introduction

https://en.wikipedia.org/wiki/Help:Introduction

https://en.wikipedia.org/wiki/Help:Introduction

https://en.wikipedia.org/wiki/Help:Introduction

https://en.wikipedia.org/wiki/Help:Introduction

Tools Actions

https://en.wikipedia.org/wiki/Help:Introduction

https://en.wikipedia.org/wiki/Help:Introduction

View history

https://en.wikipedia.org/wiki/Help:Introduction

What links here

https://en.wikipedia.org/wiki/Help:Introduction

Related changes

https://en.wikipedia.org/wiki/Help:Introduction

Upload file

https://en.wikipedia.org/wiki/Help:Introduction

Permanent link

https://en.wikipedia.org/wiki/Help:Introduction

Page information

https://en.wikipedia.org/wiki/Help:Introduction

Cite this page

https://en.wikipedia.org/wiki/Help:Introduction

Get shortened URL

https://en.wikipedia.org/wiki/Help:Introduction

Download QR code

https://en.wikipedia.org/wiki/Help:Introduction

Print/export

Download as PDF

https://en.wikipedia.org/wiki/Help:Introduction

Printable version

https://en.wikipedia.org/wiki/Help:Introduction

In other projects

Wikidata item

https://en.wikipedia.org/wiki/Help:Introduction

From Wikipedia, the free encyclopedia Theory of brain function For the speech processing technology, see

Linear predictive coding

https://en.wikipedia.org/wiki/Linear\_predictive\_coding

neuroscience

https://en.wikipedia.org/wiki/Neuroscience

predictive coding

(also known as

predictive processing

) is a theory of

https://en.wikipedia.org/wiki/Brain

function which postulates that the brain is constantly generating and updating a "

mental model

https://en.wikipedia.org/wiki/Mental\_model

" of the environment. According to the theory, such a mental model is used to predict input signals from the

https://en.wikipedia.org/wiki/Sense

that are then compared with the actual input signals from those senses. Predictive coding is member of a wider set of theories that follow the

Bayesian brain hypothesis

https://en.wikipedia.org/wiki/Bayesian\_approaches\_to\_brain\_function

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=1

Theoretical ancestors to predictive coding date back as early as 1860 with

https://en.wikipedia.org/wiki/Helmholtz

's concept of

unconscious inference

https://en.wikipedia.org/wiki/Unconscious\_inference

Unconscious inference refers to the idea that the human brain fills in visual information to make sense of a scene. For example, if something is relatively smaller than another object in the visual field, the brain uses that information as a likely cue of depth, such that the perceiver ultimately (and involuntarily) experiences depth. The understanding of perception as the interaction between sensory stimuli (bottom-up) and conceptual knowledge (top-down) continued to be established by

Jerome Bruner

https://en.wikipedia.org/wiki/Jerome\_Bruner

who, starting in the 1940s, studied the ways in which needs, motivations and expectations influence perception, research that came to be known as 'New Look' psychology. In 1981,

https://en.wikipedia.org/wiki/James\_McClelland\_(psychologist)

https://en.wikipedia.org/wiki/David\_Rumelhart

examined the interaction between processing features (lines and contours) which form letters, which in turn form words.

While the features suggest the presence of a word, they found that when letters were situated in the context of a word, people were able to identify them faster than when they were situated in a non-word without semantic context. McClelland and Rumelhart's parallel processing model describes perception as the meeting of top-down (conceptual) and bottom-up (sensory) elements.

In the late 1990s, the idea of top-down and bottom-up processing was translated into a computational model of vision by

https://en.wikipedia.org/wiki/Rajesh\_Rao

https://en.wikipedia.org/wiki/Dana\_H.\_Ballard

Their paper demonstrated that there could be a

generative model

https://en.wikipedia.org/wiki/Generative\_model

of a scene (top-down processing), which would receive feedback via error signals (how much the visual input varied from the prediction), which would subsequently lead to updating the prediction. The computational model was able to replicate well-established receptive field effects, as well as less understood extra-classical receptive field effects such as

end-stopping

https://en.wikipedia.org/wiki/Hypercomplex\_cell

Rick Grush proposed a model of neural perceptual processing according to which the brain constantly generates predictions based on a generative model (what Grush called an ‘emulator’), and compares that prediction to the actual sensory input. The difference, or ‘sensory residual’ would then be used to update the model so as to produce a more accurate estimate of the perceived domain. On Grush’s account, the top-down and bottom up signals would be combined in a way sensitive to the expected noise (aka uncertainty) in the bottom-up signal, so that in situations in which the sensory signal was known to be less trustworthy, the top-down prediction would be given greater weight, and vice-versa. The emulation framework was also shown to be hierarchical, with modality-specific emulators providing top-down expectations for sensory signals as well as higher-level emulators providing expectations of the distal causes of those signals. Grush applied the theory to visual perception, visual and motor imagery, language, and theory of mind phenomena.

General framework

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=2

Conceptual Schematic of Predictive Coding with 2 levels

Predictive coding was initially developed as a model of the

sensory system

https://en.wikipedia.org/wiki/Sensory\_system

, where the brain solves the problem of modelling distal causes of sensory input through a version of

Bayesian inference

https://en.wikipedia.org/wiki/Bayesian\_inference

. It assumes that the brain maintains an active internal representations of the distal causes, which enable it to predict the sensory inputs.

A comparison between predictions and sensory input yields a difference measure (e.g. prediction error, free energy, or surprise) which, if it is sufficiently large beyond the levels of expected statistical noise, will cause the internal model to update so that it better predicts sensory input in the future.

If, instead, the model accurately predicts driving sensory signals, activity at higher levels cancels out activity at lower levels, and the internal model remains unchanged. Thus, predictive coding inverts the conventional view of perception as a mostly bottom-up process, suggesting that it is largely constrained by prior predictions, where signals from the external world only shape perception to the extent that they are propagated up the cortical hierarchy in the form of prediction error.

Prediction errors can not only be used for inferring distal causes, but also

https://en.wikipedia.org/wiki/Unsupervised\_learning

neural plasticity

https://en.wikipedia.org/wiki/Neural\_plasticity

Here the idea is that the

representations

https://en.wikipedia.org/wiki/Neural\_coding

learned by cortical neurons reflect the

statistical regularities

https://en.wikipedia.org/wiki/Efficient\_coding\_hypothesis#Natural\_images\_and\_statistics

in the sensory data. This idea is also present in many other theories of neural learning, such as

sparse coding

https://en.wikipedia.org/wiki/Sparse\_coding

, with the central difference being that in predictive coding not only the connections to sensory inputs are learned (i.e., the

receptive field

https://en.wikipedia.org/wiki/Receptive\_field

), but also top-down predictive connections from higher-level representations. This makes predictive coding similar to some other models of hierarchical learning, such as

Helmholtz machines

https://en.wikipedia.org/wiki/Helmholtz\_machines

Deep belief networks

https://en.wikipedia.org/wiki/Deep\_belief\_network

, which however employ different learning algorithms. Thus, the dual use of prediction errors for both inference and learning is one of the defining features of predictive coding.

Precision weighting

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=3

The precision of incoming sensory input is their predictability based on

signal noise

https://en.wikipedia.org/wiki/Noise\_(signal\_processing)

and other factors. Estimates of the precision are crucial for effectively minimizing prediction error, as it allows to weight sensory inputs and predictions according to their reliability.

For instance, the noise in the visual signal varies between dawn and dusk, such that greater conditional confidence is assigned to sensory prediction errors in broad daylight than at nightfall.

Similar approaches are successfully used in other algorithms performing

Bayesian inference

https://en.wikipedia.org/wiki/Bayesian\_inference

, e.g., for

Bayesian filtering

https://en.wikipedia.org/wiki/Bayesian\_filtering

Kalman filter

https://en.wikipedia.org/wiki/Kalman\_filter

It has also been proposed that such weighting of prediction errors in proportion to their estimated precision is, in essence,

https://en.wikipedia.org/wiki/Attention

and that the process of devoting attention may be neurobiologically accomplished by

ascending reticular activating systems

https://en.wikipedia.org/wiki/Reticular\_activating\_system

(ARAS) optimizing the “gain” of prediction error units. However, it has also been argued that precision weighting can only explain "endogenous spatial attention", but not other forms of attention.

Active inference

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=4

The same principle of prediction error minimization has been used to provide an account of behavior in which motor actions are not commands but descending proprioceptive predictions. In this scheme of

active inference

https://en.wikipedia.org/wiki/Active\_inference

, classical reflex arcs are coordinated so as to selectively sample sensory input in ways that better fulfill predictions, thereby minimizing proprioceptive prediction errors.

Indeed, Adams et al. (2013) review evidence suggesting that this view of hierarchical predictive coding in the motor system provides a principled and neurally plausible framework for explaining the agranular organization of the motor cortex.

This view suggests that “perceptual and motor systems should not be regarded as separate but instead as a single active inference machine that tries to predict its sensory input in all domains: visual, auditory, somatosensory, interoceptive and, in the case of the motor system, proprioceptive."

Neural theory in predictive coding

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=5

Much of the early work that applied a predictive coding framework to neural mechanisms came from sensory processing, particularly in the

visual cortex

https://en.wikipedia.org/wiki/Visual\_cortex

These theories assume that the cortical architecture can be divided into hierarchically stacked levels, which correspond to different cortical regions. Every level is thought to house (at least) two types of neurons: "prediction neurons", which aim to predict the bottom-up inputs to the current level, and "error neurons", which signal the difference between input and prediction. These neurons are thought to be mainly non-superficial and superficial

pyramidal neurons

https://en.wikipedia.org/wiki/Pyramidal\_neurons

interneurons

https://en.wikipedia.org/wiki/Interneuron#Cortex

take up different functions.

Within cortical regions, there is evidence that different

cortical layers

https://en.wikipedia.org/wiki/Cerebral\_cortex#Layers

may facilitate the integration of feedforward and feed-backward projections across hierarchies.

These cortical layers have therefore been assumed to be central in the computation of predictions and prediction errors, with the basic unit being a

cortical column

https://en.wikipedia.org/wiki/Cortical\_column

A common view is that

error neurons

reside in supragranular layers 2 and 3, since these neurons show sparse activity and tend to respond to unexpected events

prediction neurons

reside in deep layer 5, where many neurons exhibit dense responses

precision weighting

might be implemented through diverse mechanism, such as

neuromodulators

https://en.wikipedia.org/wiki/Neuromodulators

or long range projections from other brain areas (e.g.,

https://en.wikipedia.org/wiki/Thalamus

However, thus far there is no consensus on how the brain most likely implements predictive coding. Some theories, for example, propose that supragranular layers contain not only error, but also prediction neurons.

It is also still debated through which mechanisms error neurons might compute the prediction error.

Since prediction errors can be both negative and positive, but biological neurons can only show positive activity, more complex error coding schemes are required. To circumvent this problem, more recent theories have proposed that error computation might take place in neural

https://en.wikipedia.org/wiki/Dendrites

The neural architecture and computations proposed in these dendritic theories are similar to what has been proposed in

Hierarchical temporal memory

https://en.wikipedia.org/wiki/Hierarchical\_temporal\_memory

theory of cortex.

Applying predictive coding

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=6

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=7

The empirical evidence for predictive coding is most robust for perceptual processing. As early as 1999, Rao and Ballard proposed a hierarchical

visual processing

https://en.wikipedia.org/wiki/Visual\_processing

model in which higher-order visual cortical area sends down predictions and the feedforward connections carry the residual errors between the predictions and the actual lower-level activities.

According to this model, each level in the hierarchical model network (except the lowest level, which represents the image) attempts to predict the responses at the next lower level via feedback connections, and the error signal is used to correct the estimate of the input signal at each level concurrently.

Emberson et al. established the top-down modulation in infants using a cross-modal audiovisual omission paradigm, determining that even infant brains have expectation about future sensory input that is carried downstream from visual cortices and are capable of expectation-based feedback.

Functional near-infrared spectroscopy (fNIRS) data showed that infant

occipital cortex

https://en.wikipedia.org/wiki/Occipital\_cortex

responded to unexpected visual omission (with no visual information input) but not to expected visual omission. These results establish that in a hierarchically organized perception system, higher-order neurons send down predictions to lower-order neurons, which in turn sends back up the prediction error signal.

Interoception

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=8

] Main article:

Interoception

https://en.wikipedia.org/wiki/Interoception

There have been several competing models for the role of predictive coding in

interoception

https://en.wikipedia.org/wiki/Interoception

https://en.wikipedia.org/wiki/Anil\_Seth

proposed that our subjective feeling states, otherwise known as emotions, are generated by predictive models that are actively built out of causal interoceptive appraisals.

In relation to how we attribute internal states of others to causes, Sasha Ondobaka, James Kilner, and

Karl Friston

https://en.wikipedia.org/wiki/Karl\_Friston

(2015) proposed that the

free energy principle

https://en.wikipedia.org/wiki/Free\_energy\_principle

requires the brain to produce a continuous series of predictions with the goal of reducing the amount of prediction error that manifests as “free energy”.

These errors are then used to model anticipatory information about what the state of the outside world will be and attributions of causes of that world state, including understanding of causes of others’ behavior. This is especially necessary because, to create these attributions, our multimodal sensory systems need interoceptive predictions to organize themselves. Therefore, Ondobaka posits that predictive coding is key to understanding other people's internal states.

Lisa Feldman Barrett

https://en.wikipedia.org/wiki/Lisa\_Feldman\_Barrett

and W. Kyle Simmons proposed the Embodied Predictive Interoception Coding model, a framework that unifies Bayesian active inference principles with a physiological framework of corticocortical connections.

Using this model, they posited that agranular visceromotor cortices are responsible for generating predictions about interoception, thus, defining the experience of interoception.

Contrary to the inductive notion that emotion categories are biologically distinct, Barrett proposed later the theory of constructed emotion, which is the account that a biological emotion category is constructed based on a conceptual category—the accumulation of instances sharing a goal.

In a predictive coding model, Barrett hypothesizes that, in interoception, our brains regulate our bodies by activating "embodied simulations" (full-bodied representations of sensory experience) to anticipate what our brains predict that the external world will throw at us sensorially and how we will respond to it with action. These simulations are either preserved if, based on our brain's predictions, they prepare us well for what actually subsequently occurs in the external world, or they, and our predictions, are adjusted to compensate for their error in comparison to what actually occurs in the external world and how well-prepared we were for it. Then, in a trial-error-adjust process, our bodies find similarities in goals among certain successful anticipatory simulations and group them together under conceptual categories. Every time a new experience arises, our brains use this past trial-error-adjust history to match the new experience to one of the categories of accumulated corrected simulations that it shares the most similarity with. Then, they apply the corrected simulation of that category to the new experience in the hopes of preparing our bodies for the rest of the experience. If it does not, the prediction, the simulation, and perhaps the boundaries of the conceptual category are revised in the hopes of higher accuracy next time, and the process continues. Barrett hypothesizes that, when prediction error for a certain category of simulations for x-like experiences is minimized, what results is a correction-informed simulation that the body will reenact for every x-like experience, resulting in a correction-informed full-bodied representation of sensory experience—an emotion. In this sense, Barrett proposes that we construct our emotions because the conceptual category framework our brains use to compare new experiences, and to pick the appropriate predictive sensory simulation to activate, is built on the go.

Computer science

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=9

With the rising popularity of

representation learning

https://en.wikipedia.org/wiki/Feature\_learning

, the theory has also been actively pursued and applied in

machine learning

https://en.wikipedia.org/wiki/Machine\_learning

and related fields.

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=10

One of the biggest challenges to test predictive coding has been the imprecision of exactly how prediction error minimization works.

In some studies, the increase in

https://en.wikipedia.org/wiki/Blood-oxygen-level\_dependent\_imaging

signal has been interpreted as error signal while in others it indicates changes in the input representation.

A crucial question that needs to be addressed is what exactly constitutes error signal and how it is computed at each level of information processing.

Another challenge that has been posed is predictive coding's computational tractability. According to Kwisthout and van Rooij, the subcomputation in each level of the predictive coding framework potentially hides a computationally intractable problem, which amounts to “intractable hurdles” that computational modelers have yet to overcome.

Future research could focus on clarifying the neurophysiological mechanism and computational model of predictive coding.

according to whom?

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Error-driven learning

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Blue Brain Project

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Cognitive biology

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Cognitive linguistics

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Cognitive neuropsychology

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Cognitive neuroscience

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Cognitive science

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Conceptual blending

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Conceptual metaphor

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Cortical column

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Embodied bilingual language

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Embodied cognitive science

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Embodied Embedded Cognition

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Embodied music cognition

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Extended cognition

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Extended mind thesis

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Externalism

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Image schema

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Moravec's paradox

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Neuroconstructivism

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Neuropsychology

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Neurophenomenology

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Philosophy of mind

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Plant cognition

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Practopoiesis

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Situated cognition

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

Where Mathematics Comes From

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=11

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=12

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=12

"Helmholtz's Treatise on Physiological Optics - Free"

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&action=edit&section=12

. 2018-03-20. Archived from

the original

http://poseidon.sunyopt.edu/BackusLab/Helmholtz/

on 20 March 2018 . Retrieved 2022-01-05 .

http://poseidon.sunyopt.edu/BackusLab/Helmholtz/

McClelland, J. L. & Rumelhart, D. E. (1981). "An interactive activation model of context effects in letter perception: I. An account of basic findings".

Psychological Review

(5): 375– 407.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1037/0033-295X.88.5.375

https://doi.org/10.1037%2F0033-295X.88.5.375

Rao, Rajesh P. N.; Ballard, Dana H. (1999). "Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects".

Nature Neuroscience

(1): 79– 87.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1038/4580

https://doi.org/10.1038%2F4580

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Grush, Rick (2004).

"The emulation theory of representation: Motor control, imagery, and perception"

https://www.cambridge.org/core/product/identifier/S0140525X04000093/type/journal\_article

Behavioral and Brain Sciences

(3): 377– 396.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1017/S0140525X04000093

https://doi.org/10.1017%2FS0140525X04000093

https://en.wikipedia.org/wiki/ISSN\_(identifier)

https://en.wikipedia.org/wiki/ISSN\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

Clark, Andy (2013).

"Whatever next? Predictive brains, situated agents, and the future of cognitive science"

https://doi.org/10.1017%2FS0140525X12000477

Behavioral and Brain Sciences

(3): 181– 204.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1017/S0140525X12000477

https://doi.org/10.1017%2FS0140525X12000477

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

Friston, Karl (August 2018).

"Does predictive coding have a future?"

https://www.nature.com/articles/s41593-018-0200-7

Nature Neuroscience

(8): 1019– 1021.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1038/s41593-018-0200-7

https://doi.org/10.1038%2Fs41593-018-0200-7

https://en.wikipedia.org/wiki/ISSN\_(identifier)

https://en.wikipedia.org/wiki/ISSN\_(identifier)

https://en.wikipedia.org/wiki/ISSN\_(identifier)

Friston, Karl J.; Feldman, Harriet (2010).

"Attention, Uncertainty, and Free-Energy"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3001758

Frontiers in Human Neuroscience

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.3389/fnhum.2010.00215

https://doi.org/10.3389%2Ffnhum.2010.00215

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Hohwy, Jakob (2012).

"Attention and Conscious Perception in the Hypothesis Testing Brain"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3317264

Frontiers in Psychology

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.3389/fpsyg.2012.00096

https://doi.org/10.3389%2Ffpsyg.2012.00096

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Friston, Karl (2009). "The free-energy principle: A rough guide to the brain?".

Trends in Cognitive Sciences

(7): 293– 301.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1016/j.tics.2009.04.005

https://doi.org/10.1016%2Fj.tics.2009.04.005

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

Ransom M. & Fazelpour S (2015). Three Problems for the Predictive Coding Theory of Attention.

http://mindsonline.philosophyofbrains.com/2015/session4/three-problems-for-the-predictive-coding-theory-of-attention/

http://mindsonline.philosophyofbrains.com/2015/session4/three-problems-for-the-predictive-coding-theory-of-attention/

Adams, Rick A.; Shipp, Stewart; Friston, Karl J. (2013).

"Predictions not commands: Active inference in the motor system"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3637647

Brain Structure and Function

(3): 611– 643.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1007/s00429-012-0475-5

https://doi.org/10.1007%2Fs00429-012-0475-5

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Bastos, Andre M.; Usrey, W. Martin; Adams, Rick A.; Mangun, George R.; Fries, Pascal; Friston, Karl J. (2012).

"Canonical Microcircuits for Predictive Coding"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3777738

(4): 695– 711.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1016/j.neuron.2012.10.038

https://doi.org/10.1016%2Fj.neuron.2012.10.038

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Bennett, Max (2020).

"An Attempt at a Unified Theory of the Neocortical Microcircuit in Sensory Cortex"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7416357

Frontiers in Neural Circuits

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.3389/fncir.2020.00040

https://doi.org/10.3389%2Ffncir.2020.00040

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Keller, Georg B.; Mrsic-Flogel, Thomas D. (October 2018).

"Predictive Processing: A Canonical Cortical Computation"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6400266

(2): 424– 435.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1016/j.neuron.2018.10.003

https://doi.org/10.1016%2Fj.neuron.2018.10.003

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

Millidge, Beren; Seth, Anil; Buckley, Christopher (2022-01-19). "Predictive Coding: a Theoretical and Experimental Review".

https://en.wikipedia.org/wiki/ArXiv\_(identifier)

https://arxiv.org/abs/2107.12979

https://arxiv.org/archive/cs.AI

https://arxiv.org/archive/cs.AI

Mikulasch, Fabian A.; Rudelt, Lucas; Wibral, Michael; Priesemann, Viola (January 2023). "Where is the error? Hierarchical predictive coding through dendritic error computation".

Trends in Neurosciences

(1): 45– 59.

https://en.wikipedia.org/wiki/ArXiv\_(identifier)

https://arxiv.org/abs/2205.05303

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1016/j.tins.2022.09.007

https://doi.org/10.1016%2Fj.tins.2022.09.007

https://doi.org/10.1016%2Fj.tins.2022.09.007

Whittington, James C.R.; Bogacz, Rafal (March 2019).

"Theories of Error Back-Propagation in the Brain"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6382460

Trends in Cognitive Sciences

(3): 235– 250.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1016/j.tics.2018.12.005

https://doi.org/10.1016%2Fj.tics.2018.12.005

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

Emberson, Lauren L.; Richards, John E.; Aslin, Richard N. (2015).

"Top-down modulation in the infant brain: Learning-induced expectations rapidly affect the sensory cortex at 6 months"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4534272

Proceedings of the National Academy of Sciences

(31): 9585– 9590.

https://en.wikipedia.org/wiki/Bibcode\_(identifier)

2015PNAS..112.9585E

https://ui.adsabs.harvard.edu/abs/2015PNAS..112.9585E

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1073/pnas.1510343112

https://doi.org/10.1073%2Fpnas.1510343112

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Seth, Anil K. (2013).

"Interoceptive inference, emotion, and the embodied self"

https://doi.org/10.1016%2Fj.tics.2013.09.007

Trends in Cognitive Sciences

(11): 565– 573.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1016/j.tics.2013.09.007

https://doi.org/10.1016%2Fj.tics.2013.09.007

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

Ondobaka, Sasha; Kilner, James; Friston, Karl (2017).

"The role of interoceptive inference in theory of mind"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5312780

Brain and Cognition

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1016/j.bandc.2015.08.002

https://doi.org/10.1016%2Fj.bandc.2015.08.002

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Barrett, Lisa Feldman; Simmons, W. Kyle (2015).

"Interoceptive predictions in the brain"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4731102

Nature Reviews Neuroscience

(7): 419– 429.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1038/nrn3950

https://doi.org/10.1038%2Fnrn3950

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Barrett, Lisa Feldman (2016).

"The theory of constructed emotion: An active inference account of interoception and categorization"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5390700

Social Cognitive and Affective Neuroscience

(1): 1– 23.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1093/scan/nsw154

https://doi.org/10.1093%2Fscan%2Fnsw154

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Barrett, L.F. (2017). How emotions are made: The secret life of the brain. New York: Houghton Mifflin Harcourt.

https://en.wikipedia.org/wiki/ISBN\_(identifier)

https://en.wikipedia.org/wiki/ISBN\_(identifier)

https://en.wikipedia.org/wiki/ISBN\_(identifier)

Millidge, Beren; Salvatori, Tommaso; Song, Yuhang; Bogacz, Rafal; Lukasiewicz, Thomas (2022-02-18). "Predictive Coding: Towards a Future of Deep Learning beyond Backpropagation?".

https://en.wikipedia.org/wiki/ArXiv\_(identifier)

https://arxiv.org/abs/2202.09467

https://arxiv.org/archive/cs.NE

https://arxiv.org/archive/cs.NE

Ororbia, Alexander G.; Kifer, Daniel (2022-04-19).

"The Neural Coding Framework for Learning Generative Models"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9018730

Nature Communications

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1038/s41467-022-29632-7

https://doi.org/10.1038%2Fs41467-022-29632-7

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Hinton, Geoffrey E. (2007). "Learning multiple layers of representation".

Trends in Cognitive Sciences

(10): 428– 434.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1016/j.tics.2007.09.004

https://doi.org/10.1016%2Fj.tics.2007.09.004

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

Kogo, Naoki; Trengove, Chris (2015).

"Is predictive coding theory articulated enough to be testable?"

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4561670

Frontiers in Computational Neuroscience

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.3389/fncom.2015.00111

https://doi.org/10.3389%2Ffncom.2015.00111

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMC\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

https://en.wikipedia.org/wiki/PMID\_(identifier)

Kwisthout, Johan; Van Rooij, Iris (2020). "Computational Resource Demands of a Predictive Bayesian Brain".

Computational Brain & Behavior

(2): 174– 188.

https://en.wikipedia.org/wiki/Doi\_(identifier)

10.1007/s42113-019-00032-3

https://doi.org/10.1007%2Fs42113-019-00032-3

https://en.wikipedia.org/wiki/Hdl\_(identifier)

2066/218854

https://hdl.handle.net/2066%2F218854

https://en.wikipedia.org/wiki/S2CID\_(identifier)

https://en.wikipedia.org/wiki/S2CID\_(identifier)

Retrieved from "

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&oldid=1268484164

https://en.wikipedia.org/w/index.php?title=Predictive\_coding&oldid=1268484164

https://en.wikipedia.org/wiki/Help:Category

Cognitive modeling

https://en.wikipedia.org/wiki/Help:Category

Neuropsychology

https://en.wikipedia.org/wiki/Help:Category

https://en.wikipedia.org/wiki/Help:Category

Hidden categories:

Articles with short description

https://en.wikipedia.org/wiki/Help:Category

Short description is different from Wikidata

https://en.wikipedia.org/wiki/Help:Category

All articles with specifically marked weasel-worded phrases

https://en.wikipedia.org/wiki/Help:Category

Articles with specifically marked weasel-worded phrases from January 2021

https://en.wikipedia.org/wiki/Help:Category