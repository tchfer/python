'''8. (Função sem retorno com parâmetro) Faça uma função/método para calcular a tabuada de um número informado pelo usuário.'''

def tabuada(num):
    i = 1
    while i <= 10:
        print('{} x {:2} = {:2}'.format(num, i, num * i))
        i += 1

def main():
    n = int(input('Insira um número qualquer para calcular a tabuada dele -> '))
    tabuada(n)

main()
