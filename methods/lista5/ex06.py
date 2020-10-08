'''6. Faça um programa que carregue: *um vetor com oito posições com os nomes das lojas; * um outro vetor com quatro posições com os nomes dos produtos; * uma matriz com os preços de todos os produtos em cada loja. O programa deve mostrar todas as relações (nome do produto – nome da loja) nas quais o preço não ultrapasse R$ 120,00. Escolha qual é o tipo da função que quer.'''

def adicionar_itens():
  lojas=[]
  produtos=[]
  preco_p = []
  matriz = []
  print()
  for l in range(4):
    lojas.append(input("Digite o nome da {}ª loja -> ".format(l + 1)))
  print()
  for c in range(2):
    produtos.append(input("Digite o nome do {}º produto -> ".format(c + 1)))
  print()
  for l in range(4):
    preco_p = []
    for c in range(2):
      preco_p.append(float(input("Digite o valor do {} na {} -> ".format(produtos[c], lojas[l]))))
    matriz.append(preco_p)
  print()
  for l in range(4):
    for c in range(2):
      if matriz[l][c] <= 120:
        print("A(O) {} da loja {} custa {} ".format(produtos[c], lojas[l], matriz[l][c]))
  if matriz[l][c] > 120:
    print('\nNenhum produto de nenhuma loja está abaixo de R$ 120,00')

def main():
  adicionar_itens()

main()