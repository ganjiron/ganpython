from __future__ import annotations

from abc import ABC, abstractmethod
import numpy as np


class Clusterer(ABC):
    """Strategy base class for clustering algorithms."""

    @abstractmethod
    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class KMeansClusterer(Clusterer):
    def __init__(self, n_clusters: int = 8, random_state: int | None = None):
        from sklearn.cluster import KMeans
        self.model = KMeans(n_clusters=n_clusters, random_state=random_state)

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.fit_predict(X)


class AgglomerativeClusterer(Clusterer):
    def __init__(self, n_clusters: int = 8, linkage: str = "ward"):
        from sklearn.cluster import AgglomerativeClustering
        self.model = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.fit_predict(X)


class DBSCANClusterer(Clusterer):
    def __init__(self, eps: float = 0.5, min_samples: int = 5):
        from sklearn.cluster import DBSCAN
        self.model = DBSCAN(eps=eps, min_samples=min_samples)

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.fit_predict(X)


class GaussianMixtureClusterer(Clusterer):
    def __init__(self, n_components: int = 8, covariance_type: str = "full", random_state: int | None = None):
        from sklearn.mixture import GaussianMixture
        self.model = GaussianMixture(n_components=n_components, covariance_type=covariance_type, random_state=random_state)

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.fit_predict(X)
