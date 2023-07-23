from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
    return JsonResponse({'valor': f'Recebi o valor {id} '})
