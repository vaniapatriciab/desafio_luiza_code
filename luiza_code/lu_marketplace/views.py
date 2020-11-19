from django.shortcuts import render
from django.http import HttpResponse
from . models import Produto
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin



def index(request):
    produtos = Produto.objects.all()
    search = request.GET.get('search')
    if search:
        produtos = produtos.filter(prod_nome__icontains=search)

    context = {'produtos': produtos}
    return render(request, 'lu_marketplace/index.html', context)


class CadastrarProduto(SuccessMessageMixin, CreateView):
    model = Produto
    template_name = 'cadastrar_prod.html'
    fields = '__all__'
    success_message = 'Produto cadastrado com sucesso!'
    def get_success_url(self):  
        return '/'


