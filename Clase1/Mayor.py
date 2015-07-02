mayor = 0
print("Ingrese 5 números")


for i in range(1,5,2):
    número = int(input("Ingrese un numero: "))
    if i == 0 or número > mayor:
        mayor = número

    else:
        mayor = número

print("El mayor es", mayor)
