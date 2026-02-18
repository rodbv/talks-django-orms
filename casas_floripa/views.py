from django.shortcuts import render

from casas_floripa.decorators import measure_time_and_memory
from casas_floripa.models import Pedido

DEFAULT_LIMIT = 10


@measure_time_and_memory
def vendas(request):
    pedidos = (
        Pedido.objects.order_by("-data_criacao")
        .select_related("cliente")
        .prefetch_related("itens")
    )

    if "all" not in request.GET:
        pedidos = pedidos[:DEFAULT_LIMIT]

    return render(request, "casas_floripa/vendas.html", {"pedidos": pedidos})
