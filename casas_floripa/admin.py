from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Cliente, Usuario

admin.site.register(Usuario, UserAdmin)
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email", "telefone", "data_nascimento", "status_financeiro")
    list_filter = ("status_financeiro",)
    search_fields = ("nome", "sobrenome", "email")
