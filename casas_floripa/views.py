import time
import tracemalloc

from django.shortcuts import render
from silk.profiling.profiler import silk_profile

from casas_floripa.models import Pedido

DEFAULT_LIMIT = 10


@silk_profile(name="vendas")
def vendas(request):
    tracemalloc.start()
    inicio = time.monotonic()

    pedidos = Pedido.objects.order_by("-data_criacao")

    if "all" not in request.GET:
        pedidos = pedidos[:DEFAULT_LIMIT]

    response = render(request, "casas_floripa/vendas.html", {"pedidos": pedidos})

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tempo = f"{time.monotonic() - inicio:.2f}".replace(".", ",")
    memory_mb = peak / (1024 * 1024)
    memory_str = f"{memory_mb:.1f}"

    response.content = response.content.replace(b"__TEMPO__", tempo.encode())
    response.content = response.content.replace(b"__MEMORY__", memory_str.encode())

    return response
