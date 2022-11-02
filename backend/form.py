from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AccesoLogin(FlaskForm):
    user = StringField('Inserta tu usuario', validators=[DataRequired()])
    passw = PasswordField('Inserta tu contraseña', validators=[DataRequired()])
    entrar = SubmitField('Entrar')


class InsertarContactos(FlaskForm):
    n = StringField('Inserta nombre', validators=[DataRequired()]) 
    d = StringField('Inserta direccion', validators=[DataRequired()])
    t = StringField('Inserta telefono', validators=[DataRequired()])
    c = StringField('Inserta correo', validators=[DataRequired()])
    e = StringField('Inserta empresa', validators=[DataRequired()])
    submit = SubmitField('Insertar')
