class Config:
    SECRET_KEY = "BItWeNAt1T^SkvhUI*S^"

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123lapopo123'
    MYSQL_DB = 'spotifyproyeto'

config = {
    'development':DevelopmentConfig
}