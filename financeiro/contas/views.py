from django.shortcuts import render
from rest_framework import viewsets
from .models import Contas
from .serializers import ContasSerializer


class ContasViewSet(viewsets.ModelViewSet):
    queryset = Contas.objects.all()
    serializer_class = ContasSerializer
