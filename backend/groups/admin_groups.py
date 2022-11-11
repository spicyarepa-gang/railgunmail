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
    add= InsertarGroup ()
    add.tipo.choices = [(i.id, i.nombre) for i in available_types]
    if add.validate_on_submit(): #validamos datos   
        nombre = add.nombre.data
        tipo = add.tipo.data
        dependencia = add.dependencia.data
        add_groups = Groups(id_type=tipo,nombre=nombre,dependencia=dependencia)
        db.session.add(add_groups)
        db.session.commit()
        return redirect(url_for('groups.add_groups'))
    return render_template('groups/agregar_groups.html',form=add)

#GROUPS VIEW
from sqlalchemy import desc, asc
@groups.route('/groups/view', methods=['GET', 'POST'])
@login_required
def view_groups():
    view_groups = db.session.query(Groups, GroupsTypes).select_from(Groups).join(GroupsTypes).all()
    return render_template('groups/view_groups.html', data=view_groups)

#UPDATE GRUPOS
@groups.route('/groups/view/update/<string:id>', methods=['GET', 'POST'])
@login_required
def update_groups(id):
    get_data = GroupsTypes.query.all()
    data = Groups.query.get(id)
    if request.method == 'POST':
        data.nombre = request.form['nombre']
        data.id_type = request.form['tipo']
        data.dependencia = request.form['dependencia']
        db.session.commit()
        return redirect(url_for('groups.view_groups'))
    return render_template('groups/update_groups.html', groupstype_list=get_data,data=data)














