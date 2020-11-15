'''
class Tiposerviço: # referente ao exercício 4
    codigo = 0
    descricao = '' #descrição do serviço

class TipoServicoPrestado:
  numeroServico = 0
  codigoServico = 0
  precoServico = 0.0
  codigoCliente = 0

def CadastrarTiposServico(vtiposervico):
    print('Cadastro de alunos.........................')
    for i in range(3):
        a = TipoAluno()
        a.matricula = int(input('Digite a matrícula: '))
        a.nome = input('Digite o nome: ')
        vetAluno.append(a)
    return vetAluno

def Consultar(vetAluno):
    print('Consulta por nome..........................')
    nomePesquisa = input('Qual nome quer pesquisar? ')
    for i in range(3):
        if nomePesquisa == vetAluno[i].nome:
            print('Matrícula: ',vetAluno[i].matricula,'\tNome: ',vetAluno[i].nome)
 
def Mostrar(vetAluno):
    print('Apresentaçao dos dados dos alunos..........')
    for i in range(3):
        print('Matrícula: ',vetAluno[i].matricula,'\tNome: ',vetAluno[i].nome)
            
def main():
    op = 1
    while op >=1 and op <= 2:
        print('Menu de Gerenciamento')
        print('1- Cadastrar tipo de serviço: ')
        print('2- mostrar tipos de serviço: ')
       print('3- Sair')
        op = int(input('Digite a opção: '))
        if op == 1:
            vettiposervico=[]
            vettiposervico = CadastrarTiposServico(vettiposervico)
        elif op == 2:
           MostrarTiposServico(vettiposervico)
       
main()
'''
#Estrutura Cadastro de Serviços Prestados
class Info_Serv():
  numero_servico = 0
  valor_servico = 0.0
  codigo_servico = 0
  codigo_cliente = 0

#Estrutura Cadastro Tipo de Serviços
class Servico():
  descricao = ''
  codigo = 0

#-------------------------------------------------------------------------------
#Funções
def Cadastro_Tipos_Servicos(Tipo_Servico):
  print('{:-^100}'.format('Casdastar Tipo de Serviços'))
  if len(Tipo_Servico) >= 4: #tamanho do vetor, para inibir cadastro de mais de 4 serviços
    print('O sistema já possui o número máximo de tipos de serviços cadastrados!')
  else:
    while len(Tipo_Servico) < 4: # tamanho do indice do vetor
      print('Digite o %dº Serviço: '%(len(Tipo_Servico)+1)) # %d numero inteiro 
      ts = Servico() #atribuiu a classe servico
      ts.descricao = str(input('Digite o tipo do serviço: '))
      ts.codigo = int(input('Digite o código do serviço: '))
      Tipo_Servico.append(ts)    
  return Tipo_Servico
  
def Cadastro_Servicos_Prestados(Matriz_Servico,Servico_Prestado):
  Matriz_Servico = []
  print('{:-^100}'.format('Cadastar Serviços Prestados'))
  for l in range(1):
    Servico_Prestado = []
    for c in range(3):
      sp = Info_Serv()
      sp.numero_servico = int(input('Digite o Número do Serviço: '))
      sp.valor_servico = float(input('Digite o Valor do Serviço: '))
      sp.codigo_servico = int(input('Digite o Código do Serviço: '))
      sp.codigo_cliente = int(input('Digite o Código do Cliente: '))
      Servico_Prestado.append(sp)
    Matriz_Servico.append(Servico_Prestado)
  return Matriz_Servico

def Relatorio_Servicos_Dia(Matriz_Servico):
  print('{:-^100}'.format('Relatório de serviços Prestados por dia'))
  dia = int(input('Digite o dia para gerar o relatório: '))
  for l in range(1):
    if dia == (l+1): #dia 1 = (0+1) // dia 2 = (1+1) ....
      for c in range(3):
        print('{:{align}{width}}{:{align}{width}}{:{align}{width}}{:{align}{width}}'.format('numero servico','valor servico','codigo_servico','codigo_cliente', align='^', width='20'))
        print('{:{align}{width}}{:{align}{width}}{:{align}{width}}{:{align}{width}}'.format(Matriz_Servico[l][c].numero_servico,Matriz_Servico[l][c].valor_servico,Matriz_Servico[l][c].codigo_servico,Matriz_Servico[l][c].codigo_cliente, align='^', width='20')) 
                                                                                                                                                                                       
def Relatorio_Servicos_Valor(Matriz_Servico):
  print('{:-^100}'.format('Relatório de serviços Prestados por faixa de valor'))
  print('{:{align}{width}}{:{align}{width}}{:{align}{width}}{:{align}{width}}'.format('numero_servico','valor_servico','codigo_servico','codigo_cliente', align='^', width='20')) # ^ centralizar W=20 tamanho
  valor_inicial = int(input('Digite o valor inical: '))
  valor_final = int(input('Digite o valor final: '))
  for l in range(1):
    for c in range(3):
      if valor_inicial <= Matriz_Servico[l][c].valor_servico and valor_final >= Matriz_Servico[l][c].valor_servico:
       
        print('{:{align}{width}}{:{align}{width}}{:{align}{width}}{:{align}{width}}'.format(Matriz_Servico[l][c].numero_servico,Matriz_Servico[l][c].valor_servico,Matriz_Servico[l][c].codigo_servico,Matriz_Servico[l][c].codigo_cliente, align='^', width='20'))
                                                                                                                                                                                        
def Relatorio_Geral(Matriz_Servico,Tipo_Servico):
  print('{:-^100}'.format('Relatório Geral'))
  for l in range(1):
    print('\nDia {}\n' .format(l+1))  # \n pular uma linha   {} .format(o que digitar dentro do format, volta no colchete) linha +1
    for c in range(3):
      print('{:{align}{width}}{:{align}{width}}{:{align}{width}}{:{align}{width}}{:{align}{width}}'.format('numero_servico','valor_servico','codigo_servico','descrição','codigo_cliente', align='^', width='20'))
      print('{:{align}{width}}{:{align}{width}}{:{align}{width}}{:{align}{width}}{:{align}{width}}'.format(Matriz_Servico[l][c].numero_servico,Matriz_Servico[l][c].valor_servico,Matriz_Servico[l][c].codigo_servico,Tipo_Servico[Matriz_Servico[l][c].codigo_servico-1].descricao,Matriz_Servico[l][c].codigo_cliente, align='^', width='20'))



#-------------------------------------------------------------------------------                                                                                           
#Menu
def main():
  Tipo_Servico = []
  Matriz_Servico = []
  Servico_Prestado = []
  op = 1
  while op >=1 and op <6:
    print('{:-^100}'.format('Menu do Sistema'))
    print('1 - Cadastrar os tipos de serviços')
    print('2 - Cadastrar os serviços prestados')
    print('3 - Mostrar os serviços prestados em determinado dia')
    print('4 - Mostrar os serviços prestados dentro de um intervalo de valor')
    print('5 - Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço')
    print('6 - Sair')
    op = int(input('Digite a opção desejada: '))
    if op == 1:
      Cadastro_Tipos_Servicos(Tipo_Servico)
    elif op == 2:
      Matriz_Servico = Cadastro_Servicos_Prestados(Matriz_Servico, Servico_Prestado)
    elif op == 3:
      Relatorio_Servicos_Dia(Matriz_Servico)
    elif op == 4:
      Relatorio_Servicos_Valor(Matriz_Servico)
    elif op == 5:
      Relatorio_Geral(Matriz_Servico,Tipo_Servico)
    else:
      print('{:-^100}'.format('Sistema Encerrado'))
main()