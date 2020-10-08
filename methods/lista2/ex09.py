'''9. (Função sem retorno com parâmetro) Faça uma função/método para verificar se um nome digitado é igual a ‘Ana’, mostre o valor true ou false como resposta.'''

def verificar(n):
    print(bool(n == 'ana'))

def main():
    nome = str(input('Digite o nome que gostaria de verificar, por favor -> ')).casefold()
    verificar(nome)

main()