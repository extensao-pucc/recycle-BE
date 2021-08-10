from django.shortcuts import render
from rest_framework import viewsets
from .models import Prensas
from .serializers import PrensasSerializer


class PrensasViewSet(viewsets.ModelViewSet):
    queryset = Prensas.objects.all()
    serializer_class = PrensasSerializer


