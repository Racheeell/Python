#Gerar uma lista com vinte numeros inteiros aleatorios.
#Gerar duas listas novas a partir desta lista da seguinte forma:
#-Uma lista contendo os numeros pares
#- Uma lista contendo os numeros impares

import random

lista = []
lista_par = []
lista_impar = []

qtd = 20
#comando for para gerar as 10 repetiçoes
for cont in range(0, qtd):
    #atribuindo o numero randomico para variavel elemento
    elemento =random.randrange(1,100 )
    lista.append(elemento)

    if elemento % 2 == 0:
        lista_par.append(elemento)
    else:
        lista_impar.append(elemento)

lista_par.sort()
lista_impar.sort()

print(f"lista original -> {lista}")
print(f"lista original -> {lista_par}")
print(f"lista original -> {lista_impar}")

#--------------------------------------------------
#Segunda forma
#--------------------------------------------------
lista = []
listaImpar = []
listaPar = []

i = 0

while i < 20:
    lista.append((random.randrange(1, 101)))

    if lista[i] % 2 == 0:
        listaPar.append(lista[i])
    else:
        listaImpar.append(lista[i])
        i += 1

print(listaPar)
print(listaImpar)

#---------------------------------------------------
#Terceira forma
import random

qtde = 20

numeros =[ ]
pares = [ ]
impares =[ ]

for cont in range(0, qtde):
    num = random.randrange(1, 101)
    print("numero= ", num)
    numeros.append(num)

print("\nLista gerada: ")
print(numeros, "\n")

for cont in range(0, qtde):
    if(numeros[cont] % 2 == 0 ):
        pares.append(numeros[cont])
    else:
        impares.append(numeros[cont])

print("\n lista numeros pares: ")
print(pares)

print("\n lista numeros impares: ")
print(impares)

print("\n FIM")