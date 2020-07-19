tamanho_da_escada = float (input ("Insira o tamanho da escada que será usada: "))
altura = float (input ("Agora coloque altura em que deseja pregar o quadro: "))

distancia = tamanho_da_escada ** 2 - altura ** 2
distancia =  distancia ** (1/2)

print ("A distância da parede ao ponto inicial da escada é de" , distancia , "metros.")
