'''1. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia um número e o multiplique por 2 retornando o resultado, apresente o resultado da função.'''

# def produto():
#     n = float(input('Digite um número -> '))
#     return n * 2

# def main():
#     print('Número x 2 = {}'.format(produto()))

# main()

def produto():
    n = int(input('Digite um número inteiro -> '))
    return print('{} x 2 = {}'.format(n, n * 2))

def main():
    produto()

main()