# Final Evaluation Metrics Used in the Project

## Overview

The performance of the Retrieval-Augmented Generation (RAG) system was evaluated using a combination of retrieval efficiency metrics and generation quality metrics.

Due to the absence of explicit relevance labels for retrieved documents, traditional retrieval metrics such as Precision, Recall, and Mean Reciprocal Rank (MRR) could not be computed reliably. Therefore, the evaluation focused on metrics that were directly available from the experimental outputs and generation results.

---

# Evaluation Metrics Summary

| Metric          | Purpose                                                                    | Interpretation                     | Desired Value |
| --------------- | -------------------------------------------------------------------------- | ---------------------------------- | ------------- |
| Retrieved Count | Measures the number of documents retrieved for a query                     | Indicates retrieval volume         | Higher        |
| Context Length  | Measures the amount of context supplied to the language model              | Indicates retrieval coverage       | Higher        |
| Latency         | Measures response generation time                                          | Indicates system speed             | Lower         |
| Memory Usage    | Measures memory consumed during retrieval and generation                   | Indicates computational efficiency | Lower         |
| ROUGE-L         | Measures overlap between generated answer and reference summary            | Indicates content preservation     | Higher        |
| BLEU            | Measures lexical similarity between generated answer and reference summary | Indicates phrase-level similarity  | Higher        |
| BERTScore       | Measures semantic similarity using transformer embeddings                  | Indicates meaning preservation     | Higher        |

---

# Retrieval Efficiency Metrics

## Retrieved Count

Retrieved Count represents the total number of documents returned by the retrieval system for a given query.

A higher retrieved count generally increases the likelihood of obtaining relevant information, although excessively large retrieval sets may introduce noise.

---

## Context Length

Context Length represents the total number of characters supplied to the language model after retrieval.

Larger context sizes provide more information to the language model but may increase computational cost and response latency.

---

## Latency

Latency measures the total time required to retrieve information and generate a response.

Lower latency indicates a faster and more responsive system.

---

## Memory Usage

Memory Usage measures the amount of system memory consumed during retrieval and generation.

Lower memory usage indicates better resource efficiency and scalability.

---

# Generation Quality Metrics

## ROUGE-L

ROUGE-L evaluates the overlap between generated answers and reference summaries using the Longest Common Subsequence (LCS).

Higher ROUGE-L scores indicate better preservation of important information from the reference summaries.

---

## BLEU

BLEU evaluates n-gram overlap between generated answers and reference summaries.

Higher BLEU scores indicate stronger lexical similarity and phrase-level matching.

---

## BERTScore

BERTScore uses contextual embeddings from transformer models to measure semantic similarity between generated answers and reference summaries.

Unlike ROUGE-L and BLEU, BERTScore focuses on meaning rather than exact wording.

Higher BERTScore values indicate stronger semantic alignment with the reference summaries.

---

# Best Performing Pipeline

Based on the experimental evaluation results:

| Pipeline     | ROUGE-L  | BLEU     | BERTScore |
| ------------ | -------- | -------- | --------- |
| Fusion GPT4o | 0.297738 | 0.047550 | 0.858821  |

Fusion GPT4o achieved the highest scores across all generation quality metrics.

This pipeline combines:

* Dense Retrieval (FAISS)
* Sparse Retrieval (BM25)
* Web Search Retrieval
* GPT4o Language Model

The results demonstrate that combining multiple retrieval strategies provides richer contextual information and leads to improved answer quality.

---

# Final Conclusion

The experimental findings show that retrieval strategy significantly impacts the performance of Retrieval-Augmented Generation systems.

Among all evaluated pipelines, Fusion GPT4o consistently achieved the best overall performance in terms of lexical similarity, semantic similarity, and information preservation.

Therefore, Fusion GPT4o is identified as the optimal RAG pipeline for this project and serves as the final recommended architecture based on the conducted experiments.


======================================================================================================================================================================
