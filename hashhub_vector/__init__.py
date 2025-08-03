"""
HashHub Vector SDK - Python client for HashHub Vector API

A powerful, easy-to-use Python SDK for the HashHub Vector API that provides 
high-quality text embeddings with multilingual support.

Features:
- 6 embedding models with different performance/cost trade-offs
- Support for 80+ languages including Turkish
- Async/sync support with automatic retries
- Built-in rate limiting and error handling
- OpenAI-compatible interface
- Comprehensive documentation

Example:
    >>> from hashhub_vector import HashHubVector
    >>> client = HashHubVector(api_key="your-api-key")
    >>> embeddings = client.vectorize("Merhaba dünya!")
    >>> print(embeddings.vector[:5])  # First 5 dimensions
"""

from .client import HashHubVector
from .models import (
    VectorizeRequest,
    VectorizeResponse,
    BatchVectorizeRequest,
    BatchVectorizeResponse,
    ModelInfo
)
from .exceptions import (
    HashHubVectorError,
    AuthenticationError,
    RateLimitError,
    ModelNotFoundError,
    ValidationError
)

__version__ = "1.0.0"
__author__ = "HashHub Team"
__email__ = "support@hashhub.dev"
__description__ = "Python SDK for HashHub Vector API - High-quality multilingual text embeddings"

__all__ = [
    "HashHubVector",
    "VectorizeRequest",
    "VectorizeResponse", 
    "BatchVectorizeRequest",
    "BatchVectorizeResponse",
    "ModelInfo",
    "HashHubVectorError",
    "AuthenticationError",
    "RateLimitError",
    "ModelNotFoundError",
    "ValidationError"
]
