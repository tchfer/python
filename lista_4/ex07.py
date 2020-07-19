"""Faça um algoritmo que calcule e apresente a média de alturas superior a 1.80. Informe também quantos e quais (posição) são os alunos."""
altura = []
quantidadeMaior = 0
somaAltura = 0
posicaoMaior = []
nAlturas = int(input("Quantas alturas gostaria de digitar? "))
i = 0
while i <= nAlturas - 1:
    altura.append(float(input(f"Informe a altura da {i + 1}a pessoa: ")))
    if altura[i] > 1.8:
        quantidadeMaior += 1
        posicaoMaior.append(i)
        somaAltura += altura[i]
    i += 1
mediaAltura = somaAltura / quantidadeMaior
print(f"A média de pessoas maior que 1.8 M é: {mediaAltura}")
print(f"A quantidade de pessoas que tem mais de 1.8 é de: {quantidadeMaior} pessoas")
print(f"Posição da altura maior que 1.8 na lista: {posicaoMaior}")
