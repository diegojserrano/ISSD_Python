class Persona:
    def __init__(self, nombre, apellido, documento, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.edad = edad

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor >= 0 and valor <= 120:
            self.__edad = valor

    def __str__(self):
        return "Persona: nombre = " + self.nombre + \
               " - documento = " + str(self.documento) + \
               " - edad = " + str(self.edad)

    def nombreCompleto(self):
        return self.nombre + " " + self.apellido






#
#    def nombre(self):
#        return self.__nombre
#
#    @nombre.setter
#    def nombre(self, valor):
#        self.__nombre = valor
