import math # Importa a função para ser usada para Seno

angulo = float(input("Entre o valor da medida do ângulo (em graus): "))
altura = float(input("Qual a altura em que a escada está apoiada na parede? "))

radiano = angulo * 3.14 /180
escada = round(altura / math.sin(radiano)) # Chamar a função através do math.sin

print("O tamanho da escada é de" , escada, "metros.")

