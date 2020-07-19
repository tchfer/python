# c = 1
# while c <= 10:
#     nome = str(input("Digite o nome do aluno ({}) -> ".format(c)))
#     alt = float(input("Digite altura do aluno ({}) -> ".format(c)))
#     if c == 1:
#         alto = alt
#         baixo = alt
#     if alt >= alto:
#         alto = alt
#         nomeAlto = nome
#     if alt <= baixo:
#         baixo = alt
#         nomeBaixo = nome
#     c += 1
# print("{} é o/a mais alto(a) com {:.2f} \n{} é o/a mais baixo(a) com {:.2f}".format(nomeAlto, alto, nomeBaixo, baixo))

alto = 0
baixo = 3
nomeAlto = ""
nomeBaixo = ""
for c in range(1, 11):
    nome = str(input("Digite o nome do aluno ({}) -> ".format(c)))
    alt = float(input("Digite a altura do aluno ({}) -> ".format(c)))
    if alt >= alto:
        alto = alt
        nomeAlto = nome
    if alt <= baixo:
        baixo = alt
        nomeBaixo = nome
print("{} é o/a mais alto(a) com {:.2f} \n{} é o/a mais baixo(a) com {:.2f}".format(nomeAlto, alto, nomeBaixo, baixo))
