from django.shortcuts import render
from rest_framework import viewsets
from .models import MotivosDeParada
from .serializers import MotivosDeParadaSerializer


class MotivosDeParadaViewSet(viewsets.ModelViewSet):
    queryset = MotivosDeParada.objects.all()
    serializer_class = MotivosDeParadaSerializer