'''
Escreva um programa que leia uma lista de números inteiros e 
crie uma lista encadeada circular com esses números em ordem crescente. 
Sua classe lista deve conter métodos/funções para mostrar o primeiro e ultimo elemento da lista. 
'''
from listaencadeadacircular import ListaEncadeadaCircular

lista = ListaEncadeadaCircular()
lista_aux = []
num_itens = int(input('Digite a quantidade de itens que vc quer inserir: '))

for i in range(num_itens):
    lista_aux.append(int(input(f'Digite o {i+1}° item: ')))
lista_aux.sort(reverse=True)
for i in lista_aux:
    lista.inserir_ini(i)
print(f'Mostrando a Lista Final: {lista}')
print(f'Mostrando o primerio elemento: {lista.prim_item()}')
print(f'Mostrando o último elemento: {lista.ult_item()}')