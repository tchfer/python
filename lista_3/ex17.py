# nTermos = int(input("Digite o número de termos: "))
# termo1 = 2
# termo2 = 7
# termo3 = 3
# termoAtual = 4
# while termoAtual <= nTermos:
#     print(termo1, termo2, termo3)
#     termo1 = termo1 * 2
#     print(termo1)
#     termoAtual += 1
#     if termoAtual <= nTermos:
#         termo2 = termo2 * 3
#         print(termo2)
#         termoAtual += 1
#     if termoAtual <= nTermos:
#         termo3 = termo3 * 4
#         print(termo3)
#         termoAtual+=1
#     termoAtual += 1

nTermos = int(input("Digite o número de termos: "))
termo1 = 2
termo2 = 7
termo3 = 3
for termoAtual in range(nTermos):
    print(termo1, termo2, termo3)
    termo1 = termo1 * 2
    print(termo1)
    termoAtual += 1
    if termoAtual <= nTermos:
        termo2 = termo2 * 3
        print(termo2)
        termoAtual += 1
    if termoAtual <= nTermos:
        termo3 = termo3 * 4
        print(termo3)
        termoAtual += 1
