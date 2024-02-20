"""
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre concreto que puede reusarse
invocando a la funcion tantas veces como sea necesario:

crear funcion:
def nombreDeLaFuncion(parametros):
    # bloque / conjunto de instrucciones

invocar funcion:
nombreDeLaFuncion(mi_parametro)
"""

##### EJEMPLO 1: CREAR FUNCION #####
def mostrarNombres():
    print("Kevin")
    print("Luis")
    print("Sanchez")
    print("\n")

# LLAMAR FUNCION
mostrarNombres()

##### EJEMPLO 2: PARAMETROS #####
def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("El usuario el mayor de edad")
    else:
        print("El usuario es menor de edad")
#nombre = input(f"Introduce tu nombre: ")
#edad = int(input(f"Introduce tu edad: "))

#mostrarTuNombre(nombre, edad)

##### EJEMPLO 3 #####
def tabla(numero):
    print(f"Tabla de multiplicar de {numero}")
    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")

numero = int(input(f"Escriba el numero a multiplicar: "))

tabla(numero)

##### EJEMPLO 3.1 #####
for numero_tabla in range(1,11):
    tabla(numero_tabla)

##### EJEMPLO 4: PARAMETROS OPCIONALES #####
def getEmpleado(nombre, dni = None):
    print(f"\nEL nombre es: {nombre}")
    if dni != None:
        print(f"El DNI es: {dni}")

getEmpleado("Kevin S")

##### EJEMPLO 5: RETURN O DEVOLVER DATOS #####
def saludame(nombre):
    saludame = f"Hola saludos {nombre}"
    return saludame

print(saludame("Kevin"))

##### EJEMPLO 6: RETURN O DEVOLVER DATOS #####
def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""
    if basicas != False:
        cadena += f"\nSuma es: {str(suma)}"
        cadena += f"\nResta es: {str(resta)}"
    else:
        cadena += f"\nMultiplicacion es: {str(multi)}"
        cadena += f"\nDivision es: {str(division)}"

    return cadena

print(calculadora(55, 5, True))

##### EJEMPLO 7: FUNCIONES DENTRO DE OTRAS #####
def getNombre(nombre):
    texto = f"\nEl nomres es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(devuelveTodo("Kevin", "Salcedo"))

##### EJEMPLO 7: FUNCIONES LAMBDA #####
dime_el_year = lambda year: f"\nEl año es {year}"

print(dime_el_year(2024))