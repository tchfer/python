"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa."""

from math import hypot
c_o = float(input('Digite o comprimento do cateto oposto: '))
c_a = float(input('Digite  o comprimento do cateto adjacente: '))
h = hypot(c_o, c_a)
print('A hipotenusa é: {:.2f}'.format(h))
# calculo bruto
"""h = (c_o ** 2 + c_a ** 2) ** (1/2)"""


