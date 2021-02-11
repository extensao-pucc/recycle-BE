from django.contrib import admin
from .models import Movimentacoes


class MovimentacoesAdmin(admin.ModelAdmin):
    list_display = ('id','data', 'entrada_saida', 'tipo', 'numero_tipo', 'cod_produto', 'qtd_movimentada', 'saldo_atual')
    list_display_links = ('id','data', 'entrada_saida', 'tipo', 'numero_tipo', 'cod_produto', 'qtd_movimentada', 'saldo_atual')
    list_filter = ('id','data', 'entrada_saida', 'tipo', 'numero_tipo', 'cod_produto', 'qtd_movimentada', 'saldo_atual')
    list_per_page = 10
    search_fields = ('id','data', 'entrada_saida', 'tipo', 'numero_tipo', 'cod_produto', 'qtd_movimentada', 'saldo_atual')


admin.site.register(Movimentacoes, MovimentacoesAdmin)