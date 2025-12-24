import os
import sys
import ollama

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from embeddings.search import VectorSearch
from retrieval.prompt import RAG_PROMPT_TEMPLATE


class RAGPipeline:
    """
    Deterministic, non-agentic RAG pipeline using Ollama (LLaMA 3.1).
    """

    def __init__(self, top_k: int = 7):
        self.searcher = VectorSearch()
        self.top_k = top_k
        self.model_name = "llama3.1:8b"

    def build_context(self, retrieved_chunks):
        """
        Concatenate retrieved chunks into a single context block.
        """
        return "\n\n".join(chunk["content"] for chunk in retrieved_chunks)

    def generate_answer(self, question: str) -> str:
        """
        Query → FAISS Retrieval → Prompt Injection → Ollama Generation
        """
        # Step 1: Retrieve grounded chunks
        retrieved_chunks = self.searcher.search(question, k=self.top_k)

        question_lower = question.lower()
        product_hits = [
            chunk for chunk in retrieved_chunks
            if question_lower in chunk["content"].lower()
              ]

        # If product-specific chunks exist, prioritize them
        if product_hits:
            retrieved_chunks = product_hits
 
        # Step 2: Build context
        context = self.build_context(retrieved_chunks)

        # Step 3: Fixed prompt (grounded)
        prompt = RAG_PROMPT_TEMPLATE.format(
            context=context,
            question=question
        )

        # Step 4: Single Ollama call (non-agentic)
        response = ollama.generate(
            model=self.model_name,
            prompt=prompt,
            options={
                "temperature": 0.2,
                "num_predict": 512
            }
        )

        return response["response"].strip()
