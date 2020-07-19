"""Faça um programa que:
Adicione 10 números inteiros em um vetor A.
Remova todos os números menores que 0 do vetor A e os adicione no vetor B
Exiba os vetores A e B"""
vetorA = []
vetorB = []
for i in range(5):
    vetorA.append(int(input(f"Digite o {i + 1}º a ser adicionado na lista -> ")))
i = 0
while i < len(vetorA):
    if vetorA[i] < 0:
        vetorB.append(vetorA[i])
        vetorA.remove(vetorA[i])
        i -= 1
    # Aqui pode-se ver o número total de elementos dentro do vetor após cada vez que o loop roda
    print(len(vetorA))
    i += 1
print(f"O vetor A contem os itens: {vetorA}\nO vetor B contem os itens: {vetorB}")
