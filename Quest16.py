'''
Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.
'''
lista = []
nums = int(input('Digite a quantidade de itens que você deseja inserir: '))
soma = 0
for i in range(nums):
    lista.append(int(input(f'Digite o {i + 1}° número: ')))

for i in lista:
    soma += i

print(f'A soma de todos os itens da lista é: {soma}')