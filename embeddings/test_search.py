import os
import sys

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from embeddings.search import VectorSearch


def run_tests():
    searcher = VectorSearch()

    queries = [
        "What are the nutritional benefits of this product?",
        "Is this food suitable for daily consumption?",
        "What ingredients does this product contain?"
    ]

    for q in queries:
        print("\nQUERY:", q)
        results = searcher.search(q, k=3)
        for i, r in enumerate(results, 1):
            print(f"\nResult {i}:")
            print(r["content"][:300])


if __name__ == "__main__":
    run_tests()
