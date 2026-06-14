# Evaluation Strategy Revision Report

## Project Title

Comparative Evaluation of Dense, Hybrid, and Fusion Retrieval-Augmented Generation (RAG) Pipelines using GPT4o, Llama3, and Mistral

---

# Original Evaluation Plan

The initial objective was to evaluate all nine RAG pipelines using:

500 evaluation samples

for each pipeline.

The planned evaluation pipelines were:

GPT4o

* Dense GPT4o
* Hybrid GPT4o
* Fusion GPT4o

Llama3

* Dense Llama3
* Hybrid Llama3
* Fusion Llama3

Mistral

* Dense Mistral
* Hybrid Mistral
* Fusion Mistral

This would have produced:

9 pipelines × 500 rows

= 4500 generated responses

for evaluation.

---

# GPT4o Evaluation Phase

The GPT4o evaluation phase was completed successfully.

Generated outputs:

* dense_gpt4o_eval.csv
* hybrid_gpt4o_eval.csv
* fusion_gpt4o_eval.csv

These files contain:

* query
* reference_summary
* generated_answer

and are suitable for:

* ROUGE-L
* BLEU
* BERTScore

evaluation.

---

# Transition to Local Models

After GPT4o evaluation was completed, attention shifted to:

* Llama3
* Mistral

which are executed locally through Ollama.

Example:

llm = ChatOllama(
model="llama3"
)

or

llm = ChatOllama(
model="mistral"
)

Unlike GPT4o, these models run entirely on local hardware.

---

# Performance Investigation

A speed benchmark was executed using:

response = llm.invoke(
"What is Artificial Intelligence?"
)

Execution time:

83.13 seconds

for a single response.

---

# Context Verification

To ensure that the delay was not caused by excessively large prompts, retrieval context size was measured.

Query:

"artificial intelligence"

Retrieved Documents:

5

Context Length:

2480 characters

Result:

The context size was reasonable and not responsible for the slowdown.

---

# Root Cause

The bottleneck was identified as local Llama3 inference.

The following components were verified as functioning correctly:

* FAISS retrieval
* OpenAI embeddings
* Context construction
* Prompt generation
* Ollama installation

The delay originated from:

response = llm.invoke(prompt)

which executes local Llama3 inference.

---

# Runtime Projection

Observed speed:

83.13 seconds per response

Estimated runtime for 500 rows:

500 × 83.13

= 41,565 seconds

≈ 693 minutes

≈ 11.5 hours

for a single notebook.

---

# Total Project Impact

Remaining notebooks:

Llama3

* Dense Llama3
* Hybrid Llama3
* Fusion Llama3

Mistral

* Dense Mistral
* Hybrid Mistral
* Fusion Mistral

Total:

6 notebooks

Projected runtime:

6 × 11.5 hours

≈ 69 hours

under worst-case assumptions.

This was deemed impractical.

---

# Evaluation Strategy Revision

A decision was made to reduce the evaluation sample size.

Original:

if idx >= 500:
break

Revised:

if idx >= 25:
break

for all remaining local-model evaluation notebooks.

---

# Why 25 Rows Was Selected

The purpose of the evaluation is comparative analysis rather than production deployment.

The project seeks to compare:

Retrieval Methods

* Dense
* Hybrid
* Fusion

Language Models

* GPT4o
* Llama3
* Mistral

rather than produce a large-scale benchmark.

Using 25 samples still provides:

* Comparable outputs
* Consistent retrieval behavior
* Metric computation
* Model comparison

while dramatically reducing runtime.

---

# Fairness Considerations

To maintain fairness, GPT4o evaluation outputs will also be restricted to the same evaluation subset.

For example:

dense_gpt4o_eval.csv

↓

dense_gpt4o_eval_25.csv

using:

df.head(25)

This ensures all models are evaluated on:

* identical queries
* identical reference summaries
* identical evaluation samples

---

# Final Evaluation Dataset

Each pipeline will use:

25 evaluation records

Resulting in:

9 pipelines × 25 rows

= 225 generated responses

for final comparison.

---

# Advantages of the Revised Approach

1. Reduced Runtime

From multiple days of computation

to a manageable timeframe.

---

2. Consistent Evaluation

All models are evaluated using the same examples.

---

3. Reproducibility

The evaluation set remains fixed.

---

4. Resource Efficiency

Avoids excessive local CPU and memory usage.

---

5. Sufficient for Comparative Analysis

The objective is to compare:

* retrieval methods
* language models

rather than establish state-of-the-art benchmark scores.

Twenty-five representative samples are sufficient to demonstrate performance differences.

---

# Final Evaluation Metrics

After all nine evaluation files are completed, the following metrics will be calculated:

Generation Metrics

* ROUGE-L
* BLEU
* BERTScore

Retrieval Metrics

* Precision
* Recall
* Mean Reciprocal Rank (MRR)

Performance Metrics

* Latency
* Memory Usage
* Context Length
* Response Length
* Context Relevance

---

# Final Conclusion

The original evaluation strategy of 500 samples per pipeline was revised after empirical benchmarking revealed that local Llama3 inference required approximately 83 seconds per response.

Executing 500 evaluations across six remaining local-model notebooks would have required an impractical amount of computation time.

To ensure project completion while preserving evaluation validity, the sample size was reduced to 25 records per pipeline. GPT4o outputs will be trimmed to the same evaluation subset, ensuring a fair and reproducible comparison across all retrieval methods and language models.
