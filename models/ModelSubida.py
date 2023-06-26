from .entities.Subida import Subida

class ModelSubida():
    @classmethod
    def filtrar(self, db, filtro):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT cancion_id FROM proyecto_spotify.subidas WHERE usuario_id = {}".format(filtro)
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