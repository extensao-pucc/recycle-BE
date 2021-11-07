from django.shortcuts import render
from rest_framework import viewsets
from .models import Vendas
from .serializers import VendasSerializer


class VendasViewSet(viewsets.ModelViewSet):
    queryset = Vendas.objects.all()
    serializer_class = VendasSerializer