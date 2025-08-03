"""
HashHub Vector API Python SDK - Custom Exceptions

This module defines custom exceptions for the HashHub Vector SDK,
providing clear error handling and debugging information.
"""

from typing import Optional, Dict, Any


class HashHubVectorError(Exception):
    """Base exception for all HashHub Vector SDK errors."""
    
    def __init__(self, message: str, status_code: Optional[int] = None, response_data: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_data = response_data or {}


class AuthenticationError(HashHubVectorError):
    """Raised when API key is invalid or missing."""
    
    def __init__(self, message: str = "Invalid or missing API key"):
        super().__init__(message, status_code=401)


class RateLimitError(HashHubVectorError):
    """Raised when rate limit is exceeded."""
    
    def __init__(self, message: str = "Rate limit exceeded", retry_after: Optional[int] = None):
        super().__init__(message, status_code=429)
        self.retry_after = retry_after


class ModelNotFoundError(HashHubVectorError):
    """Raised when specified model is not available."""
    
    def __init__(self, model: str):
        message = f"Model '{model}' not found. Available models: gte_base, nomic_base, e5_base, mpnet_base, e5_small, minilm_base"
        super().__init__(message, status_code=404)
        self.model = model


class ValidationError(HashHubVectorError):
    """Raised when request parameters are invalid."""
    
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class QuotaExceededError(HashHubVectorError):
    """Raised when account quota is exceeded."""
    
    def __init__(self, message: str = "Account quota exceeded"):
        super().__init__(message, status_code=402)


class ServerError(HashHubVectorError):
    """Raised when server encounters an internal error."""
    
    def __init__(self, message: str = "Internal server error"):
        super().__init__(message, status_code=500)


class TimeoutError(HashHubVectorError):
    """Raised when request times out."""
    
    def __init__(self, message: str = "Request timed out"):
        super().__init__(message, status_code=408)


class NetworkError(HashHubVectorError):
    """Raised when network connection fails."""
    
    def __init__(self, message: str = "Network connection failed"):
        super().__init__(message)
