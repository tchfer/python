# totalOperarios = 15
# sMinimo = 954
# folhaPagamento = 0
# nPecasTotal = 0
# homem = 0
# pecasHomens = 0
# mulher = 0
# pecasMulheres = 0
# salarioMaior = 0

# c = 1
# while c <= totalOperarios:
#     nOperario = str(input("Digite o número do operário({}): ".format(c)))
#     sexo = str(input("Digite o sexo do operário (M ou F): "))
#     nPecas = int(input("Digite o total de peças fabricadas pelo operário: "))
#     nPecasTotal += nPecas

#     if nPecas <= 30:
#         salario = sMinimo
#         print("O operário número {} tem o salário de R$ {:.2f}".format(nOperario, salario))
#         folhaPagamento += salario
        
#     elif salario >30 and salario <= 50:
#         salario = (sMinimo * 3 / 100) * (nPecas - 30) + sMinimo
#         print("O operário número {} tem o salário de R$ {:.2f}".format(nOperario, salario))
#         folhaPagamento += salario
        
#     elif salario > 50:
#         salario = (sMinimo * 5 / 100) * (nPecas - 30) + sMinimo
#         print("O operário número {} tem o salário de R$ {:.2f}".format(nOperario, salario))
#         folhaPagamento += salario
        
#     if sexo == "M" or sexo == "m":
#         homem += 1
#         pecasHomens += nPecas
#         print("Masculino")
#         print("*" * 60)
#     if sexo == "F" or sexo == "f":
#         mulher += 1
#         pecasMulheres += nPecas
#         print("Feminimo")
#         print("*" * 60)
#     if salario >= salarioMaior:
#         salarioMaior = salario
#         oMaiorSalario = nOperario
#     c += 1
# print("O valor da folha de pagamento da empresa é R$ {:.2f}".format(folhaPagamento))
# print("Número total de peças produzidas: {}".format(nPecasTotal))
# print("A média de peças produzidas por homens foi: {}".format(pecasHomens / homem))
# print("A média de peças produzidas por mulheres foi: {}".format(pecasMulheres / mulher))
# print("O maior salário, R$ {:.2f}, foi pago ao operário N°{}".format(salarioMaior, oMaiorSalario))

totalOperarios = 15
sMinimo = 954
folhaPagamento = 0
nPecasTotal = 0
homem = 0
pecasHomens = 0
mulher = 0
pecasMulheres = 0
salarioMaior = 0

for c in range(1,totalOperarios + 1):
    nOperario = str(input("Digite o número do operário({}): ".format(c)))
    sexo = str(input("Digite o sexo do operário (M ou F): "))
    nPecas = int(input("Digite o total de peças fabricadas pelo operário: "))
    nPecasTotal += nPecas

    if nPecas <= 30:
        salario = sMinimo
        print("O operário número {} tem o salário de R$ {:.2f}".format(nOperario, salario))
        folhaPagamento += salario
        
    elif nPecas >30 and nPecas <= 50:
        salario = (sMinimo * 3 / 100) * (nPecas - 30) + sMinimo
        print("O operário número {} tem o salário de R$ {:.2f}".format(nOperario, salario))
        folhaPagamento += salario
        
    elif nPecas > 50:
        salario = (sMinimo * 5 / 100) * (nPecas - 30) + sMinimo
        print("O operário número {} tem o salário de R$ {:.2f}".format(nOperario, salario))
        folhaPagamento += salario
        
    if sexo == "M" or sexo == "m":
        homem += 1
        pecasHomens += nPecas
        print("Masculino")
        print("*" * 60)
    if sexo == "F" or sexo == "f":
        mulher += 1
        pecasMulheres += nPecas
        print("Feminimo")
        print("*" * 60)
    if salario >= salarioMaior:
        salarioMaior = salario
        oMaiorSalario = nOperario
print("O valor da folha de pagamento da empresa é R$ {:.2f}".format(folhaPagamento))
print("Número total de peças produzidas: {}".format(nPecasTotal))
print("A média de peças produzidas por homens foi: {}".format(pecasHomens / homem))
print("A média de peças produzidas por mulheres foi: {}".format(pecasMulheres / mulher))
print("O maior salário, R$ {:.2f}, foi pago ao operário N°{}".format(salarioMaior, oMaiorSalario))
