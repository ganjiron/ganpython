from __future__ import annotations

from typing import Any, Dict, Type

from .embedding import Embedder
from .clustering import Clusterer


class EmbedderFactory:
    """Factory for creating embedders."""

    _registry: Dict[str, Type[Embedder]] = {}

    @classmethod
    def register(cls, name: str, embedder_cls: Type[Embedder]) -> None:
        cls._registry[name] = embedder_cls

    @classmethod
    def create(cls, name: str, **kwargs: Any) -> Embedder:
        if name not in cls._registry:
            raise ValueError(f"Unknown embedder '{name}'")
        return cls._registry[name](**kwargs)


class ClustererFactory:
    """Factory for creating clusterers."""

    _registry: Dict[str, Type[Clusterer]] = {}

    @classmethod
    def register(cls, name: str, clusterer_cls: Type[Clusterer]) -> None:
        cls._registry[name] = clusterer_cls

    @classmethod
    def create(cls, name: str, **kwargs: Any) -> Clusterer:
        if name not in cls._registry:
            raise ValueError(f"Unknown clusterer '{name}'")
        return cls._registry[name](**kwargs)
