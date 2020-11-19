from django.urls import path
from .views import CadastrarProduto

urlpatterns = [

    path('cad_produtos/', CadastrarProduto.as_view(),
         name='luMarketplace-cadastro')
]
