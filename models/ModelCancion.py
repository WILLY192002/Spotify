from .entities.Canciones import Canciones

class ModelCanciones():
    @classmethod
    def filtrar(self, db, filtro):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, nombre, autor, genero_id FROM proyecto_spotify.canciones"
            if filtro:
                condiciones = []

                for clave, valor in filtro.items():
                    condiciones.append(f"{clave} = '{valor}'")

                sql += " WHERE " + (" AND ".join(condiciones))
                print(sql)
            cursor.execute(sql)
            rows = cursor.fetchall()
            Salida = []
            if rows is not None:
                for i in rows:
                    Cancion = Canciones(i[0], i[1], i[2], i[3])
                    Salida.append(Cancion)
                return Salida
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def agregar(self, db, cancion):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO proyecto_spotify.canciones (nombre, autor, genero_id) VALUES ('{}', '{}', {})".format(cancion.nombre, cancion.autor, cancion.generoid)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
