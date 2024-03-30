from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Cliente, Visitante
from django.views.decorators.csrf import requires_csrf_token, csrf_protect, csrf_exempt
# criei um arquivo de funções para depois importa aqui nas views
# para a função cadastro não ficar muito grande, 
# usando definições de herança para o projeto e conceitos de modulo
from .my_functions import tamanho_valid, confere_senha

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
    user = request.POST.get('username')
    senha = request.POST.get('password')
    senha1 = request.POST.get('confirm_pass')

    if (Visitante.objects.filter(firstname=name).values()) and (Visitante.objects.filter(lastname=lname).values()):
        template = loader.get_template('has_name_lastname.html')
        return HttpResponse(template.render())
    
    elif (Visitante.objects.filter(username=user).values()):
        template = loader.get_template('has_user.html')
        return HttpResponse(template.render())
    
    else:
        
        # passado a verificação de nome e usuário, próxima verificação:
        
        if tamanho_valid(senha) == False:
            return HttpResponse(f'<h1>Senha Fraca</h1>')
        
        elif (tamanho_valid(senha) == True) and (confere_senha(senha, senha1) == False):
            return HttpResponse(f'<h1>Senha não Confere!</h1>')
        
        else:
            senha = senha         
          
        # constatado que os valores não são duplicados 
        # valores são salvos com o método save()
        
        novocad.firstname = name
        novocad.lastname = lname
        novocad.phone = request.POST.get('phone')
        novocad.address = request.POST.get('address')
        novocad.username = user
        novocad.password = senha
        novocad.save()
                
    # é passado um dicionário com todos os objetos da Classe Visitante 
    # para a variável listagem e passada como parãmetro a ser renderizado
    # alterei a identação de 64 à 68 pois estava dando erro caso tentasse
    # cadastrar o mesmo nome de visitante

    listagem = {
        'listagem': Visitante.objects.all()
    }
    return render(request, 'listagem.html', listagem)

