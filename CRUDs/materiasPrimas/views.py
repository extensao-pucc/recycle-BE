from django.shortcuts import render
from rest_framework import viewsets
from .models import MateriasPrimas
from .serializers import MateriasPrimasSerializer


class MateriasPrimasViewSet(viewsets.ModelViewSet):
    queryset = MateriasPrimas.objects.all()
    serializer_class = MateriasPrimasSerializer