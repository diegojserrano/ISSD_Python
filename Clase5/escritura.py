f = open("salida.txt","w")

hora = "20:40"
codigo = 56776
mensaje = "Error de red"

formato = "[{0}] - {1} : {2}"

f.write(formato.format(hora, codigo, mensaje))
f.write(formato.format(hora, codigo, mensaje))


f.close()
