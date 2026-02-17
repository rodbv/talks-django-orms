from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Categoria, Cliente, Produto, Usuario

admin.site.register(Usuario, UserAdmin)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email", "telefone", "data_nascimento", "status_financeiro")
    list_filter = ("status_financeiro",)
    search_fields = ("nome", "sobrenome", "email")


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "preco", "quantidade_estoque", "codigo_fabricante")
    list_filter = ("categoria", "preco")
    search_fields = ("nome", "descricao", "codigo_fabricante")
