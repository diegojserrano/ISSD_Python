equipos = []

equipos.append(("Boca",23,19,0.235))
equipos.append(("River",26,3,0.122))
equipos.append(("Belgrano",12,-5,1.8))
equipos.append(("Talleres",9,1,2.7))

formato = "{0:10}: Puntos {1:3d} - Dif. goles {2:3d} - Prom {3:1.5f}\n"

f = open("salida.txt","w")


for equipo in equipos:
    f.write(formato.format(equipo[0],equipo[1],equipo[2],equipo[3]))

f.close()

