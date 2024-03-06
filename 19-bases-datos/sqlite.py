# IMPORTAR MODULO
import sqlite3

# CONEXION
conexion = sqlite3.connect('./19-bases-datos\pruebas.db')

# CREAR CURSOR
cursor = conexion.cursor()

# CREAR TABLA
cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS("+
"ID INTEGER PRIMARY KEY AUTOINCREMENT,"+
"TITULO VARCHAR(255), "+
"DESCRIPCION TEXT, "+
"PRECIO INT(255)"+
")")

# GUARDAR CAMBIOS
conexion.commit()

# INSERTAR DATOS
cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL, 'SEGUNDO PRODUCTO', 'DESCRIPCION PRODUCTO', 550)")
conexion.commit()

# LISTAR DATOS
cursor.execute("SELECT * FROM PRODUCTOS")
PRODUCTOS = cursor.fetchall()

for elemento in PRODUCTOS:
    print("Titulo: ", elemento[1])
    print("Descripcion: ", elemento[2])
    print("\n")

cursor.execute("SELECT TITULO FROM PRODUCTOS")
PRODUCTOS = cursor.fetchone()
print(PRODUCTOS)

# CERRAR CONEXION
conexion.close()

