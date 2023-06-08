'''
Crie uma função que receba duas listas de números e 
retorne uma nova lista contendo apenas os elementos que estão presentes em ambas as listas.
'''
lista1 = []
lista2 = []
lista3 = []

nums = int(input('Digite a quantiade de números que você deseja inserir na lista: '))

for i in range(nums):
    lista1.append(int(input(f'Digite o {i + 1}° número na 1° lista: ')))

for i in range(nums):
    lista2.append(int(input(f'Digite o {i + 1}° número na 2° lista: ')))

for numero in lista1:
    if numero in lista2:
        lista3.append(numero)
        
print(f'Lista com os números em ambas as listas: {lista3}')