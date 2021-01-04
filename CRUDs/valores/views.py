from django.shortcuts import render
from rest_framework import viewsets
from .models import Valores
from .serializers import ValoresSerializer


class ValoresViewSet(viewsets.ModelViewSet):
    queryset = Valores.objects.all()
    serializer_class = ValoresSerializer
