"""Shared pytest fixtures for casas_floripa tests."""

import pytest


@pytest.fixture
def client():
    """Django test client."""
    from django.test import Client

    return Client()
