from django.shortcuts import render
from rest_framework import viewsets
from .models import CondicoesDePagamento
from .serializers import CondicoesDePagamentoSerializer


class CondicoesDePagamentoViewSet(viewsets.ModelViewSet):
    queryset = CondicoesDePagamento.objects.all()
    serializer_class = CondicoesDePagamentoSerializer