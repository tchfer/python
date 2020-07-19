"""Faça um algoritmo que calcule e apresente a média de alturas de uma sala de 35 alunos. Informe também quantos alunos e quais são os que possuem idade superior a 25 anos."""
idade = []
altura = []
somaMaior25 = 0
somaAltura = 0
i = 0
while i <= 2:
    idade.append(int(input(f"Informe a idade do aluno ({i + 1}): ")))
    altura.append(float(input(f"Informe a altura do aluno ({i + 1}): ")))
    somaMaior25 += idade[i]
    somaAltura += altura[i]
    i += 1
mediaAltura = somaAltura / i
print("*" * 50)
print(f"A média de altura da sala é: {mediaAltura:.1f} M")
contador = 0
for i in range(3):
    if idade[i] > 25:
        print(f"Idade na lista que são superiores a 25 anos: {idade[i]}")
        contador += 1
print(f"{contador} pessoas têm mais de 25 anos de idade.")
