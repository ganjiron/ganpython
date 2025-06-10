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

    def __init__(
        self,
        model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        batch_size: int = 32,
        device: str | None = None,
    ):
        from sentence_transformers import SentenceTransformer

        self.model = SentenceTransformer(model_name, device=device)
        self.batch_size = batch_size

    def embed(self, texts: List[str]) -> np.ndarray:
        embeddings = self.model.encode(
            texts, batch_size=self.batch_size, show_progress_bar=False
        )
        return np.asarray(embeddings)


class TransformerEmbedder(Embedder):
    """Embed texts using a HuggingFace transformer model."""

    def __init__(
        self, model_name: str, batch_size: int = 32, device: str | None = None
    ):
        from transformers import AutoModel, AutoTokenizer
        import torch

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.batch_size = batch_size

        if device:
            self.model.to(device)
            self.device = device
        else:
            self.device = next(self.model.parameters()).device

        self.model.eval()

    def embed(self, texts: List[str]) -> np.ndarray:
        import torch

        embeddings = []
        with torch.no_grad():
            for i in range(0, len(texts), self.batch_size):
                batch = texts[i : i + self.batch_size]
                encoded = self.tokenizer(
                    batch, padding=True, truncation=True, return_tensors="pt"
                ).to(self.device)
                output = self.model(**encoded)
                cls_emb = output.last_hidden_state[:, 0, :]
                embeddings.append(cls_emb.cpu().numpy())
        return np.vstack(embeddings)


class FastTextEmbedder(Embedder):
    """Embed texts using a FastText model."""

    def __init__(self, model_path: str, batch_size: int = 32):
        from gensim.models import FastText

        self.model = FastText.load(model_path)
        self.batch_size = batch_size

    def _embed_sentence(self, sentence: str) -> np.ndarray:
        words = [self.model.wv[w] for w in sentence.split() if w in self.model.wv]
        if words:
            return np.mean(words, axis=0)
        return np.zeros(self.model.vector_size)

    def embed(self, texts: List[str]) -> np.ndarray:
        embeddings = [self._embed_sentence(text) for text in texts]
        return np.vstack(embeddings)
