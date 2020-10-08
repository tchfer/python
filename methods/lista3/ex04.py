'''4. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia o lado de um quadrado e retorne sua área (A = lado2). Observação o número 2 significa ao quadrado.'''

def area_quad():
    a = float(input('Digite um dos lados do quadrados -> '))
    return a ** 2

def main():
    print('A área do quadrado é de: {}cm²'.format(area_quad()))

main()