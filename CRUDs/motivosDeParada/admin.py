from django.contrib import admin
from .models import MotivosDeParada


class MotivosDeParadaAdmin(admin.ModelAdmin):
    list_display = ('motivo',)
    list_display_links = ('motivo',)
    list_filter = ('motivo',)
    list_per_page = 10
    search_fields = ('motivo',)


admin.site.register(MotivosDeParada, MotivosDeParadaAdmin)