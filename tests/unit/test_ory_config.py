"""Tests for Ory configuration models."""

import pytest
from bindu.settings import (
    KratosConfig,
    OAuthProviderConfig,
)


class TestKratosConfig:
    """Test Kratos configuration."""

    def test_default_config(self):
        """Test default Kratos configuration."""
        config = KratosConfig()
        assert config.enabled is True
        assert config.timeout == 10

    def test_valid_encryption_key(self):
        """Test valid encryption key."""
        key = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="  # pragma: allowlist secret
        config = KratosConfig(encryption_key=key)
        assert config.encryption_key == key

    def test_invalid_encryption_key(self):
        """Test invalid encryption key."""
        with pytest.raises(ValueError):
            KratosConfig(encryption_key="invalid")  # pragma: allowlist secret


class TestOAuthProviderConfig:
    """Test OAuth provider configuration."""

    def test_provider_config(self):
        """Test OAuth provider configuration."""
        config = OAuthProviderConfig(
            name="github",
            client_id="test_id",  # pragma: allowlist secret
            client_secret="test_secret",  # pragma: allowlist secret
            auth_url="https://github.com/login/oauth/authorize",
            token_url="https://github.com/login/oauth/access_token",
            scope="read:user",
            redirect_uri="http://localhost:3000/callback",
        )
        assert config.name == "github"


