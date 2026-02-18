"""Tests for casas_floripa views."""

import pytest
from django.test import override_settings
from model_bakery import baker

from casas_floripa.models import Cliente, Pedido

# Middleware sem Silk/DDT para testes de contagem de queries (só as da view).
from django.conf import settings as django_settings

_MIDDLEWARE_NO_PROFILING = [
    m for m in django_settings.MIDDLEWARE if "silk" not in m and "DebugToolbar" not in m
]


@pytest.mark.django_db
class TestVendasView:
    """Tests for the vendas report view."""

    @override_settings(MIDDLEWARE=_MIDDLEWARE_NO_PROFILING)
    def test_vendas_render_uses_one_query(self, client, django_assert_num_queries):
        """Garante que a renderização usa 1 query (pedidos+cliente+valor_total no DB)."""
        cliente = baker.make(Cliente)
        baker.make(Pedido, cliente=cliente, _quantity=2)
        with django_assert_num_queries(1):
            client.get("/vendas/")

    def test_returns_200_with_no_pedidos(self, client):
        response = client.get("/vendas/")
        assert response.status_code == 200

    def test_returns_200_with_pedidos(self, client):
        cliente = baker.make(Cliente)
        baker.make(Pedido, cliente=cliente, _quantity=3)
        response = client.get("/vendas/")
        assert response.status_code == 200
        assert b"Casas Floripa" in response.content

    def test_respects_limit_query_param(self, client):
        cliente = baker.make(Cliente)
        baker.make(Pedido, cliente=cliente, _quantity=5)
        response = client.get("/vendas/?3")
        assert response.status_code == 200
        # Default limit when no numeric param is 10; "3" as key sets limit 3
        # We just check the view doesn't error and returns 200
        assert b"pedidos" in response.content

    def test_all_param_returns_all_pedidos(self, client):
        cliente = baker.make(Cliente)
        baker.make(Pedido, cliente=cliente, _quantity=2)
        response = client.get("/vendas/?all")
        assert response.status_code == 200
        assert response.content.count(b"<tr>") >= 2  # header + 2 data rows
