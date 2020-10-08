'''5. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne mostrando a str/string ‘É par’ ou se ‘É ímpar’.'''

def par_impar():
    n = int(input('Type a whole number -> '))
    if n % 2 == 0:
        print('Su número es par, papi')
        return
    print('É ímpar, mano!!!')

def main():
    par_impar()

main()