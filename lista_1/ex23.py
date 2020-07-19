numero = float(input("Insira um número real para obter a parte inteira, fracionária e arredondada desse número: "))

parte_inteira = numero // 1
parte_fracionaria = numero - parte_inteira
numero_arredondado = round(numero) #funcção round arredonda número e não precisa chamar biblioteca

print("A parte inteira do número é: " , parte_inteira)
print("A parte fracionária desse número é: " , parte_fracionaria)
print("O número que inseriu arredondado é: " , numero_arredondado)
