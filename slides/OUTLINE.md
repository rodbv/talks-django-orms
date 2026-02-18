## Django ORM performance: avoiding the most common mistakes

**Talk length:** 30–40 minutes  
**Style:** Show current situation → fix one issue → measure improvement (Debug Toolbar, profiling) → “Are we done?” → repeat until done.

---

## 1. Intro to ORM

- [ ]

- Brief intro: ORM translates Python code into SQL queries.
- Show a simple example (e.g. `Pedido.objects.filter(status='aberto')` or `Model.objects.all()`) and the SQL it generates — so the audience is clear that every Python expression can become one or more queries.

---

## 2. Show v1 (no optimizations)

- [ ]

- Demo the `/vendas` page as-is: no `prefetch_related`, no `select_related`, no `only()`, no index on ordering.
- Open Debug Toolbar and show the high query count (e.g. ~2000 with `?all` for 1000 pedidos).
- Mention the two N+1 sources: FK (`cliente`) and the `valor_total` property (iterates `itens`).

---

## 3. Fix N+1: prefetch_related + select_related

- [ ]

- Add `select_related("cliente")` and `prefetch_related("itens")`.
- Reload, show new query count and load time in Debug Toolbar.
- **“Are we done?”** → No.

---

## 4. Compute in the DB instead of Python

- [ ]

- We’re still loading all `itens` rows just to sum them for `valor_total`.
- Use `annotate(valor_total=Coalesce(Sum(F("itens__preco_venda") * F("itens__quantidade")), 0, output_field=DecimalField()))` (discount is reference-only; ignore it — just price × quantity).
- Template uses the annotated value instead of the property.
- **“Are we done?”** → No.

---

## 5. SELECT \* → only()

- [ ]

- Show that we’re still fetching all columns (SELECT \*).
- Add `only()` (and `defer()` if needed) to limit columns.
- Clarify: same number of queries, but less data per row (memory and I/O).
- **“Are we done?”** → No.

---

## 6. EXPLAIN and index

- [ ]

- Show the query plan (SQLite: `EXPLAIN QUERY PLAN`) — e.g. full table SCAN on the default ordering.
- Add an index (e.g. `db_index=True` on `data_criacao` for `ordering = ["-data_criacao"]`).
- Show plan again (SEARCH using index).
- **“Are we done?”** → No.

---

## 7. Regression: client asked for `produto.nome`

- [ ]

- Add something in the template that touches `item.produto` (e.g. product name).
- Show in Debug Toolbar that N+1 is back (queries on `Produto`).
- **Two defences:**
  - **Test:** `assertNumQueries(N)` so the test breaks when someone adds a new relation access in the template.
  - **DTO:** Build a minimal context (dicts or dataclasses) with only what the view decided to load. The template can’t trigger N+1 on data that isn’t in the DTO. Stabilizes the view→template contract.

---

## 8. If time: tooling (django-seal or zen-queries)

- [ ]

- **zen-queries:** Explicitly mark where queries are allowed; raises awareness of “queries in view vs in template.”
- **django-seal:** “Sealed” instances that block access to unloaded relations (fails fast in dev instead of in production).
- Pick one and show in 2–3 minutes as an optional safety net.

---

## Checklist for the day

- [ ] Intro: show Python → SQL (ORM in a nutshell).
- [ ] v1: no prefetch/select_related; Debug Toolbar shows high query count with `?all` (~2000 for 1000 pedidos).
- [ ] Step 3: prefetch + select_related; show drop in queries and time.
- [ ] Step 4: annotate `valor_total` with Sum in DB; template uses it.
- [ ] Step 5: add `only()`; show same query count, better memory/time.
- [ ] Step 6: EXPLAIN QUERY PLAN before/after index on `data_criacao`.
- [ ] Step 7: reintroduce `produto.nome` in template; show N+1; demo `assertNumQueries` and DTO.
- [ ] Step 8 (optional): short demo of zen-queries or django-seal.
