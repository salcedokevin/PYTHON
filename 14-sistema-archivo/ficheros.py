from io import open
import pathlib
import shutil
import os

# ABRIR ARCHIVO
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivo/ficheros_texto.txt"
archivo = open(ruta, "a+")

# ESCRIBIR DENTRO DE UN ARCHIVO
#archivo.write("*************SOY UN TEXTO DESDE PYTHON*************\n")

#CERRAR ARCHIVO
archivo.close()

# LEER ARCHIVO
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivo/ficheros_texto.txt"
archivo_lectura = open(ruta, "r")

#contenido = archivo_lectura.read()
#print(contenido)

# LEER CONTENIDO Y GUARDARLO EN LISTA
lista = archivo_lectura.readlines()
archivo_lectura.close()

for elemento in lista:
    if elemento.isnumeric():
        print("- " + elemento.lower())
"""
# COPIAR ARCHIVO
ruta_original = str(pathlib.Path().absolute()) + "/14-sistema-archivo/ficheros_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivo/ficheros_copiado.txt"
ruta_alternativa = "../14-sistema-archivo/ficheros_copiado.txt"

shutil.copyfile(ruta_original, ruta_nueva)
"""

# MOVER ARCHIVO
ruta_original = str(pathlib.Path().absolute()) + "/14-sistema-archivo/ficheros_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivo/ficheros_copiado_NUEVO.txt"

#shutil.move(ruta_original, ruta_nueva)

# ELIMINAR ARCHIVO
ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivo/ficheros_copiado_NUEVO.txt"
#os.remove(ruta_nueva)

# COMPROBAR SI EXISTE ARCHIVO
import os.path

#print(os.path.abspath("./"))
ruta_comprobar = os.path.abspath("./") + "/14-sistema-archivo/ficheros_texto.txt"

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")