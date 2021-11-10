from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from CRUDs.socios.serializers import SociosSerializer
from CRUDs.socios.models import Socios, encryptPassword, generate_key
import mysql.connector
from mysql.connector import Error
import uuid
from cryptography.fernet import Fernet


def decryptPassword(password, key):
    keyencode = key.encode()
    fernet = Fernet(keyencode)
    decryptPassw = fernet.decrypt(password.encode())
    return decryptPassw.decode()

class SigninViewSet(viewsets.ViewSet):
    
    @action(detail=True, methods=['post'])
    def signin(self, request):
       
        try:
            person = Socios.objects.get(matricula=request.data['matricula'])
            person = SociosSerializer(person)
            decryptsenha = decryptPassword(person.data['senha'], person.data['key'])


            if(decryptsenha==request.data['senha']):
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
            
            decryptsenha = decryptPassword(person.senha, person.key)
            print(decryptsenha)
            if decryptsenha != request.data['old_password']:
                return Response("Senha atual incorreta.")

            if decryptsenha == request.data['new_password']:
                return Response("Altere para uma senha diferente da atual")
            
            
            new_key = generate_key()
            new_senha = encryptPassword(request.data['new_password'], new_key)
            person.senha = new_senha
            person.key = new_key
            person.my_save()            

        except Socios.DoesNotExist:
            return Response("Usuário não existe")
        except Exception as error:
            return Response(error)
        else:
            return Response("Senha atualizada com sucesso", status=200)

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
                print(request.data['fornecedor'])
                query = ("SELECT precificacao_precificacao.id as precificacao_id, produtos_produtos.id as prod_id, produtos_produtos.descricao as prod_desc, qualidades_qualidades.id as qual_id, qualidades_qualidades.nome as qual_nome FROM produtos_produtos join precificacao_precificacao on produtos_produtos.id = precificacao_precificacao.produto_id join fornecedores_fornecedores on precificacao_precificacao.fornecedor_id = fornecedores_fornecedores.id join qualidades_qualidades on qualidades_qualidades.id = precificacao_precificacao.qualidade_id where precificacao_precificacao.fornecedor_id ="+request.data['fornecedor']+";")

                cursor.execute(query)
                row_headers=[x[0] for x in cursor.description]
                records = cursor.fetchall()

                json_data=[]

                for rows in records:
                    json_data.append(dict(zip(row_headers,rows)))
                
            connection.close()
            return Response(json_data)
        
        except Error as e:
            print("Error while connecting to MySQL", e)

        
       
       