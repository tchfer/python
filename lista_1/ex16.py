horas_trabalhadas = float(input('Qual foi o número de horas trabalhadas esse mês? '))
salario_minimo = float(input('Insira o valor do salário mínimo: '))

valor_hora_trabalhada = salario_minimo / 2
salario_bruto = valor_hora_trabalhada * horas_trabalhadas
impostos = salario_bruto * 3 / 100
salario_liquido = salario_bruto - impostos

print('O salário líquido para esse mês é: ' , salario_liquido)
