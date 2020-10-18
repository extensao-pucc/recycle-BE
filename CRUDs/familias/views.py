from django.shortcuts import render
from rest_framework import viewsets
from .models import Familias
from .serializers import FamiliasSerializer


class FamiliasViewSet(viewsets.ModelViewSet):
    queryset = Familias.objects.all()
    serializer_class = FamiliasSerializer