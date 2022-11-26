from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import EnviarCorreo
from backend.models import Admin, Groups, GroupsTypes, Contactos
from flask_login import login_required, login_user, logout_user
from vendors.database import db, mail
from flask_mail import Mail, Message
from threading import Thread

correo = Blueprint('correo', __name__)

@correo.route('/groups/view/enviar_a/<int:id>', methods=['GET', 'POST'])
@login_required
def enviar_correo(id): 
    add = EnviarCorreo()
    view_contactos = Contactos.query.filter(Contactos.id_group == id)
    view_admin = Admin.query.all()
    if add.validate_on_submit(): #validamos datos
        title = add.title.data
        body = add.body.data
        #Error aqui_q
        correo_admin = view_admin.email[0]
        nombre_admin = view_admin.nombre[0]
        def send_email_thread(title, body):
            with correo.app_context():
                mail.send(title, body, correo_admin, nombre_admin)

        with correo.app_context():
            all_emails = [c for c in view_contactos]
            for email in all_emails:        
                message = body
                subject = title
                msg = Message(recipients=[email],sender = nombre_admin+" "+"<"+correo_admin+">" ,\
                                body=message,subject=subject)
                thr = Thread(target=send_email_thread, args=[msg])
                thr.start()

        return redirect(url_for('groups.view_groups',num_page=1))
    return render_template('correo/enviar_correo.html', data=view_contactos, form=add)

