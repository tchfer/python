"""Preencha um vetor com quinze elementos inteiros
Verifique a existência de elementos iguais a 30, mostrando as posições em que apareceram."""
n = []
iguais30 = []
posicao = []
i = 0
while i < 3:
    n.append(int(input(f"Digite o {i + 1}° número: ")))
    if n[i] == 30:
        iguais30.append(n[i])
        posicao.append(i)
    i += 1
if 30 in iguais30:
    print(f"O número 30 aparece na(s) posição(ões) {posicao}")
else:
    print("Não há o número 30 na lista")
