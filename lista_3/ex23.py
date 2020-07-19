# Estrutura de loop forma decrescente para calculo de fatorial de um número
# n = int(input("Digite um numero para saber o fatorial dele -> "))
# fatorial = 1
# while n > 1:
#     fatorial = fatorial * n
#     n -= 1
# print("O fatorial do número informado é {}".format(fatorial))


E = 1
numerador = 0
denominador = 1
num = int(input("Insira um número inteiro e positivo: "))
c = 1
while c <= num:
    denominador *= numerador + 1
    E += (1 / denominador)
    numerador += 1
    c += 1
print(E)