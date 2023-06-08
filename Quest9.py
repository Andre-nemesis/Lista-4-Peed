'''
Um banco precisa armazenar as informações dos clientes em uma lista encadeada simples. 
Cada cliente possui nome, número da conta e saldo. Implemente as operações de inserir, 
remover e pesquisar um cliente na lista. A cada operações, mostrar a lista em “formado de tabela”.
'''

from listasimples import ListaEncadeada

def menu():
    print('''
    Menu do Banco Exemeplo S.A
    0 - Sair
    1 - Inserir Pessoa
    2 - Remover Pessoa
    3 - Buscar Pessoa
    ''')
    op = int(input('Digite uma opção acima: '))
    funcoes(op)

lista = ListaEncadeada()

def mostrar_tab():
    lista2 = ListaEncadeada()
    print('|Nome do Cliente|Número da Conta|Saldo\t|')
    while not lista.is_empyt():
        aux = lista.remover_ini()
        print(f'|\t{aux[0]}\t|\t{aux[1]}\t|{aux[2]}\t|')
        lista2.inserir_ini(aux)
    while not lista2.is_empyt():
        lista.inserir_ini(lista2.remover_ini())

def funcoes(op):
    if op == 0:
        print('Até Breve!')
        exit()
    elif op == 1:
        mostrar_tab()
        lista.inserir_fin(input('Digite o primeiro nome do cliente, número da conta e o saldo separado por um espaço: ').split())
        menu()
    elif op == 2:
        if lista.is_empyt():
            print('A lista está vazia!')
            menu()
        mostrar_tab()
        print(f'A pessoa {lista.remover_ini()} e suas informações da conta foram removidas!')
        menu()
    elif op == 3:
        if lista.is_empyt():
            print('A lista está vazia!')
            menu()
        mostrar_tab()
        pessoa = input('Digite o nome da pessoa que você quer procurar: ')
        lista_aux = ListaEncadeada()
        aux2 = False

        while not lista.is_empyt():
            var_aux = lista.remover_fin()
            if var_aux[0] == pessoa:
                aux2 = True
            lista_aux.inserir_fin(var_aux)

        while not lista_aux.is_empyt():
            lista.inserir_fin(lista_aux.remover_fin())

        if aux2:
            print('A pessoa {} está na lista.'.format(pessoa))
            menu()
        else:
            print('A pessoa {} não está na lista.'.format(pessoa))
            menu()
    else:
        print('Opção inválida, tente novamente.')   
        menu()

menu()