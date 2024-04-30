from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from usuarios.forms import LoginForm, CadastroForm

def login(request, sucesso=None):
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
        'sucesso': sucesso
    }

    if form.is_valid():
        username = form.cleaned_data['nome_login']
        password = form.cleaned_data['senha']
        usuario = auth.authenticate(request, username=username, password=password)

        if usuario is None:
            context['erro'] = 'Usuário ou senha inválidos'
            return render(request, 'usuarios/login.html', context)
        else:
            auth.login(request, usuario)
            return redirect('index')

    return render(request, 'usuarios/login.html', context)

def cadastro(request):
    form = CadastroForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        if form.cleaned_data['senha_1'] != form.cleaned_data['senha_2']:
            context['erro'] = 'As senhas não conferem'
            return redirect('cadastro')
        
        username = form.cleaned_data['nome_cadastro']
        email = form.cleaned_data['email']
        password = form.cleaned_data['senha_1']

        if User.objects.filter(username=username).exists():
            context['erro'] = 'Nome de usuário já cadastrado'
            return redirect('cadastro')

        usuario = User.objects.create_user(username, email, password)
        usuario.save()
        return redirect('login', sucesso='Cadastro realizado com sucesso')

    return render(request, 'usuarios/cadastro.html', context)
