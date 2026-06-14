# RAG System Development and Evaluation Report

## Project Objective

The goal of this project is to design, implement, and evaluate multiple Retrieval-Augmented Generation (RAG) architectures using different retrieval strategies and Large Language Models (LLMs).

The project compares:

### Retrieval Strategies

1. Dense Retrieval
2. Hybrid Retrieval
3. Fusion Retrieval

### Large Language Models

1. GPT-4o
2. Llama3
3. Mistral

This results in a total of nine unique RAG pipelines.

---

## Dataset Preparation

The CNN/DailyMail dataset was used as the primary knowledge source.

Dataset size:

* 20,000 news articles

Preprocessing included:

* Text cleaning
* Tokenization
* Summary extraction
* Metadata generation
* Article and summary normalization

Generated file:

cnn_processed20k.csv

---

## Retrieval Asset Construction

To support retrieval operations, two retrieval systems were built.

### Dense Retrieval Infrastructure

OpenAI embeddings:

text-embedding-3-small

were generated for document chunks.

The embeddings were indexed using:

FAISS

Generated asset:

faiss_20k/

---

### Sparse Retrieval Infrastructure

BM25 indexing was created using:

rank_bm25

Generated asset:

bm25_20k.pkl

---

### Chunk Repository

All processed chunks were stored for retrieval and evaluation.

Generated asset:

all_chunks.pkl

---

## RAG Pipelines Developed

### GPT-4o Pipelines

1. Dense GPT4o
2. Hybrid GPT4o
3. Fusion GPT4o

---

### Llama3 Pipelines

4. Dense Llama3
5. Hybrid Llama3
6. Fusion Llama3

---

### Mistral Pipelines

7. Dense Mistral
8. Hybrid Mistral
9. Fusion Mistral

---

## Retrieval Approaches

### Dense Retrieval

Workflow:

Query
→ OpenAI Embeddings
→ FAISS Search
→ Top-k Documents
→ LLM Generation

---

### Hybrid Retrieval

Workflow:

Query
→ Dense Retrieval (FAISS)

*

Sparse Retrieval (BM25)

→ Reciprocal Rank Fusion (RRF)

→ Top Documents

→ LLM Generation

---

### Fusion Retrieval

Workflow:

Query
→ Dense Retrieval

*

Sparse Retrieval

*

Web Search

→ Fusion Context

→ LLM Generation

---

## Performance Metrics Generated

For every pipeline the following metrics were collected:

* Latency
* Memory Usage
* Context Length
* Response Length

---

## Performance Evaluation Notebook

A dedicated evaluation notebook was created to compare:

* Average Latency
* Average Memory Usage
* Average Context Length
* Average Response Length
* Context Relevance

Context relevance was measured using:

OpenAI text-embedding-3-small

and cosine similarity.

---

## Evaluation Dataset Creation

A dedicated evaluation dataset was created from CNN/DailyMail.

Evaluation dataset contains:

* Query
* Article
* Reference Summary

Evaluation size:

1000 rows

Generated file:

evaluation_dataset.csv

---

## Current Status

Completed:

✓ Dataset preprocessing

✓ Retrieval asset creation

✓ FAISS index generation

✓ BM25 index generation

✓ Dense RAG pipelines

✓ Hybrid RAG pipelines

✓ Fusion RAG pipelines

✓ Performance metrics

✓ Evaluation dataset generation

Project is now ready for large-scale evaluation and benchmarking.
