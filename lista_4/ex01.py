"""Faça um algoritmo que calcule e apresente a média de idade de uma sala de 35 alunos."""
idade = []
soma = 0
i = 0
while i <= 2:
    idade.append(int(input(f"Informe a idade do aluno ({i + 1}): ")))
    soma += idade[i]
    i += 1
media = soma / i
print("*" * 50)
print(f"A média de idade da sala é: {media:.1f} anos")
