'''
Com os programas anteriores,  de soma e multiplicacao, alterar
o programa principal para que ele tenha um bloco de repeticao,
permitindo  varias vezes a escolha e chamada de um dos dois
programas, apresentando um menu das opçoes.

Indicar no menu uma opcao  de termino do programa

Exemplo:
0- Para Sair(terminar)
1- Somar de numeros
2- Multiplicacao de numeros
'''


import time
def soma():
    print("\nSoma\n")
    num1=int(input("Informe um número : "))
    num2=int(input("Informe um outro número : "))
    print("Soma dos números:", num1 + num2)

def multiplica():
    print("\nMultiplicação\n")
    num1 = int(input("Informe um número : "))
    num2 = int(input("Informe um outro número : "))
    print("Multiplicação dos números:", num1 * num2)

    
# Programa principal
print("operações com números \n")
condicao = True
while condicao:
    print("\n\n\n-----------------------------------------")
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Multiplicação")
    print("-----------------------------------------------")
    opcao = int(input("Informe uma opção: "))
    if opcao == 1:
        soma()
    elif opcao == 2:
        multiplica()
    elif opcao == 0:
        condicao = False
    else:
        print("Opção inválida")
    time.sleep(5)
print("\n Fim")