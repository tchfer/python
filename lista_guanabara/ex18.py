"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""
from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(angulo))
c = cos(radians(angulo))
t = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}\nO ângulo de {} tem o COSSENO de {:.2f}\nO ângulo de {} a TANGENTE de {:.2f}'
      .format(angulo, s, angulo, c, angulo, t))

