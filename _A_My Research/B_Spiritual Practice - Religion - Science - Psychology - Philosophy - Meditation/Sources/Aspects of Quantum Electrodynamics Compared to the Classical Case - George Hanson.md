---
tags:
  - notebooklm-import
notebook: "B_Spiritual Practice - Religion - Science - Psychology - Philosophy - Meditation"
category: "research"
---

https://georgewhanson.com/files/Aspects\_QEM.pdf

In this article, aspects of quantum electro-

magnetics (QEM) are discussed with a view toward illustrating basic concepts and mak-ing some connections with classical EM.

The similarities and differences between the mathematical representations as well as the physical interpretations in the quantum and classical cases are reviewed, and a brief dis-cussion of the different objectives and quanti-ties to be measured/computed in quantum and classical regimes is provided. The role of the classical Green function in rigorous, fully quantum electrodynamics (QED) is highlight-ed, and an example of quantum state evolution in a graphene environment is presented.

INTRODUCTION QED/QEM is the study of quantized radiation, its statistical properties, and its interaction with mate-rials. It is necessary to invoke QED when only a small number of photons are present in a system. Although both the quantum and classical cases are governed by Maxwell’s equations (the former in

Similarity and disparity of quantum and classical electromagnetics.

Aspects of Quantum Electrodynamics Compared to the Classical Case

George W. Hanson

Digital Object Identifier 10.1109/MAP.2020.2990065 Date of current version: 19 May 2020

SPECIAL SERIES

operator form), both the questions typically asked and the math-ematical operations used to answer those questions are quite dif-ferent. In this article, some of these similarities and differences are highlighted, with several examples provided.

QEM requires the use of annihilation and creation operators, so familiarity with second quantization notation is assumed. Basic quantum optics (QO) are examined in a variety of textbooks [1]–[7].

One of the first things that should be mentioned is the pho-ton concept. Despite the fact that photon properties are seem-ingly fairly well understood (that is, how photons act), photons lack an intuitive understanding in the sense of how everyday objects behave. It seems impossible to answer the question “what is a photon?” in a simple manner [8]. The photon is a rather mysterious object, hence, the old saying that “a photon is what a photon detector detects.” Furthermore, modifying from Feynman [9], given that an atom can absorb a photon and atoms are pretty small, one may think that a photon must be smaller. However, this logic is false. Photons are not tiny (hence, localized) particles of energy, because often, photons

spread out over all space. In very sharp contrast with classical electrodynamics, where a radiation mode can take any energy value by increasing or decreasing the field amplitude in a con-tinuous fashion, in quantum EM, the energy of a single mode of the field with frequency ~ can only take on values separated from each other by multiples of '~ (i.e., the mode energy can only be increased or decreased in multiples of '~). This mini-mum amount of energy is associated with the term photon as the quanta of the field.

To have an idea of the large number of EM excitations (pho-tons) usually present in EM phenomena, assume ,600 nmm = so that each photon carries .E 3 31 10p

19#'~= = - J of energy. An EM wave carrying ( / )W1 J s-n n= of power consists of N 3 1012#= photons/s, so the granularity of this flow is vir-tually unobservable. This is usually the case unless great effort is taken to reduce the intensity, and hence, the number of photons. This is why the discrete nature of light is not easily observed in everyday situations. Moreover, in addition to representing extremely low intensity light, much of QED phenomena and applications rests upon the fact that uniquely quantum energy states can be found and manipulated (number states, coherent states, squeezed states, and so on).

Figure 1 depicts a dielectric slab in vacuum, with quantum “vacuum” fluctuations [7] present in all regions. Scattering, waveguiding, surface-plasmon polaritons, and other associ-ated phenomena occur in both quantum and classical cases and share many similarities. One of the basic problems in QEM is determining how the space around a natural or artificial atom, including the vacuum fluctuations, affects the atom’s spontaneous emission rate, statistics of the atom’s florescence, and/or whether an atom can form quantum entanglement with another object.

SIMILARITIES It is useful to consider the following similarities and differences between classical and QEM:

■ Maxwell’s equations (and associated equations such as the continuity equation) have the same form for both classical and quantum fields (operators). Related to this, the bound-ary conditions imposed on quantum fields are the same as those placed on classical fields and, related phenomena, such as Snell’s laws, resonance conditions, and so forth also apply to quantum fields.

■ The spatial variation of the field is the same as in the clas-sical and quantum cases. For example, the quantum field of an atomic dipole has the same spatial form as that of the classical dipole, albeit with a probabilistic, rather than deterministic, interpretation.

■ The concept and utility of classical Green functions are important in both classical (of course) and quantum (not as obvious) cases.

DIFFERENCES ■ In classical EM, electric, magnetic, and associated fields

have a specific amplitude (and, for vector fields, vector direction/polarization) at position r and time t (or frequency ©

~), which can be measured, whereas in QEM, these quantities are replaced by operators that depend on r and t or ~. Being operators, they themselves have no intrinsic amplitude or polarization, and cannot be, themselves, measured; they need to act on a state function to produce a value.

■ In QEM, the energy of the field is quantized in multiples of ,'~ whereas in classical EM, the field energy is continuous

and can take any value. ■ Much of QEM revolves around the concept of discrete

energy eigenstates (discrete eigenstates of the energy operator), how electric and magnetic field operators act on these states, the statistics of these states, and how these states propagate in an environment or interact with objects. In the classical case, discrete energy eigenstates are nonexistent (although discrete resonant field modes of, say, a cavity, of course exist). The field energy and power associated with an EM wave, or even an EM mode in a cavity, are certainly important, but these are quantities that can take on a continuous range of values and are usu-ally computed as a secondary calculation after the fields are determined.

■ In the classical case, in the absence of sources (including thermal sources, so, e.g., at ),KT 0= there is no field. In the quantum case, vacuum fluctuations exist that lead to a field having zero mean but nonzero variance.

■ In the classical case, dispersion and absorption are easily accounted for. In the quantum case, both, but particularly absorption, are quite difficult to take into account.

HARMONIC OSCILLATORS: CLASSICAL MECHANICAL AND CLASSICAL EM The concept of a harmonic oscillator (HO) is central to quantum EM. We first discuss a general HO and show that classical cavity modes are equivalent to HOs and then show how to quantize both cases.

THE CLASSICAL MECHANICAL HO The prototypical HO is a system consisting of a mass m and spring with spring constant K. For small deformations the spring will exert a force on the mass F Kx= - by Hooke’s law. Using

/ ,F dV dx= - where V is potential energy, the potential energy profile is clearly / .V Kx 22= This mass-spring system could be literally a mass-spring system or it could be, e.g., a mass-spring model of an atomic lattice (leading to, when lattice vibrations are quantized, phonons). The same quadratic potential energy profile is obtained for a particle moving in a potential V(x) near an equilibrium point.

The classical equation of motion for the oscillator problem, ,F ma= is

d x t x t 02

^ ^h h (1)

where / ,K m0~ = with the solution .cosx t C t0~ z= +^ ^h h Although, for a mass-spring system, it is reasonable to retain the variable x t^ h to represent physical displacement of the oscil-lator, in the next section, we show that classical EM fields can be written as HOs, in which case the corresponding quantity is no longer a displacement of position. Therefore, it is common to replace x t^ h by ,q t^ h which is known as canonical position. The energy (Hamiltonian) of the classical oscillator is the sum of kinetic and potential energies:

0 2 2~= + = +e ^ ^h h o (2)

where p mv mx mq· · = = = (denoting /d dt·

a a= ). Further-more, total energy is found to be / ;H m C1 2 0

2 2~= ^ h energy can take any value because the amplitude C can take any value.

THE CLASSICAL EM CAVITY FIELD AS A HO We now see that the source-free EM field in a cavity is equiva-lent to a HO. We assume a 1D empty lossless cavity for simplic-ity, then generalize this result.

Maxwell’s equations for source-free vacuum are

· , , · , ,t t0 0E r B rd d= =^ ^h h (3)

tE r B r#d 2 2= -^ ^h h (4)

tB r E r0 0#d 2 2n f=^ ^h h (5)

For a 1D cavity along the z-coordinate from z 0= to z L= with perfect electrical conductor walls, we assume the elec-tric field is polarized along the x-coordinate so that EE x= t and .BB y= t The curl equations can be decoupled, leading to, e.g.,

2fn- =^ ^h h (6)

To solve using a separation of variables, assume that , ,E z t E z p t=^ ^ ^h h h so that

E z k E z 02

2 + =^ ^h h (7)

FIGURE 1. A cartoon depiction of a dielectric slab immersed in quantum fluctuations of varying density in all regions of space.

b + =^ ^h h (8)

with the separation constraint .k 02 2b- + = Because ,E z E z L0 0= = = =^ ^h h eigenfunctions normalized as

E z E z dzp L

d=^ ^h h# are

, , , , , ,sin k k L

kz2 1 2 3mk fr= = = =^ ^h h (9)

where k is the mode index, and therefore

, ,E z t p t E z1 k k k

0f = -^ ^ ^h h h (10)

where we have included a constant prefactor for later conve-nience.

The magnetic field is found from the electric field as

, ,B z t q t z

f =^ ^ ^h h h (11)

where we have defined ,p t tq/ o^ ^h h with the dot denoting time differentiation. The Hamiltonian is straightforwardly evaluated as a sum over modes, ,H Hk kR= where

, ,H E z t B z t dz 2 1 1

n = +c ^ ^h hm# (12)

,( ) ( )p t q t 2 1

k k k 2 2 2~= +^ h (13)

where / .ck kk 0 0f~ n= = Comparing with the classical oscillator Hamiltonian (2), we see that a classical EM cavity mode is equivalent to a classical oscillator with unit mass.

THE QUANTIZED EM CAVITY FIELD: CREATION AND ANNIHILATION OPERATORS, AND FOCK/NUMBER STATES Having found the modal solution for the cavity, the classical EM solution is complete. Of course, often one is interested in, say, the field due to a source, in which case the modal solutions can be used to form a Green function and, in turn, the source-driven field in the cavity can be found.

In the quantum case, the modal solutions need to be quan-tized. Because the evolution of energy states plays a promi-nent role in QEM, the quantum mechanical Hamiltonian is of paramount interest. The typical procedure is to start with the classical Hamiltonian and then rewrite that in terms of quan-tum mechanical operators, a procedure known as canonical quantization [3], [4], [7]. Therefore, we start with the classical Hamiltonian and elevate the momentum p t^ h and position q t^ h functions to operators for momentum p tt ^ h and canonical position :q tt ^ h

, .H q q p p m

0 2 2" " ~= +t t t

t t^ h (14)

As we will see, the key ingredient in doing this is to adopt as a basic postulate of quantum mechanics that we enforce that the commutator be

, ,q p qp pq i I'= - =t t t t t t6 @ (15)

where the identity operator I is typically dropped. The impor-tance of this commutator relation (and similar relations that will follow) cannot be overstated, as it implies/enforces the Heisenberg uncertainty principle, upon which quantum theory rests.

We then have quantized electric and magnetic field operators

, ,E z t p t E z1 k k k

0f = -t t^ ^ ^h h h (16)

, .B z t q t z

f =t t^ ^ ^h h h (17)

The operators pt and qt are Hermitian and correspond to observable quantities. An alternative procedure would be to raise the wave equation (6) to operator level and formally solve that equation in a similar manner, enforcing appropriate com-mutators to yield the necessary energy expression.

The energy of the classical HO was previously found to be a continuous quantity, ( / ) .H m C1 2 0

2 2 classical ~= For the quantum

HO, the eigenvalue problem H E} }=t leads to energy eigen-functions, which are Hermite polynomials, and energy eigenval-ues are found to be discrete [10]

, , , , ,nE n 2 1 0 1 2n 0' f~= + =c m (18)

and are equally spaced according to the index n. Because of this, we often write the energy eigenequation as

,H n E nn=t (19)

where ( / )n n 1 2 0'~= +^ h indicates that the state has n quanta of EM energy. This is known as a Fock state or number state, and these states are exceedingly important in QEM. Of course, similar HO problems and number states arise from the time-independent Schrödinger’s equation (SE), where, for a particle in a parabolic potential, the time-independent SE is an eigenvalue equation ,H n E n=t where Ht is (14).

The lowest possible energy state is the vacuum state / ;0 1 2 0'~= ^ h this state has zero photons but has energy

0 0'~= (20)

which is not zero as occurs for the classical oscillator. This zero-point energy arises from the noncommutativity of qt and .pt So, e.g., a crystal lattice has zero-point energy /1 2 k'~^ h even when phonons are absent, and the EM field has zero-point energy

/1 2 k'~^ h even when photons are absent. To understand why the noncommutativity of qt and pt results in zero-point energy, consider that for the classical oscillator, energy E 00 = when the amplitude of oscillation is zero. However, in the quantum case, this would correspond to the state , ,q p0 0= = which is forbidden by the uncertainty principle (which applies to noncommutative operators). Therefore, the vacuum state is necessary for the preservation of the commutators and the self-consistency of the quantum theory.

ENERGY STATES—CREATION AND ANNIHILATION OPERATORS At this point, we have quantized the HO problem, which may represent, e.g., photons or phonons. However, it is useful to introduce new operators [7], [10] (m 1= for the EM case):

, ,a m q i m p

a m q i m p

~ = + = -@t t

tc cm m (21)

which satisfy the commutation relation

, .a a 1=@t t6 @ (22)

The operators at and a@t are not Hermitian, and so, they are not observable/measurable.

It is easy to show that

.H a a 2 1 '~= +@t t tc m (23)

The operator n a a= @t t t is called the number operator, because it counts the quanta (in units of '~). The operator at is called the annihilation or lowering operator, and a@t is called the cre-ation or raising operator, because the action of these opera-tors is

,a n n n 1= -t (24)

.a n n n1 1= + +@t (25)

Because Ht is a nonnegative operator, there is a lowest (vacuum) state devoid of photons, such that .a 0 0=t This is an imposed condition, called a termination condition because it terminates the “ladder” operator .at Furthermore, a given number state can be created from the vacuum state as

= @t^ h (26)

Finally, we can mention that because Ht and nt are Hermitian, number states are orthogonal and form a complete set:

| , | .n n n n Inn n 0

l l / (27)

In the Heisenberg representation, the time evolution of operators satisfies [7]:

, , dt d o t i o t H

' = -t t t^ ^h h6 @ (28)

which leads to free evolution in the absence of other fields/oper-ators/objects, / ,da t dt i a t~= -t t^ ^h h and so, .a t a e0 i t= ~-t t^ ^h h

The final form for the quantized 1D cavity EM field is

, ,E z t i a t a t E z 2

= - @t t t^ ^ ^ ^h h h h6 @/ (29)

, ,B z t a t a t z

f ~ = + @t t t^ ^ ^ ^h h h h6 @/ (30)

with the equal-time commutators (i.e., commutators evaluated at the same time instant)

, , ,a t a t a t a t 0k k k k= =@ @ l lt t t t^ ^ ^ ^h h h h6 6@ @ (31)

, .a t a tk k kkd= @ l lt t^ ^h h6 @ (32)

Accounting for the normalization of the modal field, an ampli-tude constant /E Lk0 0' f~= (V/m), where L is the length of the cavity, is roughly the field amplitude “per photon” because

, ,sinE z t L

=t ^ ^h h (33)

and so, in the one-photon state, the amplitude is .E0 This quan-tity is also the expectation value of the fluctuating vacuum field [see, e.g., (53)], which has recently been measured, and found to be in good agreement with E0 [11]. It can be seen that the quantum aspects of the field/mode are contained in the ampli-tude and time dependence, and that the space dependence is the same for both the quantum and classical fields (that is, both obey the same boundary conditions).

3D QUANTIZED CAVITY FIELD For the 3D empty cavity problem, rather than the 1D wave equation (6), we have

tE r E r 00 0 2

2n f+ =^ ^h h (34)

Rather than ( / ) ,sinE z L kz2k =^ ^h h we now have 3D cavity eigenfunctions ,E rk^ h which incorporate the size and shape of the cavity. These satisfy the usual source-free Helmholtz equation

=^ ^h h (35)

and are normalized as

.dE r E r r3 k k kk$ d=l l^ ^h h# (36)

The field operators are

, ,t i a t a t2E r E r 0

' f ~= - @t t t^ ^ ^ ^h h h h6 @/ (37)

, ,t a t a t2r E rB kk 0

k k k#' d ~ f

= + @t t t^ ^ ^ ^h h h h6 @/ (38)

and the equal-time commutators are the same as (31) and (32) with the scalar k replaced by the triplet k. It can be shown that various scalar components of the electric and magnetic fields are uncorrelated among themselves and are only (inter) corre-lated at .r r= l

The 3D multimode energy operator is

k k k'~= +t t` j/ (39)

where the number operator for each mode is .n a ak k k= @t t t The multimode number states are

... , , , !

,n n n n n n n

1 2 1 2 3 1

f f f f; ; ; / ; ;= @ @t t^ ^h h

(40) such that

, , , | , , , .n n n n n n , , ,n n nn n n1 2 3 1 2 3 1 1 2 2 3 3f f fd d d=l l l l l l (41)

The state | , , ,n n n1 2 3 f contains n1 photons of energy ,1'~ n2 photons of energy ,2'~ and so on. The action of the annihi-lation and creation operators is

, , , , , , , , , , ,a n n n n n n n n n 1j j j j1 2 3 1 2 3f f f f; ;= -t (42)

, , , , , , , , , , .a n n n n n n n n n1 1j j j j1 2 3 1 2 3f f f f; ;= + +@t

3D VACUUM FIELD If we consider free space, rather than a cavity, it is con-ventional to discretize space as a cubic cavity of side L and assume that L is much larger than anything in the cube (atoms and so forth), and that L is also much larger than the longest wavelength. We then solve the usual Helm-holtz equation, applying periodic BCs in each direction,

,e eik ik L=a a+a a^ h , , ,x y za = such that

, , , , , , .L m m m m2 0 1 2k x y z ! ! fr= =a^ h (44)

The resulting (self-adjoint) field operators are

, ,t i V a t e a t e2E r e ,s

k r' f ~= -$ $@ -t t t^ ^ ^h h h6 @/ (45)

V a t e a t e2B r e ,

f ~= -$ $@ -t t t^ ^ ^h h h6 @/ (46)

where e sk indicates the polarization, with ,e e sss sk k

d=l l with the transversality condition .0k e sk

= Spin is indicated by s (a summation over the photon spin index ,s 1 2= merely indicates a summation over the two orthogonal vector polarizations; in the cavity case in the previous section, spin is inherent in the cavity polarization). The polarization vectors form a right-hand-ed coordinate system, / .e e k k1 2k k# ; ; l= = The equal-time commutators are

, , ,a t a t a t a t 0s s s sk k k k= =@ @ l ll lt t t t^ ^ ^ ^h h h h6 6@ @ (47)

, .a t a ts s ssk k kkd d=@ l ll lt t^ ^h h6 @ (48)

DIELECTRIC MEDIA Thus far, we have considered empty cavities. Unlike in classi-cal EM, it can be quite complicated to include the effects of dielectric media in quantum calculations, particularly in the lossy case. Space limitations preclude such a discussion here, although the topic is treated in many QO textbooks as well as, e.g., in [12]–[16].

QUANTUM FLUCTUATIONS OF THE FIELD: EXPECTATION VALUE AND VARIANCE Now that we have the quantized field, what can we do with it? We cannot, e.g., plug in coordinates , tr^ h into , tE rt ^ h and make a plot of electric field, as in the classical case.

Broadly speaking, in QO there are several classes of problems that are often investigated. One class of problem is to determine the statistics of the field, such as the mean, root-mean-square (rms) deviation, and various first- and higher-order correlation functions. This may be done for the vacuum field, the field in an inhomogeneous material environment, or the field interacting with, say, an atom. The examined quantities are similar to those studied in classi-cal statistical EM (e.g., the study of noise, or propagation in random media, urban environments, and so on), although in those cases the fields are not operators, nor are there vacuum fluctuations.

Another class of problem is determining how a quantum state evolves in time or space (e.g., how a quantum bit in a quantum computer evolves and decoheres). In the classi-cal case, we consider how a mode or excited field evolves in time or space, but there is no concept of energy eigenstates evolving (although one could consider how the nonquantized energy or power evolves). The evolution of quantized energy eigenstates involves but is separate from merely the evolution of EM modes.

Furthermore, one could study the interaction of atomic systems and the quantized field, and the effect that the atom’s environment has on, e.g., spontaneous emission rates, atomic population inversion, resonance fluorescence, and so forth. In this section, we consider some statistics of the field, and an example of the evolution of quantized energy eigenstates is dis-cussed in the next section.

The mean value of an observable is the expectation value of the corresponding operator. That is, for an operator ot and a state ,;} the mean value is

| | .o o} }=t t (49)

Furthermore, the standard deviation, i.e., the rms deviation about the mean, is

.o o o o o /2 1 2 2 2

T = - = -t t t t^ h (50)

If the mean is zero, which, as shown here, occurs for the oper-ators introduced thus far, then the rms deviation is simply

As an example, for the HO, we find that

| | | | ,q n q n p n p n 0= = = =t t t t (51)

which holds in any dimension and which is also the case for at and a@t and the operators that are linear combinations of those operators, such as Et and .Bt However, the rms deviations are nonzero, and these are, in fact, the vacuum fluctuations. For example, for the vacuum state,

, ,q p2 20 0

~D = = (52)

and so, these deviations satu-rate the Heisenberg inequal-ity /q p 20 0 'T T = (for nonvacuum states /q p n 1 2n n 'T T $= +^ h / ).2'

The number state n; is an energy eigenstate, so it has de -finite, nonf luctuat ing energ y

( / ) ;E n 1 2n '~= +^ h however, it is not an eigenstate of the field operators ,Et .Bt Therefore, it is not a state of well-defined (fixed, nonfluctuating) electric or mag-netic field and, conversely, the electric and magnetic fields do not have fixed (nonfluctuat-ing) energy. So, if the field is accurately known, the number of photons is not, and vice versa. However, the mean of the square of the field (the mean of intensity) is related to energy (the energy density operator is proportional to )E2t and is not zero. In 1D,

, | | ,sinE z t n E n V n kz2 2 1k2 2

2' f ~= = +t t^ c ` ^h m j h (53)

and, more generally, for a single-mode field,

, .t n 2 1r E rE0

2 2 k' ; ;f ~= +t ^ ^ `h h j (54)

Thus, in a cavity there will be positions where the rms devia-tion vanishes and other points where it is maximized; the field is spread out over the volume, so photons are not generally local-ized. The larger n is, the bigger the fluctuations will be about the zero mean. The expectation value of intensity for n 0= is / ,E V0

2 0'~ f= so again we find that the amplitude of the

vacuum field is ./ V0'~ f

Another quantity of interest is the vacuum-state correlation function [17]:

| , , | ( , , ) ,Im0 0E r E r G r r0 2'

~ d ~ ~= -@ l l l lt t^ ^ ^h h h (55)

where the dyadic Green function is defined as

, , , , , , c

G r r r G r r I r r2

2 # #d d ~ ~ f ~ ~ d- = -l l l^ ^ ^ ^h h h h (56)

where I is the unit dyadic. Equation (55) is essentially the fluctuation–dissipation (FD) theorem for T 0= (otherwise, a factor e1 / k T 1B- '~- -^ ^ hh is needed on the right side). The value of the correlation function at a common spatial position r r= l determines the power spectrum (via the Wiener–Khinchin theorem) of the vacuum field fluctuations. It is interesting, especially coming from a classical EM perspective, to see that vacuum fluctuations, an inherently quantum and seemingly

ephemeral effect, involves the clas-sical Green function. This is not some kind of semiclassical approxi-mation, but a rigorous QED result. It can be mentioned that, in a vacuum, ( , ) ,Re G r r "3^ h

/( , ) .Im k 6G r r I 0 r=^ h

ACCOUNTING FOR MATERIAL DISPERSION AND ABSORPTION The Kramers–Kronig relations [18] require that absorption be accom-panied by dispersion and vice versa. In classical EM, dispersion and absorption are easily accounted for, especially in frequency-domain

quantities. For QEM, this is not the case, because a naive imple-mentation of loss causes the commutators to vanish, violating the Heisenberg uncertainty principle.

For example, in the classical 1D infinite-space case, field dependence is ,ei kz tk~-^ h ,ckk~ = with c being the speed of light in the medium, / ,c c r r0 n f= where c0 is the vacuum speed of light, and ,rn rf are the relative mate-rial values, resulting in the space-time dependence eik z ct-^ h (assuming, of course, that the complex-conjugate term is added to render the expression real-valued). Adding material absorption/loss, ,k k ik= +l m so that the propagation factor is

.e eik z ct k z ct- - -l m^ ^h h

However, in the quantum case, a problem arises. Because k k ik= +l m is equivalent to a complex frequency ,i"~ ~ c- the commutator evolution equation becomes

,dt d a t i i a t~ c=- -t t^ ^ ^h h h (57)

, .a t a e e a t a e e0 0i t t i t t= =@ @~ c ~ c- - -t t t t^ ^ ^ ^h h h h (58)

In this case, ,a t a t e 0t2 "=@ c-t t^ ^h h6 @ as .t "3 Given that ,o p c=t t t6 @ implies uu ,( / )o p c1 2T T $ t the required commutator ,a a 1=@t t6 @ is actually a Heisenberg uncertainty relation (nor-

malized to remove the ).' So, we cannot have , .a t a t 0=@t t^ ^h h6 @ There are a variety of methods that have been devised to deal with dispersion and absorption at the quantum level, although none are simple or straightforward. A thorough review is beyond the scope of this article, and in the following section, we merely mention two widely used models.

METHOD 1: LANGEVIN NOISE SOURCE MODEL One method for solving the problem of absorption is to use a model containing a noise source that has sufficient output even at zero temperature to preserve the commutation relation

, .a a 1=@t t6 @ The concept behind this idea is the FD theorem, which says that when energy is dissipated (turning it into heat), there will be thermal fluctuations about the mean value. This is

There are a variety of methods that have been devised to deal with dispersion and absorption at the quantum level, although none are simple or straightforward.

related to Browian motion and Johnson noise. So, because we want to allow dissipation, we need to have a noise source that will supply energy, which will maintain the commutator. Therefore,

i a t f t 2 2

~ c=- + + t

t t^ ^ ^ ^h h h h (59)

where f tt^ h is an operator-valued Langevin noise source that essentially pumps energy into the system to prop up the operators. With the addition of the Langevin noise source ,f tt ^ h it can be shown that ,a t a t 1=@t t^ ^h h6 @ [2]. The operator f tt ^ h can be interpreted as noise when its expec-tation value vanishes, .f t 0=t ^ h This is a form of Markov-ian damping theory.

An important series of papers [19]–[22] implemented this idea in the following manner. Working in the frequency domain, the natural mode wave equation is

0E r r E r2

2 # #d d ~ ~ f ~ ~- =^ ^ ^h h h (60)

where ,rf ~^ h is the dispersive, complex-valued permittivity. With the advent of absorption, we cannot simply raise the fields in (60) to operator level because the resulting operator ,E r ~t ^ h would be damped and would not preserve the correct commuta-tor relations. Thus, a fluctuating current ,J rnoise ~^ h is added to Ampere’s law:

, , , ,Imr r rJ f0 noise

f ~ ~= lt t^ ^ ^ ^h hh h (61)

, , , , . c

iE r r r rE J2

2 0 noise# #d d ~ ~ f ~ ~ ~n ~- =t t t^ ^ ^ ^h h h h (62)

The canonically conjugate dynamical variables of the field-mat-ter system are , ,f r ~t ^ h , ,f r ~@t ^ h with postulated commutator relations

, , , ,f fr r r rk k kk~ ~ d d ~ ~ d= - -@ l l l ll l t t^ ^ ^ ^h h h h8 B (63)

, , , .f f 0r rk k~ ~ =l ll t t^ ^h h8 B (64)

The result is a field operator:

, , , , ,Im

G r r r f r r

with the field-matter Hamiltonian

, , ,H d dr r f rf 0

$'~ ~ ~ ~= 3 @t t t^ ^h h# # (66)

which is analogous to the simple HO result (23). The ground-energy eigenstate (Fock state) of the free Hamil-tonian satisfies u ,H 0 0=t " , where u u , , ,0 0 0 0 f=" , and, more generally,

uu , ,H 1 1r ri i'~ ~ ~=m m t ^ ^h h , (67)

where the state u ,1 ri ~m^ h indicates that the thm field mode of the nonuniform continuum is populated with a single quanta and that it is vector valued with field component in the ith direc-tion, obtained from the ground state as

u u, ( , ) .{ }f1 0r ri i~ ~= @ m m

A two-quanta Fock state is obtained as

u , , ( , ) , ,f f1 1 0r r r ri j i j~ ~ ~ ~= @ @ m m m ml ll l

t t^ ^ ^h h h " , (69)

and so on. It should be noted that the ~ in (69) is really a continuum

modal frequency, not the Fourier transform frequency. Then, summing over all modes,

E r r G r r

which can be thought of as the Schrödinger-picture field operator ,E rt ^ h

,d H.c.E r E r 0 ~ ~= +

t t^ ^h h# (71)

Therefore, the integral y d~3 m0 is not an inverse Fourier trans-

form integral, it is a mode summation, like ,,sk/ but over con-tinuum modes. Conversion to the time domain is achieved by changing to the Heisenberg picture, where operators At trans-form as

,A t e A e/ / H

iH t iH t Sch

Sch Sch= ' '-t tt t^ h (72)

, , , , ,Im

G r r r f r r

m m ml l l l

This method is a fully quantum theory, although at a mac-roscopic, phenomenological level. One must assume some (perhaps vanishingly small) loss in the system, at least until the end calculation, at which point ( )Im f disappears explic-itly from the result. It has been widely applied to a variety of problems because it is, in many cases, simpler than micro-scopic theories. A critical assessment is provided in [23], where a comparison with a generalized Huttner–Barnett approach is discussed, and also in [24], where the phenom-enological assumptions are derived from a canonical formula-tion. Dissipation and a Langevin noise source model are also discussed in [25].

METHOD 2: BEAMSPLITTER MODEL In method 1, a fluctuating noise source is added to the field to maintain the correct commutator relation. Because it involves the Green function, very complicated geometries can be con-sidered (at least when using a numerically generated Green function). It is particularly well suited for the study of the inter-action of atoms and quantized fields [22], [26]–[31], although it can also be applied to propagation problems as input–out-put relations and to quantum state evolution. However, a somewhat simpler, albeit approximate, method is particularly useful for propagation problems. This involves modeling a dispersive, lossy region of space as consisting of N quantum beamsplitters [12], [32]–[34] (a continuum is then formed, taking ).N "3 Each beamsplitter includes as inputs the propagating field mode, ,b ~t^ h as well as quantized fluctuating noise modes ,ci ~t ^ h , ,Ni 1 f= as depicted in Figure 2. The field bath operators satisfy the bosonic commutation relations

, .c ci j ij~ ~ d d ~ ~= -@ l lt t^ ^ ^h h h6 @ The beamsplitter method used to account for attenuation is

equivalent to solving the (interaction picture) master equation

,dt d t a a a a a a2 2t

c t t t= - -@ @ @t t t t t t t t t t^ ^h h (74)

describing the time evolution of the density operator for a damped HO at zero temperature under the Born–Markov approximations [34], [35]. In (74), c is the damping rate, and a@t and at are the creation and annihilation operators of the oscilla-tor, respectively. This method will be applied in the next section to consider the decoherence of a quantum state as it propagates in the presence of absorption.

QUANTUM STATE TRANSFER, PROPAGATION, AND DECOHERENCE The following example is taken from [36], although the results presented did not appear in that article.

Consider an EM energy incident on a graphene surface. A prism is used to couple free-space energy to surface plasmon polaritons (SPPs) supported by the graphene, and the SPPs then propagate away from the prism region, attenuating as they travel along the surface, as shown in Figure 3. In the quantum case, we must consider a joint photon-SPP state, and as the state propagates, its nature changes from a pure state to a mixed state due to absorption. The following method is approximate, as the graphene quantization assumed lossless graphene, but the realistic loss is incorporated during propagation using the con-tinuum of beamsplitters.

The coupling of the photon and quantized plasmon fields (the SPP quantization is provided in [36]) can be described in the Heisenberg picture by a unitary transformation matrix [37], [38], assuming linear response

h h= = =G G G (75)

where 12 2; ; ; ;c ~ b ~+ =^ ^h h and a ~t ^ h is an annihilat ion operator for the photon f ield which, toget her w it h

@t ^ h sat i sf ies t he boson ic commutat ion r e l a t i o n , .a a

~ d ~ ~= -@ l lt t^ ^ ^h h h6 @ Similarly, b ~t ^ h and b ~@t ^ h are

annihilation and creation operators for the SPP field, which also satisfy bosonic commutation relations. It is shown in [36], [39], and [40] that efficient coupling of incident photons and graphene SPPs is possible.

ε1 > ε0 Prism

FIGURE 3. An incident field inside a prism coupling to quantized SPPs supported by graphene.

b in(ω ) bout(ω,x )

c1(ω ) c2(ω ) cN (ω )

FIGURE 2. A multiple quantum beamsplitter model of a lossy, dispersive medium.

The input state | | |0 ba 0

in }W = interacts with the gra -phene region via the prism, producing the output state | | | ,baout } pW = where | bp is the graphene SPP and | a} is the part of the joint photon-SPP field associated with radiation.

The incoming photon field is assumed to be a superposition of coherent states [37]

| | | | ,N e 0a a i

bin in inina aW = + -z^ h (76)

where // /| | | ! | ,exp nn2a n n2

0! !a a a= - 3 =^ ^h h where N =

cose2 2 /| |2 1 2 z+ a- -^ h is a normalization factor. Note that

| |D 0a a! !a a= ^ h where expD a aa a a= - )@^ ^h h is the displacement operator. Given that ,a a bin out outc b= -) b b ain out outc b= + ) from (75), we have

out out out

where ,sin gb = ,cos gc = setting .0z=

For perfect coupling / ,g 2r=^ h

| | | | | ,N e 00 a b i

baout out out out out a aW = - + z^ h (78)

and the coherent-state superposition is identically transferred to an SPP superposition. Furthermore, if the input is a sim-ple coherent state | | | ,0a bin in in

aW = the output under per-fect coupling is | | |0 a bout out out

aW = -^ h so that the average number of generated SPPs is the same as the average number of input photons, .| |2a For a given input coherent state, the probability of simultaneously exciting n SPPs is given by the Poissonian distribution / !.| |P e n| |

a= a- In the same man-ner, if the input is a number state | | |n 0a binW = then for perfect coupling, | | |n0– , ,a bout out outW = and exactly n SPPs will be excited.

The density operator for the system is | |.out outt W W=t Because we are interested in the SPP itself, we trace-out the unobserved photon mode Trb a

0 out outt t=t t to obtain

| | | | | | | |

sin sin sin sin sin sin sin sinc

g g g g b 0

outt a a a a

where .| |exp cosc g20 2a= -^ h

Equation (79) describes the SPP excited by the photon-coherent superposition. We take this as the initial mixture (at

)x 0= that we want to propagate a distance x along the gra-phene in the presence of material loss and characterize decoher-ence of the state. We obtain [36]

( ) | | | | ,

sin sin sin sin

sin sin sin sin

where /| |k kl =m m and .| |exp sinc x g e2 1 x2 2a= - - l- m^ ^ ^h hh Note that at long times (large x), the SPP moves toward the vacuum state as expected, and at early times (small x), c x 1-^ h and .xb b

0 out out-t tt t^ h

The von Neumann entropy lnS TrV t t=- t t^ h provides a characterization of the loss of coherence of a quantum state [37] (many other quantities can also be used). Although determining lntt is, in general, very difficult, in a diagonal basis we have

,ln lnS xV m m m m=- -+ + - -^ ^ ^h h h (81)

where m! are eigenvalues of the diagonalized density opera-tor. For ,R!a the coherent superposition can be diagonal-ized, leading to [37] / ,NN N c c x2 12

0!m =! ) !^ ^ ^h hh where .exp sinN g e2 2 2 /x2 2 2 1 2

! a= -! l- -m^ ^ h h The resulting entropy

depends only on the input photon-coherent-state value ,a the photon-graphene coupling parameter g, and the graphene damping factor .lm

Figure 4 shows entropy as the SPP propagates for the transverse magnetic (TM) quantized SPP at T 300 K= (the graphene material model is described in [36]). For perfect coupling / ,g 2r= the entropy is zero at x 0= (the known input state is perfectly transferred to the SPP), it rapidly increases as the SPP propagates and the state becomes mixed and then eventually decreases to zero as the state decays toward the vacuum state. For nonperfect coupling and suf-ficiently large a (Schrödinger cat state), the entropy first increases as correlations are established, becomes maximum ( .max lnS 2 0 693V = = ), and decreases as the SPP propa-gates, tending toward the vacuum state. For very small a (e.g., . ),0 1a = the entropy varies with propagation distance in a similar manner but remains very small and appears to be S 0v + on the scale of the plots.

0 50 100 150 200 250 300 350 400 450 500 0

7,000 (T = 0 K)

(T = 0 K) 70

α = 2 α = 5

54.543.532.521.510.5

f = 2 THz T = 300 K

g = π /2 g = 1.2 g = 1 g = 0.8

FIGURE 4. Entropy evolution as the transverse magnetic-quantized SPP propagates for .T 300 K= The scaling of the horizontal axis for T 0 K= is indicated. (Source: S. Ali Hassani Gangaraj; used with permission.)

At ,T 0 K= lower electron scattering decreases lm for the TM mode . ,0 014l =m^ h resulting in longer SPP propagation and a rescaling of the horizontal axis; the horizontal axis limit for T 0 K= is indicated in the figure. In general, as lm increases, the entropy tends toward the vacuum value more rapidly with increasing distance.

CONCLUSIONS The basic aspects of QEM were presented in this article, with an emphasis on the similarities and differences between quan-tum and classical EM. The different objectives and quantities to be measured or computed in quantum and classical regimes were discussed, and the role of the classical Green function in rigorous, fully QED was highlighted. An example of the quan-tum state evolution of a coherent-state superposition in a gra-phene environment was presented.

ACKNOWLEDGMENT The author would like to thank S. Ali Hassani Gangaraj for his helpful comments and for the use of his plot in Figure 4.

AUTHOR INFORMATION George W. Hanson (george@uwm.edu) is with the De -partment of Electrical Engineering and Computer Science, the University of Wisconsin–Milwaukee. His research interests include nanoelectromagnetics, quantum optics, mathematical methods in electromagnetics, and electro-magnetic wave phenomena in layered media. He is a Fellow of the IEEE.

REFERENCES [1] P. W. Milonni, The Quantum Vacuum. San Diego: Academic, 1994. [2] W. Vogel and D.-G. Welsch, Quantum Optics. Weinheim, Germany: Wiley-VCH Verlag GmbH Co. KGaA, 2006. [3] C. C. Gerry and P. L. Knight, Introductory Quantum Optics. Cambridge, U.K.: Cambridge Univ. Press, 2006. [4] J. C. Garrison and R. Y. Chiao, Quantum Optics. Oxford, U.K.: Oxford Univ. Press, 2008. [5] G. Grynberg, A. Aspect, and C. Fabre, Introduction to Quantum Optics. Cambridge, U.K.: Cambridge Univ. Press, 2010. [6] O. Keller, Quantum Theory of Near-Field Electrodynamics. Berlin: Springer-Verlag, 2011. [7] P. W. Milonni, An Introduction to Quantum Optics and Quantum Fluctua-tions. Oxford, U.K.: Oxford Univ. Press, 2019. [8] C. Roychoudhuri, A. F. Kracklauer, and K. Creath, The Nature of Light: What Is a Photon? Boca Raton, FL: CRC, 2019. [9] R. P. Feynman, The Pleasure of Finding Things Out. New York: Basic Books, 1999. [10] R. Shankar, Principles of Quantum Mechanics, 2nd ed. New York: Kluwer/ Plenum, 1994. [11] C. Riek et al., “Direct sampling of electric-field vacuum fluctuations,” Science, vol. 350, no. 6259, pp. 420–423, 2015. doi: 10.1126/science.aac9788. [12] R. J. Glauber and M. Lewenstein, “Quantum optics of dielectric media,” Phys. Rev. A, vol. 43, p. 467, Jan. 1991. doi: 10.1103/PhysRevA.43.467. [13] R. Matloob, R. Loudon, S. M. Barnett, and J. Jeffers, “Electromagnetic field quantization in absorbing dielectrics,” Phys. Rev. A, vol. 52, p. 4823, Dec. 1995. doi: 10.1103/PhysRevA.52.4823. [14] B. Huttner and S. M. Barnett, “Quantization of the electromagnetic field in dielectrics,” Phys. Rev. A, vol. 46, p. 4306, Oct. 1992. doi: 10.1103/PhysRevA. 46.4306. [15] W. C. Chew, A. Y. Liu, C. Salazar-Lazaro, and W. E. I. Sha, “Quantum electromagnetics: A new look, part I,” IEEE J. Multiscale Multiphys. Comput. Techn., vol. 1, pp. 73–84, Oct. 2016. doi: 10.1109/JMMCT.2016.2617018.

[16] W. C. Chew, A. Y. Liu, C. Salazar-Lazaro, and W. E. I. Sha, “Quantum electromagnetics: A new look, part II,” IEEE J. Multiscale Multiphys. Comput. Techn., vol. 1, pp. 85–97, Oct. 2016. doi: 10.1109/JMMCT.2016.2614800. [17] S. Y. Buhmann and D.-G. Welsch, “Dispersion forces in macroscopic quan-tum electrodynamics,” Progr. Quant. Electron., vol. 31, no. 2, pp. 51–130, 2007. doi: 10.1016/j.pquantelec.2007.03.001. [18] J. D. Jackson, Classical Electrodynamics, 3rd ed. New York: Wiley: 1999. [19] L. Knöll, S. Scheel, and D.-G. Welsch, “QED in dispersing and absorbing media,” in Coherence and Statistics of Photons and Atoms, J. Perina, Ed. Wein-heim, Germany: Wiley-VCH, 2001, pp. 1–64. [20] T. Gruner and D.-G. Welsch, “Green-function approach to the radiation-field quantization for homogeneous and inhomogeneous Kramers-Kronig dielectrics,” Phys. Rev. A, vol. 53, p. 1818, Mar. 1996. doi: 10.1103/PhysRevA. 53.1818. [21] H. T. Dung, L. Knöll, and D.-G. Welsch, “Three-dimensional quantiza-tion of the electromagnetic field in dispersive and absorbing inhomogeneous dielectrics,” Phys. Rev. A, vol. 57, p. 3931, May 1998. doi: 10.1103/Phys RevA.57.3931. [22] H. T. Dung, L. Knöll, and D.-G. Welsch, “Spontaneous decay in the pres-ence of dispersing and absorbing bodies: General theory and application to a spherical cavity,” Phys. Rev. A, vol. 62, p. 053804, Oct. 2000. doi: 10.1103/Phys-RevA.62.053804. [23] A. Drezet, “Equivalence between the Hamiltonian and Langevin noise descriptions of plasmon polaritons in a dispersive and lossy inhomogeneous medium,” Phys. Rev. A, vol. 96, p. 033849, Sept. 2017. doi: 10.1103/PhysRevA. 96.033849. [24] T. G. Philbin, “Canonical quantization of macroscopic electromagnetism,” New J. Phys., vol. 12, p. 123008, Dec. 2010. doi: 10.1088/1367-2630/12/12/ 123008. [25] W. E. I. Sha, A. Y. Liu, and W. C. Chew, “Dissipative quantum electromag-netics,” IEEE J. Multiscale Multiphys. Comput. Techn., vol. 3, pp. 198–213, Nov. 2018. doi: 10.1109/JMMCT.2018.2881691. [26] S. Y. Buhmann, D. T. Butcher, and S. Scheel, “Macroscopic quantum electrodynamics in nonlocal and nonreciprocal media,” New. J. Phys, vol. 14, pp. 083034, Aug. 2012. doi: 10.1088/1367-2630/14/8/083034. [27] S. Y. Buhmann, Dispersion Forces I. Berlin: Springer-Verlag, 2012. [28] S. Y. Buhmann, Dispersion Forces II. Berlin: Springer-Verlag, 2012. [29] G. Angelatos and S. Hughes, “Entanglement dynamics and Mollow nonuplets between two coupled quantum dots in a nanowire photonic-crystal system,” Phys. Rev. A, vol. 91, p. 051803(R), May 2015. doi: 10.1103/PhysRevA. 91.051803. [30] D. Martin-Cano, A. Gonzalez-Tudela, L. Martin-Moreno, F. J. Garcia-Vidal, C. Tejedor, and E. Moreno, “Dissipation-driven generation of two-qubit entanglement mediated by plasmonic waveguides,” Phys. Rev. B, vol. 84, p. 235306, Dec. 2011. doi: 10.1103/PhysRevB.84.235306. [31] S. A. Hassani Gangaraj, G. W. Hanson, and M. Antezza, “Robust entangle-ment with three-dimensional nonreciprocal photonic topological insula-tors,” Phys. Rev. A, vol. 95, p. 063807, June 2017. doi: 10.1103/PhysRevA.95. 063807. [32] R. Loudon, The Quantum Theory of Light, 3rd ed. New York: Oxford Univ. Press, 2000. [33] C. M. Caves and D. D. Crouch, “Quantum wideband traveling-wave analy-sis of a degenerate parametric amplifier,” J. Opt. Soc. Am. B, vol. 4, no. 10, pp. 1535–1545, 1987. doi: 10.1364/JOSAB.4.001535. [34] J. R. Jeffers, N. Imoto, and R. Loudon, “Quantum optics of traveling-wave attenuators and amplifiers,” Phys. Rev. A, vol. 47, p. 3346, Apr. 1993. doi: 10.1103/PhysRevA.47.3346. [35] S. J. D. Phoenix, “Wave-packet evolution in the damped oscillator,” Phys. Rev. A, vol. 41, no. 9, pp. 5132–5138, 1990. doi: 10.1103/PhysRevA.41.5132. [36] G. W. Hanson, S. A. Hassani Gangaraj, C. Lee, D. G. Angelakis, and M. Tame, “Quantum plasmonic excitation in graphene and loss-insensitive propa-gation,” Phys. Rev. A, vol. 92, pp. 013828, July 2015. doi: 10.1103/PhysRevA. 92.013828. [37] M. S. Tame et al., “Single-photon excitation of surface plasmon polaritons,” Phys. Rev. Lett., vol. 101, p. 190504, Nov. 2008. doi: 10.1103/PhysRevLett. 101.190504. [38] D. Ballester, M. S. Tame, C. Lee, J. Lee, and M. S. Kim, “Long-range sur-face-plasmon-polariton excitation at the quantum level,” Phys. Rev. A, vol. 79, p. 053845, May 2009. doi: 10.1103/PhysRevA.79.053845. [39] Q. Bao et al., “Broadband graphene polarizer,” Nat. Photon., vol. 5, no. 7, pp. 411–415, 2011. doi: 10.1038/nphoton.2011.102. [40] Z. Fei et al., “Gate-tuning of graphene plasmons revealed by infrared nano-imaging,” Nature, vol. 487, no. 7405, pp. 82–85, 2012. doi: 10.1038/nature11253.