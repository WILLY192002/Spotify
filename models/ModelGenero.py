from .entities.Genero import Genero

class ModelGenero():
    @classmethod
    def Select(self, db, filtro):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, nombre FROM proyecto_spotify.generomusica"
            if filtro:
                sql += " WHERE nombre = '{}'".format(filtro)
                
            cursor.execute(sql)
            rows = cursor.fetchall()
            Salida = []
            if rows is not None:
                for i in rows:
                    generos = Genero(i[0], i[1])
                    Salida.append(generos)
                return Salida
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def Insert(self, db, new_genero):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO proyecto_spotify.generomusica (nombre) VALUE ('{}')".format(new_genero)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)