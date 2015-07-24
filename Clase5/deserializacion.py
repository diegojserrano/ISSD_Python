f = open("equipos.txt","r")

contenido = f.read()

f.close()

import json

equipos = json.loads(contenido)

for e in equipos:
    print(e)
