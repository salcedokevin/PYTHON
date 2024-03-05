# CAPTURAR EXCEPCIONES Y MANJEAR ERRORES EN CODIGOS SUCEPTIBLES A ERRORES
"""
try:
    nombre = input("Cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error")

else:
    print("Todo funciona bien")
finally:
    print("Fin de la iteracion")
"""
# MANEJAR MULTIPLES EXCEPCIONES
"""
try:
    numero = int(input("Dime el numero para elevarlo al cuadrado: "))
    print("El cuadrado es: " +str(numero*numero))

except TypeError:
    print("Debes convertir tus cadenas a enteros en el codigo")

#except ValueError:
#    print("Introduce un numero correcto")

except Exception as e:
    print(type(e))
    print("A ocurrido un error: ", type(e).__name__)
"""

# EXCEPCIONES PERSONALIZADAS O LANZAR EXCEPCIONES
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <=1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al master en python {nombre}")
except ValueError:
    print("Introduce correctamente los datos")
except Exception as e:
    print("Existe un error", e)