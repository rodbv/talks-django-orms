from django.db.models import F, Sum
from django.shortcuts import render

from casas_floripa.decorators import measure_time_and_memory
from casas_floripa.models import Pedido

DEFAULT_LIMIT = 10
STATUS_DISPLAY = dict(Pedido.StatusPedido.choices)


@measure_time_and_memory
def vendas(request):
    rows = (
        Pedido.objects.order_by("-data_criacao")
        .annotate(
            valor_total_calc=Sum(F("itens__preco_venda") * F("itens__quantidade"))
        )
        .values(
            "id",
            "status",
            "desconto_pct",
            "data_entrega",
            "data_criacao",
            "cliente__nome",
            "cliente__sobrenome",
            "valor_total_calc",
        )
    )

    if "all" not in request.GET:
        rows = rows[:DEFAULT_LIMIT]

    pedidos = [
        {
            **row,
            "status_display": STATUS_DISPLAY.get(row["status"], row["status"]),
            "cliente": f"{row['cliente__nome']} {row['cliente__sobrenome']}",
        }
        for row in rows
    ]
    for p in pedidos:
        del p["cliente__nome"], p["cliente__sobrenome"]

    return render(request, "casas_floripa/vendas.html", {"pedidos": pedidos})
