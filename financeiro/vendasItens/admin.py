from django.contrib import admin
from .models import VendasItens


class VendasItensAdmin(admin.ModelAdmin):
    list_display = ('venda','precificacao')
    list_display_links = ('venda','precificacao')
    list_filter = ('venda','precificacao')
    list_per_page = 10
    search_fields = ('venda','precificacao')


admin.site.register(VendasItens, VendasItensAdmin)