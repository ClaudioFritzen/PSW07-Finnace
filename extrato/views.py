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

        # TODO: fazer as mensagens aparecer de acordo com o tipo saida e entrada
        if tipo != 'S' and tipo != 'E':
            messages.add_message(request, constants.WARNING, 'Muito espertinho você! <br> Manda um email para teste@gmail.com')
            return redirect('/extrato/novo_valor' )
        

        ## FIXME: Essa função nao esta funcionando
        if valor.strip() == 0:
            valor = float(valor)
            print(f'Convertendo', type())
            if valor <= 0:
                print(type(valor))
                messages.add_message(request, constants.WARNING, 'Muito espertinho você! Não pode enviar numeros negativos!')
                return redirect('/extrato/novo_valor' )
                
            messages.add_message(request, constants.WARNING, 'Muito espertinho você! Não pode enviar numeros negativos ou espaços vazio!')
            return redirect('/extrato/novo_valor' )
        

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
        if tipo == 'S':
            messages.add_message(request, constants.INFO, 'Saída Registrada com sucesso!')
            return redirect('/extrato/novo_valor' )

        elif tipo == 'E':
            messages.add_message(request, constants.INFO, 'Entrada Registrada com sucesso!')
            return redirect('/extrato/novo_valor' )
        
        
        

        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    
    