divida = float(input("Digite o valor da divida: "))
parcela = 1
print("Valor da divida: ", end="\t\t")
print("Valor do juros: ", end="\t\t")
print("Quantidade de parcelas: ", end="\t\t")
print("Valor da parcela: ")
for i in range(5):
    if parcela == 1:
        juros = 1
        valorJuros = 0
    elif parcela == 4:
        parcela = 3
        juros = 1.10
    elif parcela == 7 or parcela == 6:
        parcela = 6
        juros = 1.15
    elif parcela == 10 or parcela == 9:
        parcela = 9
        juros = 1.20
    elif parcela == 13 or parcela == 12:
        parcela = 12
        juros = 1.25
    valorJuros = divida * (juros - 1)
    divida_com_juros = divida * juros
    valorParcela = divida_com_juros / parcela
    print(f"{divida_com_juros:.2f}", end="\t\t\t")
    print(f"{valorJuros:.2f}", end="\t\t\t\t")
    print(f"{parcela}", end="\t\t\t\t\t")
    print(f"R${valorParcela:.2f}")
    parcela += 3
    