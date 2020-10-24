from django.shortcuts import render
from rest_framework import viewsets
from .models import Lote
from .serializers import LoteSerializer


class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer