import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from ingestion.pdf_loader import load_pdf, extract_text_from_pages
from ingestion.chunker import create_chunks_with_metadata


PDF_PATH = "data/healthy_food_products.pdf"


def run_ingestion():
    """
    Runs the full PDF ingestion pipeline.
    """
    pages = load_pdf(PDF_PATH)
    documents = extract_text_from_pages(pages)
    chunks = create_chunks_with_metadata(documents)
    return chunks


if __name__ == "__main__":
    chunks = run_ingestion()

    print(f"PDF ingestion completed successfully.")
    print(f"Total chunks created: {len(chunks)}")

    # Preview first 2 chunks for validation
    for i in range(min(2, len(chunks))):
        print("\n--- Chunk Preview ---")
        print(f"Page: {chunks[i]['metadata']['page_number']}")
        print(f"Product Index: {chunks[i]['metadata']['product_index']}")
        print(chunks[i]['content'][:500])
