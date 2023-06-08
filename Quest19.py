'''
Implemente uma função que receba uma lista de palavras e 
retorne a palavra mais longa presente na lista.
'''
lista = []
aux = 0
palavrafin = ""
nums = int(input('Digite a quantiade de palavras que você deseja inserir na lista: '))

for i in range(nums):
    lista.append(input(f'Digite a {i + 1}° palavra: '))

for palavra in lista:
    if aux < len(palavra):
        aux = len(palavra)
        palavrafin = palavra
print(f'A maior palavra foi: {palavrafin}')