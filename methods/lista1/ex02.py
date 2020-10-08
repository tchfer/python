def somar_intervalos():
    a = float(input('Insira um número qualquer -> '))
    b = float(input('Insira outro número -> '))
    if a > b:
        aux = a
        a = b
        b = aux
    soma = 0
    while a <= b:
        soma += a
        a += 1
        print(soma)
    print(soma)

def main():
    somar_intervalos()

main()