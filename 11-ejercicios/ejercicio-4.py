"""
script de 4 variables tipo lista, string, entero y booleano, el programa debe imprimir
que tipo de variables es cada una, usar funciones
"""

lista = ["Pepe", 5]
texto = "Hola"
entero = 123
boleano = True

def variables(dato, tipo):
    text = isinstance(dato, tipo)
    resultado = ""

    if text:
        resultado = f"Dato de tipo {type(tipo)}"
    else:
        resultado = "No es el tipo correcto CTM"
    return resultado

print(variables(lista, list))
print(variables(texto, str))
print(variables(entero, int))
print(variables(boleano, tuple))