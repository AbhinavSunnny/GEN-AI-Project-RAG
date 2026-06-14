# Evaluation Metrics Explanation

This notebook uses three generation evaluation metrics and three retrieval evaluation metrics to assess the performance of different Retrieval-Augmented Generation (RAG) pipelines.

---

# 1. ROUGE-L

## Definition

ROUGE stands for:

**Recall-Oriented Understudy for Gisting Evaluation**

ROUGE-L measures the similarity between the generated answer and the reference summary using the **Longest Common Subsequence (LCS)**.

It evaluates how much of the reference content appears in the generated answer while preserving word order.

### Example

Reference:

```text
The cat sat on the mat
```

Generated Answer:

```text
The cat is sitting on the mat
```

Common Sequence:

```text
The cat on the mat
```

ROUGE-L measures the overlap between these sequences.

---

## Range

```text
0 to 1
```

---

## Interpretation

| ROUGE-L Score | Interpretation |
|--------------|----------------|
| 0.0 | No overlap |
| 0.2 | Weak overlap |
| 0.4 | Good overlap |
| 0.6+ | Strong overlap |
| 1.0 | Perfect match |

---

## Desired Value

✅ Higher is Better

A higher ROUGE-L score indicates that the generated answer contains more information from the reference summary.

---

# 2. BLEU

## Definition

BLEU stands for:

**Bilingual Evaluation Understudy**

BLEU measures n-gram overlap between the generated answer and the reference summary.

It evaluates whether the generated answer uses similar words and phrases as the reference.

---

## Example

Reference:

```text
The company reported strong earnings
```

Generated Answer:

```text
The company reported excellent earnings
```

Although the meaning is similar, BLEU decreases because:

```text
strong ≠ excellent
```

---

## Range

```text
0 to 1
```

---

## Interpretation

| BLEU Score | Interpretation |
|------------|----------------|
| 0.0 | No overlap |
| 0.1 | Weak |
| 0.3 | Good |
| 0.5+ | Very Good |
| 1.0 | Exact Match |

---

## Desired Value

✅ Higher is Better

A higher BLEU score indicates greater lexical similarity between the generated answer and the reference summary.

---

# 3. BERTScore

## Definition

BERTScore uses contextual embeddings from transformer models such as BERT or RoBERTa to compare the semantic similarity between the generated answer and the reference summary.

Unlike ROUGE and BLEU, BERTScore focuses on meaning rather than exact word matching.

---

## Example

Reference:

```text
The company reported strong earnings
```

Generated Answer:

```text
The organization announced excellent profits
```

BLEU:

```text
Low
```

BERTScore:

```text
High
```

because both sentences convey a similar meaning.

---

## Range

```text
0 to 1
```

---

## Interpretation

| BERTScore | Interpretation |
|------------|----------------|
| 0.5 | Weak |
| 0.7 | Good |
| 0.8 | Very Good |
| 0.9+ | Excellent |

---

## Desired Value

✅ Higher is Better

A higher BERTScore indicates stronger semantic similarity between the generated answer and the reference summary.

---

# 4. Precision

## Definition

Precision measures how many retrieved documents are actually relevant.

### Formula

Precision = Relevant Retrieved Documents / Total Retrieved Documents

---

## Example

Retrieved Documents:

```text
10
```

Relevant Documents:

```text
8
```

Precision:

```text
8 / 10 = 0.80
```

---

## Range

```text
0 to 1
```

---

## Desired Value

✅ Higher is Better

A higher Precision score indicates that fewer irrelevant documents were retrieved.

---

# 5. Recall

## Definition

Recall measures how many relevant documents were successfully retrieved from all available relevant documents.

### Formula

Recall = Relevant Retrieved Documents / Total Relevant Documents

---

## Example

Available Relevant Documents:

```text
20
```

Retrieved Relevant Documents:

```text
15
```

Recall:

```text
15 / 20 = 0.75
```

---

## Range

```text
0 to 1
```

---

## Desired Value

✅ Higher is Better

A higher Recall score indicates that more relevant information was retrieved.

---

# 6. Mean Reciprocal Rank (MRR)

## Definition

MRR evaluates how early the first relevant document appears in the retrieval ranking.

### Formula

MRR = 1 / Rank of First Relevant Document

---

## Examples

Relevant Document at Rank 1:

```text
MRR = 1/1 = 1.0
```

Relevant Document at Rank 2:

```text
MRR = 1/2 = 0.5
```

Relevant Document at Rank 5:

```text
MRR = 1/5 = 0.2
```

---

## Range

```text
0 to 1
```

---

## Desired Value

✅ Higher is Better

A higher MRR score indicates that relevant documents are appearing earlier in the ranked retrieval results.

---

# Summary Table

| Metric | Purpose | Range | Desired Value |
|----------|----------|----------|----------|
| ROUGE-L | Longest Common Subsequence Similarity | 0-1 | Higher Better |
| BLEU | N-Gram Similarity | 0-1 | Higher Better |
| BERTScore | Semantic Similarity | 0-1 | Higher Better |
| Precision | Retrieval Accuracy | 0-1 | Higher Better |
| Recall | Retrieval Coverage | 0-1 | Higher Better |
| MRR | Retrieval Ranking Quality | 0-1 | Higher Better |

---

# Best Generation Result

Based on the experimental results:

| Pipeline | ROUGE-L | BLEU | BERTScore |
|----------|----------|----------|----------|
| Fusion GPT4o | 0.2977 | 0.0476 | 0.8588 |

Fusion GPT4o achieved the highest scores across all generation metrics, indicating superior lexical overlap and semantic similarity with the reference summaries.

This demonstrates that combining Dense Retrieval, Sparse Retrieval, and Web Search provides the most effective retrieval strategy for enhancing RAG system performance.

======================================================================================================================================================================

# Analysis of Generation Evaluation Results

The performance of nine Retrieval-Augmented Generation (RAG) pipelines was evaluated using ROUGE-L, BLEU, and BERTScore metrics.

## Best Performing Pipeline

Among all evaluated pipelines, **Fusion GPT4o** achieved the highest performance across all evaluation metrics.

| Metric | Score |
|----------|----------|
| ROUGE-L | 0.297738 |
| BLEU | 0.047550 |
| BERTScore | 0.858821 |

This indicates that Fusion GPT4o generated answers that were both lexically similar and semantically closer to the reference summaries compared to all other pipelines.

---

## Why Fusion GPT4o Performed Best

The Fusion GPT4o pipeline combines three retrieval sources:

1. Dense Retrieval (FAISS + Embeddings)
2. Sparse Retrieval (BM25)
3. Web Search Retrieval

These retrieval results are combined and provided as context to GPT4o.

This approach offers several advantages:

- Dense retrieval captures semantic similarity.
- Sparse retrieval captures exact keyword matches.
- Web search introduces additional external knowledge.
- GPT4o effectively synthesizes information from multiple sources.

As a result, the model receives richer and more relevant context before generating responses.

---

## ROUGE-L Analysis

Fusion GPT4o achieved the highest ROUGE-L score of **0.297738**.

ROUGE-L measures the overlap between the generated answer and the reference summary using the Longest Common Subsequence (LCS).

A higher ROUGE-L score indicates that the generated answer preserves more information from the reference summary.

The superior ROUGE-L score suggests that Fusion GPT4o was able to capture important concepts and factual content more accurately than other pipelines.

---

## BLEU Analysis

Fusion GPT4o achieved the highest BLEU score of **0.047550**.

BLEU evaluates word and phrase overlap between generated and reference texts.

Although BLEU values appear numerically low, this is common in abstractive summarization and generative question-answering tasks where multiple valid phrasings may exist.

The highest BLEU score indicates that Fusion GPT4o produced responses with greater lexical similarity to the reference summaries.

---

## BERTScore Analysis

Fusion GPT4o achieved the highest BERTScore of **0.858821**.

BERTScore evaluates semantic similarity using transformer embeddings.

Unlike ROUGE and BLEU, BERTScore focuses on meaning rather than exact wording.

The high BERTScore demonstrates that Fusion GPT4o generated answers whose meanings closely matched the reference summaries.

This metric is particularly important for RAG systems because semantic correctness is often more valuable than exact word matching.

---

## Comparison with Other Pipelines

Hybrid Mistral and Fusion Mistral achieved the second and third highest BERTScores respectively.

| Pipeline | BERTScore |
|----------|----------|
| Fusion GPT4o | 0.858821 |
| Hybrid Mistral | 0.851480 |
| Fusion Mistral | 0.849840 |

This indicates that Mistral performed competitively despite being a smaller local model.

Llama3 pipelines generally achieved lower scores compared to GPT4o and Mistral, suggesting that retrieval improvements alone cannot fully compensate for differences in language model capabilities.

---

## Key Observation

The results demonstrate that retrieval strategy significantly impacts answer quality.

Across all models:

Fusion Retrieval > Hybrid Retrieval > Dense Retrieval

in most evaluation scenarios.

This validates the hypothesis that combining multiple retrieval techniques provides richer contextual information and improves generation performance.

---

## Conclusion

Based on ROUGE-L, BLEU, and BERTScore results, Fusion GPT4o was identified as the best-performing pipeline.

Its superior performance can be attributed to the combination of dense retrieval, sparse retrieval, web search augmentation, and GPT4o's strong reasoning and language generation capabilities.

Therefore, Fusion GPT4o is selected as the optimal Retrieval-Augmented Generation pipeline in this study.