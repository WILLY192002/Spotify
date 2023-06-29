class ModelCrearTabla():
    @classmethod
    def CrearTablaUsurio(self, db, usuario_id):
        nombreTabla = "TableUser"+str(usuario_id)
        try:
            cursor = db.connection.cursor()
            sql = "CREATE TABLE "+nombreTabla+ """(id INT PRIMARY KEY AUTO_INCREMENT,
                    usuario_id INT,
                    nombrecancion VARCHAR(100),
                    autor VARCHAR(100),
                    genero_id INT,
                    foto BOOLEAN,
                    FOREIGN KEY (usuario_id) REFERENCES user(id),
                    FOREIGN KEY (genero_id) REFERENCES generomusica(id)
                );"""
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)