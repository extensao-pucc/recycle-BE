from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from CRUDs.condicoesDePagamento.views import CondicoesDePagamentoViewSet
from CRUDs.estoque.views import EstoqueViewSet
from CRUDs.familias.views import FamiliasViewSet
from CRUDs.fornecedores.views import FornecedoresViewSet
from CRUDs.lote.views import LoteViewSet
from CRUDs.loteItens.views import LoteItensViewSet
from CRUDs.loteParadas.views import LoteParadasViewSet
from CRUDs.materiasPrimas.views import MateriasPrimasViewSet
from CRUDs.motivosDeParada.views import MotivosDeParadaViewSet
from CRUDs.movimentacoes.views import MovimentacoesViewSet
from CRUDs.naturezaDasOperacoes.views import NaturezaDasOperacoesViewSet
from CRUDs.parametros.views import ParametrosViewSet
from CRUDs.prensas.views import PrensasViewSet
from CRUDs.produtos.views import ProdutosViewSet
from CRUDs.qualidades.views import QualidadesViewSet
from CRUDs.socios.views import SociosViewSet
from CRUDs.transportadoras.views import TransportadorasViewSet
from CRUDs.unidadesDeMedida.views import UnidadesDeMedidaViewSet
from utils.authentication import SigninViewSet
from utils.authentication import ForgetPasswordViewSet

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'condicoesDePagamento', CondicoesDePagamentoViewSet)
router.register(r'estoque', EstoqueViewSet)
router.register(r'familias', FamiliasViewSet)
router.register(r'fornecedores', FornecedoresViewSet)
router.register(r'lote', LoteViewSet)
router.register(r'loteItens', LoteItensViewSet)
router.register(r'loteParadas', LoteParadasViewSet)
router.register(r'materiasPrimas', MateriasPrimasViewSet)
router.register(r'motivosDeParada', MotivosDeParadaViewSet)
router.register(r'movimentacoes', MovimentacoesViewSet)
router.register(r'naturezaDasOperacoes', NaturezaDasOperacoesViewSet)
router.register(r'parametros', ParametrosViewSet)
router.register(r'prensas', PrensasViewSet)
router.register(r'produtos', ProdutosViewSet)
router.register(r'qualidades', QualidadesViewSet)
router.register(r'socios', SociosViewSet)
router.register(r'transportadoras', TransportadorasViewSet)
router.register(r'unidadesDeMedida', UnidadesDeMedidaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', SigninViewSet.as_view({'post':'signin'})),
    path('login/forget/', ForgetPasswordViewSet.as_view({'post':'forget'}))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
