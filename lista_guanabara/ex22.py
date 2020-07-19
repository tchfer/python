'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

# a funcção strip já guarda o valor da string sem os espaços
n = str(input("Digite seu nome completo -> ")).strip()
print("*" * 30)
# (variável.upper/lower()) vai transformar tudo que foi digitado em maiúsculo ou minúsculo
print("Seu nome em letras maiúsculas fica: {}".format(n.upper()))
print("Seu nome em letras minúsculas fica: {}".format(n.lower()))
print("O seu nome completo contém {} letras".format(len(n) - n.count(' ')))
# transforma a string em uma lista com cada elemento tendo uma posição de índice, começando por 0
listaNomes = n.split()
# imprime o primeiro elemento[0] da lista e fala o tamanho do elemento [0] - 0, 1, 2, 3, 4, 5, 6
print("O seu primeiro nome é {} e contém {} letras".format(listaNomes[0], len(listaNomes[0])))
# outra forma de mostrar é encontrar o primeiro espaço na string e contar tudo que vem antes dele
# print("Seu primeiro nome tem {} letras".format(n.find(" ")))
