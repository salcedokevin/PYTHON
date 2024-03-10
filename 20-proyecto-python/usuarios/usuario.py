import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # CIFRAR CONTRASEÑA
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO USUARIOS VALUES (NULL, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            return [cursor.rowcount, self]
        except:
            result = [0, self]
        return result

    def identificar(self):
        sql = "SELECT * FROM USUARIOS WHERE EMAIL = %s AND PASSWORD = %s"

        # CIFRAR CONTRASEÑA
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # DATOS PARA LA CONSULTA
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        resultado =  cursor.fetchone()

        return resultado