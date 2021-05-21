from django.contrib import admin
from .models import Produtos

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'familia')
    list_display_links = ('codigo', 'descricao', 'familia')
    list_filter = ('codigo', 'descricao', 'familia')
    list_per_page = 10
    search_fields = ('codigo', 'descricao', 'familia')


admin.site.register(Produtos, ProdutosAdmin)