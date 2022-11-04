from vendors.database import db
from flask_login import UserMixin

class Roles(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(300), nullable=False)
    rel = db.relationship('Admin', backref='Roles')

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id'))
    usuario = db.Column(db.String(50), nullable=False, unique=True)
    clave = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    temp = db.Column(db.String(100), nullable=True)
    __tablename__="users"

class GroupsTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(300), nullable=False)
    rel = db.relationship('Groups', backref='GroupsTypes')

class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_type = db.Column(db.Integer, db.ForeignKey('groups_types.id'))
    nombre = db.Column(db.String(300), nullable=False)
    dependencia = db.Column(db.String(300), nullable=False)
    rel = db.relationship('SubGroups', backref='Groups')

class SubGroups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_group = db.Column(db.Integer, db.ForeignKey('groups.id'))
    nombre = db.Column(db.String(300), nullable=False)
    rel = db.relationship('Contactos', backref='SubGroups')

class Contactos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_subgroup = db.Column(db.Integer, db.ForeignKey('sub_groups.id'))
    nombre = db.Column(db.String(300), nullable=False)
    direccion = db.Column(db.String(500), nullable=False)
    telefono = db.Column(db.String(200), nullable=False)
    correo = db.Column(db.String(300), nullable=False)
    extension = db.Column(db.String(300), nullable=False)
    cargo = db.Column(db.String(300), nullable=False)
    departamento = db.Column(db.String(300), nullable=False)