from django.contrib import admin
from .models import NaturezaDasOperacoes


class NaturezaDasOperacoesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'tipo')
    list_display_links = ('codigo', 'descricao', 'tipo')
    list_filter = ('codigo', 'descricao', 'tipo')
    list_per_page = 10
    search_fields = ('codigo', 'descricao', 'tipo')


admin.site.register(NaturezaDasOperacoes, NaturezaDasOperacoesAdmin)