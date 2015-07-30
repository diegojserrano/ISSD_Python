import json

def indexar(nombre):
    archivo = open(nombre)

    indice = list()

    linea = archivo.readline()

    while linea != "":
        palabras = linea.split()
        for palabra in palabras:
            if not palabra in indice:
                indice.append(palabra)
        linea = archivo.readline()

    archivo.close()
    return indice

def guardarIndice(indice,nombre):
    archivo = open(nombre,"w")
    json.dump(indice,archivo)
    archivo.close()

ind = indexar("pg21231.txt")
guardarIndice(ind,"pg21231.ind")
