from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import AccesoLogin, InsertarContactos,InsertarGroupType
from backend.models import Admin, Groups, GroupsTypes
from flask_login import login_required, login_user, logout_user
from vendors.database import db

groupstypes = Blueprint('groupstypes', __name__)

#GROUPSTYPES ADD
@groupstypes.route('/groupstypes/agregar', methods=['GET','POST'])
@login_required
def add_groups_types():
    add= InsertarGroupType()
    if add.validate_on_submit(): #validamos datos
        nombre = add.nombre.data
        add_groups_types = GroupsTypes(nombre=nombre)
        db.session.add(add_groups_types)
        db.session.commit()
        return redirect(url_for('groupstypes.view_groups_types'))  
    return render_template('groups/agregar_groups_types.html',form=add)
    

#UPDATE TIPOS DE GRUPOS
@groupstypes.route('/groupstypes/view/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_groupstypes(id):
    data = GroupsTypes.query.get(id)
    if request.method == 'POST':
        data.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('groupstypes.view_groups_types'))
    return render_template('groups/update_groups_types.html', data=data)





#GROUPSTYPES VIEW
from sqlalchemy import desc, asc
@groupstypes.route('/groupsTypes/view', methods=['GET', 'POST'])
@login_required
def view_groups_types():
    view_groups_types = GroupsTypes.query.order_by(desc('id'))
    return render_template('groups/view_groups_types.html', data=view_groups_types)