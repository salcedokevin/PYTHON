"""
Diccionario es un tipo de dato que almacena un grupo de datos en formato clave valor
parecido a un array  asociativo o un objeto tipo json
"""

persona = {
    "nombre": "Victor",
    "apellido": "robles",
    "web": "victorroblesweb.com"
}

print(type(persona))
print(persona["apellido"])

# lista con diccionario

contactos = [
    {
        "nombre": "kevin",
        "mail": "salcedo.kevin.31@gmail.com"
    },
    {
        "nombre": "luis",
        "mail": "luis.gaa@gmail.com"
    },
    {
        "nombre": "salvador",
        "mail": "salvador.com@gmail.com"
    }
]

contactos[0]["nombre"] = "kevincito"
print(contactos[0]["nombre"])

for contacto in contactos:
    print(f"El nombre del contacto es: {contacto["nombre"]}")
    print(f"El mail del contacto es: {contacto["mail"]}")
    print("------------------")