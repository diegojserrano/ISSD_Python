from Clase7.Academia import *
import random

def llenar(alumno):
    c = random.randint(0,5)
    for i in range(c):
        alumno.agregar_nota(random.randint(0,10))


cursos = []

ingles1 = Curso("Ingles Inicial")
ingles2 = Curso("Ingles Intermedio")
ingles3 = Curso("Ingles Avanzado")
frances = Curso("Frances Inicial")

cursos.append(ingles1)
cursos.append(ingles2)
cursos.append(ingles3)
cursos.append(frances)

alumno11 = Alumno("Juan", 11)
alumno12 = Alumno("APedro", 12)
alumno21 = Alumno("Luis", 21)
alumno31 = Alumno("Ana", 31)
alumno41 = Alumno("Maria", 41)
alumno42 = Alumno("Susana", 42)

print (alumno11 < alumno12)

ingles1 += alumno12
ingles1 += alumno11
ingles2 += alumno21
ingles3 += alumno31
frances += alumno42

llenar(alumno11)
llenar(alumno12)
llenar(alumno21)
llenar(alumno31)
llenar(alumno42)


for curso in cursos:
    print(curso)
    bajos = curso.alumnos_promedio_bajo()
    for alu in bajos:
        print(alu)


