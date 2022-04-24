# ---------------------------------------------#
#                                             #
#  Nome: Miguel Fernandes Santos              #
#  Projeto: Conta bancaria.                   #
#  Data: 25/10/2021                           #
#                                             #
# ---------------------------------------------#

# Importa a biblioteca para conseguir pegar a data atual:
from datetime import date

# Importa a bibloteca para criar grafico:
import matplotlib.pyplot as plt

# Importa a biblioteca matematica:
import math

# Importa a biblioteca Os:
import os

# Importa a biblioteca Sqlite:
import sqlite3

# Importa o pandas:
import pandas as pd


####################################################################################
def NovaTabela():
    # Cria uma query sql para criar a tabela:
    QueryTb = 'Create table if not exists Tb_Estatistica' \
              '(Tb_Estatistica_Id integer not null primary key autoincrement,' \
              'Tb_Estatistica_Media decimal(10, 5),' \
              'Tb_Estatistica_Moda decimal(10, 5),' \
              'Tb_Estatistica_Mediana decimal(10, 5),' \
              'Tb_Estatistica_PrimeiroQuartil decimal(10, 5),' \
              'Tb_Estatistica_TerceiroQuartil decimal(10, 5),' \
              'Tb_Estatistica_Amplitude decimal(10, 5),' \
              'Tb_Estatistica_DesvioPadrao decimal(10,5))'

    QueryDeletar = 'DELETE FROM Tb_Estatistica'

    # executa a query de criação da tabela:
    cursor.execute(QueryTb)

    # Executa a query para limpar os dados da tabela:
    cursor.execute(QueryDeletar)

    # O comando anterior foi utilizado para que de forma didatica o banco sempre comece
    # sem nenhum registro das execusoes anteriores, entretando no cotidiano é algo
    # que normalmente nao deve ser feito


####################################################################################
def BancoInserir(Valores=[]):
    # Query para inserir valores no banco de dados:
    QueryTbInserir = 'insert into Tb_Estatistica' \
                     '(Tb_Estatistica_Media, Tb_Estatistica_Moda,' \
                     'Tb_Estatistica_Mediana, Tb_Estatistica_PrimeiroQuartil,' \
                     'Tb_Estatistica_TerceiroQuartil, Tb_Estatistica_Amplitude,' \
                     'Tb_Estatistica_DesvioPadrao)' \
                     'values (?,?,?,?,?,?,?)'

    # Executa a query trocando os "?" pelos valores do array:
    cursor.execute(QueryTbInserir, Valores)

    # Salva a mudança no banco:
    conexao.commit()


####################################################################################
def ExibirBanco():
    # Cria uma serie de lista para receber cada valor do banco:
    listaMedia = []
    listaModa = []
    listaMediana = []
    listaPrimeiroQuartil = []
    listaTerceiroQuartil = []
    listaAmplitude = []
    listaDesviopadrao = []

    # Query para selecionar todos os conteudos do banco:
    QueryTbSelecionar = "select * from Tb_Estatistica"

    # execulta a query:
    cursor.execute(QueryTbSelecionar)

    # Um variavel receber o que foi retornado da query:
    valores = cursor.fetchall()

    # faz um laço que percorre cada valor retornado:
    for linha in valores:

    # Atribui para as listas os valores respectivos:
        listaMedia.append(linha[1])
        listaModa.append(linha[2])
        listaMediana.append(linha[3])
        listaPrimeiroQuartil.append(linha[4])
        listaTerceiroQuartil.append(linha[5])
        listaAmplitude.append(linha[6])
        listaDesviopadrao.append(linha[7])

    # Cria um dicionario para fazer um DataFrame pandas:
    Banco = {

        'Media': listaMedia,
        'Moda': listaModa,
        'Mediana': listaMediana,
        'PriQuartil': listaPrimeiroQuartil,
        'TercQuartil': listaTerceiroQuartil,
        'Amplitude': listaAmplitude,
        'DesvPadrao': listaDesviopadrao

    }

    # Cria um DataFrame:
    banco_df = pd.DataFrame(Banco)

    # Mostra o DataFrame:
    display(banco_df)


####################################################################################

# 1 - MÉDIA ARITMÉTICA SIMPLES
def mediasimples(valores=[]):
    media = 0
    # qtde_elementos recebe o valor referente a quantidade de elementos presentes na lista de valores.
    qtde_elementos = len(valores)

    # para cada elemento nessa lista de valores, incrementa-se na variável média.
    for item in valores:
        media += item

    # Calcula-se então o valor da média dividindo o valor da variavel media pela quantidade de elementos.
    media = media / qtde_elementos
    return media


####################################################################################

#             2 - MODA
def moda(valores=[]):
    # Cria-se um dicionário onde cada elemento na lista de valores é uma chave com valor inicial 0.
    dic = {item: 0 for item in valores}
    # É feita uma varredura na lista de valores e caso uma chave seja encontrada, incrementa-se 1 em seu valor.
    for item in valores:
        if item in dic.keys():
            dic[item] += 1

    # Cria-se uma lista com as reincidências dos valores.
    valor_moda = [item for item in dic.values()]

    # Capturam-se as chaves que possuem os valores iguais ao valor mais alto de valor_moda.
    resultado_moda = [numero for numero in dic.keys() if dic[numero] == max(valor_moda) and max(valor_moda) > 1]

    if len(resultado_moda) != 0:
        return resultado_moda

    else:
        return None


####################################################################################

#             3 - MEDIANA
def mediana(valores=[]):
    # qtde_elementos recebe o valor referente a quantidade de elementos presentes na lista de valores.
    qtde_elementos = len(valores)

    # Verifica se a divisão por 2 é exata.
    if qtde_elementos % 2 == 0:
        # Aplicação da formula n / 2; (Como nesse caso a divisão foi exata, soma-se ao valor seguinte ao resultado e divide-se por 2).
        med = (valores[int((qtde_elementos / 2) - 1)] + valores[int((qtde_elementos / 2))]) / 2

    else:
        # Também aplicação da fórmula n / 2; (Nesse caso não trata-se de uma divisão exata, portanto utiliza-se somente a parte inteira através do cast).
        med = valores[int((qtde_elementos / 2))]

    return med


####################################################################################

#             4 - PRIMEIRO QUARTIL
def primeiroquartil(valores=[]):
    # qtde_elementos recebe o valor referente a quantidade de elementos presentes na lista de valores.
    qtde_elementos = len(valores)

    # Verifica se a divisão por 4 é exata.
    if qtde_elementos % 4 == 0:
        # Aplicação da formula n / 4; (Como nesse caso a divisão foi exata, soma-se ao valor seguinte ao resultado e divide-se por 2).
        q1 = (valores[int((qtde_elementos / 4) - 1)] + valores[int((qtde_elementos / 4))]) / 2

    else:
        # Também aplicação da fórmula n / 4; (Nesse caso não trata-se de uma divisão exata, portanto utiliza-se somente a parte inteira através do cast).
        q1 = valores[int((qtde_elementos / 4))]

    return q1


####################################################################################

#             5 - TERCEIRO QUARTIL
def terceiroquartil(valores=[]):
    # qtde_elementos recebe o valor referente a quantidade de elementos presentes na lista de valores.
    qtde_elementos = len(valores)

    # Verifica se a divisão por 4 é exata.
    if (3 * qtde_elementos) % 4 == 0:
        # Aplicação da formula 3n / 4; (Como nesse caso a divisão foi exata, soma-se ao valor seguinte ao resultado e divide-se por 2).
        q3 = (valores[int((3 * qtde_elementos / 4) - 1)] + valores[int((3 * qtde_elementos / 4))]) / 2
    else:
        # Também aplicação da fórmula 3n / 4; (Nesse caso não trata-se de uma divisão exata, portanto utiliza-se somente a parte inteira através do cast).
        q3 = valores[int(((3 * qtde_elementos) / 4))]

    return q3


####################################################################################

#             6 - AMPLITUDE
def amplitude(valores=[]):
    # Recebe o MAIOR valor da lista de valores.
    maior = max(valores)
    # Recebe o MENOR valor da lista de valores.
    menor = min(valores)
    # Recebe a diferença entre o MAIOR valor e o MENOR valor.
    amplitude = maior - menor

    return amplitude


####################################################################################

#             7 - DESVIO-PADRÃO
def desvioPadrao(valores=[]):
    media = 0
    tamanho = len(valores) - 1
    indice = 0
    valor = 0
    soma = 0
    variancias = [None for _ in range(tamanho + 1)]
    varianciasQuadrada = [None for _ in range(tamanho + 1)]

    for item in valores:
        media += item

    media = media / (tamanho + 1)

    for item in valores:
        valor = item - media
        variancias[indice] = valor
        indice += 1

    indice = 0

    for item in variancias:
        valor = item * item
        varianciasQuadrada[indice] = valor
        indice += 1

    soma = sum(varianciasQuadrada)
    soma = soma / tamanho
    soma = math.sqrt(soma)

    return soma


####################################################################################

#             9 - TUDO
def tudo(valores=[]):
    dados = [None for _ in range(7)]
    dados[0] = mediasimples(valores)
    dados[1] = moda(valores)
    dados[2] = mediana(valores)
    dados[3] = primeiroquartil(valores)
    dados[4] = terceiroquartil(valores)
    dados[5] = amplitude(valores)
    dados[6] = desvioPadrao(valores)

    BancoInserir(dados)


####################################################################################

# função para criar um grafico da movimentação do saldo:
def GraficoLinha(valores=[]):
    # pega a quantidade de movimentações:
    tamanho = len(valores)
    # Declara uma variavel para colocar no eixo:
    x = 1
    # Cria uma lista para ser o eixo:
    Eixo = []

    # Laço para deixar o eixo com a mesma quantidade de valores que o saldo:
    while (x <= tamanho):
        # Adiciona no eixo o valor de X:
        Eixo.append(x)
        # Adiciona +1 no X:
        x = x + 1

    # Cria um Grafico:
    plt.plot(Eixo, valores)
    # Eixo Y recebe a palavra Saldo:
    plt.ylabel('Saldo')
    # Eixo X recebe a palavra Quantidade:
    plt.xlabel('Quantidade')
    # Mostra o grafico:
    plt.show()


####################################################################################

# função para criar um grafico de barras:
def GraficoBarra(valores={}):
    # coloca as label em baixo das barras:
    Tipos = ['Saldo', 'Credito', 'Credito Pagar']
    # Os valores usados para a altura da barra baseado no seu valor:
    Dados = [valores["Saldo"], valores["Credito"], valores["CreditoPagar"], ]
    # criando o grafico de barras:
    plt.bar(Tipos, Dados, color="black")
    # Label do Y:
    plt.ylabel("Valor")
    # TItulo do grafico:
    plt.title("Saldos")
    # mostrar o grafico:
    plt.show()


####################################################################################

# função para retornar o valor do credito que vc possue:
def SeuCredito(salario):
    # Cria uma lista com 3 valores que se iniciam em 0:
    dados = [0 for _ in range(3)]

    # Credito de 50% a mais:
    dados[0] = ((salario / 100) * 50) + salario

    # Credito de 75% a mais:
    dados[1] = ((salario / 100) * 75) + salario

    # Credito de 100% a mais:
    dados[2] = ((salario / 100) * 100) + salario

    return dados


####################################################################################

# função para gerar arquivo txt do extrato na mesma pasta que o arquivo:
def Extrato(valores={}, nome=""):
    # Pega a data atual:
    Data = date.today()

    # Pega a quantidade total de valores no historico:
    Tamanho = len(valores["Historico"])

    # Abre um documento chamado 'extrato.txt':
    with open('extrato.txt', 'w+') as extrato:
        # Escreve no documento a data atual:
        extrato.write("Data atual: " + str(Data) + "\n")
        # Escreve no documento o nome:
        extrato.write("Nome: " + str(nome) + "\n")
        # Escreve no documento o Saldo atual:
        extrato.write("Saldo atual: " + str(valores["Saldo"]) + "\n")
        # Escreve no documento o Credito atual:
        extrato.write("Credito atual: " + str(valores["Credito"]) + "\n")
        # Escreve no documento o credito a pagar atual:
        extrato.write("Credito a Pagar: " + str(valores["CreditoPagar"]) + "\n")

        # Se existir algo no historico
        if (Tamanho > 0):
            extrato.write("\n\n---------- HISTORICO ---------\n")
            # escrever cada uma das informaçoes do historico:
            for historico in valores["Historico"]:
                extrato.write(str(historico) + "\n")


####################################################################################

# Adiciona no historico de transaçoes:
def Historico(palavra, valor, ):
    # Pega a data Atual:
    Data = date.today()
    # Declara a variavel frase:
    Frase = ""

    # A variavel frase recebe a data mais o tipo de movimento mais o valor:
    Frase = str(Data) + " - Foi " + palavra + " um valor de " + str(valor)

    return Frase


####################################################################################

# função para retirar o dinheiro:
def Retirar(valor, saldo):
    # Se o saldo for menor que o valor a retirar:
    if (saldo < valor):
        print("Infelizmente o valor que deseja retirar é maior que o seu saldo atual.")
        return saldo

    else:
        saldo = saldo - valor

    return saldo


####################################################################################

# função para adicionar valor a sua conta:
def Adicionar(valor, saldo):
    # adiciona saldo:
    saldo = saldo + valor

    return saldo


####################################################################################

# função para pedir credito:
def Credito(valor, credito, saldo, divida):
    # Cria uma lista com 3 valores que se iniciam em 0
    dados = [0 for _ in range(3)]

    # Se seu credito for menor que o valor que vc deseja retirar:
    if (valor > credito):
        print("\nInfelizmente seu credito é menor que o necessario!!!")
        return dados

    # indice 0 é o saldo atual + o credito:
    dados[0] = valor
    # indice 1 é o valor de credito que tem que pagar:
    dados[1] = divida + valor
    # indice 2 é o valor de credito que vc ainda possui:
    dados[2] = credito - valor

    # retorna a lista:
    return dados


####################################################################################

def PagarCredito(Saldo, CreditoPagar):
    Opcao = 0
    Pagar = 0

    # Primeiro observa se existe credito a pagar:
    if (CreditoPagar <= 0):
        print("Você nao possui credito a pagar.\n")
        return 0

    else:  # Se existir um valor a pagar:

        # Mostra o valor que voce tem a pagar:
        print("\nO seu credito a pagar é de " + str(CreditoPagar))
        # Faz a leitura de quanto o usuario quer pagar:
        Pagar = converter(input("\nQual o valor que deseja pagar?"))

        # Se o usuario digitou letras ou o numero 0:
        if (Pagar == 0):
            print("Infelizmente o valor é invalido ou igual a 0, tenta novamente mais tarde!")
            return 0

        # Se o seu saldo é insuficiente para realizar o pagamento:
        elif (Pagar > Saldo):
            print("Não possui saldo suficiente para realizar esse pagamento, tente novamente mais tarde!")
            return 0

        # Se o usuario deseja pagar mais que o necessario:
        elif (Pagar > CreditoPagar):

            # laço para fazer o usuario escolher uma das opções:
            while (Opcao != 1 or Opcao != 2):

                # Mostra que o valor que deseja pagar é superior que o valor necessario:
                print("\n\nO valor que deseja pagar é maior que " + str(CreditoPagar) + ".\n")

                # Pergunta se deseja realmente pagar:
                opcao = converter(input("Deseja pagar o valor total?\n 1 - Sim\n 2 - Não"))

                # Se deseja:
                if (opcao == 1):
                    # Pagar recebe o valor total da divida:
                    Pagar = CreditoPagar
                    print("Okay, foi pago o valor total!")
                    # Retorna o valor total a pagar:
                    return Pagar

                elif (opcao == 2):  # Se Nao deseja
                    print("Okay, nao foi realizado o pagamento do credito!")
                    return 0

                else:  # Se nao ser nenhuma das 2:
                    print("Opção invalida!!!\n\n")

        else:  # Se nao paga normalmente
            print("Foi pago um valor total de " + str(Pagar))
            return Pagar


####################################################################################

# IMPORTANTE:

# função para descobrir se o que foi digitado é um numero:
def converter(valor):
    # declara a variavel retorno:
    retorno = None

    # Vai tentar converter o valor passado para float:
    try:
        retorno = float(valor)

    # se nao der certo retorna 0:
    except:
        print("O valor inserido anteriormente nao é um numero!!!!!")
        return 0

    return retorno


####################################################################################

# Dicionario das variaveis da pessoa:
Pessoa = {

    "Nome": "",
    "Salario": 0,
    "Menu": 0,
    "opcoes": []

}

# Dicionario das variaveis que seram usadas na conta:
Dados = {

    "Saldo": 0,
    "SaldoProvisorio": 0,
    "Credito": 0,
    "CreditoPagar": 0,
    "AuxiliarRetirar": 0,
    "AuxiliarColocar": 0,
    "Historico": [],
    "HistoricoSaldo": [],
    "Estatistica": [],
    "Menu": 0,

}

# ---------- Cadastro da pessoa ---------- :


# ---------- Controle da conta ---------- :

print("\n---------- Cadastrar ---------")

# Vai pedir o seu nome:
Pessoa["Nome"] = input("Digite o seu nome: ")

# Vai forçar vc a digitar um salario maior que 0:
while Pessoa["Salario"] <= 0:
    # Pede para digitar o salario, e chama a funçao que retorna o valor em float se possivel_
    # Caso nao seja um numero retorna o valor 0, entao volta a pedir o salario:
    Pessoa["Salario"] = converter(input("Digite o seu salario: "))

# Chama a funçao que descobre os creditos que vc tem direito:
Dados["Saldo"] = Pessoa["Salario"]
Dados["HistoricoSaldo"].append(Dados["Saldo"])

Pessoa["opcoes"] = SeuCredito(Pessoa["Salario"])

# Força o usuario a escolher uma das 3 opçoes:
while (Pessoa["Menu"] < 1) or (Pessoa["Menu"] > 3):

    print("\nBaseado em seu salario você tem direito a creditos de: \n")
    print(" 1 - " + str(Pessoa["opcoes"][0]))
    print(" 2 - " + str(Pessoa["opcoes"][1]))
    print(" 3 - " + str(Pessoa["opcoes"][2]))

    # pergunta a sua escolha e chama a funçao converter que retorna o valor em float_
    # Caso nao seja possivel retorna 0 e volta o laço do começo:
    Pessoa["Menu"] = converter(input("Qual das opções acima você deseja?"))

    # 50%
    if Pessoa["Menu"] == 1:
        Dados["Credito"] = Pessoa["opcoes"][0]

    # 75%
    elif (Pessoa["Menu"] == 2):
        Dados["Credito"] = Pessoa["opcoes"][1]

    # 100%
    elif (Pessoa["Menu"] == 3):
        Dados["Credito"] = Pessoa["opcoes"][2]

    else:
        print("Opção invalida!!!!")

# --------- Fim do Cadastro da pessoa --------- :

print("\nBem vindo: \n\n")

# Ele faz a conexao com o banco de dados e caso nao exista ele cria o banco:
conexao = sqlite3.connect('Estatistica.db')

# Criando um cursor para percorrer o banco de dados:
cursor = conexao.cursor()

NovaTabela()

while (Dados["Menu"] != 10):

    valores = []

    # Cria um Menu
    # pagar credito &¨& transferencia:
    print("\n--------- MENU ---------")
    print(
        "\n 1 - Retirar\n 2 - Colocar\n 3 - Credito\n 4 - Pagar Credito\n 5 - Transferencia\n 6 - Extrato\n 7 - Movimentação\n 8 - Estatistica\n 9 - Exibir Banco\n 10 - Sair\n")
    print("--------- MENU ---------\n")

    # Pergunta qual a escolha do usuario:
    Dados["Menu"] = 0
    Dados["Menu"] = converter(input("Qual a sua escolha?"))

    # Opção numero 1 é retirar:
    if (Dados["Menu"] == 1):
        # Pede para o usuario digitar o valor que deseja transferir:
        Dados["AuxiliarRetirar"] = input("Digite o valor que deseja retirar: ")

        # Chama a função que converte o valor:
        Dados["AuxiliarRetirar"] = converter(Dados["AuxiliarRetirar"])

        # Chama a função para retirar o valor da conta:
        Dados["SaldoProvisorio"] = Retirar(Dados["AuxiliarRetirar"], Dados["Saldo"])

        # Se foi realizado:
        if (Dados["SaldoProvisorio"] != Dados["Saldo"]):

            # Saldo recebe o novo saldo:
            Dados["Saldo"] = Dados["SaldoProvisorio"]

            # Adiciona no historico:
            Dados["Historico"].append(Historico("retirar", Dados["AuxiliarRetirar"]))

            # Adiciona o valor atual do saldo:
            Dados["HistoricoSaldo"].append(Dados["Saldo"])

    # opção numero 2 é inserir:
    elif (Dados["Menu"] == 2):
        # Pede para o usuario digitar o valor que deseja inserir:
        Dados["AuxiliarColocar"] = input("Digite o valor que deseja inserir: ")
        # Chama a função que converte o valor:
        Dados["AuxiliarColocar"] = converter(Dados["AuxiliarColocar"])
        # Chama a função para inserir o valor na conta:
        Dados["Saldo"] = Adicionar(Dados["AuxiliarColocar"], Dados["Saldo"])
        # Adiciona no historico:
        Dados["Historico"].append(Historico("Adicionado", Dados["AuxiliarColocar"]))
        # Adiciona o valor atual do saldo:
        Dados["HistoricoSaldo"].append(Dados["Saldo"])

        # opção numero 3 é credito:
    elif (Dados["Menu"] == 3):
        # Pede para o usuario digitar o valor que deseja inserir:
        Dados["AuxiliarColocar"] = input("Digite o valor que deseja de credito: ")
        # Chama a função que converte o valor:
        Dados["AuxiliarColocar"] = converter(Dados["AuxiliarColocar"])
        # Chama a função que calcula o credito e retorna um vetor:
        valores = Credito(Dados["AuxiliarColocar"], Dados["Credito"], Dados["Saldo"], Dados["CreditoPagar"])
        # Adiciona no saldo o valor que foi pedido:
        Dados["Saldo"] = Dados["Saldo"] + valores[0]
        # Adiciona no credito a pagar o valor que foi pedido:
        Dados["CreditoPagar"] = Dados["CreditoPagar"] + valores[1]
        # Diminui o credito a recuperar:
        Dados["Credito"] = Dados["Credito"] - valores[2]
        # Coloca no historico:
        Dados["Historico"].append(Historico("adicionado um credito em", valores[0]))
        # Adiciona o valor atual do saldo:
        Dados["HistoricoSaldo"].append(Dados["Saldo"])

    # opção numero 4 Pagar Credito:
    elif (Dados["Menu"] == 4):
        # Chama função pagar credito:
        Dados["AuxiliarRetirar"] = PagarCredito(Dados["Saldo"], Dados["CreditoPagar"])
        # diminui o valor do saldo baseado no retorno da função:
        Dados["Saldo"] = Dados["Saldo"] - Dados["AuxiliarRetirar"]
        # aumenta o valor do credito baseado no retorno da função:
        Dados["Credito"] = Dados["Credito"] + Dados["AuxiliarRetirar"]
        # diminui o valor a pagar de credito baseado no retorno da função:
        Dados["CreditoPagar"] = Dados["CreditoPagar"] - Dados["AuxiliarRetirar"]
        # Se o valor retornado ser diferente de 0:
        if (Dados["AuxiliarRetirar"]) != 0:
            # Adiciona no historico:
            Dados["Historico"].append(Historico("pago a divida credito em", Dados["AuxiliarRetirar"]))
            # Grava o saldo atual no historico:
            Dados["HistoricoSaldo"].append(Dados["Saldo"])

    # opção numero 5 Transferencia:
    elif (Dados["Menu"] == 5):
        # Pede para o usuario digitar o valor que deseja transferir:
        Dados["AuxiliarRetirar"] = input("Digite o valor que deseja transferir: ")
        # Chama a função que converte o valor:
        Dados["AuxiliarRetirar"] = converter(Dados["AuxiliarRetirar"])
        # Chama a função para retirar o valor da conta:
        Dados["SaldoProvisorio"] = Retirar(Dados["AuxiliarRetirar"], Dados["Saldo"])
        # Se foi realizado:
        if (Dados["SaldoProvisorio"] != Dados["Saldo"]):
            # Saldo recebe o novo saldo:
            Dados["Saldo"] = Dados["SaldoProvisorio"]
            # Adiciona no historico:
            Dados["Historico"].append(Historico("transferido", (Dados["Saldo"] - Dados["AuxiliarRetirar"])))
            # Adiciona o valor atual do saldo:
            Dados["HistoricoSaldo"].append(Dados["Saldo"])

    # opção numero 6 Extrato:
    elif (Dados["Menu"] == 6):
        Extrato(Dados, Pessoa["Nome"])

    # opção numero 7 Graficos:
    elif (Dados["Menu"] == 7):
        GraficoLinha(Dados["HistoricoSaldo"])
        GraficoBarra(Dados)

    # opção numero 8 Estatistica:
    elif (Dados["Menu"] == 8):
        # Se o tamanho da lista ser maior que 1:
        if (len(Dados["HistoricoSaldo"]) > 1):
            # Chama a função que calcula todas as analises estatistica:
            tudo(Dados["HistoricoSaldo"])
            # Mostra para o usuario que foi realizado com sucesso.
            print("Foi realizado a analise estatistica, caso deseje ver utilize a opção numero 9 do menu!")

        else:  # Se o tamanho ser menor ou igual a 1:
            # Mostra para o usuario que nao teve movimentaçoes na conta:
            print("Não é possivel realizar pois nao ocorreu movimentação na sua conta!\n\n")

    # opção numero 9 exibe o banco em um dataframe pandas:
    elif (Dados["Menu"] == 9):
        ExibirBanco()

    # opção numero 10 sair:
    elif (Dados["Menu"] == 10):
        print("Saindo...")
        conexao.close()

    else:
        print("Opção invalida!!!!")