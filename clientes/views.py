from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Cliente, Visitante
from django.views.decorators.csrf import requires_csrf_token, csrf_protect, csrf_exempt

def clientes(request):
    clientes = Cliente.objects.all().values()
    template = loader.get_template('lista_clientes.html')
    context = {
        'clientes': clientes,
    }
    return HttpResponse(template.render(context, request))

def detalhes(request, id):
    cliente = Cliente.objects.get(id=id)
    template = loader.get_template('detalhes.html')
    context = {
        'cliente': cliente,
    }
    return HttpResponse(template.render(context, request))

"""def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())"""

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

# foi necessário definir novas funções já que as funções anteriores só fazem 
# novos cadastros mediante um administrador. E não é viável o administrador 
# cadastrar cada visitante sempre que solicitado
def cadastro(request):
    template = loader.get_template('cadastro.html')
    return HttpResponse(template.render())

@csrf_protect
@csrf_exempt # -> único método que funcionou sem restricão do token
def novocad(request):
    # novocad recebe um objeto da classe Visitante
    novocad = Visitante()
    # aqui as variáveis recebem valores de nome e sobrenome do post 
    # para posterior comparação de valores contidos na variável que recebe os objetos 
    # da classe Visistante
    name = request.POST.get('firstname')
    lname = request.POST.get('lastname')

    if (Visitante.objects.filter(firstname=name).values()) | (Visitante.objects.filter(lastname=lname).values()):
        # Aqui falta implementar um código que retorna um alerta ao visitante 
        # mostrando que não pôde concluir cadastro por duplicidade 
        pass
    else:
        # constatado que os valores de nome e sobenome não são duplicados 
        # valores de telefone e  endereço são salvos na variável como método save()
        novocad.firstname = name
        novocad.lastname = lname
        novocad.phone = request.POST.get('phone')
        novocad.address = request.POST.get('address')
        novocad.save()
    
        # é passado um dicionário com todos os objetos da Classe Visitante 
        # para a variável listagem e passada como parãmetro a ser renderizado
        listagem = {
            'listagem': Visitante.objects.all()
        }
        return render(request, 'listagem.html', listagem)
    
def template(request):   
    return HttpResponse('hello world')