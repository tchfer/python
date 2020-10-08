'''2. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado.'''

def somar(a,b):
    soma = a + b
    return soma

def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print('{} + {} = {}'.format(n1, n2, somar(n1,n2)))

main()