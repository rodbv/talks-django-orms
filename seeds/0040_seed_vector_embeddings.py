"""
Seed 0040: preenche vector_embedding com dados fake (vetor-like) em Cliente, Produto, Pedido e ItemPedido.
Rodar após 0010, 0020, 0030. Uso: uv run python manage.py seed
"""

import random

from casas_floripa.models import Cliente, ItemPedido, Pedido, Produto

random.seed(42)
fake_vector = (
    "[" + ",".join(str(round(random.uniform(-1, 1), 6)) for _ in range(1536)) + "]"
)

n_clientes = Cliente.objects.all().update(vector_embedding=fake_vector)
n_produtos = Produto.objects.all().update(vector_embedding=fake_vector)
n_pedidos = Pedido.objects.all().update(vector_embedding=fake_vector)
n_itens = ItemPedido.objects.all().update(vector_embedding=fake_vector)

print(
    f"Vector embedding (fake) atualizado: {n_clientes} clientes, {n_produtos} produtos, {n_pedidos} pedidos, {n_itens} itens."
)
