"""Faça um programa que:
Insira dez números inteiros em um vetor
Crie um segundo vetor, substituindo os números multiplos de 3 por " * "
Exiba os dois vetores"""
n = []
mult3 = []
for i in range(5):
    n.append(int(input(f"Digite o {i + 1}º número a ser adicionado na lista -> ")))
i = 0
while i < 4:
    if n[i] % 3 == 0:
        mult3.append("*")
    i += 1
print(f"A 1ª lista ficou assim: {n}\nA 2ª lista fcou assim: {mult3}")
