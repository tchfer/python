'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome'''
n = str(input("Digite seu nome completo: ")).strip()
print("Seu nome tem 'Silva'? {} ".format('SILVA' in n.upper()))
