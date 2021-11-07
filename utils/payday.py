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