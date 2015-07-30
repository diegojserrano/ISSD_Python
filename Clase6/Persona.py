class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def __str__(self):
        return self.nombre+ ' ' + self.apellido

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

p1 = Persona("juan", "perez")
p2 = Persona("juana", "pereza")

print(p1)
print(p2)
p1.nombre = "asdfasdf"

print(p1)