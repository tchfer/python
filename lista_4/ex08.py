"""Criar um algoritmo que a partir de um vetor de 10 elementos inteiros, crie outros dois vetores, um deles armazenará os elementos positivos e o outro os negativos e ao final apresente-os."""
numP = []
numN = []
num = []

for i in range(4):
    num.append(int(input("Digite um número inteiro: ")))
    if num[i] >= 0:
        numP.append(num[i])
    else:
        numN.append(num[i])
print(f"Os números positivos são {numP} e os negativos são {numN}")