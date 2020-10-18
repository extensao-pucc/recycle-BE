from django.shortcuts import render
from rest_framework import viewsets
from .models import Transportadoras
from .serializers import TransportadorasSerializer


class TransportadorasViewSet(viewsets.ModelViewSet):
    queryset = Transportadoras.objects.all()
    serializer_class = TransportadorasSerializer