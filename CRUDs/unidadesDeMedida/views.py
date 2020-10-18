from django.shortcuts import render
from rest_framework import viewsets
from .models import UnidadesDeMedida
from .serializers import UnidadesDeMedidaSerializer


class UnidadesDeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadesDeMedida.objects.all()
    serializer_class = UnidadesDeMedidaSerializer