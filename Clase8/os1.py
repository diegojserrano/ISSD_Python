import os


print(os.getcwd())

os.chdir("/datos/Dropbox/ISSD/Ejercicios")

print(os.system("ls -l"))

for a in os.listdir():
    print(a)

os.chdir("./Clase1")

import glob

print("Glob: ",glob.glob("M*.py"))

for a in os.listdir():
    print(a)


os.chdir("..")

print("Resultado de walk")
recorrido = os.walk(".")
for d in recorrido:
    nombre, carpetas, archivos = d
    if not nombre.startswith("./.git"):
        print("Nombre = " + nombre)
        print("Carpetas = " + str(carpetas))
        print("Archivos = " + str(archivos))
        for arch in archivos:
            nombrec = os.path.join(nombre, arch)
            print(nombrec, os.path.getsize(nombrec))






print(os.getcwd())
print(os.environ)
print(os.getenv('PATH'))

name = os.uname()

for x in name:
    print(x)

import platform
for x in platform.uname():
    print(x)

import shutil

shutil.make_archive("/datos/Dropbox/ISSD/Ejercicios/Curso","zip")

# De os
#     getcwd
#     chdir
#     mkdir
#     rmdir
#     listdir
#     walk
#     system
# De os.path
#     join
#     getsize
# De platform
#     uname
#
# De shutil
#     copyfile
#     copytree
#     move
#     makearchive
# De glob
#     glob
