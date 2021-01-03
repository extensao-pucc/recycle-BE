from django.contrib import admin
from .models import Estoque


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id','produto','fornecedor','qualidade','quantidade')
    list_display_links = ('id','produto','fornecedor','qualidade','quantidade')
    list_filter = ('id','produto','fornecedor','qualidade','quantidade')
    list_per_page = 10
    search_fields = ('id','produto','fornecedor','qualidade','quantidade')


admin.site.register(Estoque, EstoqueAdmin)