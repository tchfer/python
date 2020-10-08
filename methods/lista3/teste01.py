# retorno sem valor

def dividir():
    a = float(input("Informe um número: "))
    b = float(input("Informe um número: "))
    if b == 0.0:
        print("Divisão por zero!")
        return
    print("Resultado da divisão: ", a / b)
    
def main():
    dividir()
    
main()