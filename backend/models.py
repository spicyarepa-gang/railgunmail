from vendors.database import db
from flask_login import UserMixin

class Roles(db.Model):
    __tablename__='roles'
    __table_args__={'schema':'public'}
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(300), nullable=False)

class Admin(UserMixin, db.Model):
    __tablename__='users'
    __table_args__={'schema':'public'}
    id = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, nullable=False)
    usuario = db.Column(db.String(50), nullable=False, unique=True)
    clave = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    temp = db.Column(db.String(100), nullable=True)

class GroupsTypes(db.Model):
    __table_args__={'schema':'public'}
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(300), nullable=False)

class Groups(db.Model):
    __table_args__={'schema':'public'}
    id = db.Column(db.Integer, primary_key=True)
    id_type = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(300), nullable=False)
    dependencia = db.Column(db.String(300), nullable=False)

class Contactos(db.Model):
    __table_args__={'schema':'public'}
    id = db.Column(db.Integer, primary_key=True)
    id_group = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(300), nullable=False)
    direccion = db.Column(db.String(500), nullable=False)
    telefono = db.Column(db.String(200), nullable=False)
    correo = db.Column(db.String(300), nullable=False)
    extension = db.Column(db.String(300), nullable=False)
    cargo = db.Column(db.String(300), nullable=False)
    departamento = db.Column(db.String(300), nullable=False)

# class SubGroups(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     id_group = db.Column(db.Integer, db.ForeignKey('groups.id'))
#     nombre = db.Column(db.String(300), nullable=False)
#     rel = db.relationship('Contactos', backref='SubGroups')