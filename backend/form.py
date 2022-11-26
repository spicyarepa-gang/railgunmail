from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class AccesoLogin(FlaskForm):
    user = StringField('Usuario:', render_kw={"placeholder": "Nombre de usuario"}, validators=[DataRequired()])
    passw = PasswordField('Contraseña:', render_kw={"placeholder": "Contraseña"}, validators=[DataRequired()])
    entrar = SubmitField('Entrar')

class InsertarContactos(FlaskForm):
    nombre = StringField('Nombre del contacto:', render_kw={"placeholder": "Nombre del contacto"}, validators=[DataRequired()]) 
    direccion = TextAreaField('Dirección del contacto:', render_kw={"placeholder": "Dirección del contacto"}, validators=[DataRequired()])
    telefono = StringField('Teléfono del contacto:', render_kw={"placeholder": "Teléfono del contacto"}, validators=[DataRequired()])
    correo = StringField('Correo electrónico:', render_kw={"placeholder": "ej: ejemplo@correo.com"}, validators=[DataRequired()])
    extension = StringField('Extensión del contacto:', render_kw={"placeholder": "Extensión del contacto"}, validators=[DataRequired()])
    cargo = StringField('Cargo del contacto:', render_kw={"placeholder": "Cargo del contacto"}, validators=[DataRequired()])
    departamento = StringField('Departamento de procedencia:', render_kw={"placeholder": "Departamento de procedencia"}, validators=[DataRequired()])
    grupo = SelectField('Asignar grupo:', choices=[], validators=[DataRequired()])
    submit = SubmitField('Añadir contacto')

class InsertarGroupType(FlaskForm):
    nombre = StringField('Nombre del tipo de grupo', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class InsertarGroup(FlaskForm):
    nombre = StringField('Nombre del grupo:', validators=[DataRequired()])
    tipo = SelectField('Tipo de grupo:', choices=[], validators=[DataRequired()])
    dependencia = StringField('Dependencia:', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class EnviarCorreo(FlaskForm):
    title = StringField('Asunto:', validators=[DataRequired()], render_kw={"placeholder": "Escriba el asunto"})
    body = CKEditorField('Escriba el mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar')

# class InsertarSubGroups(FlaskForm):
#     grupo = SelectField('Grupo al que pertenece:', choices=[], validators=[DataRequired()])
#     nombre = StringField('Nombre del subgrupo:', validators=[DataRequired()]) 
#     submit = SubmitField('Ingresar')