'''5. Crie uma função que a partir de uma matriz 4x4 mostre a soma dos elementos da diagonal principal. Mostre também a soma dos elementos que estão acima da diagonal principal. Diagonal principal é identificada pelos elementos que estão no mesmo índice de linha e coluna, exemplo, [1][1], [2][2], etc.'''
# as partes que estão comentadas tinha sido feito com o usuário colocando o número de 
# linhas e colunas que queria trabalhar, mas o exercício pede um número fixo de 4x4
# então a função sem parametros já é o bastante nesse caso

# def somar_diagonal(linha,coluna):
def somar_diagonal():
    soma_acima = 0
    soma = 0
    matriz = []
    # for c in range(linha):
    for c in range(4):
        linhas = []
        for i in range(4):
        # for i in range(coluna):
            elementos = int(input('Digite o {}º elemento da {}ª linha: '.format(i + 1, c + 1)))
            if c == i:
                soma += elementos
            linhas.append(elementos)
        matriz.append(linhas)

    print('\n\033[0;32m*****Matriz gerada*****')
    # for l in range (linha):
    for l in range (4):
        # for c in range (coluna):
        for c in range (4):
            if c > l:
                soma_acima += matriz[l][c]
            print(matriz[l][c] , end='   ')
        print()
    return print('A soma da diagonal principal é: {}\nA soma a soma dos números acima da diagonal é: {}\033[m'.format(soma, soma_acima))

def main():
    # m = int(input('Digite o número de linhas que quer inserir na matriz -> '))
    # n = int(input('Agora digite o número de colunas -> '))
    # somar_diagonal(m, n)
    somar_diagonal()

main()