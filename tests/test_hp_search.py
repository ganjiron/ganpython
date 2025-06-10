from interlock_ml import TfidfEmbedder, KMeansClusterer, search_best_pipeline


def test_search_best_pipeline_returns_params_and_score():
    texts = ["cat meows" for _ in range(5)] + ["dog barks" for _ in range(5)]
    param_grid = {"n_clusters": [2, 3]}
    best_params, best_score = search_best_pipeline(TfidfEmbedder, KMeansClusterer, param_grid, texts)
    assert isinstance(best_score, float)
    assert "n_clusters" in best_params
