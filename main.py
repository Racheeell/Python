#-----------------------------------------------------------------------
instituicao = "Fatec"
nota_min = 6.0
#-----------------------------------------------------------------------

nome= input("Informe seu nome: ")
nota1 = float(input("informe a primeira nota: "))
#nota2= float(input("informe a segunda nota: "))
#print("ola", nome, "sua media é: ", (nota1+nota2)/2)
#print("Lembrando que a nota minima  \n para aprovacao no curso da ", instituicao, "é: ", nota_min)

if nota1 > 6:
    print("Voce foi aprovado")
    print("-----------")
else:
    print("Voce foi reprovado")
