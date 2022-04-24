import random

frutas = ("banana","laranja", "uva", "morango", 40)
for fr in frutas:
    print(fr)

escolha = random.choice(frutas)
print("\na fruta escolhida foi: ", escolha)

escolha2 = random.choice(range(1,11)) #escolha de 1 a 10
print("\n o numero escolhido: ", escolha2)

print("\n Fim")