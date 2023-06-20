from .entities.User import User

class ModelUser():

    @classmethod
    def login(self,db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, name, email, password, username FROM user
                     WHERE email ='{}'""".format(user.email)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2], User.check_password(row[3], user.password), row[4])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self,db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, name, email, username FROM user
                     WHERE id ='{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2], None, row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)