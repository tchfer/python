'''6. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba duas notas (P1, P2) calcule a média, chame outra função que avalie se este aluno esta aprovado ou reprovado retornando a str/string 'Aprovado' ou 'Reprovado'.'''

def verifica(a):
    if a < 6:
        return 'Reprovado'
    else:
        return 'Aprovado'
def media(a, b):
    media = (a + b) / 2
    print(f'***********\nCalculando sua média...\nMédia {media} - {verifica(media)}')

def main():
    p1 = float(input('Digite a nota da P1: '))
    p2 = float(input('Digite a nota da P2: '))
    media(p1, p2)

main()