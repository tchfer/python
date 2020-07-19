'''Crie um programa
que leia quanto
dinheiro uma pessoa
tem na carteira e
mostre quantos
Dólares ela pode
comprar.'''
real = float(input('Quanto dinheiro você tem na carteira? R$'))
print()
dolar = real / 5.20
euro = real / 5.69
libra = real / 6.53
print('Na data de hoje, com R${:.2f} você consegue comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você consegue comprar €{:.2f}'.format(real, euro))
print('E com R${:.2f} você consegue comprar £{:.2f}'.format(real, libra))
