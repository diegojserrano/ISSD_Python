def cargarConj(conj):
    cantidad = int(input("Ingrese la cantidad de elementos: "))
    for i in range(cantidad):
        conj.add(int(input("Ingrese un numero: ")))


conj1 = set()
conj2 = set()

cargarConj(conj1)
cargarConj(conj2)

#interseccion = set()
#for a in conj1:
#    if a in conj2:
#        interseccion.add(a)

interseccion = conj1 & conj2

print(interseccion)