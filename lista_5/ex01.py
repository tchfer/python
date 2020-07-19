"""preencha um vetor com seis elementos numéricos inteiros.
Mostre:

todos os números pares;
a quantidade de números pares;
todos os números ímpares;
a quantidade de números ímpares"""
n = []
nPares = []
qtdPares = 0
nImpares = []
qtdImpares = 0

for i in range(6):
    n.append(int(input(f"Digite o {i + 1}° número a ser inserido na lista: ")))
    if n[i] % 2 == 0:
        nPares.append(n[i])
        qtdPares += 1
        nPares.sort()
    else:
        nImpares.append(n[i])
        qtdImpares +=1
        nImpares.sort()
print(f"{qtdPares} dos números são pares e eles são os seguintes: {nPares}")
print(f"{qtdImpares} dos números são ímpares e eles são os seguintes: {nImpares}")
