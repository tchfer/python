'''6. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um valor inicial e um valor final realizar o acumulo desse valores e apresentar o resultado.'''

def somar_intervalos(num1, num2):
    
    if num1 > num2:
        aux = num1
        num1 = num2
        num2 = aux
    soma = 0
    while num1 <= num2:
        soma += num1
        num1 += 1
    print(soma)

def main():
    n1 = float(input('Insira um número qualquer -> '))
    n2 = float(input('Insira outro número -> '))
    somar_intervalos(n1, n2)

main()