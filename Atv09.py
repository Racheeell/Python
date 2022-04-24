#Fazer um programa contendo uma tupla inicial definida com 6 strings
#Depois criar uma outra tupla, com o mesmo conteudo da tupla inicial
#mas em  ordem invertida

#Todas as tuplas definidas nos exercícios podem ser criadas através do
#comando input, criação de uma tupla com a entrada fornecida e uso
#da propriedade de concatenação de tuplas

#PRIMEIRA FORMA
v_tupla1 =("123", "abc", "def", "45", "7890", "ghi")
v_nova_tupla = v_tupla1[1::-1]

qtde = len(v_tupla1)

print("tupla inicial = ", v_tupla1)
print("nova tupla: ", v_nova_tupla)
print("==================================================")
print("\n FIM")

#SEGUNDA FORMA
v_nova_tupla = ()
qtde = len(v_tupla1)

print("tupla inicial = ", v_tupla1)

for cont in range(qtde-1, -1, -1):
    print("Extensao = ", v_tupla1[cont:cont+1])
    v_nova_tupla = v_nova_tupla[:] + v_tupla1[cont: cont+1]
    print("nova tupla (parcial): ", v_nova_tupla)
    print("================================================")

print("\n\n\n==============================================")
print("tupla inicial = ", v_tupla1)
print("nova tupla: ", v_nova_tupla)
print("====================================================")
print("\nFIM")


v_nova_tupla =()

qtde =len(v_tupla1)
print