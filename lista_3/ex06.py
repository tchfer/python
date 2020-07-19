# c = 1
# maior = 0
# while c <= 10:
#     i = int(input("Insira a idade número {} -> ".format(c)))
#     c += 1
#     if i >= 18:
#         maior += 1
#     else:
#         menor = 10 - maior
# print("{} pessoa(s) é/são maior(es) de idade e {} é/são menor(es) de idade".format(maior, 10 - maior))


maior = 0
for c in range(1, 6):
    i = int(input("Insira a idade número {} -> ".format(c)))
    if i >= 18:
        maior += 1
print("{} pessoa(s) é/são maior(es) de idade e {} é/são menor(es) de idade".format(maior, 5 - maior))
