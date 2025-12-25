import os
import sys
import pickle
import faiss
import numpy as np

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from embeddings.embedding_model import EmbeddingModel

STORE_DIR = os.path.join("embeddings", "store")
FAISS_INDEX_PATH = os.path.join(STORE_DIR, "faiss.index")
METADATA_PATH = os.path.join(STORE_DIR, "metadata.pkl")


class VectorSearch:
    def __init__(self):
        self.index = faiss.read_index(FAISS_INDEX_PATH)
        with open(METADATA_PATH, "rb") as f:
            data = pickle.load(f)
            self.texts = data["texts"]
            self.metadata = data["metadata"]

        self.model = EmbeddingModel()

    def search(self, query: str, k: int = 5):
        query_vec = self.model.embed_query(query).astype("float32")
        distances, indices = self.index.search(query_vec, k)

        results = []
        for idx in indices[0]:
            results.append({
                "content": self.texts[idx],
                "metadata": self.metadata[idx]
            })
        return results
