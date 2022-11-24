from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import AccesoLogin, InsertarContactos
from backend.models import Admin, Contactos, Groups
from flask_login import login_required, login_user, logout_user
from vendors.database import db

email = Blueprint('email', __name__)

#INICIAR SESION
@email.route('/', methods=['GET', 'POST'])
def iniciar_sesion():
    formulario_login = AccesoLogin()
    if formulario_login.validate_on_submit():
        admin = Admin.query.filter_by(usuario=formulario_login.user.data, clave=formulario_login.passw.data).first()
        if admin:
            login_user(admin)
            return redirect(url_for('email.correos'))
        return redirect(url_for('email.iniciar_sesion'))
    return render_template('login/login.html', data=formulario_login)

#CERRAR SESION
@email.route('/close')
@login_required
def close():
    logout_user()
    return redirect(url_for('email.iniciar_sesion'))

@email.route('/correos')
@login_required
def correos():
    return render_template('panel/admin.html')

#CONTACTOS ADD
@email.route('/contactos/agregar', methods=['GET','POST'])
@login_required
def add_contactos():
    available_groups = Groups.query.all()
    add= InsertarContactos ()
    add.grupo.choices = [(i.id, i.nombre) for i in available_groups]
    
    if add.validate_on_submit(): #validamos datos
        nombre = add.nombre.data
        direccion = add.direccion.data
        telefono = add.telefono.data
        correo = add.correo.data
        extension = add.extension.data
        cargo = add.cargo.data
        departamento = add.departamento.data
        id_group = add.grupo.data
        add_contactos = Contactos(nombre=nombre,direccion=direccion,telefono=telefono,correo=correo,extension=extension,cargo=cargo,departamento=departamento,id_group=id_group)
        db.session.add(add_contactos)
        db.session.commit()
        return redirect(url_for('email.view_contactos', num_page=1))
    return render_template('contactos/agregar_contactos.html',form=add)

#CONTACTOS VIEW
from sqlalchemy import desc, asc
@email.route('/contactos/view/<int:num_page>', methods=['GET', 'POST'])
@login_required
def view_contactos(num_page):
    view_contactos = db.session.query(Contactos, Groups).select_from(Contactos).join(Groups).paginate(per_page=5, page=num_page, error_out=False)
    return render_template('contactos/view_contactos.html', data=view_contactos, num_page=1)

#UPDATE CONTACTOS
@email.route('/contactos/view/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_contactos(id):
    data = Contactos.query.get(id)
    if request.method == 'POST':
        data.nombre = request.form['nombre']
        data.direccion = request.form['direccion']
        data.telefono = request.form['telefono']
        data.correo = request.form['correo']
        data.extension = request.form['extension']
        data.cargo = request.form['cargo']
        data.departamento = request.form['departamento']
        db.session.commit()
        return redirect(url_for('email.view_contactos',num_page=1))
    return render_template('contactos/update_contactos.html', data=data)

#DELETE CONTACTOS
@email.route('/contactos/view/delete/<int:id>')
@login_required
def delete_contactos(id):
    data = Contactos.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('email.view_contactos',num_page=1))