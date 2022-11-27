from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from vendors.database import db, mail
from vendors.config import DevConfig
from datetime import timedelta
from backend.contactos.admin_contactos import email
from backend.groups.admin_groups import groups
from backend.group_types.admin_groupstypes import groupstypes
from backend.correo.correo import correo
from flask_wtf.csrf import CSRFProtect
from flask_ckeditor import CKEditor
from flask_mail import Mail, Message
from threading import Thread
from backend.form import EnviarCorreo
from backend.models import Admin, Groups, GroupsTypes, Contactos
from flask_login import login_required, login_user, logout_user

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(hours=24)
app.config.from_object(DevConfig)
db.init_app(app)

#mail
mail.init_app(app)

#ckeditor
ckeditor = CKEditor()
ckeditor.init_app(app)

secure = CSRFProtect()
secure.init_app(app)

app.register_blueprint(email)
app.register_blueprint(groups)
app.register_blueprint(groupstypes)
#app.register_blueprint(correo)

from flask_login import LoginManager
login = LoginManager()
login.init_app(app)
login.login_view = 'email.iniciar_sesion'

@app.teardown_appcontext
def shutdown_database_conection(exception=None):
    db.session.remove()

from backend.models import Admin
@login.user_loader
def load_admin_or_user(id):
    admin = Admin.query.get(int(id))
    if admin:
        return admin

with app.app_context():
    db.create_all()

import smtplib, ssl, csv
from email.message import EmailMessage

@app.route('/groups/view/enviar_a/<int:id>', methods=['GET', 'POST'])
@login_required
def enviar_correo(id): 
    add = EnviarCorreo()
    view_contactos = db.session.query(Contactos.correo).filter(Contactos.id_group == id)
    emails = [c for c in view_contactos]
    if add.validate_on_submit(): #validamos datos
        subject = add.title.data
        body_message = add.body.data
        #conexion al server
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL('smtp.gmail.com', DevConfig.MAIL_PORT, context=context)
        server.login(DevConfig.MAIL_USERNAME, DevConfig.MAIL_PASSWORD)
        #envio del correo
        for row in emails:
            em = EmailMessage()
            em['From'] = DevConfig.MAIL_USERNAME
            em['To'] = row
            em['Subject'] = subject
            em.set_content(body_message, subtype="html")
            server.send_message(em)

        server.close()
        print('done')

        return redirect(url_for('groups.view_groups',num_page=1))
    return render_template('correo/enviar_correo.html', data=view_contactos, form=add)