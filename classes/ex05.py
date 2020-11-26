'''Faça um programa que realize o cadastro de contas bancarias com as seguintes informações: numero da conta, nome do titular e saldo. O banco permitirá o cadastramento de 15 contas. Crie uma função para cada opção do menu a seguir. Utilize a estrutura na passagem de parâmetro:
Menu de opções:

Cadastrar contas
Visualizar todas as contas
Consultar por nome
Alterar nome e/ou saldo de um número de conta
Excluir a conta com menor saldo
Sair'''
import emoji

class Conta:
  numero_conta = 0
  nome_titular = ""
  saldo = 0.0

def cadastrar(conta):
  contas = []
  for x in range(2):
    conta = Conta()
    conta.nome_titular = input("\nDigite o nome do {}º titular -> ".format(x + 1))
    conta.saldo = float(input("Digite o saldo disponível na conta -> "))
    conta.numero_conta = int(input("Digite o número da conta -> "))
    contas.append(conta)
  print("\n\033[0;32mCadastro realizado com sucesso.\033[m")
  return contas

def listar(contas):
  print()
  for z in range(len(contas)):
    print("-" * 100)
    print("Titular da conta: {}\t\tNúmero da conta: {}\t\tSaldo da conta: {:.2f}".format(contas[z].nome_titular, contas[z].numero_conta, contas[z].saldo))

def consultar_nome(contas):
  nome = input("\n\033[93mDigite o nome completo do titular que deseja encontrar -> \033[00m")
  n_existe = True
  for y in range(len(contas)):
    if contas[y].nome_titular == nome:
      n_existe = False
      print("-" * 100)
      print("Titular da conta: {}\t\tNúmero da conta: {}\t\tSaldo da conta: {:.2f}".format(contas[y].nome_titular, contas[y].numero_conta, contas[y].saldo))
  if n_existe:
    print("Desculpa! O nome {} não está cadastrado no nosso Sistema.".format(nome))

def alterar(contas):
  numero_conta = int(input("Digite o número da conta que deseja fazer a alteração do nome/saldo -> "))
  n_existe = True
  for y in range(len(contas)):
    if contas[y].numero_conta == numero_conta:
      n_existe = False   
      print("*"*50)
      print("MENU")
      print("*"*50)
      print("1. Digite 1 para alterar o nome -> ")
      print("2. Digite 2 para alterar o saldo -> ")
      print("3. Digite 3 para alterar o nome e o saldo -> ")
      resposta = int(input("Digite uma das opções acima para continuar -> "))
      if resposta == 1:
        contas[y].nome_titular = input("Digite a alteração do nome da conta nº{} -> ".format(numero_conta))
      elif resposta == 2:
        contas[y].saldo = float(input("Digite a alteração do saldo da conta nº{} -> ".format(numero_conta)))
      elif resposta == 3:
        contas[y].nome_titular = input("Digite a alteração do nome da conta nº{} -> ".format(numero_conta))
        contas[y].saldo = float(input("Digite a alteração do saldo da conta nº{} -> ".format(numero_conta)))
  if n_existe:
    print("Número de conta {} não existe em nosso banco de dados.".format(numero_conta))
  voltar_menu(contas)

def deletar(contas):
  menor = 0.0
  index_a_remover = 0
  for k in range(len(contas)):
    if k == 0:
      menor = contas[k].saldo
    else:
      if menor > contas[k].saldo:
        menor = contas[k].saldo
        index_a_remover = k
  contas.pop(index_a_remover)
  print("\n\033[0;32mConta com saldo menor excluída com sucesso.\033[m")
  return contas

def sair():
  print(emoji.emojize("\n\033[0;32mObrigado por usar nosso sistema! :sunglasses: \033[m", use_aliases=True))

def menu():
  print("-" * 100)
  print("\t\t\t\t\t\033[95mBem-vindo ao NuBank!\033[00m")
  print("-" * 100)
  print("\033[93mEscolha um dos números para realizar a função desejada.\033[00m")
  print("1 - Cadastrar clientes.")
  print("2 - Consultar cliente através do nome.")
  print("3 - Visualizar todos os clientes e seus dados.")
  print("4 - Excluir conta de cliente com menor saldo.")
  print("5 - Alterar nome/saldo da conta")
  print("6 - Sair.\n")
  escolha = int(input("Qual opção acima você deseja fazer? -> "))
  return escolha

def main():
  contas = []
  build(contas)

def voltar_menu(contas):
  voltar = input("\n\033[93mDigite qualquer tecla para voltar pro menu ou 6 para sair do sistema -> \033[00m")
  if voltar == "6":
    return sair()
  else:
    build(contas)

def build(contas):
  conta = Conta()
  resposta = menu()

  if resposta == 1:
    contas = cadastrar(conta)
    voltar_menu(contas)

  elif resposta == 2:
    if len(contas) == 0:
      print("Nenhum cliente cadastrado no banco de dados, cadastre para pesquisar")
      voltar_menu(contas)
    else:
      consultar_nome(contas)
      voltar_menu(contas)
  
  elif resposta == 3:
    if len(contas) == 0:
      print("Nenhum cliente cadastrado no banco de dados, cadastre para pesquisar.")
    else:
      listar(contas)
      voltar_menu(contas)
  
  elif resposta == 4:
    if len(contas) == 0:
        print("Nenhum cliente cadastrado no banco de dados, cadastre para deletar")
        voltar_menu(contas)
    else:
      contas = deletar(contas) 
      voltar_menu(contas)
  
  elif resposta == 5:
    if len(contas) == 0:
      print("Nenhum cliente cadastrado no banco de dados, cadastre para pesquisar")
      voltar_menu(contas)
    else:
      alterar(contas)
      voltar_menu(contas)
  
  elif resposta == 6:
    sair()

main()