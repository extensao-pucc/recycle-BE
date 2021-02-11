from django.shortcuts import render
from rest_framework import viewsets
from .models import Movimentacoes
from .serializers import MovimentacoesSerializer


class MovimentacoesViewSet(viewsets.ModelViewSet):
    queryset = Movimentacoes.objects.all()
    serializer_class = MovimentacoesSerializer