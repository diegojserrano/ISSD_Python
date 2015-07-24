equipos = []

equipos.append(("Boca",23,19,0.235))
equipos.append(("River",26,3,0.122))
equipos.append(("Belgrano",12,-5,1.8))
equipos.append(("Talleres",9,1,2.7))

import json

f = open("equipos.txt","w")
f.write(json.dumps(equipos))
f.close()

