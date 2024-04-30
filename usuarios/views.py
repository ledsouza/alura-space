from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

from usuarios.forms import LoginForm, CadastroForm

def login(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data['nome_login']
        password = form.cleaned_data['senha']
        usuario = auth.authenticate(request, username=username, password=password)

        if usuario is None:
            messages.error(request, 'Usuário ou senha inválidos')
            return redirect('login')
        else:
            auth.login(request, usuario)
            messages.success(request, 'Login realizado com sucesso')
            return redirect('index')

    return render(request, 'usuarios/login.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('login')

def cadastro(request):
    form = CadastroForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():       
        username = form.cleaned_data['nome_cadastro']
        email = form.cleaned_data['email']
        password = form.cleaned_data['senha_1']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Usuário já cadastrado')
            return redirect('cadastro')

        usuario = User.objects.create_user(username, email, password)
        usuario.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')

    return render(request, 'usuarios/cadastro.html', context)
