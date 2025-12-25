# Healthy Food Product Advisor (RAG System)

A production-ready Retrieval-Augmented Generation (RAG) system that answers user queries about healthy food products using a structured PDF as the knowledge source. The system provides factual, document-grounded responses while presenting nutritional benefits in a value-driven, ethical, and customer-friendly manner.

---

## Key Features

- Product-aware PDF ingestion
- Semantic search using FAISS vector database
- Deterministic RAG pipeline (non-agentic)
- Local LLM inference using Ollama (LLaMA 3.1 8B)
- Ethical purchase-influence response framing
- ChatGPT-style interactive UI built with Gradio

---

## System Architecture

1. **PDF Ingestion**
   - Product-level chunking
   - Metadata-preserved extraction

2. **Embeddings & Vector Store**
   - Sentence-Transformers embeddings
   - FAISS for fast similarity search

3. **Retrieval-Augmented Generation**
   - Context retrieved deterministically
   - Strict grounding to source document
   - No hallucination or external knowledge

4. **LLM Layer**
   - Ollama (local)
   - LLaMA 3.1 8B
   - Conservative generation parameters

5. **Frontend UI**
   - ChatGPT-style interface
   - Clean, minimal, fast interaction
   - End-to-end flow from query to response

---

## Tech Stack

- Python 3.10+
- Ollama (LLaMA 3.1 8B)
- FAISS
- Sentence-Transformers
- Gradio
- PDF processing libraries

