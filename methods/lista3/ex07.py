# '''7. (Função com retorno sem parâmetro) Faça uma função/método retorne um vetor com os três primeiros números perfeitos. Sabe-se que um número é perfeitos quando é igual a soma de seus divisores (exceto ele mesmo). Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito.'''

def numero_perfeito():
    soma_divisor = 0
    n_perfeito = 0
    vetor = []
    while len(vetor) < 2:
        #vou incrementar o numero perfeito que estou testando (evitando leitura - input e definicao de range).
        #começa no numero 1 e vai incrementando após nova inserção do array. Neste caso irá testar varias possibilidades (1 - n)
        #Quando encontrar os primeiros 3 numeros perfeitos já não entrara mais nesse while.
        n_perfeito += 1
        # zerando o soma para não manter a somatoria do último numero perfeito identificado
        soma_divisor = 0
        #definindo o range de 1 a n_perfeito. Desta forma eu sempre vou pegar todos os divisores de 1 ao numero perfeito. Exemplo: Range de 1 a 6(onde 6 eh o numero perfeito)
        for n in range(1, n_perfeito):
            if n_perfeito % n == 0:
                soma_divisor += n
        # fica aqui para verificar no final se a soma dos divisores é igual o número perfeito
        if soma_divisor == n_perfeito:
            vetor.append(n_perfeito)
    return vetor

def main():
    print(numero_perfeito())

main()