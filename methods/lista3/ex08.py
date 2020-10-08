'''8. (Função com retorno sem parâmetro) Faça uma função/método que leia e armazene 5 elementos inteiros no vetor A, deverá ser gerado um vetor B, de mesmo tamanho, que armazenará o fatorial de cada elemento de A. Retorne/apresente o vetor B.'''

def vet_fatorial():
    vetA = []
    vetB = []
    f = 1
    for i in range(5):
        vetA.append(int(input(f'Digite o {i + 1}º número -> ')))
    for j in range(1, vetA[i] + 1):
        f = f * j
        vetB.append(f)
    return vetB

def main():
    print(vet_fatorial())

main()