i = int(input(print("Ingrese un nro: ")))
j = int(input(print("Ingrese un nro: ")))

mayor=0

for n in range(i,j+1):

    c=1
    x=n

    while x!=1:

        if x % 2 == 1:
            x = (x*3)+1
        else:
            x = x//2

        c+=1

    if c > mayor:
        mayor=c

print(i,j,mayor)
