altura_do_degrau = float(input("Digite o tamanho do degrau em metros: "))
altura_desejada = float(input("Agora digite a altura que deseja alcançar também em metros: "))

quantidade_degraus = altura_desejada // altura_do_degrau

print("A quantidade de degraus que terá que andar é de: " , quantidade_degraus, "degraus.")
