import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota():
    def __init__(self, usuario_id, titulo = "", descripcion = ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def Guardar(self):
        sql = "INSERT INTO NOTAS VALUES (NULL, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]
    
    def Listar(self):
        sql = f"SELECT * FROM NOTAS WHERE USUARIO_ID = {self.usuario_id}"

        cursor.execute(sql)
        resultado = cursor.fetchall()

        return resultado
    
    def Eliminar(self):
        sql = f"DELETE FROM NOTAS WHERE USUARIO_ID = {self.usuario_id} AND TITULO LIKE '%{self.titulo}%'"

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]