from django.urls import path
from .views import listar_clientes
from .views import adicionar_clientes

urlpatterns = [
    path('', listar_clientes, name='listar_clientes'),
    path('adicionar_clientes/', adicionar_clientes, name='adicionar_clientes')
]
