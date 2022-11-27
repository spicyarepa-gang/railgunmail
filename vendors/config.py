import os 
from datetime import timedelta


class Config(object):
    SECRET_KEY = os.urandom(16)
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('CONEXION_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #ckeditor
    CKEDITOR_PKG_TYPE = 'standard'
    CKEDITOR_HEIGHT = 350
    #mails
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'railgunmail069@gmail.com'
    MAIL_PASSWORD = 'cenielywcsjjekca'

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('CONEXION_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
