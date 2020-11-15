'''Elabore uma estrutura para representar um p (código, nome, preço). Crie uma função para cadastrar 5 produtos. Crie outra função para aplicar 10% de aumento no preço do produto e apresente todos os dados do preço.'''

class Produto: # tipo de dado
  codigo = 0
  nome = ''
  preco = 0.0

def main ():
  vetP = []
  print('Leitura dos dados do produto......')
  for i in range(2):
    p = Produto() # variável p agora recebe a estrutura produto
    p.codigo = int(input('Digite o código: '))
    p.nome = input('Digite o nome do produto: ')
    p.preco = float(input('Digite o preço do produto: '))
    vetP.append(p)
  aumento(vetP)

def aumento (vetP):
    for i in range(2):
      vetP[i].preco = vetP[i].preco * 10/100 + vetP[i].preco
      print("-"*70)
      print('Código: {}\tNome: {}\tNovo Preço: {:.2f}'.format(vetP[i].codigo, vetP[i].nome, vetP[i].preco))
    
main()