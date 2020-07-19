salario = float(input('Insira o valor do seu salário: '))
percentual = float(input('Agora insira o valor percentual do aumento dele: '))

aumento = salario * percentual / 100

print('O valor de aumento do seu salário é de: ' , aumento)

novo_salario = salario + aumento

print('O valor do seu salário com o aumento de', percentual ,'% é de:', novo_salario)
