import re
from typing import List, Dict


def normalize_text(text: str) -> str:
    """
    Normalizes spacing and formatting artifacts.
    """
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def split_by_product(text: str) -> List[str]:
    """
    Splits text so that each chunk corresponds to exactly ONE product.

    Assumes each product starts with 'Product #:'.
    """
    raw_products = text.split("Product #:")
    product_chunks = []

    for product in raw_products:
        product = product.strip()
        if not product:
            continue

        # Reattach the delimiter to keep structure intact
        product_chunks.append("Product #:" + product)

    return product_chunks


def create_chunks_with_metadata(documents: List[Dict]) -> List[Dict]:
    """
    Creates product-level chunks with metadata from extracted PDF documents.
    Each chunk represents exactly one product.
    """
    all_chunks = []

    for doc in documents:
        normalized_text = normalize_text(doc["text"])

        # Split by product boundary
        product_chunks = split_by_product(normalized_text)

        for idx, chunk in enumerate(product_chunks):
            all_chunks.append({
                "content": chunk,
                "metadata": {
                    "page_number": doc["page_number"],
                    "product_index": idx
                }
            })

    return all_chunks
