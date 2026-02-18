"""Tests for casas_floripa views."""

import pytest
from model_bakery import baker

from casas_floripa.models import Cliente, Pedido


@pytest.mark.django_db
class TestVendasView:
    """Tests for the vendas report view."""

    def test_returns_200_with_no_pedidos(self, client):
        response = client.get("/vendas/")
        assert response.status_code == 200

    def test_returns_200_with_pedidos(self, client):
        cliente = baker.make(Cliente)
        baker.make(Pedido, cliente=cliente, _quantity=3)
        response = client.get("/vendas/")
        assert response.status_code == 200
        assert b"Casas Floripa" in response.content

    def test_all_param_returns_all_pedidos(self, client):
        cliente = baker.make(Cliente)
        baker.make(Pedido, cliente=cliente, _quantity=2)
        response = client.get("/vendas/?all")
        assert response.status_code == 200
        assert response.content.count(b"<tr>") >= 2  # header + 2 data rows
