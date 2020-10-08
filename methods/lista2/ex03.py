'''3. (Função sem retorno com parâmetro) Faça uma função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, chame/crie OUTRA função que verifique se esta média aprova ou reprova o aluno.'''

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    print('A sua média final foi: {}'.format(media))
    verificar_media(media)

def verificar_media(m):
    if m >= 6:
        print('Parabéns! Você passou :-)')
    else:
        print('Sua nota final ficou abaixo da média. Procure a secretaria.')

def main():
    p1 = float(input('Digite a 1ª nota -> '))
    p2 = float(input('Digite a 2ª nota -> '))
    calcular_media(p1, p2)

main()
