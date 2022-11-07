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
    ex = StringField('Inserta extension', validators=[DataRequired()])
    ca = StringField('Inserta cargo', validators=[DataRequired()])
    de = StringField('Inserta departamento', validators=[DataRequired()])
    submit = SubmitField('Insertar')

class InsertarGroupType(FlaskForm):
    nombre = StringField('Insertar el nombre del tipo de grupo', validators=[DataRequired()])
    submit = SubmitField('Insertar')


class InsertarGroup(FlaskForm):
    nombre = StringField('Insertar el nombre del tipo de grupo', validators=[DataRequired()])
    dependencia = StringField('Insertar el nombre del tipo de grupo', validators=[DataRequired()])
    submit = SubmitField('Insertar')