import math

def distanciaAlOrigen(punto):
    x = punto[0]
    y = punto[1]
    return math.sqrt(x**2+y**2)

def distancia(punto1, punto2):
    dx = punto1[0] - punto2[0]
    dy = punto1[1] - punto2[1]
    return math.sqrt(dx**2+dy**2)

puntoA = 1,1
puntoB = 1,2

print(distanciaAlOrigen(puntoA))
print(distancia(puntoA,puntoB))