"""Criar um algoritmo que leia dados para um vetor de 100 elementos inteiros, imprimir o maior, o menor, o percentual de números pares e a média dos elementos do vetor. 
Obs.: percentual = quantidade contada * 100 / quantidade total. Não devem utilizar as funções: min(), max() e sum()."""
elementos = []
elementoMaior = 0
elementoMenor = 0
pares = []
qtdP = 0
somaElementos = 0
for i in range(6):
    elementos.append(int(input("Digite o número desejado: ")))
    if i == 0:
        elementoMenor = elementos[i]
        elementoMaior = elementos[i]
    if elementos[i] > elementoMaior:
        elementoMaior = elementos[i]
    if elementos[i] < elementoMenor:
        elementoMenor = elementos[i]
    if elementos[i] % 2 == 0:
        pares.append(elementos[i])
        qtdP += 1
    percent = qtdP * 100 / (i + 1)
    somaElementos += elementos[i]
media = somaElementos / (i + 1)
print(f"O elemento maior da lista é {elementoMaior}, o menor é {elementoMenor}, a média dos elementos é {media} e {percent:.2f}% deles são pares")
