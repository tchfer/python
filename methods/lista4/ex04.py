'''4. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento via parâmetro, aplique este aumento a um salário de um funcionário, retorne e apresente o novo salário.'''

def novo_salario(a,b):
    novo_sal = a + (a * b) / 100
    return novo_sal

def main():
    
    salario = float(input('Digite o salário do funcionário -> '))
    aumento = float(input('Digite a porcentagem do aumento -> '))
    print('\nO novo salário é: R${:.2f}'.format(novo_salario(salario, aumento)))

main()