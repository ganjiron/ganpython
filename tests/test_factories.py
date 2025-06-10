import pytest

from interlock_ml.embedding import EMBEDDER_FACTORY, TfidfEmbedder
from interlock_ml.clustering import CLUSTERER_FACTORY, KMeansClusterer


def test_default_embedder_registered():
    assert "tfidf" in EMBEDDER_FACTORY
    assert EMBEDDER_FACTORY["tfidf"] is TfidfEmbedder


def test_default_clusterer_registered():
    assert "kmeans" in CLUSTERER_FACTORY
    assert CLUSTERER_FACTORY["kmeans"] is KMeansClusterer
