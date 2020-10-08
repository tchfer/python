# retorno com valor

def dividir():
    a = float(input("Informe um número: "))
    b = float(input("Informe um número: "))
    if b == 0.0:
        print("Divisão por zero!")
        return
    else:
        return a / b
    
def main():
    print("Resultado da divisão: ", dividir())
main()