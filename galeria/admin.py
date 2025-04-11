from django.contrib import admin
from .models import Fotografia

''' Classe para listagem das fotografias '''
class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada') # Campos a serem exibidos
    list_display_links = ('id', 'nome') # Campos que serão links
    list_filter = ('categoria', 'usuario') # Filtros
    list_editable = ('publicada',)
    # list_per_page = 1 # Quantidade de fotografias por página
    search_fields = ('nome',) # Campo de busca

''' Registro das fotografias no painel de administração '''
admin.site.register(Fotografia, ListandoFotografias)