def calcular_percent_acrescimo():
  preco_antigo = float(input('Digite o preço antigo do produto, por favor -> '))
  preco_novo = float(input('Digite o preço novo do produto, por favor -> '))
  percent = ((preco_novo - preco_antigo) * 100) / preco_antigo

  print('O percentual de acréscimo é de: {}%.'.format(percent))

def main():
  calcular_percent_acrescimo()

main()

