from django.shortcuts import render
from django.http import HttpResponse
from . models import Produto
from django.views.generic import CreateView


def index(request):
    produtos = Produto.objects.all()
    search = request.GET.get('search')
    if search:
        produtos = produtos.filter(prod_nome=search)

    context = {'produtos': produtos}
    return render(request, 'lu_marketplace/index.html', context)


class CadastrarProduto(CreateView):
    model = Produto
    template_name = 'cadastrar_prod.html'
    fields = '__all__'
