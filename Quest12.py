'''
Crie uma agenda telefônica utilizando uma lista encadeada dupla. 
Cada entrada na agenda deve conter o nome e o número de telefone de uma pessoa. 
Implemente as operações de inserir, remover e buscar uma pessoa na agenda.
'''
from listaencadeadadupla import ListaEncadeadaDupla
lista = ListaEncadeadaDupla()

def menu():
    print('''
    Menu para a Agenda Telefônica
    0 - Sair
    1 - Inserir Pessoa
    2 - Remover Pessoa
    3 - Buscar Pessoa
    ''')
    op = int(input('Digite uma opção acima: '))
    funcoes(op)

def funcoes(op):
    if op == 0:
        print('Até Breve!')
        exit()
    elif op == 1:
        lista.inserir_fin(input('Digite o nome da pessoa e seu número: ').split())
        menu()
    elif op == 2:
        if lista.is_empyt():
            print('A lista está vazia')
            menu()
        else:
            print(f'A pessoa {lista.remover_ini()} e seu número foram removidos!')
            menu()
    elif op == 3:
        aux2 = False
        pessoa = input('Digite o nome da pessoa que você quer procurar: ')
        lista_aux = ListaEncadeadaDupla()
        while not lista.is_empyt():
            aux = lista.remover_ini()
            lista_aux.inserir_ini(aux)
            if aux[0] == pessoa:
                aux2 = True
                break
        if aux2:
            while not lista_aux.is_empyt():
                lista.inserir_ini(lista_aux.remover_ini())
            print('A pessoa {} está na lista.'.format(pessoa))
            menu()
        else:
            while not lista_aux.is_empyt():
                lista.inserir_ini(lista_aux.remover_ini())
            print('A pessoa {} não está na lista.'.format(pessoa))
            menu()
    else:
        print('Opção inválida, tente novamente.')   
        menu()

menu()