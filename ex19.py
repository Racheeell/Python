lista1 = []
lista2 = [2,6]
lista3 =[1, "teste", 3*4]

print("Lista 1")
for item in lista1:
    print(item)

print("\n lista 2")
for item in lista2:
    print(item)

print("\n Lista 3")
for cont in range(0,3):
    print("posicao= ", cont, "conteudo da lista(do vetor)=", lista3[cont])

print("\n lista 3 - ultimo elemento")
print(lista3[-1])

print("\n lista 3 - penultimo elemento")
print(lista3[-2])

print("\n\n Lista 3: \n", lista3)

#acessar posicao inexistente