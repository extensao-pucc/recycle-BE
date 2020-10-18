from django.shortcuts import render
from rest_framework import viewsets
from .models import Produtos
from .serializers import ProdutosSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer