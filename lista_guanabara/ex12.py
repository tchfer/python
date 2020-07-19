'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
preco_do_produto = float(input('Qual o preço do produto? '))
preco_final = preco_do_produto - (preco_do_produto * 5 / 100)
print('O preço original do produto é R${:.2f} e o preço ajustado com 5% de desconto é de R${:.2f}'.format(preco_do_produto, preco_final))