"""Faça um programa que:
Receba dez números inteiros e armazene-os em um vetor
Armazene os numeros em dois vetores, um com números pares e o outro com os ímpares"""
n = []
nPares = []
nImpares = []
for i in range(5):
    n.append(int(input(f"Insira o {i + 1}° número -> ")))
    if n[i] % 2 == 0:
        nPares.append(n[i])
    else:
        nImpares.append(n[i])
nPares.sort()
nImpares.sort()
print("Os números pares são {} e os ímpares são {}".format(nPares, nImpares))
