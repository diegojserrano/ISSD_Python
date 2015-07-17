def mayor(lista):
    mayor = lista[0]
    c = 0
    pos = 0
    for valor in lista:
        if valor > mayor:
            mayor = valor
            pos = c
        c = c + 1

    return mayor,pos

cantidad = int(input("Ingrese la cantidad de elementos: "))
lista = []
for i in range(cantidad):
    lista.append(int(input("Ingrese un numero: ")))

m = mayor(lista)
for x in m: print(x)