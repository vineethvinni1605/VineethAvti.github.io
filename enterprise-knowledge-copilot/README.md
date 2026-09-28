# Enterprise Knowledge Copilot

A Retrieval-Augmented Generation (RAG) system that answers employee questions using a grounded enterprise knowledge base.

## Project Overview

Enterprise Knowledge Copilot combines semantic search with a Large Language Model to generate answers grounded in internal company documents.

Instead of relying only on the LLM's general knowledge, the system retrieves relevant document chunks and provides them as context before generating an answer.

## RAG Pipeline

Documents  
→ Text Chunking  
→ Embeddings  
→ Semantic Search  
→ Context Retrieval  
→ LLM  
→ Grounded Answer

## Knowledge Base

The synthetic enterprise knowledge base contains policies covering:

- Remote work
- Paid time off
- Information security
- Expense reimbursement
- AI usage
- Technical support

## Document Processing

Documents are divided into overlapping text chunks to support retrieval.

Configuration:

- Chunk size: 500 characters
- Chunk overlap: 100 characters

## Embeddings & Retrieval

The project uses the `all-MiniLM-L6-v2` Sentence Transformer model to generate vector embeddings.

Cosine similarity is used to compare the user's question with document chunks and retrieve the three most relevant pieces of context.

## Grounded Generation

Retrieved context is passed to an OpenAI language model.

The model is instructed to answer only from the supplied company knowledge and return a fallback response when the information is unavailable.

## Evaluation

### Grounded Question

Question:

`How many PTO days can carry over?`

Result:

The system correctly retrieved the PTO policy and answered that unused PTO may carry over up to a maximum of five days.

### Unsupported Question

Question:

`What is the company's dental insurance policy?`

Result:

The system responded:

`I could not find that information in the company knowledge base.`

This demonstrated basic hallucination control for information absent from the retrieved knowledge.

## Technologies

- Python
- OpenAI API
- Sentence Transformers
- Scikit-learn
- Semantic Search
- Embeddings
- Cosine Similarity
- Retrieval-Augmented Generation (RAG)

## Key Takeaway

This project demonstrates an end-to-end RAG workflow that retrieves relevant enterprise knowledge before generating responses, helping produce answers grounded in an approved source rather than relying solely on an LLM's internal knowledge.