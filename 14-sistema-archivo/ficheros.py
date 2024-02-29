from io import open
import pathlib

# ABRIR ARCHIVO
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivo/ficheros_texto.txt"
archivo = open(ruta, "a+")

# ESCRIBIR DENTRO DE UN ARCHIVO
archivo.write("*************SOY UN TEXTO DESDE PYTHON*************\n")

#CERRAR ARCHIVO
archivo.close()