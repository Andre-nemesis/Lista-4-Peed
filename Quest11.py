'''
Escreva um programa que leia uma lista de nomes e crie uma lista 
encadeada dupla com esses nomes em ordem alfabética. 
'''
from listaencadeadadupla import ListaEncadeadaDupla
lista = []
lista_encad = ListaEncadeadaDupla()
qtd_nomes = int(input('Digite a quantidade de nomes que você deseja inserir: '))

for i in range(qtd_nomes):
    lista.append(input(f'Digite o {i + 1}° nome: '))
    
lista.sort(reverse=True)

for ind in lista:
    lista_encad.inserir_ini(ind)

print(lista_encad)
