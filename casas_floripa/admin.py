from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html

from .models import Categoria, Cliente, ItemPedido, Pedido, Produto, Usuario

admin.site.register(Usuario, UserAdmin)


class PedidoInlineForCliente(admin.TabularInline):
    model = Pedido
    extra = 0
    fields = ("link_pedido", "status", "valor_total_fmt", "data_entrega_fmt", "data_criacao_fmt")
    readonly_fields = ("link_pedido", "status", "valor_total_fmt", "data_entrega_fmt", "data_criacao_fmt")
    show_change_link = False
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def link_pedido(self, obj):
        url = reverse("admin:casas_floripa_pedido_change", args=[obj.pk])
        return format_html('<a href="{}">{}</a>', url, str(obj.id)[:8])
    link_pedido.short_description = "Pedido"

    def valor_total_fmt(self, obj):
        return f"R$ {obj.valor_total:,.2f}"
    valor_total_fmt.short_description = "Valor Total"

    def data_entrega_fmt(self, obj):
        return obj.data_entrega.strftime("%d/%m/%Y") if obj.data_entrega else "-"
    data_entrega_fmt.short_description = "Data Entrega"

    def data_criacao_fmt(self, obj):
        return obj.data_criacao.strftime("%d/%m/%Y %H:%M")
    data_criacao_fmt.short_description = "Data Criação"


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email", "telefone", "data_nascimento_fmt", "status_financeiro")
    list_filter = ("status_financeiro",)
    search_fields = ("nome", "sobrenome", "email")
    inlines = [PedidoInlineForCliente]

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
    list_display = ("id_curto", "cliente", "status", "valor_total_fmt", "desconto_pct", "data_entrega_fmt", "data_criacao_fmt")
    list_filter = ("status", "data_entrega")
    search_fields = ("cliente__nome", "cliente__sobrenome")
    readonly_fields = ("valor_total_fmt",)
    inlines = [ItemPedidoInline]

    @admin.display(description="ID")
    def id_curto(self, obj):
        return str(obj.id)[:8]

    @admin.display(description="Valor Total")
    def valor_total_fmt(self, obj):
        return f"R$ {obj.valor_total:,.2f}"

    @admin.display(description="Data Entrega")
    def data_entrega_fmt(self, obj):
        return obj.data_entrega.strftime("%d/%m/%Y") if obj.data_entrega else "-"

    @admin.display(description="Data Criação")
    def data_criacao_fmt(self, obj):
        return obj.data_criacao.strftime("%d/%m/%Y %H:%M")
