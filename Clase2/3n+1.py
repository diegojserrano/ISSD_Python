def longitud(x):
    c = 1
    while x != 1:
        if x % 2 == 1:
            x = x * 3 + 1
        else:
            x = x / 2
        c += 1

    return c

def longitudMaxima (i, j):
    mayor = 0

    for n in range(i,j+1):
        c = longitud(n)
        if c > mayor: mayor = c

    return mayor

def cargarDatos():
    i = int(input())
    j = int(input())
    return i, j

def principal():
    i, j = cargarDatos()

    while (i != 0) and (j != 0):
        print (longitudMaxima(i, j))
        i, j = cargarDatos()


principal()
