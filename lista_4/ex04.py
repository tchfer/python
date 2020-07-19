"""Faça um programa que carregue um vetor com nota de dez alunos, calcule e mostre a MÉDIA DA SALA e quantos alunos estão acima e abaixo da média da sala."""
nota = []
soma = 0
i = 0
while i <= 2:
    nota.append(float(input(f"Informe a nota do aluno ({i + 1}): ")))
    soma += nota[i]
    i += 1
media = soma / i
acimaMedia = 0
abaixoMedia = 0
contador = 0
for i in range(3):
    if nota[i] > media:
        acimaMedia += 1
    if nota[i] < media:
        abaixoMedia += 1
print(f"A média da sala foi: {media:.1f}.\n{acimaMedia} aluno(s) ficou/ficaram acima da média e {abaixoMedia} abaixo.")