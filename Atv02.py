#--------------------------------------------------------------------
#Fazer um programa em python que faz a leitura numeros inteiros
# ate que seja informado o numero zero

#Como saida o programa apresenta ao final a quantidade de numeros
#pares e a quantidade de numeros impares.

num = 1
par: int = 0
impar: int = 0

while num!=0:
    num = int(input("Digite um numero inteiro: "))
    if num % 2 == 0: 
        par += 1

    else:
      impar += 1

print("O resultado da soma \n dos numeros Pares = ", par)
print("Impar = ", impar)
print("FIM")