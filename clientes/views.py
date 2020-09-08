from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Cliente

# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all().order_by('-id')

    paginator = Paginator(clientes, 5)
    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    
    return render(request, 'clientes/listar_clientes.html', {'clientes':clientes})