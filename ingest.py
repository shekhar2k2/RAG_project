# ingest.py
import fitz  # PyMuPDF
from typing import List, Dict

def extract_text_from_pdf_bytes(file_bytes: bytes) -> str:
    """Extract raw text from uploaded PDF bytes."""
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

def sentence_chunk(text: str, chunk_size: int = 800, chunk_overlap: int = 200) -> List[Dict]:
    """Split long text into overlapping chunks for RAG."""
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk_text = " ".join(words[start:end])
        chunks.append({"text": chunk_text})
        start += chunk_size - chunk_overlap
    return chunks
