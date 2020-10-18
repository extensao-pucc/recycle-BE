from django.shortcuts import render
from rest_framework import viewsets
from .models import Parametros
from .serializers import ParametrosSerializer


class ParametrosViewSet(viewsets.ModelViewSet):
    queryset = Parametros.objects.all()
    serializer_class = ParametrosSerializer