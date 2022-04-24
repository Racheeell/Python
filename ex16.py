import random

frutas = ("banana", "laranja", "uva", "morango", "mamao", "pera", "graviola")
print("todas as frutas", frutas)

for cont in range(1,6):
    sorteio = random.randrange(len(frutas))
    print("Repetição = ", cont)
    print("Sorteio =", sorteio)
    print("Fruta sorteada: ", frutas[sorteio], "\n", "=" * 40)

#print("\n\nparte 8")
#for cont in range(1,10):
# print("Sorteio = ", random.randrange(3)) #sorteio dos numeros 0,1 ou 2

print("\nFIM")