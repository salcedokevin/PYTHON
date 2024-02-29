import os, shutil

# CREAR CARPETA
if not os.path.isdir("./14-sistema-archivo/mi_carpeta"):
    os.mkdir("./14-sistema-archivo/mi_carpeta")
else:
    print("Ya existe el directorio")

# ELIMINAR CARPETA
#os.rmdir("./14-sistema-archivo/mi_carpeta")
    
# COPIAR CARPETA
ruta_original = "./14-sistema-archivo/mi_carpeta"
ruta_nueva = "./14-sistema-archivo/mi_carpeta_copiada"

#shutil.copytree(ruta_original, ruta_nueva)

# ELIMINAR CARPETA
#os.rmdir("./14-sistema-archivo/mi_carpeta_copiada")

print("Contenido de mi carpeta")
contenido = os.listdir("./14-sistema-archivo/mi_carpeta")
print(contenido)

for fichero in contenido:
    print("Fichero: " + fichero)