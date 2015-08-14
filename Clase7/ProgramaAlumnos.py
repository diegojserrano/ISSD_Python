
from Clase7.Academia import Alumno

curso = []

cantidad = int(input("Ingrese la cantidad de alumnos: "))

for i in range(cantidad):
    legajo = int(input("Ingrese el legajo: "))
    nombre = input("Ingrese el nombre: ")
    a = Alumno(nombre, legajo)
    curso.append(a)

print(len(curso))

for a in curso:
    print(str(a.legajo) + ": " + str(a.nombre))

cantidadNotas = int(input("Ingrese la cantidad de examenes"))
for i in range(cantidadNotas):
    legajo = int(input("Ingrese el legajo"))
    nota = int(input("Ingrese la nota"))

    for alu in curso:
        if legajo == alu.legajo:
            alu.agregar_nota(nota)
            print("nota agregada")
            break
    else:
        print("el legajo no existe")

for alu in curso:
    print(alu.nombre + ": " + str(alu.promedio()))

