x = input('Insira algo: ')
print('O tipo primitivo é: ', type(x)) #comando type(variável) verifica o tipo da variável
print('Só tem espaços? ', x.isspace()) #.isspace verifica se só há espaços no input
print('E um número? ', x.isnumeric())#.isnumeric verifica se só há números
print('E alfabético? ', x.isalpha())#.isalpha verifica se só há letras
print('E alfanumérico? ', x.isalnum())#.isalnum verifica se é alfanumérico
print('Está só em letras maiúsculas? ', x.isupper())#.isupper verifica se só tem letras maiúsculas
print('Está só em letras minúsculas? ', x.islower())#.islower verifica se só tem letras minúsculas
print('Está só com a primeira letra maiúscula? ', x.istitle())#.istitle verifica se a primeira letra está capitalizada