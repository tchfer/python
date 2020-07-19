deposito = float(input('Quanto gostaria depositar? '))
juros = float(input('Qual o valor da porcentagem para rendimento? '))

rendimento = deposito * juros / 100
total = deposito + rendimento

print('O valor após a porcentagem de juros sobre o depósito esse primeiro mês é de: ' , rendimento)
print('O valor do depósito mais os juros é de: ' , total)
