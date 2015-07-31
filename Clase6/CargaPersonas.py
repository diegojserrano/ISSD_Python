from Clase6.Persona import Persona

listaPersonas = []

for i in range(3):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    documento = int(input("Ingrese el documento: "))
    edad = int(input("Ingrese la edad: "))

    p = Persona(nombre, apellido, documento, edad)

    p.edad = 200

    print(p.nombreCompleto())
    listaPersonas.append(p)

for p in listaPersonas:
    print(p)


