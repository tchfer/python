'''a) Função com retorno com parâmetro. Faça um programa contendo uma função/método que leia uma matriz. Na passagem de parâmetro use quantidade de linhas e colunas e ao final retorne a matriz.

b) Faça uma função/método que mostre uma matriz. Na passagem de parâmetro use a matriz apenas. A quantidade de linhas e colunas deve ser identificada dentro da funcão, usando a função len() da linguagem Python.

c) Faça uma função que carregue a matriz do item a), some cada uma das linhas, armazenando o resultado das somas em um vetor. A seguir, multiplique cada elemento da matriz pela soma da linha e mostre a matriz resultante, conforme a figura apresentada. Para mostrar chame a função do item b).'''

def matriz(l, c):
    matriz = []
    for lin in range(l):
        linha = []
        for col in range(c):
            linha.append(int(input("Digite o valor de ['{},{}']: ".format(lin, col))))
        matriz.append(linha)
    print()
    print('Gerando matriz com valores inseridos...')
    return matriz

def qtd_l_c(m):
    for lin in range(len(m)): # lin percorre o tamanho das linhas da matriz (m)
        for col in range(len(m[lin])): # col percorre o tamanho das colunas/ vetores dentro de cada linha
            print(m[lin][col], end='\t') # imprime o resultado formatado
        print()
    print()
    return m

def somar_linhas(mat):
    soma = 0
    vetor_de_soma = []
    for l in range(len(mat)):
        for col in range(len(mat[l])):
            soma += mat[l][col]
        vetor_de_soma.append(soma)
        soma = 0

    matriz_resultante = []
    for lin in range(len(mat)):
        linha = []
        for col in range(len(mat[lin])):
            multiplica = vetor_de_soma[lin] * mat[lin][col]
            linha.append(multiplica)
        matriz_resultante.append(linha)
        linha = []
    print('Produto da Matriz')
    qtd_l_c(matriz_resultante)

def main():
    n_linhas = int(input('Digite o número linhas a ser inserida -> '))
    n_col = int(input('Digite o número colunas a ser inserida -> '))
    somar_linhas(qtd_l_c(matriz(n_linhas, n_col)))

main()