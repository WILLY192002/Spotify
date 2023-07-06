class ModelCrearTabla():
    @classmethod
    def CrearTablaUsurio(self, db, usuario_id):
        nombreTabla = "TableUser"+str(usuario_id)
        try:
            cursor = db.connection.cursor()
            sql = "CREATE TABLE "+nombreTabla+ """(id INT PRIMARY KEY AUTO_INCREMENT,
                    usuario_id INT NOT NULL,
                    nombrecancion VARCHAR(100) NOT NULL,
                    autor VARCHAR(100) NOT NULL,
                    genero_id INT NOT NULL,
                    foto BOOLEAN NOT NULL,
                    ilike BOOLEAN NOT NULL,
                    FOREIGN KEY (usuario_id) REFERENCES user(id),
                    FOREIGN KEY (genero_id) REFERENCES generomusica(id)
                );"""
            print(sql)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)