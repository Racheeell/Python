#Fazer um programa em python que le uma string de entrada
# e gera como saida o conteudo desta string em ordem inversa

var_str =input("Digite uma string: ")
pos_final = len(var_str) - 1
nova_str = ""

#comando for decrescente
#for cont in range(10, 0, -1):
 #   print("cont = ", cont)

for cont in range(pos_final, -1, -1):
    print("posicao", cont, "letra=", var_str[cont])
    nova_str += var_str[cont]
    print("string invertida parcial = \n \n", nova_str)

print("string informada = ", var_str)
print("string invertida = ", nova_str)


#SEGUNDA FORMA
print("\n\n\nSegunda Forma")
nova_str =""

for cont  in range(0, pos_final+1):
    print("posicao ", cont, "letra=", var_str[cont])
    nova_str = var_str[cont] + nova_str
    print("\n\nstring invertida parcial = ", nova_str)

print("string informada = ", var_str)
print("string invertida = ", nova_str)

print("FIM")