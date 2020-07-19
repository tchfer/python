import math

custo = float(input("Insira o custo do espetáculo teatral: "))
convite = float(input("Insira o preço do convite para o espetáculo: "))

quantidade = math.trunc (custo / convite) #custo e convite foram declarados como float por ser preços então a biblioteca foi usada para tirar o decimal do resultado por ser quantidade de convites

print("Você deverá vender" , quantidade , "convites para alcançar o custo do espetáculo.")
