"""Faça um programa que:
Preencha um vetor com dez números reais (float)
Calcule e mostre:
A quantidade de números negativos
A soma dos números positivos desse vetor. Não use a função sum()."""
n = []
neg = 0
somaP = 0
for i in range(5):
    n.append(float(input("Digite o {}° número da lista: ".format(i + 1))))
    if n[i] < 0:
        neg += 1
    else:
        somaP += n[i]
print(f"Essa lista contém {neg} números negativos.\nOs números positivos dela somam {somaP} ")
