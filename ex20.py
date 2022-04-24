lista = ["a", "teste", "c"]

print("\n lista")
print(lista)

for item in lista:
    print(item)

lista = lista + ["outro"] + ["mais um"]

print("\n lista - com mais itens")
for item in lista:
    print(item)

lista[1] = "b" * 4
print("\n lista - alterada 2")
for item in lista:
    print(item)
    