from django.shortcuts import render, redirect
from .models import Viagem
from .forms import ViagemForm

def index(_):
    return render("index.html")

def viagens(request):
    query = request.GET.get('busca', '')
    if query:
        viagens = Viagem.objects.filter(destino__icontains=query)
    else:
        viagens = Viagem.objects.all()

    dados = {'viagens': viagens, 'query': query}
    return render(request, 'viagens/lista.html', dados)

def cadastrar_viagem(request):
    if request.method == 'POST':
        form = ViagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viagens:lista')
    else:
        form = ViagemForm()
        dados = {'form': form}
    return render(request, 'viagens/cadastrar_viagem.html', dados)

