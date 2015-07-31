class Equipo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.jugados = 0
        self.ganados = 0
        self.empatados = 0
        self.goles_recibidos = 0
        self.goles_realizados = 0

    def perdidos(self):
        return self.jugados - self.ganados - self.empatados

    def diferencia_goles(self):
        return self.goles_realizados - self.goles_recibidos

    def puntos(self):
        return self.ganados * 3 + self.empatados

    def __str__(self):
        return self.nombre + ": " + str(self.puntos()) + " puntos "

class Liga:
    def __init__(self):
        self.equipos = []

    def agregar_equipo(self,e):
        self.equipos.append(e)

    def primero(self):
        mayor = self.equipos[0]
        for e in self.equipos:
            if e.puntos() > mayor.puntos():
                mayor = e
        return mayor


cantidad = int(input("Ingrese la cantidad de equipos: "))
liga = Liga()
for i in range(cantidad):
    nombre = input("Ingrese el nombre del equipo: ")

    eq = Equipo(nombre)
    eq.ganados = int(input("Ingrese la cantidad de partidos ganados: "))
    eq.empatados = int(input("Ingrese la cantidad de partidos empatados: "))
    print(eq)
    liga.agregar_equipo(eq)

print(liga.primero())