'''7. (Função sem retorno sem parâmetro) Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a A, deverá calcular a média aritimética das notas dos alunos, se for P, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada.'''

def calcular_media():
    n1 = float(input('Digite a 1ª nota -> '))
    n2 = float(input('Digite a 2ª nota -> '))
    n3 = float(input('Digite a 3ª nota -> '))
    letra = str(input('Digite "A" se quiser calcular a média aritmética ou "P" para calcular a ponderada -> ')).casefold()

    if letra == 'a':
        media_aritimetica = (n1 + n2 + n3) / 3
        print('A média aritimética do aluno é: {:.2f}'.format(media_aritimetica))
    elif letra == 'p':
        media_ponderada = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / (5 + 3 + 2)
        print('A média ponderada do aluno é: {:.2f}'.format(media_ponderada))

def main():
    calcular_media()

main()