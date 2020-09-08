from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Cliente

# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all().order_by('-id')
    queryset = request.GET.get('q')

    if queryset:
        clientes = Cliente.objects.filter(
            Q(nome__icontains = queryset)|
            Q(cpf__icontains = queryset)|
            Q(email__icontains = queryset)
        )

    paginator = Paginator(clientes, 5)
    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    
    return render(request, 'clientes/listar_clientes.html', {'clientes':clientes})