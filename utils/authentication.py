from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from CRUDs.socios.serializers import SociosSerializer
from CRUDs.socios.models import Socios
import mysql.connector
from mysql.connector import Error
import uuid
import json

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
    @action(detail=True, methods=['post'])
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

                

                query = ("SELECT * FROM produtos_produtos join precificacao_precificacao on produtos_produtos.id = precificacao_precificacao.produto_id join fornecedores_fornecedores on precificacao_precificacao.fornecedor_id = fornecedores_fornecedores.id where precificacao_precificacao.fornecedor_id = "+request.data['fornecedor']+";")

                cursor.execute(query)
                row_headers=[x[0] for x in cursor.description]
                records = cursor.fetchall()

                json_data=[]

                for rows in records:
                    json_data.append(dict(zip(row_headers,rows)))
            
            
            return Response(json_data)

        except Error as e:
            print("Error while connecting to MySQL", e)

        
       
       