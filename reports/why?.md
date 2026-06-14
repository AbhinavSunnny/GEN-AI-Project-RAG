# Rationale for Creating Additional Evaluation Pipelines

## Why Existing Pipeline Outputs Are Not Sufficient

The first nine notebooks were designed primarily for:

1. Retrieval testing
2. Pipeline comparison
3. Performance measurement

The outputs stored:

* Query
* Retrieved Documents
* Generated Answer
* Latency
* Memory Usage

These outputs are sufficient for operational evaluation.

However, they are not sufficient for summary-quality evaluation metrics.

---

## Metrics Still Required

The project still needs:

### Generation Metrics

* ROUGE-L
* BLEU
* BERTScore

### Retrieval Metrics

* Precision
* Recall
* Mean Reciprocal Rank (MRR)

---

## Why Additional Evaluation Files Are Needed

These metrics require a direct comparison between:

Reference Summary

and

Generated Output

For every evaluation sample.

The current pipeline result files do not contain:

Reference Summary

Therefore evaluation-specific output files must be generated.

---

## Evaluation Workflow

Input:

evaluation_dataset.csv

contains:

* Query
* Article
* Reference Summary

For each pipeline:

Query
→ Retrieval
→ Context Generation
→ LLM Response

Output:

* Query
* Reference Summary
* Generated Answer
* Pipeline Name
* Model
* Retrieval Method

---

## Why Separate Evaluation Files Are Better

Instead of one massive notebook:

9000 generations

are split into nine independent notebooks.

Benefits:

### Easier Debugging

If one pipeline fails:

Only one notebook is affected.

---

### Easier Recovery

Processing can resume from a single pipeline.

No need to rerun all pipelines.

---

### Better Experiment Tracking

Each evaluation result is isolated.

Example:

dense_gpt4o_eval.csv

contains only Dense GPT4o results.

---

### Fair Comparison

Every pipeline is evaluated using:

The same:

* Query
* Article
* Reference Summary

This guarantees fairness.

---

## Evaluation Files To Be Created

### GPT4o

6_3_Dense_GPT4o_Eval.ipynb

6_4_Hybrid_GPT4o_Eval.ipynb

6_5_Fusion_GPT4o_Eval.ipynb

---

### Llama3

6_6_Dense_Llama3_Eval.ipynb

6_7_Hybrid_Llama3_Eval.ipynb

6_8_Fusion_Llama3_Eval.ipynb

---

### Mistral

6_9_Dense_Mistral_Eval.ipynb

6_10_Hybrid_Mistral_Eval.ipynb

6_11_Fusion_Mistral_Eval.ipynb

---

## Files Generated

Each notebook will produce:

dense_gpt4o_eval.csv

hybrid_gpt4o_eval.csv

fusion_gpt4o_eval.csv

dense_llama3_eval.csv

hybrid_llama3_eval.csv

fusion_llama3_eval.csv

dense_mistral_eval.csv

hybrid_mistral_eval.csv

fusion_mistral_eval.csv

---

## Final Evaluation Stage

After generating all evaluation files:

ROUGE-L

BLEU

BERTScore

Precision

Recall

MRR

will be calculated and compared across all nine RAG pipelines.

This completes the end-to-end benchmarking framework for the project.


===================================================================================================================================================

"Due to local computational constraints associated with Llama3 and Mistral inference, all pipelines were evaluated on a common subset of 25 samples to ensure a fair and consistent comparison."