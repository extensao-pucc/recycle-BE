from django.contrib import admin
from .models import LoteParadas


class LoteParadasAdmin(admin.ModelAdmin):
    list_display = ('id','num_lote', 'motivo', 'sequencia', 'iniciado', 'finalizado', 'tempo_total')
    list_display_links = ('id','num_lote', 'motivo', 'sequencia', 'iniciado', 'finalizado', 'tempo_total')
    list_filter = ('id','num_lote', 'motivo', 'sequencia', 'iniciado', 'finalizado', 'tempo_total')
    list_per_page = 10
    search_fields = ('id','num_lote', 'motivo', 'sequencia', 'iniciado', 'finalizado', 'tempo_total')


admin.site.register(LoteParadas, LoteParadasAdmin)