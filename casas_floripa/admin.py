from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Categoria, Cliente, ItemPedido, Pedido, Produto, Usuario

admin.site.register(Usuario, UserAdmin)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email", "telefone", "data_nascimento_fmt", "status_financeiro")
    list_filter = ("status_financeiro",)
    search_fields = ("nome", "sobrenome", "email")

    @admin.display(description="Data Nascimento")
    def data_nascimento_fmt(self, obj):
        return obj.data_nascimento.strftime("%d/%m/%Y") if obj.data_nascimento else "-"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "preco", "quantidade_estoque", "codigo_fabricante")
    list_filter = ("categoria", "preco")
    search_fields = ("nome", "descricao", "codigo_fabricante")


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id_curto", "cliente", "status", "desconto_pct", "data_entrega_fmt", "data_criacao_fmt")
    list_filter = ("status", "data_entrega")
    search_fields = ("cliente__nome", "cliente__sobrenome")
    inlines = [ItemPedidoInline]

    @admin.display(description="ID")
    def id_curto(self, obj):
        return str(obj.id)[:8]

    @admin.display(description="Data Entrega")
    def data_entrega_fmt(self, obj):
        return obj.data_entrega.strftime("%d/%m/%Y") if obj.data_entrega else "-"

    @admin.display(description="Data Criação")
    def data_criacao_fmt(self, obj):
        return obj.data_criacao.strftime("%d/%m/%Y %H:%M")
