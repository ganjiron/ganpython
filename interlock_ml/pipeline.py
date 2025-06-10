from __future__ import annotations

from typing import Any, Dict, List, Type
import numpy as np

from .embedding import Embedder
from .clustering import Clusterer


class EmbeddingClusteringPipeline:
    """Combine embedding and clustering strategies into a single pipeline."""

    def __init__(
        self,
        embedder_cls: Type[Embedder],
        clusterer_cls: Type[Clusterer],
        *,
        embedder_kwargs: Dict[str, Any] | None = None,
        clusterer_kwargs: Dict[str, Any] | None = None,
    ):
        self.embedder = embedder_cls(**(embedder_kwargs or {}))
        self.clusterer = clusterer_cls(**(clusterer_kwargs or {}))

    def run(self, texts: List[str]) -> np.ndarray:
        X = self.embedder.embed(texts)
        labels = self.clusterer.fit_predict(X)
        return labels
