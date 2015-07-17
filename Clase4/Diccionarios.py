empleados = {1: "Juan", 2: "Pedro"}

print(empleados)

for e in empleados.values():
    print (e)

print("Empleado 2: ", empleados[2])
print(1 in empleados)

f = {x: x**2 for x in range(4)}

print(f)