from urllib.request import urlopen

respuesta = urlopen("http://www.lavoz.com.ar")

for l in respuesta:
    linea = str(l)
    if (linea.find("<a")>0):
        print(l)

