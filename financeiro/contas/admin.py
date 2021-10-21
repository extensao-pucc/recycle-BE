from django.contrib import admin
from .models import Contas

class ContasAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data', 'tipo', 'valor', 'situacao')
    list_display_links = ('descricao', 'data', 'tipo', 'valor', 'situacao')
    list_filter = ('descricao', 'data', 'tipo', 'valor', 'situacao')
    list_per_page = 10
    search_fields = ('descricao', 'data', 'tipo', 'valor', 'situacao')


admin.site.register(Contas, ContasAdmin)
