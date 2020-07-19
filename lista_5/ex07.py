"""Faça um programa que:
Preencha dois vetores com de dez numeros cada
Preecha um terceira vetor com os números dos dois vetores anteriores ordenados em ordem crescente"""
lista1 = []
lista2 = []
listaTotal = []
for i in range(3):
    lista1.append(int(input(f"Digite o {i + 1}° número a ser adicionado na primeira lista: ")))
for i in range(3):
    lista2.append(int(input(f"Digite o {i + 1}° número a ser adicionado na segunda lista: ")))
listaTotal = lista1 + lista2
listaTotal.sort()
print(f"Os números das duas listas em ordem crescente é: {listaTotal}")
