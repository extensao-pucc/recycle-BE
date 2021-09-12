from django.contrib import admin
from .models import Clientes


class ClientesAdmin(admin.ModelAdmin):
    list_display = ('razao_social_nome', 'CNPJ_CPF')
    list_display_links = ('razao_social_nome', 'CNPJ_CPF')
    list_filter = ('razao_social_nome', 'CNPJ_CPF')
    list_per_page = 10
    search_fields = ('razao_social_nome', 'CNPJ_CPF')


admin.site.register(Clientes, ClientesAdmin)