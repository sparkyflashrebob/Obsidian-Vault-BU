---
tags:
  - notebooklm-import
notebook: "_A_My Health Exercise Healing Physiology Anatomy & Death"
category: "personal"
---

65b80c3e-2e29-43a7-bfc3-dd29920e6df3

Risk Scoring System for Vancomycin-Associated Acute Kidney Injury - Frontiers

b259a694-0728-4a58-8010-641fb3997b49

https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.815188/pdf

Risk Scoring System for Vancomycin-Associated Acute Kidney Injury

Jee Yun Kim1,2, Kyun Young Kim3, Jeong Yee1\* and Hye Sun Gwak1\*

1College of Pharmacy and Graduate School of Pharmaceutical Sciences, Ewha Womans University, Seoul, South Korea, 2Department of Pharmacy, Catholic Kwandong University International St. Mary’s Hospital, Incheon, South Korea, 3Division of Nephrology, Department of Internal Medicine, Seoul National University Hospital, Seoul National University College of Medicine, Seoul, South Korea

Vancomycin-associated acute kidney injury (AKI) remains a major challenge for patients and clinicians. This study aimed to construct a risk scoring system for vancomycin-associated AKI. We retrospectively reviewed medical records of patients who underwent therapeutic drug monitoring for vancomycin from June 2018 to July 2019. We selected possible risk factors for AKI by univariate and multivariable logistic regression analyses and developed a scoring system for vancomycin-associated AKI. Machine learning methods were utilized to predict risk factors for the occurrence of AKI. The incidence of vancomycin-associated AKI was 31.7% among 104 patients included in this study. A bodyweight ≤60 kg (two points), a Charlson comorbidity index ≥3 (two points), a vancomycin trough serum level >15 μg/ml (one point), and concomitant use of ≥6 nephrotoxic agents (two points) were included to construct a risk scoring system based on the coefficient from the logistic regression model. The area under the receiver operating characteristic curve (AUROC) (mean, 95% confidence interval (CI)) across 10 random iterations using five-fold cross-validated multivariate logistic regression, elastic net, random forest, support vector machine (SVM)-linear kernel, and SVM-radial kernel models was 0.735 (0.638–0.833), 0.737 (0.638–0.835), 0.721 (0.610–0.833), 0.739 (0.648–0.829), and 0.733 (0.640–0.826), respectively. For total scores of 0–1, 2–3, 4–5, 6–7, the risk of vancomycin-associated AKI was 5, 25, 45, and 65%, respectively. Our scoring system can be applied to clinical settings in which several nephrotoxic agents are used along with vancomycin therapy.

Keywords: nephrotoxicity, acute kidney injury, vancomycin, scoring system, machine learning

INTRODUCTION

Vancomycin (VCM) is used for the treatment of severe infections such as sepsis, endocarditis, osteomyelitis, or meningitis caused by methicillin-resistant Staphylococcus aureus (Deresinski, 2009). To achieve optimal efficacy and avoid nephrotoxicity of this drug, therapeutic drug monitoring (TDM) is recommended (Rybak et al., 2020). VCM-associated nephrotoxicity such as acute kidney injury (AKI) is thought to be related to the serum trough level of the drug and/or the area under the curve (AUC) measured in the first 24 h of VCM use (AUC0-24 h) (Bosso et al., 2011; van Hal et al., 2013; Finch et al., 2017; Ghasemiyeh et al., 2020; Poston-Blahnik and Moenster, 2021). Furthermore, concomitant use of nephrotoxic agents along with VCM has been reported to increase

Edited by: Ayman M. Mahmoud,

Manchester Metropolitan University, United Kingdom

Reviewed by: Iman Karimzadeh,

Shiraz University of Medical Sciences, Iran Marco Allinovi,

Careggi University Hospital, Italy

\*Correspondence: Jeong Yee

jjjhello1@naver.com Hye Sun Gwak

hsgwak@ewha.ac.kr

Specialty section: This article was submitted to

Renal Pharmacology, a section of the journal

Frontiers in Pharmacology

Received: 01 December 2021 Accepted: 21 February 2022 Published: 07 March 2022

Citation: Kim JY, Kim KY, Yee J and Gwak HS

(2022) Risk Scoring System for Vancomycin-Associated Acute

Kidney Injury. Front. Pharmacol. 13:815188.

doi: 10.3389/fphar.2022.815188

ORIGINAL RESEARCH published: 07 March 2022

doi: 10.3389/fphar.2022.815188

the risk of nephrotoxicity of the VCM (Rutter et al., 2017; Gyamlani et al., 2019; Qin et al., 2020). VCM-associated AKI has been reported to worsen patients’ clinical outcomes such as the length of hospital stay, mortality, treatment failure, or economic burden (Wang et al., 2012; Jeffres, 2017). Although many attempts have been made to reduce the incidence of nephrotoxicity associated with the use of VCM, the incidence and severity of nephrotoxicity caused by VCM use are still difficult to predict (Mehta et al., 2015; Filippone et al., 2017).

To predict the AKI risk associated with VCM use, previous studies have identified risk factors for AKI associated with VCM use including sex, age, weight, height, race, renal function, and/or concomitant use of nephrotoxic agents (Finch et al., 2017; Poston-Blahnik and Moenster, 2021; Qin et al., 2020; Gyamlani et al., 2019; Rutter et al., 2017; Mehta et al., 2015; Filippone et al., 2017; See et al., 2021; O’Donnell et al., 2018). However, there are few predictive models for VCM-associated AKI risk that have used machine learning methods other than logistic regression analysis (Imai et al., 2020). Therefore, in this study, we aimed to construct a predictive model for AKI risk due to the VCM use using various machine learning methods and to develop a new scoring system for VCM-associated AKI risk in patients receiving VCM treatment.

MATERIALS AND METHODS

Study Population We retrospectively reviewed the electronic medical records of patients who were admitted to a university hospital in South Korea from June 2018 to July 2019. The included patients were those who were treated with intravenous VCM for more than 2 days (48 h) or at least four times with adjustment in the VCM dose by TDM. Those who were younger than 18 years of age or who were admitted to the hospital for less than 48 h or formore than 6months were excluded. This study was approved by the Institutional Review Board of Catholic Kwandong University International St. Mary’s Hospital (approval no. IS19RISI0040) in accordance with the 1964 Helsinki declaration and its later amendments. The requirement for obtaining informed consent was waived by the Institutional Review Board of Catholic Kwandong University International St. Mary’s Hospital, due to the retrospective nature of this study. This study is registered at the Clinical Research Information Service (approval no. KCT0005260).

Data Collection At the time of starting TDM, demographic data of patients including sex, age, weight, and height, diagnosis of chronic kidney disease (CKD) defined by glomerular filtration rate (GFR) < 60 ml/min/1.73 m2 for 3 months or more (Levey et al., 2005), status of renal replacement therapy, Charlson comorbidity index (CCI), dose and duration of treatment with VCM, and nephrotoxic agents (Supplementary Table S1) received while on VCM therapy were recorded. TDM was performed with both Bayesian dose optimizing software and the trapezoidal method for calculating the lower/upper limit of AUC0–24h/minimum inhibitory concentration (MIC). MIC

values of VCM were determined by the broth microdilution method. The serum trough levels of VCM were analyzed by chemiluminescent microparticle immunoassay methods using Architect i2000SR (Abbott Laboratories, North Chicago, IL, United States). As the first sampling of serum levels of VCM was performed after administration of at least four times of VCM, all trough levels of VCM were assumed to be at a steady state. For the repeated measurement of laboratory values, only the first serum level was included in the analysis.

AKI Definitions The primary outcome was AKI as defined by the Acute Kidney Injury Network (AKIN) criteria (Mehta et al., 2007). A nephrologist examined the changes in serum creatinine (SCr) in these patients and confirmed AKI or any possible stage of nephrotoxicity induced by VCM according to the AKIN criteria: an increase in SCr of ≥0.3 mg/dl (≥26.4 μmol/L), a percentage increase in SCr of ≥50% (1.5-fold from baseline), or a reduction in urine output (documented oliguria of less than 0.5 ml/kg per hour for more than 6 h) within 48 h of VCMuse with no other apparent cause. For patients with CKD or those who underwent any form of renal replacement therapy (hemodialysis, peritoneal dialysis, or continuous renal replacement therapy (CRRT)), both the AKIN criteria and urine output-based criteria were used to confirm the occurrence of AKI.

Statistical Analysis and Machine Learning Methods Continuous variables were compared with Student’s t-test. If the variables were not normally distributed as determined by one-sample Kolmogorov-Smirnov and Levene tests, the Mann-Whitney test was performed. The Chi-square test or Fisher’s exact test was used to compare categorical variables. The area under the receiver operator characteristic curve (AUROC) was plotted to determine the cut-off values for predicting AKI. Univariate and multivariate logistic regression analyses with the odds ratio (OR) and adjusted OR (AOR), respectively, were used to identify risk factors for AKI. Statistically significant features in the multivariate analysis were used for the machine learning analysis.

Machine learning algorithms were developed to predict risk factors for AKI occurrence (Kim et al., 2021). Five-fold cross-validated multivariate logistic regression, elastic net, random forest (RF), and support vector machine (SVM) classification models were utilized. All the methods were implemented using the R package caret. For cross-validation, the dataset was randomly divided into five equal subsets. After partitioning one data sample into five subsets, one subset was selected for model validation, while the remaining subsets were used to establish machine learning models. Each cross-validation iteration was repeated 10 times to evaluate the power of the machine learning models. To assess the ability of the constructed models to predict AKI incidence, the AUROC and its 95% confidence interval (CI) of each model were calculated.

All statistical tests were two-sided, and p values <0.05 were considered statistically significant. The data were analyzed using

TABLE 1 | Association of patient characteristics with AKI.

Characteristics AKI (n = 33) Non-AKI (n = 71) p

Sex 0.587 Male 20 (60.6) 39 (54.9) Female 13 (39.4) 32 (45.1)

Age (years) 0.455 <65 16 (48.5) 40 (56.3) ≥65 17 (51.5) 31 (43.7)

Bodyweight (kg) 0.010 ≤60 21 (63.6) 26 (36.6) >60 12 (36.4) 45 (63.4)

Body mass index (kg/m2) 0.261 <18.5 7 (21.2) 9 (12.7) ≥18.5 26 (78.8) 62 (87.3)

Chronic kidney disease 0.914 Yes 3 (9.1) 6 (8.5) No 30 (90.9) 65 (91.5)

Renal replacement therapya 0.579 Yes 5 (15.2) 8 (11.3) No 28 (84.8) 63 (88.7)

Heart failure 0.529 Yes 4 (12.1) 12 (16.9) No 29 (87.9) 59 (83.1)

ICU admission 0.464 Yes 17 (51.5) 42 (59.2) No 16 (48.5) 29 (40.8)

Charlson comorbidity index 0.001 0–2 11 (33.3) 49 (69.0) ≥3 22 (66.7) 22 (31.0)

Hospital length of stay (days) 0.210 ≤45 25 (75.8) 45 (63.4) >45 8 (24.2) 26 (36.6)

Creatinine (mg/dl) 0.847 <1.2 25 (75.8) 55 (77.5) ≥1.2 8 (24.2) 16 (22.5)

eGFR (ml/min/1.73 m2) 0.740 <30 4 (12.1) 7 (9.9) ≥30 29 (87.9) 64 (90.1)

Vancomycin trough level (mcg/ml) 0.045 ≤15 14 (43.8) 46 (64.8) >15 18 (54.5) 25 (35.2)

AUC0–24h/MIC (mcg\*hr/ml) 0.141 ≤800 32 (97.0) 71 (100) >800 1 (3.0) 0 (0)

Total vancomycin dose (g) 0.118 <3 33 (100) 66 (93.0) ≥3 0 (0) 5 (7.0)

Vancomycin treatment days 0.301 ≤7 5 (15.2) 6 (8.5) >7 28 (84.8) 65 (91.5)

Number of nephrotoxic agents during vancomycin treatment 0.019 0–5 10 (30.3) 39 (54.9) ≥6 23 (69.7) 32 (45.1)

Amikacin 0.136 Yes 2 (6.1) 13 (18.3) No 31 (93.9) 58 (81.7)

Colistin 0.093 Yes 3 (9.1) 1 (1.4) No 30 (90.9) 70 (98.6)

Contrast media Yes 11 (33.3) 30 (42.3) 0.386 No 22 (66.7) 41 (57.7)

Furosemide 0.014 Yes 26 (78.8) 38 (53.5) No 7 (21.2) 33 (46.5)

(Continued on following page)

Statistical Package for Social Sciences Version 20.0 for Windows (SPSS, Chicago, IL, United States). Machine learning algorithms were constructed using R software version 3.6.0 (R Foundation for Statistical Computing, Vienna, Austria).

Data were obtained for 788 patients, of whom 684 were excluded; 335 did not have any TDM course, 215 had insufficient records, 35 had duplicate courses, 92 had a hospital length of stay <48 h, and 7 had no serum levels of VCM measured. Therefore, 104 patients were included in this study. The baseline demographic characteristics of the study patients are shown in Table 1. The incidence of VCM-associated AKI was 31.7% (33 of 104 patients). The mean age and body weight of the study population were 63.0 ± 15.6 years and 63.0 ± 14.7 kg, respectively.

In the univariate analysis, significant factors for AKI were a bodyweight of 60 kg or less, a CCI of three or higher, concomitant use of six or more nephrotoxic agents, and a serum trough level of VCM of higher than 15 μg/ml with OR values (95% CI) of 3.03 (1.28–7.14), 4.46 (1.85–10.75), 2.80 (1.17–6.74), and 2.37 (1.01–5.54), respectively (Table 2). Among individual nephrotoxic agents, furosemide and piperacillin-tazobactam significantly increased the AKI.

Using the significant features from the univariate analysis in addition to age and sex, we performed multivariate analysis and machine learning analysis. A bodyweight of 60 kg or less, a CCI of three or higher, and concomitant use of six or more nephrotoxic agents remained significant factors after the multivariate analysis with AOR values (95% CI) of 3.33 (1.25–8.84), 3.78 (1.44–9.92), and 3.18 (1.14–8.88), respectively (Table 2). The AUROC of the multivariate analysis was 0.761 (0.665–0.846). The AUROC values (mean, 95% CI) across 10 random iterations using five-fold

cross-validated multivariate logistic regression, elastic net, RF, SVM-linear kernel, and SVM-radial kernel models were 0.735 (0.638–0.833), 0.737 (0.638–0.835), 0.721 (0.610–0.833), 0.739 (0.648–0.829), and 0.733 (0.640–0.826), respectively.

A risk scoring system was constructed with the selected features from the univariate analysis. Each coefficient from the logistic regression model was divided by the smallest one and rounded to the nearest integer. A bodyweight ≤60 kg (two points), a CCI ≥3 (two points), a VCM trough serum level >15 μg/ml (one point), and concomitant use of ≥6 nephrotoxic agents (two points) were incorporated into the risk scoring system for AKI. Patients with 0–1, 2–3, 4–5, and 6–7 points had about 4.5, 21.9, 44.4, and 64.3% risk of AKI (Table 2). As shown in Figure 1, each point increase resulted in a 10% increase in AKI risk. The AUROC value of the constructed scoring system was 0.769 (95% CI: 0.674–0.863, p < 0.001).

In this study, the number of nephrotoxic agents used concomitantly with VCM, disease severity measured by the CCI, and actual patient bodyweight were significant risk factors associated with the occurrence of VCM-associated AKI.

Known risk factors for VCM-associated AKI were patient demographics (age, BMI), VCM dose (>4 g/day), VCM treatment duration (>7 days), serum trough level (>15 μg/ml), comorbidities (e.g., chronic kidney disease and heart failure), and nephrotoxic agents (e.g., aminoglycosides, colistin, contrast media, and diuretics) (Bamgbola, 2016; Karimzadeh et al., 2017; Blair et al., 2021; Higashi et al., 2021; Suzuki et al., 2021). To simplify the risk scoring system, we used CCI and the number of nephrotoxic agents rather than each comorbidity and nephrotoxic agent. For disease severity, we found that as the CCI increased, the risk of AKI also increased. Studies have reported that there were significant differences in the clinical

TABLE 1 | (Continued) Association of patient characteristics with AKI.

Characteristics AKI (n = 33) Non-AKI (n = 71) p

Piperacillin-tazobactam 0.015 Yes 19 (57.6) 23 (32.4) No 14 (42.4) 48 (67.6)

Data are presented as number (%). AUC0–24h, area under the curve from 0 to 24 h; MIC, minimum inhibitory concentration; eGFR, estimated glomerular filtration rate. aRenal replacement therapy includes hemodialysis, peritoneal dialysis, and continuous renal replacement therapy.

TABLE 2 | Univariate and multivariable analyses and score.

Predictors Unadjusted OR (95% CI)

Adjusted OR (95% CI) Score

Bodyweight (kg) ≤60 3.03 (1.28–7.14) 3.33 (1.25–8.84)a 2 Charlson comorbidity index ≥3 4.46 (1.85–10.75) 3.78 (1.44–9.92)b 2 Number of nephrotoxic agents during vancomycin treatment ≥6 2.80 (1.17–6.74) 3.18 (1.14–8.88)a 2 Serum trough level of vancomycin (mcg/ml) >15 2.37 (1.01–5.54) 2.00 (0.76–5.26) 1

OR, odds ratio; CI, confidence interval. ap < 0.05. bp < 0.01.

https://lh3.googleusercontent.com/notebooklm/AKXwDQEaYVOqT7bgrt3bI3dH1tWX9X-JccwbEnSq4FlJKzBeI4SmDaGmkusd5oazcYO\_LwSAvKXaG3PQP-lBH-5Xl9ABcWZ\_vHfKyptqdeuM6wALF4BtVFeXBfISRV6OTYNd9EFLRKa6og=w1305-h780-v0

0f75d4bc-6268-4a9d-a2f6-63c3ffd04eb2

outcomes of patients treated with VCM according to CCI scores (Covert et al., 2020). The CCI incorporates various states such as age, cancer, chronic heart failure, chronic obstructive pulmonary disease, or diabetes mellitus (Charlson et al., 1987). Based on our results, we can stratify the patient population and differentiate the VCM treatment based on CCI for better efficacy and safety.

Regarding bodyweight, a bodyweight ≤60 kg was significantly associated with an increased incidence of AKI. When considering that higher exposure of VCM (e.g., dose, trough concentration, and AUC) was related to VCM-associated AKI (Wong-Beringer et al., 2011; Rostas et al., 2014; Zasowski et al., 2017), the lower the weight, the higher the risk of overdose. This can be also explained by the estimation of glomerular filtration rate (eGFR) as determined using the Modification of Diet in Renal Disease (MDRD) formula (Levey et al., 1999) and the nature of our study population. According to the MDRD eGFR formula, glomerular filtration is negatively related to the serum creatinine level, age, and sex. In this study, the patient group with a bodyweight ≤60 kg had higher proportions of females, those ≥65 years, and those with an intensive care unit admission than the patient group with a bodyweight >60 kg. Therefore, the patient group with a bodyweight ≤60 kg had a slower GFR than the patient group with a bodyweight >60 kg, which can increase the risk of AKI. This result is in line with the findings of previous studies, which reported that a lower body mass index (BMI) is a risk factor for AKI in Asian patients (Liu et al., 2018).

The serum trough levels of VCM were significantly associated with AKI in the univariate analysis; however, statistical significance was not found in the multivariate analysis. We included the serum trough level as a risk factor for the scoring system since higher serum trough levels of VCM were associated with an increased incidence of nephrotoxicity (Bosso et al., 2011; van Hal et al., 2013; Rybak et al., 2020).

The AUROC values indicated the favorable performance of these models, regardless of the machine learning method used in

this study (higher than 0.7). The elastic net is a penalized linear regression model that combines the penalties of the lasso and ridge methods (Zou and Hastie, 2005). RF is an ensemble method that increases the diversity by using a random subset of available features at each node and provides a more accurate prediction than a single decision tree (Breiman et al., 1984; Breiman, 2001; Hastie et al., 2009). In this study, SVMs were implemented using linear and radial basis function kernels. Linear kernel SVMs have a single tuning parameter, C, which is the cost parameter of the error term, whereas radial kernel SVMs have an additional hyperparameter, sigma, which determines the width for Gaussian distribution (Cortes and Vapnik, 1995; Hastie et al., 2009).

This study has several limitations. First, it has a small sample size with single-center cohort data and retrospective design. Second, we did not evaluate the severity and prognosis of AKI. Third, we did not perform the renal biopsy for identifying if it is a dose-independent acute tubulointerstitial nephritis or a dose-dependent renal tubular injury. Fourth, AKI was defined according to AKIN (Mehta et al., 2007) rather than other criteria (e.g., RIFLE (Bellomo et al., 2004), KDIGO (Kidney Disease: Improving, 2012), and ASHP (Rybak et al., 2009)), which may cause heterogeneity and need cautions in the interpretation. However, our results have strengths in the methodologies used to develop a scoring system and incorporate various types of possible nephrotoxic agents. Moreover, we included patients with CKD and found that their renal impairment status was not significantly related to the risk of AKI. The broad spectrum of diseases in our studied population, which included patients with CKD, is notable in that previous studies have mainly dealt with patients with CKD patients alone or excluded these renally impaired populations (Liu et al., 2018; Freitas et al., 2020; Gaggl et al., 2020; Imai et al., 2020). Thus, our scoring system for AKI can be generalized to patients with various types and severities of diseases.

FIGURE 1 | Risk (%) of vancomycin-associated acute kidney injury according to scores.

In this study, we aimed to develop an optimal scoring system for predicting VCM-associated AKI using machine learning methods. To the best of our knowledge, this is the first study to propose a risk scoring system for VCM-associated AKI in Korean patients undergoing TDM with concomitant use of various nephrotoxic agents. Moreover, our studied patients had varied disease types such as sepsis, osteomyelitis, central nervous system infections, pneumonia, and CKD of various stages and were undergoing renal replacement therapies. Thus, our results can be used to develop guidelines or effective treatment strategies for VCM use in adult patients who are receiving nephrotoxic agents. Further studies using a larger population are needed to confirm our results.

DATA AVAILABILITY STATEMENT

The raw data supporting the conclusions of this article will be made available by the authors, without undue reservation.

ETHICS STATEMENT

The studies involving human participants were reviewed and approved by the Institutional Review Board of Catholic

Kwandong University International St. Mary’s Hospital. Written informed consent for participation was not required for this study in accordance with the national legislation and the institutional requirements.

AUTHOR CONTRIBUTIONS

All the authors have made substantial contributions to the conception of the study. JK, JY, and HG contributed to designing the study. JK and KK contributed to the acquisition and analysis of data. JY and HG contributed to the interpretation of data. JK and JY contributed to the drafting of the manuscript. HG contributed to the critical revision of the manuscript. All authors approved the final manuscript.

We did not receive any fundings.

SUPPLEMENTARY MATERIAL

The SupplementaryMaterial for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fphar.2022.815188/ full#supplementary-material

Bamgbola, O. (2016). Review of Vancomycin-Induced Renal Toxicity: an Update. Ther. Adv. Endocrinol. Metab. 7, 136–147. doi:10.1177/2042018816638223

Bellomo, R., Ronco, C., Kellum, J. A., Mehta, R. L., and Palevsky, P. (2004). Acute Renal Failure - Definition, Outcome Measures, Animal Models, Fluid Therapy and Information Technology Needs: the Second International Consensus Conference of the Acute Dialysis Quality Initiative (ADQI) Group. Crit. Care 8 (4), R204–R212. doi:10.1186/cc2872

Blair, M., Côté, J. M., Cotter, A., Lynch, B., Redahan, L., and Murray, P. T. (2021). Nephrotoxicity from Vancomycin Combined with Piperacillin-Tazobactam: a Comprehensive Review. Am. J. Nephrol. 52, 85–97. doi:10.1159/000513742

Bosso, J. A., Nappi, J., Rudisill, C., Wellein, M., Bookstaver, P. B., Swindler, J., et al. (2011). Relationship between Vancomycin Trough Concentrations and Nephrotoxicity: a Prospective Multicenter Trial. Antimicrob. Agents Chemother. 55, 5475–5479. doi:10.1128/AAC.00168-11

Breiman, L., Friedman, J., Stone, C., and Olshen, R. (1984). Classification and Regression Trees. London: Chapman & Hall.

Breiman, L. (2001). Random Forests. Mach Learn. 45, 5–32. doi:10.1023/a: 1010933404324

Charlson, M. E., Pompei, P., Ales, K. L., and MacKenzie, C. R. (1987). A New Method of Classifying Prognostic Comorbidity in Longitudinal Studies: Development and Validation. J. Chronic Dis. 40, 373–383. doi:10.1016/0021-9681(87)90171-8

Cortes, C., and Vapnik, V. (1995). Support-vector Networks. Mach Learn. 20, 273–297. doi:10.1007/bf00994018

Covert, K. L., Knoetze, D., Cole, M., and Lewis, P. (2020). Vancomycin Plus Piperacillin/tazobactam and Acute Kidney Injury Risk: A Review of the Literature. J. Clin. Pharm. Ther. 45, 1253–1263. doi:10.1111/jcpt.13249

Deresinski, S. (2009). Vancomycin in Combination with Other Antibiotics for the Treatment of Serious Methicillin-Resistant Staphylococcus aureus Infections. Clin. Infect. Dis. 49, 1072–1079. doi:10.1086/605572

Filippone, E. J., Kraft, W. K., and Farber, J. L. (2017). The Nephrotoxicity of Vancomycin. Clin. Pharmacol. Ther. 102, 459–469. doi:10.1002/cpt.726

Finch, N. A., Zasowski, E. J., Murray, K. P., Mynatt, R. P., Zhao, J. J., Yost, R., et al. (2017). A Quasi-experiment to Study the Impact of Vancomycin Area under the Concentration-Time Curve-Guided Dosing on Vancomycin-Associated Nephrotoxicity. Antimicrob. Agents Chemother. 61, e01293–17. doi:10.1128/ AAC.01293-17

Freitas, F. M., Zamoner, W., Reis, P. F. D., Balbi, A. L., and Ponce, D. (2020). Vancomycin for Dialytic Therapy in Critically Ill Patients: Analysis of its Reduction and the Factors Associated with Subtherapeutic Concentrations. Int. J. Environ. Res. Public Health 17, 6861. doi:10.3390/ijerph17186861

Gaggl, M., Pate, V., Stürmer, T., Kshirsagar, A. V., and Layton, J. B. (2020). The Comparative Risk of Acute Kidney Injury of Vancomycin Relative to Other Common Antibiotics. Sci. Rep. 10, 17282. doi:10.1038/s41598-020-73687-9

Ghasemiyeh, P., Vazin, A., Zand, F., Azadi, A., Karimzadeh, I., and Mohammadi-Samani, S. (2020). A Simple and Validated HPLC Method for Vancomycin Assay in Plasma Samples: the Necessity of TDM center Development in Southern Iran. Res. Pharm. Sci. 15, 529–540. doi:10.4103/1735-5362.301337

Gyamlani, G., Potukuchi, P. K., Thomas, F., Akbilgic, O., Soohoo, M., Streja, E., et al. (2019). Vancomycin-associated Acute Kidney Injury in a Large Veteran Population. Am. J. Nephrol. 49, 133–142. doi:10.1159/000496484

Hastie, T., Tibshirani, R., and Friedman, J. (2009). The Elements of Statistical Learning: Data Mining, Inference and Prediction. 2nd ed. New York: Springer.

Higashi, T., Tsukamoto, H., Kodawara, T., Igarashi, T., Watanabe, K., Yano, R., et al. (2021). Evaluation of Risk Factors for Nephrotoxicity Associated with High-Dose Vancomycin in Japanese Patients. Pharmazie 76, 114–118. doi:10. 1691/ph.2021.0138

Imai, S., Takekuma, Y., Kashiwagi, H., Miyai, T., Kobayashi, M., Iseki, K., et al. (2020). Validation of the Usefulness of Artificial Neural Networks for Risk Prediction of Adverse Drug Reactions Used for Individual Patients in Clinical Practice. PLoS One 15, e0236789. doi:10.1371/journal.pone.0236789

Jeffres, M. N. (2017). The Whole price of Vancomycin: Toxicities, Troughs, and Time. Drugs 77, 1143–1154. doi:10.1007/s40265-017-0764-7

Karimzadeh, I., Haghighati, G., Ramzi, M., Sagheb, M. M., and Zomorodian, K. (2017). Assessing the Epidemiology of Nephrotoxicity and the Role of Urinary Kidney Injury Molecule 1 as a Biomarker of Renal Function in Hematologic-Oncologic Patients under Vancomycin Treatment in Shiraz, Iran. Iran Red Crescent Med. J. 19, e40858.

Kidney Disease: Improving Global Outcomes (KDIGO) Acute Kidney InjuryWork Group (2012). KDIGO Clinical Practice Guideline for Acute Kidney Injury. Kidney Inter. 2, 1–138.

Kim, J. W., Yee, J., Oh, S. H., Kim, S. H., Kim, S. J., Chung, J. E., et al. (2021). Machine Learning Approaches for Predicting Bisphosphonate-Related Osteonecrosis in Women with Osteoporosis Using VEGFA Gene Polymorphisms. J. Pers Med. 11, 541. doi:10.3390/jpm11060541

Levey, A. S., Bosch, J. P., Lewis, J. B., Greene, T., Rogers, N., and Roth, D. (1999). A More Accurate Method to Estimate Glomerular Filtration Rate from Serum Creatinine: a New Prediction Equation. Modification of Diet in Renal Disease Study Group. Ann. Intern. Med. 130, 461–470. doi:10.7326/0003-4819-130-6-199903160-00002

Levey, A. S., Eckardt, K. U., Tsukamoto, Y., Levin, A., Coresh, J., Rossert, J., et al. (2005). Definition and Classification of Chronic Kidney Disease: a Position Statement from Kidney Disease: Improving Global Outcomes (KDIGO). Kidney Int. 67, 2089–2100. doi:10.1111/j.1523-1755.2005.00365.x

Liu, A. Y. L., Wang, J., Nikam, M., Lai, B. C., and Yeoh, L. Y. (2018). Low, rather Than High, Body Mass Index Is a Risk Factor for Acute Kidney Injury in Multiethnic Asian Patients: A Retrospective Observational Study. Int. J. Nephrol. 2018, 3284612. doi:10.1155/2018/3284612

Mehta, R. L., Cerdá, J., Burdmann, E. A., Tonelli, M., García-García, G., Jha, V., et al. (2015). International Society of Nephrology’s 0by25 Initiative for Acute Kidney Injury (Zero Preventable Deaths by 2025): a Human Rights Case for Nephrology. Lancet 385, 2616–2643. doi:10.1016/S0140-6736(15)60126-X

Mehta, R. L., Kellum, J. A., Shah, S. V., Molitoris, B. A., Ronco, C., Warnock, D. G., et al. (2007). Acute Kidney Injury Network: Report of an Initiative to Improve Outcomes in Acute Kidney Injury. Crit. Care 11, R31. doi:10.1186/cc5713

O’Donnell, J. N., Rhodes, N. J., Miglis, C. M., Catovic, L., Liu, J., Cluff, C., et al. (2018). Dose, Duration, and Animal Sex Predict Vancomycin-Associated Acute Kidney Injury in Preclinical Studies. Int. J. Antimicrob. Agents 51, 239–243. doi:10.1016/j.ijantimicag.2017.08.012

Poston-Blahnik, A., and Moenster, R. (2021). Association between Vancomycin Area under the Curve and Nephrotoxicity: a Single center, Retrospective Cohort Study in a Veteran Population.Open Forum Infect. Dis. 8, ofab094. doi:10.1093/ ofid/ofab094

Qin, X., Tsoi, M. F., Zhao, X., Zhang, L., Qi, Z., and Cheung, B. M. Y. (2020). Vancomycin-associated Acute Kidney Injury in Hong Kong in 2012-2016. BMC Nephrol. 21, 41. doi:10.1186/s12882-020-1704-4

Rostas, S. E., Kubiak, D. W., and Calderwood, M. S. (2014). High-dose Intravenous Vancomycin Therapy and the Risk of Nephrotoxicity. Clin. Ther. 36, 1098–1101. doi:10.1016/j.clinthera.2014.05.011

Rutter, W. C., Cox, J. N., Martin, C. A., Burgess, D. R., and Burgess, D. S. (2017). Erratum for Rutter et al., Nephrotoxicity during Vancomycin Therapy in Combination with Piperacillin-Tazobactam or Cefepime. Antimicrob. Agents Chemother. 61, e02089–16. doi:10.1128/AAC.02089-1610.1128/AAC.00314-17

Rybak, M., Lomaestro, B., Rotschafer, J. C., Moellering, R., Craig, W., Billeter, M., et al. (2009). Therapeutic Monitoring of Vancomycin in Adult Patients: a Consensus Review of the American Society of Health-System

Pharmacists, the Infectious Diseases Society of America, and the Society of Infectious Diseases Pharmacists. Am. J. Health Syst. Pharm. 66, 82–98. doi:10.2146/ajhp080434

Rybak, M. J., Le, J., Lodise, T. P., Levine, D. P., Bradley, J. S., Liu, C., et al. (2020). Therapeutic Monitoring of Vancomycin for Serious Methicillin-Resistant Staphylococcus aureus Infections: A Revised Consensus Guideline and Review by the American Society of Health-System Pharmacists, the Infectious Diseases Society of America, the Pediatric Infectious Diseases Society, and the Society of Infectious Diseases Pharmacists. Am. J. Health Syst. Pharm. 77, 835–864. doi:10.1093/ajhp/zxaa036

See, Y. P., Young, B. E., Ang, L. W., Ooi, X. Y., Chan, C. P., Looi, W. L., et al. (2021). Risk Factors for Development of Acute Kidney Injury in COVID-19 Patients: a Retrospective Observational Cohort Study.Nephron 145, 256–264. doi:10.1159/ 000514064

Suzuki, A., Hamada, Y., Ikeda, H., Tanaka, H., Yanagihara, M., Namiki, M., et al. (2021). Comparison of Trough Concentration and Area under the Curve of Vancomycin Associated with the Incidence of Nephrotoxicity and Predictors of a High Trough Level. J. Infect. Chemother. 27, 455–460. doi:10.1016/j.jiac.2020. 10.014

van Hal, S. J., Paterson, D. L., and Lodise, T. P. (2013). Systematic Review and Meta-Analysis of Vancomycin-Induced Nephrotoxicity Associated with Dosing Schedules that Maintain Troughs between 15 and 20 Milligrams Per Liter. Antimicrob. Agents Chemother. 57, 734–744. doi:10.1128/AAC.01568-12

Wang, H. E., Muntner, P., Chertow, G. M., and Warnock, D. G. (2012). Acute Kidney Injury and Mortality in Hospitalized Patients. Am. J. Nephrol. 35, 349–355. doi:10.1159/000337487

Wong-Beringer, A., Joo, J., Tse, E., and Beringer, P. (2011). Vancomycin-associated Nephrotoxicity: a Critical Appraisal of Risk with High-Dose Therapy. Int. J. Antimicrob. Agents 37, 95–101. doi:10.1016/j.ijantimicag.2010.10.013

Zasowski, E. J., Murray, K. P., Trinh, T. D., Finch, N. A., Pogue, J. M., Mynatt, R. P., et al. (2017). Identification of Vancomycin Exposure-Toxicity Thresholds in Hospitalized Patients Receiving Intravenous Vancomycin. Antimicrob. Agents Chemother. 62, e01684–17. doi:10.1128/AAC.01684-17

Zou, H., and Hastie, T. (2005). Regularization and Variable Selection via the Elastic Net. J. R. Stat. Soc B 67, 301–320. doi:10.1111/j.1467-9868.2005.00503.x

Conflict of Interest: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

Publisher’s Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Copyright © 2022 Kim, Kim, Yee and Gwak. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.