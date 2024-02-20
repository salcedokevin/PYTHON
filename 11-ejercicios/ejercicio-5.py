"""
Crear una lista con el contenido de esta tabla:
ACCION  AVENTURA        DEPORTES
GTA     ASSASING        FIFA 21
COD     CRASH           PRO 21
PUBG    PRINCE PERSIA   MOTO GP 21

Mostrar esta informacion ordenada
"""
tabla = [
    {
        "Categoria": "Accion",
        "Juegos" : ["GTA", "COD", "PUBG"]
    },
    {
        "Categoria": "Aventura",
        "Juegos" : ["ASSASSINS", "CRASH", "PRINCE OF PERSIA"]
    },
    {
        "Categoria": "Deportes",
        "Juegos" : ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for catego in tabla:
    print(f"-------{catego['Categoria']}-------")
    for juego in catego['Juegos']:
        print(juego)