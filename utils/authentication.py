from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from CRUDs.socios.serializers import SociosSerializer
from CRUDs.socios.models import Socios
import mysql.connector
from mysql.connector import Error
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


class JoinPrecificacao(viewsets.ViewSet):
    @action(detail=True, methods=['get'])
    def join(self, request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

                query = ("SELECT * FROM socios_socios")

                cursor.execute(query)
                records = cursor.fetchall();
                

            return Response(records)

        except Error as e:
            print("Error while connecting to MySQL", e)

        
       
       