from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.db import models


class ModelBase(models.Model):
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


class Categoria(ModelBase):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nome


class Produto(ModelBase):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    codigo_fabricante = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    url_imagem = models.URLField(blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = "produto"
        verbose_name_plural = "produtos"

    def __str__(self):
        return self.nome


class Pedido(ModelBase):
    class StatusPedido(models.TextChoices):
        ABERTO = "aberto", "Aberto"
        FECHADO = "fechado", "Fechado"
        CANCELADO = "cancelado", "Cancelado"

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=StatusPedido.choices,
        default=StatusPedido.ABERTO,
    )
    desconto_pct = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    data_entrega = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"
        ordering = ["-data_criacao"]

    @property
    def valor_total(self):
        total = sum(item.preco_venda * item.quantidade for item in self.itens.all())
        total = Decimal(total)
        if self.desconto_pct:
            total *= 1 - self.desconto_pct / Decimal("100")
        return total.quantize(Decimal("0.01"))

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente}"


class ItemPedido(ModelBase):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "item do pedido"
        verbose_name_plural = "itens do pedido"

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
