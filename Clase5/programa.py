import sys

for path in sys.path:
    print(path)

import funciones

#Llamada con el nombre completo
print(funciones.sumar(3,6))
print(funciones.restar(3,6))

#Asignacion de una variable tipo funcion
s = funciones.sumar

print(s(3,5))

#Importacion al espacio de nombres propio
from funciones import *

print(restar(4,5))
