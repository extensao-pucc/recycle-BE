from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from CRUDs.socios.serializers import SociosSerializer
from CRUDs.socios.models import Socios

from rest_framework.parsers import JSONParser

class SigninViewSet(viewsets.ViewSet):
    
    @action(detail=True, methods=['post'])
    def signin(self, request):
       
        try:

            person = Socios.objects.get(matricula=request.data['matricula'], senha=request.data['senha'])
            person = SociosSerializer(person)
            return Response(person.data)

        except Socios.DoesNotExist:
            return Response("Usuário ou senha incorretos")
       
