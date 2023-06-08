'''
Crie um programa que exibe ao usuário um menu com as seguintes opções: 
adicionar número na fila; remover número da fila; tamanho da fila; mostrar fila.
Todas as opções devem funcionar conforme a ação que ela descreve. 
'''
from fila import Fila
fila = Fila()

def menu():
    print('''
    Menu de opções da fila:
    1 - Adicionar número na fila
    2 - Remover número da fila
    3 - Tamanho da fila
    4 - Mostrar fila
    5 - Sair
    ''')
    op = int(input('\nDigite a sua escolha de opção: '))
    funcoes(op)

def funcoes(op): 
    if op == 1:
        fila.enqueue(int(input('Digite um número: ')))
        menu()
    elif op == 2:
        if not fila.is_empty():
            print(f'O item "{fila.dequeue()}" foi removido!')
        else:
            print('A fila está vazia.')
            menu()
        menu()
    elif op == 3:
        if not fila.is_empty():
            print(f'O tamanho da fila é: {fila.tamanho()}')
        else:
            print('A fila está vazia.')
            menu()
        menu()
    elif op == 4:
        if not fila.is_empty():
           print(fila)
        else:
            print('A fila está vazia.')
            menu()
        menu()
    elif op == 5:
        print('Até breve!')
        exit()
    else:
        print('Opção Inválida. Tente novamente.')
        menu()

menu()