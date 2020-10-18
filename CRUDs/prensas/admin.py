from django.contrib import admin
from .models import Prensas


class PrensasAdmin(admin.ModelAdmin):
    list_display = ('numero', 'descricao', 'detalhes_tecnicos')
    list_display_links = ('numero', 'descricao', 'detalhes_tecnicos')
    list_filter = ('numero', 'descricao', 'detalhes_tecnicos')
    list_per_page = 10
    search_fields = ('numero', 'descricao', 'detalhes_tecnicos')


admin.site.register(Prensas, PrensasAdmin)