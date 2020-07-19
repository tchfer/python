# x = int(input("Você gostaria de ver a tabuada de qual número? "))
# contador = 0
# while contador <= 10:
#     r = x * contador
#     print("{} x {:2} = {:2}".format(x, contador, r))
#     contador += 1

n = int(input("Você gostaria de ver a tabuada de qual número? "))
for x in range(11):
    print("{} x {:2} = {:2}".format(n, x, n * x))
