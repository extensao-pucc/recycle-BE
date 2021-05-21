from django.shortcuts import render
from rest_framework import viewsets
from .models import Precificacao
from .serializers import PrecificacaoSerializer


class PrecificacaoViewSet(viewsets.ModelViewSet):
    queryset = Precificacao.objects.all()
    serializer_class = PrecificacaoSerializer