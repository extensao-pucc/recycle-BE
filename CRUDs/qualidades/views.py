from django.shortcuts import render
from rest_framework import viewsets
from .models import Qualidades
from .serializers import QualidadesSerializer


class QualidadesViewSet(viewsets.ModelViewSet):
    queryset = Qualidades.objects.all()
    serializer_class = QualidadesSerializer