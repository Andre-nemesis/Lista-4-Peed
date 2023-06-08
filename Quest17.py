'''
Implemente uma função que receba uma lista de strings e 
retorne uma nova lista contendo apenas as strings que possuem mais de 5 caracteres.
'''
lista = []
lista_5carter = []
nums = int(input('Digite a quantiade de palavras que você deseja inserir na lista: '))

for i in range(nums):
    lista.append(input(f'Digite a {i + 1}° palavra: '))

for palavra in lista:
    if len(palavra) > 5:
        lista_5carter.append(palavra)

print(f'Lista com as palavras que possuem + de 5 caracteres: {lista_5carter}')