from django.contrib import admin
from .models import Socios


class SociosAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'telefone', 'email')
    list_display_links = ('matricula', 'nome', 'telefone', 'email')
    list_filter = ('matricula', 'nome', 'telefone', 'email')
    list_per_page = 10
    search_fields = ('matricula', 'nome', 'telefone', 'email')


admin.site.register(Socios, SociosAdmin)