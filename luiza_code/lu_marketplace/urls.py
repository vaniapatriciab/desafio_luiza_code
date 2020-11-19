from .views import CadastrarProduto
from django.urls import path
from.import views

urlpatterns = [

    path('', views.index, name='luMarketplace-index'),

    path('cad_produtos/', CadastrarProduto.as_view(),
         name='luMarketplace-cadastro')
]
