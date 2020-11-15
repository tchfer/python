'''Uma escola precisa montar o cadastro geral de seus alunos. Este cadastro deverá conter as seguintes informações por aluno: nome completo, data de nascimento, telefone, endereço completo e série atual. Levando em conta que esta escola possui no máximo 500 alunos, como você faria para estruturar estas informações num sistema de cadastro e consulta de cadastro, por nome e visualização de todos os dados? Implemente utilizando estrutura. Também use a criação de funções para cada operação. Use o menu a seguir:
Menu de opções:

Cadastrar alunos
Consulta por nome
Visualizar todos os dados
Sair'''

class TipoAluno:
  nome_completo = ''
  data_nascimento = ''
  n_tel = 0
  endereco = ''
  serie = ''  
 
def Cadastrar(vetAluno):
  print('Cadastro de alunos.........................')
  for a in range(3):
    a = TipoAluno()
    a.nome_completo = (input('Digite o nome completo -> '))
    a.data_nascimento = input('Digite a data de nascimento -> ')
    a.n_tel = input('Digite o telefone -> ')
    a.endereco = input('Digite o endereço -> ')
    a.serie = input('Digite a série -> ')
    vetAluno.append(a)
  return vetAluno

def Consultar(vetAluno):
  print('Consulta por nome..........................')
  nomePesquisa = input('Qual nome quer pesquisar? ')
  for i in range(3):
    if nomePesquisa == vetAluno[i].nome_completo:
      print('Nome: {} \tData de nascimento: {} \tNúmero de tel: {} \tEndereço: {} \tSérie: {}'.format(vetAluno[i].nome_completo, vetAluno[i].data_nascimento, vetAluno[i].n_tel, vetAluno[i].endereco, vetAluno[i].serie))

def Mostrar(vetAluno):
  print('Apresentaçao dos dados dos alunos..........')
  for i in range(3):
    print('Nome: {} \tData de nascimento: {} \tNúmero de tel: {} \tEndereço: {} \tSérie: {}'.format(vetAluno[i].nome_completo, vetAluno[i].data_nascimento, vetAluno[i].n_tel, vetAluno[i].endereco, vetAluno[i].serie))
          
def main():
  op = 1
  while op >=1 and op <= 3:
    print('Menu de Gerenciamento')
    print('1- Cadastrar')
    print('2- Consultar')
    print('3- Mostrar')
    print('4- Sair')
    op = int(input('Digite a opção: '))
    if op == 1:
      vetA = []
      vetA = Cadastrar(vetA)
    elif op == 2:
      Consultar(vetA)          
    elif op == 3:
      Mostrar(vetA)

main()
