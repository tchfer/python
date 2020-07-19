"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""
dias = int(input('Qual o número de dias que o carro ficou alugado? '))
km = float(input('Qual o número de kilometros rodados nesses {} dias? '.format(dias)))
total = (dias * 60) + (km * 0.15)
print('O total a pagar pelo carro é de R${}'.format(total))