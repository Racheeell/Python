'''
Crie uma estrutura de dicionario onde a chave é o nome de um aluno
e os valores  sao as suas notas. Os alunos podem ter quantidade de notas diferentes

Monte um outro diferente, com base  nas informaçoes
do dicionario anterior, contendo os nomes dos alunos
como chave e os valores sao as medias  dos alunos.
'''

dicionario = {"jose": [5,7,8],
              "pedro":[6,6,9],
              "luiz":[9,10,9],
              "roberto":[7,8,9]}

media ={"jose":6.69,
        "pedro":7.0,
        "luiz":9.33,
        "roberto":8.0}

print("\n Itens do dicionario \n")
for item in dicionario.keys():
    print("\n chave do dicionario= ", item)

    lista_notas = dicionario[item]
