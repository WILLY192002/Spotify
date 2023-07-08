from .entities.TablaUser import TablaUser
class ModelAddToUser():
    @classmethod
    def AddToUser(self, db, usuario_id, nombrecancion, autor, genero_id, foto, ilike):
        Tabla = "TableUser"+str(usuario_id)
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO proyecto_spotify."+Tabla+" (usuario_id, nombrecancion, autor, genero_id, foto, ilike) VALUES ({},'{}','{}',{},{},{})".format(usuario_id, nombrecancion, autor, genero_id, foto, ilike)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def EditToUser(self, db,id_r , usuario_id, editar):
        Tabla = "TableUser"+str(usuario_id)
        try:
            cursor = db.connection.cursor()
            columnas_valores = ', '.join([f"{columna} = '{valor}'" for columna, valor in editar.items()])
            sql = "UPDATE proyecto_spotify."+Tabla+f" SET {columnas_valores} WHERE id = {id_r}"
            #sql = "UPDATE proyecto_spotify."+Tabla+" SET nombrecancion = '{}', autor = '{}', genero_id = {}, foto = {} WHERE id = {}".format(nombrecancion, autor, genero_id, foto, id_r)
            print("Consulta update: ", sql)
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
            sql = "SELECT id, usuario_id, nombrecancion, autor, genero_id, foto, ilike FROM proyecto_spotify."+Tabla
            if filtros:
                condiciones = []

                for clave, valor in filtros.items():
                    condiciones.append(f"{clave} = '{valor}'")

                sql += " WHERE " + (" AND ".join(condiciones))
            cursor.execute(sql)
            rows = cursor.fetchall()
            salida = []
            if rows != None:
                for i in rows:
                    Tablauser = TablaUser(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                    salida.append(Tablauser)
                return salida
            else:
                return False
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def filter(self, db, usuario_id, filtrosOR, filtrosAND):
        Tabla = "TableUser"+str(usuario_id)
        try:
            cursor = db.connection.cursor()
            
            sql = "SELECT id, usuario_id, nombrecancion, autor, genero_id, foto, ilike FROM proyecto_spotify."+Tabla
            if filtrosOR:
                sql += " WHERE ("
                condiciones = []

                for clave, valor in filtrosOR.items():
                    condiciones.append(f"{clave} {valor}")

                sql += " OR ".join(condiciones)
                sql += ")"

            if filtrosAND:
                condiciones = []
                for clave, valor in filtrosAND.items():
                    condiciones.append(f"{clave} {valor}")

                if filtrosOR and filtrosOR:
                    sql += " AND "+condiciones[0]
                else:
                    sql += " WHERE "+condiciones[0]
            
            cursor.execute(sql)
            rows = cursor.fetchall()
            salida = []
            if rows != None:
                for i in rows:
                    Tablauser = TablaUser(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                    salida.append(Tablauser)
                return salida
            else:
                return False
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def join(self, db, usuario_id,):
        Tabla = "TableUser"+str(usuario_id)
        try:
            cursor = db.connection.cursor()
            sql = "SELECT U.id, U.usuario_id, U.nombrecancion, U.autor, G.nombre, U.foto, U.ilike FROM proyecto_spotify."+Tabla+" AS U INNER JOIN proyecto_spotify.generomusica AS G ON U.genero_id = G.id" 
            cursor.execute(sql)
            rows = cursor.fetchall()
            salida = []
            if rows != None:
                for i in rows:
                    Tablauser = TablaUser(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                    salida.append(Tablauser)
                return salida
            else:
                return False
        except Exception as ex:
            raise Exception(ex)