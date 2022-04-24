'''
Fazer dois programas:
A-Programa 1(sub-rotina):
Ler dois numeros  e mostrar como saida a soma dos numeros

B-Programa 2(sub-rotina):
Ler dois numeros e mostrar como saida a multiplicacao dos numeros

O programa principal deve fazer  a chamada dos dois programas
(duas sub-rotinas)
'''

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
soma()
multiplica()
soma()
print("\n Fim")