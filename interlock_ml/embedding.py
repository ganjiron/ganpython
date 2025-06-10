from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List
import numpy as np


class Embedder(ABC):
    """Strategy base class for text embedding."""

    @abstractmethod
    def embed(self, texts: List[str]) -> np.ndarray:
        """Return an array of embeddings for the given texts."""
        raise NotImplementedError


class TfidfEmbedder(Embedder):
    """Embed texts using TF-IDF."""

    def __init__(self, **vectorizer_kwargs):
        from sklearn.feature_extraction.text import TfidfVectorizer
        self.vectorizer = TfidfVectorizer(**vectorizer_kwargs)

    def embed(self, texts: List[str]) -> np.ndarray:
        return self.vectorizer.fit_transform(texts).toarray()


class BertEmbedder(Embedder):
    """Embed texts using a sentence-transformers BERT model."""

    def __init__(self, model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", batch_size: int = 32, device: str | None = None):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(model_name, device=device)
        self.batch_size = batch_size

    def embed(self, texts: List[str]) -> np.ndarray:
        embeddings = self.model.encode(texts, batch_size=self.batch_size, show_progress_bar=False)
        return np.asarray(embeddings)
