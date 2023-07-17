from django.shortcuts import render,redirect
from django.http import HttpResponse

from perfil.models import Categoria, Conta
from django.contrib import messages
from django.contrib.messages import constants

from extrato.models import Valores
# Create your views here.
def novo_valor(request):
    if request.method == "GET":
        contas = Conta.objects.all()
        categorias = Categoria.objects.all() 
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    
    elif request.method == "POST":
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo')

        ## criando uma instancia no banco
        valores = Valores (
            valor=valor,
            categoria_id=categoria,
            data=data,
            descricao=descricao,
            conta_id=conta,
            tipo=tipo
        )

        # salvando de fato
        valores.save()

        #mensagens
        # TODO: fazer as mensagens aparecer de acordo com o tipo saida e entrada

        messages.add_message(request, constants.SUCCESS, 'Entrada/Saída cadastrada com sucesso!')

        
        return redirect('/extrato/novo_valor' )
        #return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    
    