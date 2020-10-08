'''10. (Função sem retorno com parâmetro) Faça uma função/método para verificar e contar quantas letras a tem numa frase.'''

def letras_frase(sentence):
    # c = 0
    # for i in (sentence):
    #     if i == 'a':
    #         c += 1
    i = 0
    c = 0
    while(i < len(sentence)):
        if(sentence[i] == 'a'):
            c += 1
        i += 1

    print('A letra "A" aparece {} vezes'.format(c))


def main():
    f = str(input('Digite uma frase -> ')).casefold()
    letras_frase(f)

main()