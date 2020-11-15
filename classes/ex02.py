'''Elabore uma estrutura para representar um produto (código, nome, preço). Cadastre 5 produtos, use vetor/lista. Aplique 10% de aumento no preço do produto e apresente todos os dados do preço.'''

class Produto: # tipo de dado
  codigo = 0
  nome = ''
  preco = 0.0

def main ():
  vet_precos = []
  print('\033[0;32mLendo os dados...\033[m')
  print()
  for i in range(2):
    produto = Produto() # declaração do tipo de estrutura
    produto.codigo = int(input('Digite o código do {}º produto -> '.format(i + 1)))
    produto.nome = input('Digite o nome do {}º produto -> '.format(i + 1))
    produto.preco = float(input('Por último, digite o preço do {}º produto -> '.format(i + 1)))
    produto.preco = produto.preco + produto.preco * 10/100
    vet_precos.append(produto)
  print()
  print('Apresentando o novo preço dos produtos...')
  for i in range(2):
    print('{} \tCódigo: {} \tNome: {} \tPreço:{:.2f}'.format(i + 1, vet_precos[i].codigo, vet_precos[i].nome, vet_precos[i].preco))

main()