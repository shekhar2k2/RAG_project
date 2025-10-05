# indexer.py
import chromadb
from chromadb.utils import embedding_functions
from embeddings import EmbeddingModel
import uuid

class Indexer:
    def __init__(self, persist_directory="chroma_store"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.embedder = EmbeddingModel()
        self.collection = self.client.get_or_create_collection(
            name="rag_docs",
            embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        )

    def add_chunks(self, chunks):
        texts = [c["text"] for c in chunks]
        ids = [str(uuid.uuid4()) for _ in texts]
        metas = [c.get("meta", {}) for c in chunks]
        self.collection.add(documents=texts, ids=ids, metadatas=metas)

    def query(self, query, top_k=5):
        return self.collection.query(query_texts=[query], n_results=top_k)
