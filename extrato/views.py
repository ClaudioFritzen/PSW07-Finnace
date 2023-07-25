from io import BytesIO
from django.shortcuts import render,redirect
from django.http import HttpResponse, FileResponse

## importando a função
from extrato.utils import converter_para_float

from perfil.models import Categoria, Conta
from django.contrib import messages
from django.contrib.messages import constants

from perfil.models import Conta, Categoria

from datetime import datetime

from django.conf import settings 
import os

from django.template.loader import render_to_string

from weasyprint import HTML

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

        # TODO: função working
        if tipo != 'S' and tipo != 'E':
            messages.add_message(request, constants.WARNING, 'Muito espertinho você! <br> Manda um email para teste@gmail.com')
            return redirect('/extrato/novo_valor', {'categorias':categoria, 'contas':contas} )
        
        if descricao.strip() == 0:
            messages.add_message(request, constants.WARNING, 'Descrição não pode ficar vazia!')
            return redirect('/extrato/novo_valor', {'categorias':categoria, 'contas':contas} )
        
        ## FIXME: 

         ## verificando se esta vazio
        if not valor:
            messages.add_message(request, constants.ERROR, 'O campo de valor não pode estar vazio!! ')
            return redirect('/extrato/novo_valor', {'categoria':categoria, 'conta':conta} )
        
        ##
        try:
            valor = float(valor)
            if valor < 0 or valor > 1000:
                messages.add_message(request, constants.ERROR, 'Valor permitido de 0 a 1000')
                return redirect('/extrato/novo_valor', {'categoria':categoria, 'conta':conta} )

        except ValueError:
            messages.add_message(request, constants.ERROR, 'Insira um valor ')
            return redirect('/extrato/novo_valor', {'categoria':categoria, 'contas':conta} )

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

        # Atualizando os valor dinamicamente
        conta = Conta.objects.get(id=conta)

        if tipo == 'E':
            conta.valor += int(valor)
        else:
            conta.valor -= int(valor)

        conta.save()
        return render(request, 'novo_valor.html')

def views_extrato(request):
    
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()

    valores = Valores.objects.filter(data__month=datetime.now().month)

    ### filtros
    conta_get = request.GET.get('conta')
    categoria_get = request.GET.get('categoria')

    if conta_get:
        valores = valores.filter(conta__id=conta_get)

    if categoria_get:
        valores = valores.filter(categoria__id=categoria_get)

    # TODO: limpar os filtros com um botao

    # TODO: Limpar por periodo

    return render(request, 'views_extrato.html', {'contas':contas, 'categorias':categorias, 'valores':valores})

def exportar_pdf(request):
    valores = Valores.objects.filter(data__month=datetime.now().month)
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()

    path_template = os.path.join(settings.BASE_DIR, 'templates/partials/particial_extrato.html')
    template_render = render_to_string(path_template, {'valores': valores, 'contas':contas, 'categorias':categorias})
    
    # salvando na memoria para não ocupar espaço desnessesario
    path_output = BytesIO()

    HTML(string=template_render).write_pdf(path_output)
    # voltando o ponteiro ate o inicio do arquivo
    path_output.seek(0)

    # TODO manipular css da renderização

    return FileResponse(path_output, filename='extrato.pdf')

 