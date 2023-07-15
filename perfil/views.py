from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria, Conta
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.
def home(request):
    return render(request, 'home.html')

def gerenciar(request):
    return render(request, 'gerenciar.html')

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    # validar 
    icone = request.FILES.get('icone')
    
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/perfil/gerenciar/')
    
    if "icone" in request.FILES:
        logo = request.FILES['icone']
        if 'icone':
            if logo.size > 100_000_000:
                messages.add_message(request, constants.ERROR, 'A logo deve ter menos que 10MB')
                return redirect('/perfil/gerenciar/')
            else:
                # se a logo estiver vazio, defina como None
                logo = None
    else:
        # Se a chave ´logo' nao estiver em request.FILES, defina como none
        logo = None 


    
    # realizar mais validações

    conta = Conta(
        apelido = apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()
    messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso!')
    print(request.POST)
    
    return redirect('/perfil/gerenciar/',{'conta':conta})
    

def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    #total_contas = contas.aggregate(Sum('valor'))
    total_contas = 0

    for conta in contas:
        total_contas += conta.valor

    
    return render(request, 'gerenciar.html', {'contas': contas, 'total_contas': total_contas,'categorias':categorias})

def deletar_banco(request,id):
    conta = Conta.objects.get(id=id)

    conta.delete()
    messages.add_message(request, constants.WARNING, ' Conta Deletada!')

    return redirect('/perfil/gerenciar/')


#333
def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    #todo
    # classe is_instance p/ True or False

    categoria = Categoria(
        categoria=nome,
        essencial=essencial
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso')
    return redirect('/perfil/gerenciar/',)