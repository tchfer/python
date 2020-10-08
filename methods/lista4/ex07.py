'''7. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora:

*** Minha Calculadora ***
Digite um número.....: 
Digite outro número..: 
    + Soma dois números
    - Subtrai dois números
    * Multiplica dois números
    / Divide dois números
Qual opção deseja? 
b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.

A função de desenho/construção do menu, chamará todas as outras passando a elas os valores digitados.'''

def somar(a,b):
  soma = a + b
  return soma

def subtrair(a,b):
  sub = a - b
  return sub

def multiplicar(a,b):
  mult = a * b
  return mult

def dividir(a,b):
  div = a / b
  return div

def calculadora():
  cont = 0
  while cont == 0:
    print('\n\n***Minha Calculadora***\n')
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    opcao = input('Operações:\n + Somar \n - Subtrair \n * Multiplicar \n / Dividir \n\nDigite o símbolo da operação que quer fazer -> ')
    if opcao == '+':
      print(somar(n1,n2))
    elif opcao == '-':
      print(subtrair(n1,n2))
    elif opcao == '*':
      print(multiplicar(n1,n2))
    elif opcao == '/':
      print(dividir(n1,n2))
    else:
      cont = 1
      print('Finalizado')
def main():
    calculadora()

main()