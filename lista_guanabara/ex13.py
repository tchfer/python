"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""
salario = float(input('Qual é o salário do funcionário? R$'))
novo_salario = salario + (salario * 15 / 100)
print('O funcionário que ganhava R${:.2f}, com 15% de aumento passa a ganhar R${:.2f}'.format(salario, novo_salario))
