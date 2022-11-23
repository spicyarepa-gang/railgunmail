from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import AccesoLogin, InsertarContactos,InsertarGroupType
from backend.models import Admin, Groups, GroupsTypes, Contactos
from flask_login import login_required, login_user, logout_user
from vendors.database import db

correo = Blueprint('correo', __name__)

@correo.route('/groups/view/enviar_a/<int:id>')
@login_required
def enviar_correo(id):
    view_contactos = Contactos.query.filter(Contactos.id_group == id)
    return render_template('correo/enviar_correo.html', data=view_contactos)
