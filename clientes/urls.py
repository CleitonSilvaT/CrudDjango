from django.urls import path
from .views import listar_clientes

urlpatterns = [
    path('', listar_clientes, name='listar_clientes'),
]
