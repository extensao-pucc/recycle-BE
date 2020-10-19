from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from CRUDs.condicoesDePagamento.views import CondicoesDePagamentoViewSet
from CRUDs.familias.views import FamiliasViewSet
from CRUDs.fornecedores.views import FornecedoresViewSet
from CRUDs.motivosDeParada.views import MotivosDeParadaViewSet
from CRUDs.naturezaDasOperacoes.views import NaturezaDasOperacoesViewSet
from CRUDs.parametros.views import ParametrosViewSet
from CRUDs.prensas.views import PrensasViewSet
from CRUDs.produtos.views import ProdutosViewSet
from CRUDs.qualidades.views import QualidadesViewSet
# from CRUDs.socios.views import SociosViewSet
from CRUDs.transportadoras.views import TransportadorasViewSet
from CRUDs.unidadesDeMedida.views import UnidadesDeMedidaViewSet

router = routers.DefaultRouter()
router.register(r'condicoesDePagamento', CondicoesDePagamentoViewSet)
router.register(r'familias', FamiliasViewSet)
router.register(r'fornecedores', FornecedoresViewSet)
router.register(r'motivosDeParada', MotivosDeParadaViewSet)
router.register(r'naturezaDasOperacoes', NaturezaDasOperacoesViewSet)
router.register(r'parametros', ParametrosViewSet)
router.register(r'prensas', PrensasViewSet)
router.register(r'produtos', ProdutosViewSet)
router.register(r'qualidades', QualidadesViewSet)
# router.register(r'socios', SociosViewSet)
router.register(r'transportadoras', TransportadorasViewSet)
router.register(r'unidadesDeMedida', UnidadesDeMedidaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
