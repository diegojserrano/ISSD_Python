def leerCodigos():
    archivo = open("CP.txt")
    codigos = []

    linea = archivo.readline()
    while linea != "":
        provincia = linea[0]
        codigo = int(linea[2:6])
        localidad = linea[7:].rstrip()
        codigos.append((provincia,codigo,localidad))
        linea = archivo.readline()

    return codigos


def buscarCP(lista, codigo):
    salida = []
    for c in lista:
        if c[1] == codigo:
            salida.append(c[2])

    return salida


def buscarLocalidad(lista, nombre):
    salida = []
    a = ""

    for c in lista:
        if c[2].find(nombre) != -1:
            salida.append(c)

    return salida

lista = leerCodigos()


codigoBuscado = int(input("Ingrese el codigo a buscar"))
print(buscarCP(lista,codigoBuscado))

localidad = input("Ingrese la localidad")
print(buscarLocalidad(lista,localidad))
