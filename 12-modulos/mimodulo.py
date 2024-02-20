def holaMundo(nombre):
    return f"Que tal estas {nombre}"

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