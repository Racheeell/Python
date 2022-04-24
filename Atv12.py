#Fazer um programa, que gera uma lista com dez numeros inteiros aleatorios.
#Gerar duas listas novas a partir desta lista com os dez numeros, sendo:

#-Uma lista contendo os numeros ordenados, de forma crescente.
#-Uma lista contendo os numeros ordenados, de forma decrescente.

 ''' PRIMEIRA FORMA
 import random

 qtde = 10

 for cont in range(0, qtde):
     num = random.randrange(1,101)
     print("numero= ", num)
*/
'''
#SEGUNDA FORMA-----------------------------------
import random
lista = []
i = 0

while i < 10:
    #posicao ate 9
    lista.append(random.randrange(1, 101))
    #valores sorteados ate 101
    print("Numero: ", lista[i])
i += 1

print(lista)

#ORDEM CRESCENTE
listaSort = []
listaSort.extend(lista)
listaSort.sort()
print(listaSort)

#ORDEM DECRESCENTE
listaReverse = []
listaReverse.extend(lista)
listaReverse.reverse()
print(listaReverse)

#TERCEIRA FORMA
'''
import random

qtde= 10
numeros = []
crescente= []
decrescente= []

#cresc_v2 = []

for cont in range(0, qtde):
    num = random.randrange(1,101)
    #print("numero =", num)
    numeros.append(num)
    print(numeros, "\n")
    
crescente = numeros
'''