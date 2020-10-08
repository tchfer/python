'''7. (Função sem retorno com parâmetro) Faça uma função/método sem parâmetro, para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se o valor é par ou ímpar.'''

def valor():
    n = float(input('Insira um número qualquer -> '))
    par_impar(n)

def par_impar(num):
    if num % 2 == 0:
        print('O número {} é par'.format(num))
    else:
        print('O número {} é ímpar'.format(num))

def main():
    valor()

main()
