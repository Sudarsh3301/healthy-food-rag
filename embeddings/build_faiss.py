import os
import sys
import pickle
import faiss
import numpy as np

# Add project root to path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from embeddings.embedding_model import EmbeddingModel
from embeddings.load_chunks import load_chunks

STORE_DIR = os.path.join("embeddings", "store")
FAISS_INDEX_PATH = os.path.join(STORE_DIR, "faiss.index")
METADATA_PATH = os.path.join(STORE_DIR, "metadata.pkl")


def build_faiss_index():
    os.makedirs(STORE_DIR, exist_ok=True)

    texts, metadata = load_chunks()

    model = EmbeddingModel()
    embeddings = model.embed_texts(texts)

    # Ensure numpy float32 for FAISS
    vectors = np.array(embeddings).astype("float32")
    dim = vectors.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

    # Persist index
    faiss.write_index(index, FAISS_INDEX_PATH)

    # Persist metadata aligned by vector order
    with open(METADATA_PATH, "wb") as f:
        pickle.dump(
            {
                "texts": texts,
                "metadata": metadata
            },
            f
        )

    print("FAISS index built and persisted.")
    print(f"Vectors stored: {index.ntotal}")
    print(f"Index path: {FAISS_INDEX_PATH}")
    print(f"Metadata path: {METADATA_PATH}")


if __name__ == "__main__":
    build_faiss_index()
