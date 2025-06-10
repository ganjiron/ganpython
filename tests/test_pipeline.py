from interlock_ml import EmbeddingClusteringPipeline, TfidfEmbedder, KMeansClusterer


def test_pipeline_runs():
    pipeline = EmbeddingClusteringPipeline(TfidfEmbedder, KMeansClusterer, clusterer_kwargs={"n_clusters": 2})
    texts = ["hello world", "world hello", "another document"]
    labels = pipeline.run(texts)
    assert len(labels) == len(texts)
