from django.shortcuts import render

from perfil.models import Categoria, Conta

# Create your views here.
def novo_valor(request):
    if request.method == 'GET':
        contas = Conta.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'novo_valor.html', {'categorias':categorias, 'contas':contas})