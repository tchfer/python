peso_saco = float(input('Quantos kilos de ração comprou para seus gatos? '))
consumo1 = float(input('Quantos gramas contém na porção do primeiro gato? '))
consumo2 = float(input('Quantos gramas contém na porção do outro ? '))

consumo1 = consumo1 / 1000
consumo2 = consumo2 / 1000
total_final = peso_saco - 5 * (consumo1 + consumo2)

print('Seus felinos ainda terão:' , total_final, ' gramas de ração apoś os 5 dias')
