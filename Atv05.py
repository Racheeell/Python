#Fazer um programa em python que le uma string de entrada
#e gera como saida o conteudo desta string em ordem inversa, trocando
#as letras originais 'a' por 'o', e 'o' por 'a'

var_str = input("informe uma string: ")

#inversao da string
nova_str = var_str[::-1]

#saida parcial
print("string informada = ", var_str)
print("string invertida = ", nova_str)

#substituicoes
nova_str = nova_str.replace("a", "#@$")
nova_str = nova_str.replace("o", "a")
nova_str = nova_str.replace("#@$", "o")

#saida
print("="*50)
print("string informada = ", var_str)
print("string invertida com substituiçoes= ", nova_str)

print("FIM")
