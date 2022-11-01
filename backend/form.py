from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AccesoLogin(FlaskForm):
    user = StringField('Inserta tu usuario', validators=[DataRequired()])
    passw = PasswordField('Inserta tu contraseña', validators=[DataRequired()])
    entrar = SubmitField('Entrar')