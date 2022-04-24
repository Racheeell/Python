#Fazer um programa em Python contendo uma tupla inicial definida com 6
#strings Depois criar um outra
#tupla , com o mesmo conteúdo da tupla inicial, mas em
#uma ordem aleatória.
import random

#tupla inicial
v_tupla1 = ("aa", "bb", "cc", "dd", "ee", "ff")
v_copia_inicial = v_tupla1

#tupla vazia
v_nova_tupla = ()

#verificar quantos itens tem
qtde =len(v_tupla1)

print("tupla inicial = ", v_tupla1)

#fazer loop do intervalo de 1 ate qtde mais 1
for cont in range(1, qtde+1):

    #randrange vai sortear um numero de 0 ate o comprimento da nossa tupla
    sorteio = random.randrange(len(v_tupla1))
    #v_tupla1[sorteio:sorteio+1] é so a posicao da tupla
    v_nova_tupla = v_nova_tupla[:] + v_tupla1[sorteio:sorteio+1]

    #vai sortear aqueles que ainda nao foram sorteados
    v_tupla1 = v_tupla1[:sorteio]+ v_tupla1[sorteio + 1:]

    print("tupla original ajustada= ", v_tupla1)
    print("nova tupla (parcial): ", v_nova_tupla)
    print("----------------------------------------------------------")

#Segunda Forma
import random
n1 =str(input("Digite a primeira fruta: "))
n2 =str(input("Digite a segunda fruta: "))
n3 =str(input("Digite a terceira fruta: "))
n4 =str(input("Digite a quarta fruta: "))
n5 =str(input("Digite a quinta fruta: "))
n6 =str(input("Digite a sexta fruta: "))

frutas =[n1,n2,n3,n4,n5,n6]
random.shuffle(frutas)
print(f"As frutas em ordem aleatoria {frutas}")
print(f"Frutas wm ordem alfabetica: {sorted(frutas)}")