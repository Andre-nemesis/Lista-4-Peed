'''
Escreva um programa que leia uma lista de números inteiros e 
crie uma lista encadeada simples com esses números em ordem inversa.
'''
from listasimples import ListaEncadeada
num_itens = int(input('Digite a quantidade de números que você quer inserir: '))
lista = ListaEncadeada()
lista_inv = ListaEncadeada()
for i in range(num_itens):
    lista.inserir_fin(int(input(f'Digite o {i + 1}° número: ')))
    
def inverter():
    while not lista.is_empyt():
        lista_inv.inserir_fin(lista.remover_fin())
    return lista_inv

print(f'Lista Invertida: {inverter()}')