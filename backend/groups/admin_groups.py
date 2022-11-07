from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import AccesoLogin, InsertarGroup
from backend.models import Admin, Groups, GroupsTypes
from flask_login import login_required, login_user, logout_user
from vendors.database import db

groups = Blueprint('groups', __name__)

#GROUPS ADD
@groups.route('/groups/agregar', methods=['GET','POST'])
@login_required
def add_groups():
    available_types = GroupsTypes.query.all()
    group_types = [(i.id, i.nombre) for i in available_types]
    add= InsertarGroup ()
    add.id.choices = group_types
    if add.validate_on_submit(): #validamos datos   
        nombre = add.nombre.data
        tipo = add.tipo.data(add.nombre.data,add.id.data)
        dependencia = add.dependencia.data
        add_groups = Groups(nombre=nombre,dependencia=dependencia,tipo=tipo)
        db.session.add(add_groups)
        db.session.commit()
        return redirect(url_for('groups.add_groups'))
    return render_template('groups/agregar_groups.html',form=add)

#GROUPS VIEW
from sqlalchemy import desc, asc
@groups.route('/groups/view', methods=['GET', 'POST'])
@login_required
def view_groups():
    view_groups = Groups.query.order_by(desc('id'))
    return render_template('groups/view_groups.html', data=view_groups)

