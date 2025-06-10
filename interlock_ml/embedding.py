from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Type
import math


class Embedder(ABC):
    """Strategy base class for text embedding."""

    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        """Return an array of embeddings for the given texts."""
        raise NotImplementedError


class TfidfEmbedder(Embedder):
    """Embed texts using a very small TF-IDF implementation."""

    def __init__(self, **_: object):
        self.vocab: List[str] = []
        self.idf: Dict[str, float] = {}

    def embed(self, texts: List[str]) -> List[List[float]]:
        tokenized = [t.lower().split() for t in texts]
        self.vocab = sorted({tok for toks in tokenized for tok in toks})
        n_docs = len(texts)
        for token in self.vocab:
            df = sum(token in toks for toks in tokenized)
            self.idf[token] = 1.0 + math.log(n_docs / (df or 1))
        vectors = []
        for toks in tokenized:
            tf: Dict[str, int] = {}
            for tok in toks:
                tf[tok] = tf.get(tok, 0) + 1
            vectors.append([tf.get(token, 0) * self.idf[token] for token in self.vocab])
        return vectors


class BertEmbedder(Embedder):
    """Embed texts using a sentence-transformers BERT model."""

    def __init__(self, model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", batch_size: int = 32, device: str | None = None):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model_name, device=device)
        self.batch_size = batch_size

    def embed(self, texts: List[str]) -> List[List[float]]:
        import numpy as np  # Heavy dependency optional
        embeddings = self.model.encode(texts, batch_size=self.batch_size, show_progress_bar=False)
        return np.asarray(embeddings).tolist()


# Registry of available embedder classes for convenience in tests and applications
EMBEDDER_FACTORY: Dict[str, Type[Embedder]] = {
    "tfidf": TfidfEmbedder,
    "bert": BertEmbedder,
}


def get_embedder(name: str) -> Type[Embedder]:
    """Retrieve an embedder class from the factory by name."""
    return EMBEDDER_FACTORY[name]
