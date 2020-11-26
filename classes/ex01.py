'''Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente.'''

class Produto: # tipo de dado
  codigo = 0
  nome = ''
  preco = 0.0

def main ():
  produto = Produto() # declaração do tipo de estrutura
  produto.codigo = int(input('Digite o código do produto -> '))
  produto.nome = input('Digite o nome do produto -> ')
  produto.preco = float(input('Por último, digite o preço do produto -> '))
  produto.preco += produto.preco * 10/100
  print("O preço do(a) {} com o acréscimo de 10% totaliza: R${} ".format(produto.nome, produto.preco))

main()