caro = 0
barato = 47000
c = 1
while c <= 3:
    p = float(input("Informe o preço da TV n° {} -> ".format(c)))
    if c == 1: # inicialização dos valores de caro e barato começando do primeiro input do usuário
        caro = p
        barato = p
    if p >= caro:
        caro = p
    if p <= barato:
        barato = p
    c += 1
print("A televisão mais barata custa R${:.2f} e a mais cara custa R${:.2f}".format(barato, caro))

# caro = 0
# barato = 47000
# for c in range(1, 6):
#     p = float(input("Informe o preço da TV n° {} -> ".format(c)))
#     if p >= caro:
#         caro = p
#     if p <= barato:
#         barato = p
# print("A televisão mais barata custa R${:.2f} e a mais cara custa R${:.2f}".format(barato, caro))
