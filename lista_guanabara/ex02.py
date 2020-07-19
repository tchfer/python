"""Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data
formatada """
dia = int(input('Insira o dia que você nasceu: '))
mes = int(input('Agora insira o mês: '))
ano = int(input('Por último, insira o ano de nascimento: '))
print('A sua data de nascimento formatada é: {}/{:02d}/{}'.format(dia, mes, ano)) # {:02d] insere um zero de deixa
# com dois digitos decimais
