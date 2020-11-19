from django.shortcuts import render
from django.views.generic import CreateView
from .models import Produto


class CadastrarProduto(CreateView):
    model = Produto
    template_name = 'index.html'
    fields = '__all__'
