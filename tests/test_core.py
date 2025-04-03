"""Tests for the core functionality of Verifex Omnium."""

import pytest
from verifex_omnium.core import ContentVerifier


def test_content_verifier_initialization():
    """Test that ContentVerifier can be initialized."""
    verifier = ContentVerifier()
    assert verifier.blockchain_provider == "polygon"
    
    custom_verifier = ContentVerifier(blockchain_provider="ethereum")
    assert custom_verifier.blockchain_provider == "ethereum"


def test_generate_signature():
    """Test generating a signature."""
    verifier = ContentVerifier()
    signature = verifier.generate_signature("test content", "text")
    
    assert isinstance(signature, dict)
    assert "signature" in signature
    assert signature["content_type"] == "text"
    assert "timestamp" in signature
    assert signature["blockchain"] == "polygon"


def test_verify_signature():
    """Test verifying a signature."""
    verifier = ContentVerifier()
    verification = verifier.verify_signature("test content", "sample_signature", "text")
    
    assert isinstance(verification, dict)
    assert "verified" in verification
    assert isinstance(verification["verified"], bool)
    assert "confidence" in verification
    assert verification["blockchain"] == "polygon"


def test_generate_embedding():
    """Test generating embeddings."""
    verifier = ContentVerifier()
    embedding = verifier.generate_embedding("test content", "text")
    
    assert isinstance(embedding, list)
    assert all(isinstance(val, float) for val in embedding)
