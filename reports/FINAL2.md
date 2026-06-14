Although Dense GPT4o was the most efficient retrieval pipeline, Fusion GPT4o produced the highest quality answers. Since the primary objective of a Retrieval-Augmented Generation system is to generate accurate and relevant responses, Fusion GPT4o is selected as the best overall pipeline.


Best Retrieval Efficiency  → Dense GPT4o
Best Generation Quality   → Fusion GPT4o
Overall Best Pipeline     → Fusion GPT4o


======================================================================================================================================================================

## Final Experimental Findings

The experimental results demonstrate that retrieval strategy significantly influences the overall performance of Retrieval-Augmented Generation systems.

Dense retrieval approaches achieved the highest context relevance scores and consumed fewer computational resources. However, Fusion retrieval approaches provided substantially larger contextual coverage by combining dense retrieval, sparse retrieval, and web search results.

Among all evaluated pipelines, Fusion GPT4o achieved the best generation performance with a ROUGE-L score of 0.2977, BLEU score of 0.0476, and BERTScore of 0.8588. Although its context relevance score was slightly lower than Dense GPT4o, the additional contextual information enabled GPT4o to generate more accurate and semantically meaningful responses.

Hybrid GPT4o achieved the lowest latency, making it the fastest pipeline, while Dense GPT4o demonstrated the highest retrieval efficiency and lowest memory consumption.

Overall, the results indicate that Fusion Retrieval combined with GPT4o provides the best balance between retrieval coverage and answer quality, making Fusion GPT4o the optimal architecture for this project.

Best Quality: Fusion GPT4o 🥇
Fastest: Hybrid GPT4o ⚡
Most Efficient: Dense GPT4o 💾
Largest Context: Fusion Mistral 📚
Longest Responses: Fusion Llama3 📝

======================================================================================================================================================================

memory_used = memory_after - memory_before
The operating system / Python garbage collector
memory_before = 500 MB
memory_after  = 495 MB

memory_used = -5 MB
released memory during execution.

======================================================================================================================================================================

# Retrieval Efficiency and Runtime Performance Analysis

## Overview

In addition to evaluating generation quality using ROUGE-L, BLEU, and BERTScore, retrieval performance was analyzed using operational metrics collected during experimentation. These metrics provide insights into system efficiency, computational cost, retrieval coverage, and response generation behavior.

The following metrics were analyzed:

* Latency (seconds)
* Memory Usage (MB)
* Context Length
* Response Length
* Context Relevance

The comparison was performed across nine RAG pipelines:

1. Dense GPT4o
2. Hybrid GPT4o
3. Fusion GPT4o
4. Dense Llama3
5. Hybrid Llama3
6. Fusion Llama3
7. Dense Mistral
8. Hybrid Mistral
9. Fusion Mistral

---

# Metric Definitions

## Latency

Latency represents the total time required to retrieve relevant information and generate a response.

Lower latency indicates faster response generation and better user experience.

Desired Value: Lower

---

## Memory Usage

Memory Usage measures the amount of system memory consumed during retrieval and generation.

Lower memory consumption indicates better computational efficiency.

Desired Value: Lower

---

## Context Length

Context Length represents the total amount of retrieved information supplied to the language model.

Larger context lengths generally indicate broader retrieval coverage.

Desired Value: Higher

---

## Response Length

Response Length measures the size of generated responses.

Longer responses may provide more detailed explanations but can also introduce redundancy.

Desired Value: Depends on application requirements.

---

## Context Relevance

Context Relevance measures how closely the retrieved context matches the user query.

Higher values indicate more focused and relevant retrieval.

Desired Value: Higher

---

# Experimental Results

| Pipeline       | Latency (s) | Memory (MB) | Context Length | Response Length | Context Relevance |
| -------------- | ----------- | ----------- | -------------- | --------------- | ----------------- |
| Dense GPT4o    | 2.37        | 0.03        | 2143.35        | 673.95          | 0.5622            |
| Dense Llama3   | 27.12       | 46.06       | 2143.35        | 701.80          | 0.5622            |
| Dense Mistral  | 34.92       | 6.81        | 2143.20        | 668.15          | 0.5615            |
| Fusion GPT4o   | 3.09        | 75.11       | 4541.65        | 734.80          | 0.5417            |
| Fusion Llama3  | 43.53       | -8.75       | 4615.55        | 947.45          | 0.5390            |
| Fusion Mistral | 55.97       | -5.07       | 4714.35        | 791.05          | 0.5464            |
| Hybrid GPT4o   | 2.08        | 8.35        | 2226.05        | 550.85          | 0.5587            |
| Hybrid Llama3  | 26.12       | 24.37       | 2226.05        | 823.65          | 0.5587            |
| Hybrid Mistral | 37.48       | -1.61       | 2226.20        | 679.65          | 0.5589            |

---

# Analysis of Results

## Fastest Pipeline

Hybrid GPT4o achieved the lowest latency of 2.08 seconds, making it the fastest pipeline among all evaluated approaches.

The combination of dense retrieval and sparse retrieval allowed the system to retrieve relevant information efficiently while avoiding the additional overhead introduced by web search retrieval.

This makes Hybrid GPT4o suitable for real-time applications where response speed is critical.

---

## Most Memory-Efficient Pipeline

Dense GPT4o consumed only 0.03 MB of additional memory, making it the most computationally efficient pipeline.

The dense retrieval approach relies solely on vector similarity search and therefore requires fewer retrieval operations and smaller context windows.

This result demonstrates that Dense GPT4o provides strong retrieval efficiency while minimizing resource consumption.

---

## Largest Retrieval Coverage

Fusion Mistral achieved the highest context length of 4714.35 characters.

The Fusion retrieval strategy combines:

* Dense Retrieval
* Sparse Retrieval
* Web Search Retrieval

As a result, the model receives significantly more contextual information than Dense and Hybrid retrieval approaches.

Although this increases computational cost, it improves information coverage.

---

## Longest Generated Responses

Fusion Llama3 produced the longest responses with an average response length of 947.45 characters.

This indicates that Llama3 tends to generate more verbose responses when supplied with large amounts of contextual information.

However, longer responses do not necessarily imply higher answer quality.

---

## Highest Context Relevance

Dense GPT4o achieved the highest context relevance score of 0.5622.

This indicates that dense retrieval provides highly focused and semantically relevant information for answering user queries.

Interestingly, Fusion retrieval methods produced larger contexts but slightly lower relevance scores, suggesting that increased retrieval coverage may introduce some irrelevant information.

---

# Relationship Between Retrieval and Generation Quality

The retrieval analysis reveals an important observation.

Dense GPT4o achieved the highest context relevance score, indicating highly focused retrieval. However, Fusion GPT4o achieved the best generation quality scores in ROUGE-L, BLEU, and BERTScore evaluations.

This demonstrates that generation quality is influenced not only by retrieval precision but also by retrieval coverage.

Although Fusion retrieval introduces slightly more noise, the additional contextual information enables GPT4o to generate more complete and semantically accurate responses.

---

# Overall Findings

The experimental results reveal three important conclusions:

1. Dense retrieval provides the most focused and resource-efficient retrieval mechanism.
2. Hybrid retrieval provides the fastest response generation performance.
3. Fusion retrieval provides the richest contextual information and leads to the highest answer quality when combined with GPT4o.

---

# Final Conclusion

Based on retrieval efficiency metrics, Dense GPT4o was identified as the most efficient retrieval pipeline due to its low latency, minimal memory usage, and highest context relevance.

Based on generation quality metrics, Fusion GPT4o achieved the highest ROUGE-L, BLEU, and BERTScore values, making it the best overall RAG pipeline.

Therefore, Fusion GPT4o is selected as the final recommended architecture for this project because it provides the best balance between retrieval coverage and answer generation quality.
