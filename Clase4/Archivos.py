
f = open("numeros.txt")


#linea = f.readline()
#while linea != "":
#    print(linea.rstrip())
#    linea = f.readline()
#
#f.close()

#f = open("numeros.txt")

#lista = list(f)
#lista = f.readlines()
#print(lista)

texto = f.read()
print(texto)

f.close()
#for x in lista: print(x.rstrip())

linea="3,4,6,6"
lista = linea.split(",")
print(lista)
#for x in lista: print(x.rstrip())
