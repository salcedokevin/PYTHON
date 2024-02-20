"""
SET es un tipo de dato para tener una coleccion de valores,
pero no tiene ni indice ni orden
"""

personas = {
    "victor",
    "manolo",
    "francisco"
}

personas.add("paco")
personas.remove("francisco")

print(type(personas))
print(personas)