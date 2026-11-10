---
tags:
  - notebooklm-import
notebook: "C_Game Theory"
category: "research"
---

#### Psychological Game Theory

Pierpaolo Battigalli & Martin Dufwenberg
April 30, 2019
Abstract
The mathematical framework of psychological game theory is use-ful for describing many forms of motivation where preferences depend directly on own or others beliefs. It allows for incorporation of emo-tions, reciprocity, image concerns, and self-esteem in economic analy-sis. We explain how and why, discussing basic theory, a variety of sentiments, experiments, and applied work. Keywords: psychological game theory; belief-dependent motiva-
tion; reciprocity; emotions; image concerns; self-esteem JEL codes: C72; D91

##### 1 Introduction

Economists increasingly argue that a rich variety of human motivations shape outcomes in important ways. Consider the following categories:
emotions, including guilt, disappointment, regret, frustration, anger, anxiety, shame, and fear;
Battigalli: Bocconi University and IGIER, Italy; pierpaolo.battigalli@unibocconi.it. Dufwenberg: University of Arizona, USA; University of Gothenburg, Sweden; CESifo, Germany; martind@eller.arizona.edu. We have bene ted from many stimulating discus-sions (over the years) with our coauthors of the articles cited below. For their comments and advice on (versions of) this manuscript, we thank the Editor Steven Durlauf and several referees, as well as Lina Andersson, Francesco Fabbri, Amanda Friedenberg, Sen-ran Lin, Paola Moscariello, and Jin Sohn. Financial support of ERC (grant 324219) is gratefully acknowledged.
1
reciprocity, or the inclination to respond to kindness with kindness and to be unkind to whoever is unkind;
image concerns, e.g. when someone wants others to believe that he is smart, altruistic, or honest;
self-esteem, e.g. when someone wants to believe that he is competent or brave.
These sentiments di¤er greatly, yet have in common that preferences de-pend on endogenously determined beliefs about choices and about beliefs (as we ll show). We refer to this as belief-dependent utility. Standard economic models are ill-equipped to model it. However, psychological game theory (PGT), a framework pioneered by Geanakoplos, Pearce & Stacchetti (1989) (GP&S) and further developed by Battigalli & Dufwenberg (2009) (B&D) can.1 PGT provides a useful intellectual umbrella under which many trends in psychology and economics can be understood, related, and synthesized. The objects of analysis are called psychological games (p-games). Awareness of and interest in PGT is on the rise, yet incomplete. We
explain what PGT is and what motivations can be modeled, highlighting a variety of idiosyncratic features. We present old insights and speculate about new ones that PGT may hold promise to deliver. We discuss basic theory, experimental tests, and applied work. Although we cite a lot of papers, our primary goal is not to provide a comprehensive survey. Rather we try to highlight the structure and potential of various forms of work involving PGT. Our style is semi-formal, presenting some notions verbally rather than mathematically. Readers who wish to dig deeper should compare with relevant passages of GP&S, B&D, and other articles we reference. This includes the recent methodological article Battigalli, Corrao & Dufwenberg (2019) (BC&D) which contains some key innovations relative to B&D which are re ected also in our exposition here (more on that in Section 3). Our discussion of belief-dependent motivations mostly consists of showing
how to represent them with psychological utility functions and highlighting the ensuing best-reply behavior. Sometimes we analyze strategic reasoning either by iterated elimination of non-best replies, or informally applying an
1See also Gilboa & Schmeidler (1988) who in another pioneering contribution on infor-mation dependent games anticipated some of the themes that GP&S and others developed in more depth.
2
equilibrium concept. For a broader discussion of solution concepts see B&D and BC&D, as well as our brief critical remarks in the last part of Section 6. The sections below cover: a warm-up example suggestive of many relevant
broader themes (2); the formal framework including the explanation of what a p-game is (3); how to model di¤erent forms of psychological motivations, highlighting idiosyncratic features, and mentioning some applied work (4); experimental tests (5); additional comments (6); concluding remarks (7).

##### 2 A warm-up example

A large recent literature explores humans reluctance to lie or cheat using an experimental die-roll paradigm introduced by Fischbacher & Föllmi-Heusi (2013) (F&FH).2 Dufwenberg & Dufwenberg (2018) (D&D) propose a PGT-based account of behavior. We draw on their work for our opening example, which ts the third category of our introduction: image concerns. A subject is asked to roll a six-sided die in private and to report the
outcome, but the report is non-veri able and can be submitted with impunity. The subject is paid in proportion to the reported number, with one exception: reporting six yields a payout of zero. We will refer to a six as a zero. Formally, chance (player 0) draws $x$ 2 $f0; :::;$ 5g from a uniform distribution $(x$ = 0 corresponding to rolling a six). Player 1 observes $x$ and then chooses a report $y$ 2 $f0; :::;$ 5g after which he is paid $y.$ Choice $y,$ but not realization $x,$ is observed by player 2, who is an audience. In applications the audience might be a neighbor or tax authority, but in the lab could be the experimenter or an observer imagined by player 1. Player 2 has no (active) choice, but forms beliefs about $x$ after observing $y.$ The associated game-tree is $G1:$
$[G1]$
Numbers at end-nodes are 1 s monetary payo¤s, not utilities. The analysis will not depend on 2 s payo¤s, which are therefore not speci ed. The dotted lines depict information sets across end-nodes. This is a feature rarely made explicit in traditional game-theoretic analysis, but here it will be critical. In the example, these sets re ect player 2 s end-of-play information. D&D explore the following preference: Player 1 feels bad to the extent
that player 2 believes that 1 cheats. Measure actual cheating at end node
2See Abeler, Nosenzo & Raymond (2019) (AN&R) for a survey.
3
$(x; y)$ as $[y$