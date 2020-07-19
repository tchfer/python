salario = float(input('Coloque o valor do salário base: '))
per_imposto = float(input('Entre a porcentagem do imposto a ser descontado do salário: '))

imposto = salario * per_imposto / 100
salario_liquido = salario + 50 - imposto

print('O salário líquido é: ' , salario_liquido)
