import mysql.connector

# CONEXION

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# CONEXION CORRECTA
#print(database)

# CURSOS
cursor = database.cursor(buffered=True)

"""
# CREAR BASES DE DATOS
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""

# CREAR TABLAS
cursor.execute("""
CREATE TABLE IF NOT EXISTS VEHICULOS(
ID int(10) AUTO_INCREMENT NOT NULL,
MARCA VARCHAR(40) NOT NULL,
MODELO VARCHAR(40) NOT NULL,
PRECIO FLOAT(10,2) NOT NULL,
CONSTRAINT PK_VEHICULO PRIMARY KEY(ID)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

#cursor.execute("INSERT INTO VEHICULOS VALUES (NULL, 'OPEL', 'ASTRA', '18500')")
coches = [
    ('SEAT','IBIZA','5000'),
    ('RENAULT','TRIPIO','15000'),
    ('CITROEN','SAXO','2000'),
    ('MERCEDEZ','CLASE C','35000'),
]

#cursor.executemany("INSERT INTO VEHICULOS VALUES (NULL, %s, %s, %s )", coches)

#database.commit()

cursor.execute("SELECT * FROM VEHICULOS")
resultado = cursor.fetchall()

print("-----TODOS LOS COCHES-----")
for coche in resultado:
    print(coche)

cursor.execute("DELETE FROM VEHICULOS WHERE MARCA = 'MERCEDEZ'")
database.commit()

print(cursor.rowcount, "BORRADOS")

# ACTUALIZAR 
cursor.execute("UPDATE VEHICULOS SET MODELO = 'LEON' WHERE MARCA = 'SEAT'")
database.commit()
print(cursor.rowcount, "ACTUALIZADOS")