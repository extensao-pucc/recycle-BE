from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from CRUDs.familias.models import Familias
import mysql.connector
from mysql.connector import Error
from django.db import transaction
from rest_framework.parsers import JSONParser,ParseError
from CRUDs.lote.serializers import LoteSerializer
import json

class save(viewsets.ViewSet):

#     @action(detail=True, methods=['get'])
#     def sProcedure(self,request):

#         try:
#             connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')
            
#             array = ['g', 'u', 's']
#             num = 1048
#             # , '4', '5 ','6', '7', '8', '9']
#             x = 20

#             cursor = connection.cursor()
            
#             # familia = Familias(id='28', nome='rafa')
#             # familia.save()
#             # cursor = connection.cursor()
#             # query = ("INSERT INTO familias_familias VALUES (%s, %s);")   
#             # data = ('33', 'Vanderkelen')
#             with transaction.atomic():    
#                 for kd in array:
#                     if kd == 'f':
#                         query = ("INSERT INTO prensas VALUES ('', %(descricao)s, %(detalhes_tecnicos)s, %(numero)i);")
#                         data = {
#                             'descricao':kd,
#                             'detalhes_tecnicos':'foi',
#                             'numero':num,
#                         } 
#                         cursor.execute(query,data)
#                         x = x + 1

#                         query = ("INSERT INTO condicoesdepagamento_condicoesdepagamento VALUES ('', %(descricao)s);")
#                         data = {
#                             'descricao':kd,
#                         } 
#                         cursor.execute(query,data)
                        
#                     else:
#                         query = ("INSERT INTO prensas_prensas VALUES ('', %(descricao)s, %(detalhes_tecnicos)s, %(numero)s);")
#                         data = {
#                             'descricao':kd,
#                             'detalhes_tecnicos':'foi',
#                             'numero':num,
#                         } 
                        
#                         cursor.execute(query,data)
#                         x = x + 1

#                         query = ("INSERT INTO familias_familias VALUES ('', %(nome)s);")
#                         data = {
#                             'nome':kd,
#                         } 
#                         cursor.execute(query,data)


#                 connection.commit()

#         except Error as e:
#             print("Error while connecting to MySQL", e)
#             transaction.rollback()



    @action(detail=True, methods=['POST'])
    def saveLote(self,request):
        
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')
            cursor = connection.cursor()

            lote = LoteSerializer(data=request.data)

            if lote.is_valid():
                
                with transaction.atomic():
                    
                    query = ("INSERT INTO `recycledb`.`lote_lote`(`num_lote`,`iniciado`,`finalizado`,`tempo_total`,`socio_id`,`fornecedor_id`, 'observacao' ) VALUES (%(num_lote)s,%(iniciado)s,%(finalizado)s,%(tempo_total)s,%(socio)s,%(fornecedor)s,%(observacao)s);")
                    
                    # query = (f"INSERT INTO `recycledb`.`lote_lote`(`num_lote`,`finalizado`,`iniciado`,`observacao`,`tempo_total`,`fornecedor_id`,`socio_id`) VALUES ({lote.data['num_lote']},{lote.data['finalizado']},{lote.data['iniciado']},{lote.data['observacao']},{lote.data['tempo_total']},{lote.data['fornecedor']},{lote.data['socio']});")

                    data = {
                        "num_lote":     lote.data['num_lote'],
                        "iniciado":     lote.data['iniciado'],
                        "finalizado":   lote.data['finalizado'],
                        "tempo_total":  lote.data['tempo_total'],
                        "socio":        lote.data['socio'],
                        "fornecedor":   lote.data['fornecedor'],
                        "observacao":   lote.data['observacao'],
                    } 

                    cursor.execute(query,data)

                    # query = ("INSERT INTO `recycledb`.`loteparadas_loteparadas` (`id`,`finalizado`,`iniciado`,`sequencia`,`tempo_total`,`motivo_id`,`num_lote_id`) VALUES (%(id)s,%(finalizado)s,%(iniciado)s, %(sequencia)s,%(tempo_total)s,%(motivo)s,%(num_lote)s);")
                    # data = {
                    #     "id": request.data['id'],
                    #     "finalizado": request.data['finalizado'],
                    #     "iniciado": request.data['iniciado'],
                    #     "sequencia": request.data['sequencia'],
                    #     "tempo_total": request.data['tempo_total'],
                    #     "motivo": request.data['motivo'],
                    #     "num_lote": request.data['finalizado'],
                    # } 
                    # cursor.execute(query,data)

                    # query = ("INSERT INTO `recycledb`.`loteitens_loteitens` (`id`,`finalizado`,`iniciado`,`num_recipiente`,`quantidade`,`tempo_total`,`num_lote_id`,`produto_id`,`socio_id`) VALUES (%(id)s,%(finalizado)s, %(iniciado)s, %(num_recipiente)s, %(quantidade)s, %(tempo_total)s, %(num_lote)s, %(produto)s, %(socio)s);")
                    # data = {
                    #     "id": request.data['id'],
                    #     "finalizado": request.data['finalizado'],
                    #     "iniciado": request.data['iniciado'],
                    #     "num_recipiente": request.data['num_recipiente'],
                    #     "quantidade": request.data['quantidade'],
                    #     "tempo_total": request.data['tempo_total'],
                    #     "num_lote": request.data['num_lote'],
                    #     "produto": request.data['produto'],
                    #     "socio": request.data['socio'],
                    # } 
                    # cursor.execute(query,data)

                    # query = ("INSERT INTO `recycledb`.`movimentacoes_movimentacoes VALUES (%(id: }>,%(data)s,%(entrada_saida)s,%(tipo)s,%(numero_tipo)s,%(saldo_anterior)s,%(saldo_atual)s,%(dif)s,%(cod_produto_id)s);")
                    # data = {
                    #     "id": request.data['id'],
                    #     "data": request.data['data'],
                    #     "entrada_saida": request.data['entrada_saida'],
                    #     "tipo": request.data['tipo'],
                    #     "numero_tipo": request.data['numero_tipo'],
                    #     "cod_produto": request.data['cod_produto'],
                    #     "saldo_anterior": request.data['saldo_anterior'],
                    #     "saldo_atual": request.data['saldo_atual'],
                    #     "dif": request.data['dif']
                    # } 
                    
                    connection.commit()

        except Error as e:
            print("TA KINDO NESSE EXCEPT AKI -->", e)
            transaction.rollback()
