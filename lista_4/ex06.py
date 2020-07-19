"""Faça um programa que carregue um vetor com dez nomes e faça uma verificação se um determinado nome esta nesse vetor. Se não conter o nome pesquisado informe que não encontrou. A frase "Não encontrou", quando for o caso deverá ser apresentada APENAS UMA VEZ."""
nome = []
i = 0
while i <= 2:
    nome.append(str(input(f"Informe o nome da {i + 1}a pessoa para inseri-la na lista: ")).casefold())
    i += 1
checarNome = str(input("Digite o nome para verificar se ele existe na lista -> ").casefold())
if checarNome in nome:
    print(f"O nome '{checarNome}' está na lista")
else:
    print(f"O nome '{checarNome}' não foi encontrado na lista")
