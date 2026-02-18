"""
Seed 0040: preenche vector_embedding com dados fake (vetor-like) em Cliente e Produto.
Rodar após 0010, 0020, 0030. Uso: uv run python manage.py seed
"""

import random

from casas_floripa.models import Cliente, Produto

random.seed(42)
fake_vector = (
    "[" + ",".join(str(round(random.uniform(-1, 1), 6)) for _ in range(1536)) + "]"
)

n_clientes = Cliente.objects.all().update(vector_embedding=fake_vector)
n_produtos = Produto.objects.all().update(vector_embedding=fake_vector)

print(
    f"Vector embedding (fake) atualizado: {n_clientes} clientes, {n_produtos} produtos."
)
