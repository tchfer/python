"""Faça um programa que carregue um vetor de dez elementos que contenha o nome de pessoas e outro que contenha o peso,encontre qual a pessoa mais gorda e mais magra e apresente o nome o peso das mesmas."""
nome = []
peso = []
i = 0
while i <= 2:
    nome.append(str(input(f"Informe o nome da pessoa ({i + 1}): ")))
    peso.append(float(input(f"Informe o peso da pessoa ({i + 1}): ")))
    i += 1
nome_maior = ' '
nome_menor = ' '
peso_maior = 0
peso_menor = 500
for i in range(3):
    if peso[i] >= peso_maior:
        peso_maior = peso[i]
        nome_maior = nome[i]
    if peso[i] <= peso_menor:
        peso_menor = peso[i]
        nome_menor = nome[i]
print(f"A pessoa com maior peso nessa lista tem {peso_maior} KG e seu nome é {nome_maior}")
print(f"A pessoa com menor peso nessa lista tem {peso_menor} KG e seu nome é {nome_menor}")
