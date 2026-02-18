import time

from django.shortcuts import render

from casas_floripa.models import Pedido

DEFAULT_LIMIT = 25


def vendas(request):
    inicio = time.monotonic()

    pedidos = Pedido.objects.order_by("-data_criacao")

    if "all" not in request.GET:
        pedidos = pedidos[:DEFAULT_LIMIT]

    response = render(request, "casas_floripa/vendas.html", {"pedidos": pedidos})

    tempo = f"{time.monotonic() - inicio:.2f}".replace(".", ",")

    response.content = response.content.replace(b"__TEMPO__", tempo.encode())

    return response
