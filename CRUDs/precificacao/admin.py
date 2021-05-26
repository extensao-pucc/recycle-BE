from django.contrib import admin
from .models import Precificacao

class PrecificacaoAdmin(admin.ModelAdmin):
    list_display = ('produto',)
    list_display_links = ('produto',)
    list_filter = ('produto',)
    list_per_page = 10
    search_fields = ('produto',)


admin.site.register(Precificacao, PrecificacaoAdmin)