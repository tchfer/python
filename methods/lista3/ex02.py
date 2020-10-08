'''2. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método para subtrair dois números, retornar o resultado e o apresentando.'''

def sub():
    n1 = int(input('Digite um número inteiro, por favor -> '))
    n2 = int(input('Digite o número a ser subtraído do 1º -> '))
    return print('{} - {} = {}'.format(n1, n2, n1 - n2))

def main():
    sub()

main()