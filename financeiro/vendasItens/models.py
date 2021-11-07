from django.shortcuts import render
from rest_framework import viewsets
from .models import VendasItens
from .serializers import VendasItensSerializer


class VendasItensViewSet(viewsets.ModelViewSet):
    queryset = VendasItens.objects.all()
    serializer_class = VendasItensSerializer