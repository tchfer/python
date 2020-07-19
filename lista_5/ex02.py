"""Faça um programa que:
Preencha um vetor com sete números inteiros,
Calcule (%) e mostre os números:
Múltiplos de 2;
Múltiplos de 3;
Múltiplos de 2 e de 3."""
n = []
divPor2 = []
divPor3 = []
divPorAmbos = []
qtdPares = 0
qtdImpares = 0
qtdAmbos = 0
percentPares = 0
percentImpares = 0
perCentAmbos = 0
for i in range(7):
    n.append(int(input(f"Digite o {i + 1}° número: ")))
    if n[i] % 2 == 0:
        divPor2.append(n[i])
        qtdPares += 1
    if n[i] % 3 == 0:
        divPor3.append(n[i])
        qtdImpares += 1
    if n[i] % 2 == 0 and n[i] % 3 == 0:
        divPorAmbos.append(n[i])
        qtdAmbos += 1
    percentPares = qtdPares * 100 / (i + 1)
    percentImpares = qtdImpares * 100 / (i + 1)
    perCentAmbos = qtdAmbos * 100 / (i + 1)
    divPor2.sort()
    divPor3.sort()
    divPorAmbos.sort()
print(f"A porcentagem de números pares é: {percentPares:.2f}%\nA de ímpares é: {percentImpares:.2f}%\nE a porcentagem de ambos é {perCentAmbos:.2f}%")
print(f"Os múltiplos de 2 são {divPor2}, os de 3 são {divPor3} e os de ambos são {divPorAmbos}")
