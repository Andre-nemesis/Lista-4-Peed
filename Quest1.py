'''
Implemente uma fila simples e as operações básicas: inserir, remover e mostrar o elemento da frente.
'''
from fila import Fila
itens = int(input('Diga quantos itens você quer inserir na fila: '))
fila = Fila(itens)
for i in range(itens):
    ins = input('\ninsira algo na fila: ')
    fila.enqueue(ins)
    print(f'"{ins}" foi insrido na fila')
print(f'\nMostrando a fila: {fila}')
print(f'\n"{fila.dequeue()}" foi removido da lista')
print(f'\nProximo elemento da fila: {fila.next_element()}')



