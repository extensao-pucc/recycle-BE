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
                print(request.data['data_final'])
                query = ("SELECT * FROM contas_contas WHERE DATE_FORMAT(data, '%d/%m/%Y') BETWEEN %s and %s") 
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