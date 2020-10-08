'''4. Crie uma função que receba como parâmetro duas matrizes a_mat e b_mat, deve retornar a matriz resultante após o produto (multiplicação) de a_mat por b_mat. Deve-se avaliar antes da multiplicação que o número de colunas de a_mat é igual ao número de linhas de b_mat. Use na main, a chamada da função mostrar valores de uma matriz.'''

def simetria(a,b): 
    if len(a[0]) == len(b):
        c = []
        for l in range (len(a)): 
            c.append([]) 
            for i in range (len(b[0])):
                c[l].append(0)
                for m in range (len(a[0])):
                    c[l][i] += a[l][m] * b[m][i]
        return c
    else:
        return False

def main():
    num_linhas = int(input('Digite o número de linhas da primeira matriz -> '))
    num_colunas = int(input('Digite o número de colunas da primeira matriz -> '))
    a = []
    for lin in range(num_linhas): 
        linha = []
        for col in range(num_colunas):
            linha.append(int(input('Digite o valor de [{},{}] -> '.format(lin, col))))
        a.append(linha)
    num_linhas = int(input('Digite o número de linhas da segunda matriz -> '))
    num_colunas = int(input('Digite o número de colunas da segunda matriz -> '))
    b = []
    for lin in range(num_linhas): 
        linha = []
        for col in range(num_colunas):
            linha.append(int(input('Digite o valor de [{},{}] -> '.format(lin, col))))
        b.append(linha)
    
    print(simetria(a,b))  

main()