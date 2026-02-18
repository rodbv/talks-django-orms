from django.db.models import Prefetch
from django.shortcuts import render

from casas_floripa.decorators import measure_time_and_memory
from casas_floripa.models import ItemPedido, Pedido

DEFAULT_LIMIT = 10


@measure_time_and_memory
def vendas(request):
    pedidos = (
        Pedido.objects.order_by("-data_criacao")
        .only(
            "id",
            "status",
            "desconto_pct",
            "data_entrega",
            "data_criacao",
            "cliente_id",
            "cliente__id",
            "cliente__nome",
            "cliente__sobrenome",
        )
        .select_related("cliente")
        .prefetch_related(
            Prefetch(
                "itens",
                queryset=ItemPedido.objects.only(
                    "pedido_id", "preco_venda", "quantidade"
                ),
            )
        )
    )

    if "all" not in request.GET:
        pedidos = pedidos[:DEFAULT_LIMIT]

    return render(request, "casas_floripa/vendas.html", {"pedidos": pedidos})
