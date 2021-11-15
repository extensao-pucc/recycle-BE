from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from financeiro.contas.models import Contas
from mysql.connector import Error
import mysql.connector

from datetime import datetime

class toPay(viewsets.ViewSet):

    @action(detail=True, methods=['POST'])
    def payDate (self, request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')

            if connection.is_connected():
                cursor = connection.cursor()
                query = ("SELECT * FROM contas_contas WHERE data BETWEEN %s and %s") 
                data = (request.data['data_inicial'],
                        request.data['data_final']        
                )
                cursor.execute(query,data)

                row_headers=[x[0] for x in cursor.description]
                records = cursor.fetchall()

                json_data=[]

                for rows in records:
                    json_data.append(dict(zip(row_headers,rows)))
                
                return Response(json_data)

        except mysql.connector.Error as err:
            connection.close()
            return Response(f"Error: {err}", status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def payValue (self, request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')

            if connection.is_connected():
                cursor = connection.cursor()
                query = ("SELECT * FROM contas_contas WHERE valor BETWEEN %s and %s") 
                data = (request.data['valor_inicial'],
                        request.data['valor_final']        
                )
                cursor.execute(query,data)

                row_headers=[x[0] for x in cursor.description]
                records = cursor.fetchall()

                json_data=[]

                for rows in records:
                    json_data.append(dict(zip(row_headers,rows)))
                
                return Response(json_data)

        except mysql.connector.Error as err:
            connection.close()
            return Response(f"Error: {err}", status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def payTotalValueMonthly (self, request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')

            intervalo = 12 - (12 - int(datetime.today().strftime('%m'))) - 1

            if connection.is_connected():
                cursor = connection.cursor()
                query = (
                        "SELECT                                                                     "+
                        "    MONTH(data) as mes,                                                    "+
                        "    YEAR(data) as ano,                                                     "+
                        "    sum(valor) as soma                                                     "+
                        "FROM                                                                       "+
                        "    contas_contas,                                                         "+
                        "    ( select @lastYear := date_add( DATE_FORMAT(NOW(),                     "+
                        "        '%Y-%m-01'), interval -"+str(intervalo)+" month) ) sqlvar          "+
                        "WHERE                                                                      "+
                        "    data >= @lastYear and tipo = 'A pagar' and situacao != 'Cancelado'     "+
                        "group by                                                                   "+
                        "    MONTH(data),                                                           "+
                        "    YEAR(data)                                                             "+
                        "order by                                                                   "+
                        "    YEAR(data) ASC,                                                        "+
                        "    MONTH(data) ASC                                                        "
                )

                cursor.execute(query)

                row_headers=[x[0] for x in cursor.description]
                records = cursor.fetchall()
                
                json_data=[]
                
                mes = 1
                i = 0
                while mes <= 12:
                    if i < len(records):
                        if records[i][0] != mes:
                            json_data.append(dict(zip(row_headers,(mes,int(datetime.today().strftime('%Y')), 0))))
                        else:
                            json_data.append(dict(zip(row_headers,records[i])))
                            i = i + 1
                    else:
                        json_data.append(dict(zip(row_headers,(mes,int(datetime.today().strftime('%Y')), 0))))
                    mes = mes + 1

                return Response(json_data)

        except mysql.connector.Error as err:
            connection.close()
            return Response(f"Error: {err}", status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def receiveTotalValueMonthly (self, request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')

            intervalo = 12 - (12 - int(datetime.today().strftime('%m'))) - 1

            if connection.is_connected():
                cursor = connection.cursor()
                query = (
                        "SELECT                                                                     "+
                        "    MONTH(data) as mes,                                                    "+
                        "    YEAR(data) as ano,                                                     "+
                        "    sum(valor) as soma                                                     "+
                        "FROM                                                                       "+
                        "    contas_contas,                                                         "+
                        "    ( select @lastYear := date_add( DATE_FORMAT(NOW(),                     "+
                        "        '%Y-%m-01'), interval -"+str(intervalo)+" month) ) sqlvar          "+
                        "WHERE                                                                      "+
                        "    data >= @lastYear and tipo = 'A receber' and situacao != 'Cancelado'   "+
                        "group by                                                                   "+
                        "    MONTH(data),                                                           "+
                        "    YEAR(data)                                                             "+
                        "order by                                                                   "+
                        "    YEAR(data) ASC,                                                        "+
                        "    MONTH(data) ASC                                                        "
                )

                cursor.execute(query)

                row_headers=[x[0] for x in cursor.description]
                records = cursor.fetchall()
                
                json_data=[]
                
                mes = 1
                i = 0
                while mes <= 12:
                    if i < len(records):
                        if records[i][0] != mes:
                            json_data.append(dict(zip(row_headers,(mes,int(datetime.today().strftime('%Y')), 0))))
                        else:
                            json_data.append(dict(zip(row_headers,records[i])))
                            i = i + 1
                    else:
                        json_data.append(dict(zip(row_headers,(mes,int(datetime.today().strftime('%Y')), 0))))
                    mes = mes + 1

                return Response(json_data)

        except mysql.connector.Error as err:
            connection.close()
            return Response(f"Error: {err}", status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['POST'])
    def movimentDate (self, request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')

            if connection.is_connected():
                cursor = connection.cursor()
                if request.data['inicio'] != '' and request.data['fim'] != '': 
                    query = ("SELECT * FROM movimentacoes_movimentacoes WHERE cod_produto_id= (select id from precificacao_precificacao where id= %s) AND DATE_FORMAT(data, '%Y-%m-%d') BETWEEN %s and %s") 
                    data = (request.data['product']['id'],
                            request.data['inicio'],
                            request.data['fim']        
                    )
                else:
                    query = ("SELECT * FROM movimentacoes_movimentacoes WHERE `cod_produto_id`=" + str(request.data['product']['id'])) 
                    data = (request.data['product']['id'])
                    
                cursor.execute(query,data)

                row_headers=[x[0] for x in cursor.description]
                records = cursor.fetchall()

                json_data=[]

                for rows in records:
                    json_data.append(dict(zip(row_headers,rows)))
                
                return Response(json_data)

        except mysql.connector.Error as err:
            connection.close()
            return Response(f"Error: {err}", status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['POST'])
    def productionHistory (self, request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')

            if connection.is_connected():
                cursor = connection.cursor()
                if request.data['inicio'] != '' and request.data['fim'] != '': 
                    query = ("SELECT * FROM lote_lote WHERE num_lote in (select numero_tipo from recycledb.movimentacoes_movimentacoes where tipo= %s) AND DATE_FORMAT(data, '%Y-%m-%d') BETWEEN %s and %s") 
                    data = (request.data['type'],
                            request.data['inicio'],
                            request.data['fim']        
                    )
                else:
                    query = ("SELECT * FROM lote_lote WHERE num_lote in (select numero_tipo from recycledb.movimentacoes_movimentacoes where tipo= %s)") 
                    data = (request.data['type'])
                    
                cursor.execute(query,data)

                row_headers=[x[0] for x in cursor.description]
                records = cursor.fetchall()

                json_data=[]

                for rows in records:
                    json_data.append(dict(zip(row_headers,rows)))
                
                return Response(json_data)

        except mysql.connector.Error as err:
            connection.close()
            return Response(f"Error: {err}", status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['POST'])
    def baglist (self, request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')

            if connection.is_connected():
                cursor = connection.cursor()

                query = ("SELECT `vendas_vendas`.`id`,                                                                                                      "+
                        "`vendas_vendas`.`data`,                                                                                                            "+
                        "`vendas_vendas`.`cliente_id`,                                                                                                      "+
                        "`vendas_vendas`.`forma_de_pagamento_id`,                                                                                           "+
                        "`vendas_vendas`.`vendedor_id`,                                                                                                     "+
                        "`vendasitens_vendasitens`.`venda_id`,                                                                                              "+
                        "`vendasitens_vendasitens`.`precificacao_id`,                                                                                       "+
                        "`precificacao_precificacao`.`id`,                                                                                                  "+
                        "`precificacao_precificacao`.`quantidade`,                                                                                          "+
                        "`precificacao_precificacao`.`preco_compra`,                                                                                        "+
                        "`precificacao_precificacao`.`preco_venda`,                                                                                         "+
                        "`precificacao_precificacao`.`fornecedor_id`,                                                                                       "+
                        "`precificacao_precificacao`.`produto_id`,                                                                                          "+
                        "`precificacao_precificacao`.`qualidade_id`                                                                                         "+
                        "FROM `vendas_vendas` JOIN `vendasitens_vendasitens` on vendas_vendas.id = vendasitens_vendasitens.venda_id                         "+
                        "                    JOIN `precificacao_precificacao` on vendasitens_vendasitens.precificacao_id = precificacao_precificacao.id     "+
                        "                        order by vendas_vendas.id;                                                                                 ")

                cursor.execute(query)
                row_headers=[x[0] for x in cursor.description]
                records = cursor.fetchall()

                json_data=[]
                x = ""
                itens = []
                
                for i in range (0, len(records)):
                    if x == records[i][0] or x == "":
                        x = records[i][0]
                        itens.append({
                            "id":records[i][6],
                            "quantidade":records[i][7],
                            "preco_compra":records[i][8],
                            "preco_venda":records[i][9],
                            "fornecedor_id":records[i][10],
                            "produto_id":records[i][11],
                            "qualidade_id":records[i][12],
                        })
                        i = i + 1
                    else:
                        json_data.append(dict(zip(row_headers,(records[i-1][0],records[i-1][1],records[i-1][2],records[i-1][3],records[i-1][4],records[i-1][5],itens))))
                        json_data.append(dict(zip(row_headers,(records[i][0],records[i][1],records[i][2],records[i][3],records[i][4],records[i][5],records[i][6],records[i][7],records[i][8],records[i][9],records[i][10],records[i][11],records[i][12]))))
                        x = ""
                        itens = []
                        
                return Response(json_data)

        except mysql.connector.Error as err:
            connection.close()
            return Response(f"Error: {err}", status=status.HTTP_400_BAD_REQUEST)