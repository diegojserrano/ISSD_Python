def cargarLista(lista):
    cantidad = int(input("Ingrese la cantidad de elementos: "))
    for i in range(cantidad):
        lista.append(int(input("Ingrese un numero: ")))


lista1 = []
lista2 = []

cargarLista(lista1)
cargarLista(lista2)

lista3 = []

print(lista1)
print(lista2)
for a in lista1:
    for b in lista2:
        if a == b and not a in lista3:
                lista3.append(a)


for x in lista3: print(x)