'''3. Crie uma função que receba uma matriz e retorne True se a matriz for simetrica, em caso contrario retorna False. Uma matriz é considerada simétrica quando a quantidade de linhas é igual a d coluna.'''
def criar_matriz(l, c):
    matriz = []
    for lin in range(l):
        linha = []
        for col in range(c):
            linha.append(int(input("Digite o valor de ['{},{}']: ".format(lin, col))))
        matriz.append(linha)
    if l == c:
        return True
    return False

def main():
    n_linhas = int(input('Digite o número linhas a ser inserida -> '))
    n_col = int(input('Digite o número colunas a ser inserida -> '))
    print(criar_matriz(n_linhas, n_col))
    # resultado = criar_matriz(n_linhas, n_col)
    # print(resultado)
    # if criar_matriz(n_linhas, n_col):
    # if resultado == True: # desnecessário comparar true == true (resultado já tem valor de true ou false)
    #     print('É simétrica')
    # else:
    #     print('Não é simétrica')
        
main()