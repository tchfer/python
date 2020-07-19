"""Faça um programa que:
Receba cinco números e mostre a saída a seguir:
Imprima a seguinte saída: n1 + n2 + n3 + n4 + n5 = soma_dos_numeros(valor)"""
n = []
soma = 0
for i in range(5):
    n.append(int(input("Digite o {}° desejado: ".format(i + 1))))
    soma += n[i]
print(f"A soma de {n[0]} + {n[1]} + {n[2]} + {n[3]} + {n[4]} = {soma}")
