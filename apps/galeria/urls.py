from django.urls import path

from apps.galeria import views

urlpatterns = [
    path("", views.index, name="index"),
    path("imagem/<int:foto_id>", views.imagem, name="imagem"),
    path("buscar", views.buscar, name="buscar"),
    path("nova-imagem", views.nova_imagem, name="nova_imagem"),
    path("editar-imagem/<int:foto_id>", views.editar_imagem, name="editar_imagem"),
    path("remover-imagem/<int:foto_id>", views.remover_imagem, name="remover_imagem"),
] 