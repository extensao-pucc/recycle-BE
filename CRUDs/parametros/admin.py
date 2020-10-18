from django.contrib import admin
from .models import Parametros


class ParametrosAdmin(admin.ModelAdmin):
    list_display = ('triagem', 'prensa', 'remanufatura', 'numero_proxima_NFE', 'numero_proxima_NFS')
    list_display_links = ('triagem', 'prensa', 'remanufatura', 'numero_proxima_NFE', 'numero_proxima_NFS')
    list_filter = ('triagem', 'prensa', 'remanufatura', 'numero_proxima_NFE', 'numero_proxima_NFS')
    list_per_page = 10
    search_fields = ('triagem', 'prensa', 'remanufatura', 'numero_proxima_NFE', 'numero_proxima_NFS')


admin.site.register(Parametros, ParametrosAdmin)