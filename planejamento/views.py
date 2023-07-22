from django.shortcuts import render, HttpResponse


## importando o banco de dados
from extrato.models import Valores

from perfil.models import Categoria, Conta


# Create your views here.

def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return HttpResponse(categorias)
    
