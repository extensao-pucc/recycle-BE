from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from financeiro.contas.models import Contas
from mysql.connector import Error
from django.db import transaction
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
                    print('to aqui')
                    query = ("SELECT * FROM lote_lote WHERE num_lote in (select numero_tipo from recycledb.movimentacoes_movimentacoes where tipo=" + str(request.data['producao']) +") AND DATE_FORMAT(iniciado, '%Y-%m-%d') BETWEEN " + str(request.data['inicio']) +" and " + str(request.data['fim']) + "")
                    data = (request.data['producao'],
                            request.data['inicio'],
                            request.data['fim']        
                    )
                else:
                    query = ("SELECT * FROM lote_lote WHERE `num_lote` in (select `numero_tipo` from movimentacoes_movimentacoes where `tipo`=" + str(request.data['producao']) + ")") 
                    
                cursor.execute(query,data)

                for rows in records:
                    json_data.append(dict(zip(row_headers,rows)))
                
                return Response(json_data)

        except mysql.connector.Error as err:
            connection.close()
            return Response(f"Error: {err}", status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['GET'])
    def baglist (self, request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')

            if connection.is_connected():
                cursor = connection.cursor()

                query = ("SELECT `vendas_vendas`.`id`,                                                                                                                                                         "+
                        "`vendas_vendas`.`data`,                                                                                                                                                               "+
                        "`clientes_clientes`.`razao_social_nome` as `cliente`,                                                                                                                                 "+
                        "`condicoesdepagamento_condicoesdepagamento`.`descricao` as `forma_de_pagamento`,                                                                                                      "+
                        "`socios_socios`.`nome` as `vendedor`,                                                                                                                                                 "+
                        "`vendasitens_vendasitens`.`venda_id`,                                                                                                                                                 "+
                        "`vendas_vendas`.`valor`,                                                                                                                                                              "+
                        "`precificacao_precificacao`.`id` as `itens`,                                                                                                                                          "+
                        "`precificacao_precificacao`.`quantidade` as `quantidade_estoque`,                                                                                                                                             "+
                        "`precificacao_precificacao`.`preco_compra`,                                                                                                                                           "+
                        "`precificacao_precificacao`.`preco_venda`,                                                                                                                                            "+
                        "`fornecedores_fornecedores`.`razao_social_nome` as `fornecedor`,                                                                                                                      "+
                        "`produtos_produtos`.`descricao` as `produto`,                                                                                                                                         "+
                        "`qualidades_qualidades`.`nome` as `qualidade`,                                                                                                                                        "+
                        "`vendasitens_vendasitens`.`quantidade` as `quantidade_da_venda`                                                                                                                                                "+
                        "FROM `vendas_vendas` JOIN `vendasitens_vendasitens` on vendas_vendas.id = vendasitens_vendasitens.venda_id                                                                            "+
                        "                        JOIN `precificacao_precificacao` on vendasitens_vendasitens.precificacao_id = precificacao_precificacao.id                                                    "+
                        "                            JOIN `clientes_clientes` on vendas_vendas.cliente_id = clientes_clientes.id                                                                               "+
                        "                                JOIN `socios_socios` on vendas_vendas.vendedor_id = socios_socios.id                                                                                  "+
                        "                                    JOIN `produtos_produtos` on precificacao_precificacao.produto_id = produtos_produtos.id                                                           "+
                        "                                        JOIN `condicoesdepagamento_condicoesdepagamento` on vendas_vendas.forma_de_pagamento_id = condicoesdepagamento_condicoesdepagamento.id        "+
                        "                                            JOIN `fornecedores_fornecedores` on precificacao_precificacao.fornecedor_id = fornecedores_fornecedores.id                                "+
                        "                                                JOIN `qualidades_qualidades` on precificacao_precificacao.qualidade_id = qualidades_qualidades.id order by `vendas_vendas`.`id`;")

                cursor.execute(query)
                row_headers=[x[0] for x in cursor.description]
                records = cursor.fetchall()

                json_data=[]
                x = ""
                itens = []
                i = 0
                print(len(records))
                while i < len(records):
                # for i in range (0, len(records)):
                    if x == records[i][0] or x == "":
                        print(f"if - {records[i][0]}")
                        x = records[i][0]
                        itens.append({
                            "id":records[i][7],
                            "quantidade_estoque":records[i][8],
                            "preco_compra":records[i][9],
                            "preco_venda":records[i][10],
                            "fornecedor":records[i][11],
                            "produto":records[i][12],
                            "qualidade":records[i][13],
                            "quantidade_da_venda":records[i][14],
                        })
                        i = i + 1
                    else:
                        print(f"else - {records[i][0]}")
                        json_data.append(dict(zip(row_headers,(records[i-1][0],records[i-1][1],records[i-1][2],records[i-1][3],records[i-1][4],records[i-1][5],records[i-1][6],itens))))
                        x = ""
                        itens = []
                if itens:
                    json_data.append(dict(zip(row_headers,(records[i-1][0],records[i-1][1],records[i-1][2],records[i-1][3],records[i-1][4],records[i-1][5],records[i-1][6],itens))))                 
                return Response(json_data)
        except mysql.connector.Error as err:
            connection.close()
            return Response(f"Error: {err}", status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def saveBaglist (self, request):
        try:
            connection = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='recycledb',port='3306')
            cursor = connection.cursor()
            
            with transaction.atomic():
                query = ("INSERT INTO `recycledb`.`vendas_vendas` (`data`,`cliente_id`,`forma_de_pagamento_id`,`vendedor_id`,`valor`) VALUES (%s,%s,%s,%s,%s);")
                data = (request.data['data'],
                        request.data['cliente'],
                        request.data['forma_de_pagamento'],
                        request.data['vendedor'],
                        request.data['valor'],
                )   
                cursor.execute(query,data)

                query = ("SELECT `vendas_vendas`.`id` FROM `vendas_vendas` ORDER BY `vendas_vendas`.`id` DESC LIMIT 1") 
                cursor.execute(query)
                records = cursor.fetchall()
                id_venda = records[0][0]

                for i, item in enumerate(request.data['itens']):
                    query = ("INSERT INTO `recycledb`.`vendasitens_vendasitens` (`precificacao_id`, `venda_id`, `quantidade`) VALUES (%s,%s,%s);")
                    data = (request.data['itens'][i]['id'], id_venda, request.data['itens'][i]['quantidade_da_venda'])    
                    cursor.execute(query,data) 


                connection.commit()
            connection.close()
            return Response("Everything os OK", status=200)
        except mysql.connector.Error as err:
            connection.close()
            return Response(f"Error: {err}", status=status.HTTP_400_BAD_REQUEST)