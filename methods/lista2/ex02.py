'''2. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método para subtrair dois números e apresentar o resultado.'''

def subtrair(num1, num2):
    subtracao = num1 - num2
    print('{} - {} = {}'.format(num1, num2, subtracao))

def main():
    n1 = int(input('Digite o primeiro número -> '))
    n2 = int(input('Digite o segundo número -> '))
    subtrair(n1, n2)

main()
