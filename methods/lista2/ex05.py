'''5. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem lida.'''

def calcular_percent(preco, porcentagem):
    a = (preco * porcentagem / 100) + preco
    print('O valor original do produto é R${:.2f}, com o acrescimo de {}%, ficou R${:.2f}'.format(preco, porcentagem, a))

def main():
    p = float(input('Digite o valor do produto desejado -> '))
    percent = float(input('Digite a porcentagem de reajuste -> '))
    calcular_percent(p, percent)

main()