import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class ModelBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Usuario(ModelBase, AbstractUser):
    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"


class Cliente(ModelBase):
    class StatusFinanceiro(models.TextChoices):
        REGULAR = "regular", "Regular"
        PENDENTE = "pendente", "Pendente"
        BLOQUEADO = "bloqueado", "Bloqueado"

    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    data_nascimento = models.DateField(null=True, blank=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    status_financeiro = models.CharField(
        max_length=10,
        choices=StatusFinanceiro.choices,
        default=StatusFinanceiro.REGULAR,
    )

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
