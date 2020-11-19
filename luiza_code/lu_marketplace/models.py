from django.db import models
from django.db.models.deletion import CASCADE

class Vendedor(models.Model):
    vend_nome = models.CharField(max_length=100, verbose_name='Nome')
    vend_email = models.EmailField(max_length=254, verbose_name='E-mail')

    def __str__(self) -> str:
        return self.vend_nome

    



class Produto(models.Model):
    prod_nome = models.CharField(max_length=100, verbose_name='Nome')
    prod_descricao = models.TextField(max_length=100, verbose_name='Descrição')
    prod_preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço')
    prod_codigo = models.IntegerField(verbose_name='Código do Produto')
    prod_qtd = models.IntegerField(verbose_name='Quantidade')
    prod_inativo = models.BooleanField(default=False, verbose_name='Produto Inativo')
    vend_id = models.ForeignKey(Vendedor, on_delete=CASCADE, verbose_name='Vendedor')

    def __str__(self) -> str:
        return self.prod_nome
    