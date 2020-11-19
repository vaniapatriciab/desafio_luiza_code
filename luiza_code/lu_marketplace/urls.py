from .views import CadastrarProduto
from django.urls import path
from.import views

urlpatterns = [

    path('', views.index, name='luMarketplace-index'),

    path('cadastrar-prod/', CadastrarProduto.as_view(),
         name='luMarketplace-cadastro')
]
