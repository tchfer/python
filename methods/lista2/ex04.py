'''4. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%.'''

def calcular_percent(preco):
    a = (preco * 9 / 100) + preco
    print('O valor original do produto é R${:.2f}, com o acrescimo de 9%, ficou R${:.2f}'.format(preco, a))

def main():
    p = float(input('Digite o valor do produto desejado -> '))
    calcular_percent(p)

main()