from .entities.TablaUser import TablaUser
class ModelAddToUser():
    @classmethod
    def AddToUser(self, db, usuario_id, nombrecancion, autor, genero_id, foto):
        Tabla = "TableUser"+str(usuario_id)
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO proyecto_spotify."+Tabla+" (usuario_id, nombrecancion, autor, genero_id, foto) VALUES ({},'{}','{}',{},{})".format(usuario_id, nombrecancion, autor, genero_id, foto)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def EditToUser(self, db,id_r , usuario_id, nombrecancion, autor, genero_id, foto):
        Tabla = "TableUser"+str(usuario_id)
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE proyecto_spotify."+Tabla+" SET nombrecancion = '{}', autor = '{}', genero_id = {}, foto = {} WHERE id = {}".format(nombrecancion, autor, genero_id, foto, id_r)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def deleteToUser(self, db,id_r , usuario_id):
        Tabla = "TableUser"+str(usuario_id)
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM proyecto_spotify."+Tabla+" WHERE id = {}".format(id_r)
            print("SQL: ", sql)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def Select(self, db, usuario_id, filtros):
        Tabla = "TableUser"+str(usuario_id)
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, usuario_id, nombrecancion, autor, genero_id, foto FROM proyecto_spotify."+Tabla
            if filtros:
                condiciones = []

                for clave, valor in filtros.items():
                    condiciones.append(f"{clave} = '{valor}'")

                sql += " WHERE " + (" AND ".join(condiciones))
                print(sql)
            cursor.execute(sql)
            rows = cursor.fetchall()
            salida = []
            if rows != None:
                for i in rows:
                    Tablauser = TablaUser(i[0], i[1], i[2], i[3], i[4], i[5])
                    salida.append(Tablauser)
                return salida
            else:
                return False
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def filter(self, db, usuario_id, filtros):
        Tabla = "TableUser"+str(usuario_id)
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, usuario_id, nombrecancion, autor, genero_id, foto FROM proyecto_spotify."+Tabla
            if filtros:
                sql += " WHERE "
                condiciones = []

                for clave, valor in filtros.items():
                    condiciones.append(f"{clave} LIKE '%{valor}%'")

                sql += " OR ".join(condiciones)
                print("LAQUE:",sql)
            cursor.execute(sql)
            rows = cursor.fetchall()
            salida = []
            if rows != None:
                for i in rows:
                    Tablauser = TablaUser(i[0], i[1], i[2], i[3], i[4], i[5])
                    salida.append(Tablauser)
                return salida
            else:
                return False
        except Exception as ex:
            raise Exception(ex)