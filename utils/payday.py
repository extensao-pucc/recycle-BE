from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from financeiro.contas.models import Contas
from mysql.connector import Error
import mysql.connector

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
                        "        '%Y-%m-01'), interval -12 month) ) sqlvar                          "+
                        "WHERE                                                                      "+
                        "    data >= @lastYear and tipo = 'A pagar' and situacao != 'Cancelado'     "+
                        "group by                                                                   "+
                        "    MONTH(data)                                                            "+
                        "order by                                                                   "+
                        "    YEAR(data) ASC,                                                        "+
                        "    MONTH(data) ASC                                                        "
                )
                
                cursor.execute(query)

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
    def receiveTotalValueMonthly (self, request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')

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
                        "        '%Y-%m-01'), interval -12 month) ) sqlvar                          "+
                        "WHERE                                                                      "+
                        "    data >= @lastYear and tipo = 'A receber' and situacao != 'Cancelado'   "+
                        "group by                                                                   "+
                        "    MONTH(data)                                                            "+
                        "order by                                                                   "+
                        "    YEAR(data) ASC,                                                        "+
                        "    MONTH(data) ASC                                                        "
                )
                
                cursor.execute(query)

                row_headers=[x[0] for x in cursor.description]
                records = cursor.fetchall()

                json_data=[]

                for rows in records:
                    json_data.append(dict(zip(row_headers,rows)))
                
                return Response(json_data)

        except mysql.connector.Error as err:
            connection.close()
            return Response(f"Error: {err}", status=status.HTTP_400_BAD_REQUEST)
    