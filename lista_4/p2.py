nomeProduto = []
precoProduto = []
for i in range (4) :
  nomeProduto.append(str(input(f"Digite o nome do {i + 1}º produto: ")))
  precoProduto.append(float(input(f"Digite o preço do {i + 1}º produto: ")))
  print("=-" * 50)
for i in range (4) :
  if precoProduto[i] >= 50 and precoProduto[i] <= 70 :
    aumento = precoProduto[i] * 5 / 100
    precoProduto[i] += aumento
  else:
    precoProduto[i] = precoProduto[i]
  print(f"O preço do(a) {nomeProduto[i]} é R${precoProduto[i]:.2f}")
