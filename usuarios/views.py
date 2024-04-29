from django.shortcuts import render

from usuarios.forms import LoginForm

def login(request):
    context = {
        'form': LoginForm()
    }
    return render(request, 'usuarios/login.html', context)

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')
