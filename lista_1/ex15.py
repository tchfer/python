preco_de_fabrica = float(input('Qual o preço de fábrica do carro? '))
percent_lucro_distribuidor = float(input('Qual o valor percentual de lucro do distribuidor?'))
percent_imposto = float(input('Insira o valor percentual da taxa de imposto: '))

lucro_distribuidor = preco_de_fabrica * percent_lucro_distribuidor / 100
valor_imposto = preco_de_fabrica * percent_imposto / 100
preco_final = preco_de_fabrica + lucro_distribuidor + valor_imposto

print('O Valor de lucro do distribuidor é de: ' , lucro_distribuidor)
print('A taxa de imposto que vai ser paga por esse carro é de: ' , valor_imposto)
print('O valor do carro com o lucro do distribuidor e taxa de imposto é: ' , preco_final)
