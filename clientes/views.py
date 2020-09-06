from django.shortcuts import render
from .models import Cliente

# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all().order_by('-id')

    
    return render(request, 'clientes/listar_clientes.html', {'clientes':clientes})