'''
Considere um supermercado que atende a inúmeros clientes.
Cada cliente possui um número de identificação único e chega 
ao supermercado em momentos distintos. Implemente um sistema que receba a 
chegada de clientes e mantenha uma fila para o atendimento. 
A cada hora*, o sistema deve atender o próximo cliente da fila e 
imprimir o número de identificação desse cliente.
'''
from fila import Fila
import time
import numpy as np
fila = Fila()
fila_h = Fila()

num_client = int(input('Digite a quantidade de clintes que estarão na fila do mercado: '))

def cliente():
    x = np.random.randint(0,100)
    fila.enqueue(x)
    fila_h.enqueue(time.strftime("%H:%M:%S"))

for i in range(num_client):
    cliente()
    time.sleep(1)

print(f'\nFila de clientes por seus códigos: {fila}\n')

while not fila_h.is_empty():
    h_cliente = fila_h.dequeue()
    cod_cliente = fila.dequeue()
    print(f'No horario {h_cliente} o o cliente com o código: {cod_cliente} chegou\nNo horario {time.strftime("%H:%M:%S")} o cliente do código {cod_cliente} foi atendido\n')
    time.sleep(5)