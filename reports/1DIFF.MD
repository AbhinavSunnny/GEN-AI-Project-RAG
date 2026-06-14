# RAG Pipeline Comparison Project – Experimental Design and Evaluation Strategy

## 1. Project Objective

The objective of this project is to compare different Retrieval-Augmented Generation (RAG) architectures and Large Language Models (LLMs) to determine their effectiveness in information retrieval and answer generation.

The project evaluates:

### Retrieval Architectures

1. Dense RAG
2. Hybrid RAG (Dense + Sparse Retrieval using RRF)
3. Fusion RAG (Dense + Sparse + Web Retrieval)

### Language Models

1. GPT-4o
2. Llama 3
3. Mistral-7B

This results in a total of:

9 Experimental Pipelines

* Dense GPT-4o
* Hybrid GPT-4o
* Fusion GPT-4o
* Dense Llama 3
* Hybrid Llama 3
* Fusion Llama 3
* Dense Mistral
* Hybrid Mistral
* Fusion Mistral

---

## 2. Dataset Selection

The CNN/DailyMail dataset containing 20,000 processed news articles is used as the knowledge corpus.

The dataset contains:

* News Articles
* Human-written Highlights

The articles serve as the knowledge source for retrieval.

The highlights are retained for future evaluation experiments involving reference-based metrics.

---

## 3. Why Use the Entire 20K Dataset?

The goal of a Retrieval-Augmented Generation system is to retrieve information from a large corpus.

Using only a small subset would not accurately represent a real-world retrieval environment.

Therefore:

20,000 Articles
↓
Chunking
↓
Embedding Generation
↓
FAISS Index
↓
BM25 Index

This creates a realistic retrieval corpus from which all pipelines retrieve information.

The entire dataset is therefore used for:

* Chunking
* Dense Retrieval
* Sparse Retrieval
* Hybrid Retrieval
* Fusion Retrieval

---

## 4. Retrieval Approaches

### Dense RAG

Dense RAG uses semantic embeddings.

Process:

User Query
↓
FAISS Vector Search
↓
Top-K Relevant Chunks
↓
Context Construction
↓
LLM Response

Advantages:

* Captures semantic meaning
* Good for paraphrased queries

Limitations:

* May miss exact keyword matches

---

### Hybrid RAG

Hybrid RAG combines:

* Dense Retrieval (FAISS)
* Sparse Retrieval (BM25)

Results are combined using Reciprocal Rank Fusion (RRF).

Process:

Query
↓
FAISS Results
+
BM25 Results
↓
RRF Fusion
↓
Top Documents
↓
LLM Response

Advantages:

* Combines semantic and keyword matching
* More robust retrieval

---

### Fusion RAG

Fusion RAG extends Hybrid RAG by incorporating external web information.

Process:

Query
↓
FAISS Results
+
BM25 Results
+
Web Results
↓
Fusion
↓
Context Construction
↓
LLM Response

Advantages:

* Broader knowledge coverage
* Access to external information

Limitations:

* Increased latency
* Larger context sizes

---

## 5. Language Models

### GPT-4o

Cloud-based proprietary model.

Advantages:

* High reasoning ability
* Strong instruction following
* High answer quality

---

### Llama 3

Open-source model.

Advantages:

* Strong performance
* Lower cost
* Self-hosting capability

---

### Mistral-7B

Lightweight open-source model.

Advantages:

* Local execution
* Lower hardware requirements
* Faster deployment

Limitations:

* Lower reasoning capability compared to GPT-4o

---

## 6. Evaluation Strategy

The project evaluates both retrieval quality and system performance.

Metrics are divided into two categories.

---

## 7. Retrieval Evaluation Metrics

These metrics evaluate how effectively the system retrieves information.

### Context Relevance

Measures similarity between:

Query
and
Retrieved Context

Purpose:

Determine whether retrieved context is relevant to the user's query.

Higher scores indicate better retrieval quality.

---

### Precision

Measures:

Relevant Retrieved Documents
/
Total Retrieved Documents

Purpose:

Determine the percentage of retrieved documents that are actually relevant.

Higher precision indicates fewer irrelevant documents.

---

### Recall

Measures:

Relevant Retrieved Documents
/
Total Relevant Documents

Purpose:

Determine how many relevant documents were successfully retrieved.

Higher recall indicates better coverage.

---

### Mean Reciprocal Rank (MRR)

Measures the ranking position of the first relevant document.

Formula:

MRR = 1 / Rank

Purpose:

Evaluate ranking quality.

Higher MRR indicates relevant information appears earlier in results.

---

## 8. Performance Evaluation Metrics

### Latency

Measures total response generation time.

Includes:

* Retrieval time
* Context construction
* Model generation time

Purpose:

Evaluate system responsiveness.

Lower latency is preferred.

---

### Memory Usage

Measures RAM consumed during execution.

Purpose:

Evaluate computational efficiency.

Lower memory consumption indicates better scalability.

---

## 9. Why ROUGE-L, BLEU, and BERTScore Are Not Primary Metrics

ROUGE-L, BLEU, and BERTScore are reference-based summarization metrics.

They require:

Generated Output
vs
Ground Truth Reference Output

However, the current project is designed as a Question Answering RAG system:

Query
↓
Retrieval
↓
Answer Generation

rather than a summarization system:

Document
↓
Summary Generation

Therefore retrieval-focused metrics are more appropriate for evaluating system effectiveness.

Reference-based metrics may be added later through a dedicated evaluation dataset containing query-answer pairs.

---

## 10. Information Saved by Each Pipeline

Each pipeline will save:

* Query
* Retrieved Documents
* Retrieved Count
* Context
* Generated Answer
* Latency
* Memory Usage

These outputs provide all information required to compute:

* Context Relevance
* Precision
* Recall
* MRR
* Latency
* Memory Usage

for every pipeline.

---

## 11. Expected Outcome

The project will provide a comprehensive comparison of:

* Dense Retrieval
* Hybrid Retrieval
* Fusion Retrieval

across:

* GPT-4o
* Llama 3
* Mistral-7B

using retrieval effectiveness and computational performance metrics.

The results will identify the trade-offs between retrieval quality, response quality, execution speed, and resource consumption.
