import time

from django.shortcuts import render

from casas_floripa.models import Pedido


def vendas(request):
    inicio = time.monotonic()
    if "all" in request.GET:
        pedidos = Pedido.objects.all()
    else:
        limit = 10
        for key in request.GET:
            if key.isdigit():
                limit = int(key)
                break
        pedidos = Pedido.objects.all()[:limit]
    response = render(request, "casas_floripa/vendas.html", {"pedidos": pedidos})
    tempo = f"{time.monotonic() - inicio:.2f}".replace(".", ",")
    response.content = response.content.replace(b"__TEMPO__", tempo.encode())
    return response
