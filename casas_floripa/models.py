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
