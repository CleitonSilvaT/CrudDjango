from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Cliente
from .forms import ClienteForm

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

def adicionar_clientes(request):
    form = ClienteForm(request.POST)

    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ClienteForm()
        return redirect('listar_clientes')

    return render(request, 'clientes/adicionar_clientes.html', {'form':form})