from django.contrib import admin
from .models import UnidadesDeMedida

class UnidadesDeMedidaAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'descricao')
    list_display_links = ('sigla', 'descricao')
    list_filter = ('sigla', 'descricao')
    list_per_page = 10
    search_fields = ('sigla', 'descricao')


admin.site.register(UnidadesDeMedida, UnidadesDeMedidaAdmin)