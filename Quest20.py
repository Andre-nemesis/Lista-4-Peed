'''
Escreva uma função que receba uma lista de dicionários, 
onde cada dicionário representa um aluno com as chaves "nome" e "nota". 
A função deve retornar o nome do aluno com a maior nota.
'''
lista_dict = []
qtd_alun = int(input('Informe a quantidade de alunos que você quer inserir: '))

for i in range(qtd_alun):
    nome_aluno = input(f'Digite o nome do {i + 1}° aluno: ')
    nota_aluno = int(input('Digite a nota deste aluno: '))
    lista_dict.insert(i,{'Nome':nome_aluno,'Nota':nota_aluno})

def maior_nota(lista):
    lista_d = lista
    maior = 0
    aluno_maior_nota = []
    for i in lista_d:
        if i['Nota'] >= maior:
            maior = i['Nota']
            aluno_maior_nota = i
    return aluno_maior_nota
print(f'O aluno com maior nota foi: {maior_nota(lista_dict)}')