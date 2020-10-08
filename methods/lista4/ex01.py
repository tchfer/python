'''1. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba por parâmetro um número e o multiplique por 2, retorne e apresente o resultado da função.'''

def produto(b):
    x = b * 2
    return x
def main():
    n = int(input('Digite um número -> '))
    print('{} x 2 = {}'.format(n,produto(n)))

main()
