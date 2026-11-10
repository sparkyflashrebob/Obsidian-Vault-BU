---
tags:
  - notebooklm-import
notebook: "C_Game Theory"
category: "research"
---

##### A Short Introduction to Game Theory

Heiko Hotz
CONTENTS 1
Contents
1 Introduction 2 1.1 Game Theory – What is it? . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 Game Theory – Where is it applied? . . . . . . . . . . . . . . . . . . . . . . 2
2 Definitions 3 2.1 Normal Form Games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 2.2 Extensive Form Games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 2.3 Nash Equilibrium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.3.1 Best Response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 2.3.2 Localizing a Nash Equilibrium in a Payoff-matrix . . . . . . . . . . . 4
2.4 Mixed Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3 Games 5 3.1 Prisoner’s Dilemma (PD) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.1.1 Other Interesting Two-person Games . . . . . . . . . . . . . . . . . . 6 3.2 The Ultimatum Game . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 3.3 Public Good Game . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 3.4 Rock, Paper, Scissors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
4 Evolutionary Game Theory 8 4.1 Why EGT? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 4.2 Evolutionary Stable Strategies . . . . . . . . . . . . . . . . . . . . . . . . . 9
4.2.1 ESS and Nash Equilibrium . . . . . . . . . . . . . . . . . . . . . . . 9 4.2.2 The Hawk-Dove Game . . . . . . . . . . . . . . . . . . . . . . . . . . 9 4.2.3 ESS of the Hawk-Dove Game . . . . . . . . . . . . . . . . . . . . . . 10
4.3 The Replicator Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 4.4 ESS and Replicator Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . 11
5 Applications 12 5.1 Evolution of cooperation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 5.2 Biodiversity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
A Mathematical Derivation 14 A.1 Normal form games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14 A.2 Nash equilibrium and best answer . . . . . . . . . . . . . . . . . . . . . . . 14 A.3 Evolutionary stable strategies (ESS) . . . . . . . . . . . . . . . . . . . . . . 14 A.4 Replicator equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 A.5 Evolutionary stable state of the Hawk-Dove game . . . . . . . . . . . . . . . 15
B Pogram Code 17 B.1 Spatial PD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 B.2 Hawk-Dove game . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
1 INTRODUCTION 2
1 Introduction
This paper gives a brief overview of game theory. Therefore in the first section I want to outline what game theory gener-ally is and where it is applied.
In the next section, I introduce some of the most important terms used in game theory, such as normal form games and Nash equilibrium as well as some of the most popular games, e.g. the Prisoner’s Dilemma or the Ultimatum Game.
I then present the basic concepts of evolutionary game theory (EGT), a more specialized branch of game theory. We will see how EGT uses new concepts such as evolutionary stable strategies (ESS) and replicator dynamics, and its importance to sciences like biology and physics.
At last I present two examples, pro-grammed in the language NetLogo, which will demonstrate the applications of EGT and the similarities to condensed matter physics.
1.1 Game Theory – What is it?
The concepts of game theory provide a common language to formulate, structure, analyse and eventually understand differ-ent strategical scenarios. Generally, game theory investigates conflict situations, the interaction between the agents and their decisions.
A game in the sense of game theory is given by a (mostly finite) number of players, who interact according to given rules. Those players might be individu-als, groups, companies, associations and so on. Their interactions will have an im-pact on each of the players and on the whole group of players, i.e. they are in-terdependent.
To be more precise: A game is de-scribed by a set of players and their possi-bilities to play the game according to the rules, i.e. their set of strategies.
This description leads to a widespred definition of game theory:
The subject of game theory are situations, where the re-sult for a player does not only depend on his own decisions, but also on the behaviour of the other players.
Game theory has its historical origin in 1928. By analysing parlour games, John von Neumann realised very quickly the practicability of his approaches for the analysis of economic problems.
In his book Theory of Games and Eco-nomic Behavior, which he wrote together with Oskar Morgenstern in 1944, he al-ready applied his mathematical theory to economic applications.
The publication of this book is gen-erally seen as the initial point of modern game theory.
1.2 Game Theory – Where is it applied?
As we have seen in the previous section, game theory is a branch of mathemat-ics. Mathematics provide a common lan-guage to describe these games. We have also seen that game theory was already applied to economics by von Neumann. When there is competition for a resource to be analysed, game theory can be used either to explain existing behaviour or to improve strategies.
The first is especially applied by sci-ences which analyse long-term situations, like biology or sociology. In animality, for example, one can find situations, where cooperation has developed for the sake of mutual benefits.
The latter is a crucial tool in sciences like economics. Companies use game the-ory to improve their strategical situation in the market.
2 DEFINITIONS 3
Despite the deep insights he gained from game theory’s applications to economics, von Neumann was mostly interested in applying his methods to politics and war-fare, perhaps descending from his favorite childhood game, Kriegspiel, a chess-like military simulation. He used his meth-ods to model the Cold War interaction be-tween the U.S. and the USSR, picturing them as two players in a zero-sum game.
He sketched out a mathematical model of the conflict from which he deduced that the Allies would win, applying some of the methods of game theory to his pre-dictions.
There are many more applications in the sciences, which have already been men-tioned, and in many more sciences like so-ciology, philosophy, psychology and cul-tural anthropology. It is not possible to list them all in this paper, more informa-tion can be obtained in the references at the end of this paper.
2 Definitions
I now introduce some of the basic defini-tions of game theory. I use a non-mathematical description as far as possible, since math-ematics is not really required to under-stand the basic concepts of game theory.
However, a mathematical derivation is given in appendix A.1 and A.2.
2.1 Normal Form Games
A game in normal form consists of:

1. A finite number of players.
2. A strategy set assigned to each player. (e.g. in the Prisoner’s Dilemma each player has the possibility to cooper-ate (C) and to defect (D). Thus his strategy set consists of the elements C and D.)
3. A payoff function, which assigns a certain payoff to each player depend-ing on his strategy and the strat-egy of the other players (e.g. in the Prisoner’s Dilemma the time each of the players has to spend in prison).
   The payoff function assigns each player a certain payoff depending on his strat-egy and the strategy of the other play-ers. If the number of players is limited to two and if their sets of strategies con-sist of only a few elements, the outcome of the payoff function can be represented in a matrix, the so-called payoff matrix, which shows the two players, their strate-gies and their payoffs.
   Example:
   Player1\Player2 L R U 1, 3 2, 4 D 1, 0 3, 3
   In this example, player 1 (vertical) has two different strategies: Up (U) and Down (D). Player 2 (horizontal) also has two different strategies, namely Left (L) and Right (R).
   The elements of the matrix are the outcomes for the two players for playing certain strategies, i.e. supposing, player 1 chooses strategy U and player 2 chooses strategy R, the outcome is (2, 4), i.e. the payoff for player 1 is 2 and for player 2 is 4.
   2.2 Extensive Form Games
   Contrary to the normal form game, the rules of an extensive form game are de-scribed such that the agents of the game execute their moves consecutively.
   This game is represented by a game tree, where each node represents every possible stage of the game as it is played. There is a unique node called the initial
   ![image](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAUDBAgICAgICAgICAgGBwgIBwcHBwgICAgICAgICAgICAgIChALCAgOCQgIDRUNDhERExMTCAsWGBYSGBASExIBBQUFBwYHBQgIBRIIBQgSEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEv/AABEIAmsClwMBIgACEQEDEQH/xAAcAAEAAwEBAQEBAAAAAAAAAAAABwgJBgUEAwL/xABeEAABAwMCBAMEBAgGCRIFBQADAAIEAQUSBhMHCBEiFCEyFSMxMyQ2QrUJQUNRUmFidhY0U3KBhRhVY3GCkZOVpRclNUZUVmZzg5KUo7HF09TV5URkoaLRdYTCxPH/xAAUAQEAAAAAAAAAAAAAAAAAAAAA/8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAwDAQACEQMRAD8AuWiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIoI5huYi3aX3YIKeOvboz3ijU6eGhPft0A64koTNmbHVK0LOr3NYzLaaVhUE7osx9X8xGsLpm0l5kRQ1kPkDDamsgbPkTAIzxcZT47GP6YFK/0Mc7JzclzVl4ralhvG6NfrsPZkvlNbW5SSAcchnyjkPFI9wZGch5CPo9rqP3H5ZZINXUVEOE3N3c4h3D1HSt1gk3XOlxIsYFwA/bHsNGMezFPHo9j+17WP8Af1dn2UE66Olb9FusOPPt8hkqHNFQgZDOuL6daUr5V7xkY/NjmPpR7Xje12Lm1Qe8iIg8TVGoYVsikmT5IIkYHrOYmDW/HBv7b/2aKEjc3WkGSWgo+5kE71TmW/6Mz9b2Eew/5vSKvrUFc/uuSTb4yysI7wliGKpB0q5rXzpQ6He9/ngTCOQDGVrTszP+nVd5pPk6gGswCy7jOHeJMNpugvDeCAcg8xhfHKDfINmbGu6FZnXr6PJBZrQWtrZfYlJlrmCmA60aSoq1a8T6szwOEnQgCefpfSi6dZs8rGq5OnNXxoZquCKfM9j3ONV2VKFebw4ak237e4GZh3/obn6a0mQEREBR1xO4waf045rLnOaySVtKshx2PkScela5vCP5bOyvc+raeS6rWV7HbLdOuBflWuEeW9tPtNAEhMKf8xZv8L9KzNeaocyZKqx90Ke4XKX0o94wMr3sAx/w9TAs+yzqz44YoLg6P5rNI3IlAvkyrY976MZW7R2CE7rSve44CFCNn63vZ/2KdBEa9tHNrRzX060rSuTXNVDOZ/lxiaatbLtapM6QAUhseeKfWM9zGn8gSBkAMVNvcoxlWYu+eP4YuUvcguuSXCyyLVJJUpdPHFSNV+bneBlUJsMyfXzowozs/YZtt/Mgs2iIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiCMeYfiVTS1ikXJo2GlVKKJbAG3to0w+5VlCVEyvuxgGc3qZnQGGTHPasy9Q3Y82XJmSSbkifIPJkFwYzcOd7yGfgPoxmRHu9HkrhfhIbkccWwQ2v6R5Uu4yjC6NruHiDhiA/LpnTBk2VTpTy95+y3pSdAREQFZfkl4tFs9zDp+Rtey9Qzeg6uY6pYlzMwYAPZUbHPIw7xxQOY/tZ7t+TMC51oXraeux4UuNMjE25ECQCTHLgx+2cD2EC/AnVj8SMb6/JBsEiIgyo5i7i+Vq3UZCdMmXufHp0/QiHfEH/1YGLVMbKNpRtPKlKdKLL/AJpbY2FrLUAm0q3Of4rHKru6cAc57uv88+S01tMxkmOCSN1HDlAEYb6dMXMIyhGOp/fzQZccU5roesb3JFSmcHVVxOGj8scgXM5B5+edfRRarLLW7RR3jXEkQ27obxq87ejMveR5d2fl0w88Nsi1KQEREER84M98bRN9IPpk+PGj16/oSp8SKT/qzkVW/wAHQyn8KZ3X7OnJVaf5wtitlzO2psvR+oQ1b1oy2Gl9G1xrnBeycx3l+2DJVG/B7Thj1Wdj60o6XYpgRUr9p/ioB8W/r2wEqgs/zsUp/Aa91/RrbK0/zvAp/wDlV0/Bxz3tv90i06bUiyOkP/SzizYgx/8A0lEVgueKawWibox1aUrMNbgip+d9LhHkVp/kwE/xKEfwb9po64Xue5tesWDGhsJ3Y9JRqnIzr6Ov0IP6/wDGgu+iIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgKOuYfWUvT2m7heITQEk2/we0KWN7wO358WKTcYN7CfLO/4Op+JSKoY51/qLff6r++YCDg+Vbj9etW3iTbrjGtgQR7Seax8AEoZKlHJiAox+/KKyo8JT/LH8TFaNUB/By/Wm4fu3K+8LWr/ACCn3MDzM37TupLlZ4UW0ljQKw9okuPMceu/Aiyn0I8U1jPJ530p2/41Pn8Npf8AA3+EWMfxn8E/bOzgTw3ivZPjtvDc3PD7n2M88ftKifOv9er7/Vf3NAV6+F9tHO0XZYRmtcKdpK2xite3JrmHtIBvo9n4/WggTl+5mb9qLUlts82LaRRp9Zm6SJHmNPTYgSpTKDeWa9nm8DKV7f8AErgqjXJPwwu0LUxZlztE+EK226VsGnwjAH4ozxx6MAQrOhCVjkldzOvZ+p9FeVAREQEREBEXl3+7xYMd8qZJBEjAw3JUs7I4B7j2DHunJ2Do8j2N8+nzEHqKP+KnFexabFndZ4xmqPcBAD764HphIqzCIOtHsG8kcjKGfgLOmLnNVeONfNYY5aWrRgymPJLFYK7ujOIUxXv6viwbXIBmUj31ALMzf5ZrR+gq8LhXyv3m/kdddYTJ0XxG26gSFZIvM0fhegyHkSHv8Dh7hmBmvL7sjXMFix6CKuYfjVJ1iaJUsKPBi2rf8CAZCHP9KZE36HkExYTvi1qzATMc8e/1KIFqvcuFFjNY5OnRQBwrXLExrx2/3JN0NAUDJIb1yJjHxgO3DZ57DM81m7xY0LM05dpVrmjfTwxX1imeLbbNh7hNiaDo97MHsZ6c34OzY7uY+lA4pERAXQ6DsdLndLbbd3Y9rXGHBpIw3NmsuSMG7t0e3cwqSjsMm9en9K55XY5F+DlQ0Fqu5jkDkvoWlijl92ykUwdt9zf0fmTeHIOxjXtazDqTo/dE9oXAREQVZ5zuCMy9vBe7QHxE6GDw82FV1KElAYSrxmBuVw3WZv7Ptsr+dmDq1W/iRrm3RWacHKusYbguCC3PgUpPaAjCUwA8kfxYx9NzHB3Zt9vTGi07RBTLkx4ET4s4eob1FfEbEE72XCkUxkkOdm3WUQdfMA2De9rGP6Pzfl2YUykTnt1DOtunIR7fNlwTPv0YDzQZR4hXCrb7mTbeQD2vwzGN+HX8mxWJUecaNeHsEBsqPaZt3kSj0jxo8FlSYHeMhBuPt5kYPsr5sY//AO5BB/4PvVd0uf8ACL2lcp9x8L7J2PHzpMvZ3Pae5t7734Z7Y+uH8mxWzUOcsWibja4Fwm3ijB3bVF0PdZwBU6NjOPXsD630z3HEf+zuY/YUxoPnkR2FY5j20cwrHMe2v42kpWj21/oWeHFbg1qLSF58dZwzCwwSd613S3DeYsZnR1WAlMHR7hvYPqx1X0wKyv7T2U0XRBmNcb5rXXTo8YtZ96bHK5omAhhBEETCneZ8cbADJh9s3o3P21eTls4Y00tYxQSVa+bKK6Xcisyqysh7Bs2R/nGwYxs/bwe77alVEBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAUMc6/1Fvv8AVf3zAUzqLeaG2Ul6O1ANzauoO3PldKOpTuhEHLY7y/F1Bl/Qgqn+Dl+tNw/duV94WtX+WdvIhf40LVjWSS0F7UtciDGrX0ukPNElMHV/X3eVIpP8Po37a0SQZnc6/wBer7/Vf3NAV/eBP1W01+7dm+746zz5sb1HuGsb5JjEYQTjxwtIx1HNc6JCiRCYP/H7wD1pBw/tjYNptcNtKtpAtsOK2jndXUaCMMdKV/5lEHQIiICIiAi4riZxEtWnYbpl0lMD0YV4I1CMrMmuHtsqGDFq+j5BNw4afoM3MnuY3uVRdd8ftUaxm0teko06CF3WjhwK5XA7KyRsBNlTRs/1ojs9w12D2MZvkzK9r6YBPHHDmRsmnCVig63i5NzoSFCkhaCM4ZqAIGdL7/DyOoz+5Yx7+o+5rM2PVbbZZdc8TJITTSyA2Z8vOkl4/DWaKPOZ3wYWbPackP0oNHtqUvXBhSsbXNS5wD5T4kKgJ2pdufLqIRB2bH6HBNvbn0ogyYXMmDBtcyvuvnN6SG4PpZ23wxAEIARDCCMxowBExoxhENtBsGNjOwY2M7aNpTp5IIu4I8CLLpVtChZ4241wqS7TBCcdj9moCNgjoz6BGfmfsa5z3UkVa978GYTCiIC4riZw7tWoobod0isN1YVgJNBsbMhOJtvqaDKqyr45NwAa/oP28Xte3sXaogpPrHkrlto51ovUc2Uh23GukUkfajdCYVJNibu/Ib7tvyRNd3u7OmFfEgcmGoqkG09wsgw1KxpSBPPOVgqupQhGBfEYwhMPOjKvZl083NV80QVw4Q8qFksx/FXI3t+Q3daEMqEAVuY0jBszJBe82/Ib0N3PfVnvKdmTGPVj0RAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQF80iOwrHDI2jmFY5j2V82uaTye2v8AQvpRBQfjVypXeHKKbTwaXG3lLVwo1DtZMiNfue4fSQ/pIGzya0jXZ+Xc37deLpZeJpesHb1lUfcFwylurYmLKdHs3CP2Nvy+OWLvJaWIgpJy6crU9s6PctRsbFDDKwwLW0rCyDnG+hGeK28xjjdlHYUdm/8AYV20RARFD3G7jvZdKtqIz/G3GudB2mGUTjsfs0ON04lX/QIz8wd7mue6kijmMfg/AJRuMwQBFOYowgjMcQ5ivaMYRDbUjyEe/sGNjO6rq16eSq3x05tIkakq3abFSVLZug9tlIOsKOWm30NCHTP2h+Xbm/AWYxu+kDf3RI+XrfijJYGtGDt0YxSNdQJolhhnHGGx9CHwKSRMdQjMWPeV7PFkxwG99W2d4I8udj040JyiZd7owrie05sfFoaboyA8JCe944pGVAN1C9xc9zva1+DQgLh3y5ah1XLJe9UypEBs2Q8khssD/bMmjCDHVrIpGMHbwbe+wTn07NgeIHCwVwNAaEtFgj1j2i3R4LH/ADXCo9xz4PI8fiJRMzyMKnJhm9+GeLe1deiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgKPeJnFywadxbdZ7ByHto9kILHyJbmVzq1+wPvGP3ZO9+LPjTr5rs7xN8PHPIxcTw4CmwZTJ79tlX4s/P16dFmpp/RV51TqmOG8DmRJGoriV8qXLiyRbbRhJLOMHiKfYjgI1jPs0GOnpogttYObfSMk1REfcILetG0kToTNl/nWlHfRDGeNnwr3tb66fr6TnZbnGmgFJiHFJjSGZhkR3tIIja/aGQflVUr5juWO2aesJ7xbZtwI63ljeKDPfGI0gjmHFps1BHFtkoU4/jn5UX3/g69XndLudjeR7gVh+0ooviOO4RxglYdfRueKBX/AJCn+EF1kREBERAREQEREBERAXL691lbLHDrPusxkKJR7BUK9pCPeUnyxhCBjyHJ5PdgxruwZHeTWOUCca+bS2W5pI2n8LtcGEayssjCeyA7ZiMP3jewkwnu+2oegnNkMfuPwwdE3D/hDqniBNHe9RyDggu8KN8uWHw0mXDqHeG2zxRgoBkZ9CMrvVa0WUp5W7zqFZUPT4pczt9v0mts0lGmRAy2VaNwY+/fJP0Y/iqDYB5WRGMY/LqH3rPCUJusywZ0fBXlBoNwpmqSsPTbrX2FDIWjWuIIdWeKnAex+4x7z0qIPbkMbt17cmOsbwq4aWfTEV8a0RdqhqirMklI40qWUA6MYQ5n0/nuwZgJjyExa3Ny7lB59vhiAIQAiGEEZjRgCJjRjCIbaDYMbGdgxsZ20bSnTyXoIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIqx83HMBSyNJZrMSlbwcf0qWytHNtoX9a0oz/5x7K9afoMrR36CDnefDi3GrEfpaERpTmKN93eytHNAIBGSARevX+MVOMJHfoMH+35e9yEcOZFstkm9TG1YXULY/gROp3NgD3HjN1/uzyZ0p+gIbvtrk+WDlr8RtX7VAqkrJr4iHaJLct3cpQnibiwnXcz657Nf8P9BXHY2jaUa2lKUp5UpT8SD9UREBERAREQEXg6qvsS1Q5E+4SGRYcIVSGkE64jp8KeVOryPe/BjWMpV73vY1uTnUVQOMnNTNuJzWjSscoxTCVhAuTKGfc5u68DGOt0UeL4RHv3mMzo8rmnG5vhyfALI8ZOMtj0q1lLlII6XIZvRrdDFvSzB3mDq/Cr2jAPzJWjzPZn4c+OTmYqod61XrTifNdBgC8PbY+HiIUaQ8VvAE8wZAmu5yP+nyGYMrhRlf4oRwgNrmu14P8AKbMlyHXHWJy03y+Idbwzd+ZKP4khDkuc0dHsoMgx/kSue7xeW6JzcXW10rYYtqhx4Fvjsiw4QqDDHZ1xZTrStfOveQj35vc99avc8j3Oyc6qCGuBvLJZ7B4WfOpS6XuPsm3nud4GFKZUnWsEFKM3MNxnvjZvzjjIxoXdqsGiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiDkeLeqW2SyXO7V28rbCKQLS16MfI6bcUden4nyCDZ/yiymk3M5pRJhTPdKNIfKJIq7oVxyPqR5s6edH7lclsOiDJv/AFWNU/75b/8A59uX/jqwnInrK83PUc0Fwu10ngZYZJWBn3GTLE0tLhbB0ewZ3uZuYEI3LpTyI/8APVXgRAREQERR/wAVOK9i02LO6zxjNUe4CAH31wPTCRVmEQdaPYN5I5GUM/AWdMXOagkBVw43c09nszKx7O+PfLg7NuYTOrbolKi3AGJKGzCfXcIOmyF/5M7XEE5nfBmsuL+reIUn2NZIRYkd7DlJbrdKdQhweG2T+1LiV4WPie8IzCrRMd4sbHbr6CU18FeVOz2hw5t5ey8zWsc10QsdtbRHeUI2P6Rjsc+a9hKno0xsWVYRjtpjmNcgg7T+gdZ8SpVLtOkbNqLINsyZJCNgxm7gASA2i351e/AbKd3awrohGkPu0crhcIeEll0uHatkbrIfutNcpTQluB2EeMm0+WMbduP7sPuWNaz3dHY5ZvdIyICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICLwdVX2JaocifcJDIsOEKpDSCdcR0+FPKnV5HvfgxrGUq973sa3JzqKivG7mnvF5fWPZ3yLHb25tzCZtLjLrQu4AxJQ2ZwKbYx02Qv/KHa4hWv7AvvcJYwso4pBiY4oRNcQjRNqWQYYAM6kr8x5yDYxnxc8jG/jXorHy/3eVOkPlTJJ5ck+G5KlnfIOTbYwY905O8lWDYxvn1+Wvt01qu52zdpbblPt/icd/2fNkxKm289upKxyM3MM39MvhuPQa7Ly7/d4sGO+VMkgiRgYbkqWdkcA9x7Bj3Tk7B0eR7G+fT5ipjw65yJsWCQF5t/tWYLJ8eaA4YO/uFFWgZQRR9sdWDfIrvBb3bYW7fc8y5i2WXXPEySE00sgNmfLzpJePw1mijzmd8GFmz2nJD9KDR7alL1wYUrG1zQSFxr5rDHLS1aMGUx5JYrBXd0ZxCmK9/V8WDa5AMyke+oBZmb/LNaP0FXhcK+V+838jrrrCZOi+I23UCQrJF5mj8L0GQ8iQ9/gcPcMwM15fdka5gsWPVg+CPAiy6VbQoWeNuNcKku0wQnHY/ZqAjYI6M+gRn5n7Guc91JFWve/BmEwoOd0hpe3WaMyFbIUeBFZi7ajMw3HMYIe8d/zDyajYOjjPq579umTqrokRAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQUW58eKMw90fpiOUgoFvHFJch0bRvjZhhsljzfue9hhASM9rK0Z73NzqPwE9tUFIPH+U8+qtRPMUhHtv1xFR5XvI+gwTCAAOu5XrRjAMYxrKeTGjY38Sj5AREQFoXyMcRz3mymtsrzkaW8HGEZgmDY+3ECQcFj9sldySykQ7HVxb2MB63ZvWeitH+DsllbqG4gaR9AlsRSvC0j9shY9wgDA8g+uBCMYc7Wv+zvv/Sr1C+qIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgzL4N8SdRyNRWAB7/ezhkX61iOE15nvGYRJ4GEYQZDYEY9latxr8Vposm+BP1p01+8lm+8I61kQVM/CB6ruls/g97NuVwt3iva2/4CdJib237M29zw7254bhOmf8o9dVyJahnXLTk09wmy5xmX6SBhp0o8srRUt9sJtsId7n4ZkI/Dr+Ueo8/Caf7Vv67/7oXZfg5fqtcP3klfd9rQWaREQEREBERARFDPG7mAsWmKvimeSbdhsaRtriebh1eErweLlP93EG+rB9ad5cZA3bT2uQStcZggCKcxRhBGY4hzFe0YwiG2pHkI9/YMbGd1XVr08lU/jbzdBY2sTSjaSDOq/dvE6O9gBsfHpg+DEJg8khhH+uSyjG1j+grX5tjBkTW/FGS81KsHboxhDc2pjRLDDOOMR7KjBmUkiY6hH5PYwr2eLHlgN7KNtTwR5f7FpirJQWEm3YbHDddJfm4dXhEw/hIrPdxBvqwnSveXGQRu69rkGeuv4V2HOOe9xpcW4XIhZx2XCE+EQtZRiEfJYAg2U23n36djcOrH/mXLrSbmp4Ni1Ra3lixxVv9tF/rYbdYCsgVCbhLeclWYEE9lSOFR+OBa072NebLOq4wygKUBhECeM9wzhKxwyBKN1RvGRj+8ZGP7atrTr5IPOREQF3/BniXO0rOLcLeGKU0iESERk0ZnioIhgHq5mwcT9zOKOnq6etefw10TcdRXENstoKlkH73vd2gjAZ0o+VKfSnu4zMx+f7bGta9z2MdproXh3abNaaWaFFHWA4b2SmHYw1Z7jM2zlm9WYSHmZXB/VuOFGMa1rGNY0K42jnYjPONs2wSI8WtXbpodzHLOzsJVmACxQjJ7yg6fNZ0pXLu6Y17/TnNto+XUviDz7ZQVW4ePgEJvZ7lX7fsx8inbhT14fMZjl3Y9rqLgfpGeFoT6ftrGMLQrXQo/s4uWBGUo49vqIhB9/y88PJnl2tXC6i5RdIyTMIClytrGsayseFPaUTn5krvE8eE5Kk76M6Ufh7tvb6sgkGycZtKSwDkD1HaWjLljSTPDCO3B72e8izXsMOnZWvV7e+laO9PRSOqZ37kk/jT4OoP5d0KNMtf/GeHDJmilfzGPKwP7W39lcVI5XNb2dwp1sPDLMEXBjrJdjRJkdpAkGQ1DzBx2MHVlasdi/P3/pxyQaAos/RS+L1hK8NKajkPlDER1XAZqQTWjeQbKMPVksccnrzYxzHfLy69i/uFza6wt7awpgLXIlxCmFJLPt0oEzdYZ+4M4IkgIxkZWu3jtM+X3d2SC/6Knto52IzzjbNsEiPFrV26aHcxyzs7CVZgAsUIye8oOnzWdKVy7umNe/05zbaPl1L4g8+2UFVuHj4BCb2e5V+37MfIp24U9eHzGY5d2IWDRRxZOM2lJYByB6jtLRlyxpJnhhHbg97PeRZr2GHTsrXq9vfStHenopHQEREBERAREQEREBERARFHPF7i3ZdLh3bnJ6yH7Tg22K4JbgdhHkHusiEI3bj+7N757ms93VuWWDHBIyKjupOdS5koL2bZYETHPf8fKk3GpPIe3t+H8Nt9PeU7s882enDv8zTPOTqADo9LhAtc8AxYSHCoeFMkuoKo6Gqej3gESpMHvoyPj62tazyq0L6ooI4H8yNk1GSkU/Wz3J2FBwpskLgSXENUAwwZfZ4iR1ID3L2Mf1J2tfg96ndAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQZN8CfrTpr95LN94R1rIstNatPpzWUojgu3bHqLxogufjuiZMpOi94/lseDaf1p+n/iv3pLjdpOfEHKZf7dGoVvcC5XCNClCd9trwSCMfTp1+Le3ypj1QQH+E0/2rf13/AN0Lsvwcv1WuH7ySvu+1qEueTibbr/Ptsa2GbKj2UUrdlidkEx5bgbjAkp8wbBxR1zp5e8/UrL8k9kLD0dbt5m2+eWTNa2rejnCOauw+v6ngGN9P2CDQTgiIgIi8+4zBAEU5ijCCMxxDmK9oxhENtSPIR7+wY2M7qurXp5IPQXL691lbLHDrPusxkKJR7BUK9pCPeUnyxhCBjyHJ5PdgxruwZHeTWOUAccebaFbneE04yPd5Dc2mnmcalvAUZqDqNgx0Y+4ZjYbvY9gu8LmuL3tbFXD3gdqnW8qNfNRTJAbfLxNWZMPlOkwiPOfC1xejmQ49SVrhm0QmslDKNhW9iD7eInMbqHVcsdk0tFkQGzZDBx3RDv8AbMmjCEJRz5Q3sHbwbew8rWV7NgmR3Czouv4JcooWNpL1W6kgzqs2rPBkPYAbHx65snSx4PJIYR/ojPoxtY/rK1+DbF8M+Hdq07DbDtcVgejBMNJqNlZk1w9x9DTpVGUfIJuHNX9Bm5ixrG9i7VB59vhiAIQAiGEEZjRgCJjRjCIbaDYMbGdgxsZ20bSnTyXoIiAoz4ycGrHqprK3KORsuOzZjXGGXZlhDvMJVmdWOGcfkSlGGY/DxB8cXPyUmIgp7d+SeM873Qr/ACI8WtW7QZlsHLOzsHR+ZxSgjJ7yhK/KZ0pXHu6ZV+3TfJXax1L7SvU+XlhseAixrdQfmTc3PEeJ3Ovu69uGGD/Vn2W1RBy+gtG2yxw/AWqGyFEo95qiY4hHvKT5hDGO95Dk8mNze53Rgxt8msauoREBERAREQF59xhiOIoDCGYEljhnCVjSDMIjajeMjH9hBvZ21bWnTzXoIgjHUXA/SM8LQn0/bWMYWhWuhR/ZxcsCMpRx7fURCD7/AJeeHkzy7WrhdRcoukZJmEBS5W1jWNZWPCntKJz8yV3iePCclSd9GdKPw923t9WViEQUzv3JJ/GnwdQfy7oUaZa/+M8OGTNFK/mMeVgf2tv7K4qRyua3s7hTrYeGWYIuDHWS7GiTI7SBIMhqHmDjsYOrK1Y7F+fv/TjktAUQZ+il8XrCV4aU1HIfKGIjquAzUgmtG8g2UYerJY45PXmxjmO+Xl17F/cLm11hb21hTAWuRLiFMKSWfbpQJm6wz9wZwRJARjIytdvHaZ8vu7slf9efcYYjiKAwhmBJY4ZwlY0gzCI2o3jIx/YQb2dtW1p080FTbRzsRnnG2bYJEeLWrt00O5jlnZ2EqzABYoRk95QdPms6Url3dMa9/pzm20fLqXxB59soKrcPHwCE3s9yr9v2Y+RTtwp68PmMxy7se11FwP0jPC0J9P21jGFoVroUf2cXLAjKUce31EQg+/5eeHkzy7WrhdRcoukZJmEBS5W1jWNZWPCntKJz8yV3iePCclSd9GdKPw923t9WQSDZOM2lJYByB6jtLRlyxpJnhhHbg97PeRZr2GHTsrXq9vfStHenopHVM79ySfxp8HUH8u6FGmWv/jPDhkzRSv5jHlYH9rb+yuKkcrmt7O4U62HhlmCLgx1kuxokyO0gSDIah5g47GDqytWOxfn7/wBOOSDQFFn6KXxesJXhpTUch8oYiOq4DNSCa0byDZRh6sljjk9ebGOY75eXXsX9wubXWFvbWFMBa5EuIUwpJZ9ulAmbrDP3BnBEkBGMjK128dpny+7uyQX/AEVPbRzsRnnG2bYJEeLWrt00O5jlnZ2EqzABYoRk95QdPms6Url3dMa9/pzm20fLqXxB59soKrcPHwCE3s9yr9v2Y+RTtwp68PmMxy7sQkLjXxJiaUtJLnLYU3eyPCijrVrpcx4yEGCr8KsjjqwJHPI6na0b8Wudgx+Y2qr7LusyRPuEh8qZNLUhpBOmRK/CnlTowbGMwY1jKUYxjGNbi1tFPXPBxPteoZFibaTjlxIcKZI8Yyr2u3Zcmkd8U0U42EjkZ7OG/v8AWyWx2OODn1nQEREBaEcmfGf2/B9jTySC3m0R3EfKkVqXx8FhhjGffGzykhqcAX0f1e/qMuT3PLhnupT5Xb5S36v09IoLd3bmyDhnt9PaoyW2hs8HejxWeP2tvHt9SDUVERBG/GfirbdKQmSp73kKdzhwoAMHSZTmY1fhueTBso9mZHV6U7Pi57WPq9dede8OM10W0WwMela5hkkkyTOb1+wcbxMZ5fsOXac2nBDU2p7wydBpEfCiQhRooSTajLl7w5yVGRm2PIhMPV+TYpH4R8CrDDsUCLc7HbzXB8EVboWbFjSpNJhmZyBsld9WUYV72NqF3TspWiDyuAHMpB1NJbbpMZ1suT2ucBji70WXhSlSMATBrxkwpV+D/wAX2nKwayivcIlr1VJj2qmRbRqMoLTSrssnxLg8cSlX5/nGP7S1dQEREBfiYjWNq9zqNaynVzq1xa1v61+yzy1zxl1Xrw9bLaojggmNd1tdudVzyi93nW4Ti4U8Ox/4+ghe87sulEHZ8TecG5RrrMBZI9qk22KXajy5gZpCydvyIZrwShM23ko+rOjadvT8/ndpY/6qsxbdOm2+RVtTW2YeGerK5NqWKYgCVY/p8vMdf/otgEBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERBDfHjgJatWNYcryQrkEVRCuIGMfk33lRilAr/GBse/4Ucx3x7lXK78ld+aTpEutoOLp65VZkUmX4qbY45qU+z9tXxRBUzhpycRYskUm93ClwYFzX0t0YDwgI5la1xOcj9wg/hTFrWfjVqY0dgmtGxrWDY1rGMY2jWsaP0NYxfUiAi53V+qLdZoz5tzmx4EVmTd2S/DccxhSbIGfMPJqNhKtCyjnv264tqqg8YOZi7XqQ6zaMBMY17zibOjBee53IFIz9ysKLsVJAH88ubKb2AwO6x8HsQWG4z8b7FpoR2SJQ5FzEJ1QWWM/OS8tWgINkp48mQBuYcb8zepmbmNLjhWqN61XrTifNdBgC8PbY+HiIUaQ8VvAE8wZAmu5yP8Ap8hmDK4UZX+KEcIDa5rvOEHKSeYT2nrCRI35Ekxj2kMhhjnfvjJvXG6DI/c3vf5sDXOtCDdusdmxtuLBaIsGOyLDjAiRgZ7cWIBkcA9x7yE2gD7B0eR73eXT5iCHOB/LdZNOEpKP1vFybhUc2bGC0EZwzVOM0GJ3+HkdRg989739R9rmZvYp3REBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAXn3GGI4igMIZgSWOGcJWNIMwiNqN4yMf2EG9nbVtadPNegiCMdRcD9IzwtCfT9tYxhaFa6FH9nFywIylHHt9REIPv+Xnh5M8u1q4XUXKLpGSZhAUuVtY1jWVjwp7Sic/Mld4njwnJUnfRnSj8Pdt7fVlYhEGZ/M3wbdpGfGYGQSXAugzlhyDMEMrHgNWhIpKDf7wgQEiu3sBMfv8Aa2mL1C60n5tOEhNU2kNYO37Vs7yyYDSPfRskR20pKhUfntiIbbA5j30rTOOxuTGve9ubCAiIgKSeXS2Glas04OOyhXsvMOQ5u4xuIIRhzpT+hK0p2RwHf+d23XHq7oo2VyOQzhEXdHq2ZtUC1kmPZhNe55XlyJDlTX7b8BjaykqM1j8s83uxZgJ7wugiIgKBuaTjtG0xFfCiOae+Sx9Qg9TYLH//ABUrz+H6A/t/zV9nNNxoZpOC0UbEl4ujH+AC9uQwMZ0YSYenT5bK+lv23/stf0q7y8aStF8nlv2r7/bGD8Q4ngbjd4YJdxkeshJQyka8cPz9Hln+pvrD3uS7hFJulyHqK6BJ4KAfxEMkltc7hPp1Iw1KkrmQQSe8qSvrft+rF+N8VwMLiZpII2CDqHTwxBY1ghDvVtYxjWdKMYxlDdGM6UXRaj1BBtgmnuEyJBAQrRMNOlBiCcWrHvoxhJD2sz2xvdj/AHN/5kHuIue01qu13PdpbblAuHhsd/2fNjS6B3M9upKxyP288H9MvjtvXQoC5zR+krbaA1jWuBGghc7J7IgWDzdhhmR9O8hOylM3/FdGiDJvjt9adS/vJefvCQtZFk3x2+tOpf3kvP3hIWsiAiIgIiICIiAiIgIiICIiAiIgIiiPmU4sxtLWopGlZ7VlieO0xOyrt2vVniSD6fxYPXPz8n16M+15BLiKn/Jnxh1HqK/S4V4uNZkYNkPKGLwUGNidkyANj84gGPrTbOT416d/6lcBAREQEREBERAREQERRzxe4t2XS4d25yesh+04NtiuCW4HYR5B7rIhCN24/uze+e5rPd1bllgxwSMq0cauayz2hxIVmYy8zWsa5ssUhtbRHeUJHs6yQPc+a9hKgq4IcWVYR7d1jmOaoW1lxQ1pxCkGg2GJLj21wmsNbrcfETdyMfc9q3cjAs2zM8UzZe9gn7Q24Pe3N848EeViz2ZlJF4ZHvlwdhXAwXVt0SlRbZwjikfhPruEJXeMz8mBzRiczvCDtG8L9acQpAZ19ly49tcJzw3G4gxE3cjA2/ZVoG8LNszPCv3mMYJ+0R2b3twfbrhDwksulw7VsjdZD91prlKaEtwOwjxk2nyxjbtx/dh9yxrWe7o7HLN7pGRAREQEREBERAREQEREBERAREQEREBERAREQEREFAfwjX1pt/7txfvC6KONFcB9VXiCC5W21+JgzN3YkUuNtDubBiAJ0HIlMIytCDIzub+L9akf8I19abf+7cX7wuisvyUfUWxf1p98z0FL7xoTXekg0lvBc7XHGXNxoE1hAMJ8cz+zzvYP5bPX2/8AYrOcoXHst/c+z3d9K3UIaFiy6Ux8cIdOhKPGz3bZLKd3l62ef2KqxdxgBlANGkCYaPKE8JwlbR4yiI2oyMez4VY5nl0/WsxNPE/g1rQVBnc1lg1O+K85HMa6sWPPJFkbj/RTOPuUd+L3lUFhvwlMQjgacPRtaiCW7Ce/y7SHbbyDZ/SwBv8AJrtPweUMg9KSHvZVrZV+mGA6v5QdIsAFX/5QBG/8nVSDzC8Km6utgIDpns98WeOWKTSL4nzYE4HieHcZXB9D9fJ/5NnxXr8GNCM03ZYdnYfxXgt+r5bhUA4xZBine/bo9+38zH1u+XRB3KIiAiIgIiICrVzDcsES+mkXW0EHb7vJKJ8gJnY2yY6r375iMGFxI8x+bHVezJj3DrkzIryqyqIMu9TcBtX2+gvEaenkrIzw9nsZc8durKvoT2Y82x5vp0zxz78fS5fHZODOq5Zxxx6cuzSFyxrJgGhAbgx7/eSprGBHXsrTo93fWtG+rotUEQUo4JcopnupL1W6scLaM2rPBkMecj2SK5snSx5sHHeNnojPq91JHrE5mDrj2+GIAhACIYQRmNGAImNGMIhtoNgxsZ2DGxnbRtKdPJegiAiIgozzIcHda6i1HcJ8ezuLEzbFtxH3K0j+hx24MewZJe4Njybhe+mXv/semkaf2Lmuv7R/6Ws//nlpiiDM7+xc11/aP/S1n/8APK3fOfoW6agsUOFaInjJIb2CUQW9Gj4gHCnjI+pJRGD+Ycf4+vep2UecaompjQGC0vIhxppz7Uk06j+goxBk6nA/o/ArCbf2H+v9hBBf4PmxyoBdVhki2iRZVugHpmwjWyoRLmyUHcG9zCYbg+5nbXNW3Ud8D+HLNMWukKh3S5UiQWZcbgSr85kw9Wbj+hHvqxnQbG/j/G71PcpEQEREGenFLl31jPvt6mxbPUke4Xm5yoxXXO1N3AHmHIB+BJVHszY5nqpSvn/i0LREBERAREQEREBERAREQEREBERBCHN3xCuWmbCGba3hZJm3QUHcMKhtoZoc8+8Fj/d+IzAz1tez49qqBqThfqaZZ7nrDUBJAmBoBzfaW5WfNeeYCIzABOnh4zN97m5Y+TGNa3F9Hs0hPEGWrKkY19QE3BZta7bLg8eY/wBB+29/n/dKqJedf6i33+q/vmAgrR+Dl+tNw/duV94WtX+VAfwcv1puH7tyvvC1q/yAiIgIiICIiAvLv93iwY75UySCJGBhuSpZ2RwD3HsGPdOTsHR5Hsb59PmKFuPnMhadNtNDguZdLztGoOPHewkOEdhqAwuhhvzGRhN+vhmdX+4q12zmx6rpZdKa04nzWzp5fD22Pn4ebJjvFbwBPMIMwbQAbPp8hmD6Z1fX+KDaU7exB3nF/m2PMJ7M0fHkb8iSEILsaOwxzv3yD2bdayDfub3uMHmpnWhCN2mOwe3zuDfKtNuJw3fVUgoxTCUmntr6mfc5u6873tuMomL4RHv2Xvwq8rmnI13hyfCwfBjghYtNCA+PFHIuYhNoe9SWZyXlq04yPisJkyANzDkZgH1Mwa9xcc6y0g53SGl7dZozIVshR4EVmLtqMzDccxgh7x3/ADDyajYOjjPq579umTqrokRAREQEREBERAREQEREBERAREQEREBERAREQEREBERBQH8I19abf+7cX7wuisvyUfUWxf1p98z1Wj8I19abf+7cX7wui6fl+5mbDp3Tdts82LdiyYFJm6SJHhuBXfnypTKDeWax/kw7KV7f8aC66yn4jw/aOsbtHC6la3TVU8An+qn0q6EGN36/mUqrNa+5y4ToRR2S3TqTTMewci51jAFGzHXE7GRzGrII1/Tsrh//ABUbclXC2Rd72K+ShurbbGekhpyV/jVxb0IBg6v+ZVhOhnu/uY/00Gg6IiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgKGOdf6i33+q/vmApnUdcw+jZeodN3CzwnAHJuHg9ossj2AbsT4som48bHk+WB/wbX8SCo34OX603D925X3ha1f5Vc5VuAN60leJNxuMm2GBItJ4TGQDyiEoUkmIej378UTKDwiv88vxsVo0BERARefcZggCKcxRhBGY4hzFe0YwiG2pHkI9/YMbGd1XVr08lU/jbzdBY2sTSjaSDOq/dvE6O9gBsfHpg+DEJg8khhH+uSyjG1j+grX5tCw/FXiXZ9MRWSbvK2qGqWkOMIbjSpZQDq94wBZX+Y3N+AmPIPJzc2qnnELjjqnW8qTYtOw5AbfLyDSHDBlOkwiPADO6SurmQ49SVpng4QmslEER5W969Hhjy5X3VU0t81dJmQwzyncdhG1DepJR0YMHQEiPtwIlK0rRtHN9EcbGiYx7HtuHoLRtsscPwFqhshRKPeaomOIR7yk+YQxjveQ5PJjc3ud0YMbfJrGoIA4HcpMK3O8XqN8e7yG4ODAC01LeAozVJQjyEqx9wzGwPY9jBd5muaXsc206IgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiCGuMfL7ZtVTw3C4yrmE8eEKExkA8YYtoZjnzdQ8Ur9zOUT7X4mf31xf9hZpb/d9/wD+mW3/ANOVmUQV+0xymaRh1bUoZ1yxfuN8fNp08sOzCGMLCMrh8HUr6/73ScbNa48IA40UAo0YDMBR442jENtPssGP4f0L0EQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERARQ9x/4227SAh0Izx9zmY1i2kRtl1QUfVpJUg2D9iP2va2uLs30xa3sK9lFdf8AGzU17Id8q7yxBkBMF9ugGNDt/hiPJ1ivigfRhx4HcPI2497KMa5z+iDTsUoVTPBQjKnEIZCiaRu4wZ3lGEhB+sY3vjmax/TuqAnxw8vQWM6k3QHGzU1kIB8W7yyhjhCFlunmNMt/hhvH0isinJVgB4AaPIO29jKva1zOqDUtQzxu5gLFpir4pnkm3YbGkba4nm4dXhK8Hi5T/dxBvqwfWneXGQN209rlW7WvMjqfVhY1l07BJayTijpRsCWY9zKVjyEft3DoFkOHhg9/azBgCZF23PYu34JcooWNpL1W6kgzqs2rPBkPYAbHx65snSx4PJIYR/ojPoxtY/rK1+DQjBkTW/FGS81KsHboxhDc2pjRLDDOOMR7KjBmUkiY6hH5PYwr2eLHlgN7KNtTwR5f7FpirJQWEm3YbHDddJfm4dXhEw/hIrPdxBvqwnSveXGQRu69rlK1vhiAIQAiGEEZjRgCJjRjCIbaDYMbGdgxsZ20bSnTyXoICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAvE1fex22BOuBmkeK1wpMw7A0a4rhRQvMRo6Ee1m5tsr5Vc3r+pe2od5w5ZQ6JvjhPeFzhQxOeIrxOcI9yigOOtWdK7bwEex7PtsI9qDPjiVra46iuJrncj1LIP2MY3tBGAzrVkWKytfdxmZv8v23uc57nve7kERAREQdfw11tcdO3ENztp6ikA7Hsd3Akgf0q+LKZSvvIz8B+X7DHNcxzGPbqdpG9juUCDcAtIwV0hRpgGHo1pWilBYYbSUG9zNzbfTyo53T9ayCWm3J5LKbRNicV7zOaKYJryleRzRAuUoAB0q/rXbYAbGMZ9hg2NQTEiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICjfmK05W7aXvkFrJBHlt5ZEcUVu4Y0mF0lxQMHg/POQADcG97qPrj0cpIRBjOis7zl8D/AGLLre7REoOyzcXTRArVw7dPeR/lsUZ9Ht5vd4epjS5s9014WVrEgIiIC1Q5ddOVtOl7JBcyQN4reKRIFKbgYMmb1lywEHgzbwkHO3B/c2jG5dXeao1wW5e73qiDJnxqx4UVnQcA1xoZop52FaM7R1Gxz2R2M3qb2LvejYNvwK4XV6N4v6t4eyfY17hFlx2MAUduuMp1SAB4bZB7LuInmYyJ7sbMKNKxvhCMbtPqVBoEi4bhVxLs+p4r5NolbtA1FSZGKNwZUQpx0ewZwvr/AD25szE94yYudg5dygIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAq7a85S9M3Ih5EV0u0HOImAoLxVgNlEeQlDvinY99GbhGe5CUTMBsa3D1KxKIKZ/2DH/AAo/0B/7kpD0Hyl6ZtpASJTpd3OAQ8xTnipAdKG8ZKnZFAxj6s3Bv9yYpWYEe12fqViUQFzur9L268xnwrnCjz4r8nbUlme257Cj3gP+YCTQbyUaZlWvZuVxdRdEiCi3FLlivthk1uekpMyWGIyrhtDI2L5G+jH8VUbwMEyWx7GY9A+9f4ug9p+Ob+j4K831COFD1SJgKbdae3YYy1a5wxDozxUEDHv3HvYetSh7ciDbtMbk9txlD3G7gRZdVNqUzPBXGmdR3aGITTvfs0ANs4dWfT4zMAdjnNe2kejWPZm/MJNsF3izo7JUOSCXGPntyoh2SAE23vGTaOPsJRhGPb5dflr1Fntco2s+Fk5xAv8AE2eRJkBjvI55LNcHkAN1HnhDNR8C4UGIfnkx9fCEaxxRMflZfgjzGWPUbQgKVloujyuH7MmyMmmpujGDwk17GDlEfU420F2lz3OxzWZuCckREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERB59xhiOIoDCGYEljhnCVjSDMIjajeMjH9hBvZ21bWnTzVW+OnKXEk0lXHTZaRZb90/sQox0hSC12+gYRKYez/y7sH5izINv0cbO22iIKIaE4/ao0dNra9Wxp04LelGjn1xuAGUkkYebFmkZ/rvHf79rc3vY/YHgVjWVzuBoDXdov8AHrItFxjzmM+a0VXtODN5GD8RFJgePnUBMM2Mzwyb2r8eJnDu1aihuh3SKw3VhWAk0GxsyE4m2+poMqrKvjk3ABr+g/bxe17exVF13wB1Ro6bS6aSkzpwW9auJApjcAMpJG8EKVCG/wD13jv9w52A3sfsEzExrKZhe9FUvgXzaRJNItu1IKkWW/aB7bEQdIUgtdzqaaOuHs/8g3NmYsyEd9HGzttJb5gjiEcJRmBJY0gDCe0gzCI2hGEG9nYQb2d1HUr080HoIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIoJ5z9dXTT9ihzbRL8HJNewRSF2Y0jIBIU8hGVHKG8fzAD/F17EE7Iqx8j3E2+akrfa3qd432f7M8L9FhxtvxHtDf/igGbmewH19fR/fVnEBFnpxS5iNYwL7eoUW8VHHt95ucWMJ1stTtsAJhxgZmSLV78GNZ6q1r5K3PM7qifZtKXW5W0/hp0PwOyfAJsN+5xI5PdnY4b6VGR7e5qCUkVP+TPjDqPUV+lwrxcazIwbIeUMXgoMbE7JkAbH5xAMfWm2cnxr07/1K4CAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiCDeN3LnY9RtMcQmWi6PK0ntOFHyaam6Qh/FwmPYOUR9TkdUvaXPb73NZg6tFsvWueGckIZopBrMyXhSM8nibNKHnM7IM3B/sySb6UajG0EXrg8ontpgtCV5d/tEWdHfFmRgS4x8NyLLAyQAm29hB7oCdhKMIxjvPr8tBGXBHjvZdVNoIL/AAVxphQlpmFE0737NTkdBJR/0+MzA/e1rXtpHq57GZszmFU5418oNCOLM0sVgKbba+wphS1a5wxEq/wk473v3HvYCm0btyIR26xuLG+Dwr5oLzYCOtWsIc6V4fbbQxBMj3mEPwvUYzx5DGeOz9w/MzmF94RznlyYxBeRFzukNUW68xmTbZNjz4r8W7sZ+e257BE2Ts+YCTQbx1cF9GvZuUybRdEgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAqy/hGvqtb/3ki/d90VmlWX8I19Vrf8AvJF+77og438GX/tp/qT/AL3VzFTP8GX/ALaf6k/73VzEGTfHb606l/eS8/eEhaacX9PvutgvFuE1rzT7ZKDFo92LXSqhf4fN/ToyniNvz/Usy+O31p1L+8l5+8JC1kQVg5JeE1504S8Sb1DbDJNHDDDZ4qNJc5o6yCHd1hkewY+pAfH9f5lZ9EQEREBERAREQEXPal1Xa7ZtUuVygW/xOWx7QmxolDbeG5UdZBGbmGbOuPw3GL4rRxCsU0w4sK92mZKPlsxYl0hyTvqNryPwAIlSEowbCPr5fYqg65ERAREQERc3rrVduskMs+5yWRYwaV7n1pk93xoEA/WQjulOxtK18kHSIsxuJ3HXUF2usydDut1tkQ5ekSBEucqMIAGe7FmwBGD3a9M3v8+8i05QEREBEUfcceIcbTFnPdJLN51HMDDi0ftuPKJXqMOf6HQb3v8A2BE9XwQSCizbuPGXX2pjmpBkXR2LmvrD01Fkj2G/qfCo8+32/be/8a9PQPMfqzT81ka8ElT48cgxTYF1FhOG2lPsHIzfHIqzpX31X5f05UDRFF42lL7HuMKLOivq+NcI4ZMd7m1Y5wjjoRmTK07CefpXsoCIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAo/4qcKLFqQWF1gDIag9sE8PubgCmEijMJQ6Ve8bCSCPoF+Ys65Oa5SAiDP3WXCDVvD2T7Zsk0suOxhxEuNuiuqQAPDbx/aluKwzGRPdkfnVxWN8IN7tp9RKZuBPNXb7tjEv9Q2m4O33tmUdQNoKwfQjGbxzvJEkbedMCdjtj15FYJWcVdePnLHbdQONOtzh2q7GeSQc2D3xLiUga+UoFH/AEMjjsG5xgs/KHc5pXP7QsUiz30/r7WfDWVS0zo+9ahSDbMaSMjoMlu4A8g1ouGFHszG+nb3ME6WRxAbtXK3nBvjLY9VNfS2yCNlx2b0m3TBbMsId546Pwo9wzj8h1q8L34b4MsXPxQSYiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgKB+eSzul6OmPYOhHW2VDlt6Dq9420NsPKzp1qPEZ35O/QqT4KeF592twJQDRZImHjyxODIARtHCKIjKjIx7K+WFWeX9KCjPIJri3Wy53O3zZDItb2KFWGYxGCA48V52eGzfX5r/Fdnn3bdftVbRXhvt7iwI5Zcs448WOxzynM9jRtaz4+apjxK5Org2Q81glxzQyvdVkS4FeCTGZXr0Hv0Y4chnXPv7PjT1+pR9aeVPWx30YS2giN6fOk3KA4dP1fRDGJ/iag49jmag1jV4huIG/6pcVoXM61dHnXOpPeMp/c39y1UVc+W3lwBpkrbpcjDnXVrOkeoRu8PB3B4E2akpmc/Rz2Z1a3t69vVWMQEREBERAREQFQrmF5pJ1xJIt+nikg2sZB0bchOLHuU3ZeRz3sJR7SQ4byUHTbo2hXNFTJzN14qSnz/AOuJlttMC1Q3kBTURZlJsgZaMc6HEGChIVaYZ1GZ80eTmPb2ge12bSvVCUBERBMPBHjvetKuoIL/ABturhQlpmFK4DGb1TkdBJR/0CS/M/e1rmOrIq57H4Mw0O4c6uiXy2Q7rAcR0S4Mc8W6PbIyrHkAYJGVrXoQZhkZXCrmdR9rnN6OrkgrKch+u5kPUDLG15X2++ClOdGqWjRgmRYpJbJjGbbveVDFcFzWVZnujc7PaY1BoIiIgLPDTPCvWuvZbJl4LMBF/tldxuGMbatH1bb7d2bmfRlfctYL3dcnZLQ9EGRnEizDtt5utuE5zxWq6ToQnvx3HDiSiAY5+HlV+I+tVrmsm+O31p1L+8l5+8JC1kQEREBRhx44SR9XRosWXMlRBwDukM8LQTtwr2bTM9xlfJtM/Kn8pVSeiCLOAPCUGkYc2JHkvl+OnUk+ILGaEjQ0CITAEqx9aFwcw7suz59aY+XV1RvwgUqMTVrWgcOpI9mhim0H6myd+WSjCf3TwxItf5tWKynM/wAeY2lo1YkSrJF8liyBHd3DhMf/APFSvPzp+gP7f81V75bOB0/U9wZqK/Uc61kkPlF8Tnv3g/XPo1nT+J7nTN/26Dwb682BazlbtR4OkLECS51TeC3nUI1zHNZLMeWAPQnn1YM42f4ClBfmylG9KUpSlKeTaUX6ICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIK76q5tNO2ydNt54V7ee1zZMI7wxYDxOLFMQBHs3JzH1HV4+tOrWrzv7NPS3+4L/AP8AQ7b/AOoqmnHb606l/eS8/eEhXK/sLNLf7v1B/wBMt/8A6cg7LQ3MppS7FFHZPdDkyKs2w3ED49MibdKCqfuBuZvx6Z/n6KZmupWnWnnRUA5lOWz+DMGt2tks8u3geMUwUtofExt99RsNUg6MYQdXuAzybR+ZGf4MtciHFM1zhyLFPNuyrOJhoBCOq4pIFXbbxvrWvfUJKjp1/QOOn2EFp0REHg6qsUS6w5EC4R2Soc0VRmjk64kp8aedOjxvY/B7XsrR7HsY5uLm0VQ+OHKxKtxK3bR5pDqQc5jrbU7/AGgAoz7oPY5hs3D4D9LHu3fo/Y4z34Nu0iClnB/mymRJDrdrEBa7BfDuuAYWxMin8SQZx3OEOrGVGMZPyImvb4THaK52Tba6Vv0W6w48+3yGSoc0VCBkM64vp1pSvlXvGRj82OY+lHteN7XYubVcjxk4NWPVTWVuUcjZcdmzGuMMuzLCHeYSrM6scM4/IlKMMx+HiD44ufkqh6g0DrPhrKrdoMjetQpAd6TGIR0GS3cOCOG72/Oj2ZjfXu7mCdLG0Z92rUGhCKvnA3mbs9/8LAnVpa73I2Q7L2u8DNlPqTrSCelX7ee2z3JsH5yBjY4zu5WDQEREBERAREQEREBERAREQEREBERAREQEXL6h1vZreRoLjd7ZbzPY0rAz7jGiFcKryD3BsORj6jzYRufT7D/zKPr5zL6Li0k09r+ILEoalQwoMw++UNH9WRT7HhSVe8fRhKloJ3qyx70E0oqoX7nTs7BUdb7RcpR3FbR4ppI0AVA1a/vYcBJBHk3MOyrPtk7u2lHcLfudO8PLR1vtFtigaJtHimkkzy1NRz+9hwEjjYPbw7Ks+wTu7qUaF6UWfD+LXFK7gNIhMu5INy8RQT7Pp3MAxkeQb2QZo4jjsw72Mfu7rNv1Zdy/aRwM4l3pwYd1LMdF3aF3b1qNkuGAowlwfsAlSCUf3vY17BO+f9huSC7Oodb2a3kaC43e2W8z2NKwM+4xohXCq8g9wbDkY+o82Ebn0+w/8yj6+cy+i4tJNPa/iCxKGpUMKDMPvlDR/VkU+x4UlXvH0YSpaCd6sse9QNpvkruZKF9pXqBExw2PARZNxqTyJubniPDbfT3de3PPN/pw7+5sfJfYmAG2Zc7tIktq7dNGdDiAJ3vw2wEAZ46beNPMrvhV3b1wQfjfudOzsFR1vtFylHcVtHimkjQBUDVr+9hwEkEeTcw7Ks+2Tu7aUdwt+507w8tHW+0W2KBom0eKaSTPLU1HP72HASONg9vDsqz7BO7upRtirNy7aNhnHJFYQEeLLFk2RNmhrR7SDrnFlmeAvSj/ACzZXHyd6qdV32mtKWu2btbbbYFv8Tjv+z4UaJQ23nt0JSONm5hm/pl8Nx6DMTi3ra76hmjul4rkSRFd7PxisjgbBHMl4Di9nU8dkisplCPc9/URGue9zFwauZ+Ef0t/sHehg/3RbJ0ve/8A3duBsVf/APqjs2M/nO9FFTNAREQF2nAn606a/eSzfeEdcWpq5NNK+09YWvcDvgtFS3OR73b2vCM+iGr0Ix5MJ5IPYzL49zatzQaXIiICIiDJvjt9adS/vJefvCQtZFUzW/J77UulyuX8Idj2tcpk7w/sapdrxUkh9nc8e3cw3McsWq2aCCeJ/M5YdP3WXaJsS7EkwNndJEjw3gdvxgSh1GQk1j/lnZ9lS3pG9juUCDcAtIwV0hRpgGHo1pWilBYYbSUG9zNzbfTyo53T9aqFzv8ACIAC3PVhrwxhbgWACLZ3QqNcYgwRIr2Dl+K78AgIbyF8B4/tK2PDC1PgWSzwS+ZbfaLdEL5Vp3x4YAP7fxebEHTqKOZnii3StlfKHg+4TX+HtgSebN7HqQxOtPlhHTPp9p9Rt8s1K6gnmQ4EF1jKhFrePABtscgxR623xVXFkEzOahazRdOrBR2YYfY9Xn2BSbhzqGzEvT7rq2lzubHP8U8MVgDumyau69Jr5BxfRqefYz1eTfJvxtjF5ydKDY1g7dfmsZRjGMZCtrWtaz0NYz2j5Up8FyP9gx/wo/0B/wC5J/YMf8KP9Af+5ILQ8MdaxtQ2qLd4QjjjT9/aHLYxp27Ek8V+4MT3sp1IB/2q+XRdWuH4K6J/g5YoVl8VSb7O8V9K2PDbm/MPK+RuP28d/HpnX0fiXcICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIMm+O31p1L+8l5+8JC1kWTfHb606l/eS8/eEhayIOF4+hYTSupWOp1o3T90f8A4Q4RyMr/AJRlFRrkVub4+s4Am060uUSdFfXrj0YyMSX/AIfvIg1czmj1AG3aRvZDOx8Zb5FvA2nk555w6xRtZTr5/Me+v7DHqpf4P7T75WqSTqiyFZracu7+IZ5VKRB0/nuE+V/Qx6DQdERAREQEREFXONfKXbLi0knT+FpuDyNfWIR5PZBtwxHn7BjeSGT3nbQPUTWx2M22Z5tiDRvF/VvD2T7GvcIsuOxgCjt1xlOqQAPDbIPZdxE8zGRPdjZhRpWN8IRjdp9SrQJc7q/S9uvMZ8K5wo8+K/J21JZntuewo94D/mAk0G8lGmZVr2blcXUQeRwq4l2fU8V8m0St2gaipMjFG4MqIU46PYM4X1/ntzZmJ7xkxc7By7lUW4pcsV9sMmtz0lJmSwxGVcNoZGxfI30Y/iqjeBgmS2PYzHoH3r/F0HtPxzf0fBXm+oRwoeqRMBTbrT27DGWrXOGIdGeKggY9+497D1qUPbkQbdpjcntC4yqxxx5toVud4TTjI93kNzaaeZxqW8BRmoOo2DHRj7hmNhu9j2C7wua4ve1vjc5nHmL4F2n7HKjzfa8Zr7jdIU8ZwBi1MSngwEiG/jJqArQrX9mySjcX73VlJ0E83nmn1mc7zDuEeEImDmxIlth1ALBjGVqN8wBj1zrTPve/5n6PbT6tOc22sIlC+IPAudS0bh4+AMezhuVft+zHx692dPXn8tmOPdlXxEGlvAjmBs+qqsi/7HXl9JFa2oxXl3BhpR+5Fl7bGSPdvzw7Ct2z9uDM3TWseLfMKAojhKQJ4z2kAYT3DIEo3UIwg3s7xkY/uo6levkr5aE5tdPntLZN3eSDdQidSRbo0WSZsoo250dCPRlRjGavoYYrKsfm1zsWbrwsqiqhfudOzsFR1vtFylHcVtHimkjQBUDVr+9hwEkEeTcw7Ks+2Tu7aUdwt+507w8tHW+0W2KBom0eKaSTPLU1HP72HASONg9vDsqz7BO7upRoXpRZ8P4tcUruA0iEy7kg3LxFBPs+ncwDGR5BvZBmjiOOzDvYx+7us2/Vl3L9pHAziXenBh3Usx0XdoXdvWo2S4YCjCXB+wCVIJR/e9jXsE75/wBhuSC7Oodb2a3kaC43e2W8z2NKwM+4xohXCq8g9wbDkY+o82Ebn0+w/wDMo+vnMvouLSTT2v4gsShqVDCgzD75Q0f1ZFPseFJV7x9GEqWgnerLHvUDab5K7mShfaV6gRMcNjwEWTcak8ibm54jw23093Xtzzzf6cO/ubHyX2JgBtmXO7SJLau3TRnQ4gCd78NsBAGeOm3jTzK74Vd29cEH437nTs7BUdb7RcpR3FbR4ppI0AVA1a/vYcBJBHk3MOyrPtk7u2lHcLfudO8PLR1vtFtigaJtHimkkzy1NRz+9hwEjjYPbw7Ks+wTu7qUbYqzcu2jYZxyRWEBHiyxZNkTZoa0e0g65xZZngL0o/yzZXHyd6qdV32mtKWu2btbbbYFv8Tjv+z4UaJQ23nt0JSONm5hm/pl8Nx6CjL+LXFK7gNIhMu5INy8RQT7Pp3MAxkeQb2QZo4jjsw72Mfu7rNv1Zdy/aRwM4l3pwYd1LMdF3aF3b1qNkuGAowlwfsAlSCUf3vY17BO+f8AYbktAUQUd03yV3MlC+0r1AiY4bHgIsm41J5E3NzxHhtvp7uvbnnm/wBOHf3Nj5L7EwA2zLndpEltXbpozocQBO9+G2AgDPHTbxp5ld8Ku7euCtSiCILNy7aNhnHJFYQEeLLFk2RNmhrR7SDrnFlmeAvSj/LNlcfJ3qp1Xfaa0pa7Zu1tttgW/wATjv8As+FGiUNt57dCUjjZuYZv6ZfDceuhRAREQEREBERB4OqrFEusORAuEdkqHNFUZo5OuJKfGnnTo8b2Pwe17K0ex7GObi5tFmlxr4QXXS0wopgXmgZtpCvAwEbEltfQjxj3PQCZgAmUZ7sm7b8c24PdqWvLv9oizo74syMCXGPhuRZYGSAE23sIPdATsJRhGMd59floMe0Wiuo+UnR8uovDgn2ygquz8BOITez26M3PabJFO3Cvow+Y/LLtx83TPJ/pmM4D5hrlcHgF0khJIDGhyi7O28m3EGySAefV7GUkeWDMnP7sgo9pDS9xvMlkK2QpE+U/F21GZntse8Q947/lgjUI8dHGfVrGblMnUWknLtwrj6UswofSOS4yfe3a4Rxvb4mRkSo2UITvrHCN9Qs8mflH4scV66PQGhLRYI9Y9ot0eCx/zXCo9xz4PI8fiJRMzyMKnJhm9+GeLe1degIiICIiAiIgiW48ErZJ1F/CKeaZOKJwiw7dKNUkGEcbB++APpufMHR+31wzJ1x8mYS0iICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIMm+O31p1L+8l5+8JC7P+yj11/bz/AEVZ/wDyK0xRBmdJg6810cDTiulwZVrHBMcFYlsCx/T3/XBkQdasfSubKZvb+krvcunCwGlLTSIytDzZb2yLlLpTpQp8ejWD/HSOP0sp+t7vtqU0QEREBERAREQEREBQ9xu4EWXVTalMzwVxpnUd2hiE0737NADbOHVn0+MzAHY5zXtpHo1j2ZvzmFEGRGvLHS2XS5W3d3/ZNxmQayMNrdrEkkBu7dXu286jq7DJ3Tr/AErnlJPMXbDRNWajHIZQT33mZIa3cY7IE0xJ0V/Qda0745wP/O3cpl0d1UbICIiApl5UeGkHVd5k2+4FlBDHtJ5rHwXhGWpRyYYKNfWQArNvCU/4Np8Gf3lDStT+DntRnX26TaM6x4tk8MYubK4HlzQEAzb9fVw4Ur4fyfn0yagshZuXbRsM45IrCAjxZYsmyJs0NaPaQdc4sszwF6Uf5Zsrj5O9VOq77TWlLXbN2tttsC3+Jx3/AGfCjRKG289uhKRxs3MM39MvhuPXQogIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiCl/PnwiLuk1bD2qhcyNHvInPcwrC5DhxZrNx+BBuZWLGcxmOGDHYvzK9lN1sRcYYjiKAwhmBJY4ZwlY0gzCI2o3jIx/YQb2dtW1p081TjjbyimY6svSjqyAuo/ds86QxhxvfIpgyDLJgwkdg3+iS+j20j+srn4NCnyKSL3wZ1XEOSOTTl2cQWOVY0A00Ds2Mf7uVCY8JK99KdGO7K0q31dV9mmeA2r7hQvh9PTx1j4Z+0GMtmW5V9WUH7TeHf8ANlfRlh2ZepqCK1oFyG2C2xLEeTEnw51xuxRSLmOKV+7AEyhxwYUoBX5jIx9Jr88GZ7j8XFYxj3+bwm5Q7ZEA4mo60us4m610SJKkgt4Gbg9hwyD2ZR5FGMf3Pcxnv6tw7KFdHHETly1DpSWO96WlSJ7YUhhI7YgH+2Y1HkIOjXxRseO4A29hhXMp375MgNFmgveiqNwD5tBSqhganoONJKUMePeAtaOG73ONSXQefSG9x2U98Fu17/uaFgqvdam3zBHEI4SjMCSxpAGE9pBmERtCMIN7Owg3s7qOpXp5oPQREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBEUe8WeK1n0xHZIukitHHzpFhgHuS5LhtrUlBjr8GfD3j8Gd7O7uogkJFUR/O3BpJo2lgl1ifjkVnhbJ/6Lsbf6P5VTrwg4u2bVAXvtp30PHax0qBJZQckG58HVb1qwg69fWxz2eSCRkREEKcd+X6z6qq+V/sdeX0j0pdQieXcGGlWbcqJuMZI92/DPsK3bB3YMwdVtkvW/C6S8NKMJbpJhEc6oTS7DMOSMRjKDPgIkeY2g35MY8T3+EHlmNjKu0PXn3GGI4igMIZgSWOGcJWNIMwiNqN4yMf2EG9nbVtadPNBFPBHmAsWp6siheSFdiMcR1rl+TiVYETz+ElM93LGyrydKdhcY5HbTGtUzKn/G3lFC9tZelHUjmbV+7Z50h7wEYyPTBkGWTN45DyM9El9WOrI9Ymswdy3C3mdvthk0tmrY0yWGIyjSONH2L5G+jA8LQjDvEyWx7GZdTe9f4upN1+ODwvSi5fQWsrZfIfj7VMZNiVe8NSsaQb2FH8wZgnYwgCebHYPa3qwg3ebXtXUICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICoVzW8OtXXnUdxuA7NNkwAUYC3PjjGavhQM/JhE/c75Dzv6Y5+8V9UQV4ZylaW9mUiujG8f4XB128bJ3PE7fztjc2MN3zww//KqFywXk8HV1ifGoRzpU8UI4xVf3Amu8OfOrOtSDYN+90/uFPh0zVxOa/jaDTsI1thloS93EDmBax1OsARGVZWYevTownT0M/wAL0084Y5DOFhpM+mpZTKsh22pRWylWvbWTMIyo3mZ/KRwjeRv88n7D6ILzoiICIiAuG4q8NLPqeKyNd4u7QNS1hyREcGVEKcdWPIAzKfzHYPzE94x5Ndg1dyiCgfELgdqnREqTfNOzJBrfEyNSZDPjOjQhvAfC6RejWTI9CUpng0onMikKRgm9ilngpzaWy4tHG1Bhabg8jmUljYT2QbcMNgO8j3khk953VN1E1sd79xmeDbRqvnHLlks9/wDFT4NKWu9yN428xzvAzZT6j6VnArR+3ntv98HB+cghHtM7tQWDRZ72XVetOGE1sGeLxFtkZ+HhSZDy284QTCEMa0HG/wCgSH5vrhVlP42NxQO7FbXgfxns+qw08GbZuIozTT7QajvERq51GSrH1Y0cuPn+VZ8N8ObROfgglNERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQFB3NHxuDpWHQEXA97uDK1hx3UybGFXs8adn8nR9OjGfbfSv6D1OKzR41aZ1Xfr9c7m7T+oCjlTC0iZWK5Nq2EN23EZtkBWo/cMZ5fpZoJD5beBMnVJ3ak1M4r4co7jiGZ7t+6FzruGI/8AJwuv5vX9nFtO678GIOOMYRMYMQWNYIQm0axjR+hrGU/V/wBiyn/1J9U/72r/AP5iuX/gLsODfDbUcfUVgOewXsAY9+tZTmNZp7BhEOeB5HkIQOA2MZSrsq/BBpoiIgIiICIiAiIg8u/2iLOjvizIwJcY+G5FlgZIATbewg90BOwlGEYx3n1+WqgcYOU2ZEkNuOjjlrsF8Q23mm7EyKfxIyAJbJpKMZUYxk/LFa9vhMt0rnYtumiCkXBvmpm244bRqqOUgoZKQj3J9DMucLaedj3XGKTJ80jH7LH4UYVrQEc7xBPjbvSGqLdeYzJtsmx58V+Ld2M/Pbc9gibJ2fMBJoN46uC+jXs3KZNoub4vcJLLqgO1c43SQzaaG5RWhFcAMG8hNpksg3bkf3hvcva5nvKuxyox7ai6r0Dq3hnN9q2qWWXaRFh1kTAteOHJc/cHSNeLZQzn4ZkMNpa5Nb4gOJWFfiwNAEVcOCPNPZ7yyke8Pj2O4NwbmYzqW6XSgtw5hyiMwgV3Bkpsmf8AlANaQrn9lj0BERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBFFutePGlbPOPbbldPDToe1vx6265G298Izj6kjxXjfSoyDf2u/H+peV/ZR6F/t5/oq8f8AkUEzoo60rxn0vdHDHBvcIhZDsRAM98Q5HdH9W0BLYwn2K/Z/7VIqCtHGrlTs93cSbZnss01zGtbEFHbS0SHiCRjOsYDGvhPeSgKOMHJlGDe7ae57nKFtG8UNacPZAYN9iS5FtaJzA264nyE7bjA2/ZV3GwzNsLPCs2WPeJm6RuDHuzZbviJxk03p+UOHebj4OSaM2UMXgZ8nIBHkGwlHxAPZT3gCU869fd1X1x6WDWNnGWoQXa03Bx3AfJimb3jdIiEMDxA2HiSGe/Y0zMHs+y5B+PCvivYtSCztU8ZDUHuHgG9zcAUwj1fnEJWr3jYSQNlTMzFnXFrnKQFRvipyv3mwEbddHzJ0rw+46oRlZHvMIfhehCAkR3s8dn79mAWsL7wbWsLk969jhBzbHhk9mawjyN+PJME92DHYE4H74x7NxtYxs29n3+bw0zpQQ27T3ZvcFzEXl2C7xZ0dkqHJBLjHz25UQ7JACbb3jJtHH2EowjHt8uvy16iAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgzO51/r1ff6r+5oCk3RHJ77UtdtuX8Idj2tbYc7w/sahdrxUYZ9nc8e3cw3McsWqMudf69X3+q/uaAr+8Cfqtpr927N93x0FJeNnLDctPQSXKPLHdIcSlaytqK+NJA3NjKH2M37gvOlXuo/spTL0qWuRTjBIn1Lp65ncU8UHiLXIM/IpAD8jxnvr8yrNxj2fsbn6CtDe7cKXHkRDNaUMwBI5hvbk0gjsIMgyM/Qwf0WY/LBd/Baw08bpWud0FE8v8A56hIP/8AaQS9+EbtT2Xq0Tq17JlodEo3p8HxJhzP6v8Ah/8AHM/5isrymWl8LRlhC+vWr4bpba9OnZPlHnjb/k5DF0fEjhtZNR0A28waTaQKldF+kyY7hVPt7nfEMx9aP2h+Vf5NdJaYAYccEWONoY8QIo8cLPQIIGUGMbP5g2Uog9FRLxn4IWLUojvkRRx7mUTqAvUZmElhaNAMb5TB4snjawA2YG9LM2scLLOktIgz2udl1zwzkmNCLINZmS86yWD8TZpQ84ffOhZv9mSTfRQ5uqIvXNgivbTNWS4H8yNk1GSkU/Wz3J2FBwpskLgSXENUAwwZfZ4iR1ID3L2Mf1J2tfg96me4wxHEUBhDMCSxwzhKxpBmERtRvGRj+wg3s7atrTp5qtHHHlJhXF3i9OPj2iQ7NxoBmmrbzlIahKkYQdXvt+A3m7GMeLsC1rRd7nBadFQrhnxx1Joc7LJqWDMNBiCGKPGlUYGXCjjlEHU0GVVmFzh7YzsYxz8HbAWiIJrK5XA4Z8RLVqKG2Za5TDdWCeaNUjGzITibjKBnRaPq+OTcAan6D9vJjnt7kHaoiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgzO51/r1ff6r+5oCv7wJ+q2mv3bs33fHVAudf69X3+q/uaAui0rzaaitkGFbwQrI8FrhRoQHmiz3lcKKEYBvftzmMqSrB9fJrUF+9SXYUGFLmmdRgYEU8gr6+TWtAx5CV/+yqzP5UrJWdrCxDxc5see2Y/Hr2+Ba+YNzv2NwA+q9viJx81TqoLbT7pgZdcH2+zxTULN86EGwmZDHJ6PQx3T9LJWT5NeChtPANdroKjbrchUEKO7FzoUWj6Eewlev8AGXkYPL9DbZT9NBZZERAREQEREHIa/wBCWi/x6R7vbo85jPlOLR7TgzeN5PDyh4Hj51APPB7M8MXdqp/xE5ctQ6UljvelpUie2FIYSO2IB/tmNR5CDo18UbHjuANvYYVzKd++TIDRZq96IKjcA+bQUqoYGp6DjSSlDHj3gLWjhu9zjUl0Hn0hvcdlPfBbte/7mhYKr3Wpt8wRxCOEozAksaQBhPaQZhEbQjCDezsIN7O6jqV6eaiTjvy/WfVVXyv9jry+kelLqETy7gw0qzblRNxjJHu34Z9hW7YO7BmDqtsl634XSXhpRhLdJMIjnVCaXYZhyRiMZQZ8BEjzG0G/JjHie/wg8sxsZVwaHqCOYbmIt2l92CCnjr26M94o1OnhoT37dAOuJKEzZmx1StCzq9zWMy2mlYVcncub2zPsUmZFY8d8YNjItmnCM4bzv2dwrJcdlRlhhq8ju9wXl8KRuIs2VVINQ3Y82XJmSSbkifIPJkFwYzcOd7yGfgPoxmRHu9HkgkrV/MRrC6ZtJeZEUNZD5Aw2prIGz5EwCM8XGU+Oxj+mBSv9DHOyc3JeDbuLuqQEGZuo71VwSsKNprpMkCq8btym4CQR4zjrWlKYPa5jqV7vzKPUQWp4Tc3dziHcPUdK3WCTdc6XEixgXAD9sew0Yx7MU8ej2P7XtY/39XZ9lBOujpW/RbrDjz7fIZKhzRUIGQzri+nWlK+Ve8ZGPzY5j6Ue143tdi5tVkKrL8kvFotnuYdPyNr2XqGb0HVzHVLEuZmDAB7KjY55GHeOKBzH9rPdvyZgXMNAUREBF88g7Rtc99aNYxrnvdX8TWfFZz8WOMmodXXh0K1yJg4UmV4e12u3veF529asG89R4PI9/m92fYz/AAEGkCLMCXE1joGXFqV0uzkkVdICFkwJ4crb22E3BxzvBI/J5sf/AHP9hX64C8Qhanska6NbQZ3OfHnx2OyaGYHpuM+PoeN43to6voINBIqIiAiIgIqo823MHEjw5dhsklsmfNo+NPmRyVcGAKtMDCYZlfeTH06s6M64d/wfRRf+Dl+tNw/duV94WtBf5ERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQcjd+HtimmJKm2S0zJR8d6VLtcOSd9RtYNmZyjqQlGDYNlPP7FF+P+pPpb/e1YP8xW3/wF2iIPDsGmrdb2VHAgQ4TPxMhxAx2U7qv+WBjftvfX/wD2q9xEQEREBERAREQEREBefcYYjiKAwhmBJY4ZwlY0gzCI2o3jIx/YQb2dtW1p0816CIM9+dDhLaNLntRrQyQId58duxSneYIPAsgsZ4d5Pf0o/fI9+b3+fpwb2qt6vH+EdsdSWuy3PdrTwFxkQaR8PMntGLQ+9nn7vD2Xjjj3b9fTj3UcQEREBetp67HhS40yMTbkQJAJMcuDH7ZwPYQL8CdWPxIxvr8l5K6HQdjpc7pbbbu7Hta4w4NJGG5s1lyRg3duj27mFSUdhk3r0/pQa7oiIPkmxxmG8RGNeMzHMKN9Mmva+mD2O/x9Fw0fhfpm3SB3WNZoUKTa6HkBkQhUjVH0DIYStWDq0ZKVGclOj6Y/L+GDOkiL4LtDHJCWMTLblCIEuDntdgRmD8Hsr1HXo74oM/uYzib/AKoVzs8CxW+X1iUlMiik7LZJzy9ghewZHjGxg4g/t/pq4HLbw6dpiwAtxnDdKIV0uc8PXb8UejKYMr+UwGMA8/tbagbmu5fdP2jTxbvZ47oJ7WcHiG+IlSmSQSDDi4fSzv2yMecb82fyZO34VZ7/ACLcVp11FKstyOSSa2x2yoEkxKkkPi7mwYJCP8yUYQgMHVr8CVb9hBapERAUHc4enL1dbDGhWIcosiTdhNlhiyfD0JB8HP3mSnkIwfhqk2O19cctv9SnFEFBda8tVNOaQu95ukiki7RxwmxY8R7/AAcTfucQBHvfg18iRsEI3p6G7j/X2Pp+f4OX603D925X3ha1ZfnX+ot9/qv75gKtH4OX603D925X3ha0F/kREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQctxG0jEvlsmWqe0jolwY1hdom2RlWPGcJhvpSvQgzDG+mdHM6j7mub1bXMXixoWZpy7SrXNG+nhivrFM8W22bD3CbE0HR72YPYz05vwdmx3cx9KaxriuJnDu1aihuh3SKw3VhWAk0GxsyE4m2+poMqrKvjk3ABr+g/bxe17exBk4iuBrHkrlto51ovUc2Uh23GukUkfajdCYVJNibu/Ib7tvyRNd3u7OmFebs3JvqMr2UkS7TFF4l4jOpIknO2OM7x+JCFkfbJmMe8xjys67jGu2nZUaFY1djkX4OVDQWq7mOQOS+haWKOX3bKRTB233N/R+ZN4cg7GNe1rMOpOj90T29jwh5ULJZj+KuRvb8hu60IZUIArcxpGDZmSC95t+Q3obue+rPeU7MmMerHoCIiDlOKFlkXK0XCFEO+LLlRCtiyRFeF4ZHTMD9wb2vZ7xjOtaLPrhXxSu2ldR+LuvjJz4rZFvuUSbJMWUwJCDeegXnf0oRpABf0r2P26fqe3TBRlxP4Lad1G/euUGlZbGYNnRikjHq3rXpuPH7s/997X49aoKs8ynM1E1FaHWe1QpQRTSifNkT6BG7ABmHEEA45n+e+xj6vc78n6e/qzuvwe/D+RFjzr/ACQ1HS5CZEtrnjq1z4rH0IczPhXbeQYKdftbH4132kOVHSFvI0ro0u5vY/NlLrJYQTelOmDgAGIZB9fxPa9TiADBMaxjWsYxrWMYxuLWtZ6GMYgrbxm5qf4N3ydZPYXjfZ3hvpXtbw25vwwS/keBft47+Prr6Ov6lPeg75W52u23La2Pa1uhzqR89zZpLjDPs7lGN3MKEo3PFvXp/Qqqc7fD/T7CSrtSdNJqW+HgghWgJoxBmeNsWI+vhWR9/Dw4Pjn80jPz4K1ugLN7OtNrt/Wta222Q4bq1+LvCxhg6/8AVoPfREQQxzr/AFFvv9V/fMBVo/By/Wm4fu3K+8LWrp8TtFRtQ2qVaJpTjjT9jdJEexp27EkEpm2Qo3sp1IBn2a+XVcLwc5fbNpWea4W6VczHkQiwnsnnjEFtEMA+baAiifuZxR/a/G/++gmVERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREEfRuFFiZfTai8Ex10k4O3i1c4YiiaMe8AHyxyKjG3v6ZfM/TepBREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREH/2Q==)
   2 DEFINITIONS 4
   node that represents the start of the game. Any node that has only one edge con-nected to it is a terminal node and rep-resents the end of the game (and also a strategy profile). Every non-terminal node belongs to a player in the sense that it represents a stage in the game in which it is that player’s move. Every edge repre-sents a possible action that can be taken by a player. Every terminal node has a payoff for every player associated with it. These are the payoffs for every player if the combination of actions required to reach that terminal node are actually played.
   Example:
   Figure 1: A game in extensive form
   In figure 1 the payoff for player 1 will be 2 and for player 2 will be 1, provided that player 1 plays strategy U and player 2 plays strategy D’.
   2.3 Nash Equilibrium
   In game theory, the Nash equilibrium (named after John Nash, who first described it) is a kind of solution concepts of a game involving two or more players, where no player has anything to gain by changing only his own strategy.
   If each player has chosen a strategy and no player can benefit by changing his strategy while the other players keep theirs unchanged, then the current set of
   strategy choices and the corresponding pay-offs constitute a Nash equilibrium.
   John Nash showed in 1950, that every game with a finite number of players and finite number of strategies has at least one mixed strategy Nash equilibrium.
   2.3.1 Best Response
   The best response is the strategy (or strate-gies) which produces the most favorable immediate outcome for the current player, taking other players’ strategies as given.
   With this definition , we can now de-termine the Nash equilibrium in a normal form game very easily by using the payoff matrix.
   The formal proof that this procedure leads to the desired result is given in ap-pendix A.2.
   2.3.2 Localizing a Nash Equilibrium in a Payoff-matrix
   Let us use the payoff matrix of the Pris-oner’s Dilemma, which will be introduced in 3.1, to determine the Nash equilibrium:
   Player1\Player2 C D C 3, 3 0, 5 D 5, 0 1, 1
   The procedure is the following: First we consider the options for player 1 by a given strategy of player 2, i.e. we look for the best answer to a given strategy of player 2.
   If player 2 plays C, the payoff for player 1 for coosing C will be 3, for choosing D it will be 5, so we highlight his best answer, D:
   C D C 3, 3 0, 5 D 5 , 0 1, 1
   Now we repeat this procedure for the case,
   3 GAMES 5
   that player 2 plays D (the best answer in this case is D, since C gains payoff 0 whereas D gains payoff 1), then we do the same for player 2 by a given strategy of player 1 and we will get:
   C D C 3, 3 0, 5
   D 5 , 0 1 , 1
   The Nash equilibrium is then determined by the matrix element, in which both play-ers marked their best answers.
   Thus, the strategies that constitute a Nash equilibrium is defection by both players, because if any player changed his strategy to C whereas the other one stays with D, he would get a less payoff.
   2.4 Mixed Strategies
   Consider the following payoff matrix, which corresponds to the game Matchin Pen-nies:
   Player1\Player2 Head Tail Head 1 , -1 -1 , 1 Tail -1 , 1 1 , -1
   The best responses are already marked, and it is obvious, that there is no matrix cell, in which both players marked their best response.
   What do game theorists make of a game without a Nash equilibrium? The answer is that there are more ways to play the game than are represented in the ma-trix. Instead of simply choosing Head or Tail, a player can just flip the coin to de-cide what to do. This is an example of a mixed strategy, which simply means a particular way of choosing randomly among the different strategies.
   The mixed strategy equilibrium of the matching pennies game is well known: each player should randomize 50-50 between the two alternatives.
   Mixed strategy equilibrium points out an aspect of Nash equilibrium that is of-ten confusing for beginners. Nash equi-librium does not require a positive reason for playing the equilibrium strategy. In matching pennies, the two players are in-different: they have no positive reason to randomize 50-50 rather than doing some-thing else. However, it is only an equilib-rium if they both happen to randomize 50-50. The central thing to keep in mind is that Nash equilibrium does not attempt to explain why players play the way they do. It merely proposes a way of playing so that no player would have an incentive to play differently.
   If, for example, player 1 chooses to play Head with a probability of 80 % and play Tail with a probability of 20 % , then player 2 will eventually anticipate the op-ponent’s strategy. Hence he will play Tail everytime. This will lead to a positive payoff of $0.8$ · 1 + $0.2$ · (−1) = $0.6$ per game for player 2, respectively a payoff of $−0.6$ for player 1. The best payoff one can do in such a fair zero-sum game is 0, and this will be achieved by playing 1 2 Head + 1
   2 Tail. Mathematically spoken, a mixed strat-
   egy is just a linear combination of the pure strategies.
   3 Games
   Now I want to present some of the most studied games of game theory.
   3.1 Prisoner’s Dilemma (PD)
   We have already used the payoff matrix of the Prisoner’s Dilemma in 2.3.2 to lo-calize the Nash equilibrium of this game, and now I want to tell the story behind this famous dilemma:
   Two suspects are arrested by the police. The police have insufficient evidence for
   3 GAMES 6
   a conviction, and, having separated both prisoners, an officer visits each of them to offer the same deal: if one testifies for the prosecution against the other and the other remains silent, the betrayer goes free and the silent accomplice receives the full 10-year sentence. If both stay silent, the police can sentence both prisoners to only six months in jail for a minor charge. If each betrays the other, each will receive a two-year sentence. Each prisoner must make the choice of whether to betray the other or to remain silent. However, nei-ther prisoner knows for sure what choice the other prisoner will make. So the ques-tion this dilemma poses is: How will the prisoners act?
   We will use the following abbreviations: To testify means to betray the other sus-pect and thus to defect (D), to remain silent means to cooperate (C) with the other suspect. And for the sake of clarity, we want to use positive numbers in the payoff matrix.
   C D C R=3, R=3 S=0, T=5 D T=5, S=0 P=1, P=1

* R is a Reward for mutual coopera-tion. Therefore, if both players co-operate then both receive a reward of 3 points.
* If one player defects and the other cooperates then one player receives the Temptation to defect payoff (5 in this case) and the other player (the cooperator) receives the Sucker payoff (zero in this case).
* If both players defect then they both receive the Punishment for mutual defection payoff (1 in this case).
  As we have already seen, the logical move for both players is defection (D). The dilemma lies herein, that the best result for player 1 and player 2 as a group $(R$ = 3 for both) can’t be achieved.
  In defining a PD, certain conditions have to hold. The values we used above, to demonstrate the game, are not the only values that could have been used, but they do adhere to the conditions listed below.
  Firstly, the order of the payoffs is im-portant. The best a player can do is T (temptation to defect). The worst a player can do is to get the sucker payoff, S. If the two players cooperate then the reward for that mutual cooperation, R, should be better than the punishment for mu-tual defection, P. Therefore, the following must hold:
  $T > R > P > S.$
  In repeated interactions, another condi-tion it is additionally required:
  Players should not be allowed to get out of the dilemma by taking it in turns to exploit each other. Or, to be a little more pedantic, the players should not play the game so that they end up with half the time being exploited and the other half of the time exploiting their opponent. In other words, an even chance of being ex-ploited or doing the exploiting is not as good an outcome as both players mutu-ally cooperating. Therefore, the reward for mutual cooperation should be greater than the average of the payoff for the temp-tation and the sucker. That is, the follow-ing must hold:
  $R > (S$ + $T )/2$
  3.1.1 Other Interesting Two-person Games
  Depending on the order of R, T, S, and P, we can have different games. Most are
  3 GAMES 7
  trivial, but two games stand out:
* Chicken $(T > R > S > P$ )
  C D C R=2, R=2 S=1, T=3 D T=3, S=1 P=0, P=0
  Example: Two drivers with something to prove drive at each other on a narrow road. The first to swerve loses faces among his peers (the chicken). If neither swerves, however, the obvious worst case will oc-cur.
* Stag Hunt $(R > T > P > S)$
  C D C R=3, R=3 S=0, T=2 D T=2, S=0 P=1, P=1
  Example: Two hunters can either jointly hunt a stag or individually hunt a rabbit. Hunting stags is quite challenging and re-quires mutual cooperation. Both need to stay in position and not be tempted by a running rabbit. Hunting stags is most beneficial for society but requires a lot of trust among its members. The dilemma exists because you are afraid of the oth-ers’ defection. Thus, it is also called trust dilemma.
  3.2 The Ultimatum Game
  Imagine you and a friend of yours are walking down the street, when suddenly a stranger stops you and wants to play a game with you:
  He offers you 100 $ and you have to agree on how to split this money. You, as the proposer, make an offer to your friend, the responder. If he accepts your offer, the deal goes ahead. If your friend rejects, neither player gets anything. The stranger will take back his money and the game is over.
  Obviously, rational responders should accept even the smallest positive offer, since the alternative is getting nothing. Pro-posers, therefore, should be able to claim almost the entire sum. In a large num-ber of human studies, however, conducted with different incentives in different coun-tries, the majority of proposers offer 40 to 50 % of the total sum, and about half of all responders reject offers below 30 %
  3.3 Public Good Game
  A group of 4 people are given $ 200 each to participate in a group investment project. They are told that they could keep any money they do not invest. The rules of the game are that every $1 invested will yield $ 2, but that these proceeds would be distributed to all group members. If every one invested, each would get $ 400. However, if only one person invested, that “sucker” would take home a mere $ 100. Thus, the assumed Nash equilibrium could be the combination of strategies, where no one invests any money. And we can show that this is indeed the Nash equilib-rium.
  We will not display this game in a pay-off matrix, since each player has a too big set of strategies (the strategy $sn$ is given by the amount of money that player $n$ wants to contribute, e.g. $s1$ = 10 means, that player 1 invests 10 $). Nevertheless this is a game in normal form and there-fore it has a payoff function for each player. The payoff function for, let’s say, player 1 is given by
  $P$ = 2 · $(s1$ + $s2$ + $s3$ + $s4)$
  4 − $s1$
  = 2 · $(s2$ + $s3$ + $s4)$
  4 − $0,$ 5 · $s1$
  But this means, that every investment $s1$ of player 1 will diminish his payoff. Therefore, a rational player will choose
  4 EVOLUTIONARY GAME THEORY 8
  the strategy $sn$ = 0, i.e. he will invest no money at all. But if everyone plays this strategy, no one can benefit by changing his strategy while the other players keep their strategy unchanged. And this is just the definition of the Nash equilibrium.
  The dilemma lies exactly herein, since the greatest benefit for the whole group arises, if everyone contributed all of his money.
  3.4 Rock, Paper, Scissors
  The players simultaneously change their fists into any of three ”objects”:
* Rock: a clenched fist.
* Paper : all fingers extended, palm facing downwards, upwards, or side-ways.
* Scissors: forefinger and middle fin-ger extended and separated into a ”V” shape.
  The objective is to defeat the oppo-nent by selecting a weapon which defeats their choice under the following rules:

1. Rock crushes Scissors (rock wins)
2. Scissors cut Paper (scissors win)
3. Paper covers Rock and roughness is covered (paper wins)
   If players choose the same weapon, the game is a tie and is played again.
   This is a classic non-transitive system which involves a community of three com-peting species satisfying a relationship.
   Such relationships have been demon-strated in several natural systems.
   4 Evolutionary Game The-ory
   Since game theory was established as a discipline for its own, it has been very successful.
   However, there have been situations, which could not be properly described by the language of game theory.
   Many people have attempted to use traditional game theory to analyze eco-nomic or political problems, which typi-cally involve a large population of agents interacting. However, traditional game theory is a “static” theory, which reduces its usefulness in analyzing these very sorts of situations. EGT improves upon tra-ditional game theory by providing a dy-namics describing how the population will change over time. Therefore a new math-ematical extension has been developed (mainly by John Maynard Smith in his book Evo-lution and the Theory of Games, 1982), which is called evolutionary game theory (EGT)
   I will show in the next section, in what kinds of situations EGT might be appli-cable and what are the most significant differences to game theory.
   4.1 Why EGT?
   Evolutionary game theory (EGT) stud-ies equilibria of games played by a pop-ulation of players, where the fitness of the players derives from the success each player has in playing the game. It pro-vides tools for describing situations where a number of agents interact and where agents might change the strategy they fol-low at the end of any particular interac-tion.
   So, the questions of EGT are: Which populations are stable? When do the in-dividuals adopt other strategies? Is it possible for mutants to invade a given pop-ulation?
   4 EVOLUTIONARY GAME THEORY 9
   Another very prominent application is the quest for the origins and evolution of cooperation. The effects of population structures on the performance of behav-ioral strategies became apparent only in recent years and marks the advent of an intriguing link between apparently unre-lated disciplines. EGT in structured pop-ulations reveals critical phase transitions that fall into the universality class of di-rected percolation on square lattices.
   Together with EGT as an extension of game theory, new concepts were devel-oped to investigate and to describe these very problems. I will now introduce two of them, which are crucial to describe EGT, evolutionary stable strategies and the repli-cator dynamics. The first one is applied tu study the stability of populations, the latter one investigates the adoption of strate-gies.
   4.2 Evolutionary Stable Strate-gies
   An evolutionary stable strategy (ESS) is a strategy which if adopted by a popula-tion cannot be invaded by any competing alternative strategy. The concept is an equilibrium refinement to the Nash equi-librium.
   The definition of an ESS was intro-duced by John Maynard Smith and George R. Price in 1973 based on W.D. Hamil-ton’s (1967) concept of an unbeatable strat-egy in sex ratios. The idea can be traced back to Ronald Fisher (1930) and Charles Darwin (1859).
   4.2.1 ESS and Nash Equilibrium
   A Nash equilibrium is a strategy in a game such that if all players adopt it, no player will benefit by switching to play any al-ternative strategy.
   If a player, choosing strategy $µ$ in a population where all other players play
   strategy $σ,$ receives a payoff of $E(µ, σ),$ then strategy $σ$ is a Nash equilibrium if $E(σ, σ) ≥ E(µ, σ),$ i.e. $σ$ does just as good or better playing against $σ$ than any mutant with strategy $µ$ does playing against $σ.$
   This equilibrium definition allows for the possibility that strategy $µ$ is a neutral alternative to $σ$ (it scores equally, but not better). A Nash equilibrium is presumed to be stable even if $µ$ scores equally, on the assumption that players do not play $µ.$
   Maynard Smith and Price specify (May-nard Smith & Price, 1973; Maynard Smith 1982) two conditions for a strategy $σ$ to be an ESS. Either
4. $E(σ, σ) > E(µ, σ),$ or
5. $E(σ, σ)$ = $E(µ, σ)$ and $E(σ, µ) > E(µ, µ)$
   must be true for all $σ$ 6= $µ.$ In other words, what this means is
   that a strategy $σ$ is an ESS if one of two conditions holds:
6. $σ$ does better playing against $σ$ than any mutant does playing against $σ,$ or
7. some mutant does just as well play-ing against $σ$ as $σ,$ but $σ$ does better playing against the mutant than the mutant does.
   A derivation of ESS is given in ap-pendix A.3.
   4.2.2 The Hawk-Dove Game
   As an example for ESS, we consider the Hawk-Dove Game. In this game, two in-dividuals compete for a resource of a fixed value $V$ (The value $V$ of the resource cor-responds to an increase in the Darwinian fitness of the individual who obtains the resource). Each individual follows exactly one of two strategies described below:
   4 EVOLUTIONARY GAME THEORY 10

* Hawk: Initiate aggressive behaviour, not stopping until injured or until one’s opponent backs down.
* Dove: Retreat immediately if one’s opponent initiates aggressive behaviour.
  If we assume that

1. whenever two individuals both ini-tiate aggressive behaviour, conflict eventually results and the two indi-viduals are equally likely to be in-jured,
2. the cost of the conflict reduces indi-vidual fitness by some constant value C,
3. when a hawk meets a dove, the dove immediately retreats and the hawk obtains the resource, and
4. when two doves meet the resource is shared equally between them,
   the fitness payoffs for the Hawk-Dove game can be summarized according to the fol-lowing matrix:
   Hawk Dove Hawk 1
   $2(V$ − $C),$ 1 $2(V$ − $C) V,$ 0
   Dove $0, V V/2, V/2$
   One can readily confirm that, for the Hawk-Dove game, the strategy Dove is not evo-lutionarily stable because a pure popula-tion of Doves can be invaded by a Hawk mutant. If the value $V$ of the resource is greater than the cost $C$ of injury (so that it is worth risking injury in order to obtain the resource), then the strat-egy Hawk is evolutionarily stable. In the case where the value of the resource is less than the cost of injury, there is no ESS if individuals are restricted to following pure strategies, although there is an ESS if players may use mixed strategies.
   4.2.3 ESS of the Hawk-Dove Game
   Clearly, Dove is no stable strategy, since $V$ 2 = $E(D,D) < E(H,D)$ = $V$ , a popu-lation of doves can be invaded by hawks. Because of $E(H,H)$ = 1
   $2(V−C)$ and $E(D,H)$ = 0, $H$ is an ESS if $V > C.$ But what if $V < C?$ Neither $H$ nor $D$ is an ESS.
   But we could ask: What would hap-pen to a population of individuals which are able to play mixed strategies? Maybe there exists a mixed strategy which is evo-lutianary stable.
   Consider a population consisting of a species, which is able to play a mixed strategy $I,$ i.e. sometimes Hawk and some-times Dove with probabilities $p$ and 1− $p$ respectively.
   For a mixed ESS $I$ to exist the follow-ing must hold:
   $E(D, I)$ = $E(H, I)$ = $E(I, I)$
   Suppose that there exists an ESS in which $H$ and $D,$ which are played with positive probability, have different pay-offs. Then it is worthwile for the player to increase the weight given to the strat-egy with the higher payoff since this will increase expected utility.
   But this means that the original mixed strategy was not a best response and hence not part of an ESS, which is a contradic-tion. Therefore, it must be that in an ESS all strategies with positive probabil-ity yield the same payoff.
   Thus:
   $E(H, I)$ = $E(D, I)$
   $⇔ p E(H,H)$ + (1− $p)E(H,D)$ = $p E(D,H)$ + (1− $p)E(D,D)$
   $⇔ p 2(V$ − $C)$ + (1− $p)V$ = (1− $p)V$
   2
   $⇔ p$ = $V C$
   4 EVOLUTIONARY GAME THEORY 11
   Thus a mixed strategy with a proba-bility $V/C$ of playing Hawk and a proba-bility 1 − $V/C$ of playing Dove is evolu-tionary stable, i.e. that it can not be in-vaded by players playing one of the pure strategies Hawk or Dove.
   4.3 The Replicator Dynamics
   As mentioned before, the main difference of EGT to game theory is the investiga-tion of dynamic processes. In EGT, we are interested in the dynamics of a pop-ulation, i.e. how the population evolves over time.
   Let us consider now a population consist-ing of $n$ types, and let $xi(t)$ be the fre-quency of type $i.$ Then the state of the population is given by the vector $x(t)$ = $x1(t), . . . , xn(t).$
   We want now to postulate a law of motion for $x(t).$ If individuals meet ran-domly and then engage in a symmetric game with payoff matrix $A,$ then $(Ax)i$ is the expected payoff for an individual of type $i$ and $xT Ax$ is the average payoff in the population state x.
   The evolution of x over time is de-scribed by the replicator equation:
   $ẋi$ = $xi[(Ax)i$ − $xT Ax]$ (1)
   The replicator equation describes a se-lection process: more succesful strategies spread in the population.
   A derivation of the replicator equation is given in appendix A.4
   4.4 ESS and Replicator Dynam-ics
   We have seen, that $D$ is no ESS at all and for $V > C, H$ is an ESS. We have also seen, that for $V < C$ the ESS is a mixed ESS with a probability of $V/C$ for playing $H$ and with a probability of 1 − $V/C$ for playing $D.$
   By setting $ẋi$ = 0, we obtain the evo-lutionary stable states of a population.
   A population is said to be in an evo-lutionarily stable state if its genetic com-position is restored by selection after a disturbance, provided the disturbance is not too large.
   If this equation is applied to the Hawk-Dove game, the result will be the follow-ing:
   For $V > C,$ the only evolutionary sta-ble state is a population consisting of hawks. For $V < C,$ a mixed population with a fraction $V/C$ of hawks and a fraction 1− $V/C$ of doves is evolutionary stable.
   This result will be derived in appendix A.5.
   At this point, one may see little differ-ence between the two concepts of evolu-tionary game theory. We have confirmed that, for the Hawk-Dove game and for $V > C,$ the strategy Hawk is the only ESS. Since this state is also the only sta-ble equilibrium under the replicator dy-namics, the two notions fit together quite neatly: the only stable equilibrium under the replicator dynamics occurs when ev-eryone in the population follows the only ESS. In general, though, the relationship between ESSs and stable states of the repli-cator dynamics is more complex than this example suggests.
   If only two pure strategies exist, then given a (possibly mixed) evolutionarily sta-ble strategy, the corresponding state of the population is a stable state under the replicator dynamics. (If the evolutionar-ily stable strategy is a mixed strategy $S,$ the corresponding state of the population is the state in which the proportion of the population following the first strategy equals the probability assigned to the first strategy by $S,$ and the remainder follow the second strategy.)
   However, this can fail to be true if more than two pure strategies exist.
   5 APPLICATIONS 12
   The connection between ESSs and stable states under an evolutionary dynamical model is weakened further if we do not model the dynamics by the replicator dy-namics.
   In 5.1 we use a local interaction model in which each individual plays the Pris-oner’s Dilemma with his or her neighbors. Nowak and May, using a spatial model in which local interactions occur between in-dividuals occupying neighboring nodes on a square lattice, showed that stable pop-ulation states for the Prisoner’s Dilemma depend upon the specific form of the pay-off matrix.
   5 Applications
   5.1 Evolution of cooperation
   As mentioned before, the evolution of co-operation is a fundamental problem in bi-ology because unselfish, altruistic actions apparently contradict Darwinian selection.
   Nevertheless, cooperation is abundant in nature ranging from microbial interac-tions to human behavior. In particular, cooperation has given rise to major tran-sitions in the history of life. Game theory together with its extensions to an evolu-tionary context has become an invaluable tool to address the evolution of coopera-tion. The most prominent mechanisms of cooperation are direct and indirect reci-procity and spatial structure.
   The mechanisms of reciprocity can be investigated very well with the Ultima-tum game and also with the Public Good game.
   But the prime example to investigate spatially structured populations is the Pris-oner’s Dilemma.
   Investigations of spatially extended sys-tems have a long tradition in condensed matter physics. Among the most impor-tant features of spatially extended sys-tems are the emergence of phase transi-
   tions. Their analysis can be traced back to the Ising model. The application of methods developed in statistical mechan-ics to interactions in spatially structured populations has turned out to be very fruit-ful. Interesting parallels between non equi-librium phase transitions and spatial evo-lutionary game theory have added another dimension to the concept of universality classes.
   We have already seen, that the Nash equilibrium of PD is to defect. But to overcome this dilemma, we consider spa-tially structured populations where indi-viduals interact and compete only within a limited neighborhood. Such limited lo-cal interactions enable cooperators to form clusters and thus individuals along the boundary can outweigh their losses against defectors by gains from interactions within the cluster. Results for different popula-tion structures in the PD are discussed and related to condensed matter physics.
   This problem has been investigated by Martin Nowak (Nature, 359, pp. 826-829, 1992)
   I programmed this scenario based on the investigations of Nowak. The pro-gram is written in NetLogo, the program code is given in appendix B.
   5.2 Biodiversity
   One of the central aims of ecology is to identify mechanisms that maintain bio-diversity. Numerous theoretical models have shown that competing species can coexist if ecological processes such as dis-persal, movement, and interaction occur over small spatial scales. In particular, this may be the case for nontransitive com-munities, that is, those without strict com-petitive hierarchies. The classic non-transitive system involves a community of three com-peting species satisfying a relationship sim-ilar to the children’s game rock-paper-scissors,
   ![image](data:image/jpeg;base64,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)
   ![image](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAUDBAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIChALCAgOCQgIDRYQDhIRExMTCAsXGBYSGBASExIBBQUFCAcIDwkJDhIPEQ4SEhcSHhUWEhISHhcSFRITFRISFxISEhUWEhUVEhUWEhISHhUVEhISEh4SEhUSFRUSFf/AABEIAL4BNwMBIgACEQEDEQH/xAAdAAEAAgMBAQEBAAAAAAAAAAAABQYDBAcBAggJ/8QARBAAAgIBAwICBwMICAUFAQAAAQIDBAAFERIGIRMxBxQWIkFRlBVW1SMyNnF1gZG0JDNTVWHR0tNCVHKTo3OSoaKxJf/EABcBAQEBAQAAAAAAAAAAAAAAAAABAgP/xAAsEQEBAAIABAMGBwEAAAAAAAAAAQIRAxIhMRNRcQRBgZGx8DJSYaHB0eEi/9oADAMBAAIRAxEAPwD9l4xjAYyqdEdeUNYm1GGmZeel3Go2vGjEY8dWkUiI8j4i7xt37fDLXgMZAa71jplGcVrd2GCwYlnELk+J4Lu8aycVBIQvHIP1oc3dE1urdExqyiUQSRxSkK6hXmqVr0YBdQHBrXK77ruPym2+4YAJLGM16V2KYOYpFkEcskMnE78ZYzxkjPyYHtgbGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwP589Z9NX5L+vrFpeuvem6jkm0uevDYWmFFq74rsBHsZD4lcq6sD/AIqAQ3760SOZa1dbDcp1giWZt9+UwjUSNv8AHdwx/fm5jA5lqekXpurLMla3NRj9ndNQzLVhnSV11LVmMXKdCodQynYd9pBv8MqXWkkwuahW31ExWOqYEsz0pr1eNRH0loZUW/sqB7To8nHikbRAuBuwA2PeOQ32377b7fHttv2+XcfxzxJFJIDAlexAIJB+RA8j2+OB+WdYtaqsGnSPd6jksVNPeAU0h1urNPbr6nPGJIbkKTRSX2jWFTHehljMexLbMWHQemk1GLWxJdWddJm1fVkpR1jYjEOoO/OOXVVTtYglQzpHufCRkTcM0ilO0YwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwGMYwOfHTI6/UdiY2bQFjRLLyNLZd0rKtyDvWSQlKyAEnsNvdG++2Vr0MdP0PtCPVNMijp0vskVE5TqdR1vlLDKuq6nXj2EcgCEhpPyzm3JzCbKudheBGJLIrEqUJKgkofNCSO6n5Zhq6bXiblFXhibbblHFGjbHbcbqN9uw/hgQVTX7w1ddNtUqsUM9XULlSzXvy2JHjoWtPg42K0lGJYHddRjb3JJQCjDc9mNoypap+kuk/sPqH+f6Yy24DGMYDPMr2kdZ6bbtz0a9nnareL48ZimQIIJBDL+UdAjbSMB2J8+2+TEt+Bfzpol+W8iDf+JySxzw4uGc3jZfStnGQ1nqnTYhyk1Ckg323e1Ao37nbcvtvsD/A58x9V6a68o7teQH83wpVl5HfYhfDJ5dwfL5H5Yth4uHnE3jOe9H+l3SdSnesnrNeZYmnVJ4f6yJHjjkZGgZ1HFpYQQxUnxBtvs21r9pKX9t/45f8ARk5pWOF7TwuLjz4ZSypjPMiPaWl/bf8Ajl/0ZG9S9dUKNWW07SSrFw3SKM8zzkWMcfF4p2Lg92HYH9WXmnm1nx+Hhjcsspqd1pxlS6X6/o6hWWzEl2NWZl4yUbW+6HYlXijaKVfLvGzAHkDsysBunq6oDt4eok+XbSNV2Py2b1XYjEylTH2jh5YzKZTV7LAcZDe0MZ8q94n4D1Kwv/2dAB+85XetOurlLwPVNEv3vE8TxNklj8Lhw4/1cMm/Lk3nt+Z8fhLlInF9p4fDx5sr0nlLfptfMZXdM6pSaCGZqWp1/Ghjl8GejKJo/EUP4cyRhhHKu+xBPYg59xdV1GO3C8uwP9ZpepRr2IHZ3rBSf8Afn8su434uHnE9jIf2mpbbtPw/9VJYtv8Aq8RBxP69sqt70vaRBqP2fK0y+/FH64ER6YaZEZC0iSF1QGRVLFeKncsQoLCc083Pie1cLh658pN3U9a6HjK77caN/eun/WVv9zHtxo3966f9ZW/3Mrfj8P8ANPmsOMr3txo3966f9bW/3MrOn+mXRZLxovM9cmSaKKzP4S053hDsRHYSRgqtHFI6s/EEKBvuyqVsjnl7XwcbJcpu9nR89yFr9U6bIvKO/TdfLktqBhv8tw+2+ZfaKh/ztT6iL/VjcdpxMb74lMHNP7Vq/wDMQ/8AdT/PIjpXrjSdUdoqN6CaZEMjV9zHZESlFM3q0oWUwBpEXmF48jtvv2xuHi4c0x3N3t59FkxjGVsxjGAxjGAxjGAxnHvScJI70EMk2qXDNYomXwdasaJBSr6jqtbS6wrwaYFkuyLLMrHxWOwQnmOSrls9EM8ligloz3jHKZIvU780duWlYpzzVLUSXlUSWovFhbZpCxIAO45bANyLq7fVLGnyU7EEVelLcNufw1jmWKZYmFdUdmZACWJbj5r2PfaI6G67uXZ6C3NOjpwavp8mpaZLFbey/gx+rOYb0ZrxrWtGG3E4CNIvuyDf3e9jvaD4182nceE2mz0HjG4Y+PNHIXDeQHFCP35XOiejdQqzaWbluvNX0XTZdNpiBJVls+IKka27hkYhZVhqBeK8gWmkO47DAk9U/STSf2H1D/P9MZbcoH2PDW6ppSxvaZrWj9QySixevW4lb7R6cbavDameOmm8je5CqLsFG2yqBdNSvxVo2lnkWONdt2Y7DckBVHxLFiAANySQBuThLZOtbWQFnV5bLtX08K3AlJ7jgtXgYHYogBHrM4PYqpAXY8mBHE6Oo2nsRma6507TQQPCkcRWbXI8VEzA7142JAES/lG3AYr3jzJUsWrCLFQgGn1FAVLE8PFzGAuwrUexjGxI3m48Sv8AVuDmLkYcLPizc/5x870+X3v9EVQ9HHTzXGmaCK5qFaXx52mnaV1sWY5fytioH8FWdJpGAMYUbgqBxBFth0Smm/CpWXfz4wxjfbfbfZe/mf4nOZaJ6B6NTV5Nbi1HUhfkluT+KV007TXfE8WQb0uzflX8tt9yDuCym/BdUr/8Ve/HuPMGpYVQO55KHimkJ27bRDv/AIYnT3NYex8HGa4fLPhr/Pmm4oEX81FXtsOKgdvl2HlmUgZXk6srp7txJtPf4+tpwi7nYD1uMtWJJ+Ak37jtk7DKrqGVgysAQVIIIPlsR5jLLKuXCyw7z+mlo+h0qfP1SpXreJx8T1eCOHnw5cefhqOW3Jtt/Lkckds9xmnPHCYzUmo82zV1KjBZjaGxDHPE+3KKVFkjbiwZeSOCDswB7/EDNrGCyWarV02jDWiWGvDHBEm/GKJFjjXkxZuKIABuxJ7DzJ+ebWwxjBMZJqPcbYxhoxsMYwPNsiLfTOnSzi1LQpy2Q8UonkrQvMJIShhkEjKWEiGOMqd914LttsMmM8wzlhjl3m9Gw+QxxHyGe4wunzsPlkdS0KlBNJZhqVorEvLxJ44Iklk8Rg785FXk/JwGO57kA5JYwlwxveToxvAjdyik/MqD/wDueeqx/wBmn/sX/LM2Mml1GkdLrf8ALwf9pP8ALIjpXofSdLdpaNGCGZ0MbWNjLZMTFGMPrMpaUQFo0bgG48hvtv3yx4xqM+HjzTLU3O3xe4xjK2YxjAYxjAYxjA5P6YH02TU6cGsPptOmun2pq1++DG5v+NCYoYLRdI0EZijnMZblIVi2HuEi0ehu1JNoentJXr1SI5IkjqRPDVaGCeWGvYrwuOUUM0Mcc6qe4EwHfIj0kJO2pVFk+3H0/wBTmLR6RCxjW34q8JLUsY8Rt4wwVVOw2JP53a49JSxvTgaNrTJswBuFza3WR1YTmQ8uYYEd/kMCWxny57H4nb9X/wA/DOQehX0pXdb1CapYGmFUqS2ZI6RsibT5o7z1FqTSTkx6iGVGbxq/FQU222dGIc99MPVOu1+sS1O1KK1WJKcUEVjSq8wjvQU5rKxTalQevCr2IarkzmQ/0cgOgcKnZaBt3JFnjRZ5QTwuWUkjoVNwy76fTbaW2/kDK5QOHJVwPcHOOu/R/pWvdWcZ5NVSGSlbtajXlqahVrTyaPY0unGtWW1CqWIZIrTcmqlhvDCwILhm75p1uKxDFPA6ywzRpLFIh3SSORQ6Op+KlSD+/MXG3u5+z4ZY7vFszu7cfdJPdue+zz7fojdN6eijkFid3t2hvtYn4kxg+awRqBHAu3b3FBOw3LeeTWMZqSTs7Z8TLO7r3GMZWXwyg+e2QVrpet7z1g9SY8mDVJWrK0hH50kaAxSNvt3kR/1ZP57kslbw4mWPauM+i3ReuNOnnl1m/X1aq8bkU0ljEvrEsglknhnanHwVeBRYSyx7Tnbh4ahulU+pqzOsMpepYY8VgtKYXd9tysTH8nYIH9kzjz75N5gu1Ip0aKaNJY3GzxyIrowPmGVhsR+vJqzs34mOX4sfl0/z6erODjK8enHh3On2panmRDJvaqb8QqjwJWDxRjYe7C8YPf5nIvqvrOxo1Oxc1HT5ZoKyhml06SGXkpdIwWitPE0bkvvxBcbKdmJIBc3meDMvwXf7X79NrrjK16Our4dbopfggnrxSOyoth6byMFA5PtTsSrHs5ZCshWQNG26r23s2acrjZdUxjGEMYxgMYxgMYxgMYxgMYxgMYxgMYxgMYxgMYxgMYxgfn708fZN7UopJbmjTyU6s0MdLVJZ1VblS9XtTKsQjaJ4pYIp4JHI5IrKRvudunehOLhoOnAepcPDlaIaexemkD2ZngjhkZVMvCJo1LkDmys3xyC9J+uy6fq1SSnMstyXT54zQOl6pqbCuJ4mNuM6WjyVh4pVG5qRJxj7qU3y1+jKqYdKqIzzSMwmldp6s9Fw9ixLO6LTsgS1YUaQoiP3VEQd9t8CftwLLG8bb8ZEZG2Ox4uCp2PwOxOUbov0dtQtUrE11bS6Xp76ZpyJRhqSJVfwARbmjdvWpAK6AcViQcnPAk75f8+QR3G/l2P+Hbcb/LsRgVTVf0k0n9h9Q/z/AExmx6PqU1WvNTlRlSrctR1WIAWSlJIbFXgQSCsccwg+B3rnt3zX1T9JdJ/YfUP8/wBMZua7qU1bUNMXl/RLjWakicAeNrwTaqyeIO6Lwr2YyPImSP4jvrHd6ffQqw4xjMhjGMBjGMBjGMBmlq+mVrkL1rleC3Xk4+JXswxzwycHWROcUoKNs6qw3HYqD8M3cYFXh6IoVh//AC4ItIk5cuWmww1o3bsD49dE8GxuABu6kgeRU98+hrdinsupxgRjz1CsrGqdgN2niJaSmPzjuxeMBe8g3Ayy54Rv55m4+Ttjxums5ufv8L/fT9GOvMkiq6MrowDKykMrA9wQQdiNszZXbHTvhM0unS+pyMSzxcfEpzMSSTJW3ARiWJ5RFGJ25FgNsqnpB9JVrRkq+safVV7FmKqXtahPWql5pIkWSCzDQnUxorTSyCbwXWOs5VZNuzm81vB5uuF39fv0dNxmCk0pijMyJHMUQyxxSNNEkhUGRI5XjQyoG3AYohIAPFfLM+acDGMYDGMYDGMYDGMYDGMYDGMYDGMYDGMYDGMYHO/SZoupzXK9nTpNUiaOq8Ltp82jRK4eVXKyrqcDtIwKKQR2XdttuTb2H0b3ns6XUlklnlkKyLK9l6r2PFimkikSdqSrAZUdGQ+GNgUOUn0u6J9qajWqxTVa0iU5Zms2b2rRq6RzKrV4qmmajVEjqzgu8jEqsiAA8t1tvoj8L7GpLBUgpRIs0aQVW5Vto7M0ZnrPvu0ExUzqSSxWcb7nfAsWqPIsEzRDeURSGMbb7yBCUG3x97bOH+gqKGK7o9lUoPY1jp957EtWWx9oCSF6kk8ust4xh1Cd552BlaOJ45BIg5AnbvWadLS60DySQ14IZJTvLJFDHG8h3J3kZAC53JPffzOBTfBvL1TRNqxVmhbR+oTUjr05q0sEX2j04eNiWS5Ktp+JiHJEiG6MePvALa+o6teWDlZVmjrSR3AU580kqOLEboI/eYhox7o/OBIIIJGQuq/pJpP7D6h/n+mMthG+JRgo2o5oo5omDxSxpLG6+TxyKHRhv8CCD+/NjK76P9Omp0lpzIFFSaxXrEEEPRSZzRI2JIIrGJDvsd42/wAMsWXKSXoQxjGQMYxgMYxgMYxgMYxgeZRvS36M6fUsdeG5Zu10rNKyimai8zKEBMjWa0rAAIR7hXcSOG5Aja9bZ5ks2uOVxu4h+jobEVGvBa5NPXjFd5H4b2PA/JLZ2i91fFVRJsAOPibbDbbJjIHVb0tfUKYZz6rbWSsV2BEdpAZ4WBA3AeNLCnc7bpEB3PeeyS+7yb4uN3zfm6vcYxmnMxjGAxjGAxjGAxjGAxjGAxjGAxjGAxjGBwf01aLVraikkei6KteSu169cl6br6lNO7ajXjvSNLsAJIas8to78nk4Ptud86J6EZFfQdPZDuhWfgwpxUI5EFqcJJBThRVgquoDRrty8No+RZizHHrvS1RJHMWs6jpDTSGd462oRLG7E++Y6+oRzRwKzAk+CqAkk+ZJya6T0mpAJJa9iW5JKQs1qe29yVym5VOTMUiQcieEYVRyJ279wnsgtJ6or2tQu6fCJGkoRwNPNxHgGSdpVMEb77vLH4XvbDZTIBuSGCy9uNnjkRHMTsjKsihWMbMpCuqsCCQSDsQR2yl9DdG2dMt7+t+PUWhDXHOGNJpZls255ZZnXu8rPOZGc93aVycDd1X9JdJ/YfUP8/0xltygfYVGp1TSmq06taa5o/UEtuWvXihltSjUenH8SxJGoad+Ush3fc7yN8zl/wACv6pqU0GqUImYeqXorMABCgpehUWYuJ23Ieslvcbnb1ddvM72DIvqMVUhNm2u8VEm7zCyM0JgVy0yiL3yRGZBsAdwWGx32yRicMoZSCrAFSO4II3BB+I2IzV7RH3jGMypjGMBjGMBjGMBjGMBjGMDWvV45F2kjEgRkkUEAkPGwkRl38mDKCD8wM+dKvR2YY54iTHIu67qVYfAqysN0cEEEEbggg+WbRyH0XTXrT2wvH1Wd1sRJueUc8nL1pQu2wjZgsnmSXll8u2+b3dMdXG7vWdv5+P9JnGMZpzMYxgMYxgMYxgMYxgMYxgMYxgMYxgMYxgcj9NduvSv07k1LS9UeSpNVjoXlnNiNTPE0tquK2n22MHvRrIWRVXZNmHJgd30JdKtT53Uk041LVGnHAumJtFKUmtzmR24KJFijsxVUYjmyVQX2J2Fj6p0DUHuR39LuVa1j1f1SdL1OS5BJAJTKjIIbEMkcqsz/wDEVYNsR2BH36K6SV9LhiR3lK2NQM0rosZltPqNqS5KsSFhFG9lpmVQTxVlHwwLTjMc/Pi3h8efFuAckJy2PEMQCQu+3kM5l6OLuqtqphl1U6vUTT2+05RWgSlT1pZoh6tp1qCFDNHxayDG3NoxDHybkxGBZNV/SXSf2H1D/P8ATGW3KD9ozTdU0o5KFuosGj9QpFNYei0dxftHpweLXFW1LIqbIrfllibaVe24YLfsDHNGrqyMAyupVlPcMpBBBHxBBP8AHIbobT56lCvUsEM9VWrI4cv4leF2jqyMxAPiGuIi247Ny8/MzmV2LUJotZkqSyBoLVFbVNCNiklWXwbygge8pWxSYA9wWk/drHdlnxSrHjGMypjGMBjGMBjGMBjGMBjGMDzIfq6vO9YvVLes13SxEqtx8UxHd4D324yx84+/YeID8BkznmSzbWGXLlL5NXSrsdmCKeJuUc0aSI2226uoI3B7g7HNrIqtqQ9cmpNH4ZSKOxEwI2mR2dZNhsNmSRRv59pYz8clsSrxMdX16z4mMYysGMYwGMYwGMYwGMYwGMYwGMYwGMYwKzc6PSWSSQ6hq6GR3fhHqNhI05sW4xoDsiDfYAeQAyX0DSoqVeOtCZDHGZGDSuZJGaWR5ZGeRu7MXkY7n55v4wMVmISI8ZLKHRkLISrgMCCVYd1Yb+Y/wyvdG9GVtJWKOrPeMEMArw1prcs1eONeIUJE52DAKBv59z88s2QuhdVabellgp36tqaDcyxwTJI6KJGiL7KdyglRk3G45KRvuNsCM1X9JdJ/YfUP8/0xltypar+kuk/sPqH+f6Yy24DIrqS1WqQtqFmPktJJJTKEDyQxkATyLudwgj3Ztvgh7HYDJXMF6sk0UkMiho5UaN1PkyOpVgfmCCR+/EvUZVII3Hkfj+vyz6yI6Poz1aFWtZdZZq0KQNKpJEohHhpKxIBDvGqsR8GZh323yXxZqhjGMBjGMBjGMBjGMBjGMBjGMCM1HTEksVrfLw5KvigMAuzwzKBLE5I3CFkiftt3hT4AgyIO/lnjqCCCAQQQQfIgjY7j5ZAdDxyQwyUpFceozNXhdlYLLV2WSqyMxPicYXSInf8APhk8sz2vq69csN7/AA6+V3/P1WLGMZpyMYxgMYxgMYxgMYxgMYxgMYxgMYxgMYxgauqxO8E6RnaR4ZVjO+2zsjBTv8PeIzkvou2lm6Xiip2YJNI6esVdRMsFiBasrLpkBpO0iKliV7FSV+2/aAt5ON+yYwOd610ZqU2t1bketarFXWjq6GSNNB/obWrekSwUoEm01mkgdK8x5SCVx6lH+UXk3iS/snf+8+ufT9Nfguc49LVerJP1VPa4faGnaPTm0J2f+k1ZWhtvDNp6lt4pX1CNUJjALmNFO42B7fWLFEL/AJxVeX/UQOXb4d98Cr+yV/7z659P01+C49kr/wB59c+n6a/BctuMDnZ6R1mPUI1j6j1tqM1e3NamdOnmkiuxvp8dOKFH0raOGSE3WIROPKAElS55y56Sv/efXPp+mvwXOfdUw2KV7raSpNaks+ydSxA8krzSxS769xFbf+rClAyqo25EnuWO896OaemVdX8HRxAlabQatq1HUZTA8xsFaluQISGsyRGxvId2dYl3J4jAsfslf+8+ufT9NfguPZK/959c+n6a/BctuY52AViW4AKSX3A4jY7tuew28+/ywKLq3TOtLNRFbqLWJIZLbpfd4Omg0FQUbkiSxA6Qu7m6lKPsH92Z+w25LI+yd/7z659P01+C5xhdHpRUtR1bSJZalSHp63VsXhZ31LXt2hkfWLEMRLIY41suJnUSubJICqq8uj+junSqa/qdTSErw6Yuj6NO8NPiKyXZZ9UXxFWP3Flkqx12YjuwWMnffchYPZK/959c+n6a/BceyV/7z659P01+C5bcYFB1bpnWlmoit1FrEkMlt0vu8HTQaCoKNyRJYgdIXdzdSlH2D+7M/YbclkfZO/8AefXPp+mvwXOX6xRqxazp2rabLFNLJqur0rMrStHrU+oyi9CKMsZRRLpFcwxgRkcgkcTglVJfb9DsNGOfpaamyC9qPTtmxrBhIL3JVXTGks6iV7yWY7ssyK0h5AyzL8CAHRfZK/8AefXPp+mvwXHslf8AvPrn0/TX4LltxgUHVumdaWaiK3UWsSQyW3S+7wdNBoKgo3JEliB0hd3N1KUfYP7sz9htyWR9k7/3n1z6fpr8FzjXVGt6g9/UL5r6rW1Kx0j1OtaF680SUYoJNNkprAewMoCSO8g3JmsRruQIwOhejelptXV/B0fwEqzaFUtWoqjAwPM07LVtyBCVazLELG7n3nEQ3J4jAsfslf8AvPrn0/TX4Lnnslf+8+ufT9NfguW7GBQdW6Z1pZqIrdRaxJDJbdL7vB00GgqCjckSWIHSF3c3UpR9g/uzP2G3JZH2Tv8A3n1z6fpr8FznXV1SGLWrWsP9g6i9fWNHqLUsVJJdYql1oQxx1LJkAgnSWVragROH8Q+8u3IYejoKq2OnbkPhjWruva1Dq8sZBtTwpX1o2YLh3LtBDPBSCq/aPhFxA7YHS/ZK/wDefXPp+mvwXHslf+8+ufT9NfguW3GBQOoemdaSFDS6i1iaY26KOkkHTQUVJL1eO/KCdIX346TWZF7n3o17P+a0l7J3/vPrn0/TX4LnK7iqNZm1SxDRms1uq6+nLvLaXWfCnapXqCrJHKqw1EgsmVqxR0lXxXJUsc2fRbFAkvSVmt4J1TUa+oHqCUFfXLPCnJJae4FIaR4tUFeP39/D5lRsDtgdL9kr/wB59c+n6a/BceyV/wC8+ufT9NfguW3GBRtU6e1iAQS1dd1W463tO8WtZh6fWGSk2oVl1Hm0WlxSDjRayw4OrbqNtzsDec5b6WOk9L1XU9MoT6fTltXRLYt3JK0b2o9K00xGSKKZkJjaWxZqw7ggqk0xUhgpFYkgrCd7vGFNeXravRSRGU3Rpw1GCEVATu61G0UtKY+ybMX2374HecYxgMYxgMYxgMYxgMYxgR+oaNTsSwzWKlaeau3KvLNBFLLAx3HKGR1LRNsSN128zkhjGAxjGBhWtGHaQRoJHVUeQKodkQkojNtuVBZiAfLkfmc1tI0epTDipVrVRI/iSCtBFAJHO+7uI1AZjue5+eb+MBnw6BgVIBDAgggEEHsQQexBGfeMCLodP0K7F4KNOF2UozRVoY2ZG23QsiAlTsO3l2GZtH0ipSQx06tepGztI0daGOBGkc7s5WJQC5Pck9zm9jAYxjAj00Wmtlrq1KwuOoR7YgiFlkG4CNOF5lAGbsTt3ONO0anWkmmr1K0EtludiWGCKKSd/LnM8ahpW7ebE+WSGMBjGMDE0CFxIUQyKjRiQqC4RyrOgbbcISiEjyJRfkM1dI0epTDipVrVRI/iSCtBFAJHO+7uI1AZjue5+eb+MBjGMCPm0Wm9lLj1KzXI1KR2mgiayiHbdEnK81U7DsDt2xX0anHYktx1ayWplCy2UgiWxKqkkLJMq83UEnsSfM5IYwGMYwNB9HqNYW41WubarwW0YIjYVDsConK8wuwHYH4YpaNUhmlsQ1a0NifvPPFBFHNN3B/KyqoaTuB+cT5DN/GAxjGBh9XjMgl8NPFCGMS8R4gjZgzRh9twhZVO3luo+Wax0eobIuGrWNwLwFrwIvWQhGxQT8fECbADbf4Zv4wGMYwGMYwP/9k=)
   5 APPLICATIONS 13
   where rock crushes scissors, scissors cuts paper, and paper covers rock. Such rela-tionships have been demonstrated in sev-eral natural systems. Some models pre-dict that local interaction and dispersal are sufficient to ensure coexistence of all three species in such a community, whereas diversity is lost when ecological processes occur over larger scales. Kerr et al., tested these predictions empirically using a non-transitive model community containing three populations of Escherichia coli. They found that diversity is rapidly lost in our experi-mental community when dispersal and in-teraction occur over relatively large spa-tial scales, whereas all populations coexist when ecological processes are localized.
   There exist three strains of Escherichia coli bacteria:

* Type A releases toxic colicin and produces, for its own protection, an immunity protein.
* Type B produces the immunity pro-tein only.
* Type C produces neither toxin nor immunity.
  The production of the toxic colicin and the immunity protein causes some higher costs. Thus the strain which produces the toxin colicin is superior to the strain which has no immunity protein (A beats C).
  The one with no immunity protein is superior to the strain with immunity pro-tein, since it has lower costs to reproduce (C beats B)
  The same holds for the strain with im-munity protein but no production of the colicin compared to the strain which pro-duces colicin (B beats A).
  In figure 2, one can see, that on a static plate, which is an environment in which dispersal and interaction are pri-marily local, the three strain coexist.
  Figure 2: Escherichia coli on a static plate
  green: resistant strain red: colicin producing strain blue: sensitive strain
  Figure 3: Escherichia coli in a flask
  In figure 3, where the strains are held in a flask, a well-mixed environment in which dispersal and interaction are not exclusively local, only the strain, which produces the immunity protein only will survive.
  A MATHEMATICAL DERIVATION 14
  A Mathematical Derivation
  A.1 Normal form games
  A game in normal form consists of:

1. A (finite) number of players $M$ = ${a1, . . . , an}$
2. A strategy set $Si$ assigned to each player $i ∈ M$ . The combination of all sets of strate-gies $S$ =
   $∏ i∈M Si$ is called strategy
   space.
3. A utility/payoff function $ui$ : $S 7→$ R, assigned to each player $i ∈ M$ . $⇒ ∀s ∈ S$ : $ui(s) ∈$ R
   A.2 Nash equilibrium and best answer
   Notations:
4. $s ∈ S$ = $∏$
   $i∈M Si$ ; $s$ = $(s1, . . . , sM$ ) ; $si ∈ Si$
5. $s−i$ := $(s1, . . . , si−1, si+1, . . . , sM$ ) ; $(si, s−i)$ := $s$ ; $(s−i, si)$ := $s$
6. $S−i$ = $∏$
   $j∈M, j 6=i Sj$ ; $Si$ × $S−i$ = $S$ ; $(si, s−i) ∈ Si$ × $S−i$
   Definition:
   A combination of strategies $s∗ ∈ S$ is called a Nash equilibrium iff:
   $∀i ∈ M ∀si ∈ Si$ : $ui(s∗)$ = $ui(s∗i , s$
   ∗ $−i) ≥ ui(si, s$
   ∗ $−i)$
   Definition:
   A strategy $ŝi ∈ Si$ is called best answer to a combination of strategies $s−i ∈ S−i$
   iff:
   $∀si ∈ Si$ : $ui(ŝi, s−i) ≥ ui(si, s−i) ⇔ ui(ŝi, s−i)$ = $max{ui(si, s−i)$ ; $si ∈ Si}$
   It is now easy to see, that, if every player chooses his best answer, this will
   constitute a Nash equilibrium, since an-other strategy will not lead to an increase of the payoff, since the best answer al-ready leads to the maximum payoff.
   A.3 Evolutionary stable strate-gies (ESS)
   In order for a strategy to be evolutionar-ily stable, it must have the property that if almost every member of the population follows it, no mutant (that is, an individ-ual who adopts a novel strategy) can suc-cessfully invade. This idea can be given a precise characterization as follows: Let $E(s1, s2)$ denote the payoff (measured in Darwinian fitness) for an individual fol-lowing strategy $s1$ against an opponent following strategy $s2,$ and let $W (s)$ denote the total fitness of an individual follow-ing strategy $s;$ furthermore, suppose that each individual in the population has an initial fitness of $W0.$
   We consider now a population consist-ing mainly of individulas following strat-egy $σ$ which shall be an ESS with a small frequency $p$ of some mutants playing $µ.$ Then if each indivudal engages in one con-test
   $W (σ)$ = $W0$ + (1− $p)E(σ, σ)$ + $pE(σ, µ), W (µ)$ = $W0$ + (1− $p)E(µ, σ)$ + $pE(µ, µ).$
   Since $σ$ is evolutionarily stable, the fitness of an individual following $σ$ must be greater than the fitness of an individ-ual following $µ$ (otherwise the mutant fol-lowing $µ$ would be able to invade), and so $W (σ) > W (µ).$ Now, as $p$ is very close to 0, this requires either that
   $E(σ, σ) > E(µ, σ)$
   or that
   $E(σ, σ)$ = $E(µ, σ)$ and $E(σ, µ) > E(µ, µ).$
   A MATHEMATICAL DERIVATION 15
   A.4 Replicator equation
   The fitness of a population is given by $(Ax)i$ and the total fitness of the entire population is given by $xT Ax.$ Thus, the relative fitness of a population is given by
   $(Ax)i$
   $xT Ax$
   Let us assume that the proportion of the population following the strategies in the next generation is related to the propor-tion of the population following the strate-gies current generation according to the rule:
   $xi(t$ + $∆t)$ = $xi(t) (Ax)i$
   $xT Ax ∆t$
   for $xT Ax$ 6= 0. Thus
   $xi(t+∆t)−xi(t)$ = $xi(t) (Ax)i$ − $xT Ax$
   $xT Ax ∆t$
   This yields the differential equation for $∆t →$ 0:
   $ẋi$ = $xi[(Ax)i$ − $xT Ax]$
   $xT Ax$ (2)
   for $i$ = $1, . . . , n$ with $ẋi$ denoting the deriva-tive of $xi$ after time.
   The simplified equation
   $ẋi$ = $xi[(Ax)i$ − $xT Ax]$ (3)
   has the same trajectories than (2), since every solution $x(t)$ of (2) delivers accord-ing to the time transformation
   $t(s)$ = $∫ s$
   $so$
   $x(t)T Ax(t)dt$
   a solution $y(s)$ := $x(t(s))$ of (3). Equation (3) is called the replicator
   equation.
   A.5 Evolutionary stable state of the Hawk-Dove game
   We want to show, that the replicator dy-namics and ESS yield to the same result
   for the Hawk-Dove game.
   The replicator equation is given by
   $ẋi$ = $xi[(Ax)i$ − $xT Ax)]$
   Let us denote the population of hawks $x1$
   with $p,$ thus the population of doves $x2$
   will be denoted with $1−p.$ The first term $Ax$ gives( $p$
   $2(V$ − $C)$ + $V$ (1− $p) V$ 2 (1− $p)$
   ) Since Hawk is denoted with $x1,$ we will use the first component of the vector $Ax.$
   The second term $xT Ax$ delivers
   $p2$
   2 $(V$ − $C)$ + $p V$ (1− $p)$ +
   $V$
   2 (1− $p)2$
   Thus:
   $ṗ$ = $p [p 2(V$ − $C)$ + $V$ (1− $p)− p2$
   2 $(V$ − $C) −p V$ (1− $p)− V$
   2 (1− $p)2]$
   = $p [C$ 2 $p2$ − 1
   $2(V$ + $C)p$ + $V$ 2 ]
   = $p [p2$ − $V +C C p$ + $V$
   $C$ ]
   In order to be a population evolutionary stable we set the changes of the popula-tion per time to zero, so that there is no change in time. This gives:
   $ṗ$ = 0
   $⇒ p [p2$ − $V +C C p$ + $V$
   $C$ ] = 0
   This is certainly true for $p$ = 0. This is the trivial solution. Two other solutions can be obtained by evaluating the term in the brackets:
   $p2$ − $V$ + $C$
   $C p$ +
   $V$
   $C$ = 0
   This gives
   $p1/2$ = $V +C 2C$ ±
   $√ V 2+2V C+C2$
   $4C2$ − $V C$
   = $V +C 2C$ ±
   $√ V 2−2V C+C2$
   $4C2$
   = $V +C 2C$ ± $V−C$
   $2C$
   A MATHEMATICAL DERIVATION 16
   Thus: $p1$ = $1, p2$ =
   $V$
   $C$
   $p1$ = 1 is another trivial solution, thus the only relevant result is $p2$ = $V$
   $C$ .
   B POGRAM CODE 17
   B Pogram Code
   B.1 Spatial PD
   globals [movie\_on?]
   patches-own [num\_D z z\_prev score d score\_h neighbor\_h]
   to setup
   ca
   ;;1/3 will be defectors (z=1, red); 2/3 cooperators (z=0; blue)
   ask patches [ifelse ((random 3) < 1) [set pcolor red set z 1][set pcolor blue set z 0]]
   ;;d=delta\*(2.0\*(random(1.0)-1.0))
   ask patches [set d delta \* (2.0 \* (random-float 1.0) - 1.0)]
   set movie\_on? false
   end
   to single-D
   ca
   ask patches [set pcolor blue set z 0]
   ask patches [set d delta \* (2.0 \* (random-float 1.0) - 1.0)]
   ask patch 0 0 [set pcolor red set z 1]
   set movie\_on? false
   end
   to go
   play-game
   update
   if (movie\_on?) [movie-grab-view]
   end
   to play-game
   ask patches [set z\_prev z]
   ask patches
   [
   ; num\_D = number of neighbors that are defectors
   set num\_D nsum z
   ifelse z = 1
   [
   ; if patch is defector: score is T times number of cooperators (8-num\_D)
   set score (T \* (8 - num\_D)) + (P \* (num\_D + 1))
   ]
   [
   ; if patch is cooperator: score is 1=R times number of cooperators (+1=itself)
   set score (R \* (9 - num\_D)) + (S \* num\_D)
   ]
   ]
   end
   to update
   ; find the neighbor with the highest payoff
   ask patches
   [
   ; neighbor\_h = the neighbor with the highest score
   set neighbor\_h max-one-of neighbors [score]
   ; score\_h = highest score
   set score\_h score-of neighbor\_h
   ifelse (score\_h >= score + d)
   [
   ; if highest score > own score (+d)
   ifelse z\_prev = 1
   [
   ; if this patch is defector:
   ; if neighbor with highest score is cooperator: set patch to cooperator (z=0, green)
   ; else: stay defector
   ifelse (z\_prev-of neighbor\_h) = 0 [set pcolor green set z 0][set pcolor red]
   B POGRAM CODE 18
   ]
   [
   ; if this patch is cooperator:
   ; if neighbor with highest score is defector: set patch to defector (z=1, yellow)
   ; else: stay cooperator
   ifelse (z\_prev-of neighbor\_h) = 1 [set pcolor yellow set z 1][set pcolor blue]
   ]
   set d delta \* (2.0 \* (random-float 1.0) - 1.0)
   ]
   [
   ; if own score is the highest:
   ; if cooperator: set color blue, otherwise red
   ifelse z = 0 [set pcolor blue][set pcolor red]
   ]
   ]
   end
   to perturb
   if mouse-down?
   [
   ask patch-at mouse-xcor mouse-ycor [set z 1 - z ifelse z = 0 [set pcolor blue][set pcolor red]]
   ;need to wait for a while; otherwise the procedure is run a few times after a mouse click
   wait 0.5
   ]
   end
   to movie\_start
   movie-start "out.mov"
   set movie\_on? true
   end
   to movie\_stop
   movie-close
   set movie\_on? false
   end
   B POGRAM CODE 19
   B.2 Hawk-Dove game
   breed [hawks hawk]
   breed [doves dove]
   globals [deltaD deltaH p total counter decrement reproduce\_limit]
   turtles-own [energy]
   to setup
   ca
   set-default-shape hawks "hawk"
   set-default-shape doves "butterfly"
   createH n\_hawks
   createD n\_doves
   ask turtles [set energy random-float 10.0]
   set reproduce\_limit 11.0
   set decrement 0.05
   end
   to go
   ask turtles
   [
   move
   fight
   reproduce
   ]
   while [count turtles > 600]
   [ask one-of turtles[die]]
   do-plot
   end
   to createH [num\_hawks]
   create-custom-hawks num\_hawks
   [
   set color red
   set size 1.0
   setxy random-xcor random-ycor
   ]
   end
   to createD [num\_doves]
   create-custom-doves num\_doves
   [
   set color white
   set size 1.0
   setxy random-xcor random-ycor
   ]
   end
   to fight
   ifelse (is-hawk? self)
   [
   if ((count other-hawks-here = 1) and (count other-doves-here = 0))
   [set energy (energy + 0.5 \* (V - C))]
   if ((count other-hawks-here = 0) and (count other-doves-here = 1))
   [set energy (energy + V)]
   ]
   [
   if ((count other-hawks-here = 0) and (count other-doves-here = 1))
   B POGRAM CODE 20
   [set energy (energy + V / 2)]
   ]
   ;set pcolor-of patch-here black
   end
   to move ;; turtle procedure
   rt random-float 50 - random-float 50
   fd 1
   set energy (energy - decrement)
   end
   to reproduce
   if energy > reproduce\_limit
   [
   set energy (energy / 2)
   hatch 1 [rt random 360 fd 1]
   ]
   if energy < 0
   [die]
   end
   to do-plot
   set-current-plot "ratio"
   set-current-plot-pen "ratio"
   if any? turtles
   [plot count hawks / count turtles]
   ;
   end
   References

* Maynard Smith, J. Evolution and the Theory of Games, Cambridge University Press (1982).
* Hauert, C. and Szabó, G. American Journal of Physics, 73, pp. 405-414 (2005).
* Hofbauer, J. and Sigmund, K. Bulletin of the American Mathematical Society, 40, pp. 479-519 (2003).
* Nowak, M. and May, R. Nature, 359, pp. 826-829 (1992).
* Nowak, M., Page, K. and Sigmund, K. Science, 289, pp. 1773-1775 (2000).
* Nowak, M., and Sigmund, K. Science, 303, pp. 793-799 (2004).
* Kerr, B., Riley, M. A., Feldman, M. W. and Bohannan, B. J. M. Nature, 418, pp. 171-174 (2000).
* http://cse.stanford.edu/class/sophomore-college/projects-98/game-theory/ neumann.html.
* http://plato.stanford.edu/entries/game-evolutionary/.
* http://www.economist.com/printedition/displayStory.cfm?Story ID=1045223.
* http://www.dklevine.com/general/cogsci.htm