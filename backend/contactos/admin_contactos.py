from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import AccesoLogin, InsertarContactos
from backend.models import Admin, Contactos
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
    add= InsertarContactos()
    if add.validate_on_submit(): #validamos datos
        n = add.n.data
        d = add.d.data
        t = add.t.data
        c = add.c.data
        e = add.e.data
        ca = add.ca.data
        de = add.de.data
        add_contactos = Contactos(nombre=n,direccion=d,telefono=t,correo=c,extencion=e,cargo=ca,departamento=de)
        db.session.add(add_contactos)
        db.session.commit()
        return redirect(url_for('email.add_contactos'))
    return render_template('contactos/agregar_contactos.html',form=add)

#CONTACTOS VIEW
from sqlalchemy import desc, asc
@email.route('/contactos/view', methods=['GET', 'POST'])
@login_required
def view_contactos():
    view_contactos = Contactos.query.order_by(desc('id'))
    return render_template('contactos/view_contactos.html', data=view_contactos)

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
        data.extencion = request.form['extencion']
        data.cargo = request.form['cargo']
        data.departamento = request.form['departamento']
        db.session.commit()
        return redirect(url_for('email.view_contactos'))
    return render_template('contactos/update_contactos.html', data=data)

#DELETE CONTACTOS
@email.route('/contactos/view/delete/<int:id>')
@login_required
def delete_contactos(id):
    data = Contactos.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('email.view_contactos'))