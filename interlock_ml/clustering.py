from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Type
import math
import random


class Clusterer(ABC):
    """Strategy base class for clustering algorithms."""

    @abstractmethod
    def fit_predict(self, X: List[List[float]]) -> List[int]:
        raise NotImplementedError


class KMeansClusterer(Clusterer):
    def __init__(self, n_clusters: int = 8, random_state: int | None = None, max_iter: int = 10):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.max_iter = max_iter

    @staticmethod
    def _dist(a: List[float], b: List[float]) -> float:
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

    def fit_predict(self, X: List[List[float]]) -> List[int]:
        random.seed(self.random_state)
        centers = random.sample(X, self.n_clusters)
        labels = [0] * len(X)
        for _ in range(self.max_iter):
            for i, x in enumerate(X):
                distances = [self._dist(x, c) for c in centers]
                labels[i] = distances.index(min(distances))
            new_centers = [[0.0 for _ in X[0]] for _ in range(self.n_clusters)]
            counts = [0] * self.n_clusters
            for lbl, x in zip(labels, X):
                counts[lbl] += 1
                for j, val in enumerate(x):
                    new_centers[lbl][j] += val
            for idx in range(self.n_clusters):
                if counts[idx]:
                    centers[idx] = [v / counts[idx] for v in new_centers[idx]]
        return labels


class AgglomerativeClusterer(Clusterer):
    def __init__(self, n_clusters: int = 8, linkage: str = "ward"):
        from sklearn.cluster import AgglomerativeClustering
        self.model = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)

    def fit_predict(self, X: List[List[float]]) -> List[int]:
        return self.model.fit_predict(X)


class DBSCANClusterer(Clusterer):
    def __init__(self, eps: float = 0.5, min_samples: int = 5):
        from sklearn.cluster import DBSCAN
        self.model = DBSCAN(eps=eps, min_samples=min_samples)

    def fit_predict(self, X: List[List[float]]) -> List[int]:
        return self.model.fit_predict(X)


class GaussianMixtureClusterer(Clusterer):
    def __init__(self, n_components: int = 8, covariance_type: str = "full", random_state: int | None = None):
        from sklearn.mixture import GaussianMixture
        self.model = GaussianMixture(n_components=n_components, covariance_type=covariance_type, random_state=random_state)

    def fit_predict(self, X: List[List[float]]) -> List[int]:
        return self.model.fit_predict(X)


# Registry of available clusterer classes for convenience in tests and applications
CLUSTERER_FACTORY: Dict[str, Type[Clusterer]] = {
    "kmeans": KMeansClusterer,
    "agglomerative": AgglomerativeClusterer,
    "dbscan": DBSCANClusterer,
    "gmm": GaussianMixtureClusterer,
}


def get_clusterer(name: str) -> Type[Clusterer]:
    """Retrieve a clusterer class from the factory by name."""
    return CLUSTERER_FACTORY[name]
