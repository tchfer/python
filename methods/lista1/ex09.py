'''9. (Função sem retorno sem parâmetro) Faça uma função/método que leia cinco valores inteiros, determine e mostre o maior e o menor deles'''

def mostrar_maior_menor():
    i = 1
    maior = 0
    menor = 1000000
    while i <= 5:
        n = int(input('Digite o {}º número -> '.format(i)))
        if n >= maior:
            maior = n
        if n < menor:
            menor = n
        i += 1
    print('O maior número digitado foi: {}\nO menor número digitado foi: {}'.format(maior, menor))

def main():
    mostrar_maior_menor()

main()