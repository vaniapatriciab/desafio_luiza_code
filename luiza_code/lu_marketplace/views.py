from django.shortcuts import render
from django.http import HttpResponse
from . models import Vendedor, Produto 

def index(request):
    produtos = Produto.objects.all()
    search = request.GET.get('search')
    if search:
        produtos = produtos.filter(prod_nome=search)
    context = {'produtos': produtos}
    return render(request, 'lu_marketplace/index.html', context)