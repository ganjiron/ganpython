from __future__ import annotations

from sklearn.metrics import silhouette_score
from sklearn.model_selection import ParameterGrid
from typing import Dict, Iterable, Tuple, Type
import numpy as np

from .clustering import Clusterer


def search_best_clusterer(clusterer_cls: Type[Clusterer], param_grid: Dict[str, Iterable], X: np.ndarray) -> Tuple[Dict[str, Iterable], float]:
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
