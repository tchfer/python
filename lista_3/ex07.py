# c = 1
# pares = 0
# while c <= 23:
#     n = int(input("{:2} - Insira o número desejado -> ".format(c)))
#     c += 1
#     if n % 2 == 0:
#         pares += 1
# print("A quantidade de número(s) par(es) é de {} e {} dele(s) é/são ímpar(es)".format(pares, 23 - pares))

par = 0
for c in range(1, 24):
    n = int(input("{:2} - Insira o número desejado -> ".format(c)))
    if n % 2 == 0:
        par += 1
print("A quantidade de número(s) par(es) é de {} e {} deles é/são ímpar(es)".format(par, 23 - par))
