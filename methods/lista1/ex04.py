def calcular_hora():
    segundos = int(input('Digite um número inteiro que represente um horário em segundos -> '))
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = ((segundos % 3600) % 60) // 1
    print('{} segundos é equivalente a: \n{} hora(s) \t{} minuto(s) \t{} segundo(s)'.format(segundos, h, m, s))

def main():
    calcular_hora()

main()