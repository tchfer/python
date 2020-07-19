'''Escreva um
programa que leia um
valor em metros e o
exiba convertido em
centímetros
e
milímetros.'''
metros = float(input('Digite uma distância em metros: '))
cm = metros * 100
mm = metros * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm '. format(metros, cm, mm))