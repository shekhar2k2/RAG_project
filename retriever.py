#lib
from rank_bm25 import BM25Okapi
from indexer import Indexer
from embeddings import EmbeddingModel
# retriever
class HybridRetriever:
    def __init__(self):
        self.indexer = Indexer()
        self.embedder = EmbeddingModel()
        self.docs = []  # for BM25
        self.bm25 = None
    #indexing of token/chunks func
    def index_chunks(self, chunks):
        """Index new chunks into both Chroma & BM25."""
        self.indexer.add_chunks(chunks)
        texts = [c["text"] for c in chunks]
        self.docs.extend(texts)
        tokenized = [t.split() for t in self.docs]
        self.bm25 = BM25Okapi(tokenized)
    #retriever func
    def retrieve(self, query, top_k=5, alpha=0.6):
        """Hybrid retrieval: combine BM25 & vector similarity."""
        # Vector
        vector_results = self.indexer.query(query, top_k=top_k)["documents"][0]

        # BM25
        bm25_scores = self.bm25.get_scores(query.split()) if self.bm25 else []
        ranked_bm25 = sorted(
            zip(self.docs, bm25_scores), key=lambda x: x[1], reverse=True
        )[:top_k]
        bm25_results = [doc for doc, _ in ranked_bm25]

        # Merge
        merged = vector_results[: int(alpha * top_k)] + bm25_results[: int((1 - alpha) * top_k)]
        seen, final = set(), []
        for doc in merged:
            if doc not in seen:
                final.append({"text": doc})
                seen.add(doc)
        return final[:top_k]
