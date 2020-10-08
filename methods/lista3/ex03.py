'''3. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia a base e a altura de um triângulo e retorne/apresente sua área (A = (base x altura)/2).'''

def area():
    b = float(input('Digite a medida da base do triângulo '))
    a = float(input('Digite a medida da altura do triângulo '))
    area = (b * a) / 2
    return area

def main():
    print('A área do triângulo com as medidas que você escolheu é de: {}cm²'.format(area()))

main()