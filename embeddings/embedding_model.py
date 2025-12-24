from sentence_transformers import SentenceTransformer
from typing import List


class EmbeddingModel:
    """
    Handles text embedding using a local sentence-transformer model.
    """

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: List[str]):
        """
        Converts a list of texts into embeddings.
        """
        embeddings = self.model.encode(
            texts,
            show_progress_bar=True,
            convert_to_numpy=True
        )
        return embeddings

    def embed_query(self, query: str):
        """
        Converts a single query into an embedding.
        """
        return self.model.encode([query], convert_to_numpy=True)
