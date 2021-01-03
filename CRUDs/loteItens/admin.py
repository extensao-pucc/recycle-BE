from django.contrib import admin
from .models import LoteItens


class LoteItensAdmin(admin.ModelAdmin):
    list_display = ('id','num_lote', 'num_recipiente', 'produto', 'quantidade', 'socio', 'data_iniciado', 'data_finalizado', 'hora_iniciado', 'hora_finalizado', 'tempo_total',)
    list_display_links = ('id','num_lote', 'num_recipiente', 'produto', 'quantidade', 'socio', 'data_iniciado', 'data_finalizado', 'hora_iniciado', 'hora_finalizado', 'tempo_total',)
    list_filter = ('id','num_lote', 'num_recipiente', 'produto', 'quantidade', 'socio', 'data_iniciado', 'data_finalizado', 'hora_iniciado', 'hora_finalizado', 'tempo_total',)
    list_per_page = 10
    search_fields = ('id','num_lote', 'num_recipiente', 'produto', 'quantidade', 'socio', 'data_iniciado', 'data_finalizado', 'hora_iniciado', 'hora_finalizado', 'tempo_total',)


admin.site.register(LoteItens, LoteItensAdmin)