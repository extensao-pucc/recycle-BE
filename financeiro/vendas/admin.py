from django.contrib import admin
from .models import Vendas


class VendasAdmin(admin.ModelAdmin):
    list_display = ('cliente','data', 'forma_de_pagamento', 'vendedor')
    list_display_links = ('cliente','data', 'forma_de_pagamento', 'vendedor')
    list_filter = ('cliente','data', 'forma_de_pagamento', 'vendedor')
    list_per_page = 10
    search_fields = ('cliente','data', 'forma_de_pagamento', 'vendedor')


admin.site.register(Vendas, VendasAdmin)