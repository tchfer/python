def tabela_produto():
    n = int(input('Insira um número inteiro de 1 à 9, por favor -> '))
    i = 1
    # for i in range (1, n+1):
    #     for c in range (1, i+1):
    #         produto = i * c
    #         print (produto, end = '\t')
    #     print()
    while i <= n:
        c = 1 # tem que ser declarado aqui por causa do while (não precisaria com o for)
        while c <= i:
            produto = i * c
            print('{:2}'.format(produto), end='\t')
            c += 1
        print()
        i += 1
def main():
    tabela_produto()

main()