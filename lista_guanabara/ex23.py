n = int(input("Digite um número: "))
# calculo para fatiar o número da unidade ao milhar
uni = n // 1 % 10
dez = n // 10 % 10
cent = n // 100 % 10
mil = n // 1000 % 10
print("*" * 30)
print(f"Unidade: {uni}")
print(f"Dezena: {dez}")
print(f"Centena: {cent}")
print(f"Milhar: {mil}")
