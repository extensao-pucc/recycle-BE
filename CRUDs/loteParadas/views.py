from django.shortcuts import render
from rest_framework import viewsets
from .models import LoteParadas
from .serializers import LoteParadasSerializer


class LoteParadasViewSet(viewsets.ModelViewSet):
    queryset = LoteParadas.objects.all()
    serializer_class = LoteParadasSerializer