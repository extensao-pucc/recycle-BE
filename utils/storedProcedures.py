from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from CRUDs.familias.models import Familias
from django.db import transaction
import mysql.connector
from mysql.connector import Error


from CRUDs.lote.serializers import LoteSerializer
from CRUDs.familias.serializers import FamiliasSerializer
from CRUDs.loteParadas.serializers import LoteParadasSerializer

import sys
import json

from django.http import JsonResponse

class save(viewsets.ViewSet):

    @action(detail=True, methods=['POST'])
    def saveLote(self,request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')
            cursor = connection.cursor()
            
            with transaction.atomic():               
                # --------------------    Insert na tabela de lote
                query = ("INSERT INTO lote_lote VALUES (%s,%s, %s,%s,%s, %s,%s);")
                data = (request.data['lote']['num_lote'],
                        request.data['lote']['finalizado'],
                        request.data['lote']['iniciado'],
                        request.data['lote']['observacao'],
                        request.data['lote']['tempo_total'],
                        request.data['lote']['fornecedor'],
                        request.data['lote']['socio']
                    )
                cursor.execute(query,data)
                
            # --------------------    Insert na tabela de PARADAS de um lote
                for i, item in enumerate(request.data['lote_paradas']):
                    query = ("INSERT INTO loteparadas_loteparadas VALUES (%s,%s, %s,%s, %s, %s,%s);")
                    data = (request.data['lote_parada'][i]['id'],
                            request.data['lote_parada'][i]['finalizado'],
                            request.data['lote_parada'][i]['iniciado'],
                            request.data['lote_parada'][i]['sequencia'],
                            request.data['lote_parada'][i]['tempo_total'],
                            request.data['lote_parada'][i]['motivo'],
                            request.data['lote_parada'][i]['num_lote']
                        )   
                    cursor.execute(query,data)
            
            # --------------------    Insert na tabela de ITENS pertencente ao lote              
                for i, item in enumerate(request.data['lote_itens']):
                    query = ("INSERT INTO loteitens_loteitens VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);")                   
                    data = (request.data['lote_itens'][i]['id'],
                            request.data['lote_itens'][i]['finalizado'],
                            request.data['lote_itens'][i]['iniciado'],
                            request.data['lote_itens'][i]['num_recipiente'],
                            request.data['lote_itens'][i]['quantidade'],
                            request.data['lote_itens'][i]['tempo_total'],
                            request.data['lote_itens'][i]['num_lote'],
                            request.data['lote_itens'][i]['produto'],
                            request.data['lote_itens'][i]['socio']
                        )         
                    cursor.execute(query,data)

            # --------------------    Insert na tebela de Movimentações
                for i, item in enumerate(request.data['movimentacoes']):
                    query = ("INSERT INTO loteitens_loteitens VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);")                   
                    data = (request.data['movimentacoes'][i]['id'],
                            request.data['movimentacoes'][i]['data'],
                            request.data['movimentacoes'][i]['entrada_saida'],
                            request.data['movimentacoes'][i]['tipo'],
                            request.data['movimentacoes'][i]['numero_tipo'],
                            request.data['movimentacoes'][i]['saldo_anterior'],
                            request.data['movimentacoes'][i]['saldo_atual'],
                            request.data['movimentacoes'][i]['dif'],
                            request.data['movimentacoes'][i]['cod_produto']
                        )          
                    cursor.execute(query,data)
            # --------------------  Fim dos inserts

                connection.commit()
            connection.close()
            return Response("Everything os OK", status=200)
        except Exception as err:
            return Response("Everything sucks", status=404)
            connection.close()
            raise