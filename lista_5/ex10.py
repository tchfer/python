"""Faça um programa que:
Leia um vetor com 10 números inteiros
Exiba apenas os números positivos."""
num = []
nPositivos = []
for i in range(10):
    num.append(int(input(f"Digite o {i + 1}º número: ")))
for i in range(10):
    if num[i] >= 0:
        nPositivos.append(num[i])
        nPositivos.sort()
print(f"Os números positivos digitados são: {nPositivos}")
