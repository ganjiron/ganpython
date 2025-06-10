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
    def __init__(
        self,
        n_components: int = 8,
        covariance_type: str = "full",
        random_state: int | None = None,
    ):
        from sklearn.mixture import GaussianMixture

        self.model = GaussianMixture(
            n_components=n_components,
            covariance_type=covariance_type,
            random_state=random_state,
        )

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.fit_predict(X)


class SpectralClusterer(Clusterer):
    """Cluster data using Spectral Clustering."""

    def __init__(self, n_clusters: int = 8, random_state: int | None = None):
        from sklearn.cluster import SpectralClustering

        self.model = SpectralClustering(
            n_clusters=n_clusters, random_state=random_state, assign_labels="kmeans"
        )

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.fit_predict(X)


class OPTICSClusterer(Clusterer):
    """Cluster data using OPTICS."""

    def __init__(
        self,
        min_samples: int = 5,
        xi: float = 0.05,
        min_cluster_size: int | None = None,
    ):
        from sklearn.cluster import OPTICS

        self.model = OPTICS(
            min_samples=min_samples, xi=xi, min_cluster_size=min_cluster_size
        )

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.fit_predict(X)


class AffinityPropagationClusterer(Clusterer):
    """Cluster data using Affinity Propagation."""

    def __init__(self, damping: float = 0.5, preference: float | None = None):
        from sklearn.cluster import AffinityPropagation

        self.model = AffinityPropagation(damping=damping, preference=preference)

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.fit_predict(X)


class HDBSCANClusterer(Clusterer):
    """Cluster data using HDBSCAN. Requires the ``hdbscan`` package."""

    def __init__(self, min_cluster_size: int = 5):
        from hdbscan import HDBSCAN

        self.model = HDBSCAN(min_cluster_size=min_cluster_size)

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.fit_predict(X)
