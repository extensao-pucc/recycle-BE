from django.shortcuts import render
from rest_framework import viewsets
from CRUDs.socios.models import Socios
from CRUDs.socios.serializers import SociosSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, action


# class LoginViewSet(viewsets.ViewSet):
    
#    def list(self, request):
#         try:

#             queryset = Socios.objects.get(matricula=1, nome='Carlos Eduardo')
#             serializer = SociosSerializer(queryset)
#             return Response(serializer.data)

#         except Socios.DoesNotExist:
#             return Response("Usuário ou senha incorretos")
        
#         return Response(status = 404)


@action
def person(request):

    if request.method == 'POST':
        person = SociosSerializer(data=request.data)
        
        if person.is_valid():
            
            queryset = Socios.objects.get(matricula=person.user, senha=person.password)
            serializer = SociosSerializer(queryset)
            return Response(serializer.data)

        return Response("Usuário Invalido")


