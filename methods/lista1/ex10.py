'''10. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro e positivo N e mostre o valor de S, obitos pelo seguinte cálculo:
S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!'''

def fatorial():
    E = 1
    numerador = 0
    denominador = 1
    num = int(input("Insira um número inteiro e positivo: "))
    i = 1
    while i <= num:
        denominador *= numerador + 1
        E += (1 / denominador)
        numerador += 1
        i += 1
    print(E)

def main():
    fatorial()

main()

# def fatorial():
#   num=int(input( " digite um numero para calcular o fatorial " ))
#   s = 1
#   print(f"{num}!",end="")
#   for a in range(num,0,-1):
#     s*=a
#     print(a,"x"if a > 1 else "-", end= "")
#   print(s)

# fatorial()