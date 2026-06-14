# Limitation in Calculating Precision, Recall, and Mean Reciprocal Rank (MRR)

## Background

The objective of retrieval evaluation is to measure how effectively the retrieval component of a Retrieval-Augmented Generation (RAG) system identifies and ranks relevant documents for a given query. Common retrieval evaluation metrics include Precision, Recall, and Mean Reciprocal Rank (MRR).

During the implementation phase, retrieval results were successfully generated and stored for all evaluated pipelines, including Dense Retrieval, Hybrid Retrieval, and Fusion Retrieval approaches. The stored retrieval outputs contained information such as:

* Query
* Retrieved Documents
* Retrieved Document Count
* Context
* Context Length
* Generated Answer
* Response Length
* Latency
* Memory Usage

However, the retrieval outputs did not contain relevance annotations or ground-truth labels indicating whether each retrieved document was actually relevant to the corresponding query.

---

## Why Precision Could Not Be Calculated

Precision is defined as:

Precision = Relevant Retrieved Documents / Total Retrieved Documents

To compute Precision, it is necessary to know which retrieved documents are relevant and which are not relevant.

Although retrieved documents were available, the dataset did not contain relevance labels for those documents. Therefore, the number of relevant retrieved documents could not be objectively determined.

As a result, Precision could not be calculated reliably.

---

## Why Recall Could Not Be Calculated

Recall is defined as:

Recall = Relevant Retrieved Documents / Total Relevant Documents

Calculating Recall requires knowledge of:

1. The total number of relevant documents available in the corpus.
2. The number of relevant documents successfully retrieved.

The experimental dataset did not provide a complete set of relevant documents for each query. Consequently, the denominator required for Recall calculation was unavailable.

Therefore, Recall could not be computed accurately.

---

## Why Mean Reciprocal Rank (MRR) Could Not Be Calculated

Mean Reciprocal Rank evaluates the ranking quality of retrieved documents and is calculated using the rank position of the first relevant document.

MRR = 1 / Rank of First Relevant Document

To determine the rank of the first relevant document, relevance judgments must be available for every retrieved document.

Since no relevance annotations were available, the first relevant document could not be identified. As a result, MRR could not be calculated objectively.

---

## Why Manual Labeling Was Not Used

An alternative approach would have been to manually inspect retrieved documents and assign relevance labels.

However, this approach introduces several limitations:

* Subjective human judgment
* Potential evaluator bias
* Lack of reproducibility
* Inconsistency across pipelines

Since the project aimed to maintain objective and reproducible evaluation procedures, manual relevance labeling was not incorporated into the final retrieval evaluation.

---

## Alternative Evaluation Strategy

Due to the absence of relevance labels, retrieval performance was analyzed using operational and system-level metrics that were directly available from the retrieval outputs:

* Retrieved Document Count
* Context Length
* Response Length
* Latency
* Memory Consumption

These metrics provide valuable insights into retrieval efficiency, resource utilization, and overall system performance.

In addition, generation quality was evaluated using established natural language generation metrics:

* ROUGE-L
* BLEU
* BERTScore

These metrics were sufficient to compare the effectiveness of the evaluated RAG pipelines and identify the best-performing retrieval and generation strategy.

---

## Conclusion

Precision, Recall, and Mean Reciprocal Rank (MRR) require explicit relevance judgments between queries and retrieved documents. Since the retrieval datasets generated during experimentation did not contain relevance annotations or ground-truth relevance labels, these metrics could not be computed in a reliable and reproducible manner.

Therefore, the evaluation focused on generation quality metrics and retrieval efficiency metrics, which were fully supported by the collected experimental data and provided a robust basis for comparing the performance of different RAG pipelines.
