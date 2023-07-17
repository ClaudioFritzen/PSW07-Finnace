from django.shortcuts import render
from django.http import HttpResponse

from perfil.models import Categoria, Conta

# Create your views here.
def novo_valor(request):
    if request.method == "GET":
        contas = Conta.objects.all()
        categorias = Categoria.objects.all() 
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    
    elif request.method == "POST":
        return HttpResponse("Mandou os dados para o banco!")