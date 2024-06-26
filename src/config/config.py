from decouple import config

class Config():
    SECRET_KEY = config('JWT_SECRET')

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}