# IMPORTAR MODULO
import sqlite3

# CONEXION
conexion = sqlite3.connect('./19-bases-datos\pruebas.db')

# CREAR CURSOR
cursor = conexion.cursor()

# CREAR TABLA
cursor.execute("""
CREATE TABLE IF NOT EXISTS PRODUCTOS(
    "ID INTEGER PRIMARY KEY AUTOINCREMENT,
    "TITULO VARCHAR(255),
    "DESCRIPCION TEXT,
    "PRECIO INT(255)
);
""")

# GUARDAR CAMBIOS
conexion.commit()

# INSERTAR DATOS
"""
cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL, 'SEGUNDO PRODUCTO', 'DESCRIPCION PRODUCTO', 550)")
conexion.commit()
"""

# BORRAR REGISTROS
cursor.execute("DELETE FROM PRODUCTOS")
conexion.commit()

# INSERTAR MUCHOS REGISTROS A LA VEZ
productos = [
    ("Ordenador portatil", "Buen pc", 700),
    ("tablet", "15 pulgadas", 500),
    ("PC", "gaaaa", 1800),
]
cursor.executemany("INSERT INTO PRODUCTOS VALUES (null, ?,?,?)", productos)
conexion.commit()

# ACTUALIZAR DATOS
cursor.execute("UPDATE PRODUCTOS SET PRECIO = 1200 WHERE PRECIO = 500")
conexion.commit()

# LISTAR DATOS
cursor.execute("SELECT * FROM PRODUCTOS WHERE PRECIO >= 500;")
PRODUCTOS = cursor.fetchall()

for elemento in PRODUCTOS:
    print("ID: ", elemento[0])
    print("Titulo: ", elemento[1])
    print("Descripcion: ", elemento[2])
    print("Precio: ", elemento[3])
    print("\n")

cursor.execute("SELECT TITULO FROM PRODUCTOS")
PRODUCTOS = cursor.fetchone()
print(PRODUCTOS)

# CERRAR CONEXION
conexion.close()

