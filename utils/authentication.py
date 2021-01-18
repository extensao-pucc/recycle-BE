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
                'person': {
                    'matricula': person.data['matricula'], 
                    'nome': person.data['nome'],
                    'perfil': person.data['perfil'],
                    'foto': person.data['foto']},
                'mssg': 'Usuario encontrado',               
            })

        except Socios.DoesNotExist:
            return Response({
                'mssg': "Usuário ou senha incorretos",
            })
       

class ForgetPasswordViewSet(viewsets.ViewSet):

    @action(detail=True, methods=['post'])
    def forget(self, request):

        try:
            person = Socios.objects.get(matricula=request.data['matricula'])

            if person.senha != request.data['old_password']:
                return Response("Senha atual incorreta.")

            if person.senha == request.data['new_password']:
                return Response("Altere para uma senha diferente da atual")
            
            person.senha = request.data['new_password']
            person.save()

            return Response(status=200)

        except Socios.DoesNotExist:
            return Response("Usuário não existe")