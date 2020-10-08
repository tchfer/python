def soma_divisores():
    a = int(input('Digite um número para saber quantos são divisíveis por ele -> ')) # 2
    b = int(input('Digite o 1º número para verificação -> ')) # 8 - Depois valor será reescrito por 4
    c = int(input('Digite o 2º número para verificação -> ')) # 4
    if b > c:
        aux = b # aqui 8 passa para aux
        b = c # aqui 4 passa para variável b
        c = aux # valor maior que foi mandado da variável b, passa para c
    contador = 0
    numero = []
    while b <= c:
        if b % a == 0:
            contador += 1
            numero.append(b)
        b += 1
    
    print('{} número(s) é(são) divisível(eis) por {}. Eles são: {}'.format(contador, a, numero))

def main():
    soma_divisores()

main()