salario = float(input('Coloque o valor do seu salário aqui: '))
cheque1 = float(input('Qual foi o valor emitido no primeiro cheque? '))
cheque2 = float(input('Qual foi o valor emitido no segundo cheque: '))

cpmf_cheque1 = cheque1 * 0.038 / 100 '''Não lembro se é a forma certa de 3,8 em decimal'''
saque1 = cheque1 + cpmf_cheque1
cpmf_cheque2 = cheque2 * 0.038 / 100 '''Não lembro se é a forma certa de 3,8 em decimal'''
saque2 = cheque2 + cpmf_cheque2
saldo = salario - saque1 - saque2

print('Seu saldo atual é de: ' , saldo)
