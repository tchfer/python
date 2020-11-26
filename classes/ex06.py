'''6. Uma empresa prestadora de serviços armazena informações sobre os serviços prestados. Sabe-se que a empresa pode realizar no máximo três serviços diariamente. É de interesse de sua direção manter um histórico mensal (30 dias) sobre os serviços prestados.
A empresa realiza quatro tipos de serviços:

1) pintura;

2) jardinagem;

3) faxina e

4) reforma em geral.

Cada serviço realizado deve ser cadastrado com as seguintes informações: número do serviço, valor do serviço, código do serviço e código do cliente.

Cadastre os quatro tipos de serviços (código e descrição) que a empresa poderá realizar. Para isso, utilize um vetor de quatro posições. O programa deverá mostrar o seguinte menu de opções:

Cadastrar os tipos de serviços
Mostrar todos os tipos de serviço
Cadastrar os serviços prestados
Mostrar todos os serviços prestados
Mostrar os serviços prestados em determinado dia
Mostrar os serviços prestados dentro de um intervalo de valor
Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço
Para a opção 1: deve-se cadastrar os tipos de serviços oferecidos pela empresa, com código e descrição.

Para a opção 2: deve-se considerar que deverão ser cadastrados os serviços prestados ao logo do mês. Em cada dia podem ser cadastrados, no máximo, três serviços prestados.

Utilize uma matriz capaz de armazenar em cada posição todas as informações referentes a um serviço prestado (número, valor, código do serviço, código do cliente). Cada linha representa um dia do mês. Dessa maneira, considere a matriz com dimensão 30 × 3.

Solicite o dia em que o serviço foi prestado e as demais informações. Lembre-se de que a empresa só pode prestar os serviços que já tenham sido cadastrados no vetor de tipo de serviços.

Caso o usuário digite um código de tipo de serviço inválido, o programa deverá mostrar uma mensagem de erro.

Quando o usuário tentar cadastrar mais de três serviços prestados em um mesmo dia, também deverá mostrar uma mensagem de erro.

Para a opção 3: o programa deverá receber o dia que se deseja consultar e mostrar os respectivos serviços prestados.

Para a opção 4: o programa deverá receber o valor mínimo e o valor máximo e mostrar os serviços prestados que estiverem nesse intervalo.

Para a opção 5: o programa deverá mostrar todos os serviços prestados, conforme o exemplo a seguir.

              DIA 01
No do serviço	Valor do serviço R$	Código do serviço	Descrição	Código do cliente
100	200,00	1	Pintura	1
150	100,00	3	Faxina	5
              DIA 02
No do serviço	Valor do serviço R$	Código do serviço	Descrição	Código do cliente
301	600,00	4	Reforma em geral	3
280	352,00	1	Pintura	2
'''
class Tiposervico:
  codigo = 0
  descricao = ""
class Servico:
  numero = 0
  codigo = 0
  valor = 0.0
  codigo_cliente = 0
def menu():
  print("-" * 80)
  print("\033[1m\33[34m\t\t\t\tMenu\033[00m")
  print("-" * 80)
  print("\033[41mEscolha entre 1 e 7 para habilitar uma das funções a seguir:\n\033[00m")  
  print("1. Cadastrar serviços")
  print("2. Mostrar todos os tipos de serviço")
  print("3. Cadastrar os serviços prestados")
  print("4. Mostrar todos os serviços prestados")
  print("5. Mostrar os serviços prestados em um determinado dia")
  print("6. Mostrar os serviços prestados dentro de um intervalo de preço")
  print("7. Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço")
  print("-" * 80)
  resposta = int(input("Digite uma das opções acima -> "))
  return resposta

def build(a,b):
  resposta = menu()
  if resposta == 1:
    cadastrar_servico(a,b)
  elif resposta == 2:
    mostrar_t_servico(a,b)
  elif resposta == 3:
    cadastrar_servico_prestado(a,b) 
  elif resposta == 4:
    mostrar_todos_servicos_prestados(a,b)
  elif  resposta == 5:
    mostrar_dia_servicos(a,b)
  elif resposta == 6:
    mostrar_servico_intervalo(a,b)
  elif resposta == 7:
    mostrar_relatorio(a,b)
  else:
    print("\033[41mOpção inválida. Digite uma opção de 1 à 7, sem ponto, vírgulas ou espaços.\033[00m")
    build(a,b)
    
def main():
  tipos_de_servico = []
  servicos_prestados= []
  build( tipos_de_servico,servicos_prestados)

def cadastrar_servico(a,b):
  x = 0
  while x < 4:
    tipo_servico = Tiposervico()
    tipo_servico.codigo = int(input("Digite o código do serviço -> "))
    tipo_servico.descricao = input("Digite a descrição do serviço -> ")
    x += 1
    a.append(tipo_servico)
  return build(a,b)                        

def mostrar_t_servico(a,b):
  for y in range(4):
    print("Código: {}\tDescrição: {}".format(a[y].codigo, a[y].descricao))
  input("\033[41mDigite algo para continuar...\033[00m")
  return build(a,b)

def cadastrar_servico_prestado(a,b):
  b = []
  print()
  for d in range(2):
    print("{}° dia do mês".format(d + 1))
    servicos = []
    x = 0
    resposta = "S"
    while x < 3 and resposta == "S" :
      servico = Servico()
      servico.numero = int(input("Digite o número do serviço -> "))
      servico.codigo = int(input("Digite o código do serviço -> "))
      n_existe = True
      for q in range(len(a)):
        if a[q].codigo == servico.codigo:
            n_existe = False
      if n_existe:
        print("O código não existe. Por favor, cadastre o tipo de serviço.")
        input("\033[41mDigite algo para continuar...\033[00m")
        b = []
        build(a,b)
      servico.codigo_cliente = int(input("Digite o código do cliente que solicitou o serviço -> "))    
      servico.valor = float(input("Digite o preço do serviço -> "))
      servicos.append(servico)
      x +=  1
      resposta = str(input("Deseja continuar cadastrando o serviço na data presente? Digite 'S' para sim e 'N' para não -> ")).upper()
    b.append(servicos)          
  return build(a,b)
    
def mostrar_todos_servicos_prestados(a,b):
  print(b)
  print()
  for lin in range(len(b)):
    print("Dia {}°".format(lin + 1))
    for col in range(len(b[lin])):
      print("Número do serviço: {}".format(b[lin][col].numero))
      print("Código do serviço: {} ".format(b[lin][col].codigo))
      print("Código de cliente do serviço: {} ".format(b[lin][col].codigo_cliente))
      print("Preço do serviço: R${:.2f} ".format(b[lin][col].valor))
      print()
  input("\033[41mDigite algo para continuar...\033[00m")
  return build(a,b)

def mostrar_dia_servicos(a,b):
  d = int(input("Digite o dia que você deseja ver os serviços -> ")) - 1
  print()
  for col in range(len(b[d])):
    print("{}° dia".format(d + 1))
    print("Número do serviço: {}".format(b[d][col].numero))
    print("Código do serviço: {}".format(b[d][col].codigo))
    print("Código de cliente do serviço: {}".format(b[d][col].codigo_cliente))
    print("Preço do serviço: R${:.2f}".format(b[d][col].valor))
  input("\033[41mDigite algo para continuar...\033[00m")            
  return build(a,b)

def mostrar_servico_intervalo(a,b):
  menor_preco = float(input("Digite o menor preço que deseja pesquisar -> "))
  maior_preco = float(input("Até que preço deseja fazer a busca? -> "))
  print()
  for lin in  range(len(b)):
    for col in range(len(b[lin])):
      if b[lin][col].valor >= menor_preco and b[lin][col].valor <= maior_preco:
        print("\33[1mPreços entre R${:.2f} e R${:.2f}\033[00m".format(menor_preco, maior_preco))
        print("{}° dia".format(lin + 1))
        print("Número do serviço: {}".format(b[lin][col].numero))
        print("Codigo do serviço: {}".format(b[lin][col].codigo))
        print("Código de cliente do serviço: {}".format(b[lin][col].codigo_cliente))
        print("Preço do serviço: {:.2f}".format(b[lin][col].valor))
  input("\033[41mDigite algo para continuar...\033[00m")
  return build(a,b)

def mostrar_relatorio(a,b):
  print(b)
  for lin in range(len(b)):
    print("{}° dia".format(lin + 1))
    for col in range(len(b[lin])):
      print("Número do serviço: {}".format(b[lin][col].numero))
      print("Código do serviço: {}".format(b[lin][col].codigo))
      print("Preço do serviço: {:.2f}".format(b[lin][col].valor))
      for x in range(len(a)):
        if a[x].codigo == b[lin][col].codigo:
          print("Descrição do Serviço: {}".format(a[x].descricao))
      print("Codigo de cliente do serviço: {}".format(b[lin][col].codigo_cliente))
  input("\033[41mDigite algo para continuar...\033[00m")
  return build(a,b)    

main()