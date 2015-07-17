def cargarConj(conj):
    cantidad = int(input("Ingrese la cantidad de elementos: "))
    for i in range(cantidad):
        conj.add(int(input("Ingrese un numero: ")))


#conj1 = set()
#conj2 = set()

#cargarConj(conj1)
#cargarConj(conj2)

conj1 = {x for x in range(4) if x % 2 == 0}
conj2 = {x for x in range(3,8)}

print(conj1)
print(conj2)
#interseccion = set()
#for a in conj1:
#    if a not in conj2:
#        interseccion.add(a)

diferencia = conj1 - conj2
print(diferencia)

union = conj1 | conj2
print(union)

unionexcl = conj1^conj2
print(unionexcl)