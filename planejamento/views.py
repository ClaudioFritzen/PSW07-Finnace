from django.shortcuts import render


# lib para deixar de fazer a csrf_token 
from django.views.decorators.csrf import csrf_exempt

import json
from django.http import JsonResponse

from django.http import HttpResponse, JsonResponse

## importando o banco de dados
from extrato.models import Valores

from perfil.models import Categoria, Conta


# Create your views here.

def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})


@csrf_exempt
def update_valor_categoria(request, id):

    novo_valor = json.load(request)['novo_valor']
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = novo_valor
    print(categoria)

    categoria.save()

    return JsonResponse({'status': 'Sucesso '})
