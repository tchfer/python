salario = float(input('Digite o valor base do seu salário: '))

gratificacao = salario * 5 / 100
imposto = salario * 7 / 100
salario_liquido = salario + gratificacao - imposto

print('O valor do seu salário liquido é: ' , salario_liquido)
