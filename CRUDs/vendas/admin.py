from django.contrib import admin
from .models import Vendas


class VendasAdmin(admin.ModelAdmin):
    list_display = ('id','descricao')
    list_display_links = ('id','descricao')
    list_filter = ('id','descricao')
    list_per_page = 10
    search_fields = ('id','descricao')


admin.site.register(Vendas, VendasAdmin)