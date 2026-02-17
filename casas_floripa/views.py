import time

from django.shortcuts import render

from casas_floripa.models import Pedido


def vendas(request):
    inicio = time.monotonic()
    if "all" in request.GET:
        pedidos = Pedido.objects.all()
    else:
        pedidos = Pedido.objects.all()[:10]
    response = render(request, "casas_floripa/vendas.html", {"pedidos": pedidos})
    tempo = f"{time.monotonic() - inicio:.1f}".replace(".", ",")
    response.content = response.content.replace(b"__TEMPO__", tempo.encode())
    return response
