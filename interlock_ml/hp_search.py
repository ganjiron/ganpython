from __future__ import annotations

import itertools
import math
from typing import Any, Dict, Iterable, List, Tuple, Type

from .clustering import Clusterer
from .embedding import Embedder


def _parameter_grid(param_grid: Dict[str, Iterable]) -> Iterable[Dict[str, Any]]:
    keys = list(param_grid)
    if not keys:
        yield {}
    else:
        for values in itertools.product(*(param_grid[k] for k in keys)):
            yield dict(zip(keys, values))


def _silhouette_score(X: List[List[float]], labels: List[int]) -> float:
    n = len(X)
    if n == 0 or len(set(labels)) < 2:
        return -1.0
    def dist(a: List[float], b: List[float]) -> float:
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
    scores = []
    for i, x in enumerate(X):
        same = [j for j, l in enumerate(labels) if l == labels[i] and j != i]
        other_clusters = {
            l: [j for j, ll in enumerate(labels) if ll == l]
            for l in set(labels)
            if l != labels[i]
        }
        a = sum(dist(x, X[j]) for j in same) / len(same) if same else 0.0
        b = min(
            sum(dist(x, X[j]) for j in idxs) / len(idxs)
            for idxs in other_clusters.values()
        )
        scores.append((b - a) / max(a, b) if max(a, b) else 0.0)
    return sum(scores) / len(scores)


def search_best_clusterer(
    clusterer_cls: Type[Clusterer],
    param_grid: Dict[str, Iterable],
    X: List[List[float]],
) -> Tuple[Dict[str, Iterable], float]:
    """Simple hyperparameter search using silhouette score."""
    best_score = -1.0
    best_params: Dict[str, Iterable] | None = None
    for params in _parameter_grid(param_grid):
        clusterer = clusterer_cls(**params)
        labels = clusterer.fit_predict(X)
        score = _silhouette_score(X, labels)
        if score > best_score:
            best_score = score
            best_params = params
    return best_params or {}, best_score


def search_best_pipeline(
    embedder_cls: Type[Embedder],
    clusterer_cls: Type[Clusterer],
    clusterer_param_grid: Dict[str, Iterable],
    texts: List[str],
    *,
    embedder_kwargs: Dict[str, Any] | None = None,
) -> Tuple[Dict[str, Iterable], float]:
    """Search best clustering hyperparameters for an embedding+clustering pipeline."""
    embedder = embedder_cls(**(embedder_kwargs or {}))
    X = embedder.embed(texts)
    return search_best_clusterer(clusterer_cls, clusterer_param_grid, X)
