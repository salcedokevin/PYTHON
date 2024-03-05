# CAPTURAR EXCEPCIONES Y MANJEAR ERRORES EN CODIGOS SUCEPTIBLES A ERRORES


try:
    nombre = input("Cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error")

else:
    print("Todo funciona bien")