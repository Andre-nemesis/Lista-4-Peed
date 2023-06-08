'''
Escreva um programa que leia uma sequência de números inteiros e 
insira-os em uma fila até que um número negativo seja digitado. 
Em seguida, remova todos os elementos da fila e exiba-os na ordem em que foram inseridos.
'''
from fila import Fila
fila = Fila()
num = float('inf')
while num>=0:
    num = int(input('Digite um número: '))
    if num >= 0:
        fila.enqueue(num)
    else:
        break
while not fila.is_empty():
    print(f'{fila.dequeue()}',end=",")
