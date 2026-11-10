---
tags:
  - notebooklm-import
notebook: "_A_My Writing Skills Learning and Education"
category: "research"
---

Speech and Language Processing
An Introduction to Natural Language Processing,
Computational Linguistics, and Speech Recognition with Language Models
Third Edition draft
Daniel Jurafsky
Stanford University
James H. Martin
University of Colorado at Boulder
Copyright ©2026. All rights reserved.
Draft of January 6, 2026. Comments and typos welcome!
Summary of Contents
I Large Language Models 1
1 Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 2 Words and Tokens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 3 N-gram Language Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 4 Logistic Regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62 5 Embeddings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96 6 Neural Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120 7 Large Language Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146 8 Transformers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173 9 Masked Language Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199 10 Post-training: Instruction Tuning, Alignment, and Test-Time Com-
pute . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218 11 Retrieval-based Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235 12 Machine Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258 13 RNNs and LSTMs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 284 14 Phonetics and Speech Feature Extraction . . . . . . . . . . . . . . . . . . . . . . . 310 15 Automatic Speech Recognition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 339
16 Text-to-Speech . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 365 II Annotating Linguistic Structure 379
17 Sequence Labeling for Parts of Speech and Named Entities . . . . . . 382 18 Context-Free Grammars and Constituency Parsing . . . . . . . . . . . . . 407 19 Dependency Parsing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 431 20 Information Extraction: Relations, Events, and Time. . . . . . . . . . . . 455 21 Semantic Role Labeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 481 22 Lexicons for Sentiment, Affect, and Connotation . . . . . . . . . . . . . . . . 501 23 Coreference Resolution and Entity Linking . . . . . . . . . . . . . . . . . . . . . 521 24 Discourse Coherence. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 551 25 Conversation and its Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 573 Bibliography. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 581 Subject Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 611
I Large Language Models 1
1 Introduction 3
2 Words and Tokens 4 2.1 Words . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 2.2 Morphemes: Parts of Words . . . . . . . . . . . . . . . . . . . . . 8 2.3 Unicode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10 2.4 Subword Tokenization: Byte-Pair Encoding . . . . . . . . . . . . 13 2.5 Corpora . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 2.6 Regular Expressions . . . . . . . . . . . . . . . . . . . . . . . . . 19 2.7 Simple Unix Tools for Word Tokenization . . . . . . . . . . . . . 27 2.8 Rule-based tokenization . . . . . . . . . . . . . . . . . . . . . . . 28 2.9 Minimum Edit Distance . . . . . . . . . . . . . . . . . . . . . . . 30 2.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3 N-gram Language Models 38 3.1 N-Grams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39 3.2 Evaluating Language Models: Training and Test Sets . . . . . . . 44 3.3 Evaluating Language Models: Perplexity . . . . . . . . . . . . . . 46 3.4 Sampling sentences from a language model . . . . . . . . . . . . . 48 3.5 Generalizing vs. overfitting the training set . . . . . . . . . . . . . 49 3.6 Smoothing, Interpolation, and Backoff . . . . . . . . . . . . . . . 51 3.7 Advanced: Perplexity’s Relation to Entropy . . . . . . . . . . . . 55 3.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
4 Logistic Regression 62 4.1 Machine learning and classification . . . . . . . . . . . . . . . . . 63 4.2 The sigmoid function . . . . . . . . . . . . . . . . . . . . . . . . 65 4.3 Classification with Logistic Regression . . . . . . . . . . . . . . . 67 4.4 Learning in Logistic Regression . . . . . . . . . . . . . . . . . . . 70 4.5 The cross-entropy loss function . . . . . . . . . . . . . . . . . . . 71 4.6 Gradient Descent . . . . . . . . . . . . . . . . . . . . . . . . . . 73 4.7 Multinomial logistic regression . . . . . . . . . . . . . . . . . . . 78 4.8 Learning in Multinomial Logistic Regression . . . . . . . . . . . . 81 4.9 Evaluation: Precision, Recall, F-measure . . . . . . . . . . . . . . 82 4.10 Test sets and Cross-validation . . . . . . . . . . . . . . . . . . . . 85 4.11 Statistical Significance Testing . . . . . . . . . . . . . . . . . . . 86 4.12 Avoiding Harms in Classification . . . . . . . . . . . . . . . . . . 89 4.13 Interpreting models . . . . . . . . . . . . . . . . . . . . . . . . . 91 4.14 Advanced: Regularization . . . . . . . . . . . . . . . . . . . . . . 91 4.15 Advanced: Deriving the Gradient Equation . . . . . . . . . . . . . 93 4.16 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
5 Embeddings 96 5.1 Lexical Semantics . . . . . . . . . . . . . . . . . . . . . . . . . . 97 5.2 Vector Semantics: The Intuition . . . . . . . . . . . . . . . . . . . 99 5.3 Simple count-based embeddings . . . . . . . . . . . . . . . . . . 101 5.4 Cosine for measuring similarity . . . . . . . . . . . . . . . . . . . 103 5.5 Word2vec . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105 5.6 Visualizing Embeddings . . . . . . . . . . . . . . . . . . . . . . . 111 5.7 Semantic properties of embeddings . . . . . . . . . . . . . . . . . 112 5.8 Bias and Embeddings . . . . . . . . . . . . . . . . . . . . . . . . 114 5.9 Evaluating Vector Models . . . . . . . . . . . . . . . . . . . . . . 115 5.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
6 Neural Networks 120 6.1 Units . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121 6.2 The XOR problem . . . . . . . . . . . . . . . . . . . . . . . . . . 123 6.3 Feedforward Neural Networks . . . . . . . . . . . . . . . . . . . . 126 6.4 Feedforward networks for NLP: Classification . . . . . . . . . . . 130 6.5 Embeddings as the input to neural net classifiers . . . . . . . . . . 132 6.6 Training Neural Nets . . . . . . . . . . . . . . . . . . . . . . . . 137 6.7 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
7 Large Language Models 146 7.1 Three architectures for language models . . . . . . . . . . . . . . 149 7.2 Conditional Generation of Text: The Intuition . . . . . . . . . . . 150 7.3 Prompting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151 7.4 Generation and Sampling . . . . . . . . . . . . . . . . . . . . . . 154 7.5 Training Large Language Models . . . . . . . . . . . . . . . . . . 158 7.6 Evaluating Large Language Models . . . . . . . . . . . . . . . . . 164 7.7 Ethical and Safety Issues with Language Models . . . . . . . . . . 167 7.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
8 Transformers 173 8.1 Attention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174 8.2 Transformer Blocks . . . . . . . . . . . . . . . . . . . . . . . . . 180 8.3 Parallelizing computation using a single matrix X . . . . . . . . . 184 8.4 The input: embeddings for token and position . . . . . . . . . . . 187 8.5 The Language Modeling Head . . . . . . . . . . . . . . . . . . . 189 8.6 More on Sampling . . . . . . . . . . . . . . . . . . . . . . . . . . 190 8.7 Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192 8.8 Dealing with Scale . . . . . . . . . . . . . . . . . . . . . . . . . . 193 8.9 Interpreting the Transformer . . . . . . . . . . . . . . . . . . . . . 196 8.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
9 Masked Language Models 199 9.1 Bidirectional Transformer Encoders . . . . . . . . . . . . . . . . . 199
9.2 Training Bidirectional Encoders . . . . . . . . . . . . . . . . . . . 202 9.3 Contextual Embeddings . . . . . . . . . . . . . . . . . . . . . . . 207 9.4 Fine-Tuning for Classification . . . . . . . . . . . . . . . . . . . . 211 9.5 Fine-Tuning for Sequence Labeling: Named Entity Recognition . . 213 9.6 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
10 Post-training: Instruction Tuning, Alignment, and Test-Time Compute 218 10.1 Instruction Tuning . . . . . . . . . . . . . . . . . . . . . . . . . . 219 10.2 Learning from Preferences . . . . . . . . . . . . . . . . . . . . . 224 10.3 LLM Alignment via Preference-Based Learning . . . . . . . . . . 228 10.4 Test-time Compute . . . . . . . . . . . . . . . . . . . . . . . . . . 232 10.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234
11 Retrieval-based Models 235 11.1 Information Retrieval . . . . . . . . . . . . . . . . . . . . . . . . 237 11.2 Evaluation of Information-Retrieval Systems . . . . . . . . . . . . 244 11.3 Information Retrieval with Dense Vectors . . . . . . . . . . . . . . 247 11.4 Retrieval-Augmented Generation (RAG) . . . . . . . . . . . . . . 250 11.5 Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252 11.6 Evaluating Question Answering . . . . . . . . . . . . . . . . . . . 254 11.7 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
12 Machine Translation 258 12.1 Language Divergences and Typology . . . . . . . . . . . . . . . . 259 12.2 Machine Translation using Encoder-Decoder . . . . . . . . . . . . 263 12.3 Details of the Encoder-Decoder Model . . . . . . . . . . . . . . . 267 12.4 Decoding in MT: Beam Search . . . . . . . . . . . . . . . . . . . 269 12.5 Translating in low-resource situations . . . . . . . . . . . . . . . . 273 12.6 MT Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275 12.7 Bias and Ethical Issues . . . . . . . . . . . . . . . . . . . . . . . 279 12.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283
13 RNNs and LSTMs 284 13.1 Recurrent Neural Networks . . . . . . . . . . . . . . . . . . . . . 284 13.2 RNNs as Language Models . . . . . . . . . . . . . . . . . . . . . 288 13.3 RNNs for other NLP tasks . . . . . . . . . . . . . . . . . . . . . . 291 13.4 Stacked and Bidirectional RNN architectures . . . . . . . . . . . . 294 13.5 The LSTM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296 13.6 Summary: Common RNN NLP Architectures . . . . . . . . . . . 300 13.7 The Encoder-Decoder Model with RNNs . . . . . . . . . . . . . . 301 13.8 Attention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 305 13.9 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 307 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 308
14 Phonetics and Speech Feature Extraction 310 14.1 Speech Sounds and Phonetic Transcription . . . . . . . . . . . . . 310
14.2 Articulatory Phonetics . . . . . . . . . . . . . . . . . . . . . . . . 312 14.3 Prosody . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317 14.4 Acoustic Phonetics and Signals . . . . . . . . . . . . . . . . . . . 319 14.5 Feature Extraction for Speech Recognition: Log Mel Spectrum . . 329 14.6 MFCC: Mel Frequency Cepstral Coefficients . . . . . . . . . . . . 334 14.7 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 336 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 338
15 Automatic Speech Recognition 339 15.1 The Automatic Speech Recognition Task . . . . . . . . . . . . . . 340 15.2 Convolutional Neural Networks . . . . . . . . . . . . . . . . . . . 342 15.3 The Encoder-Decoder Architecture for ASR . . . . . . . . . . . . 346 15.4 Self-supervised models: HuBERT . . . . . . . . . . . . . . . . . . 351 15.5 CTC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 355 15.6 ASR Evaluation: Word Error Rate . . . . . . . . . . . . . . . . . 359 15.7 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 362 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 362 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 364
16 Text-to-Speech 365 16.1 TTS overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . 366 16.2 Using a codec to learn discrete audio tokens . . . . . . . . . . . . 367 16.3 VALL-E: Generating audio with 2-stage LM . . . . . . . . . . . . 373 16.4 TTS Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . 375 16.5 Other speech tasks . . . . . . . . . . . . . . . . . . . . . . . . . . 376 16.6 Spoken Language Models . . . . . . . . . . . . . . . . . . . . . . 376 16.7 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 378
II Annotating Linguistic Structure 379
17 Sequence Labeling for Parts of Speech and Named Entities 382 17.1 (Mostly) English Word Classes . . . . . . . . . . . . . . . . . . . 383 17.2 Part-of-Speech Tagging . . . . . . . . . . . . . . . . . . . . . . . 385 17.3 Named Entities and Named Entity Tagging . . . . . . . . . . . . . 387 17.4 HMM Part-of-Speech Tagging . . . . . . . . . . . . . . . . . . . 389 17.5 Conditional Random Fields (CRFs) . . . . . . . . . . . . . . . . . 396 17.6 Evaluation of Named Entity Recognition . . . . . . . . . . . . . . 401 17.7 Further Details . . . . . . . . . . . . . . . . . . . . . . . . . . . 401 17.8 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 403 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 404 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 405
18 Context-Free Grammars and Constituency Parsing 407 18.1 Constituency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 408 18.2 Context-Free Grammars . . . . . . . . . . . . . . . . . . . . . . . 408 18.3 Treebanks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 412 18.4 Grammar Equivalence and Normal Form . . . . . . . . . . . . . . 414 18.5 Ambiguity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 415 18.6 CKY Parsing: A Dynamic Programming Approach . . . . . . . . 417
18.7 Span-Based Neural Constituency Parsing . . . . . . . . . . . . . . 423 18.8 Evaluating Parsers . . . . . . . . . . . . . . . . . . . . . . . . . . 425 18.9 Heads and Head-Finding . . . . . . . . . . . . . . . . . . . . . . 426 18.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 427 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 428 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 429
19 Dependency Parsing 431 19.1 Dependency Relations . . . . . . . . . . . . . . . . . . . . . . . . 432 19.2 Transition-Based Dependency Parsing . . . . . . . . . . . . . . . 436 19.3 Graph-Based Dependency Parsing . . . . . . . . . . . . . . . . . 445 19.4 Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 451 19.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 452 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 453 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 454
20 Information Extraction: Relations, Events, and Time 455 20.1 Relation Extraction . . . . . . . . . . . . . . . . . . . . . . . . . 456 20.2 Relation Extraction Algorithms . . . . . . . . . . . . . . . . . . . 458 20.3 Extracting Events . . . . . . . . . . . . . . . . . . . . . . . . . . 466 20.4 Representing Time . . . . . . . . . . . . . . . . . . . . . . . . . . 467 20.5 Representing Aspect . . . . . . . . . . . . . . . . . . . . . . . . . 470 20.6 Temporally Annotated Datasets: TimeBank . . . . . . . . . . . . . 471 20.7 Automatic Temporal Analysis . . . . . . . . . . . . . . . . . . . . 472 20.8 Template Filling . . . . . . . . . . . . . . . . . . . . . . . . . . . 476 20.9 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 478 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 479 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 480
21 Semantic Role Labeling 481 21.1 Semantic Roles . . . . . . . . . . . . . . . . . . . . . . . . . . . 482 21.2 Diathesis Alternations . . . . . . . . . . . . . . . . . . . . . . . . 482 21.3 Semantic Roles: Problems with Thematic Roles . . . . . . . . . . 484 21.4 The Proposition Bank . . . . . . . . . . . . . . . . . . . . . . . . 485 21.5 FrameNet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 486 21.6 Semantic Role Labeling . . . . . . . . . . . . . . . . . . . . . . . 488 21.7 Selectional Restrictions . . . . . . . . . . . . . . . . . . . . . . . 492 21.8 Primitive Decomposition of Predicates . . . . . . . . . . . . . . . 496 21.9 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 497 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 498 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 500
22 Lexicons for Sentiment, Affect, and Connotation 501 22.1 Defining Emotion . . . . . . . . . . . . . . . . . . . . . . . . . . 502 22.2 Available Sentiment and Affect Lexicons . . . . . . . . . . . . . . 504 22.3 Creating Affect Lexicons by Human Labeling . . . . . . . . . . . 505 22.4 Semi-supervised Induction of Affect Lexicons . . . . . . . . . . . 507 22.5 Supervised Learning of Word Sentiment . . . . . . . . . . . . . . 510 22.6 Using Lexicons for Sentiment Recognition . . . . . . . . . . . . . 515 22.7 Using Lexicons for Affect Recognition . . . . . . . . . . . . . . . 516 22.8 Lexicon-based methods for Entity-Centric Affect . . . . . . . . . . 517 22.9 Connotation Frames . . . . . . . . . . . . . . . . . . . . . . . . . 517
22.10 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 519 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 520 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 520
23 Coreference Resolution and Entity Linking 521 23.1 Coreference Phenomena: Linguistic Background . . . . . . . . . . 524 23.2 Coreference Tasks and Datasets . . . . . . . . . . . . . . . . . . . 529 23.3 Mention Detection . . . . . . . . . . . . . . . . . . . . . . . . . . 530 23.4 Architectures for Coreference Algorithms . . . . . . . . . . . . . 533 23.5 Classifiers using hand-built features . . . . . . . . . . . . . . . . . 535 23.6 A neural mention-ranking algorithm . . . . . . . . . . . . . . . . 537 23.7 Entity Linking . . . . . . . . . . . . . . . . . . . . . . . . . . . . 540 23.8 Evaluation of Coreference Resolution . . . . . . . . . . . . . . . . 544 23.9 Winograd Schema problems . . . . . . . . . . . . . . . . . . . . . 545 23.10 Gender Bias in Coreference . . . . . . . . . . . . . . . . . . . . . 546 23.11 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 547 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 548 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 550
24 Discourse Coherence 551 24.1 Coherence Relations . . . . . . . . . . . . . . . . . . . . . . . . . 553 24.2 Discourse Structure Parsing . . . . . . . . . . . . . . . . . . . . . 556 24.3 Centering and Entity-Based Coherence . . . . . . . . . . . . . . . 560 24.4 Representation learning models for local coherence . . . . . . . . 564 24.5 Global Coherence . . . . . . . . . . . . . . . . . . . . . . . . . . 566 24.6 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 569 Historical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 570 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 572
25 Conversation and its Structure 573 25.1 Properties of Human Conversation . . . . . . . . . . . . . . . . . 573 25.2 Dialog Acts and Corpora . . . . . . . . . . . . . . . . . . . . . . 577
Bibliography 581
Subject Index 611
LARGE LANGUAGE MODELS
In the first part of the book we introduce the fundamental suite of algorithmic and linguistic tools that make up the modern neural large language model. We begin with tokenization and preprocessing, including Unicode, and then proceed to intro-duce many basic language modeling ideas using simple n-gram language models, we then introduce the algorithms which are the components of large language models: logistic regression, embeddings, and feedforward networks. Next we are ready to introduce the principles of large language modeling, encoder, decoders and pretrain-ing, then the fundamental transformer architecture, then masked language model and other architectures like RNNs and LSTMs, information retrieval and retrieval-based algorithms like RAG, machine translation and the encoder-decoder model, and finally spoken language modeling including both ASR and TTS.
1 Introduction
La dernière chose qu’on trouve en faisant un ouvrage est de savoir celle qu’il faut mettre la première. [The last thing you figure out in writing a book is what to put first.]
4 CHAPTER 2 • WORDS AND TOKENS
2 Words and Tokens
User: I need some help, that much seems certain.
ELIZA: WHAT WOULD IT MEAN TO YOU IF YOU GOT SOME HELP
User: Perhaps I could learn to get along with my mother.
ELIZA: TELL ME MORE ABOUT YOUR FAMILY
User: My mother takes care of me.
ELIZA: WHO ELSE IN YOU FAMILY TAKES CARE OF YOU
User: My father.
ELIZA: YOUR FATHER
User: You are like my father in some ways.
Weizenbaum (1966)
The dialogue above is from ELIZA, an early natural language processing systemELIZA
that could carry on a limited conversation with a user by imitating the responses of a Rogerian psychotherapist (Weizenbaum, 1966). ELIZA is a surprisingly simple program that uses pattern matching on words to recognize phrases like “I need X” and change the words into suitable outputs like “What would it mean to you if you got X?”. ELIZA’s mimicry of human conversation, while very crude by modern standards, was remarkably successful: many people who interacted with ELIZA came to believe that it really understood them. As a result, this work led researchers to first think about the impacts of chatbots on their users (Weizenbaum, 1976).
Of course modern chatbots don’t use the simple pattern-based mimicry that ELIZA pioneered. Yet the pattern-based approach to words instantiated in ELIZA is still relevant today in the context of tokenization, the task of separating out ortokenization
tokenizing words and word parts from running text. Tokenization, the first step in modern NLP, includes pattern-based approaches that date back to ELIZA.
To understand tokenization we first need to ask: What is a word? Is um a word? What about New York? Is the nature of words similar across languages? Some languages, like Vietnamese or Cantonese, have very short words while others, like Turkish, have very long words. We also need to think about how to represent words in terms of characters. We’ll introduce Unicode, the modern system for represent-ing characters, and the UTF-8 text encoding. And we’ll introduce the morpheme, the meaningful subpart of words (like the morpheme -er in the word longer)
The standard way to tokenize text is to use the input characters to guide us. So once we understand the possible subparts of words, we’ll introduce the stan-dard Byte-Pair Encoding (BPE) algorithm that automatically breaks up input textBPE
into tokens. This algorithm uses simple statistics of letter sequences to induce a vocabulary of subword tokens. All tokenization systems also depend on regular expressions as a processing step. The regular expression is a language for formallyregular
expressions specifying and manipulating text strings, an important tool in all modern NLP sys-tems. We’ll introduce regular expressions and show examples of their use
Finally, we’ll introduce a metric called edit distance that measures how similar two words or strings are based on the number of edits (insertions, deletions, substi-tutions) it takes to change one string into the other. Edit distance plays a role in NLP whenever we need compare two words or strings, for example in the crucial word error rate metric for automatic speech recognition.
2.1 • WORDS 5
How many words are in the following sentence?
They picnicked by the pool, then lay back on the grass and
looked at the stars.
This sentence has 16 words if we don’t count punctuation as words, 18 if we count punctuation. Whether we treat period (“.”), comma (“,”), and so on as words depends on the task. Punctuation is critical for finding boundaries of things (com-mas, periods, colons) and for identifying some aspects of meaning (question marks, exclamation marks, quotation marks). Large language models generally count punc-tuation as separate words.
Spoken language introduces other complications with regard to defining words. What about this utterance from a spoken conversation? (Utterance is the technicalutterance
linguistic term for the spoken correlate of a sentence).
I do uh main- mainly business data processing
This utterance has two kinds of disfluencies. The broken-off word main- isdisfluency
called a fragment. Words like uh and um are called fillers or filled pauses. Shouldfragment
filled pause we consider these to be words? Again, it depends on the application. If we are building a speech transcription system, we might want to eventually strip out the disfluencies. But we also sometimes keep disfluencies around. Disfluencies like uh or um are actually helpful in speech recognition in predicting the upcoming word, because they may signal that the speaker is restarting the clause or idea, and so for speech recognition they are treated as regular words. Because different people use different disfluencies they can also be a cue to speaker identification. In fact Clark and Fox Tree (2002) showed that uh and um have different meanings in English. What do you think they are?
Perhaps most important, in thinking about what is a word, we need to distinguish two ways of talking about words that will be useful throughout the book. Word typesword type
are the number of distinct words in a corpus; if the set of words in the vocabulary is V , the number of types is the vocabulary size |V |. Word instances are the totalword instance
number N of running words.1 If we ignore punctuation, the picnic sentence has 14 types and 16 instances:
They picnicked by the pool, then lay back on the grass and
looked at the stars.
We still have decisions to make! For example, should we consider a capitalized string (like They) and one that is uncapitalized (like they) to be the same word type? The answer is that it depends on the task! They and they might be lumped together as the same type in some tasks where we care less about the formatting, while for other tasks, capitalization is a useful feature and is retained. Sometimes we keep around two versions of a particular NLP model, one with capitalization and one without capitalization.
So far we have been talking about orthographic words: words based on our English writing system. But there are many other possible ways to define words. For example, while orthographically I’m is one word, grammatically it functions as two words: the subject pronoun I and the verb ’m, short for am.
1 In earlier tradition, and occasionally still, you might see word instances referred to as word tokens, but we now try to reserve the word token instead to mean the output of subword tokenization algorithms.
6 CHAPTER 2 • WORDS AND TOKENS
Corpus Types = |V | Instances = N Shakespeare 31 thousand 884 thousand Brown corpus 38 thousand 1 million Switchboard telephone conversations 20 thousand 2.4 million COCA 2 million 440 million Google n-grams 13 million 1 trillion
Figure 2.1 Rough numbers of wordform types and instances for some English language corpora. The largest, the Google n-grams corpus, contains 13 million types, but this count only includes types appearing 40 or more times, so the true number would be much larger.
The distinctions get even harder to make once we start to think about other lan-guages. For example the writing systems of languages like Chinese, Japanese, and Thai simply don’t have orthographic words at all! That is, they don’t use spaces to mark potential word-boundaries. In Chinese, for example, words are composed of characters (called hanzi in Chinese). Each character generally represents a singlehanzi
unit of meaning (called a morpheme, introduced below) and is pronounceable as a single syllable. Words are about 2.4 characters long on average. But since Chinese has no orthographic words, deciding what counts as a word in Chinese is complex. For example, consider the following sentence:
(2.1) 姚明进入总决赛 yáo mı́ng jı̀n rù zǒng jué sài “Yao Ming reaches the finals”
As Chen et al. (2017b) point out, this could be treated as 3 words (a definition of words called the ‘Chinese Treebank’ definition, in which Chinese names (family name followed by personal names) are treated as a single word):
(2.2) 姚明 YaoMing
But the same sentence could be treated as 5 words (‘Peking University’ standard), in which names are separated into their own units and some adjectives appear as distinct words:
(2.3) 姚 Yao 明 Ming
Finally, it is possible in Chinese simply to ignore words altogether and use characters as the basic elements, treating the sentence as a series of 7 characters, which works pretty well for Chinese since characters are at a reasonable semantic level for most applications (Li et al., 2019):
(2.4) 姚 Yao 明 Ming
But that method doesn’t work for Japanese and Thai, where the individual character is too small a unit.
These issues with defining words makes it hard to use words as the basis for tokenizing text in NLP across languages.
But there’s another problem with words. There are too many of them!!! How many words are there in English? When we speak about the number of words in the language, we are generally referring to word types. Fig. 2.1 shows the rough numbers of types and instances computed from some English corpora.
You will notice that the larger the corpora we look at, the more word types we find! That suggests that there is not a clear answer to how many words there are; the answer keeps growing as we see more data! We can see this fact mathematically
2.1 • WORDS 7
because the relationship between the number of types |V | and number of instances N is called Herdan’s Law (Herdan, 1960) or Heaps’ Law (Heaps, 1978) after itsHerdan’s Law
Heaps’ Law discoverers (in linguistics and information retrieval respectively). It is shown in Eq. 2.5, where k and
are positive constants, and
The value of
depends on the corpus size and the genre; numbers from 0.44 to 0.56 or even higher have often been reported. Roughly we can say that the vocabulary size for a text goes up a little faster than the square root of its length in words.
There are also variants of the law, which capture the fact that we can distinguish roughly two classes of words. One is function words, the grammatical words likefunction words
English a and of, that tend not to grow indefinitely (a language tends to have a fixed number of these). The other is content words: nouns, adjectives and verbs that tendcontent words
to have meanings about people and places and events. Nouns, and especially partic-ular nouns like names and technical terms do tend to grow indefinitely. So models that are sensitive to this difference between function words and content words have one value of
for the initial part of the corpus where all words are still appearing, and then a second
afterwords for when only the content words are still appearing. Fig. 2.2 shows an example from Tria et al. (2018) showing two values of
in their figure) for Heaps law computed on the Gutenberg corpus of books. Note thatEntropy 2018, 20, 752 4 of 19
Figure 2. Growth of the number of distinct words computed on the Gutenberg corpus of texts [15]. The position of texts in the corpus is chosen at random. In this case
' 0.44. Similar behaviours are observed in many other systems.
2.3. Zipf’s vs. Heaps’ Laws
In this section we compare the two laws just observed, Zipf’s law for the frequencies of occurrence of the elements in a system and Heaps’ law for their temporal appearance. It has often been claimed that Heaps’ and Zipf’s law are trivially related and that one can derive Heaps’s law once the Zipf’s is known. This is not true in general. It turns out to be true only under the specific hypothesis of random-sampling as follows. Suppose the existence of a strict power-law behaviour of the frequency-rank distribution, f (R)
and construct a sequence of elements by randomly sampling from this Zipf distribution f (R). Through this procedure, one recovers a Heaps’ law with the functional form D(t)
[23,24] with
In order to do that we need to consider the correct expression for f (R) that includes the normalisation factor, whose expression can be derived through the following approximated integral:
1 f (R̃)dR̃ = 1 . (3)
Let us now distinguish the two cases. For
6= 1 one has
Figure 2. The thick blue line shows V cabulary size |V | (called D in their figure) as a function of text l ngth (thei w), omputed on the Gutenb rg corpus of publicly av ilable books. Note th t at the beginning of the corpus, we see both common and function words and the relationship between corpus size and vocabulary is roughly linear (green line,
= 1). Later, after the function words have mainly appeared, the number of new words slows down and is closer to the square root of the corpus size. Figure from Tria et al. (2018).
The fact that words grow without end leads to a problem for any computational model. No matter how big our vocabulary, we will never have a vocabulary that captures all the possible words that might occur! That means that our computational model will constantly see unknown words: words that it has never seen before. This is a huge problem for machine learning models.
Because of these two problems (first, that many languages don’t h ve ortho-graphic words, and defining them post-hoc is challenging and second, that the num-ber of words grows without bound), language models and other NLP models don’t
8 CHAPTER 2 • WORDS AND TOKENS
tend to use words as their unit of processing. Instead, they use smaller units called subwords that can be recombined to model new words that our model has never seen before. To think about defining subwords, we first need to talk about units that are smaller than words; morphemes and characters.
2.2 Morphemes: Parts of Words
Words have parts. At the level of characters, this is obvious. The word cats is com-posed of four characters, ‘c’, ‘a’, ‘t’, ‘s’. But this is also true at a more subtle level: words have components that themselves have coherent meanings. These compo-nents are called morphemes, and the study of morphemes is called morphology. Amorphology
morpheme is a minimal meaning-bearing unit in a language. So, for example, themorpheme
word fox consists of one morpheme (the morpheme fox) while the word cats consists of two: the morpheme cat and the morpheme -s that indicates plural.
Here’s a sentence in English segmented into morphemes with hyphens:
(2.6) Doc work-ed care-ful-ly wash-ing the glass-es
As we mentioned above, in Chinese, conveniently, the writing system is set up so that each character mainly describes a morpheme. Here’s a sentence in Mandarin Chinese with each morpheme character glossed, followed by the translation:
(2.7) 梅 plum
干 dry 菜 vegetable
用 use 清 clear
软 soft ， , 捞 remove
出 out 后 after
， , 沥 drip 干 dry
Soak the preserved vegetable in water until soft, remove, drain, and chop
We generally distinguish two broad classes of morphemes: roots—the centralroot
morpheme of the word, supplying the main meaning—and affixes—adding “ad-affix
ditional” meanings of various kinds. In the English example above, for the word worked, work is a root and -ed is an affix; similarly for glasses, glass is a root and -es an affix.
Affixes themselves fall into two classes, or more correctly a continuum between two poles. At one end, inflectional morphemes are grammatical morphemes thatinflectional
morphemes tend to play a syntactic role, such as marking agreement. For example, English has the inflectional morpheme -s (or -es) for marking the plural on nouns and the inflec-tional morpheme -ed for marking the past tense on verbs. Inflectional morphemes tend to be productive and often obligatory and their meanings tend to be predictable. Derivational morphemes are more idiosyncratic in their application and meaning.derivational
morphemes Usually they apply only to a specific subclass of words and result in a word of a dif-ferent grammatical class than the root, often with a meaning hard to predict exactly. In the example above, the word care (a noun) can be combined with the derivational affix -full to produce an adjective (careful), and another derivational affix -ly to result in an adverb (carefully).
There is another class of morphemes: clitics. A clitic is a morpheme that actsclitic
syntactically like a word but is reduced in form and attached (phonologically and sometimes orthographically) to another word. For example the English morpheme ’ve in the word I’ve is a clitic; it has the grammatical meaning of the word have, but in form in cannot appear alone (you can’t just say the sentence “’ve”). The English possessive morpheme ’s in the phrase the teacher’s book is a clitic. French definite
2.2 • MORPHEMES: PARTS OF WORDS 9
article l’ in the word l’opera is a clitic, as are prepositions in Arabic like b ‘by/with’ and conjunctions like w ‘and’.
The study of how languages vary in their morphology, i.e., how words break up into their parts, is called morphological typology. While morphologies of lan-morphological
typology guages can differ along many dimensions, two dimensions are particularly relevant for computational word tokenization.
The first dimension is the number of morphemes per word. In some languages, like Vietnamese and Cantonese, each word on average has just over one morpheme. We call languages at this end of the scale isolating languages. For example eachisolating
word in the following Cantonese sentence has one morpheme (and one syllable):
(2.8) keoi5 he
cyun4 entire
gwok3 country
gaan1 building
gaan1 building
“He said the biggest house in the country was this one”
Alternatively, in languages like Koryak, a Chukotko-Kamchatkan language spo-ken in the northern part of the Kamchatka peninsula in Russia, a single word may have very many morphemes, corresponding to a whole sentence in English (Arkadiev, 2020; Kurebito, 2017). We call languages toward this end of the scale synthetic lan-synthetic
guages, and the very end of the scale polysynthetic languages.polysynthetic
(2.9) t-@-nk’e-mejN-@-jetem@-nni-k 1SG.S-E-midnight-big-E-yurt.cover-E-sew-1SG.S[PFV] “I sewed a lot of yurt covers in the middle of a night.” (Koryak, Chukotko-Kamchatkan, Russia; Kurebito (2017, 844))
Fig. 2.3 shows an early computation of morphemes per words on a few languages by the linguistic typologist Joseph Greenberg (1960).
Analytic Synthetic
Farsi Greenlandic
(Inuit) Sanskr
Swahili Yakut
Old English
English Vietnamese
1.1 1.5 1.7 2.1 2.2 2.5 2.6 3.7
Morphemes per Word
Polysynthetic
Figure 2.3 An early estimate of morphemes per word by Joseph Greenberg (1960).
The second dimension is the degree to which morphemes are easily segmentable, ranging from agglutinative languages like Turkish, in which morphemes have rel-agglutinative
atively clean boundaries, to fusion languages like Russian, in which a single affixfusion
may conflate multiple morphemes, like -om in the word stolom (table-SG-INSTR-DECL1), which fuses the distinct morphological categories instrumental, singular, and first declension.
The English -s suffix in She reads the article is an example of fusion, since the suffix means both third person singular but also means present tense, and there’s no way to divide up the meaning to different parts of the -s.
Although we have loosely talked about these properties (analytic, polysynthetic, fusional, agglutinative) as if they are properties of languages, in fact languages can make use of different morphological systems so it would be more accurate to talk about these as general tendencies.
10 CHAPTER 2 • WORDS AND TOKENS
Nonetheless, the fact morphemes can be hard to define, and that many languages can have complex morphemes that aren’t easy to break up into pieces makes it very difficult to use morphemes as a standard for tokenization cross-lingually.
2.3 Unicode
Another option we could consider for tokenization is the level of the individual char-acter. How do we even represent characters across languages and writing system? The Unicode standard is a method for representing text written using any characterUnicode
in any script of the languages of the world (including dead languages like Sumerian cuneiform, and invented languages like Klingon).
Let’s start with a brief historical note about an English-specific subset of Unicode (technically called ‘Basic Latin’ in Unicode, and commonly referred to as ASCII). Starting in the 1960s, the Latin characters used to write English (like the ones used in this sentence), were represented with a code called ASCII (American StandardASCII
Code for Information Interchange). ASCII represented each character with a single byte. A byte can represent 256 different characters, but ASCII only used 127 of them; the high-order bit of ASCII bytes is always set to 0. (Actually it only used 95 of them and the rest were control codes for an obsolete machine called a teletype). Here’s a few ASCII characters with their representation in hex and decimal:
Ch Hex Dec Ch Hex Dec Ch Hex Dec Ch Hex Dec < 3C 60 @ 40 64 ... \ 5C 92 ‘ 60 96 = 3D 61 A 41 65 ... [ 5D 93 a 61 97 > 3E 62 B 42 66 ... ˆ 5E 94 b 62 98 ? 3F 63 C 43 67 ... \_ 5F 95 c 63 99 Figure 2.4 Some selected ASCII codes for some English letters, with the codes shown both in hexadecimal and decimal.
But ASCII is of course insufficient since there are lots of other characters in the world’s writing systems! Even for scripts that use Latin characters, there are many more than the 95 in ASCII. For example, this Spanish phrase (meaning “Sir, replied Sancho”) has two non-ASCII characters, ñ and ó:
(2.10) Señor- respondió Sancho-
And lots of languages aren’t based on Latin characters at all! The DevanagariDevanagari
script is used for 120 languages (including Hindi, Marathi, Nepali, Sindhi, and San-skrit). Here’s a Devanagari example from the Hindi text of the Universal Declaration of Human Rights:
Chinese has about 100,000 Chinese characters in Unicode (including overlap-ping and non-overlapping variants used in Chinese, Japanese, Korean, and Viet-namese, collectively referred to as CJKV).
All in all there are more than 150,000 characters and 168 different scripts sup-ported in Unicode 16.0. Even though many scripts from around the world have yet to be added to Unicode, there are so many there, from scripts used by mod-ern languages (Chinese, Arabic, Hindi, Cherokee, Ethiopic, Khmer, N’Ko, Turkish,
2.3 • UNICODE 11
Spanish) to scripts of ancient languages (Cuneiform, Ugaritic, Egyptian Hieroglyph, Pahlavi), as well as mathematical symbols, emojis, currency symbols, and more.
2.3.1 Code Points
How does it work? Unicode assigns a unique id, called a code point, for each onecode point
of these 150,000 characters. The code point is an abstract representation of the character, and each code point
is represented by a number, traditionally written in hexadecimal, from number 0 through 0x10FFFF (which is 1,114,111 decimal). Having over a million code points means there is a lot of room for new characters. It is traditional to represent these code points with the prefix “U+” (which just means “the following is a Unicode hex representation of a code point”). So the code point for the character a is U+0061
which is the same as 0x0061. (Note that Unicode was designed to be backwards compatible with ASCII, which means that the first 127 code points, including the code for a, are identical with ASCII.) Here are some sample code points; some (but not all) come with descriptions:
U+0061 a LATIN SMALL LETTER A
U+0062 b LATIN SMALL LETTER B
U+0063 c LATIN SMALL LETTER C
U+00F9 ù LATIN SMALL LETTER U WITH GRAVE
U+00FA ú LATIN SMALL LETTER U WITH ACUTE
U+00FB û LATIN SMALL LETTER U WITH CIRCUMFLEX
U+00FC ü LATIN SMALL LETTER U WITH DIAERESIS
U+8FDB 进 U+8FDC 远 U+8FDD 违 U+8FDE 连
5/23/25, 5:26 PM x.html
GRINNING FACE
5/23/25, 5:26 PM x.html
MAHJONG TILE EIGHT OF CHARACTERS
Note that a code point does not specifiy the glyph, the visual representationglyph
of a character. Glyphs are stored in fonts. The code point U+0061 is an abstract representation of a. There can be an indefinite number of visual representations, for example in different fonts like Times Roman (a) or Courier (a), or different font styles like boldface (a) or italic (a). But all of them are represented by the same code point U+0061.
2.3.2 UTF-8 Encoding
While the code point (the unique id) is the abstract Unicode representation of the character, we don’t just stick that id in a text file.
Instead, whenever we need to represent a character in a text string, we write an encoding of the character. There are many different possible encoding methods, butencoding
the encoding method called UTF-8 is by far the most frequent (for example almost the entire web is encoded in UTF-8).
Let’s talk about encodings. The Unicode representation of the word hello con-sists of the following sequence of 5 code points:
U+0068 U+0065 U+006C U+006C U+006F
12 CHAPTER 2 • WORDS AND TOKENS
We can imagine a very simple encoding method: just write the code point id in a file. Since there are more than 1 million characters, 16 bits (2 bytes) isn’t enough, so we’ll need to use 4 bytes (32 bit) to capture the 21 bits we need to represent 1.1 million characters. (We could fit it in 3 bytes but it’s inconvenient to use multiples of 3 for bytes.)
With this 4-byte representation the word hello would be encoded as the follow-ing set of bytes:
00 00 00 68 00 00 00 65 00 00 00 6C 00 00 00 6C 00 00 00 6F
But we don’t use this encoding (which is technically called UTF-32) because it makes every file 4 times longer than it would have been in ASCII, making files really big and full of zeros. Also those zeros cause another problem: it turns out that having any byte that is completely zero messes things up for backwards compatibility for ASCII-based systems that historically used a 0 byte as an end-of-string marker.
Instead, the most common encoding standard is UTF-8 (Unicode Transforma-UTF-8
tion Format 8), which represents characters efficiently (using fewer bytes on av-erage) by writing some characters using fewer bytes and some using more bytes. UTF-8 is thus a variable-length encoding.variable-length
encoding For some characters (the first 127 code points, i.e. the set of ASCII characters),
UTF-8 encodes them as a single byte, so the UTF-8 encoding of hello is :
68 65 6C 6C 6F
This conveniently means that files encoded in ASCII are also valid UTF-8 en-codings!
But UTF-8 is a variable length encoding, meaning that code points
are encoded as a sequence of two, three, or four bytes. Each of these bytes are between 128 and 255, so they won’t be confused with ASCII, and each byte indicates in the first few bits whether it’s a 2-byte, 3-byte, or 4-byte encoding.
Code Points UTF-8 Encoding From - To Bit Value Byte 1 Byte 2 Byte 3 Byte 4 U+0000-U+007F 0xxxxxxx xxxxxxxx U+0080-U+07FF 00000yyy yyxxxxxx 110yyyyy 10xxxxxx U+0800-U+FFFF zzzzyyyy yyxxxxxx 1110zzzz 10yyyyyy 10xxxxxx U+010000-U+10FFFF 000uuuuu zzzzyyyy yyxxxxxx 11110uuu 10uuzzzz 10yyyyyy 10xxxxxx Figure 2.5 Mapping from Unicode code point to the variable length UTF-8 encoding. For a given code point in the From-To range, the bit value in column 2 is packed into 1, 2, 3, or 4 bytes. Figure adapted from Unicode 16.0 Core Spec Chapter 3 Table 3-6.
Fig. 2.5 shows how this mapping occurs. For example these rules explain how the character ñ, which has code point U+00F1, or bit sequence 00000000 11110001, (where blue indicates the sequence yyyyy and red the sequence xxxxxx) is encoded into to the two-byte bit sequence 11000011 10110001 or 0xC3B1. As a result of these rules, the first 127 characters (ASCII) are mapped to one byte, most remain-ing characters in European, Middle Eastern, and African scripts map to two bytes, most Chinese, Japanese, and Korean characters map to three bytes, and rarer CJKV characters and emojis and some symbols map to 4 bytes.
UTF-8 has a number of advantages. It’s relatively efficient, using fewer bytes for commonly-encountered characters, it doesn’t use zero bytes (except when literally representing the NULL character which is U+0000), it’s backwards compatible with ASCII, and it’s self-synchronizing, meaning that if a file is corrupted, it’s always possible to find the start of the next or prior character just by moving up to 3 bytes left or right.
2.4 • SUBWORD TOKENIZATION: BYTE-PAIR ENCODING 13
Unicode and Python: Starting with Python 3, all Python strings are stored in-ternally as Unicode, each string a sequence of Unicode code points. Thus string functions and regular expressions all apply natively to code points. For example, functions like len() of a string return its length in characters, i.e., code points, not its length in bytes.
When reading or writing from a file, however, the code points need to be encoded and decoding using a method like UTF-8. That is, every file is encoded in some encoding. If it’s not UTF-8, it’s an older encoding method like ASCII or Latin-1 (iso 8859 1). There is no such thing as a text file without an encoding. The encoding method is specified in Python when opening a file for reading and writing.
2.4 Subword Tokenization: Byte-Pair Encoding
Tokenization, the first stage of natural language processing, is the process of seg-tokenization
menting the running input text into tokens.tokens
We’ve seen three candidates for tokens: words, morphemes and characters. But each has problems as a unit. Words and morphemes seem approximately at the right level for NLP processing, since they tend to have consistent meanings, but they are challenging to define formally. Characters are clearer to define, but seem too small a unit to choose for tokens.
In this section we introduce what we do in practice for NLP: use a data-driven approach to define tokens that will generally result in units about the size of mor-phemes or words, but occasionally use units as small as characters.
Why tokenize the input? One reason is that converting an input to a deterministic fixed set of units means that different algorithms and systems can agree on simple questions. For example, How long is this text? (How many units are in it?). Or: Is don’t or New York one token or two? Standardizing is thus essential for repli-cability in NLP experiments, and many algorithms that we introduce in this book (like the perplexity metric for language models) assume that all texts have a fixed tokenization.
Tokenization algorithms that include smaller tokens for morphemes and letters also eliminate the problem of unknown words. What are these? As we will see in the next chapter, NLP algorithms often learn some facts about language from one corpus (a training corpus) and then use these facts to make decisions about a separate test corpus and its language. Thus if our training corpus contains, say the words low, new, and newer, but not lower, then if the word lower appears in our test corpus, our system will not know what to do with it.
To deal with this unknown word problem, modern tokenizers automatically in-duce sets of tokens that include tokens smaller than words, called subwords. Sub-subwords
words can be arbitrary substrings, or they can be meaning-bearing units like the morphemes -est or -er. In modern tokenization schemes, many tokens are words, but other tokens are frequently occurring morphemes or other subwords like -er. Every unseen word can thus be represented by some sequence of known subword units. For example, if we had happened not to ever see the word lower, when it ap-pears we could segment it successfully into low and er which we had already seen. In the worst case, a really unusual word (perhaps an acronym like GRPO) could be tokenized as a sequence of individual letters if necessary.
Two tokenization algorithms are widely used in modern language models: byte-pair encoding (BPE) (Sennrich et al., 2016), and unigram language modeling
14 CHAPTER 2 • WORDS AND TOKENS
(ULM) (Kudo, 2018).2 In this section we introduce the byte-pair encoding or BPEBPE
algorithm (Sennrich et al., 2016; Gage, 1994); see Fig. 2.6. Like most tokenization schemes, the BPE algorithm has two parts: a trainer,
and an encoder. In general in the token training phase we take a raw training corpus (usually roughly pre-separated into words, for example by whitespace) and induce a vocabulary, a set of tokens. Then a token encoder takes a raw test sentence and encodes it into the tokens in the vocabulary that were learned in training.
2.4.1 BPE training The BPE training algorithm iteratively merges frequent neighboring tokens to create longer and longer tokens. The algorithm begins with a vocabulary that is just the set of all individual characters. It then examines the training corpus, and finds the two characters that are most frequently adjacent. Imagine our original corpus is 10 characters long, using a vocabulary of 5 characters, {A, B, C, D, E}:
A B D C A B E C A B
The most frequent neighboring pair of characters is “A B” so we merge those, add a new merged token ‘AB’ to the vocabulary, and replace every adjacent ‘A’ ‘B’ in the corpus with the new ‘AB’:
AB D C AB E C AB
Now we have a vocabulary of 6 possible tokens {A, B, C, D, E, AB}, and the corpus has length 7. And now the most frequent pair of tokens is “C AB”, so we merge those, leading to a vocabulary with 7 tokens {A, B, C, D, E, AB, CAB}, and the corpus has length 5.
AB D CAB E CAB
The algorithm continues to count and merge, creating new longer and longer character strings, until k merges have been done creating k novel tokens; k is thus a parameter of the algorithm. The resulting vocabulary consists of the original set of characters plus k new symbols. That’s the core of the algorithm.
The only additional complication is that in practice, instead of running on the raw sequence of characters, the algorithm is usually run only inside words. That is, the algorithm does not merge across word boundaries. To do this, the input corpus is often first separated at white space and punctuation (using the regular expressions that we define later in the chapter). This gives a starting set of strings, each corre-sponding to the characters of a word, (with the white space usually attached to the start of the word), together with the counts of the words. Then while counts come from a corpus, merges are only allowed within the strings.
Let’s see how the full algorithm thus works on this tiny synthetic corpus, where we’ve explicitly marked the spaces between words:3
(2.11) set new new renew reset renew
First, we’ll break up the corpus into words, with leading whitespace, together with their counts; no merges will be allowed to go beyond these word boundaries. The result looks like the following list of 4 words and a starting vocabulary of 7 characters:
2 The SentencePiece library includes implementations of both of these (Kudo and Richardson, 2018a), and people sometimes use the name SentencePiece to simply mean ULM tokenization. 3 Yes, we realize this isn’t a particularly likely or exciting sentence.
2.4 • SUBWORD TOKENIZATION: BYTE-PAIR ENCODING 15
corpus vocabulary 2 n e w , e, n, r, s, t, w
2 r e n e w
1 r e s e t
The BPE training algorithm first counts all pairs of adjacent symbols: the most frequent is the pair n e because it occurs in new (frequency of 2) and renew (fre-quency of 2) for a total of 4 occurrences. We then merge these symbols, treating ne
as one symbol, and count again:
corpus vocabulary 2 ne w , e, n, r, s, t, w, ne
1 r e s e t
Now the most frequent pair is ne w (total count=4), which we merge.
corpus vocabulary 2 new , e, n, r, s, t, w, ne, new
1 r e s e t
Next r (total count of 3) get merged to r, and then r e (total count 3) gets merged to re. The system has essentially induced that there is a word-initial prefix re-:
corpus vocabulary 2 new , e, n, r, s, t, w, ne, new, r, re
If we continue, the next merges are: merge current vocabulary ( , new) , e, n, r, s, t, w, ne, new, r, re, new
( re, new) , e, n, r, s, t, w, ne, new, r, re, new, renew
(s, e) , e, n, r, s, t, w, ne, new, r, re, new, renew, se
(se, t) , e, n, r, s, t, w, ne, new, r, re, new, renew, se, set
function BYTE-PAIR ENCODING(strings C, number of merges k) returns vocab V
unique characters in C # initial set of tokens is characters for i = 1 to k do # merge tokens k times
frequent pair of adjacent tokens in C
tL + tR # make new token by concatenating

* tNEW # update the vocabulary Replace each occurrence of tL, tR in C with tNEW # and update the corpus
  Figure 2.6 The training part of the BPE algorithm for taking a corpus broken up into in-dividual characters or bytes, and learning a vocabulary by iteratively merging tokens. Figure adapted from Bostrom and Durrett (2020).
  16 CHAPTER 2 • WORDS AND TOKENS
  2.4.2 BPE encoder Once we’ve learned our vocabulary, the BPE encoder is used to tokenize a test sentence. The encoder just runs on the test data the merges we have learned from the training data. It runs them greedily, in the order we learned them. (Thus the frequencies in the test data don’t play a role, just the frequencies in the training data). So first we segment each test sentence word into characters. Then we apply the first rule: replace every instance of n e in the test corpus with ne, and then the second rule: replace every instance of ne w in the test corpus with new, and so on. By the end of course many of the merges simple recreated words in the training set. But the merges also created knowledge of morphemes like the re- prefix (that might appear in perhaps unseen combinations like revisit or rearrange), or the morpheme new without an initial space (hence word-internal) that might appear at the start of sentences or in words unseen in training like anew.
  Of course in real settings BPE is run with tens of thousands of merges on a very large input corpus, to produce vocabulary sizes of 50,000, 100,000, or even 200,000 tokens. The result is that most words can be represented as single tokens, and only the rarer words (and unknown words) will have to be represented by multiple tokens. At least for English. For multilingual systems, the tokens can be dominated by English, leaving fewer tokens for other languages, as we’ll discuss below.
  2.4.3 BPE in practice The example above just showed simple BPE learning from sequences of ASCII bytes. How does BPE work with Unicode input? We normally run BPE on the individual bytes of UTF-8-encoded text. That is, we take a Unicode representations of text as a series of code points, encode it in bytes using UTF-8, and we treat each of these individual bytes as the input to BPE. Thus BPE likely begins by rediscovering the 2-byte and common 3-byte sequences that UTF-8 uses to encode various code points. Again, running BPE only inside presegmented words helps avoid problems. Because there are only 256 possible values of a byte, there will be no unknown to-kens, although it’s possible that BPE will learn some illegal UTF-8 sequences across character boundaries. These will be very rare, and can be eliminated with a filter.
  Let’s see some examples of the industrial application of the BPE tokenizer used in large systems like OpenAI GPT4o. This tokenizer has 200K tokens, which is a comparatively large number. We can use Tat Dat Duong’s Tiktokenizer visualizer (https://tiktokenizer.vercel.app/) to see the number of tokens in a given sentence. For example here’s the tokenization of a nonsense sentence we made up; the visualizer uses a center dot to indicate a space:
  The visualization shows colors to separate out words, but of course the true out-put of the tokenizer is simply a sequence of unique token ids. (In case you’re in-terested, they were the following 13 tokens: 11865, 8923, 11, 31211, 6177, 23919, 885, 220, 19427, 7633, 18887, 147065, 0)
  Notice that most words are their own token, usually including the leading space. Clitics like ’s are segmented off when they appear on proper nouns like Jane, but are counted as part of a word for frequent words like she’s. Numbers tend to be segmented into chunks of 3 digits. And some words (like anyhow) are segmented differently if they appear capitalized sentence-initially (two tokens, Any and how), then if they appear after a space, lower case (one token anyhow).
  2.5 • CORPORA 17
  Some of these are related to preprocessing steps. As we mentioned briefly above, language models usually create their tokens in a pretokenization stage that first seg-pretokenization
  ments the input using regular expressions, for example breaking the input at spaces and punctuation, stripping off clitics, and breaking numbers into sets of digits. We’ll see how to use regular expressions in Section 2.6.
  It’s possible to change this pretokenization to allow BPE tokens to span multiple words. For example the SuperBPE (Liu et al., 2025) and BoundlessBPE (SchmidtSuperBPE
  BoundlessBPE et al., 2025) algorithms first induce regular BPE subword tokens by enforcing preto-kenization. They then run a second stage of BPE allowing merges across spaces and punctuation. The result is a large set of tokens that can be more efficient (Fig. 2.7).
  Figure 1: SuperBPE tokenizers encode text much more efficiently than BPE, and the gap grows with larger vocabulary size. Encoding efficiency (y-axis) is measured with bytes-per-token, the number of bytes encoded per token on average over a large corpus of text. In the above text with 40 bytes, SuperBPE uses 7 tokens and BPE uses 13, so the methods’ efficiencies are 40/7 = 5.7 and 40/13 = 3.1 bytes-per-token, respectively. In the graph, the encoding efficiency of BPE plateaus early due to exhausting the valuable whitespace-delimited words in the training data. In fact, it is bounded above by the gray dotted line, which shows the maximum achievable encoding efficiency with BPE, if every whitespace-delimited word were in the vocabulary. On the other hand, SuperBPE has dramatically better encoding efficiency that continues to improve with increased vocabulary size, as it can continue to add common word sequences to treat as tokens to the vocabulary. The different gradient lines show different transition points from learning subword to superword tokens, which always gives an immediate improvement. SuperBPE also has better encoding efficiency than a naive variant of BPE that does not use whitespace pretokenization at all.
  performing well on these languages. Including multi-word tokens promises to be beneficial in several ways: it can lead to shorter token sequences, lowering the computational costs of LM training and inference, and may also offer representational advantages by segmenting text into more semantically cohesive units (Salehi et al., 2015; Otani et al., 2020; Hofmann et al., 2021).
  In this work, we introduce a superword tokenization algorithm that produces a vocabulary of both subword and “superword” tokens, which we use to refer to tokens that bridge more than one word. Our method, SuperBPE, introduces a pretokenization curriculum to the popu-lar byte-pair encoding (BPE) algorithm (Sennrich et al., 2016): whitespace pretokenization is initially used to enforce learning of subword tokens only (as done in conventional BPE), but is disabled in a second stage, where the tokenizer transitions to learning superword tokens. Notably, SuperBPE tokenizers scale much better with vocabulary size—while BPE quickly hits a point of diminishing returns and begins adding increasingly rare subwords to the vocabulary, SuperBPE can continue to discover common word sequences to treat as single tokens and improve encoding efficiency (see Figure 1).
  In our main experiments, we pretrain English LMs at 8B scale from scratch. When fixing the model size, vocabulary size, and training compute—varying only the algorithm for learning the vocabulary—we find that models trained with SuperBPE tokenizers consistently and significantly improve over counterparts trained with a BPE tokenizer, while also being 27– 33% more efficient at inference time. Our best SuperBPE model achieves an average +4.0%
  Figure 2.7 The SuperBPE algorithm creating larger tokens by allowing a second stage of merging across spaces. Figure from Liu et al. (2025).
  Many of the tokenizers used in practice for large language models are multilin-gual, trained on many languages. But because the training data for large language models is vastly dominated by English text, these multilingual BPE tokenizers tend to use most of the tokens for English, leaving fewer of them for other languages. The result is that they do a better job of tokenizing English, and the other languages tend to get their words split up into shorter tokens. For example let’s look at a Spanish sentence from a recipe for plantains, together with an English translation.
  The English has 18 tokens; each of the 14 words is a token (none of the words are split into multiple tokens):
  By contrast, the original 16 words in Spanish have been encoded into 33 tokens, a much larger number. Notice that many b sic words have b en broken into pi ces. For example hondo, ‘deep’, has been segmented into h and ondo. Similarly for jugo, ‘juic ’, nuez, ‘nut’ and jenjibre ‘ginger’):
  Spanish is not a particularly low-resource language; this oversegmenting can be even more serious in lower resourc languages, often down o ndividual char cters. Oversegmenting into these tiny tokens can cause various problems for the down-stream processing of the language. As will become more clear once we introduce transformer m dels in Chapter 8, such fragmentation can lead to poor representa-tions of meaning, the need for longer contexts, and higher costs to train models (Rust et al., 2021; Ahia et al., 2023).
  2.5 Corpora
  Words don’t appear out of nowhere. Any particular piece of text that we study is produced by one or more specific speakers or writers, in a specific dialect of a
  18 CHAPTER 2 • WORDS AND TOKENS
  specific language, at a specific time, in a specific place, for a specific function. Perhaps the most important dimension of variation is the language. NLP algo-
  rithms are most useful when they apply across many languages. The world has 7097 languages at the time of this writing, according to the online Ethnologue catalog (Simons and Fennig, 2018). It is important to test algorithms on more than one lan-guage, and particularly on languages with different properties; by contrast there is an unfortunate current tendency for NLP algorithms to be developed or tested just on English (Bender, 2019). Even when algorithms are developed beyond English, they tend to be developed for the official languages of large industrialized nations (Chi-nese, Spanish, Japanese, German etc.), but we don’t want to limit tools to just these few languages. Furthermore, most languages also have multiple varieties, often spo-ken in different regions or by different social groups. Thus, for example, if we’re processing text that uses features of African American English (AAE) or AfricanAAE
  American Vernacular English (AAVE)—the variations of English that can be used by millions of people in African American communities (King 2020)—we must use NLP tools that function with features of those varieties. Twitter posts might use fea-tures often used by speakers of African American English, such as constructions like iont (I don’t in Mainstream American English (MAE)), or talmbout correspondingMAE
  to MAE talking about, both examples that influence word segmentation (Blodgett et al. 2016, Jones 2015).
  It’s also quite common for speakers or writers to use multiple languages in a sin-gle utterance, a phenomenon called code switching. Code switching is enormouslycode switching
  common across the world; here are examples showing Spanish and (transliterated) Hindi code switching with English (Solorio et al. 2014, Jurgens et al. 2017):
  (2.12) Por primera vez veo a @username actually being hateful! it was beautiful:) [For the first time I get to see @username actually being hateful! it was beautiful:) ]
  (2.13) dost tha or ra- hega ... dont wory ... but dherya rakhe [“he was and will remain a friend ... don’t worry ... but have faith”]
  Another dimension of variation is the genre. The text that our algorithms must process might come from newswire, fiction or non-fiction books, scientific articles, Wikipedia, or religious texts. It might come from spoken genres like telephone conversations, business meetings, police body-worn cameras, medical interviews, or transcripts of television shows or movies. It might come from work situations like doctors’ notes, legal text, or parliamentary or congressional proceedings.
  Text also reflects the demographic characteristics of the writer (or speaker): their age, gender, race, socioeconomic class can all influence the linguistic properties of the text we are processing.
  And finally, time matters too. Language changes over time, and for some lan-guages we have good corpora of texts from different historical periods.
  Because language is so situated, when developing computational models for lan-guage processing from a corpus, it’s important to consider who produced the lan-guage, in what context, for what purpose. How can a user of a dataset know all these details? The best way is for the corpus creator to build a datasheet (Gebru et al.,datasheet

2020. or data statement (Bender et al., 2021) for each corpus. A datasheet specifies properties of a dataset like:
      Motivation: Why was the corpus collected, by whom, and who funded it? Situation: When and in what situation was the text written/spoken? For example,
      was there a task? Was the language originally spoken conversation, edited text, social media communication, monologue vs. dialogue?
      2.6 • REGULAR EXPRESSIONS 19
      Language variety: What language (including dialect/region) was the corpus in? Speaker demographics: What was, e.g., the age or gender of the text’s authors? Collection process: How big is the data? If it is a subsample how was it sampled?
      Was the data collected with consent? How was the data pre-processed, and what metadata is available?
      Annotation process: What are the annotations, what are the demographics of the annotators, how were they trained, how was the data annotated?
      Distribution: Are there copyright or other intellectual property restrictions?
      2.6 Regular Expressions
      One of the most useful tools for text processing in computer science is the regular expression (or regex), a language for specifying text strings. Regexes are used inregular
      expression every computer language, in text processing tools like Unix grep, and in editors like vim or Emacs. And they play an important role in the pre-tokenization step for tokenization algorithms like BPE. Formally, a regular expression is an algebraic notation for characterizing a set of strings. Practically, we can use a regex to search for a string in a text and to specify how to change the string, both of which are key to tokenization.
      We use regular expressions to search for a pattern in a string which can be astring
      single line or a longer text. For example, the Python function re.search(pattern,string)
      scans through the string and returns the first match inside it for the pattern. In the following examples we generally highlight the exact string that matches the regular expression and show only the first match. We’ll use Python syntax, expressing the regex as a raw string delimited by double quotes: r"regex". Raw strings treat backslashes as literal characters, which will be important since many regex patterns we’ll introduce use backslashes.
      Regular expressions come in different variants, so using an online regex tester can help make sure your regex does what you think it’s doing.
      2.6.1 Character Disjunction: The Square Bracket The simplest kind of regular expression is a sequence of simple characters. The pat-tern r"Buttercup" matches the substring Buttercup in any string (like the string I’m called little Buttercup). But often we need to use special characters. For example, we might want to match either some character or another. For exam-ple, regular expressions are generally case sensitive: r"s" matches a lower case s
      but not an upper case S. To match both s and S we can use the character disjunc-tion operator, the square braces [ and ]. The string of characters inside the bracescharacter
      disjunction specifies a disjunction of characters to match. For example, Fig. 2.8 shows that the pattern r"[mM]" matches patterns containing either m or M.
      Pattern Match String r"[mM]ary" Mary or mary “Mary Ann stopped by Mona’s” r"[abc]" ‘a’, ‘b’, or ‘c’ “In uomini, in soldati” r"[1234567890]" any one digit “plenty of 7 to 5”
      Figure 2.8 The use of the brackets [] to specify a disjunction of characters.
      20 CHAPTER 2 • WORDS AND TOKENS
      The regular expression r"[1234567890]" specifies any single digit. This can get awkward (imagine typing r"[ABCDEFGHIJKLMNOPQRSTUVWXYZ]" to mean an uppercase letter) so the brackets can also be used with a dash (-) to specify any one character in a range. The pattern r"[2-5]" specifies any one of the characters 2, 3,range
      4, or 5. The pattern r"[b-g]" specifies one of the characters b, c, d, e, f, or g. Some other examples are shown in Fig. 2.9.
      Regex Match Example Patterns Matched r"[A-Z]" an upper case letter “we should call it ‘Drenched Blossoms’ ” r"[a-z]" a lower case letter “my beans were impatient to be hoed!” r"[0-9]" a single digit “Chapter 1: Down the Rabbit Hole”
      Figure 2.9 The use of the brackets [] plus the dash - to specify a range.
      The square braces can also be used to specify what a single character cannot be, by use of the caret ˆ. If the caret ˆ is the first symbol after the open square brace [, the resulting pattern is negated. For example, the pattern r"[ˆa]" matches any single character (including special characters) except a. This is only true when the caret is the first symbol after the open square brace. If it occurs anywhere else, it usually stands for a caret; Fig. 2.10 shows some examples.
      Regex Match (single characters) Example Patterns Matched r"[ˆA-Z]" not an upper case letter “Oyfn pripetchik” r"[ˆSs]" neither ‘S’ nor ‘s’ “I have no exquisite reason for’t” r"[ˆ.]" not a period “our resident Djinn” r"[eˆ]" either ‘e’ or ‘ˆ’ “look up ˆ now” r"aˆb" the pattern ‘aˆb’ “look up aˆ b now”
      Figure 2.10 The caret ˆ for negation or just to mean ˆ. See below re: the backslash for escaping the period.
      2.6.2 Counting, Optionality, and Wildcards How can we talk about optional elements, like an optional s if we want to match both koala and koalas? We can’t use the square brackets, because while they allow us to say “s or S”, they don’t allow us to say “s or nothing”. For this we use the question mark r"?", which means “the preceding character or nothing”,. So r"colou?r"
      matches both color and colour, and r"koalas?" matches koala or koalas. There’s another way to talk about elements that may or may not occur. Consider
      the language of certain sheep, which consists of strings that look like the following:
      This sheep language consists of strings with a b, followed by at least two (and arbitrarily more) a’s, followed by an exclamation point. To represent this language, we’ll use a useful operator that is represented by the asterisk or *, called the Kleene \* (generally pronounced “cleany star”). The Kleene star means “zero or more oc-Kleene \*
      currences of the immediately previous character or regular expression”. So r"a*"
      means “any string of zero or more as”. Could r"ba\*" represent the sheep language? It will correctly match ba or
      baaaaaa, but there’s a problem! It will also match b, with no a, or ba with only one
      2.6 • REGULAR EXPRESSIONS 21
      a. That’s because Kleene star means “zero or more occurrences”. Instead, for the sheep language we’ll want r"baaa\*", meaning b followed by aa followed by zero or more additional as. More complex patterns can also be repeated. So r"[ab]*"
      means “zero or more a’s or b’s” (not “zero or more right square braces”). This will match strings like aaaa or ababab or bbbb, as well as the empty string. For speci-fying an integer (a string of digits) we can use r"[0-9][0-9] *". (Why isn’t it just r"[0-9]* "?)
      There is a slightly shorter way to specify “at least one” of some character: the Kleene +, which means “one or more occurrences of the immediately precedingKleene +
      character or regular expression”. So r"[0-9]+" is the normal way to specify “a sequence of digits”, and we could also specify the sheep language as r"baa+!".
      Besides the Kleene \* and Kleene + we can also use explicit numbers as coun-ters, by enclosing them in curly brackets. The operator r"{3}" means “exactly 3 occurrences of the previous character or expression”. So r"ax{10}z" will match a
      followed by exactly 10 x’s followed by z. An important special character is the period (r"."), a wildcard expression thatperiod
      matches any single character (except a newline). The wildcard is often used together with the Kleene star to mean “any string
      of characters”. For example, suppose we want to find any line in which a particu-lar word, for example, rose, appears twice. We can specify this with the regular expression r"rose.*rose", meaning two roses, with a sequence of zero or more characters (of any kind) between them. Fig. 2.11 summarizes.
      Regex Match \* zero or more occurrences of the previous char or expression + one or more occurrences of the previous char or expression ? zero or one occurrence of the previous char or expression {n} exactly n occurrences of the previous char or expression . any single char .* any string of zero or more chars
      Figure 2.11 Counting and wildcards.
      2.6.3 Anchors and Boundaries Anchors are special characters that anchor regular expressions to particular placesanchors
      in a string. The most common anchors are the caret ˆ and the dollar sign $. The caret ˆ matches the start of a line. The pattern r"ˆThe" matches the word The only at the start of a line. Thus, the caret ˆ has three uses: to match the start of a line, to indicate a negation inside of square brackets, and just to mean a caret. (What are the contexts that allow the system to know which function a given caret is supposed to have?) The dollar sign $ matches the end of a line. So the pattern $is a useful pattern for matching a space at the end of a line, and r"ˆThe dog\.$ " matches a line that contains only the phrase The dog. with a final period.
      Note that we have to use the backslash in the prior example since we want the . to mean “period” and not the wildcard. By contrast, the regular expression r"ˆThe dog.$" would match The dog. but also The dog! and The dogo. As we’ll discuss below, all the special characters we’ve defined so far (* + ? . [
      ]) need to be backslashed when we mean to use them literally. There are other anchors: \b matches a word boundary, and \B matches a non
      word-boundary. Thus, r"\bthe\b" matches the word the but not the word other.
      22 CHAPTER 2 • WORDS AND TOKENS
      Regex Match ˆ start of line $ end of line \b word boundary \B non-word boundary
      Figure 2.12 Anchors in regular expressions.
      A “word” for the purposes of a regex is defined (based on words in programming languages) as a sequence of digits, underscores, or letters. Thus r"\b99\b" will match the string 99 in There are 99 bottles of beer on the wall (because 99 follows a space) but not 99 in There are 299 bottles of beer on the
      wall (since 99 follows a number). But it will match 99 in $99 (since 99 follows a dollar sign ($ ), which is not a digit, underscore, or letter).
      Note that all these anchors and boundary operators technically match the empty string, meaning that they don’t eat up any characters of the string. The carat in the pattern r"ˆThe" matches the start of "The" but doesn’t actually advance over the first character T. And the pattern r"the\b the" matches the the; the \b is aware of the fact that the space is a boundary, but it matches the empty string right before the space, not the space, so that the space character is available to be matched.
      2.6.4 Disjunction, Grouping, and Precedence Suppose we need to search for texts about pets; perhaps we are particularly interested in cats and dogs. In such a case, we might want to search for either the string cat or the string dog. Since we can’t use the square brackets to search for “cat or dog” (why wouldn’t r"[catdog]" do the right thing?), we need a new operator, the disjunction operator, also called the pipe symbol |. The pattern r"cat|dog"disjunction
      matches either the string cat or the string dog. Sometimes we need to use this disjunction operator in the midst of a larger se-
      quence. For example, suppose I want to search for mentions of pet fish. How can I specify both guppy and guppies? We cannot simply say r"guppy|ies", because that would match only the strings guppy and ies. This is because sequences like guppy take precedence over the disjunction operator |. To make the disjunctionprecedence
      operator apply only to a specific pattern, we need to use the parenthesis operators ( and ). Enclosing a pattern in parentheses makes it act like a single character for the purposes of neighboring operators like the pipe | and the Kleene\*. So the pattern r"gupp(y|ies)" would specify that we meant the disjunction only to apply to the suffixes y and ies.
      The parenthesis operator ( is also useful when we are using counters like the Kleene\*. Unlike the | operator, the Kleene\* operator applies by default only to a single character, not to a whole sequence. Suppose we want to match repeated instances of a string. Perhaps we have a line that has column labels of the form Column 1 Column 2 Column 3. The expression r"Column [0-9]+ *" will not match any number of columns; instead, it will match a single column followed by any number of spaces! The star here applies only to the space that precedes it, not to the whole sequence. With the parentheses, we could write the expression r"(Column [0-9]+ +)* " to match the word Column, followed by a number and spaces, the whole pattern repeated zero or more times.
      This idea that one operator may take precedence over another, requiring us to sometimes use parentheses to specify what we mean, is formalized by the operator precedence hierarchy for regular expressions. The following table gives the orderoperator
      2.6 • REGULAR EXPRESSIONS 23
      of operator precedence, from highest precedence to lowest precedence.
      Parenthesis ()
      Counters \* + ? {}
      Sequences and anchors the ˆmy end$
      Disjunction |
      Thus, because counters have a higher precedence than sequences, r"the\*" matches theeeee but not thethe. Because sequences have a higher prece-dence than disjunction, r"the|any" matches the or any but not thany or theny.
      Patterns can be ambiguous in another way. Consider the expression r"[a-z]\*"
      when matching against the text once upon a time. Since r"[a-z]\*" matches zero or more letters, this expression could match nothing, or just the first letter o, on, onc, or once. In these cases regular expressions always match the largest string they can; we say that patterns are greedy, expanding to cover as much of a string as they can.greedy
      There are, however, ways to enforce non-greedy matching, using another mean-non-greedy
      ing of the ? qualifier. The operator \*? is a Kleene star that matches as little text as\* ?
      possible. The operator +? is a Kleene plus that matches as little text as possible.+?
      2.6.5 A Simple Example Suppose we wanted to write a regex to find cases of the English article the. A simple (but incorrect) pattern might be:
      r"the" (2.14)
      One problem is that this pattern will miss the word when it begins a sentence and hence is capitalized (i.e., The). This might lead us to the following pattern:
      r"[tT]he" (2.15)
      But we will still overgeneralize, incorrectly return texts with the embedded in other words (e.g., other or there). So we need to specify that we want instances with a word boundary on both sides:
      r"\b[tT]he\b" (2.16)
      The simple process we just went through was based on fixing two kinds of errors: false positives, strings that we incorrectly matched like other or there, and falsefalse positives
      negatives, strings that we incorrectly missed, like The. Addressing these two kindsfalse negatives
      of errors comes up again and again in language processing. Reducing the overall error rate for an application thus involves two antagonistic efforts:
      Increasing precision (minimizing false positives)
      Increasing recall (minimizing false negatives)
      We’ll come back to precision and recall with more precise definitions in Chapter 4.
      2.6.6 More Operators Figure 2.13 shows some useful aliases for common ranges:
      Finally, certain special characters are referred to by special notation based on the backslash () (see Fig. 2.14). The most common of these are the newline characternewline
      \n and the tab character \t.
      24 CHAPTER 2 • WORDS AND TOKENS
      Regex Expansion Match First Matches \d [0-9] any digit Party of 5 \D [ˆ0-9] any non-digit Blue moon \w [a-zA-Z0-9\_] any alphanumeric/underscore Daiyu \W [ˆ\w] a non-alphanumeric !!!! \s [ \r\t\n\f] whitespace (space, tab) in Concord \S [ˆ\s] Non-whitespace in Concord
      Figure 2.13 Aliases for common sets of characters.
      How do we refer to characters that are special themselves (like ., \*, -, [, and ) when we mean them literally, not in their special usage? That is, if we are trying to match a period, or a star, or a bracket or paren? To get the literal meaning of a special character, we need to precede them with a backslash, (i.e., r".", r"\*", r"[", and r"\").
      Regex Match First Patterns Matched \* an asterisk “ \*” “K\* A \*P\* L \*A\* N” . a period “.” “Dr. Livingston, I presume” ? a question mark “Why don’t they come and lend a hand?” \n a newline \t a tab
      Figure 2.14 Some characters that need to be escaped (via backslash).
      2.6.7 Substitutions and Capture Groups An important use of regular expressions is in substitutions, where we want to re-substitution
      place one string with another. Regular expression can help us specify the string to be replaced as well as the replacement. In Python we use the function re.sub()
      (similar functions exist in other languages and environments). re.sub(pattern, repl, string) takes three arguments: a pattern to search for, a
      replacement to replace it with, and a string in which to do the search and replacing We could for example change every instance of cherry to apricot in string:
      re.sub(r"cherry", r"apricot", string)
      Or we could convert to upper case all the instances of a particular name:
      re.sub(r"janet", r"Janet", string)
      More often, however, the substitution depends in a more complex way on the string that matched the pattern. For example, suppose we have a document in which all the dates are in US format (mm/dd/yyyy) and we want to change them into the format used in the EU and many other regions: (dd-mm-yyyy). The pat-tern r"\d{2}/\d{2}/\d{4}" will match a date. But how do we specify in the replacement that we want to swap the date and month values?
      The tool in regular expression for this is the capture group. A capture groupcapture group
      uses parentheses to capture (store) the values that we matched in the search, so we can reuse them in the replacement. We put a set of parentheses around the part of the pattern we want to capture, and it will get stored in a numbered group (groups are numbered from left to right). Then in the repl, we refer back to that group with a number command.
      Consider the following expression:
      2.6 • REGULAR EXPRESSIONS 25
      re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\2-\1-\3", string)}
      We’ve put parentheses ( and ) around the two month digits, the two day digits, and the four year digits, thus storing the first 2 digits in group 1, the second 2 digits in group 2, and the final digits in group 3. Then in the repl string, we use number operators \1, \2, and \3, to refer back to the first, second, and third registers. The result would take a string like
      The date is 10/15/2011
      and convert it to
      The date is 15-10-2011
      Capture groups can be useful even if we are not doing substitutions. For example we can use them to find repetitions, something we often need in text processing. For example, to find a repeated word in a string, we can use this pattern which searches for a word, captures it in a group, and then refers back to it after whitespace:
      r"\b([A-Za-z]+)\s+\1\b"
      Parentheses thus have a double function in regular expressions; they are used to group terms for specifying the order in which operators should apply, and they are used to capture the match. Occasionally we need parentheses for grouping, but don’t want to capture the resulting pattern. In that case we use a non-capturing group,non-capturing
      group which is specified by putting the special commands ?: after the open parenthesis, in the form (?: pattern ). Non-capture groups are usually used when we are trying to capture only part of a long or complex pattern. Perhaps we are matching a sequence of dates (\d\d/\d\d/\d\d\d\d) separated by spaces and we want to extract only the 15th one. We need to use parenthesis in order to use the counting operator on the first 14, but we don’t want to store all the useless information. The following pattern only stores the 15th date in group 1:
      r"(?:\d\d/\d\d/\d\d\d\d\s+){14}(\d\d/\d\d/\d\d\d\d)" (2.17)
      Substitutions and capture groups are also useful for implementing historically important chatbots like ELIZA (Weizenbaum, 1966). Recall that ELIZA simulates a Rogerian psychologist by carrying on conversations like the following:
      User2: They’re always bugging us about something or other. ELIZA2: CAN YOU THINK OF A SPECIFIC EXAMPLE User3: Well, my boyfriend made me come here. ELIZA3: YOUR BOYFRIEND MADE YOU COME HERE User4: He says I’m depressed much of the time. ELIZA4: I AM SORRY TO HEAR YOU ARE DEPRESSED
      ELIZA works by having a series or cascade of regex substitutions each of which matches and changes some part of the input lines. After the input is uppercased, substitutions change all instances of MY to YOUR, and I’M to YOU ARE, and so on. That way when ELIZA repeats back part of the user utterance, it will seem to be referring correctly to the user. The next set of substitutions matches and replaces other patterns in the input, turning the input into a complete response. Here are some examples:
      re.sub(r".\* YOU ARE (DEPRESSED|SAD) .\*",r"I AM SORRY TO HEAR YOU ARE \1",input)
      re.sub(r".\* YOU ARE (DEPRESSED|SAD) .\*",r"WHY DO YOU THINK YOU ARE \1",input)
      re.sub(r".\* ALWAYS .\*",r"CAN YOU THINK OF A SPECIFIC EXAMPLE",input)
      26 CHAPTER 2 • WORDS AND TOKENS
      2.6.8 Lookahead Assertions Finally, there will be times when we need to predict the future: look ahead in the text to see if some pattern matches, but not yet advance the pointer we always keep to where we are in the text, so that we can then deal with the pattern if it occurs, but if it doesn’t we can check for something else instead.
      These lookahead assertions make use of the (? syntax that we saw in the previ-lookahead
      ous section for non-capture groups. The operator (?= pattern) is true if pattern occurs, but is zero-width, i.e. the match pointer doesn’t advance, just as we sawzero-width
      with anchors and boundary markers like \b. The operator (?! pattern) only re-turns true if a pattern does not match, but again is zero-width and doesn’t advance the pointer. Negative lookahead is commonly used when we are parsing some com-plex pattern but want to rule out a special case. For example suppose we want to capture the first word on the line, but only if it doesn’t start with the letter T. We can use negative lookahead to do this:
      r"ˆ(?![tT])(\w+)\b" (2.18)
      The first negative lookahead says that the line must not start with a t or T, but matches the empty string, not moving the match pointer. Then the capture group captures the first word.
      2.6.9 Regular Expressions for BPE pre-tokenization
      import regex as re
      pat = re.compile(
      ... # Contractions: ’t and ’m are tokens
      ... r"’s|’t|’re|’ve|’m|’ll|’d|"
      ... # Words: sequence of Unicode letters (after optional space)
      ... r" ?\p{L}+|"
      ... #Number: sequence of digits (after optional space)
      ... r" ?\p{N}+|"
      ... # Punctuation: sequence of non-alphanumeric/non-space
      ... #(after optional space)
      ... r" ?[ˆ\s\p{L}\p{N}]+|"
      ... # whitespace
      ... r"\s+(?!\S)|\s+"
      text = "We’re 350 dogs! Um, lunch?"
      print(pat.findall(text))
      [’We’, "’re", ’ 350’, ’ dogs’, ’!’, ’ Um’, ’,’, ’ lunch’, ’?’]
      Figure 2.15 The GPT-2 pre-tokenizer regular expression, used to split (roughly) on white-space before running the BPE algorithm.
      We described in Section 2.4 how before we run a BPE tokenization algorithm on a corpus we first pre-tokenize, splitting the corpus roughly by whitespace. Then the BPE tokenization algorithm builds up tokens from sequences of characters inside words and doesn’t tokenize across word boundaries.
      Here’s the regular expression used to do this pretokenization that is used for one influential language model, the GPT-2 language model (Radford et al., 2019):
      2.7 • SIMPLE UNIX TOOLS FOR WORD TOKENIZATION 27
      r"’s|’t|’re|’ve|’m|’ll|’d| ?\p{L}+| ?\p{N}+| ?[ˆ\s\p{L}\p{N}]+|\s+(?!\S)|\s+"
      This is quite a complex regular expression, and also makes use of some advanced Unicode-related features we haven’t described yet. These features are part of a pop-ular external Python 3 library called regex (which is more powerful than the internal Python 3 library called re).
      For example the regex library has special \p and \P operators that can match if the current character has particular Unicode codepoint properties. For example \p{L} matches any Unicode letter, \P{L} matches any non-letter, \p{N} matches any number, and \P{N} matches any non-number.
      Fig. 2.15 annotates the regular expression more clearly, and also shows the output of running the GPT-2 tokenizer on the sentence We’re 350 dogs! Um,
      lunch?. Note that the tokenizer splits We’re into We and ’re, that punctuation is split
      off from dogs and lunch, and that some tokens like dogs start with a space, and others like We and ! do not.
      2.7 Simple Unix Tools for Word Tokenization
      For English it is possible to do simple naive word tokenization and frequency com-putation in a single Unix command-line. As Church (1994) points out, this can be useful when we need quick information about a text corpus. We’ll make use of some Unix commands: tr, used to systematically change particular characters in the in-put; sort, which sorts input lines in alphabetical order; and uniq, which collapses and counts adjacent identical lines.
      For example let’s begin with the ‘complete words’ of Shakespeare in one file, sh.txt. We can use tr to tokenize the words by changing every sequence of non-alphabetic characters to a newline (’A-Za-z’ means alphabetic and the -c option complements to non-alphabet, so together they mean to change every non-alphabetic character into a newline. The -s (‘squeeze’) option is used to replace the result of multiple consecutive changes into a single output, so a series of non-alphabetic characters in a row would all be ‘squeezed’ into a single newline):
      tr -sc ’A-Za-z’ ’\n’ < sh.txt
      The output of this command will be:
      Shakespeare
      Now that there is one word per line, we can sort the lines, and pass them to uniq
      -c which will collapse and count them:
      tr -sc ’A-Za-z’ ’\n’ < sh.txt | sort | uniq -c
      with the following output:
      28 CHAPTER 2 • WORDS AND TOKENS
      Alternatively, we can collapse all the upper case to lower case:
      tr -sc ’A-Za-z’ ’\n’ < sh.txt | tr A-Z a-z | sort | uniq -c
      whose output is
      1 abaissiez
      2 abandoned
      Now we can sort again to find the frequent words. The -n option to sort means to sort numerically rather than alphabetically, and the -r option means to sort in reverse order (highest-to-lowest):
      tr -sc ’A-Za-z’ ’\n’ < sh.txt | tr A-Z a-z | sort | uniq -c | sort -n -r
      The results show that the most frequent words in Shakespeare, as in any other corpus, are the short function words like articles, pronouns, prepositions:
      Unix tools of this sort can be very handy in building quick word count statistics for any corpus in English. For anything more complex, we generally turn to the more sophisticated tokenization algorithms we’ve discussed above.
      2.8 Rule-based tokenization
      While data-based tokenization like BPE is the most common way of doing tokeniza-tion, there are also situations where we want to constrain our tokens to be words and not subwords. This might be useful if we are running parsing algorithms for English where the parser might need grammatical words as input. Or it can be useful for any linguistic application where we have some a prior definition of the token that we
      2.8 • RULE-BASED TOKENIZATION 29
      are interested in studying. Or it can be useful for social science applications where orthographic words are useful domains of study.
      In rule-based tokenization, we pre-define a standard and implement rules to im-plement that kind of tokenization. Let’s explore this for English word tokenization.
      We have some desiderata for English. We often want to break off punctua-tion as a separate token; commas are a useful piece of information for parsers, and periods help indicate sentence boundaries. But we’ll often want to keep the punctuation that occurs word internally, in examples like m.p.h., Ph.D., AT&T, and cap’n. Special characters and numbers will need to be kept in prices ($45.55) and dates (01/02/06); we don’t want to segment that price into separate tokens of “45” and “55”. And there are URLs (https://www.stanford.edu), Twitter hashtags (#nlproc), or email addresses (someone@cs.colorado.edu).
      Number expressions introduce complications; in addition to appearing at word boundaries, commas appear inside numbers in English, every three digits: 555,500.50. Tokenization differs by language; languages like Spanish, French, and German, for example, use a comma to mark the decimal point, and spaces (or sometimes periods) where English puts commas, for example, 555 500,50.
      A rule-based tokenizer can also be used to expand clitic contractions that areclitic
      marked by apostrophes, converting what’re to the two tokens what are, and we’re to we are. A clitic is a part of a word that can’t stand on its own, and can only oc-cur when it is attached to another word. Such contractions occur in other alphabetic languages, including French pronouns (j’ai and articles l’homme).
      Depending on the application, tokenization algorithms may also tokenize mul-tiword expressions like New York or rock ’n’ roll as a single token, which re-quires a multiword expression dictionary of some sort. Rule-based tokenization is thus intimately tied up with named entity recognition, the task of detecting names, dates, and organizations (Chapter 17).
      One commonly used tokenization standard is known as the Penn Treebank to-kenization standard, used for the parsed corpora (treebanks) released by the Lin-Penn Treebank
      tokenization guistic Data Consortium (LDC), the source of many useful datasets. This standard separates out clitics (doesn’t becomes does plus n’t), keeps hyphenated words to-gether, and separates out all punctuation (to save space we’re showing visible spaces ‘ ’ between tokens, although newlines is a more common output):
      Input: "The San Francisco-based restaurant," they said,
      "doesn’t charge $10".
      Output: " The San Francisco-based restaurant , " they said ,
      " does n’t charge $ 10 " .
      In practice, since tokenization is run before any other language processing, it needs to be very fast. For rule-based word tokenization we generally use deter-ministic algorithms based on regular expressions compiled into efficient finite state automata. For example, Fig. 2.16 shows a basic regular expression that can be used to tokenize English with the nltk.regexp tokenize function of the Python-based Natural Language Toolkit (NLTK) (Bird et al. 2009; https://www.nltk.org).
      Carefully designed deterministic algorithms can deal with the ambiguities that arise, such as the fact that the apostrophe needs to be tokenized differently when used as a genitive marker (as in the book’s cover), a quotative as in ‘The other class’, she said, or in clitics like they’re.
      30 CHAPTER 2 • WORDS AND TOKENS
      text = ’That U.S.A. poster-print costs $12.40...’
      pattern = r’’’(?x) # set flag to allow verbose regexps
      ... (?:[A-Z].)+ # abbreviations, e.g. U.S.A.
      ... | \w+(?:-\w+)\* # words with optional internal hyphens
      ... | $?\d+(?:.\d+)?%? # currency, percentages, e.g. $12.40, 82%
      ... | ... # ellipsis
      ... | [][.,;"’?():\_‘-] # these are separate tokens; includes ], [
      nltk.regexp\_tokenize(text, pattern)
      [’That’, ’U.S.A.’, ’poster-print’, ’costs’, ’$12.40’, ’...’]
      Figure 2.16 A Python trace of regular expression tokenization in the NLTK Python-based natural language processing toolkit (Bird et al., 2009), commented for readability; the (?x)
      verbose flag tells Python to strip comments and whitespace. Figure from Chapter 3 of Bird et al. (2009).
      2.8.1 Sentence Segmentation Rule-based segmentation is commonly used for another kind of tokenization pro-cess: the sentence. Sentence segmentation is a step that is can be optionally appliedsentence
      segmentation in text processing. It is especially important when applying NLP algorithms to tasks of detecting structure, like parse structure.
      Sentence segmentation depends on the language and the genre. The most useful cues for segmenting a text into sentences in English written text tend to be punc-tuation, like periods, question marks, and exclamation points. Question marks and exclamation points are relatively unambiguous markers of sentence boundaries, and simple rules can segment sentences when they appear.
      The period character “.”, on the other hand, is ambiguous between a sentence boundary marker and a marker of abbreviations like Dr. or Inc. The previous sen-tence that you just read showed an even more complex case of this ambiguity, in which the final period of Inc. marked both an abbreviation and the sentence bound-ary marker. For this reason, sentence tokenization and word tokenization can be addressed jointly.
      Many English sentence tokenization methods work by first deciding (often based on deterministic rules, but sometimes via machine learning) whether a period is part of the word or is a sentence-boundary marker. An abbreviation dictionary can help determine whether the period is part of a commonly used abbreviation; the dictio-naries can be hand-built or machine-learned (Kiss and Strunk, 2006), as can the final sentence splitter. In the Stanford CoreNLP toolkit (Manning et al., 2014), for exam-ple sentence splitting is rule-based, a deterministic consequence of tokenization; a sentence ends when a sentence-ending punctuation (., !, or ?) is not already grouped with other characters into a token (such as for an abbreviation or number), optionally followed by additional final quotes or brackets.
      2.9 Minimum Edit Distance
      We often need a way to compare how similar two words or strings are. As we’ll see in later chapters, this comes up most commonly in tasks like automatic speech recognition or machine translation, where we want to know how similar the sequence
      2.9 • MINIMUM EDIT DISTANCE 31
      of words is to some reference sequence of words. Edit distance gives us a way to quantify these intuitions about string similarity.
      More formally, the minimum edit distance between two strings is defined as theminimum edit distance
      minimum number of editing operations (operations like insertion, deletion, substitu-tion) needed to transform one string into another. In this section we’ll introduce edit distance for single words, but the algorithm applies equally to entire strings.
      The gap between intention and execution, for example, is 5 (delete an i, substi-tute e for n, substitute x for t, insert c, substitute u for n). It’s much easier to see this by looking at the most important visualization for string distances, an alignmentalignment
      between the two strings, shown in Fig. 2.17. Given two sequences, an alignment is a correspondence between substrings of the two sequences. Thus, we say I aligns with the empty string, N with E, and so on. Beneath the aligned strings is another representation; a series of symbols expressing an operation list for converting the top string into the bottom string: d for deletion, s for substitution, i for insertion.
      I N T E \* N T I O N
      | | | | | | | | | | \* E X E C U T I O N
      Figure 2.17 Representing the minimum edit distance between two strings as an alignment. The final row gives the operation list for converting the top string into the bottom string: d for deletion, s for substitution, i for insertion.
      We can also assign a particular cost or weight to each of these operations. The Levenshtein distance between two sequences is the simplest weighting factor in which each of the three operations has a cost of 1 (Levenshtein, 1966)—we assume that the substitution of a letter for itself, for example, t for t, has zero cost. The Lev-enshtein distance between intention and execution is 5. Levenshtein also proposed an alternative version of his metric in which each insertion or deletion has a cost of 1 and substitutions are not allowed. (This is equivalent to allowing substitution, but giving each substitution a cost of 2 since any substitution can be represented by one insertion and one deletion). Using this version, the Levenshtein distance between intention and execution is 8.
      2.9.1 The Minimum Edit Distance Algorithm How do we find the minimum edit distance? We can think of this as a search task, in which we are searching for the shortest path—a sequence of edits—from one string to another.
      n t e n t i o n i n t e c n t i o n i n x e n t i o n
      del ins subst
      i n t e n t i o n
      Figure 2.18 Finding the edit distance viewed as a search problem
      The space of all possible edits is enormous, so we can’t search naively. However, lots of distinct edit paths will end up in the same state (string), so rather than recom-puting all those paths, we could just remember the shortest path to a state each time
      32 CHAPTER 2 • WORDS AND TOKENS
      we saw it. We can do this by using dynamic programming. Dynamic programmingdynamic programming
      is the name for a class of algorithms, first introduced by Bellman (1957), that apply a table-driven method to solve problems by combining solutions to subproblems. Some of the most commonly used algorithms in natural language processing make use of dynamic programming, such as the Viterbi algorithm (Chapter 17) and the CKY algorithm for parsing (Chapter 18).
      The intuition of a dynamic programming problem is that a large problem can be solved by properly combining the solutions to various subproblems. Consider the shortest path of transformed words that represents the minimum edit distance between the strings intention and execution shown in Fig. 2.19.
      n t e n t i o n
      i n t e n t i o n
      e t e n t i o n
      e x e n t i o n
      e x e n u t i o n
      e x e c u t i o n
      substitute n by e
      substitute t by x
      substitute n by c
      Figure 2.19 Path from intention to execution.
      Imagine some string (perhaps it is exention) that is in this optimal path (whatever it is). The intuition of dynamic programming is that if exention is in the optimal operation list, then the optimal sequence must also include the optimal path from intention to exention. Why? If there were a shorter path from intention to exention, then we could use it instead, resulting in a shorter overall path, and the optimal sequence wouldn’t be optimal, thus leading to a contradiction.
      The minimum edit distance algorithm was named by Wagner and Fischer minimum edit
      distance algorithm
      (1974) but independently discovered by many people (see the Historical Notes sec-tion of Chapter 17).
      Let’s first define the minimum edit distance between two strings. Given two strings, the source string X of length n, and target string Y of length m, we’ll define
      j] as the edit distance between X
      j], i.e., the first i characters of X and the first j characters of Y . The edit distance between X and Y is thus
      We’ll use dynamic programming to compute
      bottom up, combining so-lutions to subproblems. In the base case, with a source substring of length i but an empty target string, going from i characters to 0 requires i deletes. With a target substring of length j but an empty source going from 0 characters to j characters requires j inserts. Having computed
      j] for small
      j we then compute larger
      j] based on previously computed smaller values. The value of
      j] is com-puted by taking the minimum of the three possible paths through the matrix which arrive there:
      j]+del-cost(source[i])
      j−1]+ ins-cost(target[ j])
      sub-cost(source[i],
      target[ j])
      We mentioned above two versions of Levenshtein distance, one in which substitu-tions cost 1 and one in which substitutions cost 2 (i.e., are equivalent to an insertion plus a deletion). Let’s here use that second version of Levenshtein distance in which the insertions and deletions each have a cost of 1 (ins-cost(·) = del-cost(·) = 1), and
      2.9 • MINIMUM EDIT DISTANCE 33
      substitutions have a cost of 2 (except substitution of identical letters has zero cost). Under this version of Levenshtein, the computation for
      j] becomes:
      2; if source[i] 6= target[ j] 0; if source[i] = target[ j]
      The algorithm is summarized in Fig. 2.20; Fig. 2.21 shows the results of applying the algorithm to the distance between intention and execution with the version of Levenshtein in Eq. 2.20.
      function MIN-EDIT-DISTANCE(source, target) returns min-distance
      n←LENGTH(source) m←LENGTH(target)
      Create a distance matrix D[n+1,m+1]

### Initialization: the zeroth row and column is the distance from the empty string D[0,0] = 0 for each row i from 1 to n do

D[i,0]←D[i-1,0]

* del-cost(source[i]) for each column j from 1 to m do
  D[0,j]←D[0,
  j-1] + ins-cost(target[j])

### Recurrence relation: for each row i from 1 to n do

for each column j from 1 to m do D[i,
D[i−1, j] + del-cost(source[i]),
D[i−1, j−1] + sub-cost(source[i], target[j]), D[i, j−1] + ins-cost(target[j]))

### Termination return D[n,m]

Figure 2.20 The minimum edit distance algorithm, an example of the class of dynamic programming algorithms. The various costs can either be fixed (e.g.,
ins-cost(x) = 1) or can be specific to the letter (to model the fact that some letters are more likely to be in-serted than others). We assume that there is no cost for substituting a letter for itself (i.e.,
sub-cost(x,x)
Alignment Knowing the minimum edit distance is useful for algorithms like find-ing potential spelling error corrections. But the edit distance algorithm is important in another way; with a small change, it can also provide the minimum cost align-ment between two strings. Aligning two strings is useful throughout speech and language processing. In speech recognition, minimum edit distance alignment is used to compute the word error rate (Chapter 15). Alignment plays a role in ma-chine translation, in which sentences in a parallel corpus (a corpus with a text in two languages) need to be matched to each other.
To extend the edit distance algorithm to produce an alignment, we can start by visualizing an alignment as a path through the edit distance matrix. Figure 2.22 shows this path with boldfaced cells. Each boldfaced cell represents an alignment of a pair of letters in the two strings. If two boldfaced cells occur in the same row,
34 CHAPTER 2 • WORDS AND TOKENS
Src\Tar # e x e c u t i o n # 0 1 2 3 4 5 6 7 8 9 i 1 2 3 4 5 6 7 6 7 8
n 2 3 4 5 6 7 8 7 8 7 t 3 4 5 6 7 8 7 8 9 8 e 4 3 4 5 6 7 8 9 10 9 n 5 4 5 6 7 8 9 10 11 10 t 6 5 6 7 8 9 8 9 10 11 i 7 6 7 8 9 10 9 8 9 10 o 8 7 8 9 10 11 10 9 8 9 n 9 8 9 10 11 12 11 10 9 8
Figure 2.21 Computation of minimum edit distance between intention and execution with the algorithm of Fig. 2.20, using Levenshtein distance with cost of 1 for insertions or dele-tions, 2 for substitutions.
there will be an insertion in going from the source to the target; two boldfaced cells in the same column indicate a deletion.
Figure 2.22 also shows the intuition of how to compute this alignment path. The computation proceeds in two steps. In the first step, we augment the minimum edit distance algorithm to store backpointers in each cell. The backpointer from a cell points to the previous cell (or cells) that we came from in entering the current cell. We’ve shown a schematic of these backpointers in Fig. 2.22. Some cells have mul-tiple backpointers because the minimum extension could have come from multiple previous cells. In the second step, we perform a backtrace. In a backtrace, we startbacktrace
from the last cell (at the final row and column), and follow the pointers back through the dynamic programming matrix. Each complete path between the final cell and the initial cell is a minimum distance alignment. Exercise 2.7 asks you to modify the minimum edit distance algorithm to store the pointers and compute the backtrace to output an alignment.

### e x e c u t i o n # 0

Figure 2.22 When entering a value in each cell, we mark which of the three neighboring cells we came from with up to three arrows. After the table is full we compute an alignment (minimum edit path) by using a backtrace, starting at the 8 in the lower-right corner and following the arrows back. The sequence of bold cells represents one possible minimum cost alignment between the two strings, again using Levenshtein distance with cost of 1 for insertions or deletions, 2 for substitutions. Diagram design after Gusfield (1997).
While we worked our example with simple Levenshtein distance, the algorithm in Fig. 2.20 allows arbitrary weights on the operations. For spelling correction, for example, substitutions are more likely to happen between letters that are next to
2.10 • SUMMARY 35
each other on the keyboard. The Viterbi algorithm is a probabilistic extension of minimum edit distance. Instead of computing the “minimum edit distance” between two strings, Viterbi computes the “maximum probability alignment” of one string with another. We’ll discuss this more in Chapter 17.
2.10 Summary
This chapter introduced the fundamental concepts of tokens and tokenization in lan-guage processing. We discussed the linguistic levels of words, morphemes, and characters, introduced Unicode code points and the UTF-8 encoding, introduced the BPE algorithm for tokenization, and introduced the regular expression and the minimum edit distance algorithm for comparing strings. Here’s a summary of the main points we covered about these ideas:
Words and morphemes are useful units of representation, but difficult to define formally.
Unicode is a system for representing characters in the many scripts used to write the languages of the world.
Each character is represented internally with a unique id called a code point, and can be encoded in a file via encoding methods like UTF-8, which is a variable-length encoding.
Byte-Pair Encoding or BPE is the standard way to induce tokens in a data-driven way. It is the first step in most large language models.
BPE tokens are often roughly word or morpheme-sized, although they can be as small as single characters.
The regular expression language is a powerful tool for pattern-matching.
Basic operations in regular expressions include disjunction of symbols ([], |), counters (\*, +, and {n,m}), anchors (ˆ, $), capture groups ((,)), and substitutions.
The minimum edit distance between two strings is the minimum number of operations it takes to edit one into the other. Minimum edit distance can be computed by dynamic programming, which also results in an alignment of the two strings.
Historical Notes
For more on Herdan’s law and Heaps’ Law, see Herdan (1960, p. 28), Heaps (1978), Egghe (2007) and Baayen (2001);
Unicode drew on ASCII and ISO character encoding standards. Early drafts were worked out in discussions between engineers from Xerox and Apple. An early draft standard was published in 1988, with a more formal release of the Unicode Stanford in 1991. What became UTF-8 began with ISO drafts in 1989, with various extensions. The self-synchronizing aspects were famously outlined on a placemat in a New Jersey dinner in 1992 by Ken Thompson.
Word tokenization and other text normalization algorithms have been applied since the beginning of the field. This include stemming, like the widely used stem-mer of Lovins (1968), and applications to the digital humanities like those of by Packard (1973), who built an affix-stripping morphological parser for Ancient Greek.
36 CHAPTER 2 • WORDS AND TOKENS
BPE, originally a text compression method proposed by Gage (1994), was applied to subword tokenization in the context of early neural machine translation by Sen-nrich et al. (2016). It was then taken up in OpenAI’s GPT-2 (Radford et al., 2019) as the default tokenization method, and also included in the open-source Sentence-Piece library (Kudo and Richardson, 2018b). There is a nice a public implemen-tation, minbpe, https://github.com/karpathy/minbpe, by Andrej Karpathy, who also has a popular lecture introducing BPE (https://www.youtube.com/ watch?v=zduSFxRajkE).
Kleene 1951; 1956 first defined regular expressions and the finite automaton, based on the McCulloch-Pitts neuron. Ken Thompson was one of the first to build regular expressions compilers into editors for text searching (Thompson, 1968). His editor ed included a command “g/regular expression/p”, or Global Regular Expres-sion Print, which later became the Unix grep utility.
NLTK is an essential tool that offers both useful Python libraries (https:// www.nltk.org) and textbook descriptions (Bird et al., 2009) of many algorithms including text normalization and corpus interfaces.
For more on edit distance, see Gusfield (1997). Our example measuring the edit distance from ‘intention’ to ‘execution’ was adapted from Kruskal (1983). There are various publicly available packages to compute edit distance, including Unix diff
and the NIST sclite program (NIST, 2005). In his autobiography Bellman (1984) explains how he originally came up with
the term dynamic programming:
“...The 1950s were not good years for mathematical research. [the] Secretary of Defense ...had a pathological fear and hatred of the word, research... I decided therefore to use the word, “programming”. I wanted to get across the idea that this was dynamic, this was multi-stage... I thought, let’s ... take a word that has an absolutely precise meaning, namely dynamic... it’s impossible to use the word, dynamic, in a pejorative sense. Try thinking of some combination that will pos-sibly give it a pejorative meaning. It’s impossible. Thus, I thought dynamic programming was a good name. It was something not even a Congressman could object to.”
2.1 Write regular expressions for the following languages.

1. the set of all alphabetic strings; 2. the set of all lower case alphabetic strings ending in a b; 3. the set of all strings from the alphabet
   such that each a is immedi-
   ately preceded by and immediately followed by a b;
   2.2 Write regular expressions for the following languages. By “word”, we mean an alphabetic string separated from other words by whitespace, any relevant punctuation, line breaks, and so forth.
2. the set of all strings with two consecutive repeated words (e.g., “Hum-bert Humbert” and “the the” but not “the bug” or “the big bug”);
3. all strings that start at the beginning of the line with an integer and that end at the end of the line with a word;
   EXERCISES 37
4. all strings that have both the word grotto and the word raven in them (but not, e.g., words like grottos that merely contain the word grotto);
5. write a pattern that places the first word of an English sentence in a register. Deal with punctuation.
   2.3 Implement an ELIZA-like program, using substitutions such as those described on page 25. You might want to choose a different domain than a Rogerian psy-chologist, although keep in mind that you would need a domain in which your program can legitimately engage in a lot of simple repetition.
   2.4 Compute the edit distance (using insertion cost 1, deletion cost 1, substitution cost 1) of “leda” to “deal”. Show your work (using the edit distance grid).
   2.5 Figure out whether drive is closer to brief or to divers and what the edit dis-tance is to each. You may use any version of distance that you like.
   2.6 Now implement a minimum edit distance algorithm and use your hand-computed results to check your code.
   2.7 Augment the minimum edit distance algorithm to output an alignment; you will need to store pointers and add a stage to compute the backtrace.
   38 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   3 N-gram Language Models
   “You are uniformly charming!” cried he, with a smile of associating and now and then I bowed and they perceived a chaise and four to wish for.
   Random sentence generated from a Jane Austen trigram model
   Predicting is difficult—especially about the future, as the old quip goes. But how about predicting something that seems much easier, like the next word someone is going to say? What word, for example, is likely to follow
   The water of Walden Pond is so beautifully ...
   You might conclude that a likely word is blue, or green, or clear, but probably not refrigerator nor this. In this chapter we formalize this intuition by intro-ducing n-gram language models or LMs. A language model is a machine learninglanguage model
   LM model that predicts upcoming words. More formally, a language model assigns a probability to each possible next word, or equivalently gives a probability distribu-tion over possible next words. Language models can also assign a probability to an entire sentence. Thus an LM could tell us that the following sequence has a much higher probability of appearing in a text:
   all of a sudden I notice three guys standing on the sidewalk
   than does this same set of words in a different order:
   on guys all I of notice sidewalk three a sudden standing the
   Why would we want to predict upcoming words? The main reason is that large language models are built just by training them to predict words!! As we’ll see in chapters 5-9, large language models learn an enormous amount about language solely from being trained to predict upcoming words from neighboring words.
   This probabilistic knowledge can be very practical. Consider correcting gram-mar or spelling errors like Their are two midterms, in which Therewas mistyped as Their, or Everything has improve, in which improve should have been improved. The phrase There are is more probable than Their are, and has
   improved than has improve, so a language model can help users select the more grammatical variant.
   Or for a speech system to recognize that you said I will be back soonish
   and not I will be bassoon dish, it helps to know that back soonish is a more probable sequence. Language models can also help in augmentative and alterna-tive communication (Trnka et al. 2007, Kane et al. 2017). People can use AACAAC
   systems if they are physically unable to speak or sign but can instead use eye gaze or other movements to select words from a menu. Word prediction can be used to suggest likely words for the menu.
   In this chapter we introduce the simplest kind of language model: the n-gramn-gram
   3.1 • N-GRAMS 39
   language model. An n-gram is a sequence of n words: a 2-gram (which we’ll call bigram) is a two-word sequence of words like The water, or water of, and a 3-gram (a trigram) is a three-word sequence of words like The water of, or water of Walden. But we also (in a bit of terminological ambiguity) use the word ‘n-gram’ to mean a probabilistic model that can estimate the probability of a word given the n-1 previous words, and thereby also to assign probabilities to entire sequences.
   In later chapters we will introduce the much more powerful neural large lan-guage models, based on the transformer architecture of Chapter 8. But because n-grams have a remarkably simple and clear formalization, we use them to intro-duce some major concepts of large language modeling, including training and test sets, perplexity, sampling, and interpolation.
   3.1 N-Grams
   Let’s begin with the task of computing P(w|h), the probability of a word w given some history h. Suppose the history h is “The water of Walden Pond is so
   beautifully ” and we want to know the probability that the next word is blue:
   P(blue|The water of Walden Pond is so beautifully) (3.1)
   One way to estimate this probability is directly from relative frequency counts: take a very large corpus, count the number of times we see The water of Walden Pond
   is so beautifully, and count the number of times this is followed by blue. This would be answering the question “Out of the times we saw the history h, how many times was it followed by the word w”, as follows:
   P(blue|The water of Walden Pond is so beautifully) =
   C(The water of Walden Pond is so beautifully blue)
   C(The water of Walden Pond is so beautifully) (3.2)
   If we had a large enough corpus, we could compute these two counts and estimate the probability from Eq. 3.2. But even the entire web isn’t big enough to give us good estimates for counts of entire sentences. This is because language is creative; new sentences are invented all the time, and we can’t expect to get accurate counts for such large objects as entire sentences. For this reason, we’ll need more clever ways to estimate the probability of a word w given a history h, or the probability of an entire word sequence W .
   Let’s start with some notation. First, throughout this chapter we’ll continue to refer to words, although in practice we usually compute language models over to-kens like the BPE tokens of page 13. To represent the probability of a particular random variable Xi taking on the value “the”, or P(Xi = “the”), we will use the simplification P(the). We’ll represent a sequence of n words either as w1
   or w1:n. Thus the expression w1:n−1 means the string
   w1,w2, ...,wn−1,
   but we’ll also be using the equivalent notation
   which can be read as “all the elements of w from w1 up to and including wn−1”. For the joint probability of each word in a se-quence having a particular value P(X1 =
   = wn) we’ll use
   P(w1,w2, ...,wn).
   Now, how can we compute probabilities of entire sequences like
   P(w1,w2, ...,wn)?
   One thing we can do is decompose this probability using the chain rule of proba-
   40 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   = P(X1)P(X2|X1)P(X3|X1:2)
   . . .P(Xn|X1:n−1)
   P(Xk|X1:k−1) (3.3)
   Applying the chain rule to words, we get
   P(w1:n) = P(w1)P(w2|w1)P(w3|w1:2)
   . . .P(wn|w1:n−1)
   P(wk|w1:k−1) (3.4)
   The chain rule shows the link between computing the joint probability of a sequence and computing the conditional probability of a word given previous words. Equa-tion 3.4 suggests that we could estimate the joint probability of an entire sequence of words by multiplying together a number of conditional probabilities. But using the chain rule doesn’t really seem to help us! We don’t know any way to compute the exact probability of a word given a long sequence of preceding words, P(wn|w1:n−1). As we said above, we can’t just estimate by counting the number of times every word occurs following every long string in some corpus, because language is creative and any particular context might have never occurred before!
   3.1.1 The Markov assumption The intuition of the n-gram model is that instead of computing the probability of a word given its entire history, we can approximate the history by just the last few words.
   The bigram model, for example, approximates the probability of a word givenbigram
   all the previous words P(wn|w1:n−1) by using only the conditional probability given the preceding word P(wn|wn−1). In other words, instead of computing the probabil-ity
   P(blue|The water of Walden Pond is so beautifully) (3.5)
   we approximate it with the probability
   P(blue|beautifully) (3.6)
   When we use a bigram model to predict the conditional probability of the next word, we are thus making the following approximation:
   P(wn|w1:n−1)≈
   P(wn|wn−1) (3.7)
   The assumption that the probability of a word depends only on the previous word is called a Markov assumption. Markov models are the class of probabilistic modelsMarkov
   that assume we can predict the probability of some future unit without looking too far into the past. We can generalize the bigram (which looks one word into the past) to the trigram (which looks two words into the past) and thus to the n-gram (whichn-gram
   looks n−1 words into the past). Let’s see a general equation for this n-gram approximation to the conditional
   probability of the next word in a sequence. We’ll use N here to mean the n-gram
   3.1 • N-GRAMS 41
   size, so N = 2 means bigrams and N = 3 means trigrams. Then we approximate the probability of a word given its entire context as follows:
   P(wn|w1:n−1)≈
   P(wn|wn−N+1:n−1) (3.8)
   Given the bigram assumption for the probability of an individual word, we can com-pute the probability of a complete word sequence by substituting Eq. 3.7 into Eq. 3.4:
   P(w1:n)≈ n∏
   P(wk|wk−1) (3.9)
   3.1.2 How to estimate probabilities How do we estimate these bigram or n-gram probabilities? An intuitive way to estimate probabilities is called maximum likelihood estimation or MLE. We get
   maximum likelihood estimation
   the MLE estimate for the parameters of an n-gram model by getting counts from a corpus, and normalizing the counts so that they lie between 0 and 1. For proba-normalize
   bilistic models, normalizing means dividing by some total count so that the resulting probabilities fall between 0 and 1 and sum to 1.
   For example, to compute a particular bigram probability of a word wn given a previous word wn−1, we’ll compute the count of the bigram C(wn−1wn) and normal-ize by the sum of all the bigrams that share the same first word wn−1:
   P(wn|wn−1) =
   w C(wn−1w) (3.10)
   We can simplify this equation, since the sum of all bigram counts that start with a given word wn−1 must be equal to the unigram count for that word wn−1 (the reader should take a moment to be convinced of this):
   P(wn|wn−1) = C(wn−1wn)
   C(wn−1) (3.11)
   Let’s work through an example using a mini-corpus of three sentences. We’ll first need to augment each sentence with a special symbol
   at the beginning of the sentence, to give us the bigram context of the first word. We’ll also need a special end-symbol .1
    ~~I am Sam~~ 
    ~~Sam I am~~ 
    ~~I do not like green eggs and ham~~ 
   Here are the calculations for some of the bigram probabilities from this corpus
   P(I|~~) = 2 3 =
   P(Sam|~~) = 1
   P(am|I) = 2 3 =
   P(~~|Sam) = 1 2 =
   P(Sam|am) = 1
   P(do|I) = 1 3 =
   For the general case of MLE n-gram parameter estimation:
   P(wn|wn−N+1:n−1) = C(wn−N+1:n−1 wn)
   C(wn−N+1:n−1) (3.12)
   1 We need the end-symbol to make the bigram grammar a true probability distribution. Without an end-symbol, instead of the sentence probabilities of all sentences summing to one, the sentence probabilities for all sentences of a given length would sum to one. This model would define an infinite set of probability distributions, with one distribution per sentence length. See Exercise 3.5.
   42 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   Equation 3.12 (like Eq. 3.11) estimates the n-gram probability by dividing the observed frequency of a particular sequence by the observed frequency of a prefix. This ratio is called a relative frequency. We said above that this use of relativerelative
   frequency frequencies as a way to estimate probabilities is an example of maximum likelihood estimation or MLE. In MLE, the resulting parameter set maximizes the likelihood of the training set T given the model M (i.e., P(T |M)). For example, suppose the word Chinese occurs 400 times in a corpus of a million words. What is the probability that a random word selected from some other text of, say, a million words will be the word Chinese? The MLE of its probability is 400
   is not the best possible estimate of the probability of Chinese occurring in all situations; it might turn out that in some other corpus or context Chinese is a very unlikely word. But it is the probability that makes it most likely that Chinese will occur 400 times in a million-word corpus. We present ways to modify the MLE estimates slightly to get better probability estimates in Section 3.6.
   Let’s move on to some examples from a real but tiny corpus, drawn from the now-defunct Berkeley Restaurant Project, a dialogue system from the last century that answered questions about a database of restaurants in Berkeley, California (Ju-rafsky et al., 1994). Here are some sample user queries (text-normalized, by lower casing and with punctuation striped) (a sample of 9332 sentences is on the website):
   can you tell me about any good cantonese restaurants close by tell me about chez panisse i’m looking for a good place to eat breakfast when is caffe venezia open during the day
   Figure 3.1 shows the bigram counts from part of a bigram grammar from text-normalized Berkeley Restaurant Project sentences. Note that the majority of the values are zero. In fact, we have chosen the sample words to cohere with each other; a matrix selected from a random set of eight words would be even more sparse.
   i want to eat chinese food lunch spend i 5 827 0 9 0 0 0 2 want 2 0 608 1 6 6 5 1 to 2 0 4 686 2 0 6 211 eat 0 0 2 0 16 2 42 0 chinese 1 0 0 0 0 82 1 0 food 15 0 15 0 1 4 0 0 lunch 2 0 0 0 0 1 0 0 spend 1 0 1 0 0 0 0 0
   Figure 3.1 Bigram counts for eight of the words (out of V = 1446) in the Berkeley Restau-rant Project corpus of 9332 sentences. Zero counts are in gray. Each cell shows the count of the column label word following the row label word. Thus the cell in row i and column want means that want followed i 827 times in the corpus.
   Figure 3.2 shows the bigram probabilities after normalization (dividing each cell in Fig. 3.1 by the appropriate unigram for its row, taken from the following set of unigram counts):
   i want to eat chinese food lunch spend 2533 927 2417 746 158 1093 341 278
   3.1 • N-GRAMS 43
   i want to eat chinese food lunch spend i 0.002 0.33 0 0.0036 0 0 0 0.00079 want 0.0022 0 0.66 0.0011 0.0065 0.0065 0.0054 0.0011 to 0.00083 0 0.0017 0.28 0.00083 0 0.0025 0.087 eat 0 0 0.0027 0 0.021 0.0027 0.056 0 chinese 0.0063 0 0 0 0 0.52 0.0063 0 food 0.014 0 0.014 0 0.00092 0.0037 0 0 lunch 0.0059 0 0 0 0 0.0029 0 0 spend 0.0036 0 0.0036 0 0 0 0 0
   Figure 3.2 Bigram probabilities for eight words in the Berkeley Restaurant Project corpus of 9332 sentences. Zero probabilities are in gray.
   Here are a few other useful probabilities:
   P(english|want) =
   P(food|english) =
   P(~~|food) =
   Now we can compute the probability of sentences like I want English food or I want Chinese food by simply multiplying the appropriate bigram probabilities to-gether, as follows:
   P( ~~i want english food~~ )
   = P(i|~~)P(want|i)P(english|want)
   P(food|english)P(~~|food)
   0.25×0.33×0.0011×0.5×0.68
   We leave it as Exercise 3.2 to compute the probability of i want chinese food. What kinds of linguistic phenomena are captured in these bigram statistics?
   Some of the bigram probabilities above encode some facts that we think of as strictly syntactic in nature, like the fact that what comes after eat is usually a noun or an adjective, or that what comes after to is usually a verb. Others might be a fact about the personal assistant task, like the high probability of sentences beginning with the words I. And some might even be cultural rather than linguistic, like the higher probability that people are looking for Chinese versus English food.
   3.1.3 Dealing with scale in large n-gram models In practice, language models can be very large, leading to practical issues.
   Log probabilities Language model probabilities are always stored and computed in log space as log probabilities. This is because probabilities are (by definition) lesslog
   probabilities than or equal to 1, and so the more probabilities we multiply together, the smaller the product becomes. Multiplying enough n-grams together would result in numerical underflow. Adding in log space is equivalent to multiplying in linear space, so we combine log probabilities by adding them. By adding log probabilities instead of multiplying probabilities, we get results that are not as small. We do all computation and storage in log space, and just convert back into probabilities if we need to report probabilities at the end by taking the exp of the logprob:
   p1× p2× p3× p4 = exp(log p1 + log p2 + log p3 + log p4) (3.13)
   In practice throughout this book, we’ll use log to mean natural log (ln) when the base is not specified.
   44 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   Longer context Although for pedagogical purposes we have only described bi-gram models, when there is sufficient training data we use trigram models, whichtrigram
   condition on the previous two words, or 4-gram or 5-gram models. For these larger4-gram
   5-gram n-grams, we’ll need to assume extra contexts to the left and right of the sentence end. For example, to compute trigram probabilities at the very beginning of the sentence, we use two pseudo-words for the first trigram (i.e., P(I|~~~~).
   Some large n-gram datasets have been created, like the million most frequent n-grams drawn from the Corpus of Contemporary American English (COCA), a curated 1 billion word corpus of American English (Davies, 2020), Google’s Web 5-gram corpus from 1 trillion words of English web text (Franz and Brants, 2006), or the Google Books Ngrams corpora (800 billion tokens from Chinese, English, French, German, Hebrew, Italian, Russian, and Spanish) (Lin et al., 2012a)).
   It’s even possible to use extremely long-range n-gram context. The infini-gram
   project (Liu et al., 2024) allows n-grams of any length. Their idea is to avoid the expensive (in space and time) pre-computation of huge n-gram count ta-bles. Instead, n-gram probabilities with arbitrary n are computed quickly at inference time by using an efficient representation called suffix arrays. This allows computing of n-grams of every length for enormous corpora of 5 trillion tokens.
   Efficiency considerations are important when building large n-gram language models. It is standard to quantize the probabilities using only 4-8 bits (instead of 8-byte floats), store the word strings on disk and represent them in memory only as a 64-bit hash, and represent n-grams in special data structures like ‘reverse tries’. It is also common to prune n-gram language models, for example by only keeping n-grams with counts greater than some threshold or using entropy to prune less-important n-grams (Stolcke, 1998). Efficient language model toolkits like KenLM (Heafield 2011, Heafield et al. 2013) use sorted arrays and use merge sorts to effi-ciently build the probability tables in a minimal number of passes through a large corpus.
   3.2 Evaluating Language Models: Training and Test Sets
   The best way to evaluate the performance of a language model is to embed it in an application and measure how much the application improves. Such end-to-end evaluation is called extrinsic evaluation. Extrinsic evaluation is the only way toextrinsic
   evaluation know if a particular improvement in the language model (or any component) is really going to help the task at hand. Thus for evaluating n-gram language models that are a component of some task like speech recognition or machine translation, we can compare the performance of two candidate language models by running the speech recognizer or machine translator twice, once with each language model, and seeing which gives the more accurate transcription.
   Unfortunately, running big NLP systems end-to-end is often very expensive. In-stead, it’s helpful to have a metric that can be used to quickly evaluate potential improvements in a language model. An intrinsic evaluation metric is one that mea-intrinsic
   evaluation sures the quality of a model independent of any application. In the next section we’ll introduce perplexity, which is the standard intrinsic metric for measuring language model performance, both for simple n-gram language models and for the more so-phisticated neural large language models of Chapter 8.
   In order to evaluate any machine learning model, we need to have at least three distinct datasets: the training set, the development set, and the test set.training set
   development set
   3.2 • EVALUATING LANGUAGE MODELS: TRAINING AND TEST SETS 45
   The training set is the data we use to learn the parameters of our model; for simple n-gram language models it’s the corpus from which we get the counts that we normalize into the probabilities of the n-gram language model.
   The test set is a different, held-out set of data, not overlapping with the training set, that we use to evaluate the model. We need a separate test set to give us an unbiased estimate of how well the model we trained can generalize when we apply it to some new unknown dataset. A machine learning model that perfectly captured the training data, but performed terribly on any other data, wouldn’t be much use when it comes time to apply it to any new data or problem! We thus measure the quality of an n-gram model by its performance on this unseen test set or test corpus.
   How should we choose a training and test set? The test set should reflect the language we want to use the model for. If we’re going to use our language model for speech recognition of chemistry lectures, the test set should be text of chemistry lectures. If we’re going to use it as part of a system for translating hotel booking re-quests from Chinese to English, the test set should be text of hotel booking requests. If we want our language model to be general purpose, then the test set should be drawn from a wide variety of texts. In such cases we might collect a lot of texts from different sources, and then divide it up into a training set and a test set. It’s important to do the dividing carefully; if we’re building a general purpose model, we don’t want the test set to consist of only text from one document, or one author, since that wouldn’t be a good measure of general performance.
   Thus if we are given a corpus of text and want to compare the performance of two different n-gram models, we divide the data into training and test sets, and train the parameters of both models on the training set. We can then compare how well the two trained models fit the test set.
   But what does it mean to “fit the test set”? The standard answer is simple: whichever language model assigns a higher probability to the test set—which means it more accurately predicts the test set—is a better model. Given two proba-bilistic models, the better model is the one that better predicts the details of the test data, and hence will assign a higher probability to the test data.
   Since our evaluation metric is based on test set probability, it’s important not to let the test sentences into the training set. Suppose we are trying to compute the probability of a particular “test” sentence. If our test sentence is part of the training corpus, we will mistakenly assign it an artificially high probability when it occurs in the test set. We call this situation training on the test set or also data contamination. Training on the test set introduces a bias that makes the probabilitiesdata
   contamination all look too high, and causes huge inaccuracies in perplexity, the probability-based metric we introduce below.
   Even if we don’t train on the test set, if we test our language model on the test set many times after making different changes, we might implicitly tune to its characteristics, by noticing which changes seem to make the model better. For this reason, we only want to run our model on the test set once, or a very few number of times, once we are sure our model is ready.
   For this reason we normally instead have a third dataset called a developmentdevelopment test
   test set or, devset. We do all our testing on this dataset until the very end, and then we test on the test set once to see how good our model is.
   How do we divide our data into training, development, and test sets? We want our test set to be as large as possible, since a small test set may be accidentally un-representative, but we also want as much training data as possible. At the minimum, we would want to pick the smallest test set that gives us enough statistical power
   46 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   to measure a statistically significant difference between two potential models. It’s important that the devset be drawn from the same kind of text as the test set, since its goal is to measure how we would do on the test set.
   3.3 Evaluating Language Models: Perplexity
   We said above that we evaluate language models based on which one assigns a higher probability to the test set. A better model is better at predicting upcoming words, and so it will be less surprised by (i.e., assign a higher probability to) each word when it occurs in the test set. Indeed, a perfect language model would correctly guess each next word in a corpus, assigning it a probability of 1, and all the other words a probability of zero. So given a test corpus, a better language model will assign a higher probability to it than a worse language model.
   But in fact, we often do not use raw probability as our metric for evaluating language models. The reason is that the probability of a test set (or any sequence) depends on the number of words or tokens in it; the probability of a test set gets smaller the longer the text. It’s useful to have a metric that is per-word, normalized by length, so we could compare across texts of different lengths. There is a such a metric! It’s a function of probability called perplexity, and it is used for evaluating large language models as well as n-gram models.
   The perplexity (sometimes abbreviated as PP or PPL) of a language model on aperplexity
   test set is the inverse probability of the test set (one over the probability of the test set), normalized by the number of words (or tokens). For this reason it’s sometimes called the per-word or per-token perplexity. We normalize by the number of words N by taking the Nth root. For a test set W = w1w2
   perplexity(W ) = P(w1w2
   Or we can use the chain rule to expand the probability of W :
   perplexity(W ) = N
   Note that because of the inverse in Eq. 3.15, the higher the probability of the word sequence, the lower the perplexity. Thus the the lower the perplexity of a model on the data, the better the model. Minimizing perplexity is equivalent to maximizing the test set probability according to the language model. Why does perplexity use the inverse probability? It turns out the inverse arises from the original definition of perplexity from cross-entropy rate in information theory; for those interested, the explanation is in the advanced Section 3.7. Meanwhile, we just have to remember that perplexity has an inverse relationship with probability.
   The details of computing the perplexity of a test set W depends on which lan-guage model we use. Here’s the perplexity of W with a unigram language model (just the geometric mean of the inverse of the unigram probabilities):
   perplexity(W ) = N
   3.3 • EVALUATING LANGUAGE MODELS: PERPLEXITY 47
   The perplexity of W computed with a bigram language model is still a geometric mean, but now of the inverse of the bigram probabilities:
   perplexity(W ) = N
   1 P(wi|wi−1)
   What we generally use for word sequence in Eq. 3.15 or Eq. 3.17 is the entire sequence of words in some test set. Since this sequence will cross many sentence boundaries, if our vocabulary includes a between-sentence token~~  but not the beginning-of-sentence marker  ~~in our count of N; This is because the end-sentence token is followed directly by the begin-sentence token with probability almost 1, so we don’t want the probability of that fake transition to influence our perplexity.
   48 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   language that is deterministic (no probabilities), any word can follow any word, and whose vocabulary consists of only three colors:
   {red,blue,green}
   The branching factor of this language is 3. Now let’s make a probabilistic version of the same LM, let’s call it A, where each
   word follows each other with equal probability 1 3 (it was trained on a training set with
   equal counts for the 3 colors), and a test set T = “red red red red blue”. Let’s first convince ourselves that if we compute the perplexity of this artificial
   color language on this test set (or any such test set) we indeed get 3. By Eq. 3.15, the perplexity of A on T is:
   perplexityA(T ) = PA(red red red red blue)− 1 5
   But now suppose red was very likely in the training set of a different LM B, and so B has the following probabilities:
   We should expect the perplexity of the same test set red red red red blue for language model B to be lower since most of the time the next color will be red, which is very predictable, i.e. has a high probability. So the probability of the test set will be higher, and since perplexity is inversely related to probability, the perplexity will be lower. Thus, although the branching factor is still 3, the perplexity or weighted branching factor is smaller:
   perplexityB(T ) = PB(red red red red
   3.4 Sampling sentences from a language model
   One important way to visualize what kind of knowledge a language model embodies is to sample from it. Sampling from a distribution means to choose random pointssampling
   according to their likelihood. Thus sampling from a language model—which rep-resents a distribution over sentences—means to generate some sentences, choosing each sentence according to its likelihood as defined by the model. Thus we are more likely to generate sentences that the model thinks have a high probability and less likely to generate sentences that the model thinks have a low probability.
   This technique of visualizing a language model by sampling was first suggested very early on by Shannon (1948) and Miller and Selfridge (1950). It’s simplest to visualize how this works for the unigram case. Imagine all the words of the English language covering the number line between 0 and 1, each word covering an interval
   3.5 • GENERALIZING VS. OVERFITTING THE TRAINING SET 49
   .09 .11 .13 .15
   however (p=0.0003)
   polyphonic p=0.0000018
   Figure 3.3 A visualization of the sampling distribution for sampling sentences by repeat-edly sampling unigrams. The blue bar represents the relative frequency of each word (we’ve ordered them from most frequent to least frequent, but the choice of order is arbitrary). The number line shows the cumulative probabilities. If we choose a random number between 0 and 1, it will fall in an interval corresponding to some word. The expectation for the random number to fall in the larger intervals of one of the frequent words (the, of, a) is much higher than in the smaller interval of one of the rare words (polyphonic).
   proportional to its frequency. Fig. 3.3 shows a visualization, using a unigram LM computed from the text of this book. We choose a random value between 0 and 1, find that point on the probability line, and print the word whose interval includes this chosen value. We continue choosing random numbers and generating words until we randomly generate the sentence-final token~~ .
   We can use the same technique to generate bigrams by first generating a ran-dom bigram that starts with  ~~(according to its bigram probability). Let’s say the second word of that bigram is w. We next choose a random bigram starting with w (again, drawn according to its bigram probability), and so on.
   3.5 Generalizing vs. overfitting the training set
   The n-gram model, like many statistical models, is dependent on the training corpus. One implication of this is that the probabilities often encode specific facts about a given training corpus. Another implication is that n-grams do a better and better job of modeling the training corpus as we increase the value of n.
   We can use the sampling method from the prior section to visualize both of these facts! To give an intuition for the increasing power of higher-order n-grams, Fig. 3.4 shows random sentences generated from unigram, bigram, trigram, and 4-gram models trained on Shakespeare’s works.
   The longer the context, the more coherent the sentences. The unigram sen-tences show no coherent relation between words nor any sentence-final punctua-tion. The bigram sentences have some local word-to-word coherence (especially considering punctuation as words). The trigram sentences are beginning to look a lot like Shakespeare. Indeed, the 4-gram sentences look a little too much like Shake-speare. The words It cannot be but so are directly from King John. This is because, not to put the knock on Shakespeare, his oeuvre is not very large as corpora go (N =
   and our n-gram probability matrices are ridiculously sparse. There are V 2 =
   844,000,000
   possible bigrams alone, and the number of possible 4-grams is V 4 = 7× 1017. Thus, once the generator has chosen the first 3-gram (It cannot be), there are only seven possible next words for the 4th element (but, I, that, thus, this, and the period).
   To get an idea of the dependence on the training set, let’s look at LMs trained on a completely different corpus: the Wall Street Journal (WSJ) newspaper. Shakespeare
   50 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   –To him swallowed confess hear both. Which. Of save on trail for are ay device and rote life have
   gram –Hill he late speaks; or! a more to leg less first you enter
   –Why dost stand forth thy canopy, forsooth; he is this palpable hit the King Henry. Live king. Follow.
   gram –What means, sir. I confess she? then all sorts, he is trim, captain.
   –Fly, and will rid me these news of price. Therefore the sadness of parting, as they say, ’tis done.
   gram –This shall forbid it should be branded, if renown made it empty.
   –King Henry. What! I will go seek the traitor Gloucester. Exeunt some of the watch. A great banquet serv’d in;
   gram –It cannot be but so. Figure 3.4 Eight sentences randomly generated from four n-gram models computed from Shakespeare’s works. All characters were mapped to lower-case and punctuation marks were treated as words. Output is hand-corrected for capitalization to improve readability.
   and the WSJ are both English, so we might have expected some overlap between our n-grams for the two genres. Fig. 3.5 shows sentences generated by unigram, bigram, and trigram models trained on 40 million words from WSJ.
   1 Months the my and issue of year foreign new exchange’s september
   were recession exchange new endorsed a acquire to six executives
   Last December through the way to preserve the Hudson corporation N. B. E. C. Taylor would seem to complete the major central planners one
   gram point five percent of U. S. E. has already old M. X. corporation of living on information such as more frequently fishing to keep her
   They also point to ninety nine point six billion dollars from two hundred four oh six three percent of the rates of interest stores as Mexico and
   gram Brazil on market conditions Figure 3.5 Three sentences randomly generated from three n-gram models computed from 40 million words of the Wall Street Journal, lower-casing all characters and treating punctua-tion as words. Output was then hand-corrected for capitalization to improve readability.
   Compare these examples to the pseudo-Shakespeare in Fig. 3.4. While they both model “English-like sentences”, there is no overlap in the generated sentences, and little overlap even in small phrases. Statistical models are pretty useless as predictors if the training sets and the test sets are as different as Shakespeare and the WSJ.
   How should we deal with this problem when we build n-gram models? One step is to be sure to use a training corpus that has a similar genre to whatever task we are trying to accomplish. To build a language model for translating legal documents, we need a training corpus of legal documents. To build a language model for a question-answering system, we need a training corpus of questions.
   It is equally important to get training data in the appropriate dialect or variety, especially when processing social media posts or spoken transcripts. For exam-ple some tweets will use features of African American English (AAE)— the name for the many variations of language used in African American communities (King, 2020). Such features can include words like finna—an auxiliary verb that marks immediate future tense —that don’t occur in other varieties, or spellings like den for then, in tweets like this one (Blodgett and O’Connor, 2017):
   3.6 • SMOOTHING, INTERPOLATION, AND BACKOFF 51
   (3.22) Bored af den my phone finna die!!!
   while tweets from English-based languages like Nigerian Pidgin have markedly dif-ferent vocabulary and n-gram patterns from American English (Jurgens et al., 2017):
   (3.23) @username R u a wizard or wat gan sef: in d mornin - u tweet, afternoon - u tweet, nyt gan u dey tweet. beta get ur IT placement wiv twitter
   Is it possible for the testset nonetheless to have a word we have never seen be-fore? What happens if the word Jurafsky never occurs in our training set, but pops up in the test set? The answer is that although words might be unseen, we normally run our NLP algorithms not on words but on subword tokens. With subword tokeniza-tion (like the BPE algorithm of Chapter 2) any word can be modeled as a sequence of known smaller subwords, if necessary by a sequence of tokens corresponding to individual letters. So although for convenience we’ve been referring to words in this chapter, the language model vocabulary is normally the set of tokens rather than words, and in this way the test set can never contain unseen tokens.
   3.6 Smoothing, Interpolation, and Backoff
   There is a problem with using maximum likelihood estimates for probabilities: any finite training corpus will be missing some perfectly acceptable English word se-quences. That is, cases where a particular n-gram never occurs in the training data but appears in the test set. Perhaps our training corpus has the words ruby and slippers in it but just happens not to have the phrase ruby slippers.
   These unseen sequences or zeros—sequences that don’t occur in the training setzeros
   but do occur in the test set—are a problem for two reasons. First, their presence means we are underestimating the probability of word sequences that might occur, which hurts the performance of any application we want to run on this data. Second, if the probability of any word in the test set is 0, the probability of the whole test set is 0. Perplexity is defined based on the inverse probability of the test set. Thus if some words in context have zero probability, we can’t compute perplexity at all, since we can’t divide by zero!
   The standard way to deal with putative “zero probability n-grams” that should re-ally have some non-zero probability is called smoothing or discounting. Smoothingsmoothing
   discounting algorithms shave off a bit of probability mass from some more frequent events and give it to unseen events. Here we’ll introduce some simple smoothing algorithms: Laplace (add-one) smoothing, stupid backoff, and n-gram interpolation.
   3.6.1 Laplace Smoothing The simplest way to do smoothing is to add one to all the n-gram counts, before we normalize them into probabilities. All the counts that used to be zero will now have a count of 1, the counts of 1 will be 2, and so on. This algorithm is called Laplace smoothing. Laplace smoothing does not perform well enough to be usedLaplace
   smoothing in modern n-gram models, but it usefully introduces many of the concepts that we see in other smoothing algorithms, gives a useful baseline, and is also a practical smoothing algorithm for other tasks like text classification (Appendix K).
   Let’s start with the application of Laplace smoothing to unigram probabilities. Recall that the unsmoothed maximum likelihood estimate of the unigram probability
   52 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   of the word wi is its count ci normalized by the total number of word tokens N:
   N Laplace smoothing merely adds one to each count (hence its alternate name add-one smoothing). Since there are V words in the vocabulary and each one was in-add-one
   cremented, we also need to adjust the denominator to take into account the extra V observations. (What happens to our P values if we don’t increase the denominator?)
   PLaplace(wi) = ci +1 N +V
   Now that we have the intuition for the unigram case, let’s smooth our Berkeley Restaurant Project bigrams. Figure 3.6 shows the add-one smoothed counts for the bigrams in Fig. 3.1.
   i want to eat chinese food lunch spend i 6 828 1 10 1 1 1 3 want 3 1 609 2 7 7 6 2 to 3 1 5 687 3 1 7 212 eat 1 1 3 1 17 3 43 1 chinese 2 1 1 1 1 83 2 1 food 16 1 16 1 2 5 1 1 lunch 3 1 1 1 1 2 1 1 spend 2 1 2 1 1 1 1 1
   Figure 3.6 Add-one smoothed bigram counts for eight of the words (out of V = 1446) in the Berkeley Restaurant Project corpus of 9332 sentences. Previously-zero counts are in gray.
   Figure 3.7 shows the add-one smoothed probabilities for the bigrams in Fig. 3.2, computed by Eq. 3.26 below. Recall that normal bigram probabilities are computed by normalizing each row of counts by the unigram count:
   PMLE(wn|wn−1) = C(wn−1wn)
   C(wn−1) (3.25)
   For add-one smoothed bigram counts, we need to augment the unigram count in the denominator by the number of total word types in the vocabulary V . We can see why this is in the following equation, which makes it explicit that the unigram count in the denominator is really the sum over all the bigrams that start with wn−1. Since we add one to each of these, and there are V of them, we add a total of V to the denominator:
   PLaplace(wn|wn−1) =
   C(wn−1wn)+1∑
   w (C(wn−1w)+1)
   = C(wn−1wn)+1 C(wn−1)+V
   Thus, each of the unigram counts given on page 42 will need to be augmented by V = 1446. The result, using Eq. 3.26, is the smoothed bigram probabilities in Fig. 3.7.
   One useful visualization technique is to reconstruct an adjusted count matrix so we can see how much a smoothing algorithm has changed the original counts. This adjusted count C∗ is the count that, if divided by C(wn−1), would result in the smoothed probability. This adjusted count is easier to compare directly with the MLE counts. That is, the Laplace probability can equally be expressed as the adjusted count divided by the (non-smoothed) denominator from Eq. 3.25:
   PLaplace(wn|wn−1) = C(wn−1wn)+1 C(wn−1)+V
   = C∗(wn−1wn)
   3.6 • SMOOTHING, INTERPOLATION, AND BACKOFF 53
   i want to eat chinese food lunch spend i 0.0015 0.21 0.00025 0.0025 0.00025 0.00025 0.00025 0.00075 want 0.0013 0.00042 0.26 0.00084 0.0029 0.0029 0.0025 0.00084 to 0.00078 0.00026 0.0013 0.18 0.00078 0.00026 0.0018 0.055 eat 0.00046 0.00046 0.0014 0.00046 0.0078 0.0014 0.02 0.00046 chinese 0.0012 0.00062 0.00062 0.00062 0.00062 0.052 0.0012 0.00062 food 0.0063 0.00039 0.0063 0.00039 0.00079 0.002 0.00039 0.00039 lunch 0.0017 0.00056 0.00056 0.00056 0.00056 0.0011 0.00056 0.00056 spend 0.0012 0.00058 0.0012 0.00058 0.00058 0.00058 0.00058 0.00058
   Figure 3.7 Add-one smoothed bigram probabilities for eight of the words (out of V = 1446) in the BeRP corpus of 9332 sentences computed by Eq. 3.26. Previously-zero probabilities are in gray.
   Rearranging terms, we can solve for C∗(wn−1wn) :
   C∗(wn−1wn) = [C(wn−1wn)+1]×C(wn−1)
   C(wn−1)+V (3.27)
   Figure 3.8 shows the reconstructed counts, computed by Eq. 3.27.
   i want to eat chinese food lunch spend i 3.8 527 0.64 6.4 0.64 0.64 0.64 1.9 want 1.2 0.39 238 0.78 2.7 2.7 2.3 0.78 to 1.9 0.63 3.1 430 1.9 0.63 4.4 133 eat 0.34 0.34 1 0.34 5.8 1 15 0.34 chinese 0.2 0.098 0.098 0.098 0.098 8.2 0.2 0.098 food 6.9 0.43 6.9 0.43 0.86 2.2 0.43 0.43 lunch 0.57 0.19 0.19 0.19 0.19 0.38 0.19 0.19 spend 0.32 0.16 0.32 0.16 0.16 0.16 0.16 0.16
   Figure 3.8 Add-one reconstituted counts for eight words (of V = 1446) in the BeRP corpus of 9332 sentences, computed by Eq. 3.27. Previously-zero counts are in gray.
   Note that add-one smoothing has made a very big change to the counts. Com-paring Fig. 3.8 to the original counts in Fig. 3.1, we can see that C(want to) changed from 608 to 238. We can see this in probability space as well: P(to|want) decreases from 0.66 in the unsmoothed case to 0.26 in the smoothed case. Looking at the dis-count d, defined as the ratio between new and old counts, shows us how strikingly the counts for each prefix word have been reduced; the discount for the bigram want to is 0.39, while the discount for Chinese food is 0.10, a factor of 10. The sharp change occurs because too much probability mass is moved to all the zeros.
   3.6.2 Add-k smoothing One alternative to add-one smoothing is to move a bit less of the probability mass from the seen to the unseen events. Instead of adding 1 to each count, we add a fractional count k (0.5? 0.01?). This algorithm is therefore called add-k smoothing.add-k
   P∗Add-k(wn|wn−1) = C(wn−1wn)+ k C(wn−1)+ kV
   Add-k smoothing requires that we have a method for choosing k; this can be done, for example, by optimizing on a devset. Although add-k is useful for some tasks (including text classification), it turns out that it still doesn’t work well for
   54 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   language modeling, generating counts with poor variances and often inappropriate discounts (Gale and Church, 1994).
   3.6.3 Language Model Interpolation There is an alternative source of knowledge we can draw on to solve the problem of zero frequency n-grams. If we are trying to compute P(wn|wn−2wn−1) but we have no examples of a particular trigram wn−2wn−1wn, we can instead estimate its probability by using the bigram probability P(wn|wn−1). Similarly, if we don’t have counts to compute P(wn|wn−1), we can look to the unigram P(wn). In other words, sometimes using less context can help us generalize more for contexts that the model hasn’t learned much about.
   The most common way to use this n-gram hierarchy is called interpolation:interpolation
   computing a new probability by interpolating (weighting and combining) the tri-gram, bigram, and unigram probabilities. In simple linear interpolation, we com-bine different order n-grams by linearly interpolating them. Thus, we estimate the trigram probability P(wn|wn−2wn−1) by mixing together the unigram, bigram, and trigram probabilities, each weighted by a
   P̂(wn|wn−2wn−1) =
   +λ2P(wn|wn−1)
   +λ3P(wn|wn−2wn−1)
   s must sum to 1, making Eq. 3.29 equivalent to a weighted average. In a slightly more sophisticated version of linear interpolation, each
   weight is com-puted by conditioning on the context. This way, if we have particularly accurate counts for a particular bigram, we assume that the counts of the trigrams based on this bigram will be more trustworthy, so we can make the
   s for those trigrams higher and thus give that trigram more weight in the interpolation. Equation 3.30 shows the equation for interpolation with context-conditioned weights, where each lambda takes an argument that is the two prior word context:
   P̂(wn|wn−2wn−1) =
   λ1(wn−2:n−1)P(wn)
   +λ2(wn−2:n−1)P(wn|wn−1)
   +λ3(wn−2:n−1)P(wn|wn−2wn−1)
   How are these
   values set? Both the simple interpolation and conditional interpo-lation
   s are learned from a held-out corpus. A held-out corpus is an additionalheld-out
   training corpus, so-called because we hold it out from the training data, that we use to set these
   values.3 We do so by choosing the
   values that maximize the likeli-hood of the held-out corpus. That is, we fix the n-gram probabilities and then search for the
   values that—when plugged into Eq. 3.29—give us the highest probability of the held-out set. There are various ways to find this optimal set of
   s. One way is to use the EM algorithm, an iterative learning algorithm that converges on locally optimal
   s (Jelinek and Mercer, 1980).
   3.6.4 Stupid Backoff An alternative to interpolation is backoff. In a backoff model, if the n-gram we needbackoff
   3 Held-out corpora are generally used to set hyperparameters, which are special parameters, unlike regular counts that are learned from the training data; we’ll discuss hyperparameters in Chapter 6.
   3.7 • ADVANCED: PERPLEXITY’S RELATION TO ENTROPY 55
   has zero counts, we approximate it by backing off to the (n-1)-gram. We continue backing off until we reach a history that has some counts. For a backoff model to give a correct probability distribution, we have to discount the higher-order n-gramsdiscount
   to save some probability mass for the lower order n-grams. In practice, instead of discounting, it’s common to use a much simpler non-discounted backoff algorithm called stupid backoff (Brants et al., 2007).stupid backoff
   Stupid backoff gives up the idea of trying to make the language model a true probability distribution. There is no discounting of the higher-order probabilities. If a higher-order n-gram has a zero count, we simply backoff to a lower order n-gram, weighed by a fixed (context-independent) weight. This algorithm does not produce a probability distribution, so we’ll follow Brants et al. (2007) in referring to it as S:
   S(wi|wi−N+1: i−1) =
   count(wi−N+1: i) count(wi−N+1: i−1)
   if count(wi−N+1:
   λS(wi|wi−N+2:
   i−1) otherwise (3.31)
   The backoff terminates in the unigram, which has score S(w) = count(w) N . Brants et al.
   (2007) find that a value of 0.4 worked well for
   3.7 Advanced: Perplexity’s Relation to Entropy
   We introduced perplexity in Section 3.3 as a way to evaluate n-gram models on a test set. A better n-gram model is one that assigns a higher probability to the test data, and perplexity is a normalized version of the probability of the test set. The perplexity measure actually arises from the information-theoretic concept of cross-entropy, which explains otherwise mysterious properties of perplexity (why the inverse probability, for example?) and its relationship to entropy. Entropy is aEntropy
   measure of information. Given a random variable X ranging over whatever we are predicting (words, letters, parts of speech), the set of which we’ll call
   , and with a particular probability function, call it p(x), the entropy of the random variable X is:
   p(x) log2 p(x) (3.32)
   The log can, in principle, be computed in any base. If we use log base 2, the resulting value of entropy will be measured in bits.
   One intuitive way to think about entropy is as a lower bound on the number of bits it would take to encode a certain decision or piece of information in the optimal coding scheme. Consider an example from the standard information theory textbook Cover and Thomas (1991). Imagine that we want to place a bet on a horse race but it is too far to go all the way to Yonkers Racetrack, so we’d like to send a short message to the bookie to tell him which of the eight horses to bet on. One way to encode this message is just to use the binary representation of the horse’s number as the code; thus, horse 1 would be 001, horse 2 010, horse 3 011, and so on, with horse 8 coded as 000. If we spend the whole day betting and each horse is coded with 3 bits, on average we would be sending 3 bits per race.
   Can we do better? Suppose that the spread is the actual distribution of the bets placed and that we represent it as the prior probability of each horse as follows:
   56 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   Horse 1 1 2 Horse 5 1
   64 Horse 2 1
   4 Horse 6 1 64
   Horse 3 1 8 Horse 7 1
   64 Horse 4 1
   16 Horse 8 1 64
   The entropy of the random variable X that ranges over horses gives us a lower bound on the number of bits and is
   p(i) log2 p(i)
   = − 1 2 log2
   4 log2 1 4− 1
   8 log2 1 8− 1
   16−4( 1 64 log2
   = 2 bits (3.33)
   A code that averages 2 bits per race can be built with short encodings for more probable horses, and longer encodings for less probable horses. For example, we could encode the most likely horse with the code 0, and the remaining horses as 10, then 110, 1110, 111100, 111101, 111110, and 111111.
   What if the horses are equally likely? We saw above that if we used an equal-length binary code for the horse numbers, each horse took 3 bits to code, so the average was 3. Is the entropy the same? In this case each horse would have a probability of 1
   8 . The entropy of the choice of horses is then
   log2 1 8 =− log2
   1 8 = 3 bits (3.34)
   Until now we have been computing the entropy of a single variable. But most of what we will use entropy for involves sequences. For a grammar, for example, we will be computing the entropy of some sequence of words W =
   {w1,w2, . . . ,wn}.
   One way to do this is to have a variable that ranges over sequences of words. For example we can compute the entropy of a random variable that ranges over all se-quences of words of length n in some language L as follows:
   H(w1,w2, . . . ,wn)
   p(w1:n) log p(w1:n) (3.35)
   We could define the entropy rate (we could also think of this as the per-wordentropy rate
   entropy) as the entropy of this sequence divided by the number of words:
   H(w1:n) =− 1 n
   p(w1:n) log p(w1:n) (3.36)
   But to measure the true entropy of a language, we need to consider sequences of infinite length. If we think of a language as a stochastic process L that produces a sequence of words, and allow W to represent the sequence of words
   w1, . . . ,wn,
   then L’s entropy rate H(L) is defined as
   p(w1:n) log p(w1:n) (3.37)
   3.7 • ADVANCED: PERPLEXITY’S RELATION TO ENTROPY 57
   The Shannon-McMillan-Breiman theorem (Algoet and Cover 1988, Cover and Thomas 1991) states that if the language is regular in certain ways (to be exact, if it is both stationary and ergodic),
   n log p(w1:n) (3.38)
   That is, we can take a single sequence that is long enough instead of summing over all possible sequences. The intuition of the Shannon-McMillan-Breiman theorem is that a long-enough sequence of words will contain in it many other shorter se-quences and that each of these shorter sequences will reoccur in the longer sequence according to their probabilities.
   A stochastic process is said to be stationary if the probabilities it assigns to aStationary
   sequence are invariant with respect to shifts in the time index. In other words, the probability distribution for words at time t is the same as the probability distribution at time t + 1. Markov models, and hence n-grams, are stationary. For example, in a bigram, Pi is dependent only on Pi−1. So if we shift our time index by x, Pi+x is still dependent on Pi+x−1. But natural language is not stationary, since as we show in Appendix D, the probability of upcoming words can be dependent on events that were arbitrarily distant and time dependent. Thus, our statistical models only give an approximation to the correct distributions and entropies of natural language.
   To summarize, by making some incorrect but convenient simplifying assump-tions, we can compute the entropy of some stochastic process by taking a very long sample of the output and computing its average log probability.
   Now we are ready to introduce cross-entropy. The cross-entropy is useful whencross-entropy
   we don’t know the actual probability distribution p that generated some data. It allows us to use some m, which is a model of p (i.e., an approximation to p). The cross-entropy of m on p is defined by
   p(w1, . . . ,wn) logm(w1, . . . ,wn)
   That is, we draw sequences according to the probability distribution p, but sum the log of their probabilities according to m.
   Again, following the Shannon-McMillan-Breiman theorem, for a stationary er-godic process:
   n logm(w1w2
   This means that, as for entropy, we can estimate the cross-entropy of a model m on some distribution p by taking a single sequence that is long enough instead of summing over all possible sequences.
   What makes the cross-entropy useful is that the cross-entropy
   is an up-per bound on the entropy H(p). For any model m:
   H(p)≤ H(p,m)
   This means that we can use some simplified model m to help estimate the true en-tropy of a sequence of symbols drawn according to probability p. The more accurate m is, the closer the cross-entropy
   will be to the true entropy H(p). Thus, the difference between
   and H(p) is a measure of how accurate a model is. Between two models m1 and m2, the more accurate model will be the one with the
   58 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   lower cross-entropy. (The cross-entropy can never be lower than the true entropy, so a model cannot err by underestimating the true entropy.)
   We are finally ready to see the relation between perplexity and cross-entropy as we saw it in Eq. 3.40. Cross-entropy is defined in the limit as the length of the observed word sequence goes to infinity. We approximate this cross-entropy by relying on a (sufficiently long) sequence of fixed length. This approximation to the cross-entropy of a model M = P(wi|wi−N+1: i−1) on a sequence of words W is
   H(W ) =− 1 N
   The perplexity of a model P on a sequence of words W is now formally defined asperplexity
   2 raised to the power of this cross-entropy:
   Perplexity(W ) = 2H(W )
   3.8 Summary
   This chapter introduced language modeling via the n-gram model, a classic model that allows us to introduce many of the basic concepts in language modeling.
   Language models offer a way to assign a probability to a sentence or other sequence of words or tokens, and to predict a word or token from preceding words or tokens.
   N-grams are perhaps the simplest kind of language model. They are Markov models that estimate words from a fixed window of previous words. N-gram models can be trained by counting in a training corpus and normalizing the counts (the maximum likelihood estimate).
   N-gram language models can be evaluated on a test set using perplexity.
   The perplexity of a test set according to a language model is a function of
   the probability of the test set: the inverse test set probability according to the model, normalized by the length.
   Sampling from a language model means to generate some sentences, choos-ing each sentence according to its likelihood as defined by the model.
   Smoothing algorithms provide a way to estimate probabilities for events that were unseen in training. Commonly used smoothing algorithms for n-grams include add-1 smoothing, or rely on lower-order n-gram counts through inter-polation.
   Historical Notes
   The underlying mathematics of the n-gram was first proposed by Markov (1913), who used what are now called Markov chains (bigrams and trigrams) to predict whether an upcoming letter in Pushkin’s Eugene Onegin would be a vowel or a con-sonant. Markov classified 20,000 letters as V or C and computed the bigram and
   HISTORICAL NOTES 59
   trigram probability that a given letter would be a vowel given the previous one or two letters. Shannon (1948) applied n-grams to compute approximations to English word sequences. Based on Shannon’s work, Markov models were commonly used in engineering, linguistic, and psychological work on modeling word sequences by the 1950s. In a series of extremely influential papers starting with Chomsky (1956) and including Chomsky (1957) and Miller and Chomsky (1963), Noam Chomsky argued that “finite-state Markov processes”, while a possibly useful engineering heuristic, were incapable of being a complete cognitive model of human grammatical knowl-edge. These arguments led many linguists and computational linguists to ignore work in statistical modeling for decades.
   The resurgence of n-gram language models came from Fred Jelinek and col-leagues at the IBM Thomas J. Watson Research Center, who were influenced by Shannon, and James Baker at CMU, who was influenced by the prior, classified work of Leonard Baum and colleagues on these topics at labs like the US Institute for Defense Analyses (IDA) after they were declassified. Independently these two labs successfully used n-grams in their speech recognition systems at the same time (Baker 1975b, Jelinek et al. 1975, Baker 1975a, Bahl et al. 1983, Jelinek 1990). The terms “language model” and “perplexity” were first used for this technology by the IBM group. Jelinek and his colleagues used the term language model in a pretty modern way, to mean the entire set of linguistic influences on word sequence prob-abilities, including grammar, semantics, discourse, and even speaker characteristics, rather than just the particular n-gram model itself.
   Add-one smoothing derives from Laplace’s 1812 law of succession and was first applied as an engineering solution to the zero frequency problem by Jeffreys (1948) based on an earlier Add-K suggestion by Johnson (1932). Problems with the add-one algorithm are summarized in Gale and Church (1994).
   A wide variety of different language modeling and smoothing techniques were proposed in the 80s and 90s, including Good-Turing discounting—first applied to the n-gram smoothing at IBM by Katz (Nádas 1984, Church and Gale 1991)— Witten-Bell discounting (Witten and Bell, 1991), and varieties of class-based n-gram mod-class-based
   n-gram els that used information about word classes. Starting in the late 1990s, Chen and Goodman performed a number of carefully controlled experiments comparing dif-ferent algorithms and parameters (Chen and Goodman 1999, Goodman 2006, inter alia). They showed the advantages of Modified Interpolated Kneser-Ney, which became the standard baseline for n-gram language modeling around the turn of the century, especially because they showed that caches and class-based models pro-vided only minor additional improvement. SRILM (Stolcke, 2002) and KenLM (Heafield 2011, Heafield et al. 2013) are publicly available toolkits for building n-gram language models.
   Large language models are based on neural networks rather than n-grams, en-abling them to solve the two major problems with n-grams: (1) the number of param-eters increases exponentially as the n-gram order increases, and (2) n-grams have no way to generalize from training examples to test set examples unless they use iden-tical words. Neural language models instead project words into a continuous space in which words with similar contexts have similar representations. We’ll introduce transformer-based large language models in Chapter 8, along the way introducing feedforward language models (Bengio et al. 2006, Schwenk 2007) in Chapter 6 and recurrent language models (Mikolov, 2012) in Chapter 13.
   60 CHAPTER 3 • N-GRAM LANGUAGE MODELS
   3.1 Write out the equation for trigram probability estimation (modifying Eq. 3.11).
   Now write out all the non-zero trigram probabilities for the I am Sam corpus on page 41.
   3.2 Calculate the probability of the sentence i want chinese food. Give two probabilities, one using Fig. 3.2 and the ‘useful probabilities’ just below it on page 43, and another using the add-1 smoothed table in Fig. 3.7. Assume the additional add-1 smoothed probabilities P(i|~~)=
   and P(~~|food)=
   3.3 Which of the two probabilities you computed in the previous exercise is higher, unsmoothed or smoothed? Explain why.
   3.4 We are given the following corpus, modified from the one in the chapter:
    ~~I am Sam~~ 
    ~~Sam I am~~ 
    ~~I am Sam~~ 
    ~~I do not like green eggs and Sam~~ 
   Using a bigram language model with add-one smoothing, what is P(Sam | am)? Include  ~~and~~  in your counts just like any other token.
   3.5 Suppose we didn’t use the end-symbol~~ . Train an unsmoothed bigram grammar on the following training corpus without using the end-symbol~~ :
   Demonstrate that your bigram model does not assign a single probability dis-tribution across all sentence lengths by showing that the sum of the probability of the four possible 2 word sentences over the alphabet {a,b} is 1.0, and the sum of the probability of all possible 3 word sentences over the alphabet {a,b} is also 1.0.
   3.6 Suppose we train a trigram language model with add-one smoothing on a given corpus. The corpus contains V word types. Express a formula for esti-mating P(w3|w1,w2), where w3 is a word which follows the bigram (w1,w2), in terms of various n-gram counts and V. Use the notation c(w1,w2,w3) to denote the number of times that trigram (w1,w2,w3) occurs in the corpus, and so on for bigrams and unigrams.
   3.7 We are given the following corpus, modified from the one in the chapter:
    ~~I am Sam~~ 
    ~~Sam I am~~ 
    ~~I am Sam~~ 
    ~~I do not like green eggs and Sam~~ 
   If we use linear interpolation smoothing between a maximum-likelihood bi-gram model and a maximum-likelihood unigram model with
   1 2 , what is P(Sam|am)? Include  ~~and~~  in your counts just like any other token.
   3.8 Write a program to compute unsmoothed unigrams and bigrams.
   EXERCISES 61
   3.9 Run your n-gram program on two different small corpora of your choice (you might use email text or newsgroups). Now compare the statistics of the two corpora. What are the differences in the most common unigrams between the two? How about interesting differences in bigrams?
   3.10 Add an option to your program to generate random sentences.
   3.11 Add an option to your program to compute the perplexity of a test set.
   3.12 You are given a training set of 100 numbers that consists of 91 zeros and 1 each of the other digits 1-9. Now we see the following test set: 0 0 0 0 0 3 0 0 0 0. What is the unigram perplexity?
   62 CHAPTER 4 • LOGISTIC REGRESSION
   4 Logistic Regression and Text
   Classification
   En sus remotas páginas está escrito que los animales se dividen en: a. pertenecientes al Emperador h. incluidos en esta clasificación b. embalsamados i. que se agitan como locos c. amaestrados j. innumerables d. lechones k. dibujados con un pincel finı́simo de pelo de camello e. sirenas l. etcétera f. fabulosos m. que acaban de romper el jarrón g. perros sueltos n. que de lejos parecen moscas
   Borges (1964)
   Classification lies at the heart of language processing and intelligence. Recog-nizing a letter, a word, or a face, sorting mail, assigning grades to homeworks; these are all examples of assigning a category to an input. The challenges of classification were famously highlighted by the fabulist Jorge Luis Borges (1964), who imagined an ancient mythical encyclopedia that classified animals into:
   (a) those that belong to the Emperor, (b) embalmed ones, (c) those that are trained, (d) suckling pigs, (e) mermaids, (f) fabulous ones, (g) stray dogs, (h) those that are included in this classification, (i) those that tremble as if they were mad, (j) innumerable ones, (k) those drawn with a very fine camel’s hair brush, (l) others, (m) those that have just broken a flower vase, (n) those that resemble flies from a distance.
   Luckily, the classes we use for language processing are easier to define than those of Borges. In this chapter we introduce the logistic regression algorithm for classification, and apply it to text categorization, the task of assigning a label ortext
   categorization category to a text or document. We’ll focus on one text categorization task, senti-ment analysis, the categorization of sentiment, the positive or negative orientationsentiment
   analysis that a writer expresses toward some object. A review of a movie, book, or product expresses the author’s sentiment toward the product, while an editorial or political text expresses sentiment toward an action or candidate. Extracting sentiment is thus relevant for fields from marketing to politics.
   For the binary task of labeling a text as indicating positive or negative stance, words (like awesome and love, or awful and ridiculously are very informative, as we can see from these sample extracts from movie/restaurant reviews:

* ...awesome caramel sauce and sweet toasty almonds. I love this place! − ...awful pizza and ridiculously overpriced...
  There are many text classification tasks. In spam detection we assign an emailspam detection
  to one of the two classes spam or not-spam. Language id is the task of determin-language id
  ing what language a text is written in, while authorship attribution is the task ofauthorship attribution
  determining a text’s author, relevant to both humanistic and forensic analysis.
  4.1 • MACHINE LEARNING AND CLASSIFICATION 63
  But what makes classification so important is that language modeling can also be viewed as classification: each word can be thought of as a class, and so predicting the next word is classifying the context-so-far into a class for each next word. As we’ll see, this intuition underlies large language models.
  The algorithm for classification we introduce in this chapter, logistic regression, is equally important, in a number of ways. First, logistic regression has a close relationship with neural networks. As we will see in Chapter 6, a neural network can be viewed as a series of logistic regression classifiers stacked on top of each other. Second, logistic regression introduces ideas that are fundamental to neural networks and language models, like the sigmoid and softmax functions, the logit,sigmoid
  softmax logit
  and the key gradient descent algorithm for learning. Finally, logistic regression is also one of the most important analytic tools in the social and natural sciences.
  4.1 Machine learning and classification
  The goal of classification is to take a single input (we call each input an observa-tion), extract some useful features or properties of the input, and thereby classifyobservation
  the observation into one of a set of discrete classes. We’ll call the input x, and say that the output comes from a fixed set of output classes Y =
  {y1,y2, ...,yM}.
  Our goal is return a predicted class from Y. Sometimes you’ll see the output classes referred to as the set C instead of Y .
  For sentiment analysis, the input x might be a review, or some other text. And the output set Y might be the set:
  {positive,negative}
  For language id, the input might be a text that we need to know what language it was written in, and the output set Y is the set of languages, i.e.,
  {Abkhaz,Ainu,Albanian,Amharic, ...Zulu,Zuñi}
  There are many ways to do classification. One method is to use rules handwritten by humans. For example, we might have a rule like:
  If the word ‘‘love’’ appears in x, and it’s not preceded by the
  word ‘‘don’t", classify as positive
  Handwritten rules can be components of modern NLP systems, such as the hand-written lists of positive and negative words that can be used in sentiment analysis, as we’ll see below. But rules can be fragile, as situations or data change over time, and for many tasks there are complex interactions between different features (like the example of negation with “don’t” in the rule above), so it can be quite hard for humans to come up with rules that are successful over many situations.
  Another method that we will introduce later is to ask a large language model (of the type we will introduce in Chapter 7) by prompting the model to give a label to some text. Prompting can be powerful, but again has weaknesses: language models often hallucinate, and may not be able to explain why they chose the class they did.
  For these reasons the most common way to do classification is to use super-vised machine learning. Supervised machine learning is a paradigm in which, in
  supervised machine learning
  64 CHAPTER 4 • LOGISTIC REGRESSION
  addition to the input and the set of output classes, we have a labeled training set and a learning algorithm. We talked about training sets in Chapter 3 as a locus for computing n-gram statistics. But in supervised machine learning the training set is labeled, meaning that it contains a set of input observations, each observation asso-ciated with the correct output (a ‘supervision signal’). We can generally refer to a training set of m input/output pairs, where each input x is a text, in the case of text classification, and each is hand-labeled with an associated class (the correct label):.
  training set:
  {(x(1),y(1)),(x(2),y(2)), . . . ,(x(m),y(m))}
  We’ll use superscripts in parentheses to refer to individual observations or instances in the training set. So for sentiment classification, a training set might be a set of sentences or other texts, each with their correct sentiment label.
  Our goal is to learn from this training set a classifier that is capable of mapping from a new input x to its correct class y
  Y . It does this by learning to find features in these training sentences (perhaps words like “awesome” or “awful”). Proba-bilistic classifiers like logistic regression are classifiers that in addition to giving an answer (the class this observation is in), also give the probability of the observation being in the class. This distribution over the classes can be useful information for downstream decisions; avoiding making discrete decisions early on can be useful when combining systems. Probabilistic classifiers like logistic regression have four components:

1. A feature representation of the input. For each input observation x(i), this will be a vector of features
   [x1,x2, ...,xn].
   We will generally refer to feature i for input x( j) as x( j)
   i , sometimes simplified as xi, but we will also see the notation fi, fi(x), or, for multiclass classification,
2. A classification function that computes the estimated class, by computing the probability P(y = yi|x) for each output class yi. We will introduce the sigmoid and softmax tools for classification.
3. An objective function that we want to optimize for learning, usually involv-ing minimizing a loss function corresponding to error on training examples. We will introduce the cross-entropy loss function.
4. An algorithm for optimizing the objective function. We introduce the stochas-tic gradient descent algorithm.
   At the highest level, logistic regression, and really any probabilistic machine learning classifier, has two phases
   training: We train the system (in the case of logistic regression that means train-ing the weights w and b, introduced below) using stochastic gradient descent and the cross-entropy loss.
   test: Given a test example x we compute the probability P(y = yi|x) for each output class yi. Then, given this vector of probabilities, we return the higher probability label y = 1 or y = 0.
   Logistic regression can be used to classify an observation into one of two classes (like ‘positive sentiment’ and ‘negative sentiment’), or into one of many classes. Because the mathematics for the two-class case is simpler, we’ll first describe this special case of logistic regression in the next few sections, beginning with the sig-moid function, and then turn to multinomial logistic regression for more than two classes and the use of the softmax function in Section 4.7.
   4.2 • THE SIGMOID FUNCTION 65
   4.2 The sigmoid function
   The goal of binary logistic regression is to train a classifier that can make a binary decision about the class of a new input observation. Here we introduce the sigmoid classifier that will help us make this decision.
   Consider a single input observation x, which we will represent by a vector of features
   [x1,x2, ...,xn].
   (We’ll show sample features in the next subsection.) The classifier output y can be 1 (meaning the observation is a member of the class) or 0 (the observation is not a member of the class). We want to know the probability P(y = 1|x) that this observation is a member of the class. So perhaps the decision is “positive sentiment” versus “negative sentiment”, the features represent counts of words in a document, P(y = 1|x) is the probability that the document has positive sentiment, and P(y = 0|x) is the probability that the document has negative senti-ment.
   Logistic regression solves this task by learning, from a training set, a vector of weights and a bias term. Each weight wi is a real number, and is associated with one of the input features xi. The weight wi represents how important that input feature is to the classification decision, and can be positive (providing evidence that the in-stance being classified belongs in the positive class) or negative (providing evidence that the instance being classified belongs in the negative class). Thus we might expect in a sentiment task the word awesome to have a high positive weight, and abysmal to have a very negative weight. The bias term, also called the intercept, isbias term
   intercept another real number that’s added to the weighted inputs. To make a decision on a test instance—after we’ve learned the weights in training—
   the classifier first multiplies each xi by its weight wi, sums up the weighted features, and adds the bias term b. The resulting single number z expresses the weighted sum of the evidence for the class.
   In the rest of the book we’ll represent such sums using the dot product notationdot product
   from linear algebra. The dot product of two vectors a and b, written as a ·b, is the sum of the products of the corresponding elements of each vector. (Notice that we represent vectors using the boldface notation b). Thus the following is an equivalent formation to Eq. 4.2:
   z = w ·x+b (4.3)
   But note that nothing in Eq. 4.3 forces z to be a legal probability, that is, to lie between 0 and 1. In fact, since weights are real-valued, the output might even be negative; z ranges from
   To create a probability, we’ll pass z through the sigmoid function,
   sigmoid function (named because it looks like an s) is also called the logistic func-tion, and gives logistic regression its name. The sigmoid has the following equation,logistic
   function shown graphically in Fig. 4.1:
   1+ exp(−z) (4.4)
   (For the rest of the book, we’ll use the notation exp(x) to mean ex.) The sigmoid has a number of advantages; it takes a real-valued number and maps it into the range
   66 CHAPTER 4 • LOGISTIC REGRESSION
   Figure 4.1 The sigmoid function
   = 1 1+e−z takes a real value and maps it to the range
   It is nearly linear around 0 but outlier values get squashed toward 0 or 1.
   which is just what we want for a probability. Because it is nearly linear around 0 but flattens toward the ends, it tends to squash outlier values toward 0 or 1. And it’s differentiable, which as we’ll see in Section 4.15 will be handy for learning.
   We’re almost there. If we apply the sigmoid to the sum of the weighted features, we get a number between 0 and 1. To make it a probability, we just need to make sure that the two cases, P(y = 1) and P(y = 0), sum to 1. We can do this as follows:
   1+ exp(−(w ·x+b))
   = 1− 1 1+ exp(−(w ·x+b))
   = exp(−(w ·x+b))
   1+ exp(−(w ·x+b)) (4.5)
   The sigmoid function has the property
   so we could also have expressed P(y = 0) as
   ·x+b)). Finally, two terminological points. First, the input to the sigmoid function, the
   score z = w · x+ b from Eq. 4.3, is often called the logit. This is because the logitlogit
   function is the inverse of the sigmoid. The logit function is the log of the odds ratio p
   Using the term logit for z is a way of reminding us that by using the sigmoid to turn z (which ranges from
   into a probability, we are implicitly interpreting z as not just any real-valued number, but as specifically a log odds.
   Second, for binary classification it will be convenient to refer to the output of the sigmoid function
   ·x+b) which is computing P(y = 1), as ŷ. We pronounce this symbol as y hat. We thus use ŷ to mean “the probability of the input observa-y hat
   ŷ tion having the positive class”. When we introduce multinomial or softmax logistic regression in Section 4.7, we will introduce an extension of ŷ that will be a vector of probabities over all the output classes, but for binary classification we just keep one scalar probability, knowing that we can always compute the missing probability P(y = 0) as 1−P(y = 1).
   4.3 • CLASSIFICATION WITH LOGISTIC REGRESSION 67
   4.3 Classification with Logistic Regression
   The sigmoid function from the prior section thus gives us a way to take an instance x and compute the probability P(y = 1|x).
   How do we make a decision about which class to apply to a test instance x? For a given x, we say yes if the probability P(y = 1|x) is more than .5, and no otherwise. We call .5 the decision boundary:decision
   decision(x) =
   { 1 if P(y =
   0 otherwise
   Let’s have some examples of applying logistic regression as a classifier for language tasks.
   4.3.1 Sentiment Classification Suppose we are doing binary sentiment classification on movie review text, and we would like to know whether to assign the sentiment class + or − to a review document doc. We’ll represent each input observation by the 6 features x1
   of the input shown in the following table; Fig. 4.2 shows features in a sample mini test document.
   Var Definition Value in Fig. 4.2 x1 count(positive lexicon words
   doc) 3 x2 count(negative lexicon words
   { 1 if “no”
   doc 0 otherwise 1
   x4 count(1st and 2nd pronouns
   doc 0 otherwise 0
   x6 ln(word+punctuation count of doc) ln(66) =
   It's hokey . There are virtually no surprises , and the writing is second-rate . So why was it so enjoyable ? For one thing , the cast is great . Another nice touch is the music . I was overcome with the urge to get off the couch and start dancing . It sucked me in , and it'll do the same to you .
   x1=3 x6=4.19
   Figure 4.2 A sample mini test document showing the extracted features in the vector x.
   Let’s assume for the moment that we’ve already learned a real-valued weight for each of these features, and that the 6 weights corresponding to the 6 features are
   [2.5,−5.0,−1.2,0.5,2.0,0.7],
   while b = 0.1. (We’ll discuss in the next section how the weights are learned.) The weight w1, for example indicates how important a feature the number of positive lexicon words (great, nice, enjoyable, etc.) is to
   68 CHAPTER 4 • LOGISTIC REGRESSION
   a positive sentiment decision, while w2 tells us the importance of negative lexicon words. Note that w1 =
   is positive, while w2
   meaning that negative words are negatively associated with a positive sentiment decision, and are about twice as important as positive words.
   Given these 6 features and the input review x, P(+|x) and P(−|x) can be com-puted using Eq. 4.5:
   P(+|x) = P(y = 1|x) =
   σ([2.5,−5.0,−1.2,0.5,2.0,0.7]
   [3,2,1,3,0,4.19]+0.1)
   P(−|x) = P(y = 0|x) =
   4.3.2 Other classification tasks and features Logistic regression is applied to all sorts of NLP tasks, and any property of the input can be a feature. Consider the task of period disambiguation: deciding if a periodperiod
   disambiguation is the end of a sentence or part of a word, by classifying each period into one of two classes, EOS (end-of-sentence) and not-EOS. We might use features like x1 below expressing that the current word is lower case, perhaps with a positive weight. Or a feature expressing that the current word is in our abbreviations dictionary (“Prof.”), perhaps with a negative weight. A feature can also express a combination of proper-ties. For example a period following an upper case word is likely to be an EOS, but if the word itself is St. and the previous word is capitalized then the period is likely part of a shortening of the word street following a street name.
   { 1 if “Case(wi) = Lower” 0 otherwise
   AcronymDict” 0 otherwise
   { 1 if “wi = St. & Case(wi−1) = Upper” 0 otherwise
   Designing versus learning features: In classic models, features are designed by hand by examining the training set with an eye to linguistic intuitions and literature, supplemented by insights from error analysis on the training set of an early version of a system. We can also consider feature interactions, complex features that arefeature
   interactions combinations of more primitive features. We saw such a feature for period disam-biguation above, where a period on the word St. was less likely to be the end of the sentence if the previous word was capitalized. Features can be created automatically via feature templates, abstract specifications of features. For example a bigramfeature
   templates template for period disambiguation might create a feature for every pair of words that occurs before a period in the training set. Thus the feature space is sparse, since we only have to create a feature if that n-gram exists in that position in the training set. The feature is generally created as a hash from the string descriptions. A user description of a feature as, “bigram(American breakfast)” is hashed into a unique integer i that becomes the feature number fi.
   It should be clear from the prior paragraph that designing features by hand re-quires extensive human effort. For this reason, recent NLP systems avoid hand-
   4.3 • CLASSIFICATION WITH LOGISTIC REGRESSION 69
   designed features and instead focus on representation learning: ways to learn fea-tures automatically in an unsupervised way from the input. We’ll introduce methods for representation learning in Chapter 5 and Chapter 6.
   Scaling input features: When different input features have extremely different ranges of values, it’s common to rescale them so they have comparable ranges. We standardize input values by centering them to result in a zero mean and a standardstandardize
   deviation of one (this transformation is sometimes called the z-score). That is, if µiz-score
   is the mean of the values of feature xi across the m observations in the input dataset, and
   is the standard deviation of the values of features xi across the input dataset, we can replace each feature xi by a new feature x′i computed as follows:
   x′i = xi−µi
   Alternatively, we can normalize the input features values to lie between 0 and 1:normalize
   x′i = xi−min(xi)
   max(xi)−min(xi) (4.10)
   Having input data with comparable range is useful when comparing values across features. Data scaling is especially important in large neural networks, since it helps speed up gradient descent.
   Another very common type of scaling for natural language data is to take logs, for example when inputs are word counts, or bigram counts, or anything else that follows a Zipfian distribution.
   4.3.3 Processing many examples at once We’ve shown the equations for logistic regression for a single example. But in prac-tice we’ll of course want to process an entire test set with many examples. Let’s suppose we have a test set consisting of m test examples each of which we’d like to classify. We’ll continue to use the notation from page 64, in which a superscript value in parentheses refers to the example index in some set of data (either for train-ing or for test). So in this case each test example x(i) has a feature vector x(i),
   m. (As usual, we’ll represent vectors and matrices in bold.)
   One way to compute ŷ(i) (which is how we refer to P(y(1) = 1), i.e., the prob-ability that the output for input x(i)i has the value 1), is just to have a for-loop and compute each test example one at a time:
   foreach x(i) in input
   [x(1),x(2), ...,x(m)]
   ŷ(i) = P(y(i) = 1) =
   ·x(i)+b) (4.11)
   For the first 3 test examples, then, we would be separately computing the pre-dicted output probability as follows:
   ŷ(1) = P(y(1) = 1|x(1)) =
   ŷ(2) = P(y(2) = 1|x(2)) =
   ŷ(3) = P(y(3) = 1|x(3)) =
   70 CHAPTER 4 • LOGISTIC REGRESSION
   But it turns out that we can slightly modify our original equation Eq. 4.5 to do this much more efficiently. We’ll use matrix arithmetic to assign a class to all the examples with one matrix operation!
   First, we’ll pack all the input feature vectors for each input x into a single input matrix X, where each row i is a row vector consisting of the feature vector for in-put example x(i) (i.e., the vector x(i)). Assuming each example has f features and weights, X will therefore be a matrix of shape [m× f ], as follows:
   x(1)1 x(1)2
   x(2)1 x(2)2
   x(3)1 x(3)2
   Now if we introduce b as a vector of length m which consists of the scalar bias term b repeated m times, b =
   [b,b, ...,b],
   [ŷ(1), ŷ(2)...,
   ŷ(m)] as the vector of outputs (one scalar ŷ(i) = P(y(i) = 1) for each input x(i) and its feature vector x(i)), and represent the weight vector w as a column vector, we can compute all the outputs with a single matrix multiplication and one addition:
   You should convince yourself that Eq. 4.13 computes the same thing as our for-loop in Eq. 4.11. For example ŷ(1), the first entry of the output vector ŷ, will correctly be:
   ,x(1)2 , ...,x(1)f
   [w1,w2, ...,w
   Note that we had to reorder X and w from the order they appeared in Eq. 4.5 to make the multiplications come out properly. Here is Eq. 4.13 again with the shapes shown:
   (m×1) (m× f ) ( f ×1) (m×1) (4.15)
   Modern compilers and compute hardware can compute this matrix operation very efficiently, making the computation much faster, which becomes important when training or testing on very large datasets.
   Note by the way that we could have kept X and w in the original order (as ŷ =
   b)) if we had chosen to define X differently as a matrix of column vectors, one vector for each input example, instead of row vectors, and then it would have shape [ f ×m]. But we conventionally represent inputs as rows.
   4.4 Learning in Logistic Regression
   How are the parameters of the model, the weights w and bias b, learned? Binary logistic regression is an instance of supervised classification in which we know the correct label y (either 0 or 1) for each observation x. What the system produces via Eq. 4.5 is ŷ, the system’s probability of y being 1, which we can think of an estimate of the true y (which is either 1 or 0). We want to learn parameters (meaning w and b) that make the probability value ŷ for each training observation as close as possible
   4.5 • THE CROSS-ENTROPY LOSS FUNCTION 71
   to the true y. That is, if y is 1, then we want the system’s estimate ŷ = P(y = 1) to be high, i.e. as close to 1 as possible. If y is in fact 0, then we want the system’s estimate ŷ = P(y = 1) to be low, i.e. as close to 0 as possible.
   This requires two components that we foreshadowed in the introduction to the chapter. The first is a metric for how close ŷ (the systems’s estimate of the probabil-ity that the observation is in the positive class) is to the true gold label y. Rather than measure similarity, we usually talk about the opposite of this: the distance between the system output and the gold output, and we call this distance the loss function orloss
   the cost function. In the next section we’ll introduce the loss function that is com-monly used for logistic regression and also for neural networks, the cross-entropy loss.
   The second thing we need is an optimization algorithm for iteratively updating the weights so as to minimize this loss function. The standard algorithm for this is gradient descent; we’ll introduce the stochastic gradient descent algorithm in the following section.
   We’ll describe these algorithms for the simpler case of binary logistic regres-sion in the next two sections, and then turn to multinomial logistic regression in Section 4.8.
   4.5 The cross-entropy loss function
   We need a loss function that expresses, for an observation x, how close the classifier output (ŷ =
   · x+ b)) is to the correct output (y, which is 0 or 1). Recall that ŷ expresses the probability that the classifier assigns to observation x being in the positive class 1. So both ŷ and y express probabilities, but y is always 0 or 1 but ŷ can also lie in between. We’ll call this measure of loss or distance:
   = How much ŷ differs from the true y (4.16)
   We do this via a loss function that prefers the correct class labels of the train-ing examples to be more likely. This is called conditional maximum likelihood estimation: we choose the parameters
   that maximize the log probability of the true y labels in the training data given the observations x. The resulting loss function is the negative log likelihood loss, generally called the cross-entropy loss.cross-entropy
   loss Let’s derive this loss function, applied to a single observation x. We’d like to
   learn weights that maximize the probability of the correct label p(y|x). Since there are only two discrete outcomes (1 or 0), this is a Bernoulli distribution, and we can express the probability p(y|x) that our classifier produces for one observation as the following (keeping in mind that if y = 1, Eq. 4.17 simplifies to ŷ; if y = 0, Eq. 4.17 simplifies to 1− ŷ):
   p(y|x) = ŷ y (1− ŷ)1−y (4.17)
   Now we take the log of both sides. This will turn out to be handy mathematically, and doesn’t hurt us; whatever values maximize a probability will also maximize the log of the probability:
   log p(y|x) = log [ ŷ y (1− ŷ)1−y]
   = y log ŷ+(1− y) log(1− ŷ) (4.18)
   72 CHAPTER 4 • LOGISTIC REGRESSION
   Eq. 4.18 describes a log likelihood that should be maximized. In order to turn this into a loss function (something that we need to minimize), we’ll just flip the sign on Eq. 4.18. The result is the cross-entropy loss LCE:
   =− log p(y|x) = − [y log ŷ+(1− y) log(1− ŷ)] (4.19)
   Finally, we can plug in the definition of ŷ =
   ·x+b)+(1− y)
   ·x+b))] (4.20)
   Let’s see if this loss function does the right thing for our example from Fig. 4.2. We want the loss to be smaller if the model’s estimate is close to correct, and bigger if the model is confused. So first let’s suppose the correct gold label for the sentiment example in Fig. 4.2 is positive, i.e., y = 1. In this case our model is doing well, since from Eq. 4.8 it indeed gave the example a higher probability of being positive (.70) than negative (.30). If we plug
   and y = 1 into Eq. 4.20, the right side of the equation drops out, leading to the following loss (we’ll use log to mean natural log when the base is not specified):
   ·x+b)+(1− y)
   By contrast, let’s pretend instead that the example in Fig. 4.2 was actually negative, i.e., y = 0 (perhaps the reviewer went on to say “But bottom line, the movie is terrible! I beg you not to see it!”). In this case our model is confused and we’d want the loss to be higher. Now if we plug y = 0 and
   from Eq. 4.8 into Eq. 4.20, the left side of the equation drops out:
   ·x+b)+(1− y)
   Sure enough, the loss for predicting the correct label (.36) is less than the loss for predicting the incorrect label (1.2).
   Why does minimizing this negative log probability do what we want? A perfect classifier would assign probability 1 to the correct outcome (y = 1 or y = 0) and probability 0 to the incorrect outcome. That means if y equals 1, the higher ŷ is (the closer it is to 1), the better the classifier; the lower ŷ is (the closer it is to 0), the worse the classifier. If y equals 0, instead, the higher 1− ŷ is (closer to 1), the better the classifier. The negative log of ŷ (if the true y equals 1) or 1− ŷ (if the true y equals 0) is a convenient loss metric since it goes from 0 (negative log of 1, no loss) to infinity (negative log of 0, infinite loss). This loss function also ensures that as the probability of the correct answer is maximized, the probability of the incorrect answer is minimized; since the two sum to one, any increase in the probability of the correct answer is coming at the expense of the incorrect answer. It’s called the cross-entropy loss, because Eq. 4.18 is also the formula for the cross-entropy between the true probability distribution y and our estimated distribution ŷ.
   Now we know what we want to minimize; in the next section, we’ll see how to find the minimum.
   4.6 • GRADIENT DESCENT 73
   4.6 Gradient Descent
   Our goal with gradient descent is to find the optimal weights: minimize the loss function we’ve defined for the model. In Eq. 4.21 below, we’ll explicitly represent the fact that the cross-entropy loss function LCE is parameterized by the weights. In machine learning in general we refer to the parameters being learned as
   ; in the case of logistic regression
   So we’ll represent ŷ(i) as f
   to make the dependence on
   more obvious. The goal is to find the set of weights which minimizes the loss function, averaged over all examples:
   (x(i);θ),y(i))
   How shall we find the minimum of this (or any) loss function? Gradient descent is a method that finds a minimum of a function by figuring out in which direction (in the space of the parameters
   ) the function’s slope is rising the most steeply, and moving in the opposite direction. The intuition is that if you are hiking in a canyon and trying to descend most quickly down to the river at the bottom, you might look around yourself in all directions, find the direction where the ground is sloping the steepest, and walk downhill in that direction.
   For logistic regression, this loss function is conveniently convex. A convex func-convex
   tion has at most one minimum; there are no local minima to get stuck in, so gradient descent starting from any point is guaranteed to find the minimum. (By contrast, the loss for multi-layer neural networks is non-convex, and gradient descent may get stuck in local minima for neural network training and never find the global opti-mum.)
   Although the algorithm (and the concept of gradient) are designed for direction vectors, let’s first consider a visualization of the case where the parameter of our system is just a single scalar w, shown in Fig. 4.3.
   Given a random initialization of w at some value w1, and assuming the loss function L happened to have the shape in Fig. 4.3, we need the algorithm to tell us whether at the next iteration we should move left (making w2 smaller than w1) or right (making w2 bigger than w1) to reach the minimum.
   The gradient descent algorithm answers this question by finding the gradientgradient
   of the loss function at the current point and moving in the opposite direction. The gradient of a function of many variables is a vector pointing in the direction of the greatest increase in a function. The gradient is a multi-variable generalization of the slope, so for a function of one variable like the one in Fig. 4.3, we can informally think of the gradient as the slope. The dotted line in Fig. 4.3 shows the slope of this hypothetical loss function at point w = w1. You can see that the slope of this dotted line is negative. Thus to find the minimum, gradient descent tells us to go in the opposite direction: moving w in a positive direction.
   The magnitude of the amount to move in gradient descent is the value of the slope d
   weighted by a learning rate
   . A higher (faster) learninglearning rate
   rate means that we should move w more on each step. The change we make in our parameter is the learning rate times the gradient (or the slope, in our single-variable example):
   Now let’s extend the intuition from a function of one scalar variable w to many
   74 CHAPTER 4 • LOGISTIC REGRESSION
   slope of loss at w1 is negative
   one step of gradient
   Figure 4.3 The first step in iteratively finding the minimum of this loss function, by moving w in the reverse direction from the slope of the function. Since the slope is negative, we need to move w in a positive direction, to the right. Here superscripts are used for learning steps, so w1 means the initial value of w (which is 0), w2 the value at the second step, and so on.
   variables, because we don’t just want to move left or right, we want to know where in the N-dimensional space (of the N parameters that make up
   ) we should move. The gradient is just such a vector; it expresses the directional components of the sharpest slope along each of those N dimensions. If we’re just imagining two weight dimensions (say for one weight w and one bias b), the gradient might be a vector with two orthogonal components, each of which tells us how much the ground slopes in the w dimension and in the b dimension. Fig. 4.4 shows a visualization of the value of a 2-dimensional gradient vector taken at the red point.
   In an actual logistic regression, the parameter vector w is much longer than 1 or 2, since the input feature vector x can be quite long, and we need a weight wi for each xi. For each dimension/variable wi in w (plus the bias b), the gradient will have a component that tells us the slope with respect to that variable. In each dimension wi, we express the slope as a partial derivative
   of the loss function. Essentially
   we’re asking: “How much would a small change in that variable wi influence the total loss function L?”
   Figure 4.4 Visualization of the gradient vector at the red point in two dimensions w and b, showing a red arrow in the x-y plane pointing in the direction we will go to look for the minimum: the opposite direction of the gradient (recall that the gradient points in the direction of increase not decrease).
   4.6 • GRADIENT DESCENT 75
   Formally, then, the gradient of a multi-variable function f is a vector in which each component expresses the partial derivative of f with respect to one of the vari-ables. We’ll use the inverted Greek delta symbol
   to refer to the gradient, and represent ŷ as f
   to make the dependence on
   more obvious:
   The final equation for updating
   based on the gradient is thus
   4.6.1 The Gradient for Logistic Regression In order to update
   , we need a definition for the gradient
   Recall that for logistic regression, the cross-entropy loss function is:
   ·x+b)+(1− y)
   ·x+b))] (4.25)
   It turns out that the derivative of this function for one observation vector x is Eq. 4.26 (the interested reader can see Section 4.15 for the derivation of this equation):
   ∂LCE(ŷ,y) ∂w
   ·x+b)− y]x j
   = (ŷ− y)x j (4.26)
   You’ll also sometimes see this equation in the equivalent form:
   ∂LCE(ŷ,y) ∂w
   = −(y− ŷ)x j (4.27)
   Note in these equations that the gradient with respect to a single weight w j rep-resents a very intuitive value: the difference between the true y and our estimated ŷ =
   · x+ b) for that observation, multiplied by the corresponding input value x j.
   By the way, we’ll also need a term for the partial derivative with respect to b. That turns out to be:
   ∂LCE(ŷ,y) ∂b
   = ŷ− y (4.28)
   4.6.2 The Stochastic Gradient Descent Algorithm Stochastic gradient descent is an online algorithm that minimizes the loss function by computing its gradient after each training example, and nudging
   in the right direction (the opposite direction of the gradient). (An “online algorithm” is one that processes its input example by example, rather than waiting until it sees the entire input.) Stochastic gradient descent is called stochastic because it chooses a single
   76 CHAPTER 4 • LOGISTIC REGRESSION
   function STOCHASTIC GRADIENT DESCENT(L(), f (), x, y) returns

### where: L is the loss function # f is a function parameterized by

### x is the set of training inputs

x(1), x(2), ...,

### y is the set of training outputs (labels)

y(1), y(2), ...,

### (or small random values) repeat til done # see caption

For each training tuple
y(i)) (in random order) 1. Optional (for reporting): # How are we doing on this tuple?
Compute ŷ (i) = f

### What is our estimated output ŷ? Compute the loss L(ŷ

### How far off is ŷ(i) from the true output y(i)?

(x(i);θ),y(i))

### How should we move

to maximize loss? 3.
g # Go the other way instead
Figure 4.5 The stochastic gradient descent algorithm. Step 1 (computing the loss) is used mainly to report how well we are doing on the current tuple; we don’t need to compute the loss in order to compute the gradient. The algorithm can terminate when it converges (when the gradient norm
or when progress halts (for example when the loss starts going up on a held-out set). Weights are initialized to 0 for logistic regression, but to small random values for neural networks, as we’ll see in Chapter 6.
random example at a time; in Section 4.6.4 we’ll discuss other versions of gradient descent that batch many examples at once. Fig. 4.5 shows the algorithm.
The learning rate
is a hyperparameter that must be adjusted. If it’s too high,hyperparameter
the learner will take steps that are too large, overshooting the minimum of the loss function. If it’s too low, the learner will take steps that are too small, and take too long to get to the minimum. It is common to start with a higher learning rate and then slowly decrease it, so that it is a function of the iteration k of training; the notation
can be used to mean the value of the learning rate at iteration k.
We’ll discuss hyperparameters in more detail in Chapter 6, but in short, they are a special kind of parameter for any machine learning model. Unlike regular param-eters of a model (weights like w and b), which are learned by the algorithm from the training set, hyperparameters are special parameters chosen by the algorithm designer that affect how the algorithm works.
4.6.3 Working through an example Let’s walk through a single step of the gradient descent algorithm. We’ll use a simplified version of the example in Fig. 4.2 as it sees a single observation x, whose correct value is y = 1 (this is a positive review), and with a feature vector x=
consisting of these two features:
x1 = 3 (count of positive lexicon words) x2 = 2 (count of negative lexicon words)
Let’s assume the initial weights and bias in
0 are all set to 0, and the initial learning rate
w1 = w2 = b = 0
4.6 • GRADIENT DESCENT 77
The single update step requires that we compute the gradient, multiplied by the learning rate
(x(i);θ),y(i))
In our mini example there are three parameters, so the gradient vector has 3 dimen-sions, for w1, w2, and b. We can compute the first gradient as follows:
∂LCE(ŷ,y) ∂w1
∂LCE(ŷ,y) ∂w2
∂LCE(ŷ,y) ∂b
·x+b)− y)x1
·x+b)− y)x2
(σ(0)−1)x1 (σ(0)−1)x2 σ(0)−1
−0.5x1 −0.5x2 −0.5
−1.5 −1.0 −0.5
Now that we have a gradient, we compute the new parameter vector
1 by moving
0 in the opposite direction from the gradient:
−1.5 −1.0 −0.5
So after one step of gradient descent, the weights have shifted to be: w1 =
Note that this observation x happened to be a positive example. We would expect that after seeing more negative examples with high counts of negative words, that the weight w2 would shift to have a negative value.
4.6.4 Mini-batch training
Stochastic gradient descent is called stochastic because it chooses a single random example at a time, moving the weights so as to improve performance on that single example. That can result in very choppy movements, so it’s common to compute the gradient over batches of training instances rather than a single instance.
For example in batch training we compute the gradient over the entire dataset.batch training
By seeing so many examples, batch training offers a superb estimate of which di-rection to move the weights, at the cost of spending a lot of time processing every single example in the training set to compute this perfect direction.
A compromise is mini-batch training: we train on a group of m examples (per-mini-batch
haps 512, or 1024) that is less than the whole dataset. (If m is the size of the dataset, then we are doing batch gradient descent; if m = 1, we are back to doing stochas-tic gradient descent.) Mini-batch training also has the advantage of computational efficiency. The mini-batches can easily be vectorized, choosing the size of the mini-batch based on the computational resources. This allows us to process all the exam-ples in one mini-batch in parallel and then accumulate the loss, something that’s not possible with individual or batch training.
We just need to define mini-batch versions of the cross-entropy loss function we defined in Section 4.5 and the gradient in Section 4.6.1. Let’s extend the cross-entropy loss for one example from Eq. 4.19 to mini-batches of size m. We’ll continue to use the notation that x(i) and y(i) mean the ith training features and training label,
78 CHAPTER 4 • LOGISTIC REGRESSION
respectively. We make the assumption that the training examples are independent:
log p(training labels) = log
p(y(i)|x(i))
log p(y(i)|x(i))
LCE(ŷ(i),y(i))
Now the cost function for the mini-batch of m examples is the average loss for each example:
LCE(ŷ(i),y(i))
·x(i)+b)+(1− y(i)) log (
The mini-batch gradient is the average of the individual gradients from Eq. 4.26:
∂Cost(ŷ,y) ∂w
·x(i)+b)− y(i)
] x(i)j (4.31)
Instead of using the sum notation, we can more efficiently compute the gradient in its matrix form, following the vectorization we saw on page 70, where we have a matrix X of size [m× f ] representing the m inputs in the batch, and a vector y of size [m×1] representing the correct outputs:
∂Cost(ŷ,y) ∂w
= 1 m (ŷ−y)ᵀX
(σ(Xw+b)−y)ᵀX
4.7 Multinomial logistic regression
Sometimes we need more than two classes. Perhaps we might want to do 3-way sentiment classification (positive, negative, or neutral). Or we could be assigning some of the labels we will introduce in Chapter 17, like the part of speech of a word (choosing from 10, 30, or even 50 different parts of speech), or the named entity type of a phrase (choosing from tags like person, location, organization). Or, for large language models, we’ll be predicting the next word out of the |V | possible words in the vocabulary, so it’s |V |-way classification.
In such cases we use multinomial logistic regression, also called softmax re-multinomial
logistic regression gression (in older NLP literature you will sometimes see the name maxent classi-
fier). In multinomial logistic regression we want to label each observation with a class k from a set of K classes, under the stipulation that only one of these classes is the correct one (sometimes called hard classification; an observation can not be in
4.7 • MULTINOMIAL LOGISTIC REGRESSION 79
multiple classes). Let’s use the following representation: the output y for each input x will be a vector of length K. If class c is the correct class, we’ll set yc = 1, and set all the other elements of y to be 0, i.e., yc = 1 and y j = 0
j 6= c. A vector like this y, with one value=1 and the rest 0, is called a one-hot vector. The job of the classifier is to produce an estimate vector ŷ. For each class k, the value ŷk will be the classifier’s estimate of the probability P(yk = 1|x).
4.7.1 Softmax The multinomial logistic classifier uses a generalization of the sigmoid, called the softmax function, to compute p(yk = 1|x). The softmax function takes a vectorsoftmax
[z1,z2, ...,zK
] of K arbitrary values and maps them to a probability distribution, with each value in the range [0,1], and all the values summing to 1. Like the sigmoid, it is an exponential function.
For a vector z of dimensionality K, the softmax is defined as:
softmax(zi) =
j=1 exp(z j)
The softmax of an input vector z=
[z1,z2, ...,zK
] is thus a vector itself:
softmax(z) =
i=1 exp(zi)
, exp(z2)∑K
i=1 exp(zi)
, ..., exp(zK)∑K
i=1 exp(zi)
The denominator
i=1 exp(zi) is used to normalize all the values into probabilities. Thus for example given a vector:
[0.6,1.1,−1.5,1.2,3.2,−1.1]
the resulting (rounded) softmax(z) is
[0.05,0.09,0.01,0.1,0.74,0.01]
Like the sigmoid, the softmax has the property of squashing values toward 0 or 1. Thus if one of the inputs is larger than the others, it will tend to push its probability toward 1, and suppress the probabilities of the smaller inputs.
Finally, note that, just as for the sigmoid, we refer to z, the vector of scores that is the input to the softmax, as logits (see Eq. 4.7).
4.7.2 Applying softmax in logistic regression When we apply softmax for logistic regression, the input will (just as for the sig-moid) be the dot product between a weight vector w and an input vector x (plus a bias). But now we’ll need separate weight vectors wk and bias bk for each of the K classes. The probability of each of our output classes ŷk can thus be computed as:
P(yk = 1|x) = exp(wk ·x+bk)
exp(w j ·x+b j)
The form of Eq. 4.35 makes it seem that we would compute each output sep-arately. Instead, it’s more common to set up the equation for more efficient com-putation by modern vector processing hardware. We’ll do this by representing the
80 CHAPTER 4 • LOGISTIC REGRESSION
set of K weight vectors as a weight matrix W and a bias vector b. Each row k of W corresponds to the vector of weights wk. W thus has shape [K× f ], for K the number of output classes and f the number of input features. The bias vector b has one value for each of the K output classes. If we represent the weights in this way, we can compute ŷ, the vector of output probabilities for each of the K classes, by a single elegant equation:
ŷ = softmax(Wx+b) (4.36)
If you work out the matrix arithmetic, you can see that the estimated score of the first output class ŷ1 (before we take the softmax) will correctly turn out to be w1 ·x+b1.
One helpful interpretation of the weight matrix W is to see each row wk as a prototype of class k. The weight vector wk that is learned represents the class asprototype
a kind of template. Since two vectors that are more similar to each other have a higher dot product with each other, the dot product acts as a similarity function. Logistic regression is thus learning a protoype representation for each class, such that incoming vectors are assigned the class k they are most similar to from the K classes (Doumbouya et al., 2025).
Fig. 4.6 shows the difference between binary and multinomial logistic regression by illustrating the weight vector versus weight matrix in the computation of the output class probabilities.
4.7.3 Features in Multinomial Logistic Regression Features in multinomial logistic regression act like features in binary logistic regres-sion, with the difference mentioned above that we’ll need separate weight vectors and biases for each of the K classes. Recall our binary exclamation point feature x5 from page 67:
doc 0 otherwise
In binary classification a positive weight w5 on a feature influences the classifier toward y = 1 (positive sentiment) and a negative weight influences it toward y = 0 (negative sentiment) with the absolute value indicating how important the feature is. For multinomial logistic regression, by contrast, with separate weights for each class, a feature can be evidence for or against each individual class.
In 3-way multiclass sentiment classification, for example, we must assign each document one of the 3 classes +, −, or 0 (neutral). Now a feature related to excla-mation marks might have a negative weight for 0 documents, and a positive weight for + or − documents:
Feature Definition
w5,+ w5,− w5,0
doc 0 otherwise
3.5 3.1 −5.3
Because these feature weights are dependent both on the input text and the output class, we sometimes make this dependence explicit and represent the features them-selves as f
a function of both the input and the class. Using such a notation f5(x) above could be represented as three features
f5(x,+), f5(x,−),
each of which has a single weight. We’ll use this kind of notation in our description of the CRF in Chapter 17.
4.8 • LEARNING IN MULTINOMIAL LOGISTIC REGRESSION 81
Binary Logistic Regression
Output sigmoid
Input words
p(+) = 1- p(-)
Input feature vector
positive lexicon words = 1
count of “no” = 0
wordcount =3
x1 x2 x3 xf
dessert was great
Weight vector
Multinomial Logistic Regression
Output softmax
Input words
Input feature vector
positive lexicon words = 1
count of “no” = 0
wordcount =3
x1 x2 x3 xf
dessert was great
p(-) p(neut)
Weight matrix
These f red weights
are a row of W corresponding
to weight vector w3, (= weights for class 3,
= a prototype of class 3)
Figure 4.6 Binary versus multinomial logistic regression. Binary logistic regression uses a single weight vector w, and has a scalar output ŷ. In multinomial logistic regression we have K separate weight vectors corresponding to the K classes, all packed into a single weight matrix W, and a vector output ŷ. We omit the biases from both figures for clarity.
4.8 Learning in Multinomial Logistic Regression
The loss function for multinomial logistic regression generalizes the loss function for binary logistic regression from 2 to K classes. Recall that the cross-entropy loss for binary logistic regression (repeated from Eq. 4.19) is:
=− log p(y|x) = − [y log ŷ+(1− y) log(1− ŷ)] (4.37)
The loss function for multinomial logistic regression generalizes the two terms in Eq. 4.37 (one that is non-zero when y = 1 and one that is non-zero when y = 0) to K terms. As we mentioned above, for multinomial regression we’ll represent both y and ŷ as vectors. The true label y is a vector with K elements, each corresponding to a class, with yc = 1 if the correct class is c, with all other elements of y being 0. And our classifier will produce an estimate vector with K elements ŷ, each element ŷk of which represents the estimated probability p(yk = 1|x).
82 CHAPTER 4 • LOGISTIC REGRESSION
The loss function for a single example x, generalizing from binary logistic re-gression, is the sum of the logs of the K output classes, each weighted by the indi-cator function yk (Eq. 4.38). This turns out to be just the negative log probability of the correct class c (Eq. 4.39):
yk log ŷk (4.38)
(where c is the correct class) (4.39)
= − log p̂(yc = 1|x) (where c is the correct class)
= − log exp(wc
j=1 exp(wj ·x+b j)
(c is the correct class) (4.40)
How did we get from Eq. 4.38 to Eq. 4.39? Because only one class (let’s call it c) is the correct one, the vector y takes the value 1 only for this value of k, i.e., has yc = 1 and y j = 0
j 6= c. That means the terms in the sum in Eq. 4.38 will all be 0 except for the term corresponding to the true class c. Hence the cross-entropy loss is simply the log of the output probability corresponding to the correct class, and we therefore also call Eq. 4.39 the negative log likelihood loss.negative log
likelihood loss Of course for gradient descent we don’t need the loss, we need its gradient. The
gradient for a single example turns out to be very similar to the gradient for binary logistic regression, (ŷ−y)x, that we saw in Eq. 4.26. Let’s consider one piece of the gradient, the derivative for a single weight. For each class k, the weight of the ith element of input x is
What is the partial derivative of the loss with respect to
This derivative turns out to be just the difference between the true value for the class k (which is either 1 or 0) and the probability the classifier outputs for class k, weighted by the value of the input xi corresponding to the ith element of the weight vector for class k:
= −(yk− ŷk)xi
= −(yk− p(yk = 1|x))xi
j=1 exp(wj ·x+b j)
) xi (4.41)
We’ll return to this case of the gradient for softmax regression when we introduce neural networks in Chapter 6, and at that time we’ll also discuss the derivation of this gradient in equations Eq. 6.35–Eq. 6.43.
4.9 Evaluation: Precision, Recall, F-measure
To introduce the methods for evaluating text classification, let’s first consider some simple binary detection tasks. For example, in spam detection, our goal is to label every text as being in the spam category (“positive”) or not in the spam category (“negative”). For each item (email document) we therefore need to know whether our system called it spam or not. We also need to know whether the email is actually spam or not, i.e. the human-defined labels for each document that we are trying to match. We will refer to these human labels as the gold labels.gold labels
4.9 • EVALUATION: PRECISION, RECALL, F-MEASURE 83
Or imagine you’re the CEO of the Delicious Pie Company and you need to know what people are saying about your pies on social media, so you build a system that detects tweets concerning Delicious Pie. Here the positive class is tweets about Delicious Pie and the negative class is all other tweets.
In both cases, we need a metric for knowing how well our spam detector (or pie-tweet-detector) is doing. To evaluate any system for detecting things, we start by building a confusion matrix like the one shown in Fig. 4.7. A confusion matrixconfusion
matrix is a table for visualizing how an algorithm performs with respect to the human gold labels, using two dimensions (system output and gold labels), and each cell labeling a set of possible outcomes. In the spam detection case, for example, true positives are documents that are indeed spam (indicated by human-created gold labels) that our system correctly said were spam. False negatives are documents that are indeed spam but our system incorrectly labeled as non-spam.
To the bottom right of the table is the equation for accuracy, which asks what percentage of all the observations (for the spam or pie examples that means all emails or tweets) our system labeled correctly. Although accuracy might seem a natural metric, we generally don’t use it for text classification tasks. That’s because accuracy doesn’t work well when the classes are unbalanced (as indeed they are with spam, which is a large majority of email, or with tweets, which are mainly not about pie).
true positive
false negative
false positive
true negative
gold positive gold negative system positive system
gold standard labels
system output labels
recall = tp
precision = tp
accuracy = tp+tn
tp+fp+tn+fn
Figure 4.7 A confusion matrix for visualizing how well a binary classification system per-forms against gold standard labels.
To make this more explicit, imagine that we looked at a million tweets, and let’s say that only 100 of them are discussing their love (or hatred) for our pie, while the other 999,900 are tweets about something completely unrelated. Imagine a simple classifier that stupidly classified every tweet as “not about pie”. This classifier would have 999,900 true negatives and only 100 false negatives for an accuracy of 999,900/1,000,000 or 99.99%! What an amazing accuracy level! Surely we should be happy with this classifier? But of course this fabulous ‘no pie’ classifier would be completely useless, since it wouldn’t find a single one of the customer comments we are looking for. In other words, accuracy is not a good metric when the goal is to discover something that is rare, or at least not completely balanced in frequency, which is a very common situation in the world.
That’s why instead of accuracy we generally turn to two other metrics shown in Fig. 4.7: precision and recall. Precision measures the percentage of the items thatprecision
the system detected (i.e., the system labeled as positive) that are in fact positive (i.e., are positive according to the human gold labels). Precision is defined as
Precision = true positives
true positives + false positives
84 CHAPTER 4 • LOGISTIC REGRESSION
Recall measures the percentage of items actually present in the input that wererecall
correctly identified by the system. Recall is defined as
Recall = true positives
true positives + false negatives
Precision and recall will help solve the problem with the useless “nothing is pie” classifier. This classifier, despite having a fabulous accuracy of 99.99%, has a terrible recall of 0 (since there are no true positives, and 100 false negatives, the recall is 0/100). You should convince yourself that the precision at finding relevant tweets is equally problematic. Thus precision and recall, unlike accuracy, emphasize true positives: finding the things that we are supposed to be looking for.
There are many ways to define a single metric that incorporates aspects of both precision and recall. The simplest of these combinations is the F-measure (vanF-measure
Rijsbergen, 1975) , defined as:
parameter differentially weights the importance of recall and precision, based perhaps on the needs of an application. Values of
1 favor recall, while values of
1 favor precision. When
= 1, precision and recall are equally bal-anced; this is the most frequently used metric, and is called
or just F1:F1
F-measure comes from a weighted harmonic mean of precision and recall. The harmonic mean of a set of numbers is the reciprocal of the arithmetic mean of recip-rocals:
HarmonicMean(a1,a2,a3,a4, ...,an)
and hence F-measure is
Harmonic mean is used because the harmonic mean of two values is closer to the minimum of the two values than the arithmetic mean is. Thus it weighs the lower of the two numbers more heavily, which is more conservative in this situation.
4.9.1 Evaluating with more than two classes The simple example we gave above in defining precision and recall involved text classification with only two classes. But as we saw in Section 4.7, lots of NLP classification tasks have more than two classes. Even for sentiment analysis we often have 3 classes (positive, negative, neutral) and many more classes are common in tasks like text classification or emotion detection, and so on.
To deal with more than two classes we’ll need to slightly modify our definitions of precision and recall. Consider the sample confusion matrix for a hypothetical 3-way one-of email categorization decision (urgent, normal, spam) shown in Fig. 4.8.
4.10 • TEST SETS AND CROSS-VALIDATION 85
urgent normal
gold labels
system output
precisionu=
recalln = recalls =
precisionn=
precisions=
60 10+60+30
200 1+50+200
Figure 4.8 Confusion matrix for a three-class categorization task, showing for each pair of classes
how many documents from c1 were (in)correctly assigned to c2.
The matrix shows, for example, that the system mistakenly labeled one spam docu-ment as urgent, and we have shown how to compute a distinct precision and recall value for each class. In order to derive a single metric that tells us how well the system is doing, we can combine these values in two ways. In macroaveraging,macroaveraging
we compute the performance for each class, and then average over classes. In mi-croaveraging, we collect the decisions for all classes into a single confusion matrix,microaveraging
and then compute precision and recall from that table. Fig. 4.9 shows the confusion matrix for each class separately, and shows the computation of microaveraged and macroaveraged precision.
true urgent
system urgent
true normal
system normal system
system spam
precision = 8+11
8 = .42 precision =
= .86precision = 60+55
60 = .52 microaverage
precision 268+99 268
macroaverage precision 3
.42+.52+.86 = .60=
PooledClass 3: SpamClass 2: NormalClass 1: Urgent
Figure 4.9 Separate confusion matrices for the 3 classes from the previous figure, showing the pooled confu-sion matrix and the microaveraged and macroaveraged precision.
As the figure shows, a microaverage is dominated by the more frequent class (in this case spam), since the counts are pooled. The macroaverage better reflects the statistics of the smaller classes, and so is more appropriate when performance on all the classes is equally important.
4.10 Test sets and Cross-validation
The training and testing procedure for text classification follows what we saw with language modeling (Section 3.2): we use the training set to train the model, then use the development test set (also called a devset) to perhaps tune some parameters,development
test set devset
86 CHAPTER 4 • LOGISTIC REGRESSION
and in general decide what the best model is. Once we come up with what we think is the best model, we run it on the (hitherto unseen) test set to report its performance.
While the use of a devset avoids overfitting the test set, having a fixed train-ing set, devset, and test set creates another problem: in order to save lots of data for training, the test set (or devset) might not be large enough to be representative. Wouldn’t it be better if we could somehow use all our data for training and still use all our data for test? We can do this by cross-validation.cross-validation
In cross-validation, we choose a number k, and partition our data into k disjoint subsets called folds. Now we choose one of those k folds as a test set, train ourfolds
classifier on the remaining k− 1 folds, and then compute the error rate on the test set. Then we repeat with another fold as the test set, again training on the other k−1 folds. We do this sampling process k times and average the test set error rate from these k runs to get an average error rate. If we choose k = 10, we would train 10 different models (each on 90% of our data), test the model 10 times, and average these 10 values. This is called 10-fold cross-validation.10-fold
cross-validation The only problem with cross-validation is that because all the data is used for
testing, we need the whole corpus to be blind; we can’t examine any of the data to suggest possible features and in general see what’s going on, because we’d be peeking at the test set, and such cheating would cause us to overestimate the perfor-mance of our system. However, looking at the corpus to understand what’s going on is important in designing NLP systems! What to do? For this reason, it is com-mon to create a fixed training set and test set, then do 10-fold cross-validation inside the training set, but compute error rate the normal way in the test set, as shown in Fig. 4.10.
Training Iterations
Training Training
Training Training
Training Training
Training Training
Training Training
Training Test Set
Figure 4.10 10-fold cross-validation
4.11 Statistical Significance Testing
In building systems we often need to compare the performance of two systems. How can we know if the new system we just built is better than our old one? Or better than some other system described in the literature? This is the domain of statistical hypothesis testing, and in this section we introduce tests for statistical significance for NLP classifiers, drawing especially on the work of Dror et al. (2020) and Berg-Kirkpatrick et al. (2012).
4.11 • STATISTICAL SIGNIFICANCE TESTING 87
Suppose we’re comparing the performance of classifiers A and B on a metric M such as F1, or accuracy. Perhaps we want to know if our new sentiment classifier A gets a higher F1 score than our previous sentiment classifier B on a particular test set x. Let’s call
the score that system A gets on test set x, and
(x) the performance difference between A and B on x:
M(A,x)−M(B,x)
We would like to know if
0, meaning that our new classifier A has a higher F1 than our old classifier B on x.
(x) is called the effect size; a bigger
means thateffect size
A seems to be way better than B; a small
means A seems to be only a little better. Why don’t we just check if
(x) is positive? Suppose we do, and we find that
the F1 score of A is higher than B’s by .04. Can we be certain that A is better? We cannot! That’s because A might just be accidentally better than B on this particular x. We need something more: we want to know if A’s superiority over B is likely to hold again if we checked another test set x′, or under some other set of circumstances.
In the paradigm of statistical hypothesis testing, we test this by formalizing two hypotheses.
The hypothesis H0, called the null hypothesis, supposes that
(x) is actually nega-null hypothesis
tive or zero, meaning that A is not better than B. We would like to know if we can confidently rule out this hypothesis, and instead support H1, that A is better.
We do this by creating a random variable X ranging over all test sets. Now we ask how likely is it, if the null hypothesis H0 was correct, that among these test sets we would encounter the value of
(x) that we found, if we repeated the experiment a great many times. We formalize this likelihood as the p-value: the probability,p-value
assuming the null hypothesis H0 is true, of seeing the
(x) that we saw or one even greater
(x)|H0 is true) (4.47)
So in our example, this p-value is the probability that we would see
(x) assuming A is not better than B. If
(x) is huge (let’s say A has a very respectable F1 of .9 and B has a terrible F1 of only .2 on x), we might be surprised, since that would be extremely unlikely to occur if H0 were in fact true, and so the p-value would be low (unlikely to have such a large
if A is in fact not better than B). But if
(x) is very small, it might be less surprising to us even if H0 were true and A is not really better than B, and so the p-value would be higher.
A very small p-value means that the difference we observed is very unlikely under the null hypothesis, and we can reject the null hypothesis. What counts as very small? It is common to use values like .05 or .01 as the thresholds. A value of .01 means that if the p-value (the probability of observing the
we saw assuming H0 is true) is less than .01, we reject the null hypothesis and assume that A is indeed better than B. We say that a result (e.g., “A is better than B”) is statistically significant ifstatistically
significant the
we saw has a probability that is below the threshold and we therefore reject this null hypothesis.
How do we compute this probability we need for the p-value? In NLP we gen-erally don’t use simple parametric tests like t-tests or ANOVAs that you might be familiar with. Parametric tests make assumptions about the distributions of the test
88 CHAPTER 4 • LOGISTIC REGRESSION
statistic (such as normality) that don’t generally hold in our cases. So in NLP we usually use non-parametric tests based on sampling: we artificially create many ver-sions of the experimental setup. For example, if we had lots of different test sets x′
we could just measure all the
(x′) for all the x′. That gives us a distribution. Now we set a threshold (like .01) and if we see in this distribution that 99% or more of those deltas are smaller than the delta we observed, i.e., that p-value(x)—the proba-bility of seeing a
(x) as big as the one we saw—is less than .01, then we can reject the null hypothesis and agree that
(x) was a sufficiently surprising difference and A is really a better algorithm than B.
There are two common non-parametric tests used in NLP: approximate ran-domization (Noreen, 1989) and the bootstrap test. We will describe bootstrapapproximate
randomization below, showing the paired version of the test, which again is most common in NLP. Paired tests are those in which we compare two sets of observations that are aligned:paired
each observation in one set can be paired with an observation in another. This hap-pens naturally when we are comparing the performance of two systems on the same test set; we can pair the performance of system A on an individual observation xi with the performance of system B on the same xi.
4.11.1 The Paired Bootstrap Test
The bootstrap test (Efron and Tibshirani, 1993) can apply to any metric; from pre-bootstrap test
cision, recall, or F1 to the BLEU metric used in machine translation. The word bootstrapping refers to repeatedly drawing large numbers of samples with replace-bootstrapping
ment (called bootstrap samples) from an original set. The intuition of the bootstrap test is that we can create many virtual test sets from an observed test set by repeat-edly sampling from it. The method only makes the assumption that the sample is representative of the population.
Consider a tiny text classification example with a test set x of 10 documents. The first row of Fig. 4.11 shows the results of two classifiers (A and B) on this test set. Each document is labeled by one of the four possibilities (A and B both right, both wrong, A right and B wrong, A wrong and B right). A slash through a letter ( B) means that that classifier got the answer wrong. On the first document both A and B get the correct class (AB), while on the second document A got it right but B got it wrong (A B). If we assume for simplicity that our metric is accuracy, A has an accuracy of .70 and B of .50, so
(x) is .20.
Now we create a large number b (perhaps 105) of virtual test sets x(i), each of size n = 10. Fig. 4.11 shows a couple of examples. To create each virtual test set x(i), we repeatedly (n = 10 times) select a cell from row x with replacement. For example, to create the first cell of the first virtual test set x(1), if we happened to randomly select the second cell of the x row, we would copy the value A B into our new cell, and move on to create the second cell of x(1), each time sampling (randomly choosing) from the original x with replacement.
Now that we have the b test sets, providing a sampling distribution, we can do statistics on how often A has an accidental advantage. There are various ways to compute this advantage; here we follow the version laid out in Berg-Kirkpatrick et al. (2012). Assuming H0 (A isn’t better than B), we would expect that
(X), estimated over many test sets, would be zero or negative; a much higher value would be surprising, since H0 specifically assumes A isn’t better than B. To measure exactly how surprising our observed
(x) is, we would in other circumstances compute the p-value by counting over many test sets how often
(x(i)) exceeds the expected zero
4.12 • AVOIDING HARMS IN CLASSIFICATION 89
1 2 3 4 5 6 7 8 9 10 A% B%
() x AB A B AB