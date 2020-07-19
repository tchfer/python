import math

hora = float(input("Insira a hora no formato (H.MINUTOS) "))

# h = hora // 1 = As duas barras fariam o mesmo comando que foi feito na biblioteca math.trunc
h = math.trunc (hora)
minutos = hora - h
conversao = (h * 60) + (minutos * 100)

print("A conversão das horas para minutos é de: " , conversao)
