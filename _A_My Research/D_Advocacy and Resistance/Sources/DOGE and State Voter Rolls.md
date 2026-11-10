---
tags:
  - notebooklm-import
notebook: "D_Advocacy and Resistance"
category: "research"
---

Skip to content Home

* Link to link
* Link to facebook
* Link to linkedin
* Link to instagram

1. The Threat
2. The Strategy
3. Our Impact
4. Our WorkOur Impact
5. Latest Updates
6. Protecting Free & Fair Elections
7. Defending the Rule of Law
8. Safeguarding the Public Square
9. Shaping the Democracy of Tomorrow
10. News & ResourcesResearch & Analysis
11. The Authoritarian Playbook
12. How You Can Protect Democracy
13. The Faithful Fight Toolkits
14. Find an ExpertProtecting Free & Fair Elections
15. Safeguarding the Public Square
16. Defending the Rule of Law
17. Shaping the Democracy of Tomorrow
18. AboutAbout Us
19. Our Team
20. Our Advisors and Board
21. Our Cross-Ideological Strategy
22. Careers

### Site Menu Close Menu DOGE and State Voter Rolls

* Protecting Elections
* Research & Analysis
* Analysis
* July 15, 2025
* Share
  *While efforts by the Trump administration to expand an immigration data system for verifying voting eligibility might initially sound sensible, it is a solution in search of a problem.* *The administration is creating a massive surveillance system on Americans in search of a needle in a haystack. More technically, the system’s complexity and the Department of Government Efficiency’s (DOGE) inexperience and poor record for accuracy make this a high-stakes recipe for technical problems — and one where American citizens are likely to be unfairly ensnared in the process.*

#### Executive summary

* Noncitizen voting is extremely rare, but has become a major focus among those questioning the validity of U.S. elections. The states already have processes to verify the citizenship of voter registrants and the federal government has historically shared citizenship data cautiously, aware of its systems’ limitations and the potential to disenfranchise U.S. citizens.
* DOGE and the Department of Homeland Security (DHS) have [recently expanded](https://www.uscis.gov/newsroom/news-releases/uscis-deploys-common-sense-tools-to-verify-voters) an existing U.S. Citizenship and Immigration Services (USCIS) system (SAVE) to address noncitizen voting without providing much information on how this was accomplished or the accuracy of the resulting tools.
* These efforts involve complex technical challenges that, when previously attempted, have resulted in [errors](https://ohiocapitaljournal.com/2024/09/04/citizens-caught-in-ohio-noncitizen-voting-audit-say-latest-letter-offers-incomplete-information/) and [disenfranchisement](https://www.npr.org/2024/10/29/nx-s1-5169204/virginia-noncitizen-voter-purge) of [American](https://www.votebeat.org/texas/2024/10/15/greg-abbott-noncitizen-voter-roll-removal-investigation/)[citizens](https://www.votebeat.org/texas/2024/10/15/greg-abbott-noncitizen-voter-roll-removal-investigation/).
* When external non-experts get involved in maintaining a state’s voter rolls, they have consistently gotten it wrong. DOGE specifically does not have a good track record in dealing with large and complex systems. They have [mistakenly fired crucial federal employees](https://www.forbes.com/sites/saradorn/2025/04/04/trumps-great-rehiring-over-26000-fired-by-doge-likely-to-return-so-far/), consistently [misinterpreted Social Security data](https://www.wired.com/story/elon-musk-doge-social-security-150-year-old-benefits/), and have been [accused of illegally misusing sensitive personal information](https://health.wusf.usf.edu/2025-04-11/how-doge-may-have-improperly-used-social-security-data-to-push-voter-fraud-narratives).
* Because the potential consequence of failure is the disenfranchisement of American citizens, we must ensure the absolute highest level of confidence when removing records from the voter rolls. To date, neither the Social Security Administration (SSA), DHS, nor DOGE have offered any information concerning how the new SAVE expansions were implemented, nor have they provided any evidence confirming the new system’s accuracy.
* Until such transparency and verification have been established, it would be irresponsible to consider this new system as the final source of truth when it comes to voter eligibility.

#### Background

While the [data](https://www.brennancenter.org/our-work/research-reports/noncitizen-voting-missing-millions)[consistently](https://www.brennancenter.org/our-work/research-reports/noncitizen-voting-missing-millions)[show](https://www.brennancenter.org/our-work/research-reports/noncitizen-voting-missing-millions) that it is so rare as to be virtually nonexistent, inflammatory rhetoric surrounding noncitizen voting has emerged as a central component of the decreased confidence in our elections. States already take many steps to confirm the citizenship of those who register to vote, like cross-checking DMV records or jury duty surveys. The federal government has also long shared information on citizenship status with the states, but it has done so in a careful way and with a recognition of the inherent deficiencies of their data systems.

###### Want more Democracy Insights?

###### [Subscribe to our weekly newsletter](https://www.brennancenter.org/our-work/research-reports/noncitizen-voting-missing-millions)

On March 25, Trump issued an [executive order](https://www.whitehouse.gov/presidential-actions/2025/03/preserving-and-protecting-the-integrity-of-american-elections/) that directed DHS and DOGE to review states’ public voter rolls and identify individuals who are illegally registered to vote. DOGE initially announced [57 referrals](https://www.nbcnews.com/politics/trump-administration/live-blog/trump-administration-tariffs-economy-musk-immigration-live-updates-rcna203237#rcrd78221) (among the 5 million Enumeration-Beyond-Entry [EBE] enrollees or 0.00114%) for prosecution of noncitizens who voted, which were likely identified from matching individuals with specific immigrant-issued Social Security numbers to state-level voter records. For perspective, a well-conducted DNA test has a likelihood of false positives at around .001%,
Soon after, DHS and DOGE [announced an update](https://www.uscis.gov/newsroom/news-releases/uscis-deploys-common-sense-tools-to-verify-voters) to an immigration data system (SAVE) that integrated information from the SSA meant “to help verify U.S. citizenship and prevent aliens from voting in American elections.”
These moves may seem like common sense, but they are, in fact, technically complex. Compounding the issue, the process was executed hastily, with a timeline of less than four months, by actors with less-than-exceptional track records and limited familiarity with the data. In data science, things are never simple, especially when dealing with disparate and siloed data – data that does not “talk” to each other – which makes integration and analysis all the more challenging. While access to more accurate and intelligible data could be invaluable to election administrators, it is far from clear that that is what the federal government is offering in this instance.

#### Technical challenges

The commonality of biographical information (names and birthdays) [can lead to significant false positives](http://www.asasrms.org/Proceedings/y2010/Files/307481_58657.pdf) when two datasets being matched do not contain the same unique record-level identifier. Such false positives could incorrectly identify U.S. citizens as noncitizens. Due to the lack of transparency, we have no information on how disparate datasets at SSA and USCIS were matched, nor do we have any information on accuracy testing that may or may not have been performed. This is further complicated by unavoidable errors in large datasets that occur when people make mistakes filling out forms or entering data into databases. Even if these mistakes are eventually corrected, incorrect data can still be propagated to other databases and systems, especially when engaging in careless matching. SAVE is also known to [contain outdated citizenship information](https://s3.amazonaws.com/dl.ncsbe.gov/sboe/Post-Election%20Audit%20Report_2016%20General%20Election/Post-Election_Audit_Report.pdf) for naturalized citizens, frequently incorrectly indicating that they are noncitizens. Given that more than [7.9 million](https://www.uscis.gov/citizenship-resource-center/naturalization-statistics) people have been naturalized in the last decade, the scale of this issue is not insignificant.
**Read more: The DOGE Debacle**  [Read more: The DOGE Debacle](https://www.uscis.gov/citizenship-resource-center/naturalization-statistics) 
These types of complications were at the root of the Kansas Crosscheck program’s failures, which was [found to be 99% inaccurate](https://archive.ph/0T7ue) when trying to identify ineligible voters. We’ve also seen similar failures across several states:

* **Ohio** : Incorrectly challenged several [naturalized U.S. citizens](https://ohiocapitaljournal.com/2024/09/04/citizens-caught-in-ohio-noncitizen-voting-audit-say-latest-letter-offers-incomplete-information/) in the lead up to 2024. In 2023 521 cases were referred; only [one person was ultimately prosecuted](https://ohiocapitaljournal.com/2023/09/27/ohio-sec-of-state-larose-flagged-more-than-520-cases-of-noncitizen-voter-fraud-only-one-was-legit/).
* **Alabama** : [3,251 inactivated](https://www.npr.org/2024/08/30/nx-s1-5091032/noncitizens-voting-election-gop-texas-tennessee-alabama); at least [2,074 were citizens](https://www.npr.org/2024/10/12/nx-s1-5147789/voting-election-2024-noncitizen-fact-check-trump).
* **Virginia** : [Multiple](https://www.npr.org/2024/10/29/nx-s1-5169204/virginia-noncitizen-voter-purge)[verified](https://www.npr.org/2024/10/29/nx-s1-5169204/virginia-noncitizen-voter-purge) U.S. [citizens](https://www.npr.org/2024/10/29/nx-s1-5169204/virginia-noncitizen-voter-purge) were removed in a last-minute purge.
* **Texas** : [Thousands of cancellations](https://www.votebeat.org/texas/2024/10/15/greg-abbott-noncitizen-voter-roll-removal-investigation/); only 581 confirmed noncitizens on the rolls over 3 years (out of more than 18 million voters).

#### Unreliable actors

Voter registration systems are complex, vary by state, and require extensive expertise to understand and manage effectively. Whether it was [Crosscheck](https://archive.ph/0T7ue), [Cyber Ninjas](https://elections.maricopa.gov/asset/jcr:a9e03750-0a8f-4162-859f-1d46ac54b485/Correcting%20The%20Record%20-%20January%202022%20Report.pdf), or [EagleAI](https://www.nbcnews.com/politics/elections/conservative-activists-errors-software-voter-fraud-rcna161028), when external non-experts get involved in the maintenance of a state’s voter rolls, they simply get it wrong. Getting it wrong here means that American citizens could be disenfranchised. In this specific instance, implementation is in the hands of DOGE, which has unabashedly embraced a [‘move fast, break things’ approach](https://www.washingtonpost.com/technology/2025/02/24/doge-fast-cuts-federal-workers-programs-elon-musk/). There are serious concerns that in moving fast to integrate two massive legacy systems (SSA and SAVE) originally built for wholly different purposes, what DOGE may have [broken is the underlying accuracy of the information](https://www.opb.org/article/2025/06/29/trump-dhs-links-data-for-new-citizenship-tracking-tool/) they are making available.
**Read more: DOGE’s data “panopticon” pales compared to what’s next**  [Read more: DOGE’s data “panopticon” pales compared to what’s next](https://www.opb.org/article/2025/06/29/trump-dhs-links-data-for-new-citizenship-tracking-tool/) 
This tendency to ignore future consequences was particularly apparent when the federal government had to [rehire thousands of critical workers mistakenly fired by DOGE](https://www.forbes.com/sites/saradorn/2025/04/04/trumps-great-rehiring-over-26000-fired-by-doge-likely-to-return-so-far/), including [health workers](https://www.cbsnews.com/news/rfk-jr-hhs-job-cuts-doge-mistakes/) at the Centers for Disease Control and [weapons inspectors](https://www.cnn.com/2025/02/17/climate/trump-nnsa-nuclear-staff-reinstated/index.html) at the National Nuclear Security Administration. DOGE’s handling and discussion of federal data reveals similar carelessness. [Musk’s claim](https://www.foxbusiness.com/politics/musk-claims-150-year-olds-receiving-social-security-benefits) that DOGE uncovered 150-year-olds receiving Social Security benefits, for instance, resulted from a misunderstanding of how the [database language dealt with birth dates](https://www.wired.com/story/elon-musk-doge-social-security-150-year-old-benefits/) and [how eligibility for benefits is determined](https://www.cbsnews.com/news/social-security-doge-100-150-year-olds-cobol-elon-musk/). More troubling, evidence suggests DOGE staffers may have [accessed sensitive personal information](https://health.wusf.usf.edu/2025-04-11/how-doge-may-have-improperly-used-social-security-data-to-push-voter-fraud-narratives) from SSA data in contravention of a federal court’s order. All of this suggests that DOGE’s claims regarding uncovering noncitizen voter fraud and creating an expanded SAVE system cannot be taken at face value and must be subject to significant transparency and verification.

#### High stakes

Although noncitizen voting remains [“vanishingly rare,”](https://abcnews.go.com/US/election-fact-check-noncitizens-vote-instances-vanishingly-rare/story?id=115025674) false narratives about its prevalence have gained traction, with [polls showing a majority of Americans](https://www.npr.org/2024/10/03/nx-s1-5130284/election-concerns-voter-fraud-trump-harris-poll) having concerns about noncitizens voting in the 2024 presidential race. In this moment when election officials are facing significant pressure to implement some form of citizen verification, we should remain vigilant in ensuring that the tools we employ do not cause harm to eligible citizens. As those who work with ‘big data’ will know, systems at this scale can never be perfect and demand a level of expertise and area-specific knowledge to be leveraged successfully. Furthermore, the cost of failure is high. Not only will an unreliable system add significant complications to the work of state and local election administrators, but it will also burden an unknown number of legitimate citizens, potentially depriving them of their right to vote.

#### Join Us.

Building a stronger, more resilient democracy is possible, but we can’t do it alone. Become part of the fight today.
 [Donate](https://www.npr.org/2024/10/03/nx-s1-5130284/election-concerns-voter-fraud-trump-harris-poll)  Sign Up for Updates  [Sign Up for Updates](https://protectdemocracy.org/get-updates/) 
Explore Careers  [Explore Careers](https://protectdemocracy.recruitee.com/) 
How to Protect Democracy  [How to Protect Democracy](https://protectdemocracy.org/about/democracy-playbook/) 
Follow Us

* [Link to link](https://protectdemocracy.org/about/democracy-playbook/)
* [Link to facebook](https://protectdemocracy.org/about/democracy-playbook/)
* [Link to linkedin](https://protectdemocracy.org/about/democracy-playbook/)
* [Link to instagram](https://protectdemocracy.org/about/democracy-playbook/)
  Protect Democracy United is a registered 501(c)(4) social welfare organization. Protect Democracy Project is a registered 501(c)(3) charitable organization. Learn about the difference [here](https://protectdemocracy.org/about/#c3-c4).
  [Privacy Policy](https://protectdemocracy.org/about/#c3-c4) / [Terms of Use](https://protectdemocracy.org/terms-and-conditions-of-use/)
  © Protect Democracy United. All Rights reserved. 2025

#### Mobile Menu Overlay

1. [Site Menu Close Menu](https://protectdemocracy.org/terms-and-conditions-of-use/) [The Threat](https://protectdemocracy.org/terms-and-conditions-of-use/)
2. [The Strategy](https://protectdemocracy.org/terms-and-conditions-of-use/)
3. [Our Impact](https://protectdemocracy.org/terms-and-conditions-of-use/)
4. [Our Work](https://protectdemocracy.org/terms-and-conditions-of-use/)[Our Impact](https://protectdemocracy.org/terms-and-conditions-of-use/)
5. [Latest Updates](https://protectdemocracy.org/terms-and-conditions-of-use/)
6. [Protecting Free & Fair Elections](https://protectdemocracy.org/terms-and-conditions-of-use/)
7. [Defending the Rule of Law](https://protectdemocracy.org/terms-and-conditions-of-use/)
8. [Safeguarding the Public Square](https://protectdemocracy.org/terms-and-conditions-of-use/)
9. [Shaping the Democracy of Tomorrow](https://protectdemocracy.org/terms-and-conditions-of-use/)
10. [News & Resources](https://protectdemocracy.org/terms-and-conditions-of-use/)[Research & Analysis](https://protectdemocracy.org/terms-and-conditions-of-use/)
11. [The Authoritarian Playbook](https://protectdemocracy.org/terms-and-conditions-of-use/)
12. [How You Can Protect Democracy](https://protectdemocracy.org/terms-and-conditions-of-use/)
13. [The Faithful Fight Toolkits](https://protectdemocracy.org/terms-and-conditions-of-use/)
14. [Find an Expert](https://protectdemocracy.org/terms-and-conditions-of-use/)[Protecting Free & Fair Elections](https://protectdemocracy.org/terms-and-conditions-of-use/)
15. [Safeguarding the Public Square](https://protectdemocracy.org/terms-and-conditions-of-use/)
16. [Defending the Rule of Law](https://protectdemocracy.org/terms-and-conditions-of-use/)
17. [Shaping the Democracy of Tomorrow](https://protectdemocracy.org/terms-and-conditions-of-use/)
18. [About](https://protectdemocracy.org/terms-and-conditions-of-use/)[About Us](https://protectdemocracy.org/terms-and-conditions-of-use/)
19. [Our Team](https://protectdemocracy.org/terms-and-conditions-of-use/)
20. [Our Advisors and Board](https://protectdemocracy.org/terms-and-conditions-of-use/)
21. [Our Cross-Ideological Strategy](https://protectdemocracy.org/terms-and-conditions-of-use/)
22. [Careers](https://protectdemocracy.org/terms-and-conditions-of-use/)

* [Link to link](https://protectdemocracy.org/terms-and-conditions-of-use/)
* [Link to facebook](https://protectdemocracy.org/terms-and-conditions-of-use/)
* [Link to linkedin](https://protectdemocracy.org/terms-and-conditions-of-use/)
* [Link to instagram](https://protectdemocracy.org/terms-and-conditions-of-use/)