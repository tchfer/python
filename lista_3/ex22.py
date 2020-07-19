total_produtos = 3
total_baratos = 0
total_normais = 0
total_caros = 0
total_de_custo_adicionais = 0
total_de_impostos = 0
preco_mais_barato = 0
preco_mais_caro = 0

for produto in range(total_produtos):
    preco = float(input("Digite o preço unitário: "))
    categoria = str(input("Digite uma das letras a seguir que represente a categoria: 'A' para ALIMENTAÇÃO, 'L' para LIMPEZA OU 'V' VESTUÁRIO -> ")).upper()
    refrigeracao = str(input("O produto precisa de refrigeração? Digite S para SIM ou N para NÃO. -> ")).upper()

    if preco <= 20:
        if categoria == "A":
            custo_de_estocagem = 2
        if categoria == "L":
            custo_de_estocagem = 3
        if categoria == "V":
            custo_de_estocagem = 4

    if preco > 20 and preco <= 50:
        if refrigeracao == "S":
            custo_de_estocagem = 6
        else:
            custo_de_estocagem = 0

    if preco > 50:
        if refrigeracao == "S":
            if categoria == "A":
                custo_de_estocagem = 5
            if categoria == "L":
                custo_de_estocagem = 2
            if categoria == "V":
                custo_de_estocagem = 4
        else:
            if categoria == "A" or categoria == "V": # verificar se é = ou ==
                custo_de_estocagem = 0
            if categoria == "L":
                custo_de_estocagem = 1

    if categoria == "A" and refrigeracao == "S":
        imposto_do_produto = 2 / 100
    else:
        imposto_do_produto = 4 / 100
 
    preco_final = preco + custo_de_estocagem + (imposto_do_produto * (preco + custo_de_estocagem))
    print("*" * 120)
    print(f"O custo de estocagem é R${custo_de_estocagem:.2f}, a taxa do imposto que está sendo cobrado é de {imposto_do_produto:.2f}% e o preço final do produto é de R${preco_final:.2f}")
    print()

    if preco_final <= 20:
        total_baratos += 1
        classificacao = "PRODUTO BARATO"
 
    if preco_final >  20 and preco_final <= 100:
        total_normais += 1
        classificacao = "PRODUTO NORMAL"
 
    if preco_final >  100:
        total_caros += 1
        classificacao = "PRODUTO CARO"
 
    custo_adicional = custo_de_estocagem + imposto_do_produto
    total_de_custo_adicionais += custo_adicional
    total_de_impostos += imposto_do_produto

    if produto == 0:
        preco_mais_caro = preco_final
        preco_mais_barato = preco_final
    else:
        if preco_mais_caro < preco_final:
            preco_mais_caro = preco_final
        if preco_mais_barato > preco_final:
            preco_mais_barato = preco_final
 
    media_valores_adicionais = total_de_custo_adicionais / total_produtos

print(f"A média de valores adicionais calculados nos produtos é de R${media_valores_adicionais:.2f}")
print(f"O preço mais caro é de R${preco_mais_caro:.2f}")
print(f"O preço mais barato é de R${preco_mais_barato:.2f}")
print(f"O número total de produtos baratos é {total_baratos}")
print(f"O número total de produtos normais é {total_normais}")
print(f"O número total de produtos caros é {total_caros}")
