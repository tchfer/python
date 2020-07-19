# soma = 0
# c = 1
# while c <= 4:
#     n = int(input("{} - Insira o número  -> ".format(c)))
#     soma += n
#
#     c += 1
# print("O valor total da soma é: {}".format(soma))

soma = 0
for c in range(1, 5):
    n = int(input("{} - Insira o número -> ".format(c)))
    soma += n
print("O valor total da soma é: {}".format(soma))
