salario = float(input("Insira o valor do salario mínimo: "))
quantidade_de_quilowatt = float(input("Qual a quantidade de quilowatts consumida: "))

valor_do_quilowatt = salario / 5
valor_em_reais = valor_do_quilowatt * quantidade_de_quilowatt
valor_do_desconto = valor_em_reais * 15 / 100
valor_com_desconto = valor_em_reais - valor_do_desconto

print("O valor de cada quilowatt é de: " , valor_do_quilowatt)
print("O valor a ser pago por essa residência é de: " , valor_em_reais)
print("O valor a ser pago com desconto de 15% é de: " , valor_com_desconto)
