"""
Seed script para criar pedidos com itens variados.
Uso: uv run python manage.py seed  (ou shell < seeds/0030_seed_pedidos.py)

ATENÇÃO: este script deleta todos os pedidos/itens existentes antes de recriar,
pois pedidos não têm chave natural fácil para get_or_create.
"""

import random
from datetime import timedelta
from decimal import Decimal

from django.utils import timezone

from casas_floripa.models import Cliente, ItemPedido, Pedido, Produto

random.seed(42)

NUM_PEDIDOS = 2000


def _sortear_quantidade():
    """90% quantidade 1, 5% quantidade 2, 5% aleatório entre 1 e 4."""
    roll = random.random()
    if roll < 0.90:
        return 1
    elif roll < 0.95:
        return 2
    else:
        return random.randint(1, 4)


def run():
    clientes = list(Cliente.objects.all())
    produtos = list(Produto.objects.all())

    if not clientes:
        print("Nenhum cliente encontrado. Rode seed_clientes.py primeiro.")
        return
    if not produtos:
        print("Nenhum produto encontrado. Rode seed_produtos.py primeiro.")
        return

    # Limpa pedidos anteriores (cascade deleta itens)
    deleted_count, _ = Pedido.objects.all().delete()
    if deleted_count:
        print(f"Removidos {deleted_count} registros anteriores (pedidos + itens).")

    now = timezone.now()
    pedidos = []
    all_itens = []

    for i in range(NUM_PEDIDOS):
        cliente = random.choice(clientes)

        # Distribuição de status: ~60% fechado, ~25% aberto, ~15% cancelado
        roll = random.random()
        if roll < 0.60:
            status = Pedido.StatusPedido.FECHADO
        elif roll < 0.85:
            status = Pedido.StatusPedido.ABERTO
        else:
            status = Pedido.StatusPedido.CANCELADO

        # Desconto: ~70% sem desconto, ~30% com 5-15%
        if random.random() < 0.70:
            desconto_pct = Decimal("0.00")
        else:
            desconto_pct = Decimal(str(random.randint(5, 15)))

        # Data de criação: nos últimos 365 dias, hora/minuto aleatórios
        segundos_atras = random.randint(0, 365 * 24 * 3600)
        data_criacao = now - timedelta(seconds=segundos_atras)

        # Data de entrega: apenas para pedidos fechados
        data_entrega = None
        if status == Pedido.StatusPedido.FECHADO:
            data_entrega = (data_criacao + timedelta(days=random.randint(2, 15))).date()

        pedido = Pedido(
            cliente=cliente,
            status=status,
            desconto_pct=desconto_pct,
            data_entrega=data_entrega,
        )
        pedidos.append((pedido, data_criacao))

    # Bulk create pedidos
    pedidos_objs = Pedido.objects.bulk_create([p for p, _ in pedidos])

    # Atualiza data_criacao (auto_now_add impede setar no bulk_create)
    for pedido_obj, (_, data_criacao) in zip(pedidos_objs, pedidos):
        Pedido.objects.filter(pk=pedido_obj.pk).update(data_criacao=data_criacao)

    # Cria itens para cada pedido
    for pedido_obj in pedidos_objs:
        num_itens = random.randint(1, 5)
        produtos_pedido = random.sample(produtos, num_itens)

        for produto in produtos_pedido:
            all_itens.append(
                ItemPedido(
                    pedido=pedido_obj,
                    produto=produto,
                    quantidade=_sortear_quantidade(),
                    preco_venda=produto.preco,
                )
            )

    ItemPedido.objects.bulk_create(all_itens)

    print(f"Pedidos criados: {len(pedidos_objs)}")
    print(f"Itens criados: {len(all_itens)}")

    # Resumo por status
    for status_choice in Pedido.StatusPedido:
        count = sum(1 for p in pedidos_objs if p.status == status_choice.value)
        print(f"  - {status_choice.label}: {count}")

    # Fake vector embedding (mesmo padrão de Produto/Cliente; útil para demo de .only())
    fake_vector = (
        "[" + ",".join(str(round(random.uniform(-1, 1), 6)) for _ in range(1536)) + "]"
    )
    n = Pedido.objects.all().update(vector_embedding=fake_vector)
    print(f"Vector embedding (fake) atualizado em {n} pedidos.")


run()
