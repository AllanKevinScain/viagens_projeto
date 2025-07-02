from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

def clientes(request):
    query = request.GET.get('busca', '')
    if query:
        clientes = Cliente.objects.filter(nome__icontains=query)
    else:
        clientes = Cliente.objects.all()
        
    dados = {'clientes': clientes, 'query': query}
    return render(request, 'clientes/lista.html', dados)

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:lista')
    else:
        form = ClienteForm()
        dados = {'form': form}
    return render(request, 'clientes/cadastrar_cliente.html', dados)

def cliente_viagens(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    viagens = cliente.viagem_set.all()  

    context = {'cliente': cliente,'viagens': viagens}

    return render(request, 'clientes/viagem_por_cliente.html', context)