# -*-coding:utf-8-*-
from django.forms import ModelForm, CharField
from .models import Produto



class CadastraProduto(ModelForm):
    class Meta:
        model = Produto
        fields = ['prod_nome', 'prod_descricao', 'prod_preco', 'prod_codigo', 'prod_qtd', 'prod_inativo', 'vend_id']
        widgets = {'prod_nome': CharField(
            attrs={'class': 'form-control'})}

