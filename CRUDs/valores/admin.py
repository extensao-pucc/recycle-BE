from django.contrib import admin
from .models import Valores

class ValoresAdmin(admin.ModelAdmin):
    list_display = ('produto', 'fornecedor', 'qualidade', 'preco_compra', 'preco_venda')
    list_display_links = ('produto', 'fornecedor', 'qualidade', 'preco_compra', 'preco_venda')
    list_filter = ('produto', 'fornecedor', 'qualidade', 'preco_compra', 'preco_venda')
    list_per_page = 10
    search_fields = ('produto', 'fornecedor', 'qualidade', 'preco_compra', 'preco_venda')


admin.site.register(Valores, ValoresAdmin)
