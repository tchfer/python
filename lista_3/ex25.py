for nNadadores in range(1,5):
    idade = int(input(f"Qual a idade do nadador n° {nNadadores} -> "))
    if idade >= 5 and idade <= 10:
        print("O nadador n°{} está na categoria Infantil".format(nNadadores))
    if idade > 10 and idade <= 17:
        print("O nadador n°{} está na categoria Juvenil".format(nNadadores))
    if idade > 18:
        print("O nadador n°{} está na categoria Adulto".format(nNadadores))
