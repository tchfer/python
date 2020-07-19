anoAtual = int(input("Qual o ano atual? "))
si = 1000
perCentAnual = 1.5 / 100
aumento_do_ano = si * perCentAnual
salario_do_ano = si + aumento_do_ano
ano = 2007
while ano <= anoAtual:
    perCentAnual *= 2
    aumento_do_ano = salario_do_ano * perCentAnual
    salario_do_ano += aumento_do_ano
    ano += 1
print("O salário referente ao ano de {} é de R${:.2f} ".format(ano - 1, salario_do_ano))

# anoAtual = int(input("Qual o ano atual? "))
# si = 1000
# perCentAnual = 1.5 / 100
# aumento_do_ano = si * perCentAnual
# salario_do_ano = si + aumento_do_ano
#
# for ano in range(2007, anoAtual + 1):
#     perCentAnual *= 2
#     aumento_do_ano = salario_do_ano * perCentAnual
#     salario_do_ano += aumento_do_ano
# print("O salário referente ao ano de {} é de R${:.2f} ".format(ano, salario_do_ano))

