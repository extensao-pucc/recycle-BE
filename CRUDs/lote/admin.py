from django.contrib import admin
from .models import Lote


class LoteAdmin(admin.ModelAdmin):
    list_display = ('num_lote', 'iniciado', 'finalizado', 'tempo_total', 'socio', 'fornecedor', 'observacao')
    list_display_links = ('num_lote', 'iniciado', 'finalizado', 'tempo_total', 'socio', 'fornecedor', 'observacao')
    list_filter = ('num_lote', 'iniciado', 'finalizado', 'tempo_total', 'socio', 'fornecedor', 'observacao')
    list_per_page = 10
    search_fields = ('num_lote', 'iniciado', 'finalizado', 'tempo_total', 'socio', 'fornecedor', 'observacao')


admin.site.register(Lote, LoteAdmin)