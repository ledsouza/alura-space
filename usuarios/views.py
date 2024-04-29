from django.shortcuts import render

from usuarios.forms import LoginForm, CadastroForm

def login(request):
    context = {
        'form': LoginForm()
    }
    return render(request, 'usuarios/login.html', context)

def cadastro(request):
    context = {
        'form': CadastroForm()
    }
    return render(request, 'usuarios/cadastro.html', context)
