---
tags:
  - notebooklm-import
notebook: "B_Spiritual Practice - Religion - Science - Psychology - Philosophy - Meditation"
category: "research"
---

https://pmc.ncbi.nlm.nih.gov/articles/PMC8169103/

Skip to main content

An official website of the United States government

Here's how you know

Official websites use .gov

website belongs to an official government organization in the United States.

Secure .gov websites use HTTPS

( Lock Locked padlock icon ) or

means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.

Publications

Account settings

Logged in as:

Publications

Account settings

Advanced Search

Journal List

As a library, NLM provides access to scientific literature. Inclusion in an NLM database does not imply endorsement of, or agreement with, the contents by NLM or the National Institutes of Health.

Learn more:

PMC Disclaimer

https://pmc.ncbi.nlm.nih.gov/about/disclaimer/

PMC Copyright Notice

https://pmc.ncbi.nlm.nih.gov/about/copyright/

. 2021 Apr 22;10:e64972. doi:

10.7554/eLife.64972

https://doi.org/10.7554/eLife.64972

Anticipation of temporally structured events in the brain

Caroline S Lee

https://doi.org/10.7554/eLife.64972

Caroline S Lee

Columbia University, Department of Psychology, New York, United States

Dartmouth College, Department of Psychological and Brain Sciences, Hanover, United States Find articles by

Caroline S Lee

https://pubmed.ncbi.nlm.nih.gov/?term=%22Lee%20CS%22%5BAuthor%5D

https://pubmed.ncbi.nlm.nih.gov/?term=%22Aly%20M%22%5BAuthor%5D

Columbia University, Department of Psychology, New York, United States Find articles by

https://pubmed.ncbi.nlm.nih.gov/?term=%22Aly%20M%22%5BAuthor%5D

Christopher Baldassano

https://pubmed.ncbi.nlm.nih.gov/?term=%22Baldassano%20C%22%5BAuthor%5D

Christopher Baldassano

Columbia University, Department of Psychology, New York, United States Find articles by

Christopher Baldassano

https://pubmed.ncbi.nlm.nih.gov/?term=%22Baldassano%20C%22%5BAuthor%5D

Editors: Marius V Peelen

, Timothy E Behrens

Columbia University, Department of Psychology, New York, United States

Dartmouth College, Department of Psychological and Brain Sciences, Hanover, United States

Radboud University, Netherlands

University of Oxford, United Kingdom

Corresponding author.

Marius V Peelen

: Reviewing Editor

Timothy E Behrens

: Senior Editor

Received 2020 Nov 17; Accepted 2021 Apr 21; Collection date 2021.

© 2021, Lee et al

This article is distributed under the terms of the

Creative Commons Attribution License

https://creativecommons.org/licenses/by/4.0/

, which permits unrestricted use and redistribution provided that the original author and source are credited.

PMC Copyright notice

https://creativecommons.org/licenses/by/4.0/

PMCID: PMC8169103 PMID:

https://pubmed.ncbi.nlm.nih.gov/33884953/

Learning about temporal structure is adaptive because it enables the generation of expectations. We examined how the brain uses experience in structured environments to anticipate upcoming events. During fMRI (functional magnetic resonance imaging), individuals watched a 90 s movie clip six times. Using a hidden Markov model applied to searchlights across the whole brain, we identified temporal shifts between activity patterns evoked by the first vs. repeated viewings of the movie clip. In many regions throughout the cortex, neural activity patterns for repeated viewings shifted to precede those of initial viewing by up to 15 s. This anticipation varied hierarchically in a posterior (less anticipation) to anterior (more anticipation) fashion. We also identified specific regions in which the timing of the brain’s event boundaries was related to those of human-labeled event boundaries, with the timing of this relationship shifting on repeated viewings. With repeated viewing, the brain’s event boundaries came to precede human-annotated boundaries by 1–4 s on average. Together, these results demonstrate a hierarchy of anticipatory signals in the human brain and link them to subjective experiences of events.

Research organism:

eLife digest

Anticipating future events is essential. It allows individuals to plan and prepare what they will do seconds, minutes, or hours in the future. But how the brain can predict future events in both the short-term and long-term is not yet clear. Researchers know that the brain processes images or other sensory information in stages. For example, visual features are processed from lines to shapes to objects, and eventually scenes. This staged approach allows the brain to create representations of many parts of the world simultaneously.

A similar hierarchy may be at play in anticipation. Different parts of the brain may track what is happening now, and what could happen in the next few seconds and minutes. This would provide a way for the brain to forecast upcoming events in the immediate, near, and more distant future at the same time.

Now, Lee et al. show that the regions in the back of the brain anticipate the immediate future, while longer-term predictions are made in brain regions near the front. In the experiments, study participants watched a 90-second clip of the movie ‘The Grand Budapest Hotel’ six times while undergoing functional magnetic resonance imaging (fMRI). Then, Lee et al. used computer modeling to compare the brain activity captured by fMRI during successive viewings. This allowed the researchers to watch participants’ brain activity moment-by-moment.

As the participants repeatedly watched the movie clip, their brains began to anticipate what was coming next. Regions near the back of the brain like the visual cortex anticipated events in the next 1 to 4 seconds. Areas in the middle of the brain anticipated 5 to 8 seconds in the future. The front of brain anticipated 8 to 15 seconds into the future. Lee et al. show that many parts of the brain work together to predict the near and more distant future. More research is needed to understand how this information translates into actions. Learning more may help scientists understand how diseases or injuries affect people’s ability to plan and respond to future events.

Introduction

A primary function of the brain is to adaptively use past experience to generate expectations about events that are likely to occur in the future (

Clark, 2013

https://pmc.ncbi.nlm.nih.gov#bib11

Friston, 2005

https://pmc.ncbi.nlm.nih.gov#bib19

). Indeed, anticipation and prediction are ubiquitous in the brain, spanning systems that support sensation, action, memory, motivation, and language (

den Ouden et al., 2010

https://pmc.ncbi.nlm.nih.gov#bib15

). For example, the visual system takes advantage of the world’s relative stability over space and time to anticipate upcoming input (

de Lange et al., 2018

https://pmc.ncbi.nlm.nih.gov#bib14

Summerfield and Egner, 2009

https://pmc.ncbi.nlm.nih.gov#bib38

). The majority of studies examining anticipatory signals, however, have tested anticipation based on memory for relatively simple associations between pairs of discrete stimuli, such as auditory tones, lines, dots, oriented gratings, or abstract objects (e.g.,

Alink et al., 2010

https://pmc.ncbi.nlm.nih.gov#bib2

Gavornik and Bear, 2014

https://pmc.ncbi.nlm.nih.gov#bib20

Hindy et al., 2016

https://pmc.ncbi.nlm.nih.gov#bib22

Kok et al., 2012

https://pmc.ncbi.nlm.nih.gov#bib26

Kok et al., 2014

https://pmc.ncbi.nlm.nih.gov#bib27

Kok and Turk-Browne, 2018

https://pmc.ncbi.nlm.nih.gov#bib28

). These studies have found anticipatory signals about a single upcoming stimulus in a variety of brain regions, from perceptual regions (

Kok et al., 2012

https://pmc.ncbi.nlm.nih.gov#bib26

) to the medial temporal lobe (

Hindy et al., 2016

https://pmc.ncbi.nlm.nih.gov#bib22

Kok and Turk-Browne, 2018

https://pmc.ncbi.nlm.nih.gov#bib28

). How does the brain use repeated experience in naturalistic environments to anticipate upcoming sequences of events that extend farther into the future?

Prior work has shown that the brain integrates information about the recent past over a hierarchy of timescales (

Aly et al., 2018

https://pmc.ncbi.nlm.nih.gov#bib3

Hasson et al., 2015

https://pmc.ncbi.nlm.nih.gov#bib21

Kurby and Zacks, 2008

https://pmc.ncbi.nlm.nih.gov#bib29

). Lower-order areas primarily represent the current moment, whereas higher-order areas are sensitive to information from many seconds or even minutes into the past. Higher-order regions with longer timescales play a critical role in organizing perceptual input into semantically meaningful schematic representations (

Baldassano et al., 2017

https://pmc.ncbi.nlm.nih.gov#bib5

Baldassano et al., 2018

https://pmc.ncbi.nlm.nih.gov#bib6

). What is less clear is whether this hierarchy also exists in a prospective direction: as we move from lower-order perceptual systems into higher-order areas, do these regions exhibit different timescales of anticipation into the future? We previously found that higher-order regions did exhibit anticipatory signals when individuals had prior knowledge of the general structure of a narrative (

Baldassano et al., 2017

https://pmc.ncbi.nlm.nih.gov#bib5

). But these individuals only had knowledge of information at relatively long timescales (e.g., the general sequence of events, and not moment-by-moment perceptual features), so we were unable to assess whether they could generate expectations across the timescale hierarchy.

Here, we examine how the brain anticipates event boundaries in familiar sequences of actions. We used a naturalistic narrative stimulus (a movie), in which regularities are present at multiple timescales. For example, upon second viewing of a movie, one can anticipate the next action to be taken in a given scene, the next character to appear, the next location that is visited, and the last scene of the movie. The presence of predictability at multiple timescales in the same stimulus enables us to identify varying timescales of anticipation in the brain that co-exist simultaneously. We hypothesized that the timescale of anticipation in the brain would vary continuously, with progressively higher-order regions (e.g., prefrontal cortex) anticipating events that are further in the future compared to lower-order regions (e.g., visual cortex).

To test this, we examined brain activity with functional magnetic resonance imaging (fMRI) while individuals watched a 90 s clip from the movie

The Grand Budapest Hotel

six times. To uncover anticipation in the brain, we used a searchlight approach in which, for each region of interest, we fit a hidden Markov model (HMM) to identify temporal shifts between multivariate activity patterns (functionally hyperaligned across individuals using the shared response model [SRM]) evoked by the first viewing of the movie clip compared to repeated viewings (

https://pmc.ncbi.nlm.nih.gov#fig1

). This model assumes that the brain’s response to a structured narrative stimulus consists of a sequence of distinct, stable activity patterns that correspond to event structure in the narrative (

Baldassano et al., 2017

https://pmc.ncbi.nlm.nih.gov#bib5

). We could then identify, on a timepoint-by-timepoint basis, the extent to which viewers were activating event-specific brain activity patterns earlier in subsequent viewings of the movie, by drawing on their prior experience. Because the HMM infers a probability distribution over states, it is able to detect subtle shifts between viewings; activity patterns may reflect a combination of current and upcoming events, and the degree of anticipation can vary throughout the clip.

Figure 1. Computing varying timescales of anticipatory signals by examining temporal shifts in events across multiple viewings of a movie.

Open in a new tab

https://pmc.ncbi.nlm.nih.gov#bib5

) Given the voxel by time pattern of responses evoked by the movie clip on each viewing (darker colors indicate higher levels of activity), our goal is to model all viewings as a series of transitions through a shared sequence of event patterns. (

) By fitting a hidden Markov model (HMM) jointly to all viewings, we can identify this shared sequence of event patterns, as well as a probabilistic estimate of event transitions. Regions with anticipatory representations are those in which event transitions occur earlier in time for repeated viewings of a stimulus compared to the initial viewing, indicated by an upward shift on the plot of the expected value of the event at each timepoint. (

) Taking the temporal derivative of the event timecourse plot in (

) produces a measure of the strength of event shifts at each moment in time, allowing for comparison with event boundary annotations from human observers.

We also compared the brain’s event boundaries (identified by the HMM) to subjective event boundary annotations made by a separate group of participants. This allowed us to test how the relationship between the brain’s events and subjective event boundaries changes with repeated viewings. Together, this approach allowed us to characterize the nature of hierarchical anticipatory signals in the brain and link them to behavioral measures of event perception.

Timescales of anticipation in the brain

To identify anticipatory signals in the brain, we examined TR-by-TR brain activity patterns during each of the six viewings of the movie clip. For each spherical searchlight within the brain volume, we fit an HMM jointly to all repetitions, to identify a sequence of event patterns common to all viewings and the timing of spatial pattern changes for each viewing. At each timepoint for each viewing, the HMM produced a probability distribution that describes the mixture of event patterns active at that timepoint. Computing the expected value of this distribution provides an index of how the brain transitions through event patterns on each viewing, allowing us to identify how this timing shifts within each region of the brain.

Our analysis revealed temporal shifts in event patterns in many brain regions, including lateral occipital cortex, angular and supramarginal gyri, lateral and anterior temporal lobe, lateral and medial prefrontal cortex (mPFC), and insular cortex (

https://pmc.ncbi.nlm.nih.gov#fig2

). The magnitude of this shift varied along a posterior-to-anterior temporal hierarchy (Spearman’s rho = 0.58, p=0.0030), with the most anterior regions in the temporal pole and prefrontal cortex showing shifts of up to 15 s on subsequent viewings compared to the first viewing. This hierarchy persisted even when computed on the unthresholded anticipation map including voxels that did not meet the threshold for statistical significance (Spearman’s rho = 0.42, p=0.0028; see

Figure 2—figure supplement 1

https://pmc.ncbi.nlm.nih.gov#fig2s1

). There were no significant correlations with the left-to-right axis (rho = 0.06, p=0.41 for thresholded map; rho = 0.12, p=0.29 for unthresholded map) or the inferior-to-superior axis (rho = 0.07, p=0.28 for thresholded map; rho = −0.11, p=0.73 for unthresholded map). We obtained a similar map when comparing the first viewing to just the sixth viewing alone (see

Figure 2—figure supplement 2

https://pmc.ncbi.nlm.nih.gov#fig2s2

Figure 2. Timescales of anticipation vary across the cortical hierarchy.

) Multiple regions exhibited shifts in event timing between initial and repeated viewings, with event transitions shifting earlier in time with subsequent viewings. Across the brain, anticipation timescales varied from a few seconds to 15 s, with the longest timescale anticipatory signals in prefrontal cortex and the temporal pole. Anticipation followed a posterior-to-anterior hierarchy, with progressively anterior areas generating anticipatory signals that reach further into the future (Spearman’s rho = 0.58, p=0.0030). Statistical thresholding was conducted via a permutation test, with correction for false discovery rate (FDR), q<0.05. (

) Event by time plots for three sample regions from (

), selected post hoc for illustration. Because the HMM produces a probability distribution across states at each timepoint, which can reflect a combination of current and upcoming event representations, we plot the expected value of the event assignments at each timepoint. The upward shift from the first viewing to subsequent viewings indexes the amount of anticipation.

Figure 2—figure supplement 1. Unthresholded statistical map of anticipation timescales.

This figure shows the same analysis as in

https://pmc.ncbi.nlm.nih.gov#fig2

, but without statistical thresholding. The posterior-to-anterior hierarchy of anticipation persists in this unthresholded map (Spearman’s rho = 0.42, p=0.0028).

Figure 2—figure supplement 2. Timescales of anticipation when the first viewing is compared to the last viewing.

This figure shows the same analysis as that in

https://pmc.ncbi.nlm.nih.gov#fig2

, except that the first viewing is compared to the last (6th) viewing only.

Figure 2—figure supplement 3. Timescales of anticipation as a function of the optimal number of events.

) This map depicts the optimal number of events in each brain region that shows statistically significant anticipation (i.e., masked by regions shown in

https://pmc.ncbi.nlm.nih.gov#fig2

). The optimal number of events was determined by maximizing the log-likelihood of the HMM on the first movie viewing. Purple indicates the fastest timescale (optimally fit by eight events, average event duration = 11 s) and yellow indicates the slowest timescale (optimally fit by two events, average event duration = 45 s). (

) Anticipation (

https://pmc.ncbi.nlm.nih.gov#fig2

) is shown binned by the optimal event timescale. Anticipation is further reaching in regions with longer timescales (Spearman’s rho = 0.319, p=0.00031).

Figure 2—figure supplement 4. Cross-correlation analysis of anticipation.

Cross-correlations were conducted between the activity timecourse of a given region for the first movie viewing and the average of the subsequent movie viewings. The regions depicted showed statistically significant shifts in activity, such that the peak correlation occurred when the subsequent viewing activity was shifted earlier in time. Statistical thresholding was conducted via a permutation test, with correction for false discovery rate (FDR), q<0.05. Colors depict the temporal shift of the peak in the cross-correlation.

Open in a new tab

https://pmc.ncbi.nlm.nih.gov/figure/fig2/

We compared how this hierarchy of anticipation timescales related to the intrinsic processing timescales in each region during the initial viewing of the movie clip. Identifying the optimal number of HMM events for each searchlight, we observed a timescale hierarchy similar to that described in previous work, with faster timescales in sensory regions and slower timescales in more anterior regions (

Figure 2—figure supplement 3a

https://pmc.ncbi.nlm.nih.gov#fig2s3

). Regions with longer intrinsic timescales also showed a greater degree of anticipation with repeated viewing (

Figure 2—figure supplement 3b

https://pmc.ncbi.nlm.nih.gov#fig2s3

We also compared these results to those obtained by using a simple cross-correlation approach, testing for a fixed temporal offset between the responses to initial and repeated viewing. This approach did detect significant anticipation in some anterior regions, but was much less sensitive than the more flexible HMM fits, especially in posterior regions (

Figure 2—figure supplement 4

https://pmc.ncbi.nlm.nih.gov#fig2s4

Relationship with human-annotated events

Our data-driven method for identifying event structure in fMRI data does not make use of information about the content of the stimulus, leaving open the question of how the HMM-identified event boundaries correspond to subjective event transitions in the movie. One possibility is that the brain’s event boundaries could

well-aligned with event boundaries in the movie and then shift earlier (indicating anticipation of upcoming stimulus content). Alternatively, they may initially lag behind stimulus boundaries (reflecting a delayed response time on initial viewing) and then shift to become

aligned with movie scene transitions on repeated viewings. Finally, both patterns may exist simultaneously in the brain, but in different brain regions.

We asked human raters to identify event transitions in the stimulus, labeling each ‘meaningful segment’ of activity (

https://pmc.ncbi.nlm.nih.gov#fig3

). To generate a hypothesis about the strength and timing of event shifts in the fMRI data, we convolved the distribution of boundary annotations with a hemodynamic response function (HRF) as shown in

https://pmc.ncbi.nlm.nih.gov#fig4

. We then explored alignment between these human-annotated event boundaries and the event boundaries extracted from the brain response to each viewing, as shown in

https://pmc.ncbi.nlm.nih.gov#fig1

. In each searchlight, we cross-correlated the brain-derived boundary timecourse with the event annotation timecourse to find the temporal offset that maximized this correlation.

Figure 3. An example of event annotations from

The Grand Budapest Hotel

Open in a new tab

Dotted lines demarcate events and phrases between the lines are brief titles given by one participant to describe each event. (Frames in this figure have been blurred to comply with copyright restrictions, but all participants were presented with the original unblurred version.)

Figure 4. Construction of behavioral boundary timecourse from human annotations.

Open in a new tab

The number of boundary annotations at each second of the movie clip (in gray) was convolved with a hemodynamic response function (HRF) to produce a continuous measure of boundary strength (black line).

We found three clusters in the middle temporal gyrus (MTG), fusiform gyrus (FG), and superior temporal sulcus (STS) in which the optimal lag for the repeated viewings was significantly earlier than for the initial viewing, indicating that the relationship between the brain-derived HMM event boundaries and the human-annotated boundaries was changing with repeated viewings (

https://pmc.ncbi.nlm.nih.gov#fig5

). The HMM boundaries on the first viewing were significantly later than the annotated boundaries in FG and STS, while the optimal lag did not significantly differ from 0 in MTG (95% confidence intervals for the optimal lag, in seconds: MTG = [−0.27, 2.86]; FG = [0.14, 1.99]; STS = [1.48, 8.53]). The HMM boundaries on repeated viewings were significantly earlier than the annotated boundaries in all three regions (95% confidence intervals for the average optimal lag, in seconds: MTG = [−4.06, –1.83]; FG = [−1.56, –0.26]; STS = [−3.06, –1.69]).

Figure 5. Correlations between the brain’s event transitions and human-annotated event boundaries.

Open in a new tab

https://pmc.ncbi.nlm.nih.gov#fig5

Cross-correlation plots show the correlation between the brain’s hidden Markov model (HMM) event boundaries and annotated event boundaries as the timecourses are shifted with respect to one another. The correlation at 0 lag indicates the similarity between the brain’s event boundaries and annotated event boundaries when the timecourses are aligned. Negative lags show the correlations when the human-annotated event timecourse is shifted earlier in time, and positive lags show the correlation when the human-annotated event timecourse is shifted later in time. Peaks in the cross-correlation plot indicate the lag that produced the highest correlation between the brain’s event boundaries and annotated event boundaries. On initial viewing, the HMM event boundaries for the fusiform gyrus and superior temporal sulcus lagged significantly behind the annotated event boundaries, while the timing of the peak correlation for the middle temporal gyrus did not significantly differ from 0 lag. On subsequent viewings, the HMM event boundaries in all three regions shifted to be significantly earlier than the initial viewing, with the timing of the peak correlation significantly preceding 0 lag.

We investigated whether the brain contains a hierarchy of anticipatory signals during passive viewing of a naturalistic movie. We found that regions throughout the brain exhibit anticipation of upcoming events in audiovisual stimuli, with activity patterns shifting earlier in time as participants repeatedly watched the same movie clip. This anticipation occurred at varying timescales along the cortical hierarchy. Anticipation in higher-order, more anterior regions reached further into the future than that in lower-order, more posterior regions. Furthermore, in a subset of these regions, the coupling between event representations and human-annotated events shifted with learning: event boundaries in the brain came to reliably precede subjective event boundaries in the movie.

Regions with anticipatory representations

One region showing long-timescale anticipatory signals was the bilateral anterior insula. This region has been linked to anticipation of diverse categories of positive and negative outcomes (

Liu et al., 2011

https://pmc.ncbi.nlm.nih.gov#bib32

), including outcomes that will be experienced by other people (

Singer et al., 2009

https://pmc.ncbi.nlm.nih.gov#bib37

). The movie stimulus used in our experiment depicts an interview in which the protagonist is initially judged to have ‘zero’ experience but then ends up impressing the interviewer, allowing for anticipation of this unexpected social outcome only on repeat viewings. Other regions showing long timescales of anticipation include the medial prefrontal cortex (mPFC), which tracks high-level narrative schemas (

Baldassano et al., 2018

https://pmc.ncbi.nlm.nih.gov#bib6

) and has been proposed to play a general role in event prediction (

Alexander and Brown, 2014

https://pmc.ncbi.nlm.nih.gov#bib1

), and lateral prefrontal cortex, including the inferior frontal gyrus, which processes structured sequences across multiple domains (

Uddén and Bahlmann, 2012

https://pmc.ncbi.nlm.nih.gov#bib39

We also observed shorter-timescale anticipation throughout lateral occipital and ventral temporal cortex, which, though primarily thought to process bottom-up visual information, also exhibits event-specific patterns during recall (

Chen et al., 2017

https://pmc.ncbi.nlm.nih.gov#bib10

). A top-down memory-driven signal could be responsible for driving anticipatory activation in these regions during repeated movie viewing (

Finnie et al., 2021

https://pmc.ncbi.nlm.nih.gov#bib18

). Future work incorporating eye-tracking measurements could determine whether anticipatory eye movements can account for the temporal shifts in these regions, or if this anticipation is separate from the representation of the current retinal input.

We did not observe widespread anticipatory signals in primary sensory areas, although some prior fMRI studies have been able to observe such signals in early regions such as V1 (

Alink et al., 2010

https://pmc.ncbi.nlm.nih.gov#bib2

Ekman et al., 2017

https://pmc.ncbi.nlm.nih.gov#bib16

Hindy et al., 2016

https://pmc.ncbi.nlm.nih.gov#bib22

Kok et al., 2012

https://pmc.ncbi.nlm.nih.gov#bib26

). One possibility is that the rich, ongoing sensory input dominated relatively small anticipatory signals in these regions. Paradigms involving periods without any sensory input (e.g., occasionally removing the audiovisual movie from the screen during repeated viewings) may be necessary to detect these subtle signals. Alternatively, ultra-fast fMRI sequences (

Ekman et al., 2017

https://pmc.ncbi.nlm.nih.gov#bib16

) or alternative imaging modalities (discussed below) may be required to track anticipation at a subsecond scale.

Relationship to previous studies of timescale hierarchies

Previous work has identified cumulatively longer timescales up the cortical hierarchy but has primarily focused on representations of the past.

Lerner et al., 2011

https://pmc.ncbi.nlm.nih.gov#bib30

demonstrated hierarchical cortical dynamics in participants who listened to variants of a 7 min narrative that was scrambled at different timescales (e.g., paragraphs, sentences, or words). Response reliability, measured as the correlation in BOLD activity timecourses across individuals, varied based on the timescale of scrambling, with higher-level brain regions responding consistently to only the more-intact narrative conditions. This led to the idea that higher-order brain regions contain larger ‘temporal receptive windows’ than lower-order areas, in that their activity at a given moment is influenced by relatively more of the past. Likewise, using intracranial EEG (iEEG),

Honey et al., 2012

https://pmc.ncbi.nlm.nih.gov#bib23

observed progressively longer temporal receptive windows in successive stages of the cortical hierarchy in participants who watched intact and scrambled versions of the movie

Dog Day Afternoon

. These findings can be described by the process memory framework (

Hasson et al., 2015

https://pmc.ncbi.nlm.nih.gov#bib21

), where hierarchical memory timescales process, represent, and support longer and longer units of information. We found that this hierarchy also exists in the prospective direction, with the degree of anticipatory temporal shifts increasing from posterior-to-anterior regions of the brain. Furthermore, regions with longer intrinsic processing timescales showed further-reaching anticipation. These results extend the process memory framework, suggesting that the timescales in these regions are relevant not only for online processing and memory, but also for future anticipation or simulation.

Although prior work has uncovered anticipatory and predictive coding in the brain, most studies have examined fixed, shorter timescales of anticipation. Moreover, these shorter timescales have often been studied using simple, non-narrative stimuli such as objects moving across the screen, short visual sequences, and visual pattern completion tasks (

Alink et al., 2010

https://pmc.ncbi.nlm.nih.gov#bib2

Ekman et al., 2017

https://pmc.ncbi.nlm.nih.gov#bib16

Gavornik and Bear, 2014

https://pmc.ncbi.nlm.nih.gov#bib20

Hindy et al., 2016

https://pmc.ncbi.nlm.nih.gov#bib22

Kok et al., 2012

https://pmc.ncbi.nlm.nih.gov#bib26

). Some studies have used dynamic movie stimuli, but anticipation was measured via correlations between initial and repeated viewing of a movie at a constant fixed lag of 2 s (

Richardson and Saxe, 2020

https://pmc.ncbi.nlm.nih.gov#bib36

). Such an approach is not well suited to capturing dynamic levels of anticipation within and across brain regions.

Research investigating longer timescales of anticipation, such as learning future state representations in a maze task, examined single timescales up to 30 s ahead in OFC-VMPFC regions (

Elliott Wimmer and Büchel, 2019

https://pmc.ncbi.nlm.nih.gov#bib17

). Some studies that use narrative stimuli have examined specially constructed texts in order to manipulate predictions about upcoming sentences; for example, work by

Kandylaki et al., 2016

https://pmc.ncbi.nlm.nih.gov#bib24

demonstrated that predictive processing of referents in narratives can be modulated by voice (passive vs. active) and causality (high vs. low). Our results show that in a naturalistic setting, in which structure exists at many timescales, anticipation at multiple levels can occur in parallel across different brain regions. We found anticipation up to approximately 15 s into the future with our 90 s stimulus, but future work with stimuli of longer duration could uncover even longer timescales of anticipation, on the scale of minutes. Simultaneously maintaining expectations at varying timescales could allow for flexible behaviors, because different timescales of anticipation may be helpful for a variety of tasks and actions. Taking action to avoid immediate harm or danger would require shorter timescales of prediction, whereas cultivating social relationships demands predictions on longer timescales.

These results are consistent with those of

Baldassano et al., 2017

https://pmc.ncbi.nlm.nih.gov#bib5

, in which some participants listening to an audio narrative had advance knowledge of the high-level events of the story (because they had previously watched a movie version of the narrative). Using a similar HMM approach as in this paper, the authors observed shifts in event boundaries in higher-level regions including angular gyrus, posterior medial cortex, and mPFC. In the current study, however, participants were repeatedly exposed to an identical movie stimulus, allowing them to generate expectations at a broad range of timescales, including the timescales of fast-changing low-level visual features. This novel approach allowed us to observe for the first time that anticipation occurs in both low- and high-level regions, with shorter-timescale anticipation in visual occipital regions and the furthest-reaching anticipatory signals in prefrontal cortex.

Our model detects anticipation as temporal shifts in events, and though timepoints can reflect ‘mixed’ event assignments, it assumes that the underlying event patterns themselves (

https://pmc.ncbi.nlm.nih.gov#fig1

) are constant. This view of anticipation is complementary to other theories of predictive representations, in which event patterns themselves should change over time to incorporate future information. One example is the ‘successor representation’ model from the field of reinforcement learning, which describes a representation in which each state (here, event representation) comes to include features of future events, weighted by their likelihood of occurring and their distance into the future (

Dayan, 1993

https://pmc.ncbi.nlm.nih.gov#bib13

). Successor representations can also be constructed at multiple scales (by changing the relative weighting of events near vs. far in the future). Such multi-scale representations are useful for goal-directed prediction that require multiple stages of planning (

Momennejad and Howard, 2018

https://pmc.ncbi.nlm.nih.gov#bib35

Brunec and Momennejad, 2019

https://pmc.ncbi.nlm.nih.gov#bib8

). Future work could explore how these two different theories could be integrated to model both mixing of event patterns and temporal shifts in the activation of these event patterns.

Anticipation in other neuroimaging modalities

The current fMRI study is complementary to investigations of memory replay and anticipation that use MEG and iEEG. In an MEG study,

Michelmann et al., 2019

https://pmc.ncbi.nlm.nih.gov#bib33

found fast, compressed replay of encoded events during recall, with the speed of replay varying across the event. Furthermore, an iEEG investigation found anticipatory signals in auditory cortex when individuals listened to the same story twice (

Michelmann et al., 2020

https://pmc.ncbi.nlm.nih.gov#bib34

). In another MEG study,

Wimmer et al., 2020

https://pmc.ncbi.nlm.nih.gov#bib40

found compressed replay of previously encoded information. Replay was forward when participants were remembering what came after an event, and backward when participants were remembering what came before an event. The forward replay observed in the Wimmer et al. study may be similar to the anticipatory signals observed in the current study, although there was no explicit demand on memory retrieval in our paradigm. Thus, one possibility is that the anticipatory signals observed in MEG or iEEG are the same as those we observe in fMRI, except that they are necessarily sluggish and smoothed in time when measured via a hemodynamic response. This possibility is supported by fMRI work showing evidence for compressed anticipatory signals, albeit at a slower timescale relative to MEG (

Ekman et al., 2017

https://pmc.ncbi.nlm.nih.gov#bib16

An alternative possibility is that the anticipatory signals measured in our study are fundamentally different from those captured via MEG or iEEG. That could explain why we failed to find widespread anticipatory signals in primary visual or primary auditory cortex: the anticipatory signals in those regions might have been too fast to be captured with fMRI, particularly when competing with incoming, dynamic perceptual input. Future studies that obtain fMRI and MEG or iEEG in participants watching the same movie would be informative in that regard. It is possible that fMRI may be particularly well suited for capturing relatively slow anticipation of stable events, as opposed to faster anticipatory signals relating to fast sub-events. Nevertheless, advances in fMRI analyses may allow the detection of very fast replay or anticipation, closing the gap between these methods and allowing more direct comparisons (

Wittkuhn and Schuck, 2021

https://pmc.ncbi.nlm.nih.gov#bib41

Future directions and conclusions

One limitation of the current work is the reliance on one movie clip. Movie clips of different durations might yield different results. For example, it is an open question whether the duration of anticipation scales with the length of the movie and playback speed or if the amount of anticipation is fixed (

Lerner et al., 2014

https://pmc.ncbi.nlm.nih.gov#bib31

Baumgarten et al., 2021

https://pmc.ncbi.nlm.nih.gov#bib7

). Furthermore, the content of the movie and how frequently event boundaries occur may change anticipation amounts. That said, anticipatory signals in naturalistic stimuli have been observed across multiple studies that use different movies and auditorily presented stories (e.g.,

Baldassano et al., 2017

https://pmc.ncbi.nlm.nih.gov#bib5

Michelmann et al., 2020

https://pmc.ncbi.nlm.nih.gov#bib34

Michelmann et al., 2019

https://pmc.ncbi.nlm.nih.gov#bib33

Elliott Wimmer and Büchel, 2019

https://pmc.ncbi.nlm.nih.gov#bib17

Wimmer et al., 2020

https://pmc.ncbi.nlm.nih.gov#bib40

). Thus, it is likely that anticipatory hierarchies will also replicate across different stimuli. There may nevertheless be important differences across stimuli. For example, the specific regions that are involved in anticipation may vary depending on what the most salient features of a movie or narrative are (e.g., particular emotional states, actions, conversations, or perceptual information).

The detection of varying timescales of anticipation in the brain can be applied to multiple domains and modalities of memory research. Future work could explore even shorter timescales using other neuroimaging modalities, or longer timescales using longer movies or narratives from TV series that span multiple episodes. Furthermore, the impact of top-down goals on the hierarchy of anticipation timescales could be explored by using different tasks that require different levels of anticipation, such as anticipating camera angle changes vs. location changes. Brain stimulation studies or studies of patients with brain lesions could also explore the extent to which anticipation in lower-level regions relies on feedback from higher-level regions (

Auksztulewicz and Friston, 2016

https://pmc.ncbi.nlm.nih.gov#bib4

Kiebel et al., 2008

https://pmc.ncbi.nlm.nih.gov#bib25

The increased use of naturalistic, dynamic stimuli in neuroscience, and the development of methods to analyze the resulting data, has opened many avenues for research exploring flexible, future-oriented behavior. Our results and analysis approach provide a new framework for studying how anticipatory signals are distributed throughout the cortex, modulated by prior memory, and adaptive for improving comprehension and behavior.

Materials and methods

Grand Budapest Hotel dataset

We used data collected by

Aly et al., 2018

https://pmc.ncbi.nlm.nih.gov#bib3

. Thirty individuals (12 men, age: M = 23.0 years, SD = 4.2; education: M = 15.3 years, SD = 3.2; all right-handed) watched movie clips from

The Grand Budapest Hotel

while undergoing fMRI. None of the participants reported previously seeing this movie. We analyzed data from the

condition, during which participants watched a continuous 90 s clip from the movie in its original temporal order. This clip was watched six times, interspersed with other video clips that are not considered here. This

clip depicts an interview scene between the protagonist and his future employer inside of the Grand Budapest Hotel. Stimuli and data are available on OpenNeuro:

https://openneuro.org/datasets/ds001545/versions/1.1.1

https://openneuro.org/datasets/ds001545/versions/1.1.1

Data were acquired on a 3T Siemens Prisma scanner with a 64-channel head/neck coil using a multiband echo planar imaging (EPI) sequence (repetition time = 1.5 s; echo time = 39 ms; flip angle = 50°; acceleration factor = 4; shift = 3; voxel size = 2.0 mm iso). T1-weighted structural images (whole-brain high-resolution; 1.0 mm iso) were acquired with an MPRAGE sequence. Field maps (40 oblique axial slices; 3 mm iso) were collected to aid registration. The fMRI scan took place over three experimental runs, each of which contained two presentations of the

movie clip (as well as other movie clips not considered here).

The first three EPI volumes of each run were discarded to allow for T1 equilibration. Data preprocessing was carried out in FSL, and included brain extraction, motion correction, high-pass filtering (max period = 140 s), spatial smoothing (3 mm FWHM Gaussian kernel), and registration to standard Montreal Neurological Institute (MNI) space. After preprocessing, the functional images for each run were divided into volumes that corresponded to each of the video clips presented within that run, and only the two

clips within each run are considered further. Finally, each voxel’s timecourse was z-scored to have zero mean and unit variance.

Event annotations by human observers

Fourteen individuals (nine men) were asked to mark event boundaries corresponding to the same 90 s

The Grand Budapest Hotel

as shown to the fMRI participants. Each participant was asked to pause the clip at the end of a meaningful segment and to record the time and a brief title corresponding to the segment (

https://pmc.ncbi.nlm.nih.gov#fig3

). Specifically, they were given the following instructions:

The movie clip can be divided into meaningful segments. Record the times denoting when you feel like a meaningful segment has ended. Pause the clip at the end of the segment, write down the time in the spreadsheet, and provide a short, descriptive title. Try to record segments with as few viewings of the movie clip as possible; afterward, record the number of times you viewed the clip.

Although participants were allowed to watch the clip multiple times, they were instructed to minimize and report the number of viewings needed to complete the task. No participant reported watching the clip more than three times.

Detecting anticipatory signals using an event segmentation model

Group-averaged fMRI data were fit with the event segmentation model described by

Baldassano et al., 2017

https://pmc.ncbi.nlm.nih.gov#bib5

. This HMM assumes that (1) events are a sequence of discrete states, (2) each event is represented in the brain by a unique spatial activity pattern, and (3) all viewings of the movie evoke the same sequence of activity patterns in the same order (though possibly with different timings). We fit the HMM jointly to all six viewings. This fitting procedure involved simultaneously estimating a sequence of event activity patterns that were shared across viewings, and estimating the probability of belonging to each of these events for every timepoint in all six datasets. The model was fit with seven events; this number was chosen to match the approximate timescale of the semantic events in the narrative, matching the mean number of events annotated by human observers (mean = 6.5).

After fitting the HMM, we obtain an event by timepoint matrix for each viewing, giving the probability that each timepoint belongs to each event. Note that because this assignment of timepoints to events is probabilistic, it is possible for the HMM to detect that the pattern of voxel activity at a timepoint reflects a mixture of multiple event patterns. This allows us to track subtle changes in the timecourse of how the brain is transitioning between events. We took the expectation over events at each timepoint, yielding curves showing the average event label at each timepoint for each viewing. To compute shifts in time between the first viewing and the average of repeated viewings, the area under the curve (AUC) was computed for each viewing. We then computed the amount of anticipation as the average AUC for repeated viewing (viewings 2–6) minus the AUC for the first viewing. In a supplementary analysis, we compared the first viewing to the last viewing only. To convert to seconds, we divide by the vertical extent of the graph (number of events minus 1) and multiplied by the repetition time (1.5 s). We then performed a one-tailed statistical test (described below) to determine whether this difference was significantly positive, indicating earlier event transitions with repeated viewing. Not only does this approach provide a way of quantifying anticipation, it gives us a trajectory of the most likely event at any given timepoint, as well as the onset and duration of each event.

We obtained whole-brain results using a searchlight analysis. We generated spherical searchlights spaced evenly throughout the MNI volume (radius = 5 voxels; stride = 5 voxels). We retained only the searchlights with at least 20 voxels which were inside a standard MNI brain mask and for which at least 15 participants had valid data for all viewings. We then used the SRM (

Chen et al., 2015

https://pmc.ncbi.nlm.nih.gov#bib9

) to functionally hyperalign all participants into shared 10-dimensional space (jointly fitting the alignment across all six viewings) and averaged their responses together. This produced a 10 feature by 60 timepoint data matrix for each of the six viewings, which was input to the HMM analysis described above. After running the analysis in all searchlights, the anticipation in each voxel was computed as the average anticipation of all searchlights that included that voxel.

To assess statistical significance, we utilized a permutation-based null hypothesis testing approach. We constructed null datasets by randomly shuffling each participant’s six responses to the six presentations of the movie clip. The full analysis pipeline (including hyperalignment) was run 100 times, once on the real (unpermuted) dataset and 99 times on null (permuted) datasets, with each analysis producing a map of anticipation across all voxels. A one-tailed p-value was obtained in each voxel by fitting a normal distribution to the null anticipation values, and then finding the fraction of this distribution that exceeded the real result in this voxel (i.e., showed more anticipation than in our unpermuted dataset). Voxels were determined significant (q<0.05) after applying the Benjamini-Hochberg FDR correction, as implemented in AFNI (

https://pmc.ncbi.nlm.nih.gov#bib12

To determine if anticipation systematically varied across the cortex in the hypothesized posterior-to-anterior direction, we calculated the Spearman’s correlation between the Y-coordinate of each significant (q<0.05) voxel (indexing the position of that voxel along the anterior/posterior axis) and the mean amount of anticipation in that voxel. To obtain a p-value, the observed correlation was compared to a null distribution in which the Spearman’s correlation was computed with the null anticipation values from the permutation analysis described above, in which the order of the viewings was randomly scrambled for each participant. For comparison, the correlation was also computed for the X (left-right) and Z (inferior-superior) axes. This analysis was repeated on unthresholded anticipation maps, to examine if this hierarchy remained even when including regions whose anticipation amounts did not reach statistical significance.

To relate the timescales of anticipation to the intrinsic timescales of brain regions during the first viewing, we fit the HMM on the first viewing alone, varying the number of events from 2 to 10. The HMM was trained on the average response from half of the participants (fitting the sequence of activity patterns for the events and the event variance) and the log-likelihood of the model was then measured on the average response in the other half of the participants. The training and testing sets were then swapped, and the log-likelihoods from both directions were averaged together. Hyperalignment was not used during this fitting process, to ensure that the training and testing sets remained independent. The number of events that yielded the largest log-likelihood was identified as the optimal number of events for that searchlight. The optimal number of events was then compared to the anticipation timescale in that region (from the main analysis), using Spearman’s correlation.

For comparison, we also ran a searchlight looking for anticipatory effects using a non-HMM cross-correlation approach. Within each searchlight, we obtained an average timecourse across all voxels and correlated the response to the first viewing with the average response to repeated viewings at differing lags. Using the same quadratic-fit approach for identifying the optimal lag described below, we tested whether the repeated-viewing timecourse was significantly ahead of the initial-viewing timecourse (relative to a null distribution in which the viewing order was shuffled within each subject). The p-values obtained were then corrected for FDR.

Comparison of event boundaries in brain regions to annotations

We compared the event boundaries identified by the HMM within each searchlight to the event boundaries annotated by human observers. To obtain an event boundary timecourse from the annotations, we convolved the number of annotations (across all raters) at each second with the HRF (

https://pmc.ncbi.nlm.nih.gov#fig4

). Separately, we generated a continuous measure of HMM ‘boundary-ness’ at each timepoint by taking the derivative of the expected value of the event assignment for each timepoint, as illustrated in

https://pmc.ncbi.nlm.nih.gov#fig1

. Moments with high boundary strength indicate moments in which the brain pattern was rapidly switching between event patterns. We cross-correlated the HMM boundary strength timecourse for each viewing with the annotated event boundary timecourse, shifting the annotated timecourse forward and backward to determine the optimal temporal offset (with the highest correlation). We measured the timing of the peak correlation by identifying the local maximum in correlation closest to 0 lag, then fitting a quadratic function to the maximum correlation lag and its two neighboring lags and recording the location of the peak of this quadratic fit. This produced a continuous estimate of the optimal lag for each viewing. We measured the amount of shift between the optimal lag for the first viewing and the average of the optimal lags for repeated viewings, and obtained a p-value by comparing to the null distribution over maps with permuted viewing orders (as in the main analysis), then performed an FDR correction.

We identified three gray matter clusters significant at q<0.05. To statistically assess whether the optimal lags differed from 0 in the three searchlights maximally overlapping these three clusters, we repeated the cross-correlation analysis in 100 bootstrap samples, in which we resampled from the raters who generated the annotated event boundaries. We obtained 95% bootstrap confidence intervals for maximally correlated lag on the first viewing and for the average of the maximally correlated lags on repeated viewings.

Code and resource availability

Data preprocessing scripts and python code to reproduce all the results in this paper are available at

https://github.com/dpmlab/Anticipation-of-temporally-structured-events

https://github.com/dpmlab/Anticipation-of-temporally-structured-events

(copy archived at

swh:1:rev:8fbd488c04d47148f9a53048de5d05a90e1c1663

https://archive.softwareheritage.org/swh:1:dir:b4206124101d0eb41a414054ab42c61042674408;origin=https://github.com/dpmlab/Anticipation-of-temporally-structured-events;visit=swh:1:snp:e7d3b704ea175d657be758cda2c4071d7605bbfa;anchor=swh:1:rev:8fbd488c04d47148f9a53048de5d05a90e1c1663

). Results in MNI space can be viewed at

https://identifiers.org/neurovault.collection:9584

https://identifiers.org/neurovault.collection:9584

Acknowledgements

We thank the Aly and Baldassano labs for their feedback and support during this project, Janice Chen for helpful conversations about prediction hierarchies, and our three reviewers for proposing many useful improvements to the analyses.

Funding Statement

No external funding was received for this work.

Contributor Information

Christopher Baldassano, Email: c.baldassano@columbia.edu.

Marius V Peelen, Radboud University, Netherlands.

Timothy E Behrens, University of Oxford, United Kingdom.

Additional information

Competing interests

No competing interests declared.

Author contributions

Software, Formal analysis, Validation, Investigation, Visualization, Writing - original draft, Project administration, Writing - review and editing.

Conceptualization, Supervision, Writing - original draft, Writing - review and editing.

Conceptualization, Software, Formal analysis, Supervision, Validation, Visualization, Methodology, Writing - original draft, Writing - review and editing.

Additional files

Transparent reporting form

elife-64972-transrepform.docx

https://pmc.ncbi.nlm.nih.gov/articles/instance/8169103/bin/elife-64972-transrepform.docx

(247.5KB, docx)

Data availability

We used a publicly-available dataset, from

https://openneuro.org/datasets/ds001545/versions/1.1.1

https://openneuro.org/datasets/ds001545/versions/1.1.1

The following previously published dataset was used:

Aly M, Chen J, Turk-Browne NB, Hasson U. 2019. Learning Naturalistic Temporal Structure in the Posterior Medial Network. OpenNeuro.

Alexander WH, Brown JW. A general role for medial prefrontal cortex in event prediction. Frontiers in Computational Neuroscience. 2014;8:69. doi: 10.3389/fncom.2014.00069. [

https://doi.org/10.3389/fncom.2014.00069

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC4093652/

https://pubmed.ncbi.nlm.nih.gov/25071539/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Frontiers%20in%20Computational%20Neuroscience&title=A%20general%20role%20for%20medial%20prefrontal%20cortex%20in%20event%20prediction&author=WH%20Alexander&author=JW%20Brown&volume=8&publication\_year=2014&pages=69&pmid=25071539&doi=10.3389/fncom.2014.00069&

Alink A, Schwiedrzik CM, Kohler A, Singer W, Muckli L. Stimulus predictability reduces responses in primary visual cortex. Journal of Neuroscience. 2010;30:2960–2966. doi: 10.1523/JNEUROSCI.3730-10.2010. [

https://doi.org/10.1523/JNEUROSCI.3730-10.2010

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC6633950/

https://pubmed.ncbi.nlm.nih.gov/20181593/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Journal%20of%20Neuroscience&title=Stimulus%20predictability%20reduces%20responses%20in%20primary%20visual%20cortex&author=A%20Alink&author=CM%20Schwiedrzik&author=A%20Kohler&author=W%20Singer&author=L%20Muckli&volume=30&publication\_year=2010&pages=2960-2966&pmid=20181593&doi=10.1523/JNEUROSCI.3730-10.2010&

Aly M, Chen J, Turk-Browne NB, Hasson U. Learning naturalistic temporal structure in the posterior medial network. Journal of Cognitive Neuroscience. 2018;30:1345–1365. doi: 10.1162/jocn\_a\_01308. [

https://doi.org/10.1162/jocn\_a\_01308

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC6211568/

https://pubmed.ncbi.nlm.nih.gov/30004848/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Journal%20of%20Cognitive%20Neuroscience&title=Learning%20naturalistic%20temporal%20structure%20in%20the%20posterior%20medial%20network&author=M%20Aly&author=J%20Chen&author=NB%20Turk-Browne&author=U%20Hasson&volume=30&publication\_year=2018&pages=1345-1365&pmid=30004848&doi=10.1162/jocn\_a\_01308&

Auksztulewicz R, Friston K. Repetition suppression and its contextual determinants in predictive coding. Cortex. 2016;80:125–140. doi: 10.1016/j.cortex.2015.11.024. [

https://doi.org/10.1016/j.cortex.2015.11.024

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC5405056/

https://pubmed.ncbi.nlm.nih.gov/26861557/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Cortex&title=Repetition%20suppression%20and%20its%20contextual%20determinants%20in%20predictive%20coding&author=R%20Auksztulewicz&author=K%20Friston&volume=80&publication\_year=2016&pages=125-140&pmid=26861557&doi=10.1016/j.cortex.2015.11.024&

Baldassano C, Chen J, Zadbood A, Pillow JW, Hasson U, Norman KA. Discovering event structure in continuous narrative perception and memory. Neuron. 2017;95:709–721. doi: 10.1016/j.neuron.2017.06.041. [

https://doi.org/10.1016/j.neuron.2017.06.041

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC5558154/

https://pubmed.ncbi.nlm.nih.gov/28772125/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Neuron&title=Discovering%20event%20structure%20in%20continuous%20narrative%20perception%20and%20memory&author=C%20Baldassano&author=J%20Chen&author=A%20Zadbood&author=JW%20Pillow&author=U%20Hasson&volume=95&publication\_year=2017&pages=709-721&pmid=28772125&doi=10.1016/j.neuron.2017.06.041&

Baldassano C, Hasson U, Norman KA. Representation of Real-World event schemas during narrative perception. The Journal of Neuroscience. 2018;38:9689–9699. doi: 10.1523/JNEUROSCI.0251-18.2018. [

https://doi.org/10.1523/JNEUROSCI.0251-18.2018

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC6222059/

https://pubmed.ncbi.nlm.nih.gov/30249790/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=The%20Journal%20of%20Neuroscience&title=Representation%20of%20Real-World%20event%20schemas%20during%20narrative%20perception&author=C%20Baldassano&author=U%20Hasson&author=KA%20Norman&volume=38&publication\_year=2018&pages=9689-9699&pmid=30249790&doi=10.1523/JNEUROSCI.0251-18.2018&

Baumgarten TJ, Maniscalco B, Lee JL, Flounders MW, Abry P, He BJ. Neural integration underlying naturalistic prediction flexibly adapts to varying sensory input rate. Nature Communications. 2021;12:2643. doi: 10.1038/s41467-021-22632-z. [

https://doi.org/10.1038/s41467-021-22632-z

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC8113607/

https://pubmed.ncbi.nlm.nih.gov/33976118/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Nature%20Communications&title=Neural%20integration%20underlying%20naturalistic%20prediction%20flexibly%20adapts%20to%20varying%20sensory%20input%20rate&author=TJ%20Baumgarten&author=B%20Maniscalco&author=JL%20Lee&author=MW%20Flounders&author=P%20Abry&volume=12&publication\_year=2021&pages=2643&pmid=33976118&doi=10.1038/s41467-021-22632-z&

Brunec IK, Momennejad I. Predictive representations in hippocampal and prefrontal hierarchies. bioRxiv. 2019 doi: 10.1101/786434. [

https://doi.org/10.1101/786434

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC8802932/

https://pubmed.ncbi.nlm.nih.gov/34799416/

Chen P-H, Chen J, Yeshurun Y, Hasson U, Haxby JV, Ramadge PJ. A Reduced-Dimension fMRI shared response model. Advances in Neural Information Processing Systems.2015. [

Google Scholar

https://scholar.google.com/scholar\_lookup?Chen%20P-H,%20Chen%20J,%20Yeshurun%20Y,%20Hasson%20U,%20Haxby%20JV,%20Ramadge%20PJ.%20A%20Reduced-Dimension%20fMRI%20shared%20response%20model.%20Advances%20in%20Neural%20Information%20Processing%20Systems.2015.

Chen J, Leong YC, Honey CJ, Yong CH, Norman KA, Hasson U. Shared memories reveal shared structure in neural activity across individuals. Nature Neuroscience. 2017;20:115–125. doi: 10.1038/nn.4450. [

https://doi.org/10.1038/nn.4450

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC5191958/

https://pubmed.ncbi.nlm.nih.gov/27918531/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Nature%20Neuroscience&title=Shared%20memories%20reveal%20shared%20structure%20in%20neural%20activity%20across%20individuals&author=J%20Chen&author=YC%20Leong&author=CJ%20Honey&author=CH%20Yong&author=KA%20Norman&volume=20&publication\_year=2017&pages=115-125&pmid=27918531&doi=10.1038/nn.4450&

Clark A. Whatever next? predictive brains, situated agents, and the future of cognitive science. Behavioral and Brain Sciences. 2013;36:181–204. doi: 10.1017/S0140525X12000477. [

https://doi.org/10.1017/S0140525X12000477

https://pubmed.ncbi.nlm.nih.gov/23663408/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Behavioral%20and%20Brain%20Sciences&title=Whatever%20next?%20predictive%20brains,%20situated%20agents,%20and%20the%20future%20of%20cognitive%20science&author=A%20Clark&volume=36&publication\_year=2013&pages=181-204&pmid=23663408&doi=10.1017/S0140525X12000477&

Cox RW. AFNI: software for analysis and visualization of functional magnetic resonance neuroimages. Computers and Biomedical Research. 1996;29:162–173. doi: 10.1006/cbmr.1996.0014. [

https://doi.org/10.1006/cbmr.1996.0014

https://pubmed.ncbi.nlm.nih.gov/8812068/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Computers%20and%20Biomedical%20Research&title=AFNI:%20software%20for%20analysis%20and%20visualization%20of%20functional%20magnetic%20resonance%20neuroimages&author=RW%20Cox&volume=29&publication\_year=1996&pages=162-173&pmid=8812068&doi=10.1006/cbmr.1996.0014&

Dayan P. Improving generalization for temporal difference learning: the successor representation. Neural Computation. 1993;5:613–624. doi: 10.1162/neco.1993.5.4.613. [

https://doi.org/10.1162/neco.1993.5.4.613

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Neural%20Computation&title=Improving%20generalization%20for%20temporal%20difference%20learning:%20the%20successor%20representation&author=P%20Dayan&volume=5&publication\_year=1993&pages=613-624&doi=10.1162/neco.1993.5.4.613&

de Lange FP, Heilbron M, Kok P. How do expectations shape perception? Trends in Cognitive Sciences. 2018;22:764–779. doi: 10.1016/j.tics.2018.06.002. [

https://doi.org/10.1016/j.tics.2018.06.002

https://pubmed.ncbi.nlm.nih.gov/30122170/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Trends%20in%20Cognitive%20Sciences&title=How%20do%20expectations%20shape%20perception?&author=FP%20de%20Lange&author=M%20Heilbron&author=P%20Kok&volume=22&publication\_year=2018&pages=764-779&pmid=30122170&doi=10.1016/j.tics.2018.06.002&

den Ouden HE, Daunizeau J, Roiser J, Friston KJ, Stephan KE. Striatal prediction error modulates cortical coupling. Journal of Neuroscience. 2010;30:3210–3219. doi: 10.1523/JNEUROSCI.4458-09.2010. [

https://doi.org/10.1523/JNEUROSCI.4458-09.2010

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC3044875/

https://pubmed.ncbi.nlm.nih.gov/20203180/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Journal%20of%20Neuroscience&title=Striatal%20prediction%20error%20modulates%20cortical%20coupling&author=HE%20den%20Ouden&author=J%20Daunizeau&author=J%20Roiser&author=KJ%20Friston&author=KE%20Stephan&volume=30&publication\_year=2010&pages=3210-3219&pmid=20203180&doi=10.1523/JNEUROSCI.4458-09.2010&

Ekman M, Kok P, de Lange FP. Time-compressed preplay of anticipated events in human primary visual cortex. Nature Communications. 2017;8:15276. doi: 10.1038/ncomms15276. [

https://doi.org/10.1038/ncomms15276

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC5457495/

https://pubmed.ncbi.nlm.nih.gov/28534870/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Nature%20Communications&title=Time-compressed%20preplay%20of%20anticipated%20events%20in%20human%20primary%20visual%20cortex&author=M%20Ekman&author=P%20Kok&author=FP%20de%20Lange&volume=8&publication\_year=2017&pages=15276&pmid=28534870&doi=10.1038/ncomms15276&

Elliott Wimmer G, Büchel C. Learning of distant state predictions by the orbitofrontal cortex in humans. Nature Communications. 2019;10:2554. doi: 10.1038/s41467-019-10597-z. [

https://doi.org/10.1038/s41467-019-10597-z

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC6560030/

https://pubmed.ncbi.nlm.nih.gov/31186425/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Nature%20Communications&title=Learning%20of%20distant%20state%20predictions%20by%20the%20orbitofrontal%20cortex%20in%20humans&author=G%20Elliott%20Wimmer&author=C%20B%C3%BCchel&volume=10&publication\_year=2019&pages=2554&pmid=31186425&doi=10.1038/s41467-019-10597-z&

Finnie PSB, Komorowski RW, Bear MF. The spatiotemporal organization of experience dictates hippocampal involvement in primary visual cortical plasticity. bioRxiv. 2021 doi: 10.1101/2021.03.01.433430. [

https://doi.org/10.1101/2021.03.01.433430

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC8524775/

https://pubmed.ncbi.nlm.nih.gov/34314678/

Friston K. A theory of cortical responses. Philosophical Transactions of the Royal Society B: Biological Sciences. 2005;360:815–836. doi: 10.1098/rstb.2005.1622. [

https://doi.org/10.1098/rstb.2005.1622

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC1569488/

https://pubmed.ncbi.nlm.nih.gov/15937014/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Philosophical%20Transactions%20of%20the%20Royal%20Society%20B:%20Biological%20Sciences&title=A%20theory%20of%20cortical%20responses&author=K%20Friston&volume=360&publication\_year=2005&pages=815-836&pmid=15937014&doi=10.1098/rstb.2005.1622&

Gavornik JP, Bear MF. Learned spatiotemporal sequence recognition and prediction in primary visual cortex. Nature Neuroscience. 2014;17:732–737. doi: 10.1038/nn.3683. [

https://doi.org/10.1038/nn.3683

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC4167369/

https://pubmed.ncbi.nlm.nih.gov/24657967/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Nature%20Neuroscience&title=Learned%20spatiotemporal%20sequence%20recognition%20and%20prediction%20in%20primary%20visual%20cortex&author=JP%20Gavornik&author=MF%20Bear&volume=17&publication\_year=2014&pages=732-737&pmid=24657967&doi=10.1038/nn.3683&

Hasson U, Chen J, Honey CJ. Hierarchical process memory: memory as an integral component of information processing. Trends in Cognitive Sciences. 2015;19:304–313. doi: 10.1016/j.tics.2015.04.006. [

https://doi.org/10.1016/j.tics.2015.04.006

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC4457571/

https://pubmed.ncbi.nlm.nih.gov/25980649/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Trends%20in%20Cognitive%20Sciences&title=Hierarchical%20process%20memory:%20memory%20as%20an%20integral%20component%20of%20information%20processing&author=U%20Hasson&author=J%20Chen&author=CJ%20Honey&volume=19&publication\_year=2015&pages=304-313&pmid=25980649&doi=10.1016/j.tics.2015.04.006&

Hindy NC, Ng FY, Turk-Browne NB. Linking pattern completion in the Hippocampus to predictive coding in visual cortex. Nature Neuroscience. 2016;19:665–667. doi: 10.1038/nn.4284. [

https://doi.org/10.1038/nn.4284

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC4948994/

https://pubmed.ncbi.nlm.nih.gov/27065363/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Nature%20Neuroscience&title=Linking%20pattern%20completion%20in%20the%20Hippocampus%20to%20predictive%20coding%20in%20visual%20cortex&author=NC%20Hindy&author=FY%20Ng&author=NB%20Turk-Browne&volume=19&publication\_year=2016&pages=665-667&pmid=27065363&doi=10.1038/nn.4284&

Honey CJ, Thesen T, Donner TH, Silbert LJ, Carlson CE, Devinsky O, Doyle WK, Rubin N, Heeger DJ, Hasson U. Slow cortical dynamics and the accumulation of information over long timescales. Neuron. 2012;76:423–434. doi: 10.1016/j.neuron.2012.08.011. [

https://doi.org/10.1016/j.neuron.2012.08.011

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC3517908/

https://pubmed.ncbi.nlm.nih.gov/23083743/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Neuron&title=Slow%20cortical%20dynamics%20and%20the%20accumulation%20of%20information%20over%20long%20timescales&author=CJ%20Honey&author=T%20Thesen&author=TH%20Donner&author=LJ%20Silbert&author=CE%20Carlson&volume=76&publication\_year=2012&pages=423-434&pmid=23083743&doi=10.1016/j.neuron.2012.08.011&

Kandylaki KD, Nagels A, Tune S, Kircher T, Wiese R, Schlesewsky M, Bornkessel-Schlesewsky I. Predicting "When" in Discourse Engages the Human Dorsal Auditory Stream: An fMRI Study Using Naturalistic Stories. Journal of Neuroscience. 2016;36:12180–12191. doi: 10.1523/JNEUROSCI.4100-15.2016. [

https://doi.org/10.1523/JNEUROSCI.4100-15.2016

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC5148219/

https://pubmed.ncbi.nlm.nih.gov/27903727/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Journal%20of%20Neuroscience&title=Predicting%20%22When%22%20in%20Discourse%20Engages%20the%20Human%20Dorsal%20Auditory%20Stream:%20An%20fMRI%20Study%20Using%20Naturalistic%20Stories&author=KD%20Kandylaki&author=A%20Nagels&author=S%20Tune&author=T%20Kircher&author=R%20Wiese&volume=36&publication\_year=2016&pages=12180-12191&pmid=27903727&doi=10.1523/JNEUROSCI.4100-15.2016&

Kiebel SJ, Daunizeau J, Friston KJ. A hierarchy of time-scales and the brain. PLOS Computational Biology. 2008;4:e1000209. doi: 10.1371/journal.pcbi.1000209. [

https://doi.org/10.1371/journal.pcbi.1000209

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC2568860/

https://pubmed.ncbi.nlm.nih.gov/19008936/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=PLOS%20Computational%20Biology&title=A%20hierarchy%20of%20time-scales%20and%20the%20brain&author=SJ%20Kiebel&author=J%20Daunizeau&author=KJ%20Friston&volume=4&publication\_year=2008&pages=e1000209&pmid=19008936&doi=10.1371/journal.pcbi.1000209&

Kok P, Jehee JF, de Lange FP. Less is more: expectation sharpens representations in the primary visual cortex. Neuron. 2012;75:265–270. doi: 10.1016/j.neuron.2012.04.034. [

https://doi.org/10.1016/j.neuron.2012.04.034

https://pubmed.ncbi.nlm.nih.gov/22841311/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Neuron&title=Less%20is%20more:%20expectation%20sharpens%20representations%20in%20the%20primary%20visual%20cortex&author=P%20Kok&author=JF%20Jehee&author=FP%20de%20Lange&volume=75&publication\_year=2012&pages=265-270&pmid=22841311&doi=10.1016/j.neuron.2012.04.034&

Kok P, Failing MF, de Lange FP. Prior expectations evoke stimulus templates in the primary visual cortex. Journal of Cognitive Neuroscience. 2014;26:1546–1554. doi: 10.1162/jocn\_a\_00562. [

https://doi.org/10.1162/jocn\_a\_00562

https://pubmed.ncbi.nlm.nih.gov/24392894/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Journal%20of%20Cognitive%20Neuroscience&title=Prior%20expectations%20evoke%20stimulus%20templates%20in%20the%20primary%20visual%20cortex&author=P%20Kok&author=MF%20Failing&author=FP%20de%20Lange&volume=26&publication\_year=2014&pages=1546-1554&pmid=24392894&doi=10.1162/jocn\_a\_00562&

Kok P, Turk-Browne NB. Associative prediction of visual shape in the Hippocampus. The Journal of Neuroscience. 2018;38:6888–6899. doi: 10.1523/JNEUROSCI.0163-18.2018. [

https://doi.org/10.1523/JNEUROSCI.0163-18.2018

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC6070666/

https://pubmed.ncbi.nlm.nih.gov/29986875/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=The%20Journal%20of%20Neuroscience&title=Associative%20prediction%20of%20visual%20shape%20in%20the%20Hippocampus&author=P%20Kok&author=NB%20Turk-Browne&volume=38&publication\_year=2018&pages=6888-6899&pmid=29986875&doi=10.1523/JNEUROSCI.0163-18.2018&

Kurby CA, Zacks JM. Segmentation in the perception and memory of events. Trends in Cognitive Sciences. 2008;12:72–79. doi: 10.1016/j.tics.2007.11.004. [

https://doi.org/10.1016/j.tics.2007.11.004

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC2263140/

https://pubmed.ncbi.nlm.nih.gov/18178125/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Trends%20in%20Cognitive%20Sciences&title=Segmentation%20in%20the%20perception%20and%20memory%20of%20events&author=CA%20Kurby&author=JM%20Zacks&volume=12&publication\_year=2008&pages=72-79&pmid=18178125&doi=10.1016/j.tics.2007.11.004&

Lerner Y, Honey CJ, Silbert LJ, Hasson U. Topographic mapping of a hierarchy of temporal receptive windows using a narrated story. Journal of Neuroscience. 2011;31:2906–2915. doi: 10.1523/JNEUROSCI.3684-10.2011. [

https://doi.org/10.1523/JNEUROSCI.3684-10.2011

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC3089381/

https://pubmed.ncbi.nlm.nih.gov/21414912/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Journal%20of%20Neuroscience&title=Topographic%20mapping%20of%20a%20hierarchy%20of%20temporal%20receptive%20windows%20using%20a%20narrated%20story&author=Y%20Lerner&author=CJ%20Honey&author=LJ%20Silbert&author=U%20Hasson&volume=31&publication\_year=2011&pages=2906-2915&pmid=21414912&doi=10.1523/JNEUROSCI.3684-10.2011&

Lerner Y, Honey CJ, Katkov M, Hasson U. Temporal scaling of neural responses to compressed and dilated natural speech. Journal of Neurophysiology. 2014;111:2433–2444. doi: 10.1152/jn.00497.2013. [

https://doi.org/10.1152/jn.00497.2013

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC4044438/

https://pubmed.ncbi.nlm.nih.gov/24647432/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Journal%20of%20Neurophysiology&title=Temporal%20scaling%20of%20neural%20responses%20to%20compressed%20and%20dilated%20natural%20speech&author=Y%20Lerner&author=CJ%20Honey&author=M%20Katkov&author=U%20Hasson&volume=111&publication\_year=2014&pages=2433-2444&pmid=24647432&doi=10.1152/jn.00497.2013&

Liu X, Hairston J, Schrier M, Fan J. Common and distinct networks underlying reward Valence and processing stages: a meta-analysis of functional neuroimaging studies. Neuroscience & Biobehavioral Reviews. 2011;35:1219–1236. doi: 10.1016/j.neubiorev.2010.12.012. [

https://doi.org/10.1016/j.neubiorev.2010.12.012

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC3395003/

https://pubmed.ncbi.nlm.nih.gov/21185861/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Neuroscience%20&%20Biobehavioral%20Reviews&title=Common%20and%20distinct%20networks%20underlying%20reward%20Valence%20and%20processing%20stages:%20a%20meta-analysis%20of%20functional%20neuroimaging%20studies&author=X%20Liu&author=J%20Hairston&author=M%20Schrier&author=J%20Fan&volume=35&publication\_year=2011&pages=1219-1236&pmid=21185861&doi=10.1016/j.neubiorev.2010.12.012&

Michelmann S, Staresina BP, Bowman H, Hanslmayr S. Speed of time-compressed forward replay flexibly changes in human episodic memory. Nature Human Behaviour. 2019;3:143–154. doi: 10.1038/s41562-018-0491-4. [

https://doi.org/10.1038/s41562-018-0491-4

https://pubmed.ncbi.nlm.nih.gov/30944439/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Nature%20Human%20Behaviour&title=Speed%20of%20time-compressed%20forward%20replay%20flexibly%20changes%20in%20human%20episodic%20memory&author=S%20Michelmann&author=BP%20Staresina&author=H%20Bowman&author=S%20Hanslmayr&volume=3&publication\_year=2019&pages=143-154&pmid=30944439&doi=10.1038/s41562-018-0491-4&

Michelmann S, Price AR, Aubrey B, Doyle WK, Friedman D, Dugan PC, Norman KA. Moment-by-moment tracking of naturalistic learning and its underlying hippocampo-cortical interactions. bioRxiv. 2020 doi: 10.1101/2020.12.09.416438. [

https://doi.org/10.1101/2020.12.09.416438

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC8438040/

https://pubmed.ncbi.nlm.nih.gov/34518520/

Momennejad I, Howard MW. Predicting the future with multi-scale successor representations. bioRxiv. 2018 doi: 10.1101/449470. [

https://doi.org/10.1101/449470

Richardson H, Saxe R. Development of predictive responses in theory of mind brain regions. Developmental Science. 2020;23:e12863. doi: 10.1111/desc.12863. [

https://doi.org/10.1111/desc.12863

https://pubmed.ncbi.nlm.nih.gov/31125472/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Developmental%20Science&title=Development%20of%20predictive%20responses%20in%20theory%20of%20mind%20brain%20regions&author=H%20Richardson&author=R%20Saxe&volume=23&publication\_year=2020&pages=e12863&pmid=31125472&doi=10.1111/desc.12863&

Singer T, Critchley HD, Preuschoff K. A common role of insula in feelings, empathy and uncertainty. Trends in Cognitive Sciences. 2009;13:334–340. doi: 10.1016/j.tics.2009.05.001. [

https://doi.org/10.1016/j.tics.2009.05.001

https://pubmed.ncbi.nlm.nih.gov/19643659/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Trends%20in%20Cognitive%20Sciences&title=A%20common%20role%20of%20insula%20in%20feelings,%20empathy%20and%20uncertainty&author=T%20Singer&author=HD%20Critchley&author=K%20Preuschoff&volume=13&publication\_year=2009&pages=334-340&pmid=19643659&doi=10.1016/j.tics.2009.05.001&

Summerfield C, Egner T. Expectation (and attention) in visual cognition. Trends in Cognitive Sciences. 2009;13:403–409. doi: 10.1016/j.tics.2009.06.003. [

https://doi.org/10.1016/j.tics.2009.06.003

https://pubmed.ncbi.nlm.nih.gov/19716752/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Trends%20in%20Cognitive%20Sciences&title=Expectation%20(and%20attention)%20in%20visual%20cognition&author=C%20Summerfield&author=T%20Egner&volume=13&publication\_year=2009&pages=403-409&pmid=19716752&doi=10.1016/j.tics.2009.06.003&

Uddén J, Bahlmann J. A rostro-caudal gradient of structured sequence processing in the left inferior frontal gyrus. Philosophical Transactions of the Royal Society B: Biological Sciences. 2012;367:2023–2032. doi: 10.1098/rstb.2012.0009. [

https://doi.org/10.1098/rstb.2012.0009

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC3367683/

https://pubmed.ncbi.nlm.nih.gov/22688637/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Philosophical%20Transactions%20of%20the%20Royal%20Society%20B:%20Biological%20Sciences&title=A%20rostro-caudal%20gradient%20of%20structured%20sequence%20processing%20in%20the%20left%20inferior%20frontal%20gyrus&author=J%20Udd%C3%A9n&author=J%20Bahlmann&volume=367&publication\_year=2012&pages=2023-2032&pmid=22688637&doi=10.1098/rstb.2012.0009&

Wimmer GE, Liu Y, Vehar N, Behrens TEJ, Dolan RJ. Episodic memory retrieval success is associated with rapid replay of episode content. Nature Neuroscience. 2020;23:1025–1033. doi: 10.1038/s41593-020-0649-z. [

https://doi.org/10.1038/s41593-020-0649-z

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC7610376/

https://pubmed.ncbi.nlm.nih.gov/32514135/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Nature%20Neuroscience&title=Episodic%20memory%20retrieval%20success%20is%20associated%20with%20rapid%20replay%20of%20episode%20content&author=GE%20Wimmer&author=Y%20Liu&author=N%20Vehar&author=TEJ%20Behrens&author=RJ%20Dolan&volume=23&publication\_year=2020&pages=1025-1033&pmid=32514135&doi=10.1038/s41593-020-0649-z&

Wittkuhn L, Schuck NW. Dynamics of fMRI patterns reflect sub-second activation sequences and reveal replay in human visual cortex. Nature Communications. 2021;12:1795. doi: 10.1038/s41467-021-21970-2. [

https://doi.org/10.1038/s41467-021-21970-2

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC7979874/

https://pubmed.ncbi.nlm.nih.gov/33741933/

Google Scholar

https://scholar.google.com/scholar\_lookup?journal=Nature%20Communications&title=Dynamics%20of%20fMRI%20patterns%20reflect%20sub-second%20activation%20sequences%20and%20reveal%20replay%20in%20human%20visual%20cortex&author=L%20Wittkuhn&author=NW%20Schuck&volume=12&publication\_year=2021&pages=1795&pmid=33741933&doi=10.1038/s41467-021-21970-2&

eLife. doi:

10.7554/eLife.64972.sa1

https://doi.org/10.7554/eLife.64972.sa1

Decision letter

Editor: Marius V Peelen

Reviewed by: Linda Geerligs

Radboud University, Netherlands

Radboud University, Netherlands

Marius V Peelen

: Reviewing Editor

Linda Geerligs

: Reviewer

PMC Copyright notice

https://pmc.ncbi.nlm.nih.gov/about/copyright/

Our editorial process produces two outputs: i)

public reviews

https://sciety.org/articles/activity/10.1101/2020.10.14.338145

designed to be posted alongside

the preprint

https://www.biorxiv.org/content/10.1101/2020.10.14.338145v3

for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This study uses innovative fMRI analysis methods to show how the brain predicts the future. It provides compelling evidence for anticipatory neural activity during repeated viewing of a movie clip, finding that different brain regions anticipate events to different degrees, mirroring the temporal integration windows of these brain regions.

Decision letter after peer review:

Thank you for submitting your article "Anticipation of temporally structured events in the brain" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Linda Geerligs (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

Provide more statistical support for differences between brain regions and the anterior-posterior hierarchy

Analyze repeated viewings separately, also to account for differences in reliability

Reconsider the event correlation analysis (see several specific suggestions below)

Consider optimizing analyses to reduce noise (and false negatives)

Reviewer #1 (Recommendations for the authors (required)):

– Were the correlations in Figure 6 corrected for multiple comparisons?

– The introduction mentions that "The majority of studies examining anticipatory signals, however, have tested only one-step associations". Arguably, the current results might also reveal one-step associations, but with the step duration being longer in some regions than others (in line with previous findings of different temporal integration windows). Please discuss this possibility or clarify what you mean with one-step associations.

– The results are based on one 90-s movie segment with 7 events, mostly involving humans. To what extent may results be specific to this short segment and these specific events (e.g., anticipation of theory of mind or emotions)?

– To get a sense of the false-positive rate, it would be informative to see the same map (Figure 2) but testing for the opposite temporal direction, as Supplementary file.

– As Supp Figure 2, please also show unthresholded maps (cf Figure 3 of Baldassano, 2017) plotting both positive and negative anticipation. This would give a fuller insight into the data, also in regions that didn't cross the threshold.

– In the table in Figure 6, one correlation of 0.52 is not indicated as significant (cluster 7). Similarly, the difference (0.29) is also not indicated as significant. Is this correct?

Reviewer #2 (Recommendations for the authors (required)):

Below I will mention concrete suggestions for improvement related to the points in the public recommendation.

I would suggest repeating all analyses using the estimated real/optimal number of events in each brain region, rather than the number that was based on behavioural annotations.

Repeating the analyses with hyper-aligned data should reduce the amount of noise in the group-averaged data.

Using only viewing 6 as the repeated viewing condition may improve the detection of anticipatory signals in early sensory areas. Looking at how the amount of anticipation changes across all viewings would add an interesting new dimension to the results presented in the paper.

An alternative approach to this analysis is to vary the HRF delay for the annotated events and investigate which delay shows the optimal correlation. This approach would provide additional evidence for the estimated amount of anticipation shown in figure 2.

Rather than grouping voxels based on the identified cluster, I would suggest either sticking to the original searchlight definitions or grouping searchlights based on the similarity of their event boundaries.

A discussion about this issue may be a valuable addition to the Discussion section.

Reviewer #3 (Recommendations for the authors (required)):

The discussion is relatively quite long.

It seems like the brain maps in Figure 6 should be added to Figure 2, or their own figure, before the annotation correlation-related results in Figure 5 and the table in Figure 6. As presented, it is confusing and not initially clear why there are clusters with no significant correlation results – that the annotation analysis presented is independent from the analysis that identified the clusters.

In Figure 5, the temporal language is unclear. 'Backward' and 'forward' here are confusing descriptors, e.g. backward can be behind the current position (earlier in time) or pushed 'back' later in time. On a different note about this figure, it should have brain labels in the text of the correlation plots, the same cluster numbering added as in Figure 6, and panel letters.

The original report in Aly et al., (2018) notes that no participants had previously viewed the movie that the clips were taken from. I may have missed it, but it would be helpful to repeat that information here.

eLife. 2021 Apr 22;10:e64972. doi:

10.7554/eLife.64972.sa2

https://doi.org/10.7554/eLife.64972.sa2

Author response

Collection date 2021.

PMC Copyright notice

https://doi.org/10.7554/eLife.64972.sa2

Essential Revisions:

Provide more statistical support for differences between brain regions and the anterior-posterior hierarchy

Thank you for raising this important concern. We briefly outline our major changes here, and describe our changes in more detail below in response to individual reviewer comments. First, we related anticipation amounts to the position of brain regions along the anterior/posterior axis, and indeed found that anticipation amounts progressively increase from posterior to anterior parts of the brain (Spearman’s rho = 0.58, p = 0.0030). Second, this systematicity exists even when the analysis was done on an unthresholded statistical map (Spearman’s rho = 0.42, p = 0.0028; Figure 2—figure supplement 1). Finally, we explored whether brain regions with faster vs slower activity dynamics (i.e., more vs fewer events during the initial viewing of the movie) showed differences in anticipation amounts. We found that regions that integrate information over more of the past (i.e., show fewer, longer events) show more anticipation (Spearman’s rho = 0.319, p = 0.00031; Figure 2 – Figure supplement 3). This is consistent with our hypothesis that the

retrospective

temporal hierarchy observed in prior studies (Hasson et al., 2008; Hasson et al., 2015; Lerner et al., 2011) is directly related to the anticipatory hierarchy that we describe here.

Analyze repeated viewings separately, also to account for differences in reliability

We implemented the changes recommended by the viewers. First, we entered each viewing separately into the HMM analyses and then averaged the amount of anticipation across repetitions 2-6 (rather than averaging the timecourses of the repetitions before entering them into the HMM). This is now our main analysis, and each viewing is now shown as a separate line in our example time by event plots (Figure 2B). We also compared the first viewing to the last (6th) viewing alone, which yielded a similar result (Figure 2—figure supplement 2). Finally, when relating the brain’s event representations to human-annotated events (Figure 5), we examine the brain data for each viewing separately and present the data for all six movie presentations. Our main conclusions remain unchanged when taking these approaches.

Reconsider the event correlation analysis (see several specific suggestions below)

We agree that the most important test for this analysis is whether there is a systematic shift, across movie repetitions, in the timing of the peak cross-correlation between the brain’s event transitions and human-annotated event boundaries. To test this, we conducted a new analysis in which we measured the timing of the peak cross-correlation between HMM-derived event transitions in the brain and the human-annotated event boundaries, separately for each of the six movie viewings. In other words, we found the amount of shift in the brain’s event transitions that led to the maximum correlation with the timing of the human-annotated event boundaries. We then compared the timing of the correlation peak for the first movie viewing to the timing of the mean peak across viewings 2-6, and found regions of the brain where the peak shifted to be earlier with subsequent movie viewings. This was done as a whole-brain analysis with FDR correction. We include a figure (Figure 5) showing the data for the three searchlights that corresponded to clusters that met the q <.05 FDR criterion.

The preceding analysis looked for regions for which the timing of the peak cross-correlation between the brain’s events and human-annotated events shifted earlier over movie repetitions, but did not test for the absolute location of that peak correlation (relative to zero lag between the HMM events and annotated events). Do the brain’s event transitions occur before annotated event transitions, after, or are they aligned? And how does this change over movie repetitions? We examined this question in the three clusters that emerged from the analysis in the preceding paragraph. We found that for the initial viewing, the brain’s event transitions lagged behind human-annotated event boundaries for two of the three clusters, whereas for the last cluster, the brain’s transitions and subjective event boundaries were aligned. For repeated viewings, the timing of the peak correlations shifted such that the brain’s representations of an event transition reliably preceded the occurrence of the human-annotated event boundary, for all three clusters (Figure 5).

Together, these results confirm that, in some regions, the best alignment between the brain’s event transitions and human-annotated event boundaries shifts over movie repetitions such that the brain’s event transitions start to occur earlier over repetitions. In particular, the brain’s events shift to precede subjective event boundaries.

Consider optimizing analyses to reduce noise (and false negatives)

We implemented many changes to this end, which we will briefly describe here and describe in more detail in response to individual reviewer comments. First, we hyperaligned the brain data of individual participants before conducting our anticipation analyses, using the "Shared Response Model" (SRM) hyperalignment approach (Chen et al., 2015). Hyperalignment projects features (e.g., voxels) from individual brains into a common high-dimensional space, in which features across individuals share functional properties as opposed to anatomical locations. This approach increases the sensitivity of analyses, such as our HMM approach, that depend on across-brain similarities because traditional anatomical alignment approaches do not accommodate idiosyncrasies in fine-grained functional topographies across individuals. This approach uncovered anticipation in more widespread regions compared to our initial (anatomically aligned) analyses. The hyperaligned analyses now replace our prior analyses. Second, due to reviewer concerns about whether we were properly controlling the rate of false positives in our maps, we replaced our bootstrapping-based approach with a permutation-based approach. Rather than resampling participants to produce confidence intervals on our results, we permuted the order of the viewings to generate null maps and then computed p values by comparing our results to these null results. This approach yielded similar p values to our original bootstrapping approach, verifying that we are appropriately controlling our false positive rate. We then applied a False Discovery Rate (FDR) correction as before, to account for multiple comparisons across voxels. Third, we now share and analyze unthresholded maps of anticipation in the brain. As noted above, the anticipation hierarchy persists even when the analysis is conducted on an anticipation map that was not corrected for statistical significance.

Reviewer #1 (Recommendations for the authors (required)):

– Were the correlations in Figure 6 corrected for multiple comparisons?

In our initial manuscript, those correlations were not corrected for multiple comparisons. In our revision, we have replaced our initial analysis examining the relationship between the brain’s event transitions and human-annotated event boundaries with a new analysis. This new analyses tests for shifts in the relationship between brain and human-annotated event boundaries over movie viewings in a searchlight across the whole cortex (as described in Essential Revision # 3; see Figure 5). This new analysis is FDR-corrected at q < 0.05.

– The introduction mentions that "The majority of studies examining anticipatory signals, however, have tested only one-step associations". Arguably, the current results might also reveal one-step associations, but with the step duration being longer in some regions than others (in line with previous findings of different temporal integration windows). Please discuss this possibility or clarify what you mean with one-step associations.

Thank you for raising this issue. We have clarified our language, to state that most studies have used discrete items as stimuli and looked for anticipation of the single item that was coming up next:

“The majority of studies examining anticipatory signals, however, have tested anticipation based on memory for relatively simple associations between pairs of discrete stimuli, such as auditory tones , lines, dots, oriented gratings, or abstract objects (e.g., Alink, Schwiedrzik, Kohler, Singer, and Muckli, 2010; Gavornik and Bear, 2014; Hindy, Ng, and Turk-Browne, 2016; Kok, Jehee, and de Lange, 2012; Kok, Failing, and de Lange, 2014; Kok and Turk-Browne, 2018). These studies have found anticipatory signals about a single upcoming stimulus in a variety of brain regions, from perceptual regions (Kok et al., 2012, 2014) to the medial temporal lobe (Hindy et al., 2016; Kok and Turk-Browne, 2018).” (p.2)

– The results are based on one 90-s movie segment with 7 events, mostly involving humans. To what extent may results be specific to this short segment and these specific events (e.g., anticipation of theory of mind or emotions)?

Thank you for raising this point, which we agree is important. We now mention this limitation in the Discussion:

“One limitation of the current work is the reliance on one movie clip. Movie clips of different durations might yield different results. For example, it is an open question whether the duration of anticipation scales with the length of the movie or if the amount of anticipation is fixed (c.f., Lerner, Honey, Katkov, and Hasson, 2014). Furthermore, the content of the movie and how frequently event boundaries occur may change anticipation amounts. That said, anticipatory signals in naturalistic stimuli have been observed across multiple studies that use different movies and auditorily presented stories (e.g., Baldassano et al., 2017; Michelmann et al., 2020; also see Michelmann et al., 2019; Wimmer and Büchel, 2019; Wimmer et al., 2020). Thus, it is likely that anticipatory hierarchies will also replicate across different stimuli. There may nevertheless be important differences across stimuli. For example, the specific regions that are involved in anticipation may vary depending on what the most salient features of a movie or narrative are (e.g., particular emotional states, actions, conversations, or perceptual information).” (p.10)

– To get a sense of the false-positive rate, it would be informative to see the same map (Figure 2) but testing for the opposite temporal direction, as Supplementary file.

We agree that it is important to get a sense of the false-positive rate. We considered this proposed approach, but we are not sure if the opposite temporal direction provides a measure of the false positive rate. Instead, the opposite temporal direction — on repeated viewings, brain areas lag behind initial viewing — could be an interesting phenomenon in its own right. That could reflect, for example, holding on to the past for longer amounts of time in order to better integrate information with what is coming up next.

We therefore opted to use permutation tests to get a more direct measure of the false positive rate. For these permutation tests, we randomly shuffled movie viewings within each participant before conducting the anticipation analysis. This random shuffling was done 99 items, allowing us to obtain a null distribution of anticipation for each searchlight. This null distribution was used to calculate a p-value for each searchlight by computing the z-score of our result relative to the null distribution and then obtaining a p-value from a Normal survival function. The p-value map was then FDR-corrected with q < 0.05.

Although we did not statistically test for temporal shifts in the opposite direction (with activity shifting later on repeated viewings), the unthresholded map of positive and negative anticipation can be viewed at https://identifiers.org/neurovault.collection:9584, and shows very few regions with negative values of anticipation.

– As Supp Figure 2, please also show unthresholded maps (cf Figure 3 of Baldassano, 2017) plotting both positive and negative anticipation. This would give a fuller insight into the data, also in regions that didn't cross the threshold.

We agree this is useful, and have included the unthresholded map as Figure 2—figure supplement 1. As noted earlier, the posterior-to-anterior hierarchy of anticipation is also present in this unthresholded map.

– In the table in Figure 6, one correlation of 0.52 is not indicated as significant (cluster 7). Similarly, the difference (0.29) is also not indicated as significant. Is this correct?

That was actually correct; that value failed to reach statistical significance because of very high variance. That said, that analysis (and table) has since been replaced (see Essential Revision #3).

Reviewer #2 (Recommendations for the authors (required)):

Below I will mention concrete suggestions for improvement related to the points in the public recommendation.

I would suggest repeating all analyses using the estimated real/optimal number of events in each brain region, rather than the number that was based on behavioural annotations.

Please see our response under point #2 in the public recommendation of this reviewer. Briefly, we found that the optimal number of events (defined on the first viewing) did differ across the cortex in a way that was correlated with the degree of anticipation. We chose to use a fixed number of events in the anticipation analyses in the manuscript to avoid a potential confound between the number of events used in the HMM and the degree of anticipation detected.

That said, we nevertheless ran this proposed analysis, in which the number of events used in the anticipation analysis was set to the optimal value based on the first viewing in each region, and obtained the following result (thresholded at q<0.05):

Although noisier than our main analysis, this result does replicate the general posterior-to-anterior topography of anticipation. Again, we chose not to include this in the manuscript due to our concerns that this analysis could produce an artificial relationship between event timescales during initial viewing and degree of anticipation. We hope that our compromise — relating optimal event numbers to anticipation amounts in our main analysis — is a satisfactory approach given the difficulties in interpreting this proposed analysis.

Repeating the analyses with hyper-aligned data should reduce the amount of noise in the group-averaged data.

This useful suggestion has been implemented. All the analyses were repeated after hyper-alignment. The same pattern of results emerged, but anticipatory signals are now generally more widespread and robust.

Using only viewing 6 as the repeated viewing condition may improve the detection of anticipatory signals in early sensory areas. Looking at how the amount of anticipation changes across all viewings would add an interesting new dimension to the results presented in the paper.

Thank you for these recommendations. We now statistically compare the first viewing to the last viewing and show those results as Figure 2—figure supplement 2. These data exhibit the same overall pattern as the first viewing compared to all subsequent viewings. We also plot data for each viewing separately in the event by time plots in Figure 2. Finally, we show the relationship between the brain’s event boundaries and human-annotated event boundaries for each viewing separately in Figure 5. Visual inspection of the latter two figures shows that anticipation generally increases with subsequent movie viewings.

An alternative approach to this analysis is to vary the HRF delay for the annotated events and investigate which delay shows the optimal correlation. This approach would provide additional evidence for the estimated amount of anticipation shown in figure 2.

Thank you for this suggestion. If we are interpreting it correctly, this is functionally equivalent to what we did. In particular, a reduced HRF delay ( i.e., an HRF that is shifted earlier in time) is analogous to shifting the convolved timecourse earlier in time. Likewise, an increased HRF delay (i.e., an HRF that is shifted later in time) is analogous to shifting the convolved timecourse later in time. However, please let us know if we misinterpreted your comment and should consider a different alternative. For example, if the suggestion is to change the delay between the HRF onset and its peak, that would indeed yield different results. However, such an analysis would have to be done carefully so that it remains biologically plausible.

Rather than grouping voxels based on the identified cluster, I would suggest either sticking to the original searchlight definitions or grouping searchlights based on the similarity of their event boundaries.

All analyses are now conducted with the same whole-brain searchlight approach, without any post-hoc grouping or clustering.

A discussion about this issue may be a valuable addition to the Discussion section.

We have clarified that the HMM produces a probability distribution across states (events) at each time-point, i.e., an activity pattern at any given time-point can reflect a mixture of current and upcoming events.

This is clarified in the caption to Figure 1:

“By fitting a Hidden Markov Model (HMM) jointly to all viewings, we can identify this shared sequence of event patterns, as well as a probabilistic estimate of event transitions. Regions with anticipatory representations are those in which event transitions occur earlier in time for repeated viewings of a stimulus compared to the initial viewing , indicated by an upward shift on the plot of the expected value of the event at each timepoint.” (p.3)

And in the caption to Figure 2:

“Because the HMM produces a probability distribution across states at each timepoint, which can reflect a combination of current and upcoming event representations, we plot the expected value of the event assignments at each timepoint.” (p.5)

And also in the Methods:

“After fitting the HMM, we obtain an event by time-point matrix for each viewing , giving the probability that each timepoint belongs to each event. Note that, because this assignment of timepoints to events is probabilistic, it is possible for the HMM to detect that the pattern of voxel activity at a timepoint reflects a mixture of multiple event patterns, allowing us to track subtle changes in the timecourse of how the brain is transitioning between events.” (p.13)

Reviewer #3 (Recommendations for the authors (required)):

The discussion is relatively quite long.

We apologize for that! We tried to condense when possible, but it was unfortunately difficult given reviewer requests to relate our findings to other relevant work and clarify the implications of our results. We have now added subsection headings to better organize the Discussion.

It seems like the brain maps in Figure 6 should be added to Figure 2, or their own figure, before the annotation correlation-related results in Figure 5 and the table in Figure 6. As presented, it is confusing and not initially clear why there are clusters with no significant correlation results – that the annotation analysis presented is independent from the analysis that identified the clusters.

We agree that running the annotation correlation analysis on post-hoc clusters led to some confusion. In the revised version of the manuscript, the (new) annotation correlation analysis is conducted as a separate whole-brain searchlight analysis, and the significant clusters are shown in Figure 5.

In Figure 5, the temporal language is unclear. 'Backward' and 'forward' here are confusing descriptors, e.g. backward can be behind the current position (earlier in time) or pushed 'back' later in time. On a different note about this figure, it should have brain labels in the text of the correlation plots, the same cluster numbering added as in Figure 6, and panel letters.

Thank you for pointing this out. We changed that sentence to the following:

“Negative lags show the correlations when the human-annotated event timecourse is shifted earlier in time, and positive lags show the correlation when the human-annotated event timecourse is shifted later in time.” (p.7)

With respect to Figure 5, the old figure has been replaced with one depicting the analyses in which we look for significant

in the peak cross-correlation between the brain’s event boundaries and human-annotated event boundaries. The new figure has the clusters labeled clearly with their names, and we no longer use cluster numbers (see discussion with reviewer #1, with respect to functionally heterogeneous clusters).

The original report in Aly et al., (2018) notes that no participants had previously viewed the movie that the clips were taken from. I may have missed it, but it would be helpful to repeat that information here.

This is a good point, and we have added this clarification to the Methods:

“None of the participants reported previously seeing this movie.” (p.12)

Associated Data

This section collects any data citations, data availability statements, or supplementary materials included in this article.

Data Citations

Aly M, Chen J, Turk-Browne NB, Hasson U. 2019. Learning Naturalistic Temporal Structure in the Posterior Medial Network. OpenNeuro. [

https://doi.org/10.18112/openneuro.ds001545.v1.1.1

PMC free article

https://pmc.ncbi.nlm.nih.gov/articles/PMC6211568/

https://pubmed.ncbi.nlm.nih.gov/30004848/

Supplementary Materials

Transparent reporting form

elife-64972-transrepform.docx

https://pmc.ncbi.nlm.nih.gov/articles/instance/8169103/bin/elife-64972-transrepform.docx

(247.5KB, docx)

Data Availability Statement

We used a publicly-available dataset, from

https://openneuro.org/datasets/ds001545/versions/1.1.1

https://openneuro.org/datasets/ds001545/versions/1.1.1

The following previously published dataset was used:

Aly M, Chen J, Turk-Browne NB, Hasson U. 2019. Learning Naturalistic Temporal Structure in the Posterior Medial Network. OpenNeuro.

View on publisher site

https://openneuro.org/datasets/ds001545/versions/1.1.1

PDF (1.9 MB)

https://openneuro.org/datasets/ds001545/versions/1.1.1

Download .nbib .nbib

https://openneuro.org/datasets/ds001545/versions/1.1.1

Add to Collections

Unable to load your collection due to an error

Please try again

https://pmc.ncbi.nlm.nih.gov#