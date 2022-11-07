from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from vendors.database import db
from vendors.config import DevConfig
from datetime import timedelta


app = Flask(__name__)
app.permanent_session_lifetime = timedelta(hours=24)
app.config.from_object(DevConfig)
db.init_app(app)


from backend.contactos.admin_contactos import email
from backend.groups.admin_groups import groups
from backend.groups.admin_groupstypes import groupstypes
app.register_blueprint(email)
app.register_blueprint(groups)
app.register_blueprint(groupstypes)


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





