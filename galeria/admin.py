from django.contrib import admin

from galeria.models import Fotografia

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'categoria', 'publicada', 'usuario')
    list_display_links = ('id', 'nome')
    list_filter = ('categoria', 'usuario')
    list_editable = ('publicada',)
    search_fields = ('nome', 'legenda')
    list_per_page = 10

admin.site.register(Fotografia, FotografiaAdmin)
