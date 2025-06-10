from __future__ import annotations

from sklearn.metrics import silhouette_score
from sklearn.model_selection import ParameterGrid
from typing import Dict, Iterable, Tuple, Type
import numpy as np

from .clustering import Clusterer
from .embedding import Embedder


def search_best_clusterer(
    clusterer_cls: Type[Clusterer], param_grid: Dict[str, Iterable], X: np.ndarray
) -> Tuple[Dict[str, Iterable], float]:
    """Simple hyperparameter search using silhouette score."""
    best_score = -1.0
    best_params: Dict[str, Iterable] | None = None
    for params in ParameterGrid(param_grid):
        clusterer = clusterer_cls(**params)
        labels = clusterer.fit_predict(X)
        if len(set(labels)) <= 1:
            score = -1.0
        else:
            score = silhouette_score(X, labels)
        if score > best_score:
            best_score = score
            best_params = params
    return best_params or {}, best_score


def search_best_pipeline(
    embedder_cls: Type[Embedder],
    clusterer_cls: Type[Clusterer],
    embedder_grid: Dict[str, Iterable],
    clusterer_grid: Dict[str, Iterable],
    texts: Iterable[str],
) -> Tuple[Dict[str, Iterable], Dict[str, Iterable], float]:
    """Search for the best combination of embedder and clusterer params."""

    best_score = -1.0
    best_embedder_params: Dict[str, Iterable] | None = None
    best_clusterer_params: Dict[str, Iterable] | None = None

    for e_params in ParameterGrid(embedder_grid):
        embedder = embedder_cls(**e_params)
        X = embedder.embed(list(texts))
        for c_params in ParameterGrid(clusterer_grid):
            clusterer = clusterer_cls(**c_params)
            labels = clusterer.fit_predict(X)
            if len(set(labels)) <= 1:
                score = -1.0
            else:
                score = silhouette_score(X, labels)
            if score > best_score:
                best_score = score
                best_embedder_params = e_params
                best_clusterer_params = c_params

    return (best_embedder_params or {}, best_clusterer_params or {}, best_score)
