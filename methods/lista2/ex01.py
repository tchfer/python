'''1. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método que leia um número e o multiplique por 2, apresente o resultado.'''

def produto(num):
    produto = num * 2
    print('{} multiplicado por 2 é: {}'.format(num, produto))

def main():
    n = int(input('Digite o número que deseja multiplicar por 2 -> '))
    produto(n)

main()