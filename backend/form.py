from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AccesoLogin(FlaskForm):
    user = StringField('Inserta tu usuario', validators=[DataRequired()])
    passw = PasswordField('Inserta tu contraseña', validators=[DataRequired()])
    entrar = SubmitField('Entrar')

class InsertarContactos(FlaskForm):
    nombre = StringField('Inserta nombre', validators=[DataRequired()]) 
    direccion = StringField('Inserta direccion', validators=[DataRequired()])
    telefono = StringField('Inserta telefono', validators=[DataRequired()])
    correo = StringField('Inserta correo', validators=[DataRequired()])
    extension = StringField('Inserta extension', validators=[DataRequired()])
    cargo = StringField('Inserta cargo', validators=[DataRequired()])
    departamento = StringField('Inserta departamento', validators=[DataRequired()])
    submit = SubmitField('Insertar')

class InsertarGroupType(FlaskForm):
    nombre = StringField('Insertar el nombre del tipo de grupo', validators=[DataRequired()])
    submit = SubmitField('Insertar')

class InsertarGroup(FlaskForm):
    nombre = StringField('Nombre del grupo', validators=[DataRequired()])
    tipo = SelectField('Tipo de grupo', choices=[], validators=[DataRequired()])
    dependencia = StringField('Dependencia', validators=[DataRequired()])
    submit = SubmitField('Insertar')