#fazer um programa que leia uma string de entrada e gera como saida o conteudo
#desta string da seguinte forma:
#ex: Entrada: abcdef -> saida: acebdf

var_str = input("Digite uma string: ")

parte1 = var_str[::2]
parte2 = var_str[1::2]

print("parte 1 ", parte1)
print("parte 2 ", parte2)

nova = parte1 + parte2
print("String modificada final: ", nova)

print("\n\n FIM")

