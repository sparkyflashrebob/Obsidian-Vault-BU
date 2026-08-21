---
title: "Frontiers | The Mathematical Structure of Integrated Information Theory"
source: "https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/full"
author:
  - "[[Frontiers]]"
published:
created: 2025-03-02
description: "Integrated Information Theory is one of the leading models of consciousness. It aims to describe both the quality and quantity of the conscious experience of..."
tags:
  - "clippings"
---
## 1 Introduction

*Integrated Information Theory (IIT)*, developed by Giulio Tononi and collaborators \[[5](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B5), [45](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B45)–[47](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B47)\], has emerged as one of the leading scientific theories of consciousness. At the heart of the latest version of the theory \[[19](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B19), [25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B25), [26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26), [31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31), [40](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B40)\] is an algorithm which, based on the level of *integration* of the internal functional relationships of a physical system in a given state, aims to determine both the quality and quantity (‘$\Phi$ value’) of its conscious experience.

While promising in itself \[[12](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B12), [43](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B43)\], the mathematical formulation of the theory is not satisfying to date. The presentation in terms of examples and accompanying explanation veils the essential mathematical structure of the theory and impedes philosophical and scientific analysis. In addition, the current definition of the theory can only be applied to comparably simple classical physical systems \[[1](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B1)\], which is problematic if the theory is taken to be a fundamental theory of consciousness, and should eventually be reconciled with our present theories of physics.

To resolve these problems, we examine the essentials of the IIT algorithm and formally define a generalized notion of Integrated Information Theory. This notion captures the inherent mathematical structure of IIT and offers a rigorous mathematical definition of the theory which has ‘classical’ IIT 3.0 of Tononi et al. \[[25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B25), [26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26), [31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31)\] as well as the more recently introduced *Quantum Integrated Information Theory* of Zanardi, Tomka and Venuti \[[50](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B50)\] as special cases. In addition, this generalization allows us to extend classical IIT, freeing it from a number of simplifying assumptions identified in \[[3](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B3)\]. Our results are summarised in [Figure 1](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#F1).

 [![www.frontiersin.org](https://www.frontiersin.org/files/Articles/602973/fams-06-602973-HTML-r1/image_m/fams-06-602973-g001.jpg)](https://www.frontiersin.org/files/Articles/602973/fams-06-602973-HTML-r1/image_m/fams-06-602973-g001.jpg)

**FIGURE 1**. An Integrated Information Theory specifies for every system in a particular state its conscious experience, described formally as an element of an experience space. In our formalization, this is a map $\mathbf{Sys} \overset{\mathbb{E}}{\rightarrow} \mathbf{Exp}$ from the system class **Sys** into a class **Exp** of experience spaces, which, first, sends each system *S* to its space of possible experiences $\mathbb{E} \left(\right. S \left.\right)$, and, second, sends each state $s \in \text{St} \left(\right. S \left.\right)$ to the actual experience the system is having when in that space, $\text{St} \left(\right. S \left.\right) \rightarrow \mathbb{E} \left(\right. S \left.\right) s \rightarrowtail \mathbb{E} \left(\right. S , s \left.\right) \textrm{ } .$ The definition of this map in terms of axiomatic descriptions of physical systems, experience spaces and further structure used in classical IIT is given in the first half of this paper.

In the associated article \[[44](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B44)\] we show more generally how the main notions of IIT, including causation and integration, can be treated, and an IIT defined, starting from any suitable theory of physical systems and processes described in terms of category theory. Restricting to classical or quantum process then yields each of the above as special cases. This treatment makes IIT applicable to a large class of physical systems and helps overcome the current restrictions.

Our definition of IIT may serve as the starting point for further mathematical analysis of IIT, in particular if related to category theory \[[30](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B30), [49](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B49)\]. It also provides a simplification and mathematical clarification of the IIT algorithm which extends the technical analysis of the theory \[[1](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B1), [41](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B41), [42](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B42)\] and may contribute to its ongoing critical discussion \[[2](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B2), [4](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B4), [8](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B8), [23](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B23), [27](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B27), [28](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B28), [33](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B33)\]. The concise presentation of IIT in this article should also help to make IIT more easily accessible for mathematicians, physicists and other researchers with a strongly formal background.

This work is concerned with the most recent version of IIT as proposed in \[[25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B25), [26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26), [31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31), [40](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B40)\] and similar papers quoted below. Thus our constructions recover the specific theory of consciousness referred to as IIT 3.0 or IIT 3.x, which we will call classical IIT in what follows. Earlier proposals by Tononi et al. that also aim to explicate the general idea of an essential connection between consciousness and integrated information constitute alternative theories of consciousness which we do not study here. A yet different approach would be to take the term ‘Integrated Information Theory’ to refer to the general idea of associating conscious experience with some pre-theoretic notion of integrated information, and to explore the different ways that this notion could be defined in formal terms \[[4](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B4), [27](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B27), [28](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B28), [37](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B37)\].

### Relation to Other Work

This work develops a thorough mathematical perspective of one of the promising contemporary theories of consciousness. As such it is part of a number of recent contributions which seek to explore the role and prospects of mathematical theories of consciousness \[[11](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B11), [15](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B15), [18](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B18), [30](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B30), [49](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B49)\], to help overcome problems of existing models \[[17](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B17), [18](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B18), [34](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B34)\] and to eventually develop new proposals \[[6](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B6), [13](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B13), [16](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B16), [20](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B20), [22](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B22), [29](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B29), [39](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B39)\].

### 1.1 Structure of Article

We begin by introducing the necessary ingredients of a generalised Integrated Information Theory in Sections 2–4, namely physical systems, experience spaces and cause-effect repertoires. Our approach is *axiomatic* in that we state only the precise formal structure which is necessary to apply the IIT algorithm. We neither motivate nor criticize these structures as necessary or suitable to model consciousness. Our goal is simply to recover IIT 3.0. In Section 5, we introduce a simple formal tool which allows us to present the definition of the algorithm of an IIT in a concise form in Sections 6 and 7. Finally, in Section 8, we summarise the full definition of such a theory. The result is the definition of a generalized IIT. We call any application of this definition ‘an IIT’.

Following this we give several examples including IIT 3.0 in Section 9 and Quantum IIT in Section 10. In Section 11 we discuss how our formulation allows one to extend classical IIT in several fundamental ways, before discussing further modifications to our approach and other future work in Section 12. Finally, the appendix includes a detailed explanation of how our generalization of IIT coincides with its usual presentation in the case of classical IIT.

## 2 Systems

The first step in defining an Integrated Information Theory (IIT) is to specify a class $\mathbf{Sys}$ of physical *systems* to be studied. Each element $S \in \mathbf{Sys}$ is interpreted as a model of one particular physical system. In order to apply the IIT algorithm, it is only necessary that each element *S* come with the following features.

Definition 1. A *system class*$\mathbf{Sys}$ is a class each of whose elements *S*, called *systems*, come with the following data:

1\. A set $\text{St} \left(\right. S \left.\right)$ of *states*;

2\. for every $s \in \text{St} \left(\right. S \left.\right)$, a set $\left(\text{Sub}\right)_{s} \left(\right. S \left.\right) \subset \mathbf{S} \mathbf{y} \mathbf{s}$ of subsystems and for each $M \in \left(\text{Sub}\right)_{s} \left(\right. S \left.\right)$ an induced state $s \left(\left|\right.\right)_{M} \in \text{St} \left(\right. M \left.\right)$;

3\. a set $\left(\mathbb{D}\right)_{S}$ of *decompositions*, with a given *trivial decomposition*$1 \in \left(\mathbb{D}\right)_{S}$;

4\. for each $z \in \left(\mathbb{D}\right)_{S}$ a corresponding *cut system*$S^{z} \in \mathbf{S} \mathbf{y} \mathbf{s}$ and for each state $s \in \text{St} \left(\right. S \left.\right)$ a corresponding *cut state*$s^{z} \in \text{St} \left(\right. S^{z} \left.\right)$.

Moreover, we require that $\mathbf{S} \mathbf{y} \mathbf{s}$ contains a distinguished *empty system*, denoted *I*, and that $I \in \text{Sub} \left(\right. S \left.\right)$ for all *S*. For the IIT algorithm to work, we need to assume furthermore that the number of subsystems remains the same under cuts or changes of states, i.e. that we have bijections $\left(\text{Sub}\right)_{s} \left(\right. S \left.\right) \simeq \left(\text{Sub}\right)_{s '} \left(\right. S \left.\right)$ for all $s , s ' \in \text{St} \left(\right. S \left.\right)$ and $\left(\text{Sub}\right)_{s} \left(\right. S \left.\right) \simeq \left(\text{Sub}\right)_{s^{z}} \left(\right. S^{z} \left.\right)$ for all $z \in \left(\mathbb{D}\right)_{S} .$Note that taking a subsystem of a system *S* requires specifying a state *s* of *S*. An example class of systems is illustrated in [Figure 2](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#F2). In this article we will assume that each set $\left(\text{Sub}\right)_{s} \left(\right. S \left.\right)$ is finite, discussing the extension to the infinite case in Section 12. We will give examples of system classes and for all following definitions in Sections 9 and 10.

 [![www.frontiersin.org](https://www.frontiersin.org/files/Articles/602973/fams-06-602973-HTML-r1/image_m/fams-06-602973-g002.jpg)](https://www.frontiersin.org/files/Articles/602973/fams-06-602973-HTML-r1/image_m/fams-06-602973-g002.jpg)

**FIGURE 2**. As an example of Definition 1 similar to IIT 3.0, consider simple systems given by sets of nodes (or ‘elements’), with a state assigning each node the state ‘on’ (depicted green) or ‘off’ (red). Each system comes with a time evolution shown by labelling each node with how its state in the next time-step depends on the states of the others. Decompositions of a system *S* correspond to binary partition of the nodes, such as *z* above. The cut system $S^{\mathit{z}}$ is given by modifying the time evolution of *S* so that the two halves do not interact; in this case all connections between the halves are replaced by sources of noise which send ‘on’ or ‘off’ with equal likelihood, depicted as black dots above. Given a current state *s* of *S*, any subset of the nodes (such as those below the dotted line) determines a subsystem $\left(\mathit{S}\right)^{'}$, with time evolution obtained from that of *S* by fixing the nodes in $\mathit{S} ∖ \left(\mathit{S}\right)^{'}$ (here, the upper node) to be in the state specified by *s*. Note that while in this example any subsystem (subset of *S*) determines a decomposition (partition of *S*) we do not require such a relationship in general.

## 3 Experience

An IIT aims to specify for each system in a particular state its *conscious experience*. As such, it will require a mathematical model of such experiences. Examining classical IIT, we find the following basic features of the final experiential states it describes which are needed for its algorithm.

Firstly, each experience *e* should crucially come with an *intensity*, given by a number $\left|\right. \left|\right. e \left|\right. \left|\right.$ in the non-negative reals $\left(\mathbb{R}\right)^{+}$ (including zero). This intensity will finally correspond to the overall intensity of experience, usually denoted by $\Phi$. Next, in order to compare experiences, we require a notion of *distance d*(*e*,*e*′) between any pair of experiences *e*,*e*′. Finally, the algorithm will require us to be able to *rescale* any given experience *e* to have any given intensity. Mathematically, this is most easily encoded by letting us multiply any experience *e* by any number $r \in \left(\mathbb{R}\right)^{+}$. In summary, a minimal model of experience in a generalized IIT is the following.

Definition 2. An *experience space* is a set *E* with:

1\. An *intensity* function $\left|\right. \left|\right. . \left|\right. \left|\right. : E \rightarrow \left(\mathbb{R}\right)^{+}$

2\. A *distance* function $d : E \times E \rightarrow \left(\mathbb{R}\right)^{+}$

3\. A *scalar multiplication*$\left(\mathbb{R}\right)^{+} \times E \rightarrow E$, denoted $\left(\right. r , e \left.\right) \rightarrowtail r \cdot e$, satisfying

$\parallel r \cdot e \parallel = r \cdot \parallel e \parallel \textrm{ } r \cdot \left(\right. s \cdot e \left.\right) = \left(\right. r s \left.\right) \cdot e \textrm{ } 1 \cdot e = e$

for all $e \in E$ and $r , s \in \left(\mathbb{R}\right)^{+}$.

We remark that this same axiomatisation will apply both to the full space of experiences of a system, as well as to the spaces describing components of the experiences (‘concepts’ and ‘proto-experiences’ defined in later sections). We note that the distance function does not necessarily have to satisfy the axioms of a metric. While this and further natural axioms such as $d \left(\right. r \cdot e , r \cdot f \left.\right) = r \cdot d \left(\right. e , f \left.\right)$ might hold, they are not necessary for the IIT algorithm.The above definition is very general, and in any specific application of IIT, the experiences may come with further mathematical structure. The following example includes the experience spaces used in classical IIT.

Example 3. Any metric space $\left(\right. X , d \left.\right)$ may be extended to an experience space $\bar{X} : = X \times \left(\mathbb{R}\right)^{+}$ in various ways. E.g., one can define $\left|\right. \left|\right. \left(\right. x , r \left.\right) \left|\right. \left|\right. = r$, $r \cdot \left(\right. x , s \left.\right) = \left(\right. x , r s \left.\right)$ and define the distance as

$d \left(\right. \left(\right. x , r \left.\right) , \left(\right. y , s \left.\right) \left.\right) = r d \left(\right. x , y \left.\right) \left(\right. 1 \left.\right)$

This is the definition used in classical IIT (cf. Section 9 and Appendix A). An important operation on experience spaces is taking their *product*.

Definition 4. For experience spaces *E* and *F*, we define the product to be the space $E \times F$ with distance

$d \left(\right. \left(\right. e , f \left.\right) , \left(\right. e^{'} , f^{'} \left.\right) \left.\right) = d \left(\right. e , e^{'} \left.\right) + d \left(\right. f , f^{'} \left.\right) , \left(\right. 2 \left.\right)$

intensity $\parallel \left(\right. e , f \left.\right) \parallel = max \left{\right. \parallel e \parallel , \parallel f \parallel \left.\right}$ and scalar multiplication $r \cdot \left(\right. e , f \left.\right) = \left(\right. r \cdot e , r \cdot f \left.\right)$. This generalizes to any finite product $\underset{i \in I}{\prod} E_{i}$ of experience spaces.

## 4 Repertoires

In order to define the experience space and individual experiences of a system *S*, an IIT utilizes basic building blocks called ‘repertoires’, which we will now define. Next to the specification of a system class, this is the essential data necessary for the IIT algorithm to be applied.

Each repertoire describes a way of ‘decomposing’ experiences, in the following sense. Let *D* denote any set with a distinguished element 1, for example the set $\left(\mathbb{D}\right)_{S}$ of decompositions of a system *S*, where the distinguished element is the trivial decomposition $1 \in \left(\mathbb{D}\right)_{S}$.

Definition 5. Let *e* be an element of an experience space *E*. A *decomposition of e over D* is a mapping $\bar{e} : D \rightarrow E$ with $\bar{e} \left(\right. 1 \left.\right) = e$.In more detail, a repertoire specifies a proto-experience for every pair of subsystems and describes how this experience changes if the subsystems are decomposed. This allows one to assess how integrated the system is with respect to a particular repertoire. Two repertoires are necessary for the IIT algorithm to be applied, together called the cause-effect repertoire.For subsystems $M , P \in \left(\text{Sub}\right)_{s} \left(\right. S \left.\right)$, define $\left(\mathbb{D}\right)_{M , P} : = \left(\mathbb{D}\right)_{M} \times \left(\mathbb{D}\right)_{P}$. This set describes the decomposition of both subsystems simultaneously. It has a distinguished element $1 = \left(\right. 1_{M} , 1_{P} \left.\right)$.

Definition 6. A *cause-effect repertoire* at *S* is given by a choice of experience space $\mathbb{P} \mathbb{E} \left(\right. S \left.\right)$, called the space of *proto-experiences*, and for each $s \in \text{St} \left(\right. S \left.\right)$ and $M , P \in \left(\text{Sub}\right)_{s} \left(\right. S \left.\right)$, a pair of elements

$cau s_{s} \left(\right. M , P \left.\right) , ef f_{s} \left(\right. M , P \left.\right) \in \mathbb{P} \mathbb{E} \left(\right. S \left.\right) \left(\right. 3 \left.\right)$

and for each of them a decomposition over $\left(\mathbb{D}\right)_{M , P}$.Examples of cause-effect repertoires will be given in Sections 9 and 10. A general definition in terms of process theories is given in \[[44](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B44)\]. For the IIT algorithm, a cause-effect repertoire needs to be specified for every system *S*, as in the following definition.

Definition 7. A *cause-effect structure* is a specification of a cause-effect repertoire for every $S \in \mathbf{S} \mathbf{y} \mathbf{s}$ such that

$\mathbb{P} \mathbb{E} \left(\right. S \left.\right) = \mathbb{P} \mathbb{E} \left(\right. S^{z} \left.\right) \textrm{ } &nbsp; \text{for}\&\text{nbsp};\text{all} &nbsp; \textrm{ } z \in \left(\mathbb{D}\right)_{S} . \left(\right. 4 \left.\right)$

The names ‘cause’ and ‘effect’ highlight that the definitions of $\left(\text{caus}\right)_{s} \left(\right. M , P \left.\right)$ and $\left(\text{eff}\right)_{s} \left(\right. M , P \left.\right)$ in classical and Quantum IIT describe the causal dynamics of the system. They are intended to capture the manner in which the ‘current’ state *s* of the system, when restricted to *M*, constrains the ‘previous’ or ‘next’ state of *P*, respectively.

## 5 Integration

We have now introduced all of the data required to define an IIT; namely, a system class along with a cause-effect structure. From this, we will give an algorithm aiming to specify the conscious experience of a system. Before proceeding to do so, we introduce a conceptual short-cut which allows the algorithm to be stated in a concise form. This captures the core ingredient of an IIT, namely the computation of how integrated an entity is.

Definition 8. Let *E* be an experience space and *e* an element with a decomposition over some set *D*. The *integration level* of *e* relative to this decomposition is

$\phi \left(\right. e \left.\right) : = \underset{1 \neq z \in D}{min} d \left(\right. e , \bar{e} \left(\right. z \left.\right) \left.\right) . \left(\right. 5 \left.\right)$

Here, *d* denotes the distance function of *E*, and the minimum is taken over all elements of *D* besides 1. The *integration scaling* of *e* is then the element of *E* defined by

where $\hat{e}$ denotes the *normalization* of *e*, defined as

$\hat{e} : = \left{\right. \frac{1}{\parallel e \parallel} \cdot e & \&\text{nbsp};\text{if}\&\text{nbsp}; \parallel e \parallel \neq 0 \\ e & \&\text{nbsp};\text{if}\&\text{nbsp}; \parallel e \parallel = 0.$

Finally, the *integration scaling* of a pair $e_{1} , e_{2}$ of such elements is the pair

$\iota \left(\right. e_{1} , e_{2} \left.\right) : = \left(\right. \phi \cdot \hat{e_{1}} , \phi \cdot \hat{e_{2}} \left.\right) \left(\right. 7 \left.\right)$

where $\phi : = \text{min} \left(\right. \phi \left(\right. e_{1} \left.\right) , \phi \left(\right. e_{2} \left.\right) \left.\right)$ is the minimum of their integration levels.We will also need to consider indexed collections of decomposable elements. Let *S* be a system in a state $s \in \text{St} \left(\right. S \left.\right)$ and assume that for every $M \in \left(\text{Sub}\right)_{s} \left(\right. S \left.\right)$ an element $e_{M}$ of some experience space $E_{M}$ with a decomposition over some $D_{M}$ is given. We call $\left(\left(\right. e_{M} \left.\right)\right)_{M \in \left(\text{Sub}\right)_{s} \left(\right. S \left.\right)}$ a *collection* of decomposable elements, and denote it as $\left(\left(\right. e_{M} \left.\right)\right)_{M}$.

Definition 9. The *core* of the collection $\left(\left(\right. e_{M} \left.\right)\right)_{M}$ is the subsystem $C \in \left(\text{Sub}\right)_{s} \left(\right. S \left.\right)$ for which $\phi \left(\right. e_{C} \left.\right)$ is maximal.[<sup>1</sup>](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#FN1) The *core integration scaling* of the collection is $\iota \left(\right. e_{C} \left.\right)$. The *core integration scaling* of a pair of collections $\left(\right. \left(\left(\right. e_{M} \left.\right)\right)_{M} , \left(\left(\right. f_{M} \left.\right)\right)_{M} \left.\right)$ is $\iota \left(\right. e_{C} , f_{D} \left.\right)$, where $C , D$ are the cores of $\left(\left(\right. e_{M} \left.\right)\right)_{M}$ and $\left(\left(\right. f_{M} \left.\right)\right)_{M}$, respectively.

## 6 Constructions: Mechanism Level

Let $S \in \mathbf{S} \mathbf{y} \mathbf{s}$ be a physical system whose experience in a state $s \in \text{St} \left(\right. S \left.\right)$ is to be determined. The first level of the algorithm involves fixing some subsystem $M \in \left(\text{Sub}\right)_{s} \left(\right. S \left.\right)$, referred to as a ‘mechanism’, and associating to it an object called its ‘concept’ which belongs to the *concept space*

For every choice of $P \in \left(\text{Sub}\right)_{s} \left(\right. S \left.\right)$, called a ‘purview’, the repertoire values $\left(\text{caus}\right)_{s} \left(\right. M , P \left.\right)$ and $\left(\text{eff}\right)_{s} \left(\right. M , P \left.\right)$ are elements of $\mathbb{P} \mathbb{E} \left(\right. S \left.\right)$ with given decompositions over $\left(\mathbb{D}\right)_{M , P}$. Fixing *M*, they provide elements with decompositions over Sub(S) given by

$\left(\text{caus}\right)_{s} \left(\right. M \left.\right) : = \left(\left(\right. \left(\text{caus}\right)_{s} \left(\right. M , P \left.\right) \left.\right)\right)_{P \in \text{Sub} \left(\right. S \left.\right)} \\ \left(\text{eff}\right)_{s} \left(\right. M \left.\right) : = \left(\left(\right. \left(\text{eff}\right)_{s} \left(\right. M , P \left.\right) \left.\right)\right)_{P \in \text{Sub} \left(\right. S \left.\right)} \textrm{ } . \left(\right. 9 \left.\right)$

The *concept* of *M* is then defined as the core integration scaling of this pair of collections,

$\left(\mathbb{C}\right)_{S , s} \left(\right. M \left.\right) : = \text{Core}\&\text{nbsp};\text{integration}\&\text{nbsp};\text{scaling}\&\text{nbsp};\text{of} &nbsp; \left(\right. \left(\text{caus}\right)_{s} \left(\right. M \left.\right) , \left(\text{eff}\right)_{s} \left(\right. M \left.\right) \left.\right) . \left(\right. 10 \left.\right)$

It is an element of $\mathbb{C} \left(\right. S \left.\right)$. Unraveling our definitions, the concept thus consists of the values of the cause and effect repertoires at their respective ‘core’ purviews $P^{c} , P^{e}$, i.e. those which make them ‘most integrated’. These values $\text{caus} \left(\right. M , P^{c} \left.\right)$ and $\text{eff} \left(\right. M , P^{e} \left.\right)$ are then each rescaled to have intensity given by the minima of their two integration levels.

## 7 Constructions: System Level

The second level of the algorithm specifies the experience of system *S* in state *s*. To this end, all concepts of a system are collected to form its *Q-shape*, defined as

$\left(\mathbb{Q}\right)_{s} \left(\right. S \left.\right) : = \left(\left(\right. \left(\mathbb{C}\right)_{S , s} \left(\right. M \left.\right) \left.\right)\right)_{M \in \left(\text{Sub}\right)_{s} \left(\right. S \left.\right)} \textrm{ } . \left(\right. 11 \left.\right)$

This Is an Element of the Space

where $n \left(\right. S \left.\right) : = \left|\right. \left(\text{Sub}\right)_{s} \left(\right. S \left.\right) \left|\right.$, which is finite and independent of the state *s* according to our assumptions. We can also define a Q-shape for any cut of *S*. Let $z \in \left(\mathbb{D}\right)_{S}$ be a decomposition, $S^{z}$ the corresponding cut system and $s^{z}$ be the corresponding cut state. We define

$\left(\mathbb{Q}\right)_{s} \left(\right. S^{z} \left.\right) : = \left(\left(\right. \left(\mathbb{C}\right)_{S^{z} , s^{z}} \left(\right. M \left.\right) \left.\right)\right)_{M \in \left(\text{Sub}\right)_{s^{z}} \left(\right. S^{z} \left.\right)} . \left(\right. 13 \left.\right)$

Because of [Eq. 4](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e4), and since the number of subsystems remains the same when cutting, $\left(\mathbb{Q}\right)_{s} \left(\right. S^{z} \left.\right)$ is also an element of $\mathbb{E} \left(\right. S \left.\right)$. This gives a map

which is a decomposition of $\left(\mathbb{Q}\right)_{s} \left(\right. S \left.\right)$ over $\left(\mathbb{D}\right)_{S}$. Considering this map for every subsystem of *S* gives a collection of decompositions defined as

$\mathbb{Q} \left(\right. S , s \left.\right) : = \left(\left(\right. \left(\bar{\mathbb{Q}}\right)_{M , s \left(\left|\right.\right)_{M}} \left.\right)\right)_{M \in \left(\text{Sub}\right)_{s} \left(\right. S \left.\right)}$

This is the system level-object of relevance and is what specifies the experience of a system according to IIT.

Definition 10. The *experience* of system *S* in the state $s \in \text{St} \left(\right. S \left.\right)$ is

$\mathbb{E} \left(\right. S , s \left.\right) : = \text{Core}\&\text{nbsp};\text{integration}\&\text{nbsp};\text{scaling}\&\text{nbsp};\text{of}\&\text{nbsp}; \mathbb{Q} \left(\right. S , s \left.\right) \textrm{ } . \left(\right. 14 \left.\right)$

The definition implies that $\mathbb{E} \left(\right. S , s \left.\right) \in \mathbb{E} \left(\right. M \left.\right)$, where $M \in \left(\text{Sub}\right)_{s} \left(\right. S \left.\right)$ is the core of the collection $\mathbb{Q} \left(\right. S , s \left.\right)$, called the *major complex*. It describes which part of system *S* is actually conscious. In most cases there will be a natural embedding $\mathbb{E} \left(\right. M \left.\right) \rightarrow \mathbb{E} \left(\right. S \left.\right)$ for a subsystem *M* of *S*, allowing us to view $\mathbb{E} \left(\right. S , s \left.\right)$ as an element of $\mathbb{E} \left(\right. S \left.\right)$ itself. Assuming this embedding to exist allows us to define an Integrated Information Theory concisely in the next section.

## 8 Integrated Information Theories

We can now summarize all that we have said about IITs.

Definition 11. An *Integrated Information Theory* is determined as follows. The *data* of the theory is a system class $\mathbf{S} \mathbf{y} \mathbf{s}$ along with a cause-effect structure. The theory then gives a mapping

into the class $\mathbf{E} \mathbf{x} \mathbf{p}$ of all experience spaces, sending each system *S* to its space of experiences $\mathbb{E} \left(\right. S \left.\right)$ defined in [Eq. 12](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e12), and a mapping

which determines the experience of the system when in a state *s*, defined in [Eq. 14](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e14).The *quantity* of the system’s experience is given by

and the quality of the system’s experience is given by the normalized experience $\hat{\mathbb{E}} \left(\right. S , s \left.\right)$. The experience is “located” in the core of the collection $\mathbb{Q} \left(\right. S , s \left.\right)$, called *the major complex*, which is a subsystem of *S*.In the next sections we specify the data of several example IITs.

## 9 Classical IIT

In this section we show how IIT 3.0 \[[25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B25), [26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26), [31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31), [48](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B48)\] fits in into the framework developed here. A detailed explanation of how our earlier algorithm fits with the usual presentation of IIT is given in Appendix A. In \[[44](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B44)\] we give an alternative categorical presentation of the theory.

### 9.1 Systems

We first describe the system class underlying classical IIT. Physical systems *S* are considered to be built up of several components $S_{1} , \ldots , S_{n}$, called *elements*. Each element $S_{i}$ comes with a finite set of states $\text{St} \left(\right. S_{i} \left.\right)$, equipped with a metric. A state of *S* is given by specifying a state of each element, so that

$\text{St} \left(\right. S \left.\right) = \text{St} \left(\right. S_{1} \left.\right) \times \hdots \times \text{St} \left(\right. S_{n} \left.\right) . \left(\right. 17 \left.\right)$

We define a metric *d* on $\text{St} \left(\right. S \left.\right)$ by summing over the metrics of the element state spaces $\text{St} \left(\right. S_{i} \left.\right)$ and denote the collection of probability distributions over $\text{St} \left(\right. S \left.\right)$ by $\mathcal{P} \left(\right. S \left.\right)$. Note that we may view $\text{St} \left(\right. S \left.\right)$ as a subset of $\mathcal{P} \left(\right. S \left.\right)$ by identifying any $s \in \text{St} \left(\right. S \left.\right)$ with its Dirac distribution $\left(\delta\right)_{s} \in \mathcal{P} \left(\right. S \left.\right)$, which is why we abbreviate $\left(\delta\right)_{s}$ by *s* occasionally in what follows.

Additionally, each system comes with a probabilistic (discrete) *time evolution operator* or *transition probability matrix*, sending each $s \in \text{St} \left(\right. S \left.\right)$ to a probabilistic state $T \left(\right. s \left.\right) \in \mathcal{P} \left(\right. S \left.\right)$. Equivalently it may be described as a convex-linear map

Furthermore, the evolution *T* is required to satisfy a property called *conditional independence*, which we define shortly.

The class $\mathbf{S} \mathbf{y} \mathbf{s}$ consists of all possible tuples $S = \left(\right. \left(\left{\right. S_{i} \left.\right}\right)_{i = 1}^{n} , T \left.\right)$ of this kind, with the trivial system *I* having only a single element with a single state and trivial time evolution.

### 9.2 Conditioning and Marginalizing

In what follows, we will need to consider two operations on the map *T*. Let *M* be any subset of the elements of a system and $M^{\bot}$ its complement. We again denote by $\text{St} \left(\right. M \left.\right)$ the Cartesian product of the states of all elements in *M*, and by $\mathcal{P} \left(\right. M \left.\right)$ the probability distributions on $\text{St} \left(\right. M \left.\right)$. For any $p \in \mathcal{P} \left(\right. M \left.\right)$, we define the *conditioning* \[[26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26)\] of *T* on *p* as the map

$T \left|\right. p \rangle : \mathcal{P} \left(\right. M^{\bot} \left.\right) \rightarrow \mathcal{P} \left(\right. S \left.\right) \\ p^{'} \rightarrowtail T \left(\right. p \cdot p^{'} \left.\right) \left(\right. 19 \left.\right)$

where $p \cdot p^{'}$ denotes the multiplication of these probability distributions to give a probability distribution over *S*. Next, we define *marginalisation over M* as the map

such that for each $p \in \mathcal{P} \left(\right. S \left.\right)$ and $m_{2} \in \text{St} \left(\right. M^{\bot} \left.\right)$ we have

$\langle M \left|\right. p \left(\right. m_{2} \left.\right) = \underset{m_{1} \in \text{St} \left(\right. M \left.\right)}{\sum} p \left(\right. m_{1} , m_{2} \left.\right) \textrm{ } . \left(\right. 21 \left.\right)$

In particular for any map *T* as above we call $\langle M \left|\right. T$ the *marginal* of *T* over *M* and we write $T_{i} : = \langle S_{i}^{\bot} \left|\right. T$ for each $i = 1 , \ldots , n$. Conditional independence of *T* may now be defined as the requirement that

$T \left(\right. p \left.\right) = \underset{i = 1}{\overset{n}{\prod}} T_{i} \left(\right. p \left.\right) \textrm{ } &nbsp; \text{for}\&\text{nbsp};\text{all} &nbsp; p \in \mathcal{P} \left(\right. S \left.\right) \textrm{ } ,$

where the right-hand side is again a probability distribution over $\text{St} \left(\right. S \left.\right)$.

### 9.3 Subsystems, Decompositions and Cuts

Let a system *S* in a state $s \in \text{St} \left(\right. S \left.\right)$ be given. The subsystems are characterized by subsets of the elements that constitute *S*. For any subset $M = \left{\right. S_{1} , \ldots , S_{m} \left.\right}$ of the elements of *S*, the corresponding subsystem is also denoted *M* and $\text{St} \left(\right. M \left.\right)$ is again given by the product of the $\text{St} \left(\right. S_{i} \left.\right)$, with time evolution

where $s_{M^{\bot}}$ is the restriction of the state *s* to $\text{St} \left(\right. M^{\bot} \left.\right)$ and $\left|\right. s_{M^{\bot}} \rangle$ denotes the conditioning on the Dirac distribution $\left(\delta\right)_{s_{M^{\bot}}}$.

The decomposition set $\left(\mathbb{D}\right)_{S}$ of a system *S* consists of all partitions of the set *N* of elements of *S* into two disjoint sets *M* and $M^{\bot}$. We denote such a partition by $z = \left(\right. M , M^{\bot} \left.\right)$. The trivial decomposition 1 is the pair $\left(\right. N , \emptyset \left.\right)$.

For any decomposition $\left(\right. M , M^{\bot} \left.\right)$ the corresponding cut system $S^{\left(\right. M , M^{\bot} \left.\right)}$ is the same as *S* but with a new time evolution $T^{\left(\right. M , M^{\bot} \left.\right)}$. Using conditional independence, it may be defined for each $i = 1 , \ldots , n$ as

$T_{i}^{\left(\right. M , M^{\bot} \left.\right)} : = \left{\right. T_{i} & i \in M^{\bot} \\ T_{i} \left|\right. \left(\omega\right)_{M^{\bot}} \rangle \langle M^{\bot} \left|\right. & i \in M , \left(\right. 23 \left.\right)$

where $\left(\omega\right)_{M} \in \mathcal{P} \left(\right. M \left.\right)$ denotes the uniform distribution on $\text{St} \left(\right. M \left.\right)$. This is interpreted in the graph depiction as removing all those edges from the graph whose source is in $M^{\bot}$ and whose target is in *M*. The corresponding input of the target element is replaced by noise, i.e. the uniform probability distribution over the source element.

### 9.4 Proto-Experiences

For each system *S*, the first Wasserstein metric (or ‘Earth Mover’s Distance’) makes $\mathcal{P} \left(\right. S \left.\right)$ a metric space $\left(\right. \mathcal{P} \left(\right. S \left.\right) , d \left.\right)$. The space of proto-experiences of classical IIT is

where $\bar{\mathcal{P} \left(\right. S \left.\right)}$ is defined in Example 3. Thus elements of $\mathbb{P} \mathbb{E} \left(\right. S \left.\right)$ are of the form $\left(\right. p , r \left.\right)$ for some $p \in \mathcal{P} \left(\right. S \left.\right)$ and $r \in \left(\mathbb{R}\right)^{+}$, with distance function, intensity and scalar multiplication as defined in the example.

### 9.5 Repertoires

It remains to define the cause-effect repertoires. Fixing a state *s* of *S*, the first step will be to define maps $\text{caus}_{\text{s}}^{'}$ and $\text{eff}_{s}^{'}$ which send any choice of $\left(\right. M , P \left.\right) \in \text{Sub} \left(\right. S \left.\right) \times \text{Sub} \left(\right. S \left.\right)$ to an element of $\mathcal{P} \left(\right. P \left.\right)$. These should describe the way in which the current state of *M* constrains that of *P* in the next or previous time-steps. We begin with the effect repertoire. For a single element purview $P_{i}$ we define

$\text{eff}_{s}^{'} \left(\right. M , P_{i} \left.\right) : = \langle P_{i}^{\bot} \left|\right. T \left|\right. \left(\omega\right)_{M^{\bot}} \rangle \left(\right. s_{M} \left.\right) , \left(\right. 25 \left.\right)$

where $s_{M}$ denotes (the Dirac distribution of) the restriction of the state *s* to *M*. While it is natural to use the same definition for arbitrary purviews, IIT 3.0 in fact uses another definition based on consideration of ‘virtual elements’ \[[25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B25), [26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26), [48](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B48)\], which also makes calculations more efficient (Supplementary Material S1 of \[[26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26)\]). For general purviews *P*, this definition is

$\text{eff}_{s}^{'} \left(\right. M , P \left.\right) = \underset{P_{i} \in P}{\prod} \text{eff}_{s}^{'} \left(\right. M , P_{i} \left.\right) , \left(\right. 26 \left.\right)$

taking the product over all elements $P_{i}$ in the purview *P*. Next, for the cause repertoire, for a single element mechanism $M_{i}$ and each $\overset{\sim}{s} \in \text{St} \left(\right. P \left.\right)$, we define

$\text{caus}_{s}^{'} \left(\right. M_{i} , P \left.\right) \left[\right. \overset{\sim}{s} \left]\right. = \lambda \langle M_{i}^{\bot} \left|\right. T \left|\right. \left(\omega\right)_{P^{\bot}} \rangle \left(\right. \left(\delta\right)_{\overset{\sim}{s}} \left.\right) \left[\right. s_{M_{i}} \left]\right. , \left(\right. 27 \left.\right)$

where λ is the unique normalisation scalar making $\text{caus}_{s}^{'} \left(\right. M_{i} , P \left.\right)$ a valid element of $\mathcal{P} \left(\right. P \left.\right)$. Here, for clarity, we have indicated evaluation of probability distributions at particular states by square brackets. If the time evolution operator has an inverse $T^{- 1}$, this cause repertoire could be defined similarly to (25) by $\text{caus}_{\text{s}}^{'} \left(\right. M_{i} , P \left.\right) = \langle P^{\bot} \left|\right. T^{- 1} \left|\right. \left(\omega\right)_{M_{i}^{\bot}} \rangle \left(\right. s_{M_{i}} \left.\right) \textrm{ } ,$ but classical IIT does not utilize this definition.

For General Mechanisms *M*, we Then Define

$\text{caus}_{\text{s}}^{'} \left(\right. M , P \left.\right) = \kappa \underset{M_{i} \in M}{\prod} \text{caus}_{\text{s}}^{'} \left(\right. M_{i} , P \left.\right) \left(\right. 28 \left.\right)$

where the product is over all elements $M_{i}$ in *M* and where $\kappa \in \left(\mathbb{R}\right)^{+}$ is again a normalisation constant. We may at last now define

$\left(\text{caus}\right)_{s} \left(\right. M , P \left.\right) & : = \text{caus}_{\text{s}}^{'} \left(\right. M , P \left.\right) \cdot \text{caus}_{\text{s}}^{'} \left(\right. \emptyset , P^{\bot} \left.\right) \\ \left(\text{eff}\right)_{s} \left(\right. M , P \left.\right) & : = \text{eff}_{\text{s}}^{'} \left(\right. M , P \left.\right) \cdot \text{eff}_{\text{s}}^{'} \left(\right. \emptyset , P^{\bot} \left.\right) \textrm{ } , \left(\right. 29 \left.\right)$

with intensity 1 when viewed as elements of $\mathbb{P} \mathbb{E} \left(\right. S \left.\right)$. Here, the dot indicates again the multiplication of probability distributions and $\emptyset$ denotes the empty mechanism.

The distributions $\text{caus}_{\text{s}}^{'} \left(\right. \emptyset , P^{\bot} \left.\right)$ and $\text{eff}_{s}^{'} \left(\right. \emptyset , P^{\bot} \left.\right)$ are called the *unconstrained cause and effect repertoires* over $P^{\bot}$.

Remark 12. It is in fact possible for the right-hand side of [Eq. 28](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e28) to be equal to 0 for all $\overset{\sim}{s}$ for some $M_{i} \in M$. In this case we set $\text{caus}_{\text{s}}^{'} \left(\right. M , P \left.\right) = \left(\right. \left(\omega\right)_{S} , 0 \left.\right)$ in $\mathbb{P} \mathbb{E} \left(\right. S \left.\right)$.Finally we must specify the decompositions of these elements over $\left(\mathbb{D}\right)_{M , P}$. For any partitions $z_{M} = \left(\right. M_{1} , M_{2} \left.\right)$ of *M* and $z_{P} = \left(\right. P_{1} , P_{2} \left.\right)$ of *P*, we define

$\bar{\left(\text{caus}\right)_{s}} \left(\right. M , P \left.\right) \left(\right. z_{M} , z_{P} \left.\right) : = \text{caus}_{\text{s}}^{'} \left(\right. M_{1} , P_{1} \left.\right) \cdot \text{caus}_{\text{s}}^{'} \left(\right. M_{2} , P_{2} \left.\right) \cdot \text{caus}_{\text{s}}^{'} \left(\right. \emptyset , P^{\bot} \left.\right) \\ \bar{\left(\text{eff}\right)_{s}} \left(\right. M , P \left.\right) \left(\right. z_{M} , z_{P} \left.\right) : = \text{eff}_{\text{s}}^{'} \left(\right. M_{1} , P_{1} \left.\right) \cdot \text{eff}_{\text{s}}^{'} \left(\right. M_{2}^{,} P_{2} \left.\right) \cdot \text{eff}_{\text{s}}^{'} \left(\right. \emptyset , P^{\bot} \left.\right) , \left(\right. 30 \left.\right)$

where we have abused notation by equating each subset $M_{1}$ and $M_{2}$ of nodes with their induced subsystems of *S* via the state *s*. This concludes all data necessary to define classical IIT. If the generalized definition of Section 8 is applied to this data, it yields precisely classical IIT 3.0 defined by Tononi et al. In [Appendix A](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#app16), we explain in detail how our definition of IIT, equipped with this data, maps to the usual presentation of the theory.

## 10 Quantum IIT

In this section, we consider Quantum IIT defined in \[[50](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B50)\]. This is also a special case of the definition in terms of process theories we give in \[[44](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B44)\].

### 10.1 Systems

Similar to classical IIT, in Quantum IIT systems are conceived as consisting of elements $\left(\mathcal{H}\right)_{1} , \ldots \textrm{ } , \left(\mathcal{H}\right)_{n}$. Here, each element $\left(\mathcal{H}\right)_{i}$ is described by a finite dimensional Hilbert space and the state space of system *S* is defined in terms of the element Hilbert spaces as

$\text{St} \left(\right. S \left.\right) = \mathcal{S} \left(\right. \left(\mathcal{H}\right)_{S} \left.\right) \textrm{ } &nbsp; \text{with} &nbsp; \textrm{ } \left(\mathcal{H}\right)_{S} = \overset{n}{\underset{i = 1}{\bigotimes}} \left(\mathcal{H}\right)_{i} ,$

where $\mathcal{S} \left(\right. \left(\mathcal{H}\right)_{S} \left.\right) \subset L \left(\right. \left(\mathcal{H}\right)_{S} \left.\right)$ describes the positive semidefinite Hermitian operators of unit trace on $\left(\mathcal{H}\right)_{S}$, i.e. density matrices. The time evolution of the system is again given by a time evolution operator, which here is assumed to be a trace preserving (and in \[[50](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B50)\] typically unital) completely positive map

### 10.2 Subsystems, Decompositions and Cuts

Subsystems are again defined to consist of subsets *M* of the elements of the system, with corresponding Hilbert space $\left(\mathcal{H}\right)_{M} : = \left(\bigotimes\right)_{i \in M} \left(\mathcal{H}\right)_{i}$. The time-evolution $\left(\mathcal{T}\right)_{M} : L \left(\right. \left(\mathcal{H}\right)_{M} \left.\right) \rightarrow L \left(\right. \left(\mathcal{H}\right)_{M} \left.\right)$ is defined as

$\left(\mathcal{T}\right)_{M} \left(\right. \rho \left.\right) = \left(\text{tr}\right)_{M^{\bot}} \left(\right. \mathcal{T} \left(\right. \left(\text{tr}\right)_{M^{\bot}} \left(\right. s \left.\right) \bigotimes \rho \left.\right) \left.\right) \textrm{ } ,$

where $s \in \mathcal{S} \left(\right. \left(\mathcal{H}\right)_{S} \left.\right)$ and $\left(\text{tr}\right)_{M^{\bot}}$ denotes the trace over the Hilbert space $\left(\mathcal{H}\right)_{M^{\bot}}$.

Decompositions are also defined via partitions $z = \left(\right. D , D^{\bot} \left.\right) \in \left(\mathbb{D}\right)_{S}$ of the set of elements *N* into two disjoint subsets *D* and $D^{\bot}$ whose union is *N*. For any such decomposition, the cut system $S^{\left(\right. D , D^{\bot} \left.\right)}$ is defined to have the same set of states but time evolution

$\left(\mathcal{T}\right)^{\left(\right. D , D^{\bot} \left.\right)} \left(\right. s \left.\right) = \mathcal{T} \left(\right. \left(\text{tr}\right)_{D^{\bot}} \left(\right. s \left.\right) \bigotimes \left(\omega\right)_{D^{\bot}} \left.\right) \textrm{ } ,$

where $\left(\omega\right)_{D^{\bot}}$ is the maximally mixed state on $\left(\mathcal{H}\right)_{D^{\bot}}$, i.e. $\left(\omega\right)_{D^{\bot}} = \frac{1}{\text{dim} \left(\right. \left(\mathcal{H}\right)_{D^{\bot}} \left.\right)} \textrm{ } 1_{\left(\mathcal{H}\right)_{D^{\bot}}}$.

### 10.3 Proto-Experiences

For any $\rho , \sigma \in \mathcal{S} \left(\right. \left(\mathcal{H}\right)_{S} \left.\right)$, the trace distance defined as

turns $\left(\right. S \left(\right. \left(\mathcal{H}\right)_{S} \left.\right) , d \left.\right)$ into a metric space. The space of proto-experiences is defined based on this metric space as described in Example 3,

### 10.4 Repertoires

We finally come to the definition of the cause-effect repertoire. Unlike classical IIT, the definition in \[[50](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B50)\] does not consider virtual elements. Let a system *S* in state $s \in \text{St} \left(\right. S \left.\right)$ be given. As in Section 9.5, we utilize maps $\text{caus}_{\text{s}}^{'}$ and $\text{eff}_{s}^{'}$ which here map subsystems *M* and *P* to $\text{St} \left(\right. P \left.\right)$. They are defined as

$\text{eff}_{s}^{'} \left(\right. M , P \left.\right) = t r_{P^{\bot}} \mathcal{T} \left(\right. t r_{M^{\bot}} \left(\right. s \left.\right) \bigotimes \left(\omega\right)_{M^{\bot}} \left.\right) \\ \text{caus}_{s}^{'} \left(\right. M , P \left.\right) = t r_{P^{\bot}} \left(\mathcal{T}\right)^{\dagger} \left(\right. t r_{M^{\bot}} \left(\right. s \left.\right) \bigotimes \left(\omega\right)_{M^{\bot}} \left.\right) \textrm{ } ,$

where $\left(\mathcal{T}\right)^{\dagger}$ is the Hermitian adjoint of $\mathcal{T}$. We then define

$\left(\text{caus}\right)_{s} \left(\right. M , P \left.\right) : = \text{caus}_{s}^{'} \left(\right. M , P \left.\right) \bigotimes \text{caus}_{s}^{'} \left(\right. \emptyset , P^{\bot} \left.\right) \\ \text{eff} \left(\right. M , P \left.\right) : = \text{eff}_{s}^{'} \left(\right. M , P \left.\right) \bigotimes \text{eff}_{s}^{'} \left(\right. \emptyset , P^{\bot} \left.\right) ,$

each with intensity 1, where $\emptyset$ again denotes the empty mechanism. Similarly, decompositions of these elements over $\left(\mathbb{D}\right)_{M , P}$ are defined as

$\bar{\left(\text{caus}\right)_{s}} \left(\right. M , P \left.\right) \left(\right. z_{M} , z_{P} \left.\right) : = \text{caus}_{\text{s}}^{'} \left(\right. M_{1} , P_{1} \left.\right) \bigotimes \text{caus}_{\text{s}}^{'} \left(\right. M_{2} , P_{2} \left.\right) \bigotimes \text{caus}_{\text{s}}^{'} \left(\right. \emptyset , P^{\bot} \left.\right) \\ \bar{\left(\text{eff}\right)_{s}} \left(\right. M , P \left.\right) \left(\right. z_{M} , z_{P} \left.\right) : = \text{eff}_{\text{s}}^{'} \left(\right. M_{1} , P_{1} \left.\right) \bigotimes \text{eff}_{\text{s}}^{'} \left(\right. M_{2} , P_{2} \left.\right) \bigotimes \text{eff}_{\text{s}}^{'} \left(\right. \emptyset , P^{\bot} \left.\right) \textrm{ } ,$

again with intensity 1, where $z_{M} = \left(\right. M_{1} , M_{2} \left.\right) \in \left(\mathbb{D}\right)_{M}$ and $z_{P} = \left(\right. P_{1} , P_{2} \left.\right) \in \left(\mathbb{D}\right)_{P}$.

## 11 Extensions of Classical IIT

The physical systems to which IIT 3.0 may be applied are limited in a number of ways: they must have a discrete time-evolution, satisfy Markovian dynamics and exhibit a discrete set of states \[[3](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B3)\]. Since many physical systems do not satisfy these requirements, if IIT is to be taken as a fundamental theory about reality, it must be extended to overcome these limitations.

In this section, we show how IIT can be redefined to cope with continuous time, non-Markovian dynamics and non-compact state spaces, by a redefinition of the maps [Eqs. 26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e26) and [28](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e28) and, in the case of non-compact state spaces, a slightly different choice of [Eq. 24](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e24), while leaving all of the remaining structure as it is. While we do not think that our particular definitions are satisfying as a general definition of IIT, these results show that the disentanglement of the essential mathematical structure of IIT from auxiliary tools (the particular definition of cause-effect repertoires used to date) can help to overcome fundamental mathematical or conceptual problems.

In Section 11.3, we also explain which solution to the problem of non-canonical metrics is suggested by our formalism.

### 11.1 Discrete Time and Markovian Dynamics

In order to avoid the requirement of a discrete time and Markovian dynamics, instead of working with the time evolution operator [Eq. 18](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e18), we define the cause- and effect repertoires in reference to a given trajectory of a physical state $s \in \text{St} \left(\right. S \left.\right)$. The resulting definitions can be applied independently of whether trajectories are being determined by Markovian dynamics in a particular application, or not.

Let $t \in \mathcal{I}$ denote the time parameter of a physical system. If time is discrete, $\mathcal{I}$ is an ordered set. If time is continuous, $\mathcal{I}$ is an interval of reals. For simplicity, we assume $0 \in \mathcal{I}$. In the deterministic case, a trajectory of a state $s \in \text{St} \left(\right. S \left.\right)$ is simply a curve in $\text{St} \left(\right. S \left.\right)$, which we denote by $\left(\left(\right. s \left(\right. t \left.\right) \left.\right)\right)_{t \in \mathcal{I}}$ with $s \left(\right. 0 \left.\right) = s$. For probabilistic systems (such as neural networks with a probabilistic update rule), it is a curve of probability distributions $\mathcal{P} \left(\right. S \left.\right)$, which we denote by $\left(\left(\right. p \left(\right. t \left.\right) \left.\right)\right)_{t \in \mathcal{I}}$, with $p \left(\right. 0 \left.\right)$ equal to the Dirac distribution $\left(\delta\right)_{s}$. The latter case includes the former, again via Dirac distributions.

In what follows, we utilize the fact that in physics, state spaces are defined such that the dynamical laws of a system allow to determine the trajectory of each state. Thus for every $s \in \text{St} \left(\right. S \left.\right)$, there is a trajectory $\left(\left(\right. p_{s} \left(\right. t \left.\right) \left.\right)\right)_{t \in \mathcal{I}}$ which describes the time evolution of *s*.

The idea behind the following is to define, for every $M , P \in \text{Sub} \left(\right. S \left.\right)$, a trajectory $p_{s}^{\left(\right. P , M \left.\right)} \left(\right. t \left.\right)$ in $\mathcal{P} \left(\right. P \left.\right)$ which quantifies how much the state of the purview *P* at time *t* is being constrained by imposing the state *s* at time $t = 0$ on the mechanism *M*. This gives an alternative definition of the maps (26) and (28), while the rest of classical IIT can be applied as before.

Let now $M , P \in \text{Sub} \left(\right. S \left.\right)$ and $s \in \text{St} \left(\right. S \left.\right)$ be given. We first consider the time evolution of the state $\left(\right. s_{M} , v \left.\right) \in \text{St} \left(\right. S \left.\right)$, where $s_{M}$ denotes the restriction of *s* to $\text{St} \left(\right. M \left.\right)$ as before and where $v \in \text{St} \left(\right. M^{\bot} \left.\right)$ is an arbitrary state of $M^{\bot}$. We denote the time evolution of this state by $p_{\left(\right. s_{M} , v \left.\right)} \left(\right. t \left.\right) \in \mathcal{P} \left(\right. S \left.\right)$. Marginalizing this distribution over $P^{\bot}$ gives a distribution on the states of *P*, which we denote as $p_{\left(\right. s_{M} , v \left.\right)}^{P} \left(\right. t \left.\right) \in \mathcal{P} \left(\right. P \left.\right)$. Finally, we average over *v* using the uniform distribution $\left(\omega\right)_{M^{\bot}}$. Because state spaces are finite in classical IIT, this averaging can be defined pointwise for every $w \in \text{St} \left(\right. P \left.\right)$ by

$p_{s}^{\left(\right. P , M \left.\right)} \left(\right. t \left.\right) \left(\right. w \left.\right) : = \kappa \underset{v \in S t \left(\right. M^{\bot} \left.\right)}{\sum} p_{\left(\right. s_{M} , v \left.\right)}^{P} \left(\right. t \left.\right) \left(\right. w \left.\right) \left(\omega\right)_{M^{\bot}} \left(\right. v \left.\right) , \left(\right. 31 \left.\right)$

where *κ* is the unique normalization constant which ensures that $p_{s}^{\left(\right. P , M \left.\right)} \left(\right. t \left.\right) \in \mathcal{P} \left(\right. P \left.\right)$.

The probability distribution $p_{s}^{\left(\right. P , M \left.\right)} \left(\right. t \left.\right) \in \mathcal{P} \left(\right. P \left.\right)$ describes how much the state of the purview *P* at time *t* is being constrained by imposing the state *s* on *M* at time $t = 0$ as desired. Thus, for every $t \in \mathcal{I}$, we have obtained a mapping of two subsystems $M , P$ to an element $p_{s}^{\left(\right. P , M \left.\right)} \left(\right. t \left.\right)$ of $\mathcal{P} \left(\right. P \left.\right)$ which has the same interpretation as the map [Eq. 26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e26) considered in classical IIT. If deemed necessary, virtual elements could be introduced just as in [Eqs 27](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e27) and [29](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e29).

So far, our construction can be applied for any time $t \in T$. It remains to fix this freedom in the choice of time. For the discrete case, the obvious choice is to define [Eqs 27](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e27) and [29](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e29) in terms of neighboring time-steps. For the continuous case, several choices exist. E.g., one could consider the positive and negative semi-derivatives of $p_{s}^{\left(\right. P , M \left.\right)} \left(\right. t \left.\right)$ at $t = 0$, in case they exist, or add an arbitrary but fixed time scale $\Delta$ to define the cause-effect repertoires in terms of $p_{s}^{\left(\right. P , M \left.\right)} \left(\right. t_{0} \pm \Delta \left.\right)$. However, the most reasonable choice is in our eyes to work with limits, in case they exist, by defining

$\text{eff}_{s}^{'} \left(\right. M , P \left.\right) : = \underset{P_{i} \in P}{\prod} \underset{t \rightarrow \infty}{lim} p_{s}^{\left(\right. P_{i} , M \left.\right)} \left(\right. t \left.\right) \left(\right. 32 \left.\right)$

to replace [Eq. 27](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e27) and

$\text{caus}_{\text{s}}^{'} \left(\right. M , P \left.\right) : = \kappa \underset{M_{i} \in M}{\prod} \underset{t \rightarrow - \infty}{lim} p_{s}^{\left(\right. P , M_{i} \left.\right)} \left(\right. t \left.\right) \left(\right. 33 \left.\right)$

to replace [Eq. 29](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e29). The remainder of the definitions of classical IIT can then be applied as before.

### 11.2 Discrete Set of States

The problem with applying the definitions of classical IIT to systems with continuous state spaces (e.g., neuron membrane potentials \[[3](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B3)\]) is that in certain cases, uniform probability distributions do not exist. E.g., if the state space of a system *S* consists of the positive real numbers $\left(\mathbb{R}\right)^{+}$, no uniform distribution can be defined which has a finite total volume, so that no uniform *probability* distribution $\left(\omega\right)_{S}$ exists.

It is important to note that this problem is less universal than one might think. E.g., if the state space of the system is a closed and bounded subset of $\left(\mathbb{R}\right)^{+}$, e.g. an interval $\left[\right. a , b \left]\right. \subset \left(\mathbb{R}\right)^{+}$, a uniform probability distribution can be defined using measure theory, which is in fact the natural mathematical language for probabilities and random variables. Nevertheless, the observation in \[[3](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B3)\] is correct that if a system has a non-compact continuous state space, $\left(\omega\right)_{S}$ might not exist, which can be considered a problem w.r.t. the above-mentioned working hypothesis.

This problem can be resolved for all well-understood physical systems by replacing the uniform probability distribution $\left(\omega\right)_{S}$ by some other mathematical entity which allows to define a notion of averaging states. For all relevant classical systems with non-compact state spaces (whether continuous or not), there exists a canonical uniform measure $\left(\mu\right)_{S}$ which allows to define the cause-effect repertoires similar to the last section, as we now explain. Examples for this canonical uniform measure are the Lebesgue measure for subsets of $\left(\mathbb{R}\right)^{n}$ \[[35](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B35)\], or the Haar measure for locally compact topological groups \[[36](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B36)\] such as Lie-groups.

In what follows, we explain how the construction of the last section needs to be modified in order to be applied to this case. In all relevant classical physical theories, $\text{St} \left(\right. S \left.\right)$ is a metric space in which every probability measure is a Radon measure, in particular locally finite, and where a canonical locally finite uniform measure $\left(\mu\right)_{S}$ exists. We define $\left(\mathcal{P}\right)_{1} \left(\right. S \left.\right)$ to be the space of probability measures whose first moment is finite. For these, the first Wasserstein metric (or ‘Earth Mover’s Distance’) $W_{1}$ exists, so that $\left(\right. \left(\mathcal{P}\right)_{1} \left(\right. S \left.\right) , W_{1} \left.\right)$ is a metric space.

As before, the dynamical laws of the physical systems determine for every state $s \in \text{St} \left(\right. S \left.\right)$ a time evolution $p_{s} \left(\right. t \left.\right)$, which here is an element of $\left(\mathcal{P}\right)_{1} \left(\right. S \left.\right)$. Integration of this probability measure over $\text{St} \left(\right. P^{\bot} \left.\right)$ yields the marginal probability measure $p_{s}^{P} \left(\right. t \left.\right)$. As in the last section, we may consider these probability measures for the state $\left(\right. s_{M} , v \left.\right) \in \text{St} \left(\right. S \left.\right)$, where $v \in \text{St} \left(\right. M^{\bot} \left.\right)$. Since $\left(\mu\right)_{S}$ is not normalizable, we cannot define $p_{s}^{\left(\right. P , M \left.\right)} \left(\right. t \left.\right)$ as in [(32)](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e32), for the result might be infinite.

Using the fact that $\left(\mu\right)_{S}$ is locally finite, we may, however, define a somewhat weaker equivalent. To this end, we note that for every state $s_{M^{\bot}}$, the local finiteness of $\left(\mu\right)_{M^{\bot}}$ implies that there is a neighborhood $N_{s , M^{\bot}}$ in $\text{St} \left(\right. M^{\bot} \left.\right)$ for which $\left(\mu\right)_{M^{\bot}} \left(\right. N_{s , M^{\bot}} \left.\right)$ is finite. We choose a sufficiently large neighborhood which satisfies this condition. Assuming $p_{\left(\right. s_{M} , v \left.\right)}^{P} \left(\right. t \left.\right)$ to be a measurable function in *v*, for every *A* in the σ-algebra of $\text{St} \left(\right. M^{\bot} \left.\right)$, we can thus define

$p_{s}^{\left(\right. P , M \left.\right)} \left(\right. t \left.\right) \left(\right. A \left.\right) : = \kappa \underset{N_{s , M^{\bot}}}{\int} p_{\left(\right. s_{M} , v \left.\right)}^{P} \left(\right. t \left.\right) \left(\right. A \left.\right) d \left(\mu\right)_{M^{\bot}} \left(\right. v \left.\right) , \left(\right. 34 \left.\right)$

which is a finite quantity. The $p_{s}^{\left(\right. P , M \left.\right)} \left(\right. t \left.\right)$ so defined is non-negative, vanishes for $A = \emptyset$ and satisfies countable additivity. Hence it is a measure on $\text{St} \left(\right. P \left.\right)$ as desired, but might not be normalizable.

All that remains for this to give a cause-effect repertoire as in the last section, is to make sure that any measure (normalized or not) is an element of $\mathbb{P} \mathbb{E} \left(\right. S \left.\right)$. The theory is flexible enough to do this by setting $d \left(\right. \mu , \nu \left.\right) = \left|\right. \mu - \nu \left|\right. \left(\right. \text{St} \left(\right. P \left.\right) \left.\right)$ if either μ or ν is not in $\left(\mathcal{P}\right)_{1} \left(\right. S \left.\right)$, and $W_{1} \left(\right. \mu , \nu \left.\right)$ otherwise. Here, $\left|\right. \mu - \nu \left|\right.$ denotes the total variation of the signed measure $\mu - \nu$, and $\left|\right. \mu - \nu \left|\right. \left(\right. \text{St} \left(\right. P \left.\right) \left.\right)$ is the volume thereof \[[10](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B10), [32](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B32)\]. While not a metric space any more, the tuple $\left(\right. \mathcal{M} \left(\right. S \left.\right) , d \left.\right)$, with $\mathcal{M} \left(\right. S \left.\right)$ denoting all measures on St(S), can still be turned into a space of proto-experiences as in Example 3. This gives

and finally allows one to construct cause-effect repertoires as in the last section.

### 11.3 Non-canonical Metrics

Another criticism of IIT’s mathematical structure mentioned \[[3](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B3)\] is that the metrics used in IIT’s algorithm are, to a certain extend, chosen arbitrarily. Different choices indeed imply different results of the algorithm, both concerning the quantity and quality of conscious experience, which can be considered problematic.

The resolution of this problem is, however, not so much a technical as a conceptual or philosophical task, for what is needed to resolve this issue is a justification of why a particular metric should be used. Various justifications are conceivable, e.g. identification of desired behavior of the algorithm when applied to simple systems. When considering our mathematical reconstruction of the theory, the following natural justification offers itself.

Implicit in our definition of the theory as a map from systems to experience spaces is the idea that the mathematical structure of experiences spaces (Definition 2) reflects the phenomenological structure of experience. This is so, most crucially, for the distance function *d*, which describes how similar two elements of experience spaces are. Since every element of an experience space corresponds to a conscious experience, it is naturally to demand that the similarly of the two mathematical objects should reflect the similarity of the experiences they describe. Put differently, the distance function *d* of an experience space should in fact mirror (or “model”) the similarity of conscious experiences as experienced by an experiencing subject.

This suggests that the metrics *d* used in the IIT algorithm should, ultimately, be defined in terms of the phenomenological structure of similarity of conscious experiences. For the case of color qualia, this is in fact feasible \[[18](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B18), Example 3.18\], \[[21](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B21), [38](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B38)\]. In general, the mathematical structure of experience spaces should be intimately tied to the phenomenology of experience, in our eyes.

## 12 Summary and Outlook

In this article, we have propounded the mathematical structure of Integrated Information Theory. First, we have studied which exact structures the IIT algorithm uses in the mathematical description of physical systems, on the one hand, and in the mathematical description of conscious experience, on the other. Our findings are the basis of definitions of a physical system class $\mathbf{S} \mathbf{y} \mathbf{s}$ and a class $\mathbf{E} \mathbf{x} \mathbf{p}$ of experience spaces, and allowed us to view IIT as a map $\mathbf{S} \mathbf{y} \mathbf{s} \rightarrow \mathbf{E} \mathbf{x} \mathbf{p}$.

Next, we needed to disentangle the essential mathematics of the theory from auxiliary formal tools used in the contemporary definition. To this end, we have introduced the precise notion of decomposition of elements of an experience space required by the IIT algorithm. The pivotal cause-effect repertoires are examples of decompositions so defined, which allowed us to view any particular choice, e.g. the one of ‘classical’ IIT developed by Tononi et al., or the one of ‘quantum’ IIT recently introduced by Zanardi et al. as data provided to a general IIT algorithm.

The formalization of cause-effect repertoires in terms of decompositions then led us to define the essential ingredients of IIT’s algorithm concisely in terms of integration levels, integration scalings and cores. These definitions describe and unify recurrent mathematical operations in the contemporary presentation, and finally allowed to define IIT completely in terms of a few lines of definition.

Throughout the paper, we have taken great care to make sure our definitions reproduce exactly the contemporary version of IIT 3.0. The result of our work is a mathematically rigorous and general definition of Integrated Information Theory. This definition can be applied to any meaningful notion of systems and cause-effect repertoires, and we have shown that this allows one to overcome most of the mathematical problems of the contemporary definition identified to date in the literature.

We believe that our mathematical reconstruction of the theory can be the basis for refined mathematical and philosophical analysis of IIT. We also hope that this mathematisation may make the theory more amenable to study by mathematicians, physicists, computer scientists and other researchers with a strongly formal background.

### 12.1 Process Theories

Our generalization of IIT is axiomatic in the sense that we have only included those formal structures in the definition which are necessary for the IIT algorithm to be applied. This ensured that our reconstruction is as general as possible, while still true to IIT 3.0. As a result, several notions used in classical IIT, e.g., system decomposition, subsystems or causation, are merely defined abstractly at first, without any reference to the usual interpretation of these concepts in physics.

In the related article \[[44](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B44)\], we show that these concepts can be meaningfully defined in any suitable *process theory* of physics, formulated in the language of *symmetric monoidal categories*. This approach can describe both classical and Quantum IIT and yields a complete formulation of contemporary IIT in a categorical framework.

### 12.2 Further Development of IIT

IIT is constantly under development, with new and refined definitions being added every few years. We hope that our mathematical analysis of the theory might help to contribute to this development. For example, the working hypothesis that IIT is a fundamental theory, implies that technical problems of the theory need to be resolved. We have shown that our formalization allows one to address the technical problems mentioned in the literature. However, there are others which we have not addressed in this paper.

Most crucially, the IIT algorithm uses a series of maximalization and minimalization operations, unified in the notion of *core* subsystems in our formalization. In general, there is no guarantee that these operations lead to unique results, neither in classical nor Quantum IIT. Using different cores has major impact on the output of the algorithm, including the $\Phi$ value, which is a case of ill-definedness.[<sup>2</sup>](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#FN2)

Furthermore, the contemporary definition of IIT as well as our formalization rely on there being a finite number of subsystems of each system, which might not be the case in reality. Our formalisation may be extendable to the infinite case by assuming that every system has a fixed but potentially infinite indexing set $\text{Sub} \left(\right. S \left.\right)$, so that each $\left(\text{Sub}\right)_{s} \left(\right. S \left.\right)$ is the image of a mapping $\text{Sub} \left(\right. S \left.\right) \times \text{St} \left(\right. S \left.\right) \rightarrow \mathbf{S} \mathbf{y} \mathbf{s}$, but we have not considered this in detail in this paper.

Finally, concerning more operational questions, it would be desirable to develop the connection to empirical measures such as the Perturbational Complexity Index (PCI) \[[7](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B7), [9](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B9)\] in more detail, as well as to define a controlled approximation of the theory whose calculation is less expensive. Both of these tasks may be achievable by substituting parts of our formalization with simpler mathematical structure.

On the conceptual side of things, it would be desirable to have a more proper understanding of how the mathematical structure of experiences spaces corresponds to the phenomenology of experience, both for the general definition used in our formalization—which comprises the minimal mathematical structure which is required for the IIT algorithm to be applied—and the specific definitions used in classical and Quantum IIT. In particular, it would be desirable to understand how it relates to the important notion of qualia, which is often asserted to have characteristic features such as ineffability, intrinsicality, non-contextuality, transparency or homogeneity \[[24](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B24)\]. For a first analysis toward this goal, cf \[[18](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B18)\]. A first proposal to add additional structure to IIT that accounts for relations between elements of consciousness in the case of spatial experiences was recently given in \[[14](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B14)\].

## Data Availability Statement

The original contributions presented in the study are included in the article/Supplementary Material, further inquiries can be directed to the corresponding author.

## Author Contributions

JK and ST conceived the project together and wrote the article together.

## Conflict of Interest

Author ST was employed by company Cambridge Quantum Computing Limited.

The remaining author declares that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Acknowledgments

We would like to thank the organizers and participants of the *Workshop on Information Theory and Consciousness* at the Center for Mathematical Sciences of the University of Cambridge, of the *Modeling Consciousness Workshop* in Dorfgastein and of the *Models of Consciousness Conference* at the Mathematical Institute of the University of Oxford for discussions on this topic. Much of this work was carried out while Sean Tull was under the support of an EPSRC Doctoral Prize at the University of Oxford, from November 2018 to July 2019, and while Johannes Kleiner was under the support of postdoctoral funding at the Institute for Theoretical Physics of the Leibniz University of Hanover. We would like to thank both institutions.

## Footnotes

<sup><a id="FN1" class="color1">1</a></sup>If the maximum does not exist, we define the core to be the empty system *I*.

<sup><a id="FN2" class="color1">2</a></sup>The problem of ‘unique existence’ has been studied extensively in category theory using *universal properties* and the notion of a *limit*. Rather than requiring that each $E \in \mathbb{E}$ come with a metric, it may be possible to alter the IIT algorithm into a well-defined categorical form involving limits to resolve this problem.

## References

3\. Barrett, AB, and Mediano, PAM. The Phi Measure of Integrated Information Is Not Well-Defined for General Physical Systems. *J Conscious Stud* (2019). 21:133. doi:10.1021/acs.jpcb.6b05183.s001

[CrossRef Full Text](https://doi.org/10.1021/acs.jpcb.6b05183.s001) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=The+Phi+Measure+of+Integrated+Information+Is+Not+Well-Defined+for+General+Physical+Systems&btnG=)

5\. Balduzzi, D, and Tononi, G. Integrated Information in Discrete Dynamical Systems: Motivation and Theoretical Framework. *Plos Comput Biol* (2008). 4(6):e1000091. doi:10.1371/journal.pcbi.1000091

[PubMed Abstract](https://pubmed.ncbi.nlm.nih.gov/18551165/) | [CrossRef Full Text](https://doi.org/10.1371/journal.pcbi.1000091) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Integrated+Information+in+Discrete+Dynamical+Systems:+Motivation+and+Theoretical+Framework&btnG=)

7\. Casarotto, S, Comanducci, A, Rosanova, M, Sarasso, S, Fecchio, M, Napolitani, M, et al. Stratification of Unresponsive Patients by an Independently Validated Index of Brain Complexity. *Ann Neurol* (2016). 80(5):718–29. doi:10.1002/ana.24779

[PubMed Abstract](https://pubmed.ncbi.nlm.nih.gov/27717082/) | [CrossRef Full Text](https://doi.org/10.1002/ana.24779) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Stratification+of+Unresponsive+Patients+by+an+Independently+Validated+Index+of+Brain+Complexity&btnG=)

9\. Casali, AG, Gosseries, O, Rosanova, M, Boly, M, Sarasso, S, Casali, KR, et al. A Theoretically Based Index of Consciousness Independent of Sensory Processing and Behavior. *Sci Translat Med* (2015). 5:198ra105. doi:10.1126/scitranslmed.3006294

[CrossRef Full Text](https://doi.org/10.1126/scitranslmed.3006294) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=A+Theoretically+Based+Index+of+Consciousness+Independent+of+Sensory+Processing+and+Behavior&btnG=)

10\. Halmos, PR. *Measure Theory* Berlin: Springer (1974).

11\. Hardy., L. Proposal to Use Humans to Switch Settings in a Bell Experiment (2017). arXiv preprint arXiv:1705.04620.

[Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Proposal+to+Use+Humans+to+Switch+Settings+in+a+Bell+Experiment&btnG=)

12\. Haun, AM, Oizumi, M, Kovach, CK, Kawasaki, H, Oya, H, Howard, MA, et al. Contents of consciousness investigated as integrated information in direct human brain recordings. (2016). bioRxiv.

[Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Contents+of+consciousness+investigated+as+integrated+information+in+direct+human+brain+recordings&btnG=)

14\. Haun, A, and Tononi, G. Why Does Space Feel the Way it Does? towards a Principled Account of Spatial Experience. *Entropy* (2019). 21(12):1160. doi:10.3390/e21121160

[CrossRef Full Text](https://doi.org/10.3390/e21121160) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Why+Does+Space+Feel+the+Way+it+Does?+towards+a+Principled+Account+of+Spatial+Experience&btnG=)

16\. Kent, A. Toy Models of Top Down Causation. (2019). arXiv preprint arXiv:1909.12739.

[Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Toy+Models+of+Top+Down+Causation&btnG=)

17\. Kleiner, J, and Hoel, E. Falsification and Consciousness. *Neurosci Consciousness* (2021). 2021(1):niab001. doi:10.1093/nc/niab001

[Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Falsification+and+Consciousness&btnG=)

20\. Kremnizer, K, and Ranchin, A. Integrated Information-Induced Quantum Collapse. *Found Phys* (2015). 45(8):889–99. doi:10.1007/s10701-015-9905-6

[CrossRef Full Text](https://doi.org/10.1007/s10701-015-9905-6) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Integrated+Information-Induced+Quantum+Collapse&btnG=)

23\. Kelvin, J. Interpretation-neutral Integrated Information Theory. *J Conscious Stud* (2019). 26(1-2):76–106. doi:10.1007/978-1-4419-9707-4\_13

[CrossRef Full Text](https://doi.org/10.1007/978-1-4419-9707-4_13) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Interpretation-neutral+Integrated+Information+Theory&btnG=)

24\. Metzinger, T. *Grundkurs Philosophie des Geistes, Band 1*. Berlin: Phänomenales Bewusstsein (2006).

26\. William, G, Mayner, P, Marshall, W, Albantakis, L, Findlay, G, Marchman, R, et al. PyPhi: A Toolbox for Integrated Information Theory. *Plos Comput Biol* (2018). 14(7):e1006343–21. doi:10.1371/journal.pcbi.1006343

[PubMed Abstract](https://pubmed.ncbi.nlm.nih.gov/30048445/) | [CrossRef Full Text](https://doi.org/10.1371/journal.pcbi.1006343) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=PyPhi:+A+Toolbox+for+Integrated+Information+Theory&btnG=)

27\. Pedro, AM, Rosas, F, Carhart-Harris, RL, Seth, A, and Adam, B. Beyond Integrated Information: A Taxonomy of Information Dynamics Phenomena. (2019). arXiv preprint arXiv:1909.02297.

[Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Beyond+Integrated+Information:+A+Taxonomy+of+Information+Dynamics+Phenomena&btnG=)

28\. Pedro, AM, Seth, A, and Adam, B. Measuring Integrated Information: Comparison of Candidate Measures in Theory and Simulation. *Entropy* (2019). 21(1):17. doi:10.3390/e21010017

[CrossRef Full Text](https://doi.org/10.3390/e21010017) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Measuring+Integrated+Information:+Comparison+of+Candidate+Measures+in+Theory+and+Simulation&btnG=)

29\. Mueller, MP. Could the Physical World Be Emergent Instead of Fundamental, and Why Should We Ask?(short Version). (2017). arXiv preprint arXiv:1712.01816.

[Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Could+the+Physical+World+Be+Emergent+Instead+of+Fundamental,+and+Why+Should+We+Ask?\(short+Version\)&btnG=)

30\. Northoff, G, Tsuchiya, N, and Saigo, H. Mathematics and the Brain. A Category Theoretic Approach to Go beyond the Neural Correlates of Consciousness. (2019). bioRxiv.

[Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Mathematics+and+the+Brain.+A+Category+Theoretic+Approach+to+Go+beyond+the+Neural+Correlates+of+Consciousness&btnG=)

31\. Oizumi, M, Albantakis, L, and Tononi, G. From the Phenomenology to the Mechanisms of Consciousness: Integrated Information Theory 3.0. *PLoS Comput Biol* (2014). 10(5):e1003588. doi:10.1371/journal.pcbi.1003588

[PubMed Abstract](https://pubmed.ncbi.nlm.nih.gov/24811198/) | [CrossRef Full Text](https://doi.org/10.1371/journal.pcbi.1003588) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=From+the+Phenomenology+to+the+Mechanisms+of+Consciousness:+Integrated+Information+Theory+3.0&btnG=)

32.Encyclopedia of Mathematics. *Signed Measure*. Berlin: Springer (2013).

33\. Anthony, P. Consciousness as Integrated Information a Provisional Philosophical Critique. *J Conscious Stud* (2013). 20(1–2):180–206. doi:10.2307/25470707

[CrossRef Full Text](https://doi.org/10.2307/25470707) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Consciousness+as+Integrated+Information+a+Provisional+Philosophical+Critique&btnG=)

34\. Pedro, R. *Proceedings of the Workshop on Combining Viewpoints in Quantum Theory, 19–22*. Edinburgh, UK: ICMS (2018).

35\. Walter, R. *Real and Complex Analysis*. London: Tata McGraw-hill education (2006).

36\. Salamon, D. *Measure and Integration*. London: European Mathematical Society (2016). doi:10.4171/159

[CrossRef Full Text](https://doi.org/10.4171/159)

37\. Seth, A, Adam, B, and Barnett, L. Causal Density and Integrated Information as Measures of Conscious Level. *Philos Trans A Math Phys Eng Sci* (1952). 369:3748–67. doi:10.1098/rsta.2011.0079

[PubMed Abstract](https://pubmed.ncbi.nlm.nih.gov/21893526/) | [CrossRef Full Text](https://doi.org/10.1098/rsta.2011.0079) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Causal+Density+and+Integrated+Information+as+Measures+of+Conscious+Level&btnG=)

38\. Sharma, G, Wu, W, and Edul, N. Dalal. The CIEDE2000 Color-Difference Formula: Implementation Notes, Supplementary Test Data, and Mathematical Observations. London: COLOR Research and Application (2004).

[Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Dalal.+The+CIEDE2000+Color-Difference+Formula:+Implementation+Notes,+Supplementary+Test+Data,+and+Mathematical+Observations&btnG=)

39\. Miguel Signorelli, C, Wang, Q, and Khan, I. A Compositional Model of Consciousness Based on Consciousness-Only. (2020). arXiv preprint arXiv:2007.16138.

[Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=A+Compositional+Model+of+Consciousness+Based+on+Consciousness-Only&btnG=)

40\. Tononi, G, Boly, M, Massimini, M, and Koch, C. Integrated Information Theory: from Consciousness to its Physical Substrate. *Nat Rev Neurosci* (2016). 17(7):450, 61. doi:10.1038/nrn.2016.44

[PubMed Abstract](https://pubmed.ncbi.nlm.nih.gov/27225071/) | [CrossRef Full Text](https://doi.org/10.1038/nrn.2016.44) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Integrated+Information+Theory:+from+Consciousness+to+its+Physical+Substrate&btnG=)

41\. Tegmark, M. Consciousness as a State of Matter. *Chaos, Solitons Fractals* (2015). 76:238–70. doi:10.1016/j.chaos.2015.03.014

[CrossRef Full Text](https://doi.org/10.1016/j.chaos.2015.03.014) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Consciousness+as+a+State+of+Matter&btnG=)

43\. Tsuchiya, N, Haun, A, Cohen, D, and Oizumi, M. *Empirical Tests of the Integrated Information Theory of consciousnessThe Return of Consciousness: A New Science on Old Questions*. London: Axel and Margaret Ax. son Johnson Foundation (2016). p. 349–74.

44\. Tull, S, and Kleiner, J. Integrated Information in Process Theories. *J Cognit Sci* (2021). 22:135–55.

49\. Tsuchiya, N, Taguchi, S, and Saigo, H. Using Category Theory to Assess the Relationship between Consciousness and Integrated Information Theory. *Neurosci Res* (2016). 107(1–7):133. doi:10.1016/j.neures.2015.12.007

[CrossRef Full Text](https://doi.org/10.1016/j.neures.2015.12.007) | [Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Using+Category+Theory+to+Assess+the+Relationship+between+Consciousness+and+Integrated+Information+Theory&btnG=)

50\. Zanardi, P, Tomka, M, and Venuti, LC. Quantum Integrated Information Theory. (2018). arXiv preprint arXiv:1806.01421, 2018 Comparison with Standard Presentation of IIT 3.0.

[Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Quantum+Integrated+Information+Theory&btnG=)

## Appendix A: Comparison with Standard Presentation of IIT 3.0

In Section 9, we have defined the system class and cause-effect repertoires which underlie classical IIT. The goal of this appendix is to explain in detail why applying our definition of the IIT algorithm yields IIT 3.0 defined by Tononi et al. In doing so, we will mainly refer to the terminology used in \[[25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B25), [26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26), [31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31), [48](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B48)\]. We remark that a particularly detailed presentation of the algorithm of the theory, and of how the cause and effect repertoire are calculated, is given in the Supplementary Material S1 of \[[26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26)\].

### A.1 Physical Systems

The systems of classical IIT are given in Section 9.1. They are often represented as graphs whose nodes are the elements $S_{1} , \ldots , S_{n}$ and edges represent functional dependence, thus describing the time evolution of the system as a whole, which we have taken as primitive in [Eq. 18](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e18). This is similar to the presentation of the theory in terms of a transition probability function

in \[[25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B25)\]. For each probability distribution $\overset{\sim}{p}$ over $\text{St} \left(\right. S \left.\right)$, this relates to our time evolution operator *T* via

$T \left(\right. \overset{\sim}{p} \left.\right) \left[\right. v \left]\right. : = \underset{w \in \text{St} \left(\right. S \left.\right)}{\sum} p \left(\right. v , w \left.\right) \textrm{ } \overset{\sim}{p} \left(\right. w \left.\right) \textrm{ } .$

### A.2 Cause-Effect Repertoires

In contemporary presentations of the theory (\[[25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B25)\], p. 14\] or \[[48](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B48)\]), the effect repertoire is defined as

$p_{\text{effect}} \left(\right. z_{i} , m_{t} \left.\right) : = \frac{1}{\left|\right. \left(\Omega\right)_{M^{c}} \left|\right.} \underset{m^{c} \in \left(\Omega\right)_{M^{c}}}{\sum} p \left(\right. z_{i} \left|\right. d o \left(\right. m_{t} , m^{c} \left.\right) \left.\right) \textrm{ } z_{i} \in \left(\Omega\right)_{Z_{i}} \left(\right. 35 \left.\right)$

and

$p_{\text{effect}} \left(\right. z , m_{t} \left.\right) : = \prod_{i = 1}^{\left|\right. z \left|\right.} p_{\text{effect}} \left(\right. z_{i} , m_{t} \left.\right) . \left(\right. 36 \left.\right)$

Here, $m_{t}$ denotes a state of the mechanism *M* at time *t*. $M^{c}$ denotes the complement of the mechanism, denoted in our case as $M^{\bot}$, $\left(\Omega\right)_{M^{c}}$ denotes the state space of the complement, and $m^{c}$ an element thereof. $Z_{i}$ denotes an element of the purview *Z* (designated by *P* in our case), $\left(\Omega\right)_{Z_{i}}$ denotes the state space of this element, $z_{i}$ a state of this element and *z* a state of the whole purview. $\left|\right. \left(\Omega\right)_{M^{c}} \left|\right.$ denotes the cardinality of the state space of $M^{c}$, and $\left|\right. z \left|\right.$ equals the number of elements in the purview. Finally, the expression $\text{do} \left(\right. m_{t} , m^{c} \left.\right)$ denotes a variant of the so-called “do-operator”. It indicates that the state of the system, here at time *t*, is to be set to the term in brackets. This is called *perturbing the system* into the state $\left(\right. m_{t} , m^{c} \left.\right)$. The notation $p \left(\right. z_{i} \left|\right. \text{do} \left(\right. m_{t} , m^{c} \left.\right) \left.\right)$ then gives the probability of finding the purview element in the state $z_{i}$ at time $t + 1$ given that the system is prepared in the state $\left(\right. m_{t} , m^{c} \left.\right)$ at time *t*.

In our notation, the right hand side of [Eq. 35](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e35) is exactly given by the right-hand side of [Eq. 25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e25), i.e. $\text{eff}_{\text{s}}^{'} \left(\right. M , P_{i} \left.\right)$. The system is prepared in a uniform distribution on $M^{c}$ (described by the sum and prefactor in [Eq. 35](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e35)) and with the restriction $s_{M}$ of the system state, here denoted by $m_{t}$, on *M*. Subsequently, *T* is applied to evolve the system to time $t + 1$, and the marginalization $\langle P_{i}^{\bot} \left|\right.$ throws away all parts of the states except those of the purview element $P_{i}$ (denoted above as $Z_{i}$). In total, [Eq. 25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e25) is a probability distribution on the states of the purview element. When evaluating this probability distribution at one particular state $z_{i}$ of the element, one obtains the same numerical value as [Eq. 35](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e35). Finally, taking the product in [Eq. 36](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e36) corresponds exactly to taking the product in [Eq. 26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e26).

Similarly, the cause repertoire is defined as (\[[25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B25)\], p. 14\] or \[[48](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B48)\])

$p_{\text{cause}} \left(\right. z \left|\right. m_{i , t} \left.\right) : = \frac{\left(\sum\right)_{z^{c} \in \left(\Omega\right)_{Z^{c}}} p \left(\right. m_{i , t} \left|\right. \text{do} \left(\right. z , z^{c} \left.\right) \left.\right)}{\left(\sum\right)_{s \in \left(\Omega\right)_{S}} p \left(\right. m_{i , t} \left|\right. \text{do} \left(\right. s \left.\right) \left.\right)} \textrm{ } z \in \left(\Omega\right)_{Z_{t - 1}} \left(\right. 37 \left.\right)$

and

$p_{\text{cause}} \left(\right. z \left|\right. m_{t} \left.\right) : = \frac{1}{K} \prod_{i = 1}^{\left|\right. m_{t} \left|\right.} p_{\text{cause}} \left(\right. z \left|\right. m_{i , t} \left.\right) , \left(\right. 38 \left.\right)$

where $m_{i}$ denotes the state of one element of the mechanism *M*, with the subscript *t* indicating that the state is considered at time *t*. *Z* again denotes a purview, *z* is a state of the purview and $\left(\Omega\right)_{Z_{t - 1}}$ denotes the state space of the purview, where the subscript indicates that the state is considered at time $t - 1$. *K* denotes a normalization constant and $\left|\right. m_{t} \left|\right.$ gives the number of elements in *M*.

Here, the whole right hand side of [Eq. 37](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e37) gives the probability of finding the purview in state *z* at time *t* − 1 if the system is prepared in state *m*<sub><em>i</em>,<em>t</em></sub> at time *t*. In our terminology this same distribution is given by [Eq. 27](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e27), where λ is the denominator in [Eq. 37](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e37). Taking the product of these distributions and re-normalising is then precisely [Eq. 28](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e28).

As a result, the cause and effect repertoire in the sense of \[[31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31)\] correspond precisely in our notation to $\text{caus}_{\text{s}}^{'} \left(\right. M , P \left.\right)$ and $\text{eff}_{\text{s}}^{'} \left(\right. M , P \left.\right)$, each being distributions over $\text{St} \left(\right. P \left.\right)$. In (Supplementary Material S1 of \[[26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26)\]), it is explained that these need to be extended by the unconstrained repertoires before being used in the IIT algorithm, which in our formalization is done in [Eq. 29](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e29), so that the cause-effect repertoires are now distributions over $\text{St} \left(\right. S \left.\right)$. These are in fact precisely what are called the *extended* cause and effect repertoires or *expansion to full state space* of the repertoires in \[[31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31)\].

The behavior of the cause- and effect-repertoires when decomposing a system is described, in our formalism, by decompositions (Definition 5). Hence a decomposition $z \in \left(\mathbb{D}\right)_{S}$ is what is called a *parition* in the classical formalism. For the case of classical IIT, a decomposition is given precisely by a partition of the set of elements of a system, and the cause-effect repertoires belonging to the decomposition are defined in [Eq. 30](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e30), which corresponds exactly to the definition

$p_{\text{cause}}^{\text{cut}} \left(\right. z \left|\right. m_{t} \left.\right) = p_{\text{cause}} \left(\right. z^{\left(\right. 1 \left.\right)} \left|\right. m_{t}^{\left(\right. 1 \left.\right)} \left.\right) \times p_{\text{cause}} \left(\right. z^{\left(\right. 2 \left.\right)} \left|\right. m_{t}^{\left(\right. 2 \left.\right)} \left.\right)$

in \[[25](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B25)\], when expanded to the full state space, and equally so for the effect repertoire.

### A.3 Algorithm: Mechanism Level

Next, we explicitly unpack our form of the IIT algorithm to see how it compares in the case of classical IIT with \[[31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31)\]. In our formalism, the integrated information *φ* of a mechanism *M* of system *S* when in state *s* is

defined in [Eq. 10](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e10). This definition conjoins several steps in the definition of classical IIT. To explain why it corresponds exactly to classical IIT, we disentangle this definition step by step.

First, consider $\left(\text{caus}\right)_{s} \left(\right. M , P \left.\right)$ in [Eq. 9](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e9). This is, by definition, a decomposition map. The calculation of the integration level of this decomposition map, cf. [Eq. 5](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e5), amounts to comparing $\left(\text{caus}\right)_{s} \left(\right. M , P \left.\right)$ to the cause-effect repertoire associated with every decomposition using the metric of the target space $\mathbb{P} \mathbb{E} \left(\right. S \left.\right)$, which for classical IIT is defined in [Eq. 24](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e24) and Example 3, so that the metric *d* used for comparison is indeed the Earth Mover’s Distance. Since cause-effect repertoires have, by definition, unit intensity, the factor *r* in the definition (1) of the metric does not play a role at this stage. Therefore, the integration level of $\left(\text{caus}\right)_{s} \left(\right. M , P \left.\right)$ is exactly the *integrated cause information*, denoted as

in \[[48](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B48)\], where $y_{t}$ denotes the (induced state of the) mechanism *M* in this notation, and $Z_{t - 1}$ denotes the purview *P*. Similarly, the integration level of $\left(\text{eff}\right)_{s} \left(\right. M , P \left.\right)$ is exactly the *integrated effect information*, denoted as

The integration scaling in [Eq. 10](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e10) simply changes the intensity of an element of $\mathbb{P} \mathbb{E} \left(\right. S \left.\right)$ to match the integration level, using the scalar multiplication, which is important for the system level definitions. When applied to $\left(\text{caus}\right)_{s} \left(\right. M , P \left.\right)$, this would result in an element of $\mathbb{P} \mathbb{E} \left(\right. S \left.\right)$ whose intensity is precisely $\varphi_{\text{cause}}^{\text{MIP}} \left(\right. y_{t} , Z_{t - 1} \left.\right)$.

Consider now the collections (9) of decomposition maps. Applying Definition 9, the core of $\left(\text{caus}\right)_{s} \left(\right. M \left.\right)$ is that purview *P* which gives the decomposition $\left(\text{caus}\right)_{s} \left(\right. M , P \left.\right)$ with the highest integration level, i.e. with the highest $\varphi_{\text{cause}}^{\text{MIP}} \left(\right. y_{t} , Z_{t - 1} \left.\right)$. This is called the *core cause*$P^{c}$ of *M*, and similarly the core of $\left(\text{eff}\right)_{s} \left(\right. M \left.\right)$ is called the *core effect*$P^{e}$ of *M*.

Finally, to fully account for [Eq. 10](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e10), we note that the integration scaling of a pair of decomposition maps rescales both elements to the minimum of the two integration levels. Hence the integration scaling of the pair $\left(\right. \left(\text{caus}\right)_{s} \left(\right. M , P \left.\right) , \text{eff} \left(\right. M , P ' \left.\right) \left.\right)$ fixes the scalar value of both elements to be exactly the *integrated information*, denoted as

$\varphi \left(\right. y_{t} , Z_{t \pm 1} \left.\right) = \text{min} \left(\right. \varphi_{\text{cause}}^{\text{MIP}} , \varphi_{\text{effect}}^{\text{MIP}} \left.\right)$

in \[[48](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B48)\], where $P = Z_{t + 1}$ and $P ' = Z_{t - 1}$.

In summary, the following operations are combined in [Eq. 10](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e10). The core of $\left(\right. \left(\text{caus}\right)_{s} \left(\right. M \left.\right) , \left(\text{eff}\right)_{s} \left(\right. M \left.\right) \left.\right)$ picks out the core cause $P^{c}$ and core effect $P^{e}$. The core integration scaling subsequently considers the pair $\left(\right. \left(\text{caus}\right)_{s} \left(\right. M , P^{c} \left.\right) , \text{eff} \left(\right. M , P^{e} \left.\right) \left.\right)$, called *maximally irreducible cause-effect repertoire*, and determines the integration level of each by analysing the behavior with respect to decompositions. Finally, it rescales both to the minimum of the integration levels. Thus it gives exactly what is called $\left(\varphi\right)^{\text{max}}$ in \[[48](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B48)\]. Using, finally, the definition of the intensity of the product $\mathbb{P} \mathbb{E} \left(\right. S \left.\right) \times \mathbb{P} \mathbb{E} \left(\right. S \left.\right)$ in Definition 4, this implies (39). The concept of *M* in our formalization is given by the tuple

$\left(\mathbb{C}\right)_{S , s} \left(\right. M \left.\right) : = \left(\right. \left(\right. \left(\text{caus}\right)_{s} \left(\right. M , P^{c} \left.\right) , \left(\varphi\right)^{max} \left(\right. M \left.\right) \left.\right) , \left(\right. \left(\text{eff}\right)_{s} \left(\right. M , P^{e} \left.\right) , \left(\varphi\right)^{max} \left(\right. M \left.\right) \left.\right) \left.\right)$

i.e., the pair of maximally irreducible repertoires scaled by $\left(\varphi\right)^{\text{max}} \left(\right. M \left.\right)$. This is equivalent to what is called a *concept*, or sometimes *quale sensu stricto*, in classcial IIT \[[48](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B48)\], and denoted as $q \left(\right. y_{t} \left.\right)$.

We finally remark that it is also possible in classical IIT that a cause repertoire value $\left(\text{caus}\right)_{s} \left(\right. M , P \left.\right)$ vanishes (Remark 12). In our formalization, it would hence be represented by $\left(\right. \left(\omega\right)_{S} , 0 \left.\right)$ in $\mathbb{P} \mathbb{E} \left(\right. S \left.\right)$, so that $d \left(\right. \left(\text{caus}\right)_{s} \left(\right. M , P \left.\right) , q \left.\right) = 0$ for all $q \in \mathbb{E} \left(\right. S \left.\right)$ according to (1), which certainly ensures that $\varphi_{\text{cause}}^{\text{MIP}} \left(\right. M , P \left.\right) = 0$.

### A.4 Algorithm: System Level

We finally explain how the system level definitions correspond to the usual definition of classical IIT.

The Q-shape $\left(\mathbb{Q}\right)_{s} \left(\right. S \left.\right)$ is the collection of all concepts specified by the mechanisms of a system. Since each concept has intensity given by the corresponding integrated information of the mechanism, this makes $\left(\mathbb{Q}\right)_{s} \left(\right. S \left.\right)$ what is usually called the *conceptual structure* or *cause-effect structure*. In \[[31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31)\], one does not include a concept for any mechanism *M* with $\left(\varphi\right)^{\text{max}} \left(\right. M \left.\right) = 0$. This manual exclusion is unnecessary in our case because the mathematical structure of experience spaces implies that mechanisms with $\left(\varphi\right)^{\text{max}} \left(\right. M \left.\right) = 0$ should be interpreted as having no conscious experience, and the algorithm in fact implies that they have ‘no effect’. Indeed we will now see that they do not contribute to the distances in $\mathbb{E} \left(\right. S \left.\right)$ or any $\Phi$ values, and so we do not manually exclude them.

When comparing $\left(\mathbb{Q}\right)_{s} \left(\right. S \left.\right)$ with the Q-shape [Eq. 13](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e13) obtained after replacing *S* by any of its cuts, it is important to note that both are elements of $\mathbb{E} \left(\right. S \left.\right)$ defined in [Eq. 12](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e12), which is a product of experience spaces. According to Definition 4, the distance function on this product is

$d \left(\right. \left(\mathbb{Q}\right)_{s} \left(\right. S \left.\right) , \left(\mathbb{Q}\right)_{s} \left(\right. S^{z} \left.\right) \left.\right) : = \underset{M \in \text{Sub} \left(\right. S \left.\right)}{\sum} d \left(\right. \left(\mathbb{C}\right)_{S , s} \left(\right. M \left.\right) , \left(\mathbb{C}\right)_{S^{z} , s^{z}} \left(\right. M \left.\right) \left.\right) \textrm{ } .$

Using Definition 3 and the fact that each concept’s intensity is $\left(\varphi\right)^{\text{max}} \left(\right. M \left.\right)$ according to the mechanism level definitions, each distance $d \left(\right. \left(\mathbb{C}\right)_{S , s} \left(\right. M \left.\right) , \left(\mathbb{C}\right)_{S^{z} , s^{z}} \left(\right. M \left.\right) \left.\right)$ is equal to

$\left(\varphi\right)^{max} \left(\right. M \left.\right) \cdot \left{\right. d \left[\right. \left(\text{caus}\right)_{s} \left(\right. M , P_{M}^{c} \left.\right) , \text{caus}_{s}^{z} \left(\right. M , P_{M}^{z , c} \left.\right) \left]\right. \\ + d \left[\right. \left(\text{eff}\right)_{s} \left(\right. M , P_{M}^{e} \left.\right) , \text{eff}_{s}^{z} \left(\right. M , P_{M}^{z , e} \left.\right) \left]\right. \left.\right} , \left(\right. 40 \left.\right)$

where $\left(\varphi\right)^{\text{max}} \left(\right. M \left.\right)$ denotes the integrated information of the concept in the original system *S*, and where the right-hand cause and effect repertoires are those of $S^{z}$ at its own core causes and effects for *M*. The factor $\left(\varphi\right)^{\text{max}} \left(\right. M \left.\right)$ ensures that the distance used here corresponds precisely to the distance used in \[[31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31)\], there called the *extended Earth Mover’s Distance*. If the integrated information $\left(\varphi\right)^{\text{max}} \left(\right. M \left.\right)$ of a mechanism is non-zero, it follows that $d \left(\right. \left(\mathbb{C}\right)_{S , s} \left(\right. M \left.\right) , \left(\mathbb{C}\right)_{S^{z} , s^{z}} \left(\right. M \left.\right) \left.\right) = 0$ as mentioned above, so that this concept does not contribute.

We remark that in Supplementary Material S1 of \[[26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26)\], an additional step is mentioned which is not described in any of the other papers we consider. Namely, if the integrated information of a mechanism is non-zero before cutting but zero after cutting, what is compared is not the distance of the corresponding concepts as in [Eq. 40](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e40), but in fact the distance of the original concept with a special null concept, defined to be the unconstrained repertoire of the cut system. We have not included this step in our definitions, but it could be included by adding a choice of distinguished point to Example 3 and redefining the metric correspondingly.

In [Eq. 14](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e14) the above comparison is being conducted for every subsystem of a system *S*. The subsystems of *S* are what is called *candidate systems* in \[[31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31)\], and which describe that ‘part’ of the system that is going to be conscious according to the theory (cf. below). Crucially, candidate systems are subsystems of *S*, whose time evolution is defined in [Eq. 22](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e22). This definition ensures that the state of the elements of *S* which are not part of the candidate system are fixed in their current state, i.e., constitute *background conditions* as required in the contemporary version of classcial IIT \[[26](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B26)\].

[Eq. 14](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e14) then compares the Q-shape of every candidate system to the Q-shape of all of its cuts, using the distance function described above, where the cuts are defined in [Eq. 23](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e23). The cut system with the smallest distance gives the system-level *minimum information partition* and the *integrated (conceptual) information* of that candidate system, denoted as $\Phi \left(\right. x_{t} \left.\right)$ in \[[48](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B48)\].

The core integration scaling finally picks out that candidate system with the largest integrated information value. This candidate system is the *major complex M* of *S*, the part of *S* which is conscious according to the theory as part of the *exclusion postulate* of IIT. Its Q-shape is the *maximally irreducible conceptual structure (MICS)*, also called *quale sensu lato*. The overall *integrated conceptual information* is, finally, simply the intensity of $\mathbb{E} \left(\right. S , s \left.\right)$ as defined in [Eq. 14](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e14),

### A.5 Constellation in Qualia Space

Expanding our definitions, and denoting the major complex by *M* with state $m = s \left(\left|\right.\right)_{M}$, in our terminology the experience of system *S* state *s* is

$\mathbb{E} \left(\right. S , s \left.\right) : = \textrm{ } \frac{\Phi \left(\right. M , m \left.\right)}{\left|\right. \left|\right. \left(\mathbb{Q}\right)_{m} \left(\right. M \left.\right) \left|\right. \left|\right.} \cdot \textrm{ } \left(\mathbb{Q}\right)_{m} \left(\right. M \left.\right) \textrm{ } . \left(\right. 41 \left.\right)$

This encodes the Q-shape $\left(\mathbb{Q}\right)_{m} \left(\right. M \left.\right)$, i.e. the maximally irreducible conceptual structure of the major complex, sometimes called *quale sensu lato*, which is taken to describe the quality of conscious experience. By construction it also encodes the integrated conceptual information of the major complex, which captures its intensity, since we have $\left|\right. \left|\right. \mathbb{E} \left(\right. S , s \left.\right) \left|\right. \left|\right. = \Phi \left(\right. M , m \left.\right)$. The rescaling of $\left(\mathbb{Q}\right)_{m} \left(\right. M \left.\right)$ in [Eq. 41](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#e41) leaves the relative intensities of the concepts in the MICS intact. Thus $\mathbb{E} \left(\right. S , s \left.\right)$ is the *constellation of concepts in qualia space*$\mathbb{E} \left(\right. M \left.\right)$ of \[[31](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2020.602973/#B31)\].