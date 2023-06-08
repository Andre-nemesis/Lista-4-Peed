'''
Implemente uma lista encadeada circular e as operações básicas: 
inserir no início, inserir no final, remover do início, remover do final e exibir a lista.
'''
from listaencadeadacircular import ListaEncadeadaCircular
lista = ListaEncadeadaCircular()

num_itens = int(input('Digite a quantidade de itens que vc quer inserir: '))

for i in range(num_itens):
    x = input('Digite algo para inserir no inicio: ')
    lista.inserir_ini(x)
    z = input('Digite algo para inserir no final: ')
    lista.inserir_fin(z)
    print(f'\nMostrando a lista: {lista}')

print('Removendo no inicio.') 
print(lista.remover_ini())

print('Removendo no final.') 
print(lista.remover_fin())

print(f'Mostrando a Lista Final: {lista}')