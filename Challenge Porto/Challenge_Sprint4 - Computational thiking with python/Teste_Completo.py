import requests
from pprint import pprint

from flask import Flask, render_template, request, redirect, url_for, jsonify
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_21_12")

def getConnection():
    try:
        connection = cx_Oracle.connect("RM98624", "291002", "oracle.fiap.com.br/ORCL")
        # connection = cx_Oracle.connect(user="a", password="b", host="c", port="1521", service="ORCL") 
        print("conexão: ", connection.version)
        return connection
    except Exception as e:
        print(f'Erro ao obter conexão: {e}')

def CREATE_TABLE_CLIENTE():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_CLIENTE = """
    CREATE TABLE CLIENTE(
    ID_CLIENTE NUMERIC(38) NOT NULL,
    DT_NASCIMENTO DATE NOT NULL,
    E_MAIL VARCHAR(50) NOT NULL,
    NR_TELEFONE VARCHAR(11) NOT NULL,
    NM_NOME VARCHAR(60) NOT NULL,
    CEP INT NOT NULL,
    CPF VARCHAR(14) NOT NULL,
    CONSTRAINT PK_ID_CLIENTE PRIMARY KEY (ID_CLIENTE)
    )"""

    try:
        cursor.execute(sql_CLIENTE)
        print("Tabela CLIENTE criada")

    except Exception as e:
        print(f'Erro ao criar a tabela CLIENTE: {e}')
    
    finally:
        cursor.close
        conn.close

def login():
    print("Faça login completo para começar os serviços!")
    lista_de_dados_cliente = []
    ID_CLIENTE = int(input("id:"))
    lista_de_dados_cliente.append(ID_CLIENTE)

    DT_NASCIMENTO = input("Data de nascimento:")
    lista_de_dados_cliente.append(DT_NASCIMENTO)

    E_MAIL = input("e-mail:")
    lista_de_dados_cliente.append(E_MAIL)

    NR_TELEFONE = input("Telefone:")
    lista_de_dados_cliente.append(NR_TELEFONE)

    NM_NOME = input("Nome Completo:")
    lista_de_dados_cliente.append(NM_NOME)

    CEP = input("CEP:")
    lista_de_dados_cliente.append(CEP)

    CPF = input("CPF:")
    lista_de_dados_cliente.append(CPF)

    return lista_de_dados_cliente

def INSERIR_DADOS_CLIENTE(lista_de_dados_cliente):
  conn = getConnection()
  cursor = conn.cursor()
  sql_query = "INSERT INTO CLIENTE (ID_CLIENTE, DT_NASCIMENTO, E_MAIL, NR_TELEFONE, NM_NOME, CEP, CPF) VALUES (:0, TO_DATE (:1, 'dd/mm/yyyy'), :2, :3, :4, :5, :6)"
  try:
      cursor.execute(sql_query, (lista_de_dados_cliente[0], lista_de_dados_cliente[1], lista_de_dados_cliente[2], lista_de_dados_cliente[3], lista_de_dados_cliente[4], lista_de_dados_cliente[5], lista_de_dados_cliente[6]))
      conn.commit()
      print("Registro de cliente inserido com sucesso.")
  except Exception as e:
      print(f'Erro ao inserir o registro de cliente: {e}')
  finally:
      cursor.close()
      conn.close()

def DROP_TABLE_CLIENTE():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_enderecodrop = """
    DROP TABLE CLIENTE
    """
    try:
        cursor.execute(sql_enderecodrop)
        print("Tabela CLIENTE dropada")
    
    except Exception as e:
        print(f'Erro ao dropar a tabela CLIENTE: {e}')

    finally:
        cursor.close
        conn.close

def menu():
    selecao = int(input("""
*-- MENU --*

1 - realizar vistoria, em caso de primeiro seguro. 
2 - realizar vistoria, em caso de renovação de seguro;
3 - realizar vistoria, em caso de furto/roubo;
 

(Em caso de respostas de sim ou não, respoder 
com 'S' para sim e 'N' para não!)


Selecionar item de acordo com necessidade: """))
    while selecao not in [1, 2, 3, 4]:
      print("------------------------------------")
      print("Selecione apenas as opções de 1 a 3!")
      selecao = int(input("""
*-- MENU --*

1 - realizar vistoria, em caso de acidente;
2 - realizar vistoria, em caso de renovação de seguro;
3 - realizar vistoria, em caso de furto/roubo; 

Selecionar item de acordo com necessidade: """))
    return selecao

def selecao_menu_1_bicicleta_geral():
    print("Declare dados gerais da bicicleta.")

    lista_de_dados_bicicleta_geral = []

    ID_BICICLETA = input("ID da bicicleta:")
    lista_de_dados_bicicleta_geral.append(ID_BICICLETA)

    MODELO_DA_BICICLETA = input("Modelo da bicicleta:")
    lista_de_dados_bicicleta_geral.append(MODELO_DA_BICICLETA)

    NOTA_FISCAL = input("Nota Fiscal(preço):")
    lista_de_dados_bicicleta_geral.append(NOTA_FISCAL)
    return lista_de_dados_bicicleta_geral

def CREATE_TABLE_DADOS_BICICLETA():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_Bicicleta = """
    CREATE TABLE BICICLETA(
    ID_BICICLETA INT NOT NULL,
    MODELO_DA_BICICLETA VARCHAR(60),
    NOTA_FISCAL FLOAT,
    ID_CLIENTE INT,
    CONSTRAINT pk_id_bicicleta PRIMARY KEY (ID_BICICLETA),
    CONSTRAINT fk_BICICLETA_CLIENTE FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTE(ID_CLIENTE)
    )"""

    try:
        cursor.execute(sql_Bicicleta)
        print("Tabela BICICLETA criada")

    except Exception as e:
        print(f'Erro ao criar a tabela BICICLETA: {e}')
    
    finally:
        cursor.close
        conn.close

def INSERT_DADOS_BICICLETA(lista_de_dados_bicicleta_geral, lista_de_dados_cliente):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO BICICLETA (ID_BICICLETA, MODELO_DA_BICICLETA, NOTA_FISCAL, ID_CLIENTE) VALUES (:0, :1, :2, :3)"
    try:
        cursor.execute(sql_query, (lista_de_dados_bicicleta_geral[0], lista_de_dados_bicicleta_geral[1], lista_de_dados_bicicleta_geral[2], lista_de_dados_cliente[0]))
        conn.commit()
        print("Registro de cliente inserido com sucesso.")
    except Exception as e:
        print(f'Erro ao inserir o registro de cliente: {e}')
    finally:
        cursor.close()
        conn.close()

def DROP_TABLE_DADOS_BICICLETA():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_enderecodrop = """
    DROP TABLE BICICLETA
    """
    try:
        cursor.execute(sql_enderecodrop)
        print("Tabela BICICLETA dropada")
    
    except Exception as e:
        print(f'Erro ao dropar a tabela BICICLETA: {e}')

    finally:
        cursor.close
        conn.close

def selecao_menu_1_datalhes_bicicleta():
    print("---------------------------------------------------------------")

    quadro = ["Quadro", "Pedal", "Pedivela", "Caixa de direção", "Garfo"]
    guidao = ["Guidão", "Manoplas", "Manete de Freio", "Alavanca de Freio"]
    selim = ["Selim", "Canote", "Mesa", "Abraçadeira"]
    rodas = ["Rodas", "Freio", "Câmbio Traseiro", 'Câmbio Dianteiro', "Cassete", "Corrente", "Suspensão Traseira"]

    print("""Certo! Agora começará uma série de perguntas relacionadas 
    a cada parte da sua bicicleta para você declarar cada peça.""")
    print("---------------------------------------------------------------")
    responseData = {
            "Quadro": [],
            "Guidão": [],
            "Selim": [],
            "Rodas": [],
        }

    for i in range(0,4):

        match i:
            case 0: 
                i = 0
                print("Insira seu ID para darmos sequência")
                ID_QUADRO = int(input("id:"))
                responseData["Quadro"].append(ID_QUADRO)
                for item in quadro:

                    print(f'Item de decleração, {item};')
                    nome_da_peça = input("Nome da peça:")
                    responseData["Quadro"].append(nome_da_peça)
                    print("-----------------------------")               

                print("Verifique se todos os itens estão corretos:")
                j = 1
                for items in responseData["Quadro"]:
                    print(f'{j} - {items}')
                    j += 1
                question = input("(S)im ou (N)ão:")
                while question != "S" and question != "N":
                    print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
                    question = input("(S)im ou (N)ão:")
                if question == "S":
                    continue
                elif question =="N":
                    quantida_de_pecas_erradas = int(input("Quantas peças estão erradas?:"))
                    if quantida_de_pecas_erradas > 0:
                        for i in range(quantida_de_pecas_erradas):
                            peca_errada = int(input(f"Digite o índice do item errado (0 a 5): "))
                            if 0 <= peca_errada < len(responseData["Quadro"]):
                                correction = input(f"Digite a correção para o item {peca_errada}: ")
                                responseData["Quadro"][peca_errada] = correction
                    print("-----------------------------")
                    print("peças corrigidas!!")
                    j = 1
                    for items in responseData["Quadro"]:
                        print(f'{j} - {items}')
                        j += 1
                    print("Daremos sequência a pesquisa")
                    print("-----------------------------")

            case 1:
                print("Insira seu ID para darmos sequência")
                ID_GUIDAO = int(input("id:"))
                responseData["Guidão"].append(ID_QUADRO)

                for item in guidao:
                    print("-----------------------------")
                    print(f'Item de decleração, {item};')
                    nome_da_peça = input("Nome da peça:")
                    responseData["Guidão"].append(nome_da_peça)
                
                print("Verifique se todos os itens estão corretos:")
                j = 1
                for items in responseData["Guidão"]:
                    print(f'{j} - {items}')
                    j += 1
                question = input("(S)im ou (N)ão:")
                while question != "S" and question != "N":
                    print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
                    question = input("(S)im ou (N)ão:")
                if question == "S":
                    continue
                elif question =="N":
                    quantida_de_pecas_erradas = int(input("Quantas peças estão erradas?:"))
                    if quantida_de_pecas_erradas > 0:
                        for i in range(quantida_de_pecas_erradas):
                            peca_errada = int(input("Digite o índice do item errado (0 a 3): "))
                            if 0 <= peca_errada < len(responseData["Guidão"]):
                                correction = input(f"Digite a correção para o item {peca_errada}: ")
                                responseData["Guidão"][peca_errada] = correction
                    print("-----------------------------")
                    print("peças corrigidas!!")
                    j = 1
                    for items in responseData["Guidão"]:
                        print(f'{j} - {items}')
                        j += 1
                    print("Daremos sequência a pesquisa")
                    print("-----------------------------")

            case 2: 

                print("Insira seu ID para darmos sequência")
                ID_SELIM = int(input("id:"))
                responseData["Selim"].append(ID_SELIM)

                for item in selim:
                    print(f'Item de decleração, {item};')
                    nome_da_peça = input("Nome da peça:")
                    responseData["Selim"].append(nome_da_peça)
                    print("-----------------------------")
                
                print("Verifique se todos os itens estão corretos:")
                j = 1
                for items in responseData["Selim"]:
                    print(f'{j} - {items}')
                    j += 1
                question = input("(S)im ou (N)ão:")
                while question != "S" and question != "N":
                    print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
                    question = input("(S)im ou (N)ão:")
                if question == "S":
                    continue
                elif question =="N":
                    quantida_de_pecas_erradas = int(input("Quantas peças estão erradas?:"))
                    if quantida_de_pecas_erradas > 0:
                        for i in range(quantida_de_pecas_erradas):
                            peca_errada = int(input("Digite o índice do item errado (0 a 3): "))
                            if 0 <= peca_errada < len(responseData["Selim"]):
                                correction = input(f"Digite a correção para o item {peca_errada}: ")
                                responseData["Selim"][peca_errada] = correction
                    print("-----------------------------")
                    print("peças corrigidas!!")
                    j = 1
                    for items in responseData["Selim"]:
                        print(f'{j} - {items}')
                        j += 1
                    print("Daremos sequência a pesquisa")
                    print("-----------------------------")

            case 3:

                print("Insira seu ID para darmos sequência")
                ID_RODAS = int(input("id:"))
                responseData["Rodas"].append(ID_RODAS)

                for item in rodas:
                    print(f'Item de decleração, {item};')
                    nome_da_peça = input("Nome da peça:")
                    responseData["Rodas"].append(nome_da_peça)
                    print("-----------------------------")

                print("Verifique se todos os itens estão corretos:")
                j = 1
                for items in responseData["Rodas"]:
                    print(f'{j} - {items}')
                    j += 1
                question = input("(S)im ou (N)ão:")
                while question != "S" and question != "N":
                    print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
                    question = input("(S)im ou (N)ão:")
                if question == "S":
                    continue
                elif question =="N":
                    quantida_de_pecas_erradas = int(input("Quantas peças estão erradas?:"))
                    if quantida_de_pecas_erradas > 0:
                        for i in range(quantida_de_pecas_erradas):
                            peca_errada = int(input("Digite o índice do item errado (0 a 6): "))
                            if 0 <= peca_errada < len(responseData["Rodas"]):
                                correction = input(f"Digite a correção para o item {peca_errada}: ")
                                responseData["Rodas"][peca_errada] = correction
                    print("-----------------------------")
                    print("peças corrigidas!!")
                    j = 1
                    for items in responseData["Rodas"]:
                        print(f'{j} - {items}')
                        j += 1
                    print("Daremos sequência a pesquisa")
                    print("-----------------------------")

        i += 1
    
    return responseData

def CREATE_TABLE_QUADRO():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_QUADRO = """
    CREATE TABLE QUADRO(
    ID_QUADRO INT NOT NULL,
    MARCA_QUADRO VARCHAR(60),
    PEDAL VARCHAR(60),
    PEDIVELA VARCHAR(60) NOT NULL,
    CAIXA_DE_DIRECAO VARCHAR(60),
    GARFO VARCHAR(60), 
    ID_BICICLETA INT NOT NULL,
    CONSTRAINT pk_id_quadro PRIMARY KEY (ID_QUADRO),
    CONSTRAINT fk_QUADRO_BICICLETA FOREIGN KEY (ID_BICICLETA) REFERENCES BICICLETA(ID_BICICLETA)
    )"""

    try:
        cursor.execute(sql_QUADRO)
        print("Tabela QUADRO criada")

    except Exception as e:
        print(f'Erro ao criar a tabela QUADRO: {e}')
    
    finally:
        cursor.close
        conn.close

def INSERT_DADOS_QUADRO(responseData, lista_de_dados_bicicleta_geral):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO QUADRO (ID_QUADRO, MARCA_QUADRO, PEDAL, PEDIVELA, CAIXA_DE_DIRECAO, GARFO, ID_BICICLETA) VALUES (:0, :1, :2, :3, :4, :5, :6)"
    try:
        cursor.execute(sql_query, (responseData["Quadro"][0], responseData["Quadro"][1], responseData["Quadro"][2], responseData["Quadro"][3],responseData["Quadro"][4], responseData["Quadro"][5], lista_de_dados_bicicleta_geral[0]))
        conn.commit()
        print("Registro de cliente inserido com sucesso.")
    
    except Exception as e:
        print(f'Erro ao inserir o registro de cliente: {e}')
    
    finally:
        cursor.close()
        conn.close()

def DROP_TABLE_QUADRO():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_quadro = """
    DROP TABLE QUADRO
    """
    try:
        cursor.execute(sql_quadro)
        print("Tabela QUADRO dropada")
    
    except Exception as e:
        print(f'Erro ao dropar a tabela QUADRO: {e}')

    finally:
        cursor.close
        conn.close

def CREATE_TABLE_GUIDAO():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_GUIDAO = """
    CREATE TABLE GUIDAO(
    ID_GUIDAO INT NOT NULL,
    MARCA_GUIDAO VARCHAR(60),
    MANOPLAS VARCHAR(60),
    MANETE_DE_FREIO VARCHAR(60),
    ALAVANCA_DE_CAMBIO VARCHAR(60) NOT NULL,
    ID_BICICLETA INT NOT NULL,
    CONSTRAINT pk_id_guidao PRIMARY KEY (ID_GUIDAO),
    CONSTRAINT fk_GUIDAO_BICICLETA FOREIGN KEY (ID_BICICLETA) REFERENCES BICICLETA(ID_BICICLETA)
    )"""

    try:
        cursor.execute(sql_GUIDAO)
        print("Tabela GUIDAO criada")

    except Exception as e:
        print(f'Erro ao criar a tabela GUIDAO: {e}')
    
    finally:
        cursor.close
        conn.close

def INSERT_DADOS_GUIDAO(responseData, lista_de_dados_bicicleta_geral):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO GUIDAO (ID_GUIDAO, MARCA_GUIDAO, MANOPLAS, MANETE_DE_FREIO, ALAVANCA_DE_CAMBIO, ID_BICICLETA) VALUES (:0, :1, :2, :3, :4, :5)"
    try:
        cursor.execute(sql_query, (responseData["Guidão"][0], responseData["Guidão"][1], responseData["Guidão"][2], responseData["Guidão"][3], responseData["Guidão"][4], lista_de_dados_bicicleta_geral[0]))
        conn.commit()
        print("Registro de cliente inserido com sucesso.")
    
    except Exception as e:
        print(f'Erro ao inserir o registro de cliente: {e}')
    
    finally:
        cursor.close()
        conn.close()

def DROP_TABLE_GUIDAO():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_GUIDAO = """
    DROP TABLE GUIDAO
    """
    try:
        cursor.execute(sql_GUIDAO)
        print("Tabela GUIDAO dropada")
    
    except Exception as e:
        print(f'Erro ao dropar a tabela GUIDAO: {e}')

    finally:
        cursor.close
        conn.close

def CREATE_TABLE_SELIM():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_SELIM = """
    CREATE TABLE SELIM(
    ID_SELIM INT NOT NULL,
    MARCA_SELIM VARCHAR(60),
    CANOTE VARCHAR(60),
    MESA VARCHAR(60),
    ABRACADEIRA VARCHAR(60),
    ID_BICICLETA INT NOT NULL,
    CONSTRAINT pk_id_selim PRIMARY KEY (ID_SELIM),
    CONSTRAINT fk_SELIM_BICICLETA FOREIGN KEY (ID_BICICLETA) REFERENCES BICICLETA(ID_BICICLETA)
    )"""

    try:
        cursor.execute(sql_SELIM)
        print("Tabela SELIM criada")

    except Exception as e:
        print(f'Erro ao criar a tabela SELIM: {e}')
    
    finally:
        cursor.close
        conn.close

def INSERT_DADOS_SELIM(responseData, lista_de_dados_bicicleta_geral):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO SELIM (ID_SELIM, MARCA_SELIM, CANOTE, MESA, ABRACADEIRA, ID_BICICLETA) VALUES (:0, :1, :2, :3, :4, :5)"
    try:
        cursor.execute(sql_query, (responseData["Selim"][0], responseData["Selim"][1], responseData["Selim"][2], responseData["Selim"][3], responseData["Selim"][4], lista_de_dados_bicicleta_geral[0]))
        conn.commit()
        print("Registro de cliente inserido com sucesso.")
    
    except Exception as e:
        print(f'Erro ao inserir o registro de cliente: {e}')
    
    finally:
        cursor.close()
        conn.close()

def DROP_TABLE_SELIM():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_selim = """
    DROP TABLE SELIM
    """
    try:
        cursor.execute(sql_selim)
        print("Tabela SELIM dropada")
    
    except Exception as e:
        print(f'Erro ao dropar a tabela SELIM: {e}')

    finally:
        cursor.close
        conn.close

def CREATE_TABLE_RODAS():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_RODAS = """
    CREATE TABLE RODAS(
    ID_RODAS INT NOT NULL,
    MARCA_RODAS VARCHAR(60),
    FREIO VARCHAR(60),
    CAMBIO_TRASEIRO VARCHAR(60) NOT NULL,
    CAMBIO_DIANTEIRO VARCHAR(60) NOT NULL,
    CASSETE VARCHAR(60) NOT NULL,
    CORRENTE VARCHAR(60),
    SUSPENSAO_TRASEIRA VARCHAR(60),
    ID_BICICLETA INT NOT NULL,
    CONSTRAINT pk_id_rodas PRIMARY KEY (ID_RODAS),
    CONSTRAINT fk_RODAS_BICICLETA FOREIGN KEY (ID_BICICLETA) REFERENCES BICICLETA(ID_BICICLETA)
    )"""

    try:
        cursor.execute(sql_RODAS)
        print("Tabela RODAS criada")

    except Exception as e:
        print(f'Erro ao criar a tabela RODAS: {e}')
    
    finally:
        cursor.close
        conn.close

def INSERT_DADOS_RODAS(responseData, lista_de_dados_bicicleta_geral):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO RODAS (ID_RODAS, MARCA_RODAS, FREIO, CAMBIO_TRASEIRO, CAMBIO_DIANTEIRO, CASSETE, CORRENTE, SUSPENSAO_TRASEIRA, ID_BICICLETA) VALUES (:0, :1, :2, :3, :4, :5, :6, :7, :8)"
    try:
        cursor.execute(sql_query, (responseData["Rodas"][0], responseData["Rodas"][1], responseData["Rodas"][2], responseData["Rodas"][3], responseData["Rodas"][4], responseData["Rodas"][5], responseData["Rodas"][6], responseData["Rodas"][7], lista_de_dados_bicicleta_geral[0]))
        conn.commit()
        print("Registro de cliente inserido com sucesso.")
    
    except Exception as e:
        print(f'Erro ao inserir o registro de cliente: {e}')
    
    finally:
        cursor.close()
        conn.close()

def DROP_TABLE_RODAS():
    conn = getConnection()
    cursor = conn.cursor() #variável de execução do cursos
    sql_RODAS = """
    DROP TABLE RODAS
    """
    try:
        cursor.execute(sql_RODAS)
        print("Tabela RODAS dropada")
    
    except Exception as e:
        print(f'Erro ao dropar a tabela RODAS: {e}')

    finally:
        cursor.close
        conn.close

def selecao_menu_2_renovacao():
    listadepecas = ["Quadro", "Guidão", "Manoplas", "Manete de Freio", "Alavanca de Câmbio", "Mesa",
                    "Caixa de Direção", "Garfo", "Rodas", "Freio", "Câmbio Dianteiro", 
                        "Câmbio Traseiro", "Cassete", "Corrente", "Movimento Central", "Pedivela", "Pedal",
                        "Selim", "Canote de Selim", "Abraçadeira de Selim", "Suspensão Traseira"]


    print("------------------------------------------------------------")

    alteração = input("""Houve alguma alteração
em relação a bicicleta usada no seguro anterior?:""")
    if alteração == "N":
        print("Certo! O encaminharemos para o setor de upload de fotos para darmos sequência a vistoria!")

    elif alteração == "S":
        qntpecas = int(input("Quantidade de peças danificadas: "))
    
    while qntpecas < 0 or qntpecas > len(listadepecas):
        print("Quantidade inválida! Máximo de 21 peças!")
        qntpecas = int(input("Quantidade de peças alteradas: "))

    quaispecas = []
    
    print("------------------------------------------------------")
    print("""
Certo! Agora declare qual(is) peça(s) foi(foram) danificada:
    1 - Quadro
    2 - Guidão
    3 - Manoplas
    4 - Manete de Freio
    5 - Alavanca de Câmbio
    6 - Mesa
    7 - Caixa de Direção
    8 - Garfo
    9 - Rodas
    10 - Freio
    11 - Câmbio Dianteiro
    12 - Câmbio Traseiro
    13 - Cassete
    14 - Corrente
    15 - Movimento Central
    16 - Pedivela
    17 - Pedal
    18 - Selim
    19 - Canote de Selim
    20 - Abraçadeira de Selim
    21 - Suspensão Traseira
    """)

    for i in range(qntpecas):

        opcao = int(input("Peça(s): "))
        while opcao < 1 or opcao > len(listadepecas):
            print("Opção inválida! Escolha um número válido.")
            opcao = int(input("Peça(s): "))

    quaispecas.append(listadepecas[opcao - 1])

    print("As peças alteradas, são:", quaispecas, ",Certo?")
    question = input("(S)im ou (N)ão:")
    while question != "S" and question != "N":
        print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
        question = input("(S)im ou (N)ão:")
    
    print("Certo! nos envie os dados, com as marcas das peças novas, na mesma ordem da lista a seguir:", quaispecas)
    list = []
    i = 0
    
    while len(list) < len(quaispecas):
        marcas = input("Marcas: ")
        list.append(marcas)
        i += 1
        
    print("As marcas que compõe sua bicicleta, são", list , "Correto?")
    question = input("(S)im ou (N)ão:")
    while question != "S" and question != "N":
        print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
        question = input("(S)im ou (N)ão:")
    print("------------------------------------------------------")

    print("""Obrigado por se utilizar de nossos serviços!
O encaminharemos para o setor de upload de fotos
para darmos sequência a vistoria!""")

def selecao_menu_3_roubo():
      case = print("Caso sua bicicleta tenha sido furtada/roubada, teremos que analisar a situação!")
      local = input("Em qual local ocorreu?:")
      data =input("Em qual dia?:")
      BO = input("Já fez B.O. policial(responder com 'S' ou 'N'?:")
      if BO == "S":
        input("Nos envie o número do protocolo:")
        print("Certo, daremos sequência ao seu caso!")
        print("O encaminharemos para o setor responsável pelo caso! Obrigado por utilizar nossos serviços!")

      elif BO == "N":
        print("Recomendamos que faça e volte aqui para darmos sequência ao seu processo!")
        print(" Obrigado por utilizar nossos serviços!")

      while BO != "S" and BO != "N":
        print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
        BO = input("Já fez B.O. policial(responder com 'S' ou 'N'?:")
        if BO == "S":
          input("Nos envie o número do protocolo:")
          print("Certo, daremos sequência ao seu caso!")
          print("O encaminharemos para o setor responsável pelo caso! Obrigado por utilizar nossos serviços!")

        elif BO == "N":
          print("Recomendamos que faça e volte aqui para darmos sequência ao seu processo!")
          print(" Obrigado por utilizar nossos serviços!")

def main():
    CREATE_TABLE_CLIENTE()
    lista_de_dados_cliente = login()
    INSERIR_DADOS_CLIENTE(lista_de_dados_cliente)

    selecao = menu()
    match selecao:
        case 1:

            CREATE_TABLE_DADOS_BICICLETA()
            lista_de_dados_bicicleta_geral = selecao_menu_1_bicicleta_geral()
            INSERT_DADOS_BICICLETA(lista_de_dados_bicicleta_geral, lista_de_dados_cliente)

            responseData = selecao_menu_1_datalhes_bicicleta()
            CREATE_TABLE_QUADRO()
            INSERT_DADOS_QUADRO(responseData, lista_de_dados_bicicleta_geral)
            #
            CREATE_TABLE_GUIDAO()
            INSERT_DADOS_GUIDAO(responseData, lista_de_dados_bicicleta_geral)
            

            CREATE_TABLE_SELIM()
            INSERT_DADOS_SELIM(responseData, lista_de_dados_bicicleta_geral)

            CREATE_TABLE_RODAS()
            INSERT_DADOS_RODAS(responseData, lista_de_dados_bicicleta_geral)
        case 2: 
            selecao_menu_2_renovacao()
        
        case 3:
            selecao_menu_3_roubo()
    



main()

'''
DROP_TABLE_RODAS()
DROP_TABLE_SELIM()
DROP_TABLE_GUIDAO()
DROP_TABLE_QUADRO()
DROP_TABLE_DADOS_BICICLETA()
DROP_TABLE_CLIENTE()
'''

