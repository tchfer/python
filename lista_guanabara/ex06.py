'''Crie um algoritmo
que leia um número e
mostre o seu dobro,
triplo e raiz quadrada.'''
n = int(input('Escreva um número: '))
print('O dodro de {} é {} \nO triplo dele é {}\nA raiz quadrada é {}'.format(n, n * 2, (n * 3), (n ** (1 / 2))))
#para fazer essa raiz quadrada, poderia fazer pow(n, n * (1 / 2))