from django.contrib import admin
from .models import Produtos

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'familia', 'unidade_de_medida')
    list_display_links = ('codigo', 'descricao', 'familia', 'unidade_de_medida')
    list_filter = ('codigo', 'descricao', 'familia', 'unidade_de_medida')
    list_per_page = 10
    search_fields = ('codigo', 'descricao', 'familia', 'unidade_de_medida')


admin.site.register(Produtos, ProdutosAdmin)