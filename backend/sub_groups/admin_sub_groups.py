from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import AccesoLogin, InsertarSubGroups
from backend.models import Admin, Groups, SubGroups
from flask_login import login_required, login_user, logout_user
from vendors.database import db

subgroups = Blueprint('subgroups', __name__)


#SUBGROUPS VIEW
from sqlalchemy import desc, asc
@subgroups.route('/subgroups/view', methods=['GET', 'POST'])
@login_required
def view_subgroups():
    view_sub_groups = db.session.query(SubGroups, Groups).select_from(SubGroups).join(Groups).all()
    return render_template('sub_groups/view_subgroups.html', data=view_sub_groups)

#SUBGROUPS VIEW
from sqlalchemy import desc, asc
@subgroups.route('/subgroups/add', methods=['GET', 'POST'])
@login_required
def add_subgroups():
    available_groups = Groups.query.all()
    add= InsertarSubGroups ()
    add.grupo.choices = [(i.id, i.nombre) for i in available_groups]

    if add.validate_on_submit(): #validamos datos   
        grupo = add.grupo.data
        nombre = add.nombre.data
        add_subgroups = SubGroups(id_group=grupo, nombre=nombre)
        db.session.add(add_subgroups)
        db.session.commit()
        return redirect(url_for('subgroups.add_subgroups'))
    return render_template('sub_groups/agregar_subgrupos.html',form=add)

@subgroups.route('/subgroups/update/<string:id>', methods=['GET','POST'])
@login_required
def update_subgroups(id):
    get_data = Groups.query.all()
    data = SubGroups.query.get(id)
    if request.method == 'POST':
        data.id_group = request.form['groups']
        data.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('subgroups.view_subgroups'))
    return render_template('sub_groups/update_subgroups.html',groups_list=get_data,data=data)


@subgroups.route('/subgroups/view/delete/<int:id>')
@login_required
def delete_subgroups(id):
    data = SubGroups.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('subgroups.view_subgroups'))
