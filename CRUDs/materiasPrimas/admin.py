from django.contrib import admin
from .models import MateriasPrimas


class MateriasPrimasAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    list_filter = ('id','nome')
    list_per_page = 10
    search_fields = ('id','nome')


admin.site.register(MateriasPrimas, MateriasPrimasAdmin)