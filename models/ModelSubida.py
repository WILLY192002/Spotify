from .entities.Subida import Subida

class ModelSubida():
    @classmethod
    def filtrar(self, db, filtro):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM proyecto_spotify.subidas WHERE usuario_id = {} AND cancion_id = {}".format(filtro[0], filtro[1])
            cursor.execute(sql)
            rows = cursor.fetchall()
            Salida = []
            if rows is not None:
                for i in rows:
                    subida = Subida(i[0], i[1])
                    Salida.append(subida)
                return Salida
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def agregar(self, db, subida):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO proyecto_spotify.subidas (usuario_id, cancion_id) VALUES ('{}', '{}')".format(subida.id_user, subida.id_cancion)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def User_join_Cancion(self, db, id_user):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT c.autor, c.nombre, c.foto FROM proyecto_spotify.canciones c JOIN proyecto_spotify.subidas s ON c.id = s.cancion_id JOIN proyecto_spotify.user u ON s.usuario_id = u.id WHERE u.id = {} AND s.activo = 1".format(id_user) 
            cursor.execute(sql)
            rows = cursor.fetchall()
            Salida = []
            if rows is not None:
                for i in rows:
                    información = [id_user,i[0], i[1], i[2]]
                    Salida.append(información)
                return Salida
            else:
                return None
        except Exception as ex:
            raise Exception(ex)