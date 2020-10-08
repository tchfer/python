'''5. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, aplique este aumento ao salário do funcionário. Na parte principal do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a função para aplicar o aumento e gerar o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento.'''

def novo_salario(a,b):
    novo_sal = a + (a * b) / 100
    return novo_sal

def main():
    soma = 0
    soma_novo = 0
    a = float(input('Digite a porcentagem do aumento para os salários dos funcionários -> '))
    for i in range(3):
        s = float(input(f'Digite o salário do {i + 1}º funcionário -> '))
        print('O novo salário do {}º funcionário é: {:.2f}\n'.format(i + 1, novo_salario(s,a)))
        soma_novo += novo_salario(s,a)
        soma += s
        gasto = soma_novo - soma
    print('O Gasto total com os novos salários será de -> {}'.format(soma_novo))
    print('A diferença entre o que se pagava e o que será pago após o aumento será de -> {}'.format(gasto))

main()