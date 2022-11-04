from vendors.database import db
from flask_login import UserMixin

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), nullable=False, unique=True)
    clave = db.Column(db.String(100), nullable=False)


class Contactos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(300), nullable=False)
    direccion = db.Column(db.String(500), nullable=False)
    telefono = db.Column(db.String(200), nullable=False)
    correo = db.Column(db.String(300), nullable=False)
    extencion = db.Column(db.String(300), nullable=False)
    cargo = db.Column(db.String(300), nullable=False)
    departamento = db.Column(db.String(300), nullable=False)