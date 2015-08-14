class Alumno:

    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0: return 0
        ac = 0

        for nota in self.notas:
            ac += nota

        return ac / len(self.notas)

    def __str__(self): # equivalente al metodo toString de java y .net
        return str(self.legajo) + " - " + self.nombre + ": " + str(self.promedio())

    def __lt__(self, other):  #lower than
        return self.nombre < other.nombre

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def inscribir_alumno(self, alumno):
        self.alumnos.append(alumno)

    def promedio(self):
        if len(self.alumnos) == 0: return 0
        ac = 0

        for alu in self.alumnos:
            ac += alu.promedio()

        return ac / len(self.alumnos)

    def alumnos_promedio_bajo(self):
        salida = []
        for alu in self.alumnos:
            if alu.promedio() < 5:
                salida.append(alu)

        return salida
        #return [alu for alu in self.alumnos if alu.promedio() < 5]

    def __str__(self):
        return self.nombre + ": " + str(self.promedio())

    def __iadd__(self, other):
        self.alumnos.append(other)
        return self
