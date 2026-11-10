---
tags:
  - notebooklm-import
notebook: "Sub_Perception"
category: "research"
---

### Skip to main content Advertisement

advanced search
Loading metrics
Open Access
Peer-reviewed
Research Article

### Computational modeling of color perception with biologically plausible spiking neural networks

Hadar Cohen-Duwek,Roles Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Resources, Software, Validation, Visualization, Writing – original draft, Writing – review & editing
Affiliation Neuro-Biomorphic Engineering Lab, Department of Mathematics and Computer Science, The Open University of Israel, Ra’anana, Israel
https://orcid.org/0000-0001-7915-179X

* ⨯
  Hamutal Slovin,Roles Data curation, Formal analysis, Methodology, Visualization, Writing – original draft
  Affiliation The Gonda Multidisciplinary Brain Research Center, Bar-Ilan University, Ramat Gan, Israel
* ⨯
  Elishai Ezra Tsur Roles Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Supervision, Validation, Visualization, Writing – original draft, Writing – review & editing
* E-mail: [elishai@nbel-lab.com](mailto:elishai@nbel-lab.com)
  Affiliation Neuro-Biomorphic Engineering Lab, Department of Mathematics and Computer Science, The Open University of Israel, Ra’anana, Israel
   [https://orcid.org/0000-0003-1304-8022](mailto:elishai@nbel-lab.com)
* [⨯](mailto:elishai@nbel-lab.com)

### Computational modeling of color perception with biologically plausible spiking neural networks

* Hadar Cohen-Duwek,
* Hamutal Slovin,
* Elishai Ezra Tsur
  x
* Published: October 27, 2022
* [https://doi.org/10.1371/journal.pcbi.1010648](mailto:elishai@nbel-lab.com)
* [Article](mailto:elishai@nbel-lab.com)
* [Authors](mailto:elishai@nbel-lab.com)
* [Metrics](mailto:elishai@nbel-lab.com)
* [Comments](mailto:elishai@nbel-lab.com)
* [Media Coverage](mailto:elishai@nbel-lab.com)
* [Peer Review](mailto:elishai@nbel-lab.com)
* [Reader Comments](mailto:elishai@nbel-lab.com)
* [Figures](mailto:elishai@nbel-lab.com)

#### Figures

#### Abstract

Biologically plausible computational modeling of visual perception has the potential to link high-level visual experiences to their underlying neurons’ spiking dynamic. In this work, we propose a neuromorphic (brain-inspired) Spiking Neural Network (SNN)-driven model for the reconstruction of colorful images from retinal inputs. We compared our results to experimentally obtained V1 neuronal activity maps in a macaque monkey using voltage-sensitive dye imaging and used the model to demonstrate and critically explore color constancy, color assimilation, and ambiguous color perception. Our parametric implementation allows critical evaluation of visual phenomena in a single biologically plausible computational framework. It uses a parametrized combination of high and low pass image filtering and SNN-based filling-in Poisson processes to provide adequate color image perception while accounting for differences in individual perception.

#### Author summary

In this work, we propose a biologically plausible computational framework for color perception. The model initiates with simulating the responses of single and double opponent cells to a visual stimulus in chromatic and achromatic channels. The double opponent and the intensity channels are reconstructed using spiking neural networks and linearly combined with the single opponent channels to provide the perceived image. Our model allows the attribution of perceptual differences to the proportions between the single and double opponent cells’ activity, while being general enough to account for a wide range of visual phenomena including color constancy, color assimilation, and ambiguous color perception.
**Citation:** Cohen-Duwek H, Slovin H, Ezra Tsur E (2022) Computational modeling of color perception with biologically plausible spiking neural networks. PLoS Comput Biol 18(10): e1010648. https://doi.org/10.1371/journal.pcbi.1010648
**Editor:** Tianming Yang, Chinese Academy of Sciences, CHINA
**Received:** April 10, 2022; **Accepted:** October 10, 2022; **Published:** October 27, 2022
**Copyright:** © 2022 Cohen-Duwek et al. This is an open access article distributed under the terms of the [Creative Commons Attribution License](http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
**Data Availability:** The project's Github with the complete codebase available in: <https://github.com/NBELab/PLoS_Comp_2022>.
**Funding:** This work was supported by The Open University of Israel Research Grant, which was granted to E.E.T. E.E.T. is a senior faculty member at The Open University of Israel. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.
**Competing interests:** The authors have declared that no competing interests exist.

#### Introduction

One of the most fundamental challenges in modeling human cognition is linking high-level experiences to low-level biologically plausible computational models. Advances in computational neuroscience, cognitive science, and artificial intelligence continually power our attempts to shed light on this grand challenge. One of the most interesting aspects of human cognition is visual perception. Visual perception initiates with the derivation of light intensity and color by retinal circuitry, which is propagated to the Lateral Geniculate Nucleus (LGN), finally advancing to the primary visual cortex (V1) and on to higher processing areas [[1](https://journals.plos.org#pcbi.1010648.ref001)]. Interestingly, while visual information is represented as Spatio-temporal edges, the perceived field of view features complete colorful filled-in surfaces, indicating that the brain reconstructs visual constructs from edges [[2](https://journals.plos.org#pcbi.1010648.ref002)]. Fronting extensive empirical research, two prominent theories have been suggested to govern perceptual filling-in: (1) **Symbolic or cognitive theory** according to surfaces’ color and shape are represented in higher- areas of visual processing; and the (2) **Isomorphic theory** , according to surfaces emerge from activation spreads from edges to the centers across the retinotopic map. This activation pattern propagates across a two-dimensional grid of neurons, representing a planar field of view. The underlying neural mechanism of perceptual filling-in remains unclear, as experimental evidence supports both hypotheses [[3](https://journals.plos.org#pcbi.1010648.ref003)]. In visual perception modeling, chromatic and achromatic receptive fields are typically modeled using spatial derivatives kernels [[4](https://journals.plos.org#pcbi.1010648.ref004)]. Recently, we proposed biologically plausible Poisson-driven perceptual filling-in Spiking Neural Networks (SNN), demonstrating the reconstruction of images from their gradients [[5](https://journals.plos.org#pcbi.1010648.ref005)]. SNNs are considered biologically plausible as they feature spiking neurons and local learning rules without a Central Processing Unit (CPU) nor a register-based memory.
In V1, visual data is represented as Spatio-temporal edges by color-responsive single- and double-opponent neurons. While single opponent cells merely report the color of their receptive field, double-opponent report chromatic edges and are orientation-selective [[6](https://journals.plos.org#pcbi.1010648.ref006)–[10](https://journals.plos.org#pcbi.1010648.ref010)]. Both single and double opponent neurons were hypothesized to govern color perception. Recently, Shapely and Colleagues suggested that while single-opponent neurons play a vital role as spatial integrators at static low color contrast visual scenes, at higher contrast, and where colors dynamically change, double-opponent neurons govern perception [[7](https://journals.plos.org#pcbi.1010648.ref007)]. Visual perception also comprises various processing pathways, combining chromatic and achromatic edge processing. While the achromatic pathway reports on color-oblivious edges, the chromatic pathway combines Red/Green and Yellow/Blue edges.
In this work, we extend our previous model, proposing an isomorphic theory-driven biologically plausible SNN for the reconstruction of colorful images from retinal inputs (Fig 1). We introduced a colored image (stimulus) to chromatic and achromatic channels, comprising models of single and double opponent neurons. The derived chromatic and achromatic edges were introduced into recurrent SNNs, implementing evidence-based feedback (horizontal) connections [[11](https://journals.plos.org#pcbi.1010648.ref011),[12](https://journals.plos.org#pcbi.1010648.ref012)] to reconstruct the embedded surfaces. Finally, the resulting surfaces were linearly combined with single opponent outputs to produce a perceived image. A weighting scheme controls the dominance of each channel in the perceived image, as was described by Shapley and colleagues [[7](https://journals.plos.org#pcbi.1010648.ref007)].
Download:

* [PPT PowerPoint slide](https://journals.plos.org#pcbi.1010648.ref007)
* [PNG larger image](https://journals.plos.org#pcbi.1010648.ref007)
* [TIFF original image](https://journals.plos.org#pcbi.1010648.ref007)
  Fig 1. A biological plausible computational framework for color perception.
  The model initiates with simulating the responses of single and double opponent cells to a visual stimulus in chromatic (red-green and blue-yellow) and achromatic channels. The DO and the intensity channels are reconstructed using SNNs and linearly combined with the SO channels to provide the perceived image. Image by Alexander Ivanov (Pixabay).
   [https://doi.org/10.1371/journal.pcbi.1010648.g001](https://journals.plos.org#pcbi.1010648.ref007)
  We further used our model to demonstrate and critically explore three important visual phenomena: (1) **color constancy** , in which an object’ perceived color is perceived under varying lighting conditions [[13](https://journals.plos.org#pcbi.1010648.ref013)]; (2) **the color assimilation grid illusion,** in which the color of a grid is assimilated into the underlying black and white surfaces; and (3) **ambiguous color perception** (e.g., #TheDress and #TheShoe). Interestingly, perceptual filling-in-driven visual illusions, featuring chromatic and achromatic phenomena, have been long known for shedding new light on neural mechanisms in the visual system [[14](https://journals.plos.org#pcbi.1010648.ref014)–[19](https://journals.plos.org#pcbi.1010648.ref019)]. For example, extensive research has been conducted on color constancy [[20](https://journals.plos.org#pcbi.1010648.ref020)], deciphering it as a result of either high-level processing with which color is estimated in accordance with prior experience [[21](https://journals.plos.org#pcbi.1010648.ref021),[22](https://journals.plos.org#pcbi.1010648.ref022)], or low-level retinal [[23](https://journals.plos.org#pcbi.1010648.ref023)] and V1 [[24](https://journals.plos.org#pcbi.1010648.ref024)–[26](https://journals.plos.org#pcbi.1010648.ref026)] processing. Our work provides a unique biological plausible computational framework in which these intricate visual phenomena can be critically and exploratory examined.

#### Methods

##### Ethics statement

All experimental procedures were approved by the Animal Care and Use Guidelines Committee of Bar-Ilan University, supervised by the Israeli authorities for animal experiments, and conformed to the National Institutes of Health (NIH) guidelines.

##### The neural engineering framework

SNNs comprise a network of interconnected spiking neurons [[27](https://journals.plos.org#pcbi.1010648.ref027)]. In this work, we utilized the Neural Engineering Framework (NEF) [[28](https://journals.plos.org#pcbi.1010648.ref028)], a theoretical framework with which spiking neurons can be used to design functional large-scale neural networks. With NEF, numerical high-dimensional constructs (e.g., vectors and functions) can be loosely encoded, decoded, and transformed. Following NEF, a spikes train *δ* is defined using: (1) where *i* is the neuron identifying index, x is the stimulus, *e* is the neuron’s preferred stimulus (encoding vector), *G* is a spiking neuron model (e.g., Leakey Integrate and Fire (LIF) neuron model), *α* is a gain term, and *J* *b* is a fixed background current.
An encoded high-dimensional numerical construct (vector), can be linearly decoded as using: (2) where *N* is the number of spiking neurons, *a* *i* (x) is the postsynaptic low-pass filtered response of neuron *i* to stimulus x and *d* *i* is a representational decoder. Representational decoders are optimized to reconstruct x using least squared optimization. Eqs [1](https://journals.plos.org#pcbi.1010648.e001) and [2](https://journals.plos.org#pcbi.1010648.e003) describe the encoding and decoding of vectors with neural spiking activity within neuronal ensembles. Propagation of data from one ensemble to another can be realized through weighted synaptic connections (transformational decoders). Transformational decoders can be optimized such as *x* could be transformed to an arbitrary *f* (x). Dynamic behavior is realized by recurrently connecting neuronal ensembles (thus, integrating NEF’s representation and transformation principles). NEF can be used to resolve the dynamic: (3) where *u* ( *t* ) is input from another neural ensemble, defining a recursive connection that resolves the transformation: *τ* ∙ *f* (x)+x, where *τ* is the synaptic time constant. A detailed description of NEF is available in [[28](https://journals.plos.org#pcbi.1010648.ref028)].

##### Single and double opponent channels

Our model initiates by simulating the responses of single and double opponent cells to a visual stimulus [[29](https://journals.plos.org#pcbi.1010648.ref029)] (Fig 1). We followed the central dogma in which the visual system utilizes separate channels for processing achromatic data and colors of different wavelengths [[9](https://journals.plos.org#pcbi.1010648.ref009)]. For the chromatic pathway, we have implemented two pathways: *L* / *M* , and ( *L* + *M* )/ *S* , where *L* represents a long light wavelength (red), *M* represents an intermediate light wavelength (green), and *S* represents a short light wavelength (blue). We used the RGB channels of the input image to describe the *L* , *M* , and *S* color intensities. The achromatic pathway comprises a Low Pass Filter (LPF) and a derivative kernel (following the on-center—off-center receptive fields of retinal ganglion cells).
The three RGB color channels of the visual stimulus were converted to two red-green *SO* *RG* and blue-yellow *SO* *BY* single opponent channels, and the achromatic (grayscale) channel, denoted *I* *LPF* , using: (4) (5) (6) where *G* ( *x* , *y* , *σ* ) is the normalized Gaussian Kernel: in which '\*' denotes the convolution operator, simulating the low-pass properties of the single opponent channel [[7](https://journals.plos.org#pcbi.1010648.ref007)], [[8](https://journals.plos.org#pcbi.1010648.ref008)], [[30](https://journals.plos.org#pcbi.1010648.ref030)]; and *RG* , *BY* (the chromatic channels), and *I* (the achromatic channel) were defined using: (7) where *M* *opp* is the color opponent transformation matrix in which *a* = 0.2989, *b* = 0587, and *c* = 0.114. The spatial dimension *s* of the gaussian kernel (measured in pixels) is , where *W* was set to 21 during model execution and to 11 or 21 during parameter evaluation (see parameter evaluation below for further details).
The chromatic double-opponent channels: *DO* *RG* and *DO* *BY* as well as the achromatic derivative signal *I* *on* − *off* were derived by convolving each chromatic single opponent channel with the Discrete Laplacian operator , constituting: (8) (9) (10)
Following [Fig 1](https://journals.plos.org#pcbi-1010648-g001), *I* on−off, *DO* *RG* and *DO* *BY* , *SO* *RG* , *SO* *BY* and *I* *LPF* were represented with spiking neurons using [Eq 1](https://journals.plos.org#pcbi.1010648.e001) and introduced into SNNs for surface filling-in.

##### Perceptual Filling-in with spiking neurons

In V1, visual data is represented as Spatio-temporal edges, constituting the image’s gradients. The perception of filled surfaces from image gradients can be described using the diffusion/heat equation: (11) where is the gradient operator, is the Laplacian operator, *div* is the divergence ( ), *I* is the perceived image (i.e., the reconstructed image), and *I* *input* is the input image (stimulus) [[31](https://journals.plos.org#pcbi.1010648.ref031)], [[32](https://journals.plos.org#pcbi.1010648.ref032)]. In the diffusion process, the inactive center of the V1-represented stimulus is gradually filled-in with neuronal activity, supporting the perception of light intensity at the center of the outlined stimulus. This diffusion-governed perceptual filling-in is often referred to as ’immediate’[[2](https://journals.plos.org#pcbi.1010648.ref002)], following experimental evidence supporting the almost instantaneous reconstruction of a perceived image [[17](https://journals.plos.org#pcbi.1010648.ref017)], [[18](https://journals.plos.org#pcbi.1010648.ref018)], [[33](https://journals.plos.org#pcbi.1010648.ref033)]. This fast dynamic allows the dismissal of , the diffusion equation’s dynamic phase. [Eq 11](https://journals.plos.org#pcbi.1010648.e016) can be therefore simplified to the steady-state Poisson equation: (12)
While the Poisson equation can be realized numerically by various techniques [[34](https://journals.plos.org#pcbi.1010648.ref034)–[36](https://journals.plos.org#pcbi.1010648.ref036)], we recently demonstrated a biologically plausible solution using NEF-defined recurrent SNNs [[5](https://journals.plos.org#pcbi.1010648.ref005)]. Our recurrent SNN iteratively solves the Poisson equation by rearranging [Eq 11](https://journals.plos.org#pcbi.1010648.e016), as: , which in conjunction with [Eq 3](https://journals.plos.org#pcbi.1010648.e004), allows the definition of the recurrent connection: (13)
Eq 13 can be iteratively defined as: (14)
Following [Eq 14](https://journals.plos.org#pcbi.1010648.e024), the perceived image *I* *k* can be iteratively reconstructed in every timestep *k* .
Eq 14 can be discretized by the Discrete Laplace operator *L* : (15)
Finally, the image *I* ( *x* , *y* ) *k* (the perceived pixel in ( *x* , *y* ) at time step k) can be derived using: (16)
In [Eq 16](https://journals.plos.org#pcbi.1010648.e026), each neuron has four recurrent connections with its four neighboring cells and one recurrent connection with itself. In each time step, neural activity is spread to his adjacent neurons. Here, we realized [Eq 16](https://journals.plos.org#pcbi.1010648.e026) using a recurrently connected single-layer SNN. Therefore, this connectivity scheme can be referred to as a horizontal neural connection [[11](https://journals.plos.org#pcbi.1010648.ref011),[12](https://journals.plos.org#pcbi.1010648.ref012)]. In this work, we further utilize this SNN to demonstrate color perception and the perception of visual artifacts.

##### Image perception

For each color opponent channel as well as the intensity channel, the above filling-in process was applied separately. Eqs [17](https://journals.plos.org#pcbi.1010648.e027)–[19](https://journals.plos.org#pcbi.1010648.e029) describe the inputs for [Eq 12](https://journals.plos.org#pcbi.1010648.e021). Solving each equation yields the filled-in surfaces *O* *RG* , *O* *BY* , *O* *I* for the RG, BY and Intensity opponent channels, respectively.
(17)(18)(19)The perceived image is generated by combining the reconstructed achromatic pathways *P* *I* , with the single and double opponent channels in each color pathway ( *P* *RG* , *P* *BY* ): (20) (21) (22) where *P* *RG* , *P* *BY* are the perceived results of the red-green, and blue-yellow channels, respectively; *α* *c* , *β* *c* , *α* *i* and *β* *i* are weight parameters, indicating the weighted contribution of each channel to the perceived result. In this study, we defined *β* = 1− *α* , allowing us to solely control *α* in the simulations.
To transform the perceived result to an RGB image, the three opponent channels are converted back to RGB representation using the inverse opponent transformation: (23)
We used the Learning Perceptual Image Patch Similarity (LPIPS) metric to measure the perceptual distance between the visual stimulus and the reconstructed image. In LPIPS, deep visual features are extracted from pairs of images derived from ImageNet-trained neural networks [[37](https://journals.plos.org#pcbi.1010648.ref037)] and compared using a weighted L2 distance (Euclidean distance). Weights were adjusted such that this similarity measure agrees with human perceptions of patch similarity [[38](https://journals.plos.org#pcbi.1010648.ref038)], based on the Berkeley Adobe Perceptual Patch Similarity (BAPPS) dataset. BAPPS contains two-alternative-force-choice (2AFC) and just-noticeable-difference (JND) judgment experiments. As part of the 2AFC experiment, two distortions are applied to a reference image patch, and observers must choose which distortion is closest to the original. In the JND experiment, the observer is asked to determine if two patches—one reference and one distorted—are the same or different.
The LPIPS distance is defined as: (24) where *O* *i* and *P* *i* are the RGB values of pixel *i* in the original and the predicted (reconstructed) image, respectively; *N* is the number of pixels, and *Φ* *l* (∙) donates the feature activations at the *l* -th layer of the AlexNet [[39](https://journals.plos.org#pcbi.1010648.ref039)] network *Φ* . Weights *w* *l* were optimized using the Berkeley Adobe Perceptual Patch Similarity (BAPPS) dataset to match human perception; Perceptual distance *d* was calculated by using the first five layers of AlexNet.

##### Model simulation

To evaluate our SNNs-driven model for color perception, we implemented the model using the Nengo neural compiler (implemented with Python), with which high-level descriptions can be translated to low-level spiking neurons [[40](https://journals.plos.org#pcbi.1010648.ref040)]. The model was directly introduced with the single and double opponent cells ( *SO* and *DO* , Eqs [4](https://journals.plos.org#pcbi.1010648.e005)–[6](https://journals.plos.org#pcbi.1010648.e007),[8](https://journals.plos.org#pcbi.1010648.e013)–[10](https://journals.plos.org#pcbi.1010648.e015)) derived from RGB images. For the *DO* cells, the spatial extents of the filters were used to represent a high-pass filter (Laplacian), and for the *SO* cells, we chose a low-pass filter with a relatively large support (wide spatial Gaussian profile). In simulations, the spatial parameters of the Gaussian kernel were *W* = 21 pixels and *σ* = 5 (Eqs [4](https://journals.plos.org#pcbi.1010648.e005)–[6](https://journals.plos.org#pcbi.1010648.e007)). Each pixel was encoded with five ensembles, each constituting 20 spiking neurons, representing five channels ( *SO* *RG* , *SO* *BY* , *DO* *RG* , *DO* *BY* and *I* on−off).Time constant *τ* ([Eq 16](https://journals.plos.org#pcbi.1010648.e026)) was set to 0.25 in all simulations. Neurons were defined with a Spiking-Rectified-Linear activation function [[41](https://journals.plos.org#pcbi.1010648.ref041)]. Simulations were accelerated on a 12GB NVIDIA Tesla K80 GPU using the OpenCL-based Nengo Simulator [[40](https://journals.plos.org#pcbi.1010648.ref040)].

##### Voltage-sensitive dye imaging and analysis

Imaging and experimental procedures were fully described in [[42](https://journals.plos.org#pcbi.1010648.ref042)]. Briefly, a monkey (6 years old 13 kg male macaque monkey ( *Macaca fascicularis* )) was trained on a fixation task while presented (21-inch CRT monitor; 85 Hz refresh rate; 100 cm from the monkey’s eyes) with black (CIE-xy = 0.279, 0.266) or red (CIE-xy = 0.616, 0.341) squared surfaces of equal luminance (15.5 cd/m2), background (CIE-xy = (0.279, 0.28); luminance (7.3 cd/m2) and a variable size. We used a 3 to 4 seconds prestimulus (varied randomly) and a 300 ms stimulus time. The center positions of all surfaces in the visual field were identical (stimulus fixation within 2° about the fixation point; verified using eye movement monitoring). The monkey was anesthetized, ventilated, and anchored (cemented to the cranium with dental acrylic) using two 25mm cranial windows, bilaterally placed over the primary visual cortices. The visual cortex was exposed (3–6 mm anterior to the Lunate sulcus) and stained using Oxonol voltage-sensitive dyes. We used Micam Ultima’s imaging system, providing a resolution of 104 pixels at 10 kHz, each pixel summing the neural activity from about 500 neurons, located at the upper 400 μm of the cortex. VSDI maps were averaged at 60–100 ms after stimulus onset. We computed spatial cuts crossing through the edges and center of the activation patches (an illustration of the spatial profile for the 1° square is shown in Fig 2B (top). VSDI responses (Fig 2A) were averaged over the width of the spatial cuts resulting in the spatial activity profiles shown in Fig 2B.
Download:

* PPT PowerPoint slide
* PNG larger image
* TIFF original image
  Fig 2. V1 recording and simulation results during perceptual filling-in of black and red squared surfaces.
  A. Averaged early (60–100 ms following stimulus onset) Macaque V1 VSDI-measured neural activity map following exposure to black (left) and red (right) squared surfaces with various sizes (0.5°– 8°) (see [Methods](https://journals.plos.org#sec002)); B. Spatial profiles crossing through the edges and center of the V1 activation patches. The continuous vertical line marks the peak activation position in the 0.5° square response profile, which corresponds to the center of square in larger stimuli. Responses to a 2° square are marked with vertical dashed lines; C. Model-derived results for the reconstruction of black and red squared surfaces with various sizes squares; D. Cross-sectional profiles of each reconstructed square along the x-axis.
   [https://doi.org/10.1371/journal.pcbi.1010648.g002](https://journals.plos.org#sec002)

#### Results

##### Filling-in V1 recording and simulation

Macaque V1 neural responses to visual stimuli of black and red squared surfaces in varying sizes, ranging from 0.5° to 8° visual degrees, were recorded using VSDI (originally reported in [[42](https://journals.plos.org#pcbi.1010648.ref042)]) (Fig 2A). We found that the spatial V1 neural responses pattern for small surfaces (0.5° and 1°) were ’filled-in’, corresponding to the stimulus topographic map. Neural responses for larger surfaces (2° to 8°) showed ’un-filled’ areas, indicated by the low response amplitude at the surface’s center. Furthermore, we derived spatial cross-sectional measurements through the edges and center of the activation patches (an illustration of the spatial profile for the 1° square is shown in Fig 2B, top). VSDI response was averaged over spatial cross-sections resulting in an activity profile, depicted in Fig 2B. For comparison, we used our image reconstruction model (Fig 1) to reconstruct five squares ranging from 5 to 80 pixels in length, each corresponding to a different visual modality used in the experimental setting (Fig 2C). Since VSDI recorded signals from the 2nd and 3rd V1 layers, which are double opponent cells dominant [[6](https://journals.plos.org#pcbi.1010648.ref006)], we set *α* *i* and *α* *c* to 1 for reconstruction. Briefly, these cortical layers are imaged using VSDI at high spatial resolution (mesoscale, 502 μm2/pixel) and temporal resolution (100 Hz). While VSDI acquired signals emphasize subthreshold membrane potentials, it reflects supra-threshold membrane potentials (i.e., spiking activity). The main advantage of this technique is the combination of wide-field imaging with high spatio-temporal resolution, enabling the visualization of the whole cortical activity patterns evoked by a visual stimulus. As a result, in this section, the simulation solely considers the double opponent cells channel. In the reconstructed surfaces, only the small 5- and 10-pixels squares were completely filled-in. The centers of the larger reconstructed squares were unfilled, corresponding to the neuronal inactive patches shown in VSDI. We measured the spatial activation profiles across the reconstructed squares (along the x-axis) and applied a 1D Gaussian filter with *σ* = 2 to smooth the responses (Fig 2D). Our cross-sectional simulation results correspond to the experimental neuronal activation profiles we experimentally obtained in V1. We further compared the reconstructed VSDI profiles with the recorded VSDI profiles using linear regression. The stimulus edges in each VSDI profile were aligned (across the x-axis of each profile) to its corresponding simulated profile and *R* 2 and its corresponding p-value were derived (S1 Fig). Results shows *R* 2 of 0.974, 0.824, 0.575, 0.938 and p-values of 1.3∙10−55, 2.5∙10−27, 4.7∙10−14, 3.3∙10−45 for the 0.5°, 1°, 2° and 3° profiles, indicating a good model fit. *R* 2 was not calculated in the 8° profile since the signal was essentially noise.

##### Color perception

We evaluated our color perception model by reconstructing four color images: a photograph of a colored face, an image of a building with reflective surfaces, a dimmed lighted photograph of the Louvre Museum, and a synthetic red square. The resulting reconstructions with various values of *α* *i* , *β* *i* , *α* *c* , and *β* *c* , are shown in Fig 3. As a general guideline, when *α* is high, and *β* is small, the reconstructed colors and intensities demonstrate high pass filtering as high spatial frequencies are mostly reconstructed. For example, when *α* *i* is high, the reflection of the Louvre in the water is clearer as the image’s finer details are better exposed. Increasing *β* (and reducing *α* ) instigates saturated colors and blurry edges. The synthetic red square image provides an intuitive illustration of this high- and low-pass filtering balance. When *α* *c* = 1, the red square is not entirely filled, and its color edges are enhanced. Since the model exhibits high-pass color filtration, the image’s complementary color–cyan–appears at the square’s exterior edges. As *α* *c* decreases, the square’s center is filled with a reddish hue. Interestingly, the reconstructed images are most similar to the original images when *α* *i* and *α* *c* are 0.5 indicating the important contribution of the different color channels to adequate image perception. We evaluated the importance of the filling-in component by removing it from the proposed perceptual pipeline. Without a recurrent connection between the SO and DO channels, our model is simplified to a combination of low- and high-pass filters where most of the band-pass signals (intermediate frequencies) are absent. When *α* *i* and *α* *c* equal 1, the resulted reconstruction is a high-pass filter of the image (the image’s Laplacian), whereas decreasing alphas merely adds low frequencies to the results (S2 Fig **)** .
Download:

* PPT PowerPoint slide
* PNG larger image
* TIFF original image
  Fig 3. Image reconstruction.
  Visual stimuli are presented in the first row and the reconstructed images are shown below, generated with various values of *α* *c* , *β* *c* , *α* *i* and *β* *i* (aligned to the left of the corresponding images). LPIPS scores are shown on the right.
  https://doi.org/10.1371/journal.pcbi.1010648.g003
  The model’s reconstructed and original images were further compared using the LPIPS distance (Fig 3, right). As expected from visual inspection, the LPIPS distances for all four images were found lowest when *α* *i* = 0.5 and *α* *c* = 0.5, indicating the importance of multiple channel integration. Finally, we further evaluated the proposed model with a non-spiking version (a conventional neural network). A SNN is considered biologically plausible as is it uses spikes to represent and transform data through local learning rules (Eq 2). However, we can analytically solve the mathematical transformation our SNN strives to approximate. Under visual inspection, the reconstructed results of the spiking and non-spiking neural networks are similar, pointing out the capacity of our model to exhibit relevant neural approximations. Interestingly, when measuring LPIPS distances during models’ convergence, the SNN outperform the conventional neural network, consistently reporting lower distances (S3 Fig). This might be due to the noise-introductory effect, which is inherit in SNNs being a neural approximation, to the resolved diffusion process (Eq 16). While here we used a SNN to increase the biological plausibility of the model, the improved diffusive filling-in process may be an interesting topic for future work.

##### Color constancy

Color constancy lies at the foundation of numerous visual illusions [[20](https://journals.plos.org#pcbi.1010648.ref020)], [[43](https://journals.plos.org#pcbi.1010648.ref043)]. In this section, we used the cube illusion created by Beau Lotto [[44](https://journals.plos.org#pcbi.1010648.ref044)] to demonstrate how our SNN-driven biological plausible model can predict perceived colors under different illumination, as well as filter ambient illumination. The first row in Fig 4A illustrates three variations of the cube illusion, illuminated by natural, yellow, and violet\bluish lights (Fig 4A **,** left to right). When illuminated by natural (or white) light, the perceived color of each of the two marked patches (Fig 4A, left cube) is profoundly different, despite having the same color (ground truth; GT). A similar disparity between the perceived and GT colors is also apparent when yellow, and violet\bluish illuminations are used (Fig 4A, middle and right cubes). We reconstructed these images with our model with various values of *α* *i* , *β* *i* , *α* *c* , and *β* *c* (Fig 4A **,** 2nd to 5th row). We were able to predict with our model the perceived color (i.e., the perceived and the GT colors are similar) under different illuminations. Furthermore, using different chromatic parameters, we could filter the ambient illumination in and out.
Download:

* PPT PowerPoint slide
* PNG larger image
* TIFF original image
  Fig 4. Reconstruction of the cube illusion.
  A. The original cube images under three illuminations: natural, yellow, and blue (First row). The model predictions with different sets of chromatic and achromatic parameters are shown in rows 2–5; B. Comparison between the true color (marked with an asterisk) and the predictions of the model with *α* *c* = 1 and *α* *c* = 0.7. Results are presented in u’v’ (CIELu’v’) color space. Each color circle surrounds the true and predicted colors of a sampled pixel in the patch. Black lines represent cone-opponent axes, S/(L + M) and L/(L + M). The intersection of the lines represents the achromatic point.
  https://doi.org/10.1371/journal.pcbi.1010648.g004
  We further evaluated color constancy by observing the model’s results in the perceptually uniform CIELu’v’ color space [[45](https://journals.plos.org#pcbi.1010648.ref045)]. We assessed the reconstructed cube illusion under natural light with different chromatic parameters ( *α* *c* = 1 and *α* *c* = 0.7) and a constant achromatic alpha ( *α* *i* = 0.5) (Fig 4B **)** . While the patches’ true colors are identical, we found that on the CIELu’v’ color space, when *α* *c* = 1, the predicted colors shift further away from each other as the upper patch becomes reddish and the lower patch’s orange hue enhances. Under yellow illumination, while the yellow patch remains the same, when *α* *c* = 1, the blue shade of the blue patch’s predicted color (gray in the original image) enhances, and the orange patch becomes reddish (Fig 4C **)** . The predicted color of the cube under blueish illumination, when *α* *c* = 1, shows that while the blue patch remains the same, the gray patch becomes yellowish, and the purple patch becomes reddish (Fig 4D). Exploring the results of the yellowish and blueish illuminations (Fig 4C and 4D, respectively), we can see that the colors at *α* *c* = 0.7 are in between the original and the predicted colors at *α* *c* = 1.

##### Color assimilation grid illusion

To demonstrate the importance of low-pass single opponent cells, we reconstructed the color assimilation grid illusion in which a selective colored grid is superimposed over an original grayscale image, resulting in a perceived color image [[46](https://journals.plos.org#pcbi.1010648.ref046)]. The color assimilation grid illusion is demonstrated in Fig 5 with a photograph of a colored face and a synthetic red square. We used two images representing two different grids’ densities. Color assimilation is predominantly parameterized with line width (here, 3 pixels), line angle (here, 45°), saturation ratio (here, 4), and line step, or the spacing between the grid’s lines (here, 15 and 50 pixels). Images were rescaled to 90x120 and created using the "grid illusion" online tool [[47](https://journals.plos.org#pcbi.1010648.ref047)]. Results show that when *β* *c* is high ( *β* *c* = 1), the predicted image’s grey areas gained color, suggesting that the low-pass single-opponent part of the model must be dominant, allowing the assimilation grid illusion to take place. As *β* *c* value decreases, the low-pass effect of the single-opponent cells degrades, resulting in persistent achromatic areas. The model further demonstrates that, as expected, as the grid becomes denser, the perceived image gets further saturated with color, as testified by the measured LPIPS distances (Fig 5 **, right)** . We note that to compare the model’s ability to reconstruct colors between the grid, as perceived in the illusion, LPIPS was calculated on the reconstructed and the full-color images (not the grid color images).
Download:

* PPT PowerPoint slide
* PNG larger image
* TIFF original image
  Fig 5. Reconstruction of the color assimilation grid illusion.
  A selective colored grid was overlaid on two grayscale images, creating the visual stimuli, shown in the first row. The model predictions with different sets of chromatic and achromatic parameters are shown in rows 2–5. LPIPS scores are shown on the right.
  https://doi.org/10.1371/journal.pcbi.1010648.g005
  Interestingly, while the LPIPS distance for the red square is consistent with our perception (the most similar image is obtained when *α* *i* = 0.5 and *α* *c* = 0), the LPIPS distances for the colored face grid illusion are inconsistent. While the smallest LPIPS distances for the reconstructed colored face grid illusion are obtained when *α* *i* = 1 and *α* *c* = 0.5 (for both grid densities), by visual inspection, the perceived best results are obtained when *α* *i* = 0.5 and *α* *c* = 0. When presented with illusory and not natural images, our results demonstrate LPIPS’s failure to measure perceptive similarity.

##### #TheDress and #TheShoe

In 2015, two images, hashtagged on social media as #TheDress and #TheShoe, became viral as they depicted individual differences in color perception. In #TheDress image, some people perceived the dress’s color as black and blue, while others perceived it as gold and silver (or gold and white) [[48](https://journals.plos.org#pcbi.1010648.ref048)–[50](https://journals.plos.org#pcbi.1010648.ref050)]. Similarly, while some perceived the colors of #TheShoe as pink and white, others perceived them as gray and cyan (turquoise) [[50](https://journals.plos.org#pcbi.1010648.ref050)] (Fig 6A). Here we reconstructed these two famous photos, allowing us to examine the model’s parameter space on the predicted colors (Fig 6B). In #TheDress reconstruction, results show that silver (achromatic) and gold (brownish) are perceived by setting the chromatic alpha to 1 ( *α* *c* = 1), and blueish and black are scented with a chromatic alpha of 0.5 ( *α* *c* = 0.5). In #TheShow reconstruction, results show that pink and light gray (slightly Cyanish) are perceived with a chromatic alpha of 1 ( *α* *c* = 1), whereas the blueish and gray (dark achromatic) are scented with a chromatic alpha of 0.5 ( *α* *c* = 0.5).
Download:

* PPT PowerPoint slide
* PNG larger image
* TIFF original image
  Fig 6. Reconstruction of #TheDress and #theShoe photos.
  A. The original images; B. Model’s prediction with different sets of chromatic and achromatic parameters; C. Comparison between the true color (marked with an asterisk) and the predictions of the model Results are presented in u’v’ (CIELu’v’) color space. Each color circle surrounds the true and predicted colors of a sampled pixel in the patch. Black lines represent cone-opponent axes, S/(L + M) and L/(L + M). The intersection of the lines represents the achromatic point. b) Comparison between the true color (mark with red \*) and the predictions of the model with *α* *c* = 1 and *α* *c* **= 0.5 presented in u’v’ (CIELu’v’ 1976) color space. Each ellipse surrounds the true and the predicted colors of a sampled pixel in the patch. Black lines represent cone-opponent axes, S/(L + M) and L/(L + M). The intersections of the lines represent the achromatic point** .
  https://doi.org/10.1371/journal.pcbi.1010648.g006
  We further evaluated these results in the CIELu’v’ color space (Fig 6C). Results show that the predicted colors are based on the chromatic parameters. When *α* *c* = 1, the dark brown (or black) patch of #TheDress becomes more saturated and brownish-orange (goldish) in appearance. The blue color of #TheDress turns more achromatic as it gets closer to the achromatic point. #TheShoe’s gray patch becomes more reddish (pink) as it goes toward the red axis, and the cyan (turquoise) patch becomes more achromatic as it moves toward the achromatic point. However, when *α* *c* = 0.5, the predicted colors are getting closer to the ground truth colors in both photos.

##### Parameter evaluation

To determine the influence of the model’s parameters on the predicted color, simulations were conducted with different *SO* ′ *s* spatial parameters ( *W* and *σ* ), *α* *i* and *α* *c* . The simulation results over a CIELu’v’ color space for both *α* *i* and *α* *c* (ranging from 0.5 to 1) are shown in Fig 7. With each image (colored face, cube with natural-yellowish-blueish illumination, #theDress, and #theShoe), we sampled pixels from different locations in the image where each location has a different color (hue) and ran simulations with varying *α* *i* and *α* *c* . For further parameter evaluation, we also changed the kernel size of the *SO* cell ( *W* = 21, *σ* = 5, *W* = 11 and *σ* = 3; Eqs [4](https://journals.plos.org#pcbi.1010648.e005)–[6](https://journals.plos.org#pcbi.1010648.e007)). It appears that predictions can range over areas of CIELu’v’ color space as well as curves. As well, the model appears to be more sensitive to the selection *α* *i* and *α* *c* rather than it is to the selection of the spatial parameters of SO cells.
Download:

* PPT PowerPoint slide
* PNG larger image
* TIFF original image
  Fig 7. Parameter evaluation with 21x21 and 11x11 kernel size (2nd and 3rd columns, respectively), compared with Retinex prediction (right column).
  Input images are shown in the left column.
  https://doi.org/10.1371/journal.pcbi.1010648.g007

##### Model comparison

We further compared the prediction of the model to a modified version of the Retinex algorithm, one of the most established retinal models in computational vision [[51](https://journals.plos.org#pcbi.1010648.ref051)]. We used a single-scale non-logarithmic version of Retinex, as was suggested in [[52](https://journals.plos.org#pcbi.1010648.ref052)]. Retinex predictions are described using: (25) where where *m* and *n* are the image width and height respectively. In the Retinex algorithm, the filter response is computed separately for each of the three image channels (R, G, B). Here, we changed the spatial scale of the Retinex predictions for a better alignment with our model, by modulating the parameter *s* : (26)
Small s values result in high pass responses, while large s values produce more low pass frequencies. As a result of the high-pass response, colors appear near the edges while achromatic areas appear between the edges. Therefore, the Retinex algorithm results are approaching the achromatic gray point when *s* decreases (Fig 7 **, right column** ). On the other hand, as *s* increases, Retinex’s results obtain more chromatic colors (predicted colors that are closer to the original color, in CIELu’v’ space). Retinex’s results verify our model predictions regarding the individual perceptual differences in the images of #theDress and #theShoe (also demonstrated in [[52](https://journals.plos.org#pcbi.1010648.ref052)]), as well as the perception of color under different illuminations. In contrast to Retinex, our proposed model is biologically plausible, allowing the attribution of these differences to the proportions between the single and double opponent cells’ activity. Furthermore, in contrast to our model, Retinex was not able to predict as accurately the color assimilation effect (S4 Fig), showcasing the generality of our proposed computational framework.

#### Discussion

Our parametric implementation of color perception allows critical evaluation of various visual phenomena in a single biological plausible computational framework. It uses a parametrized combination of high and low frequencies and an SNN-based filling-in process to provide adequate color image perception while accounting for individual perception differences. This work extends our previous SNN-based model [[5](https://journals.plos.org#pcbi.1010648.ref005)], which addressed the images’ intensity channels alone. We show that while in the perceptual reconstruction of natural color images, both single and double opponent pathways are required to achieve adequate results, the single opponent pathway is sufficient to predict the perception of the color assimilation grid illusion. Furthermore, we demonstrate individual differences in color perception using the #theDress and #theShoe images. Our proposed model can further explain both the watercolor [[14](https://journals.plos.org#pcbi.1010648.ref014)] and the Cornsweet illusion [[16](https://journals.plos.org#pcbi.1010648.ref016)] through the reconstruction of images from adapted gradients, as we recently demonstrated [[32](https://journals.plos.org#pcbi.1010648.ref032)].
Our SNNs-driven computational framework follows the model suggested by Shapley and colleagues, which proposed dual opponent mechanisms for color perception [[7](https://journals.plos.org#pcbi.1010648.ref007)]. When the color contrast is low, human color perception is characterized by spatially low pass filtering, where single-opponent neurons dominate visual perception. When color contrasts intensify, visual perception shifts from low pass to edge-sensitive filtering, where double-opponent neurons become the predominant mechanism. Our model parametrizes this duality with weighted channel contribution, allowing critical examination of the model’s prediction. We modeled the single opponent pathway with low-pass filtering, implemented by convolving a Gaussian kernel- with an opponent color channel. The double opponent was modeled with high pass filtering, serving as color contrast detectors [[53](https://journals.plos.org#pcbi.1010648.ref053)]. In our proposed model, rather than combine the double-opponent responses directly with the single-opponent responses, we used the double-opponent responses as triggers for diffusive Poisson-driven recurrent SNNs, allowing the reconstruction of low-pass properties from high-pass information. This is done in a diffusion-like process, in which a double-opponent cell activates its neighbors ([Eq 16](https://journals.plos.org#pcbi.1010648.e026)). Our recurrent SNN is a biologically plausible implementation of an iterative numerical solver of the Poisson equation, allowing accurate perceptual prediction. However, since an ensemble of spiking neurons approximates each pixel’s value, the process cannot reach a steady state, corresponding to the biological resource-constrained spike-based encoding.
In this work, we propose a biologically plausible SNNs-driven model which can serve as a potential neural mechanism for perceptual color filling-in, corresponding with the spreading of color signals in the cortex [[3](https://journals.plos.org#pcbi.1010648.ref003)], [[54](https://journals.plos.org#pcbi.1010648.ref054)]. Our model can be correlated with experimentational findings in the cortex, providing further insights. We show with voltage-sensitive dye-imaging in V1 of macaque monkeys in response to uniformly colored or achromatic large squares, that there is an unfilled area (’hole’) of activity [[42](https://journals.plos.org#pcbi.1010648.ref042)]. Our model predicts a similar pattern (partially filled square) when the chromatic alpha is large (Fig 2). It should be noted that layers 2–3 are the main cortical layers imaged by VSDI. The cells in these layers are mostly edge detectors and these layers contain a high population of double-opponent cells [[6](https://journals.plos.org#pcbi.1010648.ref006)]. Therefore, to compare VSDI signals to simulations of black and red squares, we use *α* *i* = 1 and *α* *c* = 1 (large alphas) in our simulation to account for only the double opponent pathway. As we increase the single opponent pathway dominancy (by decreasing *α* and increasing *β* ), this filling in the gap is shrinking, suggesting that the integration of the single and double opponent mechanisms does not occur in V1 but rather in higher visual regions. Furthermore, the cortex’s layer hierarchy suggests that the receptive fields of higher visual layers correspond to wider spatial areas of the stimulus [[1](https://journals.plos.org#pcbi.1010648.ref001)]. This can be interpreted as having recursive (horizontal connections) layer-based filling-in processes [[55](https://journals.plos.org#pcbi.1010648.ref055)], which reduce the distance between edges in higher layers and the propagation time of the spreading filled-in signal [[56](https://journals.plos.org#pcbi.1010648.ref056)]. Our model layer-based design supports this architecture. Consequently, this computational design can explain the results in [[42](https://journals.plos.org#pcbi.1010648.ref042)], which conclude that while V1 activity is insufficient to explain the perception of filled objects, filling-in processes that occur at both low and high levels can produce the perception of filled objects. Experimental studies on filling-in are consistent with these ideas, as neural activities in V3 and V4 areas during perceptual filling-in effects were observed in response to the watercolor and Cornsweet illusions, texture, and afterimage filling-in [[57](https://journals.plos.org#pcbi.1010648.ref057)–[60](https://journals.plos.org#pcbi.1010648.ref060)].
Recently, Yang and colleagues demonstrated similar VSDI results [[61](https://journals.plos.org#pcbi.1010648.ref061)]. Like the results reported here, they showed that V1 responses in cortical layers 2–3 are enhanced at the surface edges whereas the response at the surface center is suppressed. However, in this work we used a range of surface sizes, allowing us to compute the slope of population propagation from the edges to the surface’s center. Thus, supporting our assumption of having horizontal connections contributing to the filling-in phenomenon.
We demonstrate the model’s prediction of visual filling-in with various examples and critically examine related phenomena: color constancy, color assimilation, and individual perception. Color constancy and individual differences in color perception are widely discussed in the literature. For example, Dixon and Shapiro [[52](https://journals.plos.org#pcbi.1010648.ref052)] suggested that these visual phenomena can be explained through high-pass filtering, which subtracts a blurred modality of an image from the original one and adds a constant intensity value, shifting it back into the viewable range [[62](https://journals.plos.org#pcbi.1010648.ref062)]. This simple model was argued to account for different color perceptions, grounding it on individual frequency processing characteristics. Given the appropriate spatial parameters, the authors demonstrated that this model could explain color constancy in several illusions, such as the cube illusion [[22](https://journals.plos.org#pcbi.1010648.ref022)] as well as the individual difference phenomenon regarding the #theShoe and #theDress (their results are also reproduced in this current work; Fig 7). However, this spatial filter cannot explain other brightness and color filling-in illusions, such as the Cornsweet [[16](https://journals.plos.org#pcbi.1010648.ref016)] and the watercolor [[14](https://journals.plos.org#pcbi.1010648.ref014)] illusions, as well as color assimilation (S4 Fig). A naïve frequency filtering cannot explain these illusions as they are based on changes generated at a thin edge, extending over large distances. While other models of color constancy do relays on the combinations of high and low-pass filters [[13](https://journals.plos.org#pcbi.1010648.ref013)], [[51](https://journals.plos.org#pcbi.1010648.ref051)], [[63](https://journals.plos.org#pcbi.1010648.ref063)], they are not biologically plausible. First, they entail different filter kernel sizes to account for individuals’ color perceptions. Secondly, they require the original high-resolution image for processing, which is not conducted through the biological visual system. As was demonstrated by the model’s prediction of #TheDress and #TheShoe, despite having only global parameters, our model was able to capture differences in perception with respect to the model’s parameters (Fig 7). Thus, concurring with Gegenfurtner and colleagues, who found that there are multiple answers to the question, “what color is the dress?” [[64](https://journals.plos.org#pcbi.1010648.ref064)]. Our results extend their finding and demonstrate in a biologically plausible computational framework that there can be multiple responses to any color image. In the colored face image, for example, people may perceive and name colors differently. Some may name the orange part of the woman’s finger orange, while others might call it yellowish or greenish (the original orange color changes to greenish-yellowish with respect to the value of alpha; Fig 7 **, top row** ).
Our LPIPS-driven evaluation of the model demonstrates that LPIPS was unable to accurately capture illusive perception. Therefore, while the image with the lowest LPIPS score is the most perceptually similar to the GT, it might not capture the illusion. Therefore, here, LPIPS scores were used not to identify which parameters gave the lowest scores, but rather to illustrate: 1) the model can reconstruct images that are perceptually similar to GT; 2) that the demonstrated illusions, as were perceived by the brain, are different than the GT, resulting in a higher LPIPS score; and 3) that color perception varies across individuals. If someone perceives #theDress as black and blue, then their perception is more similar to the original/physical colors of the GT.
With #thedress image as a stimulus, numerous studies have attempted to identify the underlying mechanisms that lead to different perceptions of colors among individuals. Toscani and colleagues [[65](https://journals.plos.org#pcbi.1010648.ref065)] investigated whether people who report different colors for #thedress do so because they have different assumptions about the illumination in the scene. They found that observers reporting the dress to be white (white perceivers) adjusted the background illumination more bluely than observers reporting it to be blue (blue perceivers). The illumination appeared less chromatic to blue perceivers. Therefore, they concluded that different assumptions about illumination chromaticity in the scene can explain ambiguity in the perceived color of the dress. Similarly, Witzel and colleagues [[66](https://journals.plos.org#pcbi.1010648.ref066)] and Aston and colleagues [[67](https://journals.plos.org#pcbi.1010648.ref067)] concluded that assumptions and priors about illumination affect perceived images. According to Witzel and colleagues [[66](https://journals.plos.org#pcbi.1010648.ref066)], prior-modified images of the dress can manipulate the perceived color. The prior-modified image, however, did not predict the perceived color of the original dress image in all observers. Therefore, they concluded that interpretations of the dress’ colors are influenced by assumptions about illumination, but other factors may systematically affect interpretations. Aston and colleagues [[67](https://journals.plos.org#pcbi.1010648.ref067)] tested the possibility that color constancy could explain this phenomenon. A color constancy with illumination discrimination task was used to assess whether individual differences in generic color constancy could explain perception differences in our observers. Using the dress photograph as an example, they demonstrated that individual differences in perception may partly be explained by chromatic biases in illumination priors. Individual differences in color constancy, however, do not explain variability in the perception of dress colors. Observers individually discount achromatic features: while blue-black reporters focus on blue regions, while white-gold reporters focus on golden regions. It is consistent with the hypothesis that attention and local image statistics play a role in understanding multi-stable images. Overall, these studies confirmed the importance of background illumination, image statistics, and priors, but they could not explain the underlying mechanism. Our model allows the attribution of perceptual differences to the proportions between the single and double opponent cells’ activity, while being general enough to account for a wide range of visual phenomena including color constancy, color assimilation, and ambiguous color perception.
In our suggested model, *α* *i* and *α* *c* are two parameters that can be modified to describe different visual phenomena (where *β* *i* = 1− *α* *i* and *β* *c* = 1− *α* *c* ). To demonstrate how the model can generate different perceptions, we manually modulated these parameters. In the brain, these weights, however, are determined by visual processes that were not computationally modeled. Moreover, these parameters might be computed locally within the brain, rather than globally, as in our current framework. The precise channels’ weight setting is still unknown. When individual perceptual differences are considered (e.g., #theDress and #theShoe), *α* *i* and *α* *c* are vary among individuals and can even be different among images within an individual. For example, one person may perceive the dress as blue and black ( *α* *c* = 0.5), and the shoe as white and pink ( *α* *c* = 1). As a result, different images might be generated by a different weighting scheme. These parameters can be determined using an unknown set of visual features, supporting the concept of having them derived individually for each image. Therefore, we emphasize that our model does not suggest the existence of a single set of parameters with which all illusions can be accounted for, nor does it suggest that a single set of parameters would be sufficient for modeling individual color perception. We rather suggest that a weighted combination of the single opponent and the double opponent cells might model individual color perception. Interestingly, a recent work [[50](https://journals.plos.org#pcbi.1010648.ref050)] showed that the perception of these visual imageries remains stable over time, possibly due to "one-shot learning," which allows for the first encounter’s strong influence to determine observers’ perception [[50](https://journals.plos.org#pcbi.1010648.ref050)], [[68](https://journals.plos.org#pcbi.1010648.ref068)]. Thus, suggesting that, once acquired, our color parameters stay constant. However, our model could be further developed to account for adaptive changes and the support of local alpha values, corresponding to the image’s regional contrast differences.

#### Supporting information

##### [S1 Fig.](https://journals.plos.org#pcbi.1010648.ref068) A comparison between our model prediction and the VSDI measurements across 0.5°, 1°, 2° and 3° profiles.

[https://doi.org/10.1371/journal.pcbi.1010648.s001](https://journals.plos.org#pcbi.1010648.ref068)
(TIFF)

##### [S2 Fig.](https://journals.plos.org#pcbi.1010648.ref068) Reconstruction results without recurrent connections (i.e., without a filling-in network).

[https://doi.org/10.1371/journal.pcbi.1010648.s002](https://journals.plos.org#pcbi.1010648.ref068)
(TIFF)

##### [S3 Fig.](https://journals.plos.org#pcbi.1010648.ref068) Reconstruction results with non-spiking and spiking neural networks.

[https://doi.org/10.1371/journal.pcbi.1010648.s003](https://journals.plos.org#pcbi.1010648.ref068)
(TIFF)

##### [S4 Fig.](https://journals.plos.org#pcbi.1010648.ref068) Retinex prediction of the color assimilation effect, using filter size (s) in various sizes.

[https://doi.org/10.1371/journal.pcbi.1010648.s004](https://journals.plos.org#pcbi.1010648.ref068)
(TIFF)

#### References

1. Wandell BA. Foundations of vision. Sinauer Associates; 1995. 476 p.

* View Article
* Google Scholar

2. Von Der Heydt R, Friedman HS, Zhou H. Searching for the Neural Mechanism of Color Filling-In. In: Filling-In: From Perceptual Completion to Cortical Reorganization. Oxford University Press; 2009.
3. Komatsu H. The neural mechanisms of perceptual filling-in. Vol. 7, Nature Reviews Neuroscience. 2006. p. 220–31. pmid:16495943

* View Article
* PubMed/NCBI
* Google Scholar

4. Marr D. Vision: A computational investigation into the human representation and processing of visual information. San Francisco: W. H. Freeman and Company; 1982.
5. Cohen Duwek H, Ezra Tsur E. Biologically Plausible Spiking Neural Networks for Perceptual Filling-In. Proc Annu Meet Cogn Sci Soc. 2021;43(43).

* View Article
* Google Scholar

6. Shapley R, Hawken MJ. Color in the Cortex: single- and double-opponent cells. Vision Res [Internet]. 2011 Apr 13 [cited 2019 Jan 21];51(7):701–17. Available from: <https://www.sciencedirect.com/science/article/pii/S0042698911000526#e0005> pmid:21333672

* [View Article](https://www.sciencedirect.com/science/article/pii/S0042698911000526#e0005)
* [PubMed/NCBI](https://www.sciencedirect.com/science/article/pii/S0042698911000526#e0005)
* [Google Scholar](https://www.sciencedirect.com/science/article/pii/S0042698911000526#e0005)

7. Shapley R, Nunez V, Gordon J. Cortical double-opponent cells and human color perception. Curr Opin Behav Sci. 2019 Dec 1;30:1–7.

* View Article
* Google Scholar

8. Lennie P, Krauskopf J, Sclar G. Chromatic mechanisms in striate cortex of macaque. J Neurosci [Internet]. 1990 Feb 1 [cited 2021 Oct 11];10(2):649–69. Available from: <https://www.jneurosci.org/content/10/2/649> pmid:2303866

* [View Article](https://www.jneurosci.org/content/10/2/649)
* [PubMed/NCBI](https://www.jneurosci.org/content/10/2/649)
* [Google Scholar](https://www.jneurosci.org/content/10/2/649)

9. Schwartz J, Kandel E, Jessell T. Principles of neural science. 1991;

* View Article
* Google Scholar

10. McIlhagga W, Mullen KT. Evidence for chromatic edge detectors in human vision using classification images. J Vis [Internet]. 2018 Sep 4 [cited 2021 Oct 24];18(9):8–8. Available from: pmid:30208428

* View Article
* PubMed/NCBI
* Google Scholar

11. Gilbert CD, Wiesel TN. Morphology and intracortical projections of functionally characterised neurones in the cat visual cortex. Nature. 1979;280(5718):120–5. pmid:552600

* View Article
* PubMed/NCBI
* Google Scholar

12. Hirsch JA, Gilbert CD. Synaptic physiology of horizontal connections in the cat’s visual cortex. J Neurosci [Internet]. 1991 Jun 1 [cited 2020 Dec 20];11(6):1800–9. Available from: <https://www.jneurosci.org/content/11/6/1800> pmid:1675266

* [View Article](https://www.jneurosci.org/content/11/6/1800)
* [PubMed/NCBI](https://www.jneurosci.org/content/11/6/1800)
* [Google Scholar](https://www.jneurosci.org/content/11/6/1800)
* 13. Judd DB. Hue Saturation and Lightness of Surface Colors with Chromatic Illumination. JOSA, Vol 30, Issue 1, pp 2–32 [Internet]. 1940 Jan 1 [cited 2021 Oct 24];30(1):2–32. Available from: <https://www.osapublishing.org/viewmedia.cfm?uri=josa-30-1-2&seq=0&html=true> [View Article](https://www.osapublishing.org/viewmedia.cfm?uri=josa-30-1-2&seq=0&html=true)
* [Google Scholar](https://www.osapublishing.org/viewmedia.cfm?uri=josa-30-1-2&seq=0&html=true)

14. Pinna B, Brelstaff G, Spillmann L. Surface color from boundaries: A new “watercolor” illusion. Vision Res. 2001;41(20):2669–76. pmid:11520512

* View Article
* PubMed/NCBI
* Google Scholar

15. van Tuijl HFJM, Leeuwenberg ELJ. Neon color spreading and structural information measures. Percept Psychophys. 1979 Jul;25(4):269–84. pmid:461087

* View Article
* PubMed/NCBI
* Google Scholar

16. Cornsweet T. Visual perception. New York: Academic Press; 1970.
17. Barkan Y, Spitzer H. The Color Dove Illusion [Internet]. Vol. 1. Oxford University Press; 2017 [cited 2019 Dec 29]. Available from: <http://www.oxfordscholarship.com/view/10.1093/acprof:oso/9780199794607.001.0001/acprof-9780199794607-chapter-109>
18. van Lier R, Vergeer M, Anstis S. Filling-in afterimage colors between the lines. Vol. 19, Current Biology. 2009.

* View Article
* Google Scholar

19. Ramachandran V. Blind spots. JSTOR [Internet]. 1992 [cited 2020 Dec 9]; Available from: <https://www.jstor.org/stable/24939062> pmid:1566041

* [View Article](https://www.jstor.org/stable/24939062)
* [PubMed/NCBI](https://www.jstor.org/stable/24939062)
* [Google Scholar](https://www.jstor.org/stable/24939062)

20. Foster DH. Color constancy. Vision Res. 2011 Apr 13;51(7):674–700. pmid:20849875

* View Article
* PubMed/NCBI
* Google Scholar

21. Brainard DH, Longère P, Delahunt PB, Freeman WT, Kraft JM, Xiao B. Bayesian model of human color constancy. J Vis [Internet]. 2006 Oct 1 [cited 2021 Oct 25];6(11):10–10. Available from: <http://journalofvision.org/6/11/10/> pmid:17209734

* [View Article](http://journalofvision.org/6/11/10/)
* [PubMed/NCBI](http://journalofvision.org/6/11/10/)
* [Google Scholar](http://journalofvision.org/6/11/10/)

22. Lotto RB, Purves D. An empirical explanation of color contrast. Proc Natl Acad Sci [Internet]. 2000 Nov 7 [cited 2021 Oct 25];97(23):12834–9. Available from: <https://www.pnas.org/content/97/23/12834> pmid:11058148

* [View Article](https://www.pnas.org/content/97/23/12834)
* [PubMed/NCBI](https://www.pnas.org/content/97/23/12834)
* [Google Scholar](https://www.pnas.org/content/97/23/12834)

23. Spitzer H, Semo S. Color constancy: A biological model and its application for still and video images. Pattern Recognit. 2002 Aug;35(8):1645–59.

* View Article
* Google Scholar

24. Courtney SM, Finkel LH, Buchsbaum G. A Multistage Neural Network for Color Constancy and Color Induction. IEEE Trans Neural Networks. 1995;6(4):972–85. pmid:18263385

* View Article
* PubMed/NCBI
* Google Scholar

25. Shapley R, Hawken MJ. Color in the Cortex: Single- and double-opponent cells. Vol. 51, Vision Research. 2011. p. 701–17. pmid:21333672

* View Article
* PubMed/NCBI
* Google Scholar

26. Gegenfurtner KR. Cortical mechanisms of colour vision. Nat Rev Neurosci 2003 47 [Internet]. 2003 [cited 2021 Nov 7];4(7):563–72. Available from: <https://www.nature.com/articles/nrn1138> pmid:12838331

* [View Article](https://www.nature.com/articles/nrn1138)
* [PubMed/NCBI](https://www.nature.com/articles/nrn1138)
* [Google Scholar](https://www.nature.com/articles/nrn1138)

27. Maass W. Networks of spiking neurons: The third generation of neural network models. Neural Networks. 1997 Dec 1;10(9):1659–71.

* View Article
* Google Scholar

28. Stewart TC, Eliasmith C. Large-scale synthesis of functional spiking neural circuits. Vol. 102, Proceedings of the IEEE. Institute of Electrical and Electronics Engineers Inc.; 2014. p. 881–98.
29. Kuffler S, Nicholls J, Martin A. From Neuron to Brain, 2nd Eds. 1984;

* View Article
* Google Scholar
* 30. Johnson E, Hawken M, Neuroscience RS-J of, 2008 undefined. The orientation selectivity of color-responsive neurons in macaque V1. Soc Neurosci [Internet]. 2008 [cited 2021 Oct 11]; Available from: <https://www.jneurosci.org/content/28/32/8096.short> [View Article](https://www.jneurosci.org/content/28/32/8096.short)
* [Google Scholar](https://www.jneurosci.org/content/28/32/8096.short)

31. Cohen-Duwek H, Spitzer H. A Model for a Filling-in Process Triggered by Edges Predicts “Conflicting” Afterimage Effects. Front Neurosci [Internet]. 2018 Aug 17 [cited 2019 Mar 3];12:559. Available from: <https://www.frontiersin.org/article/10.3389/fnins.2018.00559/full> pmid:30174580

* [View Article](https://www.frontiersin.org/article/10.3389/fnins.2018.00559/full)
* [PubMed/NCBI](https://www.frontiersin.org/article/10.3389/fnins.2018.00559/full)
* [Google Scholar](https://www.frontiersin.org/article/10.3389/fnins.2018.00559/full)

32. Cohen Duwek H, Spitzer H. A compound computational model for Filling-in processes triggered by edges: watercolor illusions. Front Neurosci [Internet]. 2019 [cited 2019 Mar 3];13:225. Available from: <https://www.frontiersin.org/articles/10.3389/fnins.2019.00225/abstract> pmid:30967753

* [View Article](https://www.frontiersin.org/articles/10.3389/fnins.2019.00225/abstract)
* [PubMed/NCBI](https://www.frontiersin.org/articles/10.3389/fnins.2019.00225/abstract)
* [Google Scholar](https://www.frontiersin.org/articles/10.3389/fnins.2019.00225/abstract)

33. Pinna B. Watercolor illusion. Scholarpedia. 2008;3(1):5352.

* View Article
* Google Scholar

34. Weickert J. Theoretical Foundations of Anisotropic Diffusion in Image Processing. In 1996. p. 221–36.

* View Article
* Google Scholar

35. Mikula K. Image processing with partial differential equations. In: Modern Methods in Scientific Computing and Applications [Internet]. Springer Netherlands; 2002 [cited 2020 Nov 29]. p. 283–321. Available from: <https://link.springer.com/chapter/10.1007/978-94-010-0510-4_8>
36. Simchony T, Chellappa R, Shao M. Direct Analytical Methods for Solving Poisson Equations in Computer Vision Problems. IEEE Trans Pattern Anal Mach Intell. 1990;12(5):435–46.

* View Article
* Google Scholar

37. Russakovsky O, Deng J, Su H, Krause J, Satheesh S, Ma S, et al. ImageNet Large Scale Visual Recognition Challenge. Int J Comput Vis. 2015 Dec 1;115(3):211–52.

* View Article
* Google Scholar
* 38. Zhang R, Isola P, Efros AA, Shechtman E, Wang O. The unreasonable effectiveness of deep features as a perceptual metric. In: Proceedings of the IEEE conference on computer vision and pattern recognition [Internet]. 2018 [cited 2022 Jan 6]. p. 586–95. Available from: <http://openaccess.thecvf.com/content_cvpr_2018/html/Zhang_The_Unreasonable_Effectiveness_CVPR_2018_paper.html> [View Article](http://openaccess.thecvf.com/content_cvpr_2018/html/Zhang_The_Unreasonable_Effectiveness_CVPR_2018_paper.html)
* [Google Scholar](http://openaccess.thecvf.com/content_cvpr_2018/html/Zhang_The_Unreasonable_Effectiveness_CVPR_2018_paper.html)
* 39. Krizhevsky A, Sutskever I, Hinton GE. ImageNet Classification with Deep Convolutional Neural Networks. In: NIPS [Internet]. 2012 [cited 2022 Jan 9]. Available from: <http://code.google.com/p/cuda-convnet/> [View Article](http://code.google.com/p/cuda-convnet/)
* [Google Scholar](http://code.google.com/p/cuda-convnet/)

40. Bekolay T, Bergstra J, Hunsberger E, DeWolf T, Stewart TC, Rasmussen D, et al. Nengo: a Python tool for building large-scale functional brain models. Front Neuroinform [Internet]. 2014 Jan 6 [cited 2020 Dec 16];7(JAN):48. Available from: <http://journal.frontiersin.org/article/10.3389/fninf.2013.00048/abstract> pmid:24431999

* [View Article](http://journal.frontiersin.org/article/10.3389/fninf.2013.00048/abstract)
* [PubMed/NCBI](http://journal.frontiersin.org/article/10.3389/fninf.2013.00048/abstract)
* [Google Scholar](http://journal.frontiersin.org/article/10.3389/fninf.2013.00048/abstract)

41. DeWolf T, Jaworski P, Eliasmith C. Nengo and Low-Power AI Hardware for Robust, Embedded Neurorobotics. Front Neurorobot [Internet]. 2020 Oct 9 [cited 2022 Jan 23];14:568359. Available from: /pmc/articles/PMC7581863/ pmid:33162886

* View Article
* PubMed/NCBI
* Google Scholar

42. Zweig S, Zurawel G, Shapley R, Slovin H. Representation of Color Surfaces in V1: Edge Enhancement and Unfilled Holes. 2015;

* View Article
* Google Scholar

43. Ebner M. Color constancy [Internet]. New York, NY, USA: Wiley; 2007 [cited 2022 Jan 25]. 393 p. Available from: <https://www.wiley.com/en-gb/Color+Constancy-p-9780470058299>
44. Lotto RB, Purves D. The empirical basis of color perception. Conscious Cogn. 2002 Dec 1;11(4):609–29. pmid:12470626

* View Article
* PubMed/NCBI
* Google Scholar
* 45. Ibraheem NA, Hasan MM, Khan RZ, Mishra PK. Understanding Color Models: A Review. ARPN J Sci Technol [Internet]. 2012 [cited 2022 Jan 23];2(3). Available from: <http://www.ejournalofscience.org> [View Article](http://www.ejournalofscience.org)
* [Google Scholar](http://www.ejournalofscience.org)
* 46. Kolås Ø. Color Assimilation Grid Illusion | Øyvind Kolås on Patreon [Internet]. 2019 [cited 2021 Oct 26]. Available from: <https://www.patreon.com/posts/color-grid-28734535> [View Article](https://www.patreon.com/posts/color-grid-28734535)
* [Google Scholar](https://www.patreon.com/posts/color-grid-28734535)

47. Grid Illusion generator [Internet]. [cited 2022 Jan 6]. Available from: <https://nazomizu.com/html/lab/illusion/#>
48. Lafer-Sousa R, Hermann KL, Conway BR. Striking individual differences in color perception uncovered by ‘the dress’ photograph. Curr Biol. 2015 Jun 29;25(13):R545–6. pmid:25981795

* View Article
* PubMed/NCBI
* Google Scholar

49. Brainard DH, Hurlbert AC. Colour Vision: Understanding #TheDress. Curr Biol. 2015 Jun 29;25(13):R551–4. pmid:26126278

* View Article
* PubMed/NCBI
* Google Scholar

50. Drissi-Daoudi L, Doerig A, Parkosadze K, Kunchulia M, Herzog MH. How stable is perception in #TheDress and #TheShoe? Vision Res. 2020 Apr 1;169:1–5. pmid:32085967

* View Article
* PubMed/NCBI
* Google Scholar

51. Land EH. Recent advances in retinex theory. Vision Res. 1986 Jan 1;26(1):7–21. pmid:3716215

* View Article
* PubMed/NCBI
* Google Scholar

52. Dixon EL, Shapiro AG. Spatial filtering, color constancy, and the color-changing dress. J Vis. 2017 Mar 1;17(3):7–7. pmid:28278312

* View Article
* PubMed/NCBI
* Google Scholar

53. Johnson EN, Hawken MJ, Shapley R. The orientation selectivity of color-responsive neurons in macaque V1. J Neurosci. 2008 Aug 6;28(32):8096–106. pmid:18685034

* View Article
* PubMed/NCBI
* Google Scholar

54. Sasaki Y, Watanabe T. The primary visual cortex fills in color. Proc Natl Acad Sci [Internet]. 2004 Dec 28 [cited 2022 Jan 25];101(52):18251–6. Available from: <https://www.pnas.org/content/101/52/18251> pmid:15596726

* [View Article](https://www.pnas.org/content/101/52/18251)
* [PubMed/NCBI](https://www.pnas.org/content/101/52/18251)
* [Google Scholar](https://www.pnas.org/content/101/52/18251)
* 55. Gilbert C, Nature TW-, 1979 undefined. Morphology and intracortical projections of functionally characterised neurones in the cat visual cortex. neurosci.info [Internet]. [cited 2020 Dec 20]; Available from: <http://neurosci.info/courses/vision2/V1Circuits/gilbert79.pdf> [View Article](http://neurosci.info/courses/vision2/V1Circuits/gilbert79.pdf)
* [Google Scholar](http://neurosci.info/courses/vision2/V1Circuits/gilbert79.pdf)

56. Ricci M, Serre T. Hierarchical Models of the Visual System. In: Encyclopedia of Computational Neuroscience. Springer New York; 2020. p. 1–14.
57. De Weerd P, Gattass R, Desimone R, Ungerleider LG. Responses of cells in monkey visual cortex during perceptual filling-in of an artificial scotoma. Nature. 1995;377(6551):731–734 pmid:7477262

* View Article
* PubMed/NCBI
* Google Scholar

58. Hong SW, Tong F. Neural representation of form-contingent color filling-in in the early visual cortex. J Vis. 2017 Nov 1;17(13). pmid:29136409

* View Article
* PubMed/NCBI
* Google Scholar

59. Roe AW, Lu HD, Hung CP. Cortical processing of a brightness illusion. Proc Natl Acad Sci U S A. 2005 Mar 8;102(10):3869–74. pmid:15738406

* View Article
* PubMed/NCBI
* Google Scholar

60. Devinck F, Knoblauch K. Central mechanisms of perceptual filling-in. Vol. 30, Current Opinion in Behavioral Sciences. Elsevier Ltd; 2019. p. 135–40.
61. Yang Y, Wang T, Li Y, Dai W, Yang G, Han C, et al. Coding strategy for surface luminance switches in the primary visual cortex of the awake monkey. Nat Commun 2022 131 [Internet]. 2022 Jan 12 [cited 2022 Jul 21];13(1):1–15. Available from: <https://www.nature.com/articles/s41467-021-27892-3> pmid:35022404

* [View Article](https://www.nature.com/articles/s41467-021-27892-3)
* [PubMed/NCBI](https://www.nature.com/articles/s41467-021-27892-3)
* [Google Scholar](https://www.nature.com/articles/s41467-021-27892-3)

62. Dixon E, Shapiro A, Lu ZL. Scale-invariance in brightness illusions implicates object-level visual processing. Sci Reports 2014 41 [Internet]. 2014 Jan 29 [cited 2021 Nov 16];4(1):1–9. Available from: <https://www.nature.com/articles/srep03900> pmid:24473496

* [View Article](https://www.nature.com/articles/srep03900)
* [PubMed/NCBI](https://www.nature.com/articles/srep03900)
* [Google Scholar](https://www.nature.com/articles/srep03900)

63. Buchsbaum G. A spatial processor model for object colour perception. J Franklin Inst. 1980 Jul 1;310(1):1–26.

* View Article
* Google Scholar

64. Gegenfurtner KR, Bloj M, Toscani M. The many colours of ‘the dress.’ Curr Biol. 2015 Jun 29;25(13):R543–4. pmid:25981790

* View Article
* PubMed/NCBI
* Google Scholar
* 65. Toscani M, Gegenfurtner KR, Doerschner K. Differences in illumination estimation in #thedress. J Vis [Internet]. 2017 Jan 1 [cited 2022 Sep 17];17(1):22–22. Available from: <http://swiked.tumblr.com/post/112073818575/> [View Article](http://swiked.tumblr.com/post/112073818575/)
* [Google Scholar](http://swiked.tumblr.com/post/112073818575/)

66. Witzel C, Racey C, O’Regan JK. The most reasonable explanation of “the dress”: Implicit assumptions about illumination. J Vis. 2017 Feb 1;17(2):1–1. pmid:28146253

* View Article
* PubMed/NCBI
* Google Scholar

67. Aston S, Hurlbert A. What #theDress reveals about the role of illumination priors in color perception and color constancy. J Vis. 2017 Aug 1;17(9):4–4. pmid:28793353

* View Article
* PubMed/NCBI
* Google Scholar

68. Daoudi LD, Doerig A, Parkosadze K, Kunchulia M, Herzog MH. The role of one-shot learning in #TheDress. J Vis. 2017 Mar 1;17(3):15–15. pmid:28355627

* View Article
* PubMed/NCBI
* Google Scholar
* Download PDFCitation
* XML
  Print Share
* Reddit
* Facebook
* LinkedIn
* Mendeley
* Bluesky
* Email
  Advertisement
  Subject Areas ?
  For more information about PLOS Subject Areas, click [here](https://github.com/PLOS/plos-thesaurus/blob/master/README.md).

##### We want your feedback. Do these Subject Areas make sense for this article? Click the target next to the incorrect Subject Area and let us know. Thanks for your help!

[Color vision](https://github.com/PLOS/plos-thesaurus/blob/master/README.md)Is the Subject Area **"Color vision"** applicable to this article?
Thanks for your feedback.
Sensory perceptionIs the Subject Area **"Sensory perception"** applicable to this article?
Thanks for your feedback.
VisionIs the Subject Area **"Vision"** applicable to this article?
Thanks for your feedback.
NeuronsIs the Subject Area **"Neurons"** applicable to this article?
Thanks for your feedback.
MacaqueIs the Subject Area **"Macaque"** applicable to this article?
Thanks for your feedback.
Neural networksIs the Subject Area **"Neural networks"** applicable to this article?
Thanks for your feedback.
MonkeysIs the Subject Area **"Monkeys"** applicable to this article?
Thanks for your feedback.
Simulation and modelingIs the Subject Area **"Simulation and modeling"** applicable to this article?
Thanks for your feedback.
PLOS is a nonprofit 501(c)(3) corporation, #C2354500, based in California, US