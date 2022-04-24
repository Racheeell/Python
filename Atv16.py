
#dicionario
notas_classe = { "jose": [5,7,8] ,
                 "pedro":[6,6,9] ,
                 "luiz":[9,10,9] ,
                 "roberto":[9,10,9,10] }
#os valores sao uma lista de numeros
print(notas_classe)

media_aluno = {}
for aluno in notas_classe.keys():
    print("Aluno:", aluno)

#-------------------------------------------------------------
for aluno in notas_classe.keys():
    print("\n Aluno:", aluno)

    lista_notas = notas_classe[aluno]
    print("lista de notas: ",lista_notas )
    soma = 0
    qtde = 0
    media = 0
    for nota in lista_notas:
        print("Nota:",nota )
        soma += nota
        qtde += 1
    if qtde > 0:
        media = soma / qtde
    print("Media=", media)
    s_media = "%.2f" % media
    media = float(s_media)
    media_aluno[aluno] = media
print("Medias dos alunos:")
print(media_aluno)





maior = 0
nome = ""
for aluno in media_aluno:
    media = media_aluno[aluno]
    if media > maior:
        maior = media
        nome = aluno
print("\n\n============== [ Maior média ] =================================")
print("Aluno:", nome)
print("media:", maior)
print("================================================================")

print("\n ***   B. Maior Media  ***** ")
val_medias = media_aluno.values()
print(max(val_medias))