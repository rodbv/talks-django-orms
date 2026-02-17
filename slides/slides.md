# Django ORM — performance

Evitando os erros mais comuns

---

## O que vamos ver

- **N+1:** muitas queries onde poucas bastariam
- **SELECT \*** e **only():** trazer só o que a view usa
- **Cálculo no banco:** `Sum()`, `Count()` em vez de Python
- **Índices:** EXPLAIN e quando criar índice
- **Regressão:** assertNumQueries e DTO para não quebrar

---

## Exemplo de código

```python
# Sem otimização: 1 + N + N queries
pedidos = Pedido.objects.all()[:100]
for pedido in pedidos:
    print(pedido.cliente)      # N+1
    print(pedido.valor_total)   # N+1 (property usa itens.all())
```

**Com select_related + prefetch_related:** 3 queries no total.
