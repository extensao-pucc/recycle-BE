from django.shortcuts import render
from rest_framework import viewsets
from .models import Socios
from .serializers import SociosSerializer


class SociosViewSet(viewsets.ModelViewSet):
    queryset = Socios.objects.all()
    serializer_class = SociosSerializer