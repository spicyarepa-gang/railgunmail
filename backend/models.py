from vendors.database import db
from flask_login import UserMixin

class Admin(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id'))
    usuario = db.Column(db.String(50), nullable=False, unique=True)
    clave = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    temp = db.Column(db.String(100), nullable=True)

class Roles(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(300), nullable=False)
    rel = db.relationship('Admin', backref='Roles')

class GroupsTypes(db.Model):
    __tablename__='groups_types'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(300), nullable=False)
    rel = db.relationship('Groups', backref='GroupsTypes')

class Groups(db.Model):
    __tablename__='groups'
    id = db.Column(db.Integer, primary_key=True)
    id_type = db.Column(db.Integer, db.ForeignKey('groups_types.id'))
    nombre = db.Column(db.String(300), nullable=False)
    dependencia = db.Column(db.String(300), nullable=False)
    rel = db.relationship('Contactos', backref='Groups')

class Contactos(db.Model):
    __tablename__='contactos'
    id = db.Column(db.Integer, primary_key=True)
    id_group = db.Column(db.Integer, db.ForeignKey('groups.id'))
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