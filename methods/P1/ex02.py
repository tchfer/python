def checar_email(e):
    somar_arroba = 0
    somar_ponto = 0
    for i in range(len(e)):
        if '@' in e[i]:
            somar_arroba += 1
        if '.' in e[i]:
            somar_ponto += 1
    # teste para verificar se está somando para verificar depois
    # print(somar_ponto, somar_arroba)
    if somar_arroba == 1 and somar_ponto >= 1:
        print('\033[0;32mE-mail válido\033[m')
    else:
        print('\033[91mE-mail inválido\033[m')

def main():
  email = input('Digite um e-mail válido -> ')
  checar_email(email)

main()