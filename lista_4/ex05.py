"""Faça um programa que carregue um vetor de oito elementos numéricos inteiros, calcule e mostre os números pares e suas respectivas posições."""
numP = []
numero = []
posicao = []
i = 0
while i < 8:
    numero = (int(input(f"Informe o {i + 1}º número -> ")))
    if numero % 2 == 0:
        numP.append(numero)
        posicao.append(i)
    i += 1
print(f"Os números pares são: {numP}\nSuas posições são {posicao}")
