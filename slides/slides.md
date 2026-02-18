# ORMs com Python

Evitando os erros mais comuns.

<div style="display: flex; justify-content: space-between; margin-top: 2em; font-size: 0.7em; color: #888;">
  <span>Python Floripa 92</span>
  <span>rodrigo.vieira@gmail.com</span>
</div>

---

## O que são ORMs?

**ORM** = _Object-Relational Mapper_: mapeia objetos Python ↔ tabelas/linhas no banco

**Modelo (classe):**

```python
class Produto(ModelBase):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    codigo_fabricante = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    # ...
```

---

## O que são ORMs?

Consultas feitas em notação orientada a objetos...

```python
from datetime import date
Produto.objects.filter(
  preco__lte=100,
  data_criacao__gte=date(2026, 1, 1)
)
```

<div class="fragment">
<p>..viram consultas SQL em tempo de execução</p>
<pre><code class="language-sql" data-trim>SELECT "id","nome","descricao","preco"
FROM "casas_floripa_produto"
WHERE ("preco" <= 100
       AND "data_criacao" >= '2026-01-01 00:00:00')</code></pre>
</div>

---

## Vamos criar um relatório de vendas

<a href="http://localhost:8000/vendas/" target="_blank" rel="noopener noreferrer">Relatório de vendas</a>

---

## Como o Django usa ORMs

```python
def vendas(request):
    pedidos = Pedido.objects.order_by("-data_criacao")

    return render(
        request,
        "casas_floripa/vendas.html",
        {"pedidos": pedidos},
    )
```

---

## Como o Django usa ORMs

```jinja
<tbody>
  {% for pedido in pedidos %}
  <tr>
    <td>{{ pedido.id }}</td>
    <td>{{ pedido.cliente }}</td>
    <td>R$ {{ pedido.valor_total }}</td>
    <td>{{ pedido.desconto_pct }}%</td>
    <!-- ... mais colunas ... -->
  </tr>
  {% endfor %}
</tbody>
```
