sexoMasc = 0
sexoFem = 0
criancasMenores = 0
porcMenores = 0
porcFem = 0
porcMasc = 0
nCriancas = int(input("Digite o número de crianças nascidas: "))
print()
x = 1
while x <= nCriancas:
    idade = int(input("Informe a idade da criança n° {} -> ".format(x)))
    sexo = str(input("Agora insira o sexo da criança n° {} -> ".format(x))).upper()
    print()
    if sexo == "M":
        sexoMasc += 1
    if sexo == "F":
        sexoFem += 1
    if idade <= 2:
        criancasMenores += 1
    x += 1
    porcMenores = criancasMenores / nCriancas * 100
    porcMasc = sexoMasc / nCriancas * 100
    porcFem = sexoFem / nCriancas * 100
print()
print(f"{porcMenores} % da(s) criança(s) é/são menor(es) de 2 anos\n")
print(f"{porcMasc} % da(s) criança(s) é/são do sexo masculino\n")
print(f"{porcFem} % da(s) criança(s) é/são do sexo feminimo")