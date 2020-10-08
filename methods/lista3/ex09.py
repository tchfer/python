'''9. (Função com retorno sem parâmetro) Foi realizada uma pesquisa sobre algumas características fisicas de cinco habitantes de uma região. Foram coletados os seguintes dados de cada habitante: idade, sexo (M - masculino ou F - feminino), cor dos olhos (A - azuis ou C - castanhos), cor dos cabelos (L - louros, P - pretos ou C - castanhos).
Faça uma função/método que leia esses dados, armazenando-os em vetores (listas);
Faça uma função/método que determine e devolva ao programa principal a média de idades das pessoas com olhos castanhos e cabelos pretos.
Faça uma função/método que determine e devolva ao programa principal a maior idade entre os habitantes.
Faça uma função/método que determine e devolva ao programa principal a quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos(inclusive) e que tenham olhos azuis e cabelos louros.'''

idade = []
sexo = []
olhos = []
cabelos = []
# Média idade - Olhos Castanhos e Cabelos Pretos
def media_idade():
    cont = 0
    soma_idade = 0
    media = 0
    for i in range(5):
        if olhos[i].upper() == 'C' and cabelos[i].upper() == 'P':
            soma_idade += idade[i]
            cont += 1
            media = soma_idade / cont
    return media
# Maior idade
def maior_idade():
    maior = 0
    for i in range(5):
        if idade[i] > maior:
            maior = idade[i]
    return maior

# Qtd fem, idade entre 18 e 35 (inclusive) - Olhos Azuis e Cabelos Louros
def qtd_fem():
    qtd = 0
    for i in range(5):
        if olhos[i].upper() == 'A' and cabelos[i].upper() == 'L':
            if sexo[i].upper() == 'F':
                if idade[i] >= 18 and idade[i <= 35]:
                    qtd += 1
    return qtd

def main():
    for i in range(5):
        print(f'\n\nCaracterísticas do {i + 1}º habitante')
        idade.append(int(input('Digite a idade -> ')))
        sexo.append(input('Digite o sexo (M - masculino ou F - feminino) -> '))
        olhos.append(input('Digite a cor dos olhos (A - azuis ou C - castanhos) -> '))
        cabelos.append(input('Digite a cor do cabelo (L - louros, P - pretos ou c - castanhos) -> '))
    print('\n\nA Média de idade de pessoas com Olhos Castanhos e Cabelos Pretos é: {}'.format(media_idade()))
    print('A Maior idade entre os habitantes é: {}'.format(maior_idade()))
    print('A Quantidade de mulheres com idade entre 18 e 35 anos(inclusive), com Olhos Azuis e Cabelos Louros é: {}'.format(qtd_fem()))

main() 