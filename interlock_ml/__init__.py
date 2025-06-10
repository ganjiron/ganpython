from .embedding import (
    Embedder,
    TfidfEmbedder,
    BertEmbedder,
    TransformerEmbedder,
    FastTextEmbedder,
)
from .clustering import (
    Clusterer,
    KMeansClusterer,
    AgglomerativeClusterer,
    DBSCANClusterer,
    GaussianMixtureClusterer,
    SpectralClusterer,
    OPTICSClusterer,
    AffinityPropagationClusterer,
    HDBSCANClusterer,
)
from .hp_search import search_best_clusterer
from .pipeline import EmbeddingClusteringPipeline
from .factory import EmbedderFactory, ClustererFactory

# Register default embedders
for name, cls in [
    ("tfidf", TfidfEmbedder),
    ("bert", BertEmbedder),
    ("transformer", TransformerEmbedder),
    ("fasttext", FastTextEmbedder),
]:
    EmbedderFactory.register(name, cls)

# Register default clusterers
for name, cls in [
    ("kmeans", KMeansClusterer),
    ("agglomerative", AgglomerativeClusterer),
    ("dbscan", DBSCANClusterer),
    ("gmm", GaussianMixtureClusterer),
    ("spectral", SpectralClusterer),
    ("optics", OPTICSClusterer),
    ("affinity", AffinityPropagationClusterer),
    ("hdbscan", HDBSCANClusterer),
]:
    ClustererFactory.register(name, cls)

__all__ = [
    "Embedder",
    "TfidfEmbedder",
    "BertEmbedder",
    "TransformerEmbedder",
    "FastTextEmbedder",
    "Clusterer",
    "KMeansClusterer",
    "AgglomerativeClusterer",
    "DBSCANClusterer",
    "GaussianMixtureClusterer",
    "SpectralClusterer",
    "OPTICSClusterer",
    "AffinityPropagationClusterer",
    "HDBSCANClusterer",
    "EmbedderFactory",
    "ClustererFactory",
    "search_best_clusterer",
    "EmbeddingClusteringPipeline",
]
