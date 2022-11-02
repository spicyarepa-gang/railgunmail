from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import AccesoLogin, InsertarContactos
from backend.models import Admin, Contactos
from flask_login import login_required, login_user, logout_user
from vendors.database import db

email = Blueprint('email', __name__)


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

@email.route('/close')
@login_required
def close():
    logout_user()
    return redirect(url_for('email.iniciar_sesion'))

@email.route('/correos')
@login_required
def correos():
    return render_template('panel/admin.html')



@email.route('/contactos/agregar', methods=['GET','POST'])
@login_required
def add_contactos():
    add= InsertarContactos()
    if add.validate_on_submit(): #validamos datos
        n = add.n.data
        d= add.d.data
        t = add.t.data
        c = add.c.data
        e = add.e.data
        add_contactos = Contactos(nombre=n,direccion=d,telefono=t,correo=c,empresa=e)
        db.session.add(add_contactos)
        db.session.commit()
        return redirect(url_for('email.add_contactos'))
    return render_template('contactos/agregar_contactos.html',form=add)
