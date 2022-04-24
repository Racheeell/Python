#------------------------------------------------------------------
#Fazer um programa em python que gera dez numeros inteiros aleatorios
#e apresenta como saida:

#a soma dos numeros pares
#a soma dos numeros inteiros

from random import randrange, uniform

aleatorio = 0
somaPares = 0
somaImpares = 0

for cont in range(1,11):
    aleatorio = (randrange(11,40))
    print("O numero gerado aleatorio é: ", aleatorio)

    if aleatorio % 2 == 0:
        print("Numero par")
        somaPares = somaPares + aleatorio
        print("")
    else:
        print("Numero impar")
        somaImpares = somaImpares + aleatorio
        print("")

print("")
print("A soma dos numeros Pares é de: ", somaPares)
print("A soma dos numeros Impares é de: ", somaImpares)