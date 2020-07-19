"""Faça um programa que:
Preencha um vetor com quinze números,
Determine e mostre:
O maior número e a posição por ele ocupada no vetor;
O menor número e a posição por ele ocupada no vetor."""
n = []
maiorN = 0
menorN = 0
posicaoMaior = 0
posicaoMenor = 0
for i in range(5):
    n.append(int(input(f"Digite o {i + 1}° número: ")))
    if i == 0:
        maiorN = n[i]
        menorN = n[i]
    if n[i] > maiorN:
        maiorN = n[i]
        posicaoMaior = i
    if n[i] < menorN:
        menorN = n[i]
        posicaoMenor = i
print(f"O maior número é {maiorN} e está na posição {posicaoMaior}\nO menor é o número {menorN} e está na posição {posicaoMenor}")
