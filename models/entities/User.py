from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self, id, name, email, password, username):
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    @classmethod
    def set_password(self, password):
        return generate_password_hash(password)

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

