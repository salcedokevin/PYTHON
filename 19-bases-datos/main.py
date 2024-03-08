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
cursor = database.cursor()

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