from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import AccesoLogin, InsertarContactos,InsertarGroupType
from backend.models import Admin, Groups, GroupsTypes
from flask_login import login_required, login_user, logout_user
from vendors.database import db

correo_simple = Blueprint('correo_simple', __name__)

#GROUPS VIEW
from sqlalchemy import desc, asc
@correo_simple.route('/correo/groupsview/', methods=['GET', 'POST'])
@login_required
def view_correo():
    view_correo = db.session.query(Groups, GroupsTypes).select_from(Groups).join(GroupsTypes).all()
    return render_template('correo_simple/correo_simple.html', data=view_correo)