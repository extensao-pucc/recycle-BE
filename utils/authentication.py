from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from CRUDs.socios.serializers import SociosSerializer
from CRUDs.socios.models import Socios
import uuid


class SigninViewSet(viewsets.ViewSet):
    
    @action(detail=True, methods=['post'])
    def signin(self, request):
       
        try:

            person = Socios.objects.get(matricula=request.data['matricula'], senha=request.data['senha'])
            person = SociosSerializer(person)
            return Response({
                'token': uuid.uuid4(),
                'person': person.data
                
            })

        except Socios.DoesNotExist:
            return Response("Usuário ou senha incorretos")
       
class ForgetPasswordViewSet(viewsets.ViewSet):

    @action(detail=True, methods=['post'])
    def forget(self, request):

        try:
            person = Socios.objects.get(matricula=request.data['matricula'])

            if person.senha != request.data['old_password']:
                return Response("Senha atual incorreta.")
            
            person.senha = SociosSerializer.
            return Response(person)


        except Socios.DoesNotExist:
            return Response("Usuário não existe")