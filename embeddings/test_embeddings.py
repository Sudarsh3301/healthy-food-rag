import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from embeddings.embedding_model import EmbeddingModel
from embeddings.load_chunks import load_chunks


def test_embedding_generation():
    texts, metadata = load_chunks()

    print(f"Loaded {len(texts)} chunks")

    model = EmbeddingModel()
    embeddings = model.embed_texts(texts)

    print("Embeddings generated successfully")
    print(f"Embedding shape: {embeddings.shape}")

    print("\nSample text:")
    print(texts[0][:300])

    print("\nSample embedding vector (first 10 values):")
    print(embeddings[0][:10])


if __name__ == "__main__":
    test_embedding_generation()
