nHomens = 0
nMulheres = 0
somaAbaixo = 0
somaAltura = 0
mediaAltura = 0
for i in range(5):
    sexo = str(input(f"Digite o sexo da {i + 1}ª pessoa - 'M' ou 'F': ")).casefold()
    peso = float(input(f"Digite o peso da {i + 1}ª pessoa: "))
    altura = float(input(f"Digite a altura da {i + 1}ª pessoa: "))
    if sexo == 'm':
        nHomens += 1
    if sexo == 'f':
        nMulheres += 1
    if peso < 30:
        somaAbaixo += 1
    somaAltura += altura
mediaAltura = somaAltura / 5
print(f"{nHomens} das pessoas é/são homens. {nMulheres} é/são mulheres. {somaAbaixo} pessoas está/estão abaixo dos 30 kg e a média das alturas é {mediaAltura}")
