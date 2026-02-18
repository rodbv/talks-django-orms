"""Tests for casas_floripa models."""

from decimal import Decimal

import pytest
from model_bakery import baker

from casas_floripa.models import Cliente, ItemPedido, Pedido, Produto


@pytest.mark.django_db
class TestPedidoValorTotal:
    """Tests for Pedido.valor_total property."""

    def test_valor_total_sem_itens(self):
        cliente = baker.make(Cliente)
        pedido = baker.make(Pedido, cliente=cliente, desconto_pct=Decimal("0"))
        assert pedido.valor_total == Decimal("0.00")

    def test_valor_total_com_um_item(self):
        cliente = baker.make(Cliente)
        produto = baker.make(Produto, preco=Decimal("10.00"))
        pedido = baker.make(Pedido, cliente=cliente, desconto_pct=Decimal("0"))
        baker.make(
            ItemPedido,
            pedido=pedido,
            produto=produto,
            quantidade=2,
            preco_venda=Decimal("10.00"),
        )
        assert pedido.valor_total == Decimal("20.00")


@pytest.mark.django_db
class TestPedidoStr:
    """Tests for Pedido string representation."""

    def test_str_includes_id_and_cliente(self):
        cliente = baker.make(Cliente, nome="João", sobrenome="Silva")
        pedido = baker.make(Pedido, cliente=cliente)
        s = str(pedido)
        assert "Pedido" in s
        assert str(pedido.id) in s
        assert "João" in s or "Silva" in s
