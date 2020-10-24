from django.shortcuts import render
from rest_framework import viewsets
from .models import LoteItens
from .serializers import LoteItensSerializer


class LoteItensViewSet(viewsets.ModelViewSet):
    queryset = LoteItens.objects.all()
    serializer_class = LoteItensSerializer