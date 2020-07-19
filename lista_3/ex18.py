# reprovado = 0
# exame = 0
# aprovado = 0
# somaMedia = 0
# for nAlunos in range(1, 7):
#     n1 = float(input("Digite a primeira nota do aluno ({}) -> ".format(nAlunos)))
#     n2 = float(input("Digite a segunda nota do ({}) -> ".format(nAlunos)))

#     media = (n1 + n2) / 2
#     somaMedia += media
#     mediaTotal = somaMedia / nAlunos
#     print("A média do(a) aluno(a) {} foi {}".format(nAlunos, media))

#     if media < 3:
#         print("Reprovado")
#         reprovado += 1
#     if media >= 3 and media <=7:
#         print("Exame")
#         exame += 1
#     if media > 7:
#         print("Aprovado")
#         aprovado += 1
# print("\n{} alunos foram aprovados".format(aprovado))
# print("{} alunos ficaram de exame".format(exame))
# print("{} alunos foram reprovados".format(reprovado))
# print("A média da sala foi {}".format(mediaTotal))

reprovado = 0
exame = 0
aprovado = 0
somaMedia = 0

nAlunos = 1
while nAlunos <= 6:
    n1 = float(input("Digite a primeira nota do aluno ({}) -> ".format(nAlunos)))
    n2 = float(input("Digite a segunda nota do ({}) -> ".format(nAlunos)))

    media = (n1 + n2) / 2
    somaMedia += media
    mediaTotal = somaMedia / nAlunos
    print("A média do(a) aluno(a) {} foi {:.1f}".format(nAlunos, media))

    if media < 3:
        print("Reprovado")
        reprovado += 1
    if media >= 3 and media <=7:
        print("Exame")
        exame += 1
    if media > 7:
        print("Aprovado")
        aprovado += 1
    nAlunos += 1

print("\n{} alunos foram aprovados".format(aprovado))
print("{} alunos ficaram de exame".format(exame))
print("{} alunos foram reprovados".format(reprovado))
print("A média da sala foi {:.1f}".format(mediaTotal))
