from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import AccesoLogin
from backend.models import Admin, Contactos
from flask_login import login_required, login_user, logout_user
from vendors.database import db

email = Blueprint('email', __name__)

from sqlalchemy import desc, asc
@email.route('/view/contactos', methods=['GET', 'POST'])
@login_required
def view_contactos():
    view_contactos = Contactos.query.order_by(desc('id'))
    return render_template('contactos/view_contactos.html', datos=view_contactos)
  
