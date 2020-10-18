from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from CRUDs.condicoesDePagamento.views import CondicoesDePagamentoViewSet
from CRUDs.familias.views import FamiliasViewSet

router = routers.DefaultRouter()
router.register(r'condicoesDePagamento', CondicoesDePagamentoViewSet)
router.register(r'familias', FamiliasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
