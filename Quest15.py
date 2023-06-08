'''
Crie um jogo de simulação de roleta utilizando uma lista encadeada circular. 
Cada elemento da lista deve representar um número da roleta, e o jogador deve apostar em um número. 
Ao girar a roleta, o programa deve percorrer a lista até encontrar o número sorteado 
e indicar se o jogador ganhou ou perdeu
'''
from listaencadeadacircular import ListaEncadeadaCircular
lista = ListaEncadeadaCircular()

#colocando números exemplos para a roleta
lista.inserir_ini(3)
lista.inserir_ini(8)
lista.inserir_ini(20)
lista.inserir_ini(54)
lista.inserir_ini(56)

num_sort = int(input('Digite um número para ser sorteado: '))

if lista.buscar(num_sort):
    print('Parabéns você ganhou!')
else:
    print('Que pena você perdeu ;-;')
