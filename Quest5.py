'''
Implemente uma fila circular utilizando um vetor e as operações básicas.
'''
from filacircular import FilaCircular
filacir = FilaCircular()
print('Iserindo elemento:')
x = int(input('Diga quantos itens você quer adicionar: '))
for i in range(x):
    filacir.enqueue(input(f'Diga o {i + 1}° item: '))

print(f'Mostrando a fila: {filacir}')
print(f'\nRemovendo elemento: {filacir.dequeue()}')
