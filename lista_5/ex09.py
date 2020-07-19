"""Faça um programa que:
Preencha dois vetores com 10 números cada
Faça a multiplicação dos números na mesma posição V1[0] * V2[0] ...
O resultado deverá ser inserido no terceiro vetor"""
v1 = []
v2 = []
v3 = []
i = 0
while i < 3:
    v1.append(int(input(f"Digite o {i + 1}º número para a 1ª lista de números-> ")))
    v2.append(int(input(f"Digite o {i + 1}º número para a 2ª lista de números-> ")))
    print("-=" * 50)
    v3.append(v1[i] * v2[i])
    i += 1
for i in range(3):
    print(f"{v1[i]} x {v2[i]} = {v3[i]}")
