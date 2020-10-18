from django.shortcuts import render
from rest_framework import viewsets
from .models import NaturezaDasOperacoes
from .serializers import NaturezaDasOperacoesSerializer


class NaturezaDasOperacoesViewSet(viewsets.ModelViewSet):
    queryset = NaturezaDasOperacoes.objects.all()
    serializer_class = NaturezaDasOperacoesSerializer