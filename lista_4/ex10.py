"""Um vetor é palíndromo se ele não se alterar quando o mesmo for invertido. Por exemplo, o vetor original vo = {1, 3, 5, 2, 2, 5, 3, 1} é palíndromo, pois ele invertido é vi = {1, 3, 5, 2, 2, 5, 3, 1}, igual ao original. Escreva um algoritmo que verifique se um vetor é palíndromo, fazendo comparação de posição por posição do vetor origem (vo) com o vetor invertido(vi). Não pode usar a função reverse()."""
vetorO = []
vetorR = []
for i in range(8):
    vetorO.append(int(input("Digite um número: ")))
i = 7
while i >= 0:
    vetorR.append(vetorO[i])
    i -= 1
if vetorO == vetorR:
    print("É um palíndromo!")
else:
    print("Não é palíndromo")
