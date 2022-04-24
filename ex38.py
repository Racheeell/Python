lista = ["alberto", "roberto", "luis", "ricardo", "pamela"]

dicionario = dict.fromkeys(lista, 0)

print("Lista: \n", lista)
print("\n Dicionario criado apartir da lista: \n", dicionario)

print("Luiz=", dicionario["luiz"])

dicionario["luiz"] = 7.0
print("\n\n Alteracao do valor do Luiz.")
