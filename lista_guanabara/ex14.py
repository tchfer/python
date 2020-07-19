"""Escreva um programa que converta uma temperatura digitada em °C para °F"""
temp = float(input('Informe a temperatura em °C: '))
conversao = ((temp * 9) / 5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(temp, conversao))
