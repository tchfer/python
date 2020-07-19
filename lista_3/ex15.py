# totalCidadePesquisadas = 5
# somaVeiculosCidade = 0
# somaAcidentesCidadesMais2000 = 0
# numeroAcidenteMais200 = 0
# numeroAcidenteMais200 = 0
# mediaAcidentesCidadesMais2000 = 0
# maiorCasoAcidentes = 0
# menorCasoAcidentes = 30000
# c = 1
# while c <= totalCidadePesquisadas:
#     nomeCidade = str(input("Digite o nome da cidade n° {} -> ".format(c)))
#     numeroVeiculos = int(input("Digite o número de veículos que transitam na cidade -> "))
#     numeroAcidentes = int(input("Digite o número de acidentes ocorridos nessa cidade -> "))
#     if numeroAcidentes == 0:
#         maiorCasoAcidentes = numeroAcidentes
#         cidadeMaiorCasosAcidentes = nomeCidade
#         menorCasoAcidentes = numeroAcidentes
#         cidadeMenorCasosAcidentes = nomeCidade
#     else:
#         if numeroAcidentes > maiorCasoAcidentes:
#             maiorCasoAcidentes = numeroAcidentes
#             cidadeMaiorCasosAcidentes = nomeCidade
#         if numeroAcidentes < menorCasoAcidentes:
#             menorCasoAcidentes = numeroAcidentes
#             cidadeMenorCasosAcidentes = nomeCidade
#
#     somaVeiculosCidade += numeroVeiculos
#
#     if numeroVeiculos > 2000:
#         somaAcidentesCidadesMais2000 += numeroAcidentes
#         numeroAcidenteMais200 += 1
#     c += 1
#
# mediaCarrosCidades = somaVeiculosCidade / totalCidadePesquisadas
#
# if numeroAcidenteMais200 == 0:
#     print("Não foi informada nenhuma cidade com menos de 2000 veículos.")
# else:
#     mediaAcidentesCidadesMais2000 = somaAcidentesCidadesMais2000 / numeroAcidenteMais200
# print("A cidade que contém maior número de acidentes é: {}".format(cidadeMaiorCasosAcidentes))
# print("A cidade que contém menor número de acidentes é: {}".format(cidadeMenorCasosAcidentes))
# print("A média de carros na cidade é de: {:.0f} carros".format(mediaCarrosCidades))
# print("A média de acidentes nas cidades com mais de 2000 carros foi de: {:.0f}".format(mediaAcidentesCidadesMais2000))

totalCidadePesquisadas = 5
somaVeiculosCidade = 0
somaAcidentesCidadesMais2000 = 0
numeroAcidenteMais200 = 0
numeroAcidenteMais200 = 0
mediaAcidentesCidadesMais2000 = 0
maiorCasoAcidentes = 0
menorCasoAcidentes = 30000

for c in range(totalCidadePesquisadas):
    nomeCidade = str(input("Digite o nome da cidade n° {} -> ".format(c)))
    numeroVeiculos = int(input("Digite o número de veículos que transitam na cidade -> "))
    numeroAcidentes = int(input("Digite o número de acidentes ocorridos nessa cidade -> "))
    if numeroAcidentes == 0:
        maiorCasoAcidentes = numeroAcidentes
        cidadeMaiorCasosAcidentes = nomeCidade
        menorCasoAcidentes = numeroAcidentes
        cidadeMenorCasosAcidentes = nomeCidade
    else:
        if numeroAcidentes > maiorCasoAcidentes:
            maiorCasoAcidentes = numeroAcidentes
            cidadeMaiorCasosAcidentes = nomeCidade
        if numeroAcidentes < menorCasoAcidentes:
            menorCasoAcidentes = numeroAcidentes
            cidadeMenorCasosAcidentes = nomeCidade

    somaVeiculosCidade += numeroVeiculos

    if numeroVeiculos > 2000:
        somaAcidentesCidadesMais2000 += numeroAcidentes
        numeroAcidenteMais200 += 1

mediaCarrosCidades = somaVeiculosCidade / totalCidadePesquisadas

if numeroAcidenteMais200 == 0:
    print("Não foi informada nenhuma cidade com menos de 2000 veículos.")
else:
    mediaAcidentesCidadesMais2000 = somaAcidentesCidadesMais2000 / numeroAcidenteMais200
print("A cidade que contém maior número de acidentes é: {}".format(cidadeMaiorCasosAcidentes))
print("A cidade que contém menor número de acidentes é: {}".format(cidadeMenorCasosAcidentes))
print("A média de carros na cidade é de: {:.0f} carros".format(mediaCarrosCidades))
print("A média de acidentes nas cidades com mais de 2000 carros foi de: {:.0f}".format(mediaAcidentesCidadesMais2000))