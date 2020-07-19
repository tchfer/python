# nElementos = 8
# elementoN = 0
# elementoNmais1 = 1
# print("A sucessão de Fibonacci começa normalmente por {} e {} "
#       "e cada termo subsequente corresponde à soma dos dois anteriores.".format(elementoN, elementoNmais1))
#
# c = 1
# print("Os próximos 8 elementos da sequencia Fibonacci são:")
# while c <= nElementos:
#     vFibonacciAtual = elementoN + elementoNmais1
#     print(vFibonacciAtual)
#     elementoN = elementoNmais1
#     elementoNmais1 = vFibonacciAtual
#     c += 1

nElementos = 8
elementoN = 0
elementoNmais1 = 1
print("A sucessão de Fibonacci começa normalmente por {} e {} "
      "e cada termo subsequente corresponde à soma dos dois anteriores.".format(elementoN, elementoNmais1))

print("Os próximos 8 elementos da sequencia Fibonacci são:")
for c in range(nElementos):
    vFibonacciAtual = elementoN + elementoNmais1
    print(vFibonacciAtual)
    elementoN = elementoNmais1
    elementoNmais1 = vFibonacciAtual
