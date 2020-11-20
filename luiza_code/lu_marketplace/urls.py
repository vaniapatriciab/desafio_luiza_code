from .views import CadastrarProduto, AtualizarProduto, BuscarProduto
from django.urls import path
from.import views


urlpatterns = [

    path('', views.index, name='luMarketplace-index'),

    path('cadastrar-prod/', CadastrarProduto.as_view(),
         name='luMarketplace-cadastro'),

    path('atualizar-prod/', AtualizarProduto.as_view(),
         name='luMarketplace-atualizar'),

    path('buscar-prod/', BuscarProduto.as_view(),
         name='luMarketplace-buscar-produto'),
]
