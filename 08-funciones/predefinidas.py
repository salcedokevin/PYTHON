nombre = "Kevin S"

# FUNCIONES GENERALES
print(nombre)
print(type(nombre))

# DETECTA EL TIPADO
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variables es un String")
else:
    print("No es un String")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# LIMPIAR ESPACIOS
frase = "    mi contenido   "
print(frase)
print(frase.strip())

# ELIMINAR VARIABLES
year = 2024
print(year)
del year
#print(year)

# COMPROBAR VARIABLES VACIAS
texto = "ff     "
if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido", len(texto))

# ENCONTRAR CARACTERES DENTRO DE UN STRING
frase = "La vida es bella"
print(frase.find("vida"))

# REEMPLAZAR PALABRAS EN UN STRING
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# REEMPLAZAR MAYUSCULAS Y MINUSCULAS
print(nombre)
print(nombre.lower())
print(nombre.upper())