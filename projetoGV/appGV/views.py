from django.shortcuts import render
from .models import User

def home(request):
    return render(request,'usuarios/home.html')

def users(request):
    #dados salvos no banco de dados
    newUser = User()
    newUser.nome = request.POST.get('nome')
    newUser.idade = request.POST.get('idade')

    newUser.save()

    #exibir cadastros em outra página
    users = {
        'usuarios': User.objects.all()
    }

    #retornar os dados para a página de listagem
    return render(request, 'usuarios/usuarios.html', users)