"""
Las listas o array son colecciones de datos/valores bajo un unico nombre,
para acceder a esos valores podemos usar un indice numerico
"""
pelicula = "Batman"

# DEFINIR LISTA
peliculas = ["Batman", "Spiderman", "Barman"]
cantantes = list(("Drake", "Daft Punk", "Linkin Park"))
years = list(range(2020, 2050))
variada = ["Victor", 10, 2.5, True]

"""
print(pelicula)
print(peliculas)
print(len(peliculas))
print(cantantes)
print(years)
print(variada)
"""

# INDICES
pelicula = "otra cosa"
peliculas[1] = "Gran Torino"


print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:2])
print(peliculas[1:])

# AÑADIR ELEMENTOS A LISTA
cantantes.append("La Mente")
print(cantantes)

# RECORRER LISTA
nueva_peli = ""

while nueva_peli != "parar":
    nueva_peli = input(f"Introduce una nueva pelicula: ")

    if nueva_peli != "parar":
        peliculas.append(nueva_peli)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

# LISTA MULTIDIMENSIONALES
print("\n")

contactos = [
    ["antonio",
    "antonio.com"],
    ["luis",
     "luis.com"],
     ["salvador",
      "salvador.com"]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f"Nombre: {elemento}")
        else:
            print(f"Mail: {elemento}")
    #print(elemento)

#print(contactos[1][1])