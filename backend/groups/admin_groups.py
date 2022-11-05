from flask import Blueprint, render_template, redirect, url_for, request
from backend.form import AccesoLogin, InsertarContactos
from backend.models import Admin, Groups, GroupsTypes
from flask_login import login_required, login_user, logout_user
from vendors.database import db

groups = Blueprint('groups', __name__)

#GROUPSTYPES VIEW
from sqlalchemy import desc, asc
@groups.route('/groupsTypes/view', methods=['GET', 'POST'])
@login_required
def view_groups_types():
    view_groups_types = GroupsTypes.query.order_by(desc('id'))
    return render_template('groups/view_groups_types.html', data=view_groups_types)

#GROUPS VIEW
from sqlalchemy import desc, asc
@groups.route('/groups/view', methods=['GET', 'POST'])
@login_required
def view_groups():
    view_groups = Groups.query.order_by(desc('id'))
    return render_template('groups/view_groups.html', data=view_groups)