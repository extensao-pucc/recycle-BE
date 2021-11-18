from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from CRUDs.clientes.views import ClientesViewSet
from CRUDs.condicoesDePagamento.views import CondicoesDePagamentoViewSet
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
from CRUDs.precificacao.views import PrecificacaoViewSet
from CRUDs.prensas.views import PrensasViewSet
from CRUDs.produtos.views import ProdutosViewSet
from CRUDs.qualidades.views import QualidadesViewSet
from CRUDs.socios.views import SociosViewSet
from CRUDs.transportadoras.views import TransportadorasViewSet

from financeiro.vendas.views import VendasViewSet
from financeiro.vendasItens.views import VendasItensViewSet
from financeiro.contas.views import ContasViewSet
from utils.authentication import SigninViewSet
from utils.authentication import ForgetPasswordViewSet
from utils.authentication import JoinPrecificacao
from utils.storedProcedures import saveProduction
from utils.payday import toPay

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'clientes', ClientesViewSet)
router.register(r'condicoesDePagamento', CondicoesDePagamentoViewSet)
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
router.register(r'precificacao', PrecificacaoViewSet)
router.register(r'prensas', PrensasViewSet)
router.register(r'produtos', ProdutosViewSet)
router.register(r'qualidades', QualidadesViewSet)
router.register(r'socios', SociosViewSet)
router.register(r'transportadoras', TransportadorasViewSet)
router.register(r'vendas', VendasViewSet)
router.register(r'vendasItens', VendasItensViewSet)

 
router.register(r'contas', ContasViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', SigninViewSet.as_view({'post':'signin'})),
    path('login/forget/', ForgetPasswordViewSet.as_view({'post':'forget'})),
    path('fornproddetails/', JoinPrecificacao.as_view({'post':'join'})),
    path('procedure/', saveProduction.as_view({'post':'saveLote'})),
    path('saveRemanufatura/', saveProduction.as_view({'post':'saveRemanufatura'})),
    path('dateToPay/', toPay.as_view({'post':'payDate'})),
    path('movimentDate/', toPay.as_view({'post':'movimentDate'})),
    path('productionHistory/', toPay.as_view({'post':'productionHistory'})),
    path('valueToPay/', toPay.as_view({'post':'payValue'})),
    path('payTotalValueMonthly/', toPay.as_view({'get':'payTotalValueMonthly'})),
    path('receiveTotalValueMonthly/', toPay.as_view({'get':'receiveTotalValueMonthly'})),
    path('baglist/', toPay.as_view({'get':'baglist'})),
    path('saveBaglist/', toPay.as_view({'post':'saveBaglist'}))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
