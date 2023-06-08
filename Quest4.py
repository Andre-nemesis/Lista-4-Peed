'''
Escreva um programa que leia uma frase do usuário e verifique se ela é um palíndromo 
(ou seja, pode ser lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda). 
Utilize uma fila para armazenar os caracteres da frase.
'''
from fila import Fila

def polindromo(frase):
    lista_aux = []
    fila = Fila()
    string = ""
    for letra in frase:
        fila.enqueue(letra)
    while not fila.is_empty():
        lista_aux.append(fila.dequeue())
    lista_aux.reverse()
    for letra in lista_aux:
        fila.enqueue(letra)
    while not fila.is_empty():
        string += fila.dequeue()
    if string == frase:
        return True
    else:
        return False

s = input('Digite uma palavra ou uma frase para verificar se ela é um políndromo: ')
print(polindromo(s))