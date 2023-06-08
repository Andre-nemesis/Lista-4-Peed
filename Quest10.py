'''
Implemente uma lista encadeada dupla e as operações básicas: 
inserir no início, inserir no final, remover do início, remover do final e exibir a lista.
'''
from listaencadeadadupla import ListaEncadeadaDupla
lista = ListaEncadeadaDupla()
num_itens = int(input('Digite a quantidade de itens que vc quer inserir: '))

for i in range(num_itens):
    print('Inserindo no inicio.')
    lista.inserir_ini(input('Digite algo: '))
    print('Inserindo no final.')
    lista.inserir_fin(input('Digite algo: '))
    print(f'\nMostrando a lista: {lista}')

print(f'Removendo no inicio: {lista.remover_ini()}') 

print(f'Removendo no final: {lista.remover_fin()}') 

print(f'Lista final: {lista}')

