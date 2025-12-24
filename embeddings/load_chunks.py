import os
import sys

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from ingestion.run_ingestion import run_ingestion


def load_chunks():
    """
    Loads chunked text data produced by Phase 3 ingestion.
    """
    chunks = run_ingestion()

    texts = [chunk["content"] for chunk in chunks]
    metadata = [chunk["metadata"] for chunk in chunks]

    return texts, metadata
