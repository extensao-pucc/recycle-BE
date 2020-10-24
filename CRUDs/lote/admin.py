from django.contrib import admin
from .models import Lote


class LoteAdmin(admin.ModelAdmin):
    list_display = ('id','num_lote', 'iniciado', 'finalizado', 'socio', 'fornecedor', 'observacao')
    list_display_links = ('id','num_lote', 'iniciado', 'finalizado', 'socio', 'fornecedor', 'observacao')
    list_filter = ('id','num_lote', 'iniciado', 'finalizado', 'socio', 'fornecedor', 'observacao')
    list_per_page = 10
    search_fields = ('id','num_lote', 'iniciado', 'finalizado', 'socio', 'fornecedor', 'observacao')


admin.site.register(Lote, LoteAdmin)