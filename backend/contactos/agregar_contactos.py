from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import AccesoLogin
from backend.models import Admin
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