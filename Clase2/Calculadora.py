def menu():
    print("Calculadora")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    return int(input("Ingrese la opcion deseada: "))

def ingresarOperandos():
    op1 = int(input("Ingrese el primer número: "))
    op2 = int(input("Ingrese el segundo número: "))
    return op1, op2

def sumar(op1, op2): return op1 + op2

def restar(op1, op2): return op1 - op2

def multiplicar(op1, op2): return op1 * op2

def dividir(op1, op2): return op1 / op2

operaciones = None, sumar, restar, multiplicar, dividir

opc = menu()
while opc != 5:
    op1, op2 = ingresarOperandos()
    print("El resultado es: ", operaciones[opc](op1, op2),"\n")
    opc = menu()
