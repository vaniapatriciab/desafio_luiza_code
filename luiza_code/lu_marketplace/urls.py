from django.urls import path
from .views import CadastrarProduto

urlpatterns = [
    path('', CadastrarProduto.as_view(), name='luMarketplace-index'),
]
