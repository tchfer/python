'''6. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne/mostre o valor booleano True para par e False para ímpar.'''

def par_impar():
    n = int(input('Digite um número inteiro -> '))
    return print(bool(n % 2 == 0))

def main():
    par_impar()

main()