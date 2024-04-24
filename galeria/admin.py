from django.contrib import admin

from galeria.models import Fotografia

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')
    list_display_links = ('id', 'nome')
    list_filter = ('nome',)
    search_fields = ('nome', 'legenda')

admin.site.register(Fotografia, FotografiaAdmin)
