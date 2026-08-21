---
title: "What Is Machine Learning (ML)? | IBM"
source: "https://www.ibm.com/think/topics/machine-learning"
author:
published:
created: 2025-04-14
description: "Machine learning (ML) is a branch of AI and computer science that focuses on the using data and algorithms to enable AI to imitate the way that humans learn."
tags:
  - "clippings"
---
## Machine learning methods

Machine learning models fall into three primary categories.

### Supervised learning

[Supervised learning](https://www.ibm.com/think/topics/supervised-learning), also known as supervised machine learning, is defined by its use of labeled datasets to train algorithms to classify data or predict outcomes accurately. As input data is fed into the model, the model adjusts its weights until it has been fitted appropriately. This occurs as part of the cross validation process to ensure that the model avoids [overfitting](https://www.ibm.com/think/topics/overfitting) or [underfitting](https://www.ibm.com/think/topics/underfitting). Supervised learning helps organizations solve a variety of real-world problems at scale, such as classifying spam in a separate folder from your inbox. Some methods used in supervised learning include neural networks, [Naïve Bayes](https://www.ibm.com/think/topics/naive-bayes), [linear regression](https://www.ibm.com/think/topics/linear-regression), [logistic regression](https://www.ibm.com/think/topics/logistic-regression), [random forest](https://www.ibm.com/think/topics/random-forest), and [support vector machine (SVM)](https://www.ibm.com/think/topics/support-vector-machine).

### Unsupervised learning

[Unsupervised learning](https://www.ibm.com/think/topics/unsupervised-learning), also known as unsupervised machine learning, uses machine learning algorithms to analyze and cluster unlabeled datasets (subsets called clusters). These algorithms discover hidden patterns or data groupings without the need for human intervention.

Unsupervised learning’s ability to discover similarities and differences in information make it ideal for exploratory data analysis, cross-selling strategies, customer segmentation, and image and pattern recognition. It’s also used to reduce the number of features in a model through the process of dimensionality reduction. [Principal component analysis (PCA)](https://www.ibm.com/think/topics/principal-component-analysis) and singular value decomposition (SVD) are two common approaches for this. Other algorithms used in unsupervised learning include neural networks, [k-means clustering](https://www.ibm.com/think/topics/k-means-clustering), and probabilistic clustering methods.

### Semi-supervised learning 

Semi-supervised learning offers a happy medium between supervised and unsupervised learning. During training, it uses a smaller labeled data set to guide classification and feature extraction from a larger, unlabeled data set. Semi-supervised learning can solve the problem of not having enough labeled data for a supervised learning algorithm. It also helps if it’s too costly to label enough data.

For a deep dive into the differences between these approaches, check out "[Supervised vs. Unsupervised Learning: What's the Difference?](https://www.ibm.com/think/topics/supervised-vs-unsupervised-learning)"

### Reinforcement learning

Reinforcement learning is a machine learning model that is similar to supervised learning, but the algorithm isn’t trained using sample data. This model learns as it goes by using trial and error. A sequence of successful outcomes will be reinforced to develop the best recommendation or policy for a given problem.

The IBM Watson® system that won the *Jeopardy!* challenge in 2011 is a good example. The system [used reinforcement learning](https://developer.ibm.com/articles/cc-reinforcement-learning-train-software-agent/) to learn when to attempt an answer (or question, as it were), which square to select on the board, and how much to wager—especially on daily doubles.