from django.contrib import admin
from .models import Qualidades


class QualidadesAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = ('nome',)
    list_filter = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)


admin.site.register(Qualidades, QualidadesAdmin)