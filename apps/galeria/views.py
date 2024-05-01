from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar essa página.")
        return redirect("login")

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, "galeria/index.html", {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar essa página.")
        return redirect("login")
    
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar essa página.")
        return redirect("login")
    
    form = FotografiaForms(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Fotografia cadastrada com sucesso.")
        return redirect("index")

    context = {
        "form": form
    }
    return render(request, "galeria/nova_imagem.html", context)

def editar_imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar essa página.")
        return redirect("login")
    
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    form = FotografiaForms(instance=fotografia)
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, "Fotografia editada com sucesso.")
            return redirect("index")

    context = {
        "form": form,
        "foto_id": foto_id
    }
    return render(request, "galeria/editar_imagem.html", context)

def remover_imagem(request, foto_id):
    if not request.user.is_authenticated:
            messages.error(request, "Você precisa estar logado para acessar essa página.")
            return redirect("login")

    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    fotografia.delete()
    messages.success(request, "Fotografia removida com sucesso.")
    return redirect("index")