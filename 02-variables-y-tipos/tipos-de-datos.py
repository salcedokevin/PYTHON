nada = None
cadena = "hola soy kevin salcedo"
entero = 12
flotante = 5.9
boleano = True
lista = [10, 20, 30, 40, 200]
listaString = [44, "cincuenta", 13, 2.5]
TuplaNoCambia = ("master", "en", "python")
diccionario = {
    "nombre": "kevin",
    "apellido": "salcedo",
    "edad": "27"
}
rango = range(9)
dato_bite = b"probando"

print(nada)
print(rango)
print(dato_bite)

# mostrar tipo de datos
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(boleano))
print(type(lista))
print(type(listaString))
print(type(TuplaNoCambia))
print(type(diccionario))
print(type(rango))
print(type(dato_bite))

# convertir tipos de datos
texto = "soy un texto"
numerito = str(27)

print(type(numerito))

print(texto + " " + numerito)

numerito = int(776)
print(type(numerito))

numerito = float(776)
print(numerito)