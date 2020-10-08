'''1. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que leia uma matriz. Na passagem de parâmetro use quantidade de linhas e colunas e ao final retorne a matriz. Na função main apresenta a matriz preenchida'''

def criar_matriz(l, c):
    matriz = []
    for lin in range(l):
        linha = []
        for col in range(c):
            linha.append(int(input("Digite o valor de ['{},{}']: ".format(lin, col))))
        matriz.append(linha)
    return matriz

def main():
    n_linhas = int(input('Digite o número linhas a ser inserida -> '))
    n_col = int(input('Digite o número colunas a ser inserida -> '))
    print(criar_matriz(n_linhas, n_col))

main()